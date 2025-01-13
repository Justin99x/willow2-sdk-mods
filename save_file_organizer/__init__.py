from __future__ import annotations

import os
import re
from typing import Any, TYPE_CHECKING

from mods_base import BoolOption, ButtonOption, HiddenOption, build_mod, hook
from save_file_organizer.actions import SaveListProcessor, get_all_save_data
from save_file_organizer.utils import extract_user_save_path, get_pc
from save_file_organizer.reloader import register_module
from unrealsdk.hooks import Block, Type, prevent_hooking_direct_calls
from unrealsdk.unreal import BoundFunction, WrappedArray

if TYPE_CHECKING:
    from bl2 import FrontendGFxMovie, WillowGFxLobbyLoadCharacter, WillowPlayerController, \
        WillowSaveGameManager

NAME = "Named Saves"
SPACE_REPLACE = "@~"


@hook("WillowGame.WillowSaveGameManager:GetSaveGameList")
def get_save_game_list(obj: WillowSaveGameManager,
                       args: WillowSaveGameManager.GetSaveGameList.args,
                       ret: WillowPlayerController.GetSaveGameList.ret,
                       func: BoundFunction) -> None:
    """Hooking this to intercept the save files it finds and fill it with our own that grabs all .sav files"""

    # Bug in SDK prevents returning a list, so getting a WrappedArray here and adding to it instead.
    with prevent_hooking_direct_calls():
        new_ret: WrappedArray[str] = func(args.ControllerId, args.PS3UserNum, '')
    new_ret.clear()

    gbx_save_root: str = get_pc().OnlineSub.ProfileDataDirectory
    save_path = save_path_hidden_option.value
    saves = sorted(
        [file for file in os.listdir(save_path) if file.endswith('.sav')],
        key=lambda file: os.path.getmtime(os.path.join(save_path, file)),
        reverse=True  # Sorts from newest to oldest
    )
    for save in saves:
        new_ret.append(save)

    return Block, new_ret


def _strip_save_path(save_path: str):
    return os.path.split(save_path)[1].replace(" ", SPACE_REPLACE)


@hook("WillowGame.WillowGFxLobbyLoadCharacter:StripSavePath")
def strip_save_path(obj: WillowGFxLobbyLoadCharacter,
                    args: WillowGFxLobbyLoadCharacter.StripSavePath.args,
                    ret: WillowGFxLobbyLoadCharacter.StripSavePath.ret,
                    func: BoundFunction):
    """Game looks for 'Save' from the right and grabs everything after. We need to intercept to just grab the full filename.
    This is where we're also going to replace spaces with special characters to prevent problems with a later arg parse that looks for spaces."""
    return Block, _strip_save_path(args.Path)


@hook("WillowGame.WillowPlayerController:FixUpLoadString")
def fix_up_load_string(obj: WillowPlayerController,
                       args: WillowPlayerController.FixUpLoadString.args,
                       ret: WillowPlayerController.FixUpLoadString.ret,
                       func: BoundFunction):
    """Here the game tries to pad the save name to match Save#### format. We just need to block it and return the input, but
     with spaces restored.
    NOTE: Relies on this function only being called to create an arg to LoadGame. Something to keep an eye on.
    """
    return Block, args.InLoadString.replace(SPACE_REPLACE, " ")


@hook("WillowGame.WillowPlayerController:BuildSaveGameNameFromId")
def build_save_game_name(obj: WillowPlayerController,
                         args: WillowPlayerController.BuildSaveGameNameFromId.args,
                         ret: WillowPlayerController.BuildSaveGameNameFromId.ret,
                         func: BoundFunction):
    """When applying save game, this gets called to set pc.SaveGameName. We need to set our own instead."""
    obj.SaveGameName = obj.GetWillowGlobals().GetWillowSaveGameManager().LastLoadedFilePath
    obj.SaveGameFileId = args.SaveGameId
    return Block


@hook("WillowGame.WillowSaveGameManager:GetHighestSaveIdFromFileList")
def get_highest_save_id(obj: WillowSaveGameManager,
                        args: WillowSaveGameManager.GetHighestSaveIdFromFileList.args,
                        ret: WillowSaveGameManager.GetHighestSaveIdFromFileList.ret,
                        func: BoundFunction):
    """We need to do this for the game to recognize all our files when it's searching for next available."""
    for i, file in enumerate(args.RawList):
        match = re.search(r"(Save[0-9A-Fa-f]{4}).*\.sav$", file)
        args.RawList[i] = match.group(1) if match else file

    with prevent_hooking_direct_calls():
        return Block, func(args.ControllerId, args.RawList)


