import json
from typing import Any, Mapping, Sequence

import save_options
from mods_base import get_ordered_mod_list, get_pc, hook
from save_options.options import can_save
from save_options.registration import ModSaveOptions, registered_save_options, save_callbacks
from save_options.reloader import register_module
from unrealsdk import make_struct
from unrealsdk.hooks import Block, Type, prevent_hooking_direct_calls
from unrealsdk.unreal import BoundFunction, UObject, WrappedStruct

type JSON = Mapping[str, JSON] | Sequence[JSON] | str | int | float | bool | None

_PACKAGE_ID: int = 100


def _extract_save_data(player_save_game: UObject) -> dict[str, dict[str, JSON]]:
    """Grab the json string from UnloadableDlcLockoutList based on the package id, then load to Python object.
    Returns empty dict if no data found."""

    matching_lockout_items = [lockout_data for lockout_data in player_save_game.UnloadableDlcLockoutList if
                              lockout_data.DlcPackageId == _PACKAGE_ID]
    # If somehow there are two entries we're just going to return empty since that's essentially corrupted.
    if not len(matching_lockout_items) == 1:
        return {}
    if matching_lockout_items[0].LockoutDefName:
        extracted_save_data = json.loads(matching_lockout_items[0].LockoutDefName)
        if not type(extracted_save_data) == dict:
            raise TypeError("Could not load dict object from custom save string.")
        return extracted_save_data
    return {}


@hook("WillowGame.WillowSaveGameManager:SaveGame", immediately_enable=True)
def save_game(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    """
    We're going to inject our arbitrary save data here. This is the last time the save game can be edited before writing
    to disk. Extremely large string sizes can crash the game, so we may want to add a safety check at some point.
    1M characters has worked fine, so unlikely to be an issue.
    """
    # For callbacks, only process enabled mods. We'll run these first in case mod uses it to set save data
    enabled_mods = [mod.settings_file.stem for mod in get_ordered_mod_list()]
    callbacks_to_process = {mod: callback for mod, callback in save_callbacks.items() if mod in enabled_mods}

    for mod_name, callback in callbacks_to_process.items():
        callback()

    # For saving, we'll overwrite existing mod data for enabled mods. Any disabled/uninstalled mods will have their data left alone.
    json_save_data = _extract_save_data(args.SaveGame)
    for mod_name, mod_data in registered_save_options.items():
        if mod_name in enabled_mods:
            json_save_data[mod_name] = {identifier: save_option.value for identifier, save_option in mod_data.items()}

    str_save_data = json.dumps(json_save_data)
    custom_lockout = make_struct("UnloadableDlcLockoutData", LockoutDefName=str_save_data, DlcPackageId=_PACKAGE_ID)
    args.SaveGame.UnloadableDlcLockoutList = [custom_lockout]

    with prevent_hooking_direct_calls():
        func(args.ControllerId, args.SaveGame, args.Filename, args.PS3UserNum)

    # Reset our var tracking whether any options have changed since last save.
    save_options.options.any_option_changed = False

    return Block


@hook("WillowGame.WillowSaveGameManager:EndLoadGame", Type.POST, immediately_enable=True)
def end_load_game(obj: UObject, args: WrappedStruct, ret: Any, func: BoundFunction) -> None:
    """
    We hook this to send data back to any registered mod save options. This gets called when loading
    character in main menu also.
    No callback here because the timing of when this is called doesn't make much sense to do anything with
    it. Devs can either use the on_change field of the SaveOption or write their own hooks to do
    something with the loaded data.
    """
    extracted_save_data = _extract_save_data(ret)

    if not extracted_save_data:
        return


    for mod_name, extracted_mod_data in extracted_save_data.items():
        mod_save_options: ModSaveOptions = registered_save_options[mod_name]
        for identifier, extracted_value in extracted_mod_data.items():
            if save_option := mod_save_options.get(identifier):
                save_option.value = extracted_value

    # Resetting change tracking var here too. Obviously a load sets a bunch of options, but we don't want
    # to count that as a real change that needs to be saved.
    save_options.options.any_option_changed = False



@hook("WillowGame.FrontendGFxMovie:HideOptionsMovie", immediately_enable=True)
def hide_options_movie(obj, args, ret, func) -> None:
    """When an options movie is closed, we check to see if any save option values have changed since the last
    time the file was saved. If it has, we save the game. This is necessary since values changed while
    in the main menu would get overwritten or just get lost if a new character were selected."""
    if not can_save() or not save_options.options.any_option_changed:
        return

    pc = get_pc()
    # When in game, just use standard machinery to save
    if pc.MyWillowPawn:
        pc.SaveGame()
        return

    # When not in game, we need to load from file to get full save game. Cached save game is partial.
    save_manager = pc.GetWillowGlobals().GetWillowSaveGameManager()
    setattr(save_manager, "__OnLoadComplete__Delegate", save_manager.OnLoadComplete)

    # Loading the save game is an async operation, we need to hook OnLoadComplete to have access to the result
    @hook("WillowGame.WillowSaveGameManager:OnLoadComplete", Type.POST, immediately_enable=True)
    def on_load_complete(*_: Any) -> None:
        on_load_complete.disable()
        setattr(save_manager, "__OnLoadComplete__Delegate", None)
        # Need to prevent our hook on EndLoadGame to avoid reloading previous save option values
        with prevent_hooking_direct_calls():
            player_save_game = save_manager.EndLoadGame(pc.GetMyControllerId(), make_struct("LoadInfo"), 0)[0]
        save_manager.SaveGame(pc.GetMyControllerId(), player_save_game, save_manager.LastLoadedFilePath, -1)

    save_manager.BeginLoadGame(pc.GetMyControllerId(), save_manager.LastLoadedFilePath, -1)


register_module(__name__)