@hook("WillowGame.WillowPlayerController:SaveGame")
def wpc_save_game(obj: WillowPlayerController,
                  args: WillowPlayerController.SaveGame.args,
                  ret: WillowPlayerController.SaveGame.ret,
                  func: BoundFunction):
    """Mostly to not break saves generated programmatically (speedrun_practice). Preventing
    the game thinking multiple saves active because they share the same id"""
    if not args.Filename:
        return

    save_game_manager = obj.GetWillowGlobals().GetWillowSaveGameManager()
    file_id = save_game_manager.GetHighestSaveIdFromFileList(obj.GetMyControllerId(), [args.Filename])
    obj.BuildSaveGameNameFromId(file_id)


@hook("WillowGame.WillowPlayerController:SaveGame", Type.POST)
def wpc_save_game_post(*_: Any) -> None:
    """Need to do a post hook to update the save manager save list"""
    get_all_save_data(lambda x: None)


@hook("WillowGame.FrontendGFxMovie:NotifyAtMainMenu")
def notify_at_main_menu(obj: FrontendGFxMovie,
                        args: FrontendGFxMovie.NotifyAtMainMenu.args,
                        ret: FrontendGFxMovie.NotifyAtMainMenu.ret,
                        func):
    """This is for our auto save option. Any time we enter main menu we run this."""
    if obj.MyFrontendDefinition.Name == "Frontend_DEF" and auto_update_saves_option.value:
        SaveListProcessor.process_all_saves()


@hook("WillowGame.WillowPlayerController:LoadGame", Type.PRE)
def load_game(obj: WillowPlayerController,
              args: WillowPlayerController.LoadGame.args,
              ret: WillowPlayerController.LoadGame.ret,
              func: BoundFunction):
    """This is just here to be able to load a character on game launch. Converting the filename to our filename based on id
    when no initial file match is found."""

    save_manager: WillowSaveGameManager = obj.GetWillowGlobals().GetWillowSaveGameManager()
    attempted_file = obj.FixUpLoadString(obj.GetNextString(args.args)[0])
    attempted_id = save_manager.GetHighestSaveIdFromFileList(obj.GetMyControllerId(), [attempted_file])
    new_file_name = None
    for save in save_manager.SaveDataLoadedFromList:
        if _strip_save_path(save.FilePath) == attempted_file:
            return  # No need to do anything, found matching file
        if save.SaveGameFileId == attempted_id:
            new_file_name = _strip_save_path(save.FilePath)
    if not new_file_name:
        return  # Couldn't find a match in our list, so we just let it execute as normal

    with prevent_hooking_direct_calls():
        return Block, obj.LoadGame(new_file_name, args.SaveGame, args.bUpdatePRI, args.bLoadPlayer, args.LoadPlayerBehavior)[0]


save_path_hidden_option = HiddenOption(identifier="save_path_hidden_option", value='')
auto_update_saves_option = BoolOption(identifier="Auto Rename Saves",
                                      value=False)
update_saves_button = ButtonOption(identifier="Rename All Saves",
                                   description="Updates all saves to Save#### - CharacterName.sav format",
                                   on_press=SaveListProcessor.process_all_saves)
restore_saves_button = ButtonOption(identifier="Restore All Save Names",
                                    description="Restores all saves to Save####.sav format",
                                    on_press=SaveListProcessor.process_all_saves)
defrag_saves_button = ButtonOption(identifier="Defrag All Saves [Advanced]",
                                   description="Same as update saves, but also orders saves sequentially from 0",
                                   on_press=SaveListProcessor.process_all_saves)


def _on_enable():
    get_all_save_data(lambda x: None)  # Just need save manager to have this handy.


mod = build_mod(
    deregister_same_settings=True,
    options=[save_path_hidden_option, auto_update_saves_option, update_saves_button, restore_saves_button, defrag_saves_button],
    on_enable=_on_enable
)

if not save_path_hidden_option.value:
    print('Attempting to find game saves folder...')
    save_path = extract_user_save_path()
    save_path_hidden_option.value = save_path
    print(f'Successfully found game saves folder at {save_path}')

register_module(__name__)
