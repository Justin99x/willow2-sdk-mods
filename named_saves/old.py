from __future__ import annotations

import os
import re
import stat
from typing import TYPE_CHECKING

from legacy_compat import legacy_compat
from mods_base import BoolOption, build_mod, get_pc, hook
from mods_base.mod_factory import deregister_using_settings_file
from mods_base.options import HiddenOption
from ui_utils import show_hud_message
from unrealsdk.hooks import Block, Type, prevent_hooking_direct_calls
from unrealsdk.unreal import BoundFunction, WrappedArray

if TYPE_CHECKING:
    from bl2 import WillowGFxLobbyLoadCharacter, WillowPlayerController, WillowSaveGameManager

NAME = "Named Saves"
SPACE_REPLACE = "@~"

save_path_hidden_option = HiddenOption(identifier="save_path_hidden_option", value=None)
character_save_option = BoolOption(identifier="Save Files as Character Names", value=False,
                                   description="When off, .sav files of any format can be read and used. When on, save files are renamed to match Save#### - CharacterName.sav")


def extract_user_save_path() -> str:
    """Search the user's home directory for our path. This takes a few seconds and
     should only be used once, with result stored in a hidden option."""

    pc: WillowPlayerController = get_pc()
    save_path = pc.OnlineSub.ProfileDataDirectory

    # Get just the save folder number
    norm_path = save_path.replace("\\", "/")
    pattern = r"\d{12,}"
    match = re.search(pattern, norm_path)
    if not match:
        raise ValueError(f"{pattern} pattern not found in save game path")
    save_dir_id = match.group(0)

    # Find 'My games' folders in the user space and check if the full path from that root exists.
    for root, dirs, _ in os.walk(os.path.expanduser('~')):
        for dir_name in dirs:
            if dir_name.lower() == 'my games':
                save_dir = os.path.join(root, dir_name, 'Borderlands 2', 'WillowGame', 'SaveData', save_dir_id)
                if os.path.exists(save_dir):
                    return os.path.normpath(save_dir).replace('\\', '/')

    raise ValueError(f"Could not find save folder for id {save_dir_id}")


def _on_enable():
    if not save_path_hidden_option.value:
        save_path_hidden_option.value = extract_user_save_path()


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
    saves = [os.path.join(gbx_save_root, file) for file in os.listdir(save_path) if file[-4:] == '.sav']
    for save in saves:
        new_ret.append(save)

    return Block, new_ret


@hook("WillowGame.WillowGFxLobbyLoadCharacter:StripSavePath")
def strip_save_name(obj: WillowGFxLobbyLoadCharacter,
                    args: WillowGFxLobbyLoadCharacter.StripSavePath.args,
                    ret: WillowGFxLobbyLoadCharacter.StripSavePath.ret,
                    func: BoundFunction):
    """Game looks for 'Save' from the right and grabs everything after. We need to intercept to just grab the full filename.
    This is where we're also going to replace spaces with special characters to prevent problems with a later arg parse that looks for spaces."""
    return Block, os.path.split(args.Path)[-1].replace(" ", SPACE_REPLACE)


@hook("WillowGame.WillowPlayerController:FixUpLoadString")
def fixup_load_string(obj: WillowPlayerController,
                      args: WillowPlayerController.FixUpLoadString.args,
                      ret: WillowPlayerController.FixUpLoadString.ret,
                      func: BoundFunction):
    """Here the game tries to pad the save name to match Save#### format. We just need to block it and return the intput. We're
    also going to set our own var to be used for saving later.
    NOTE: Relies on this function only being called to create an arg to LoadGame. Something to keep an eye on.
    """
    return Block, args.InLoadString.replace(SPACE_REPLACE, " ")

#TODO: When continuing with old save after a new save is created, LastLoadedFilePath doesn't get updated.

# @hook("WillowGame.WillowPlayerController:BuildSaveGameNameFromId")
def build_save_game_name(obj: WillowPlayerController,
                         args: WillowPlayerController.BuildSaveGameNameFromId.args,
                         ret: WillowPlayerController.BuildSaveGameNameFromId.ret,
                         func: BoundFunction):
    """When applying save game, this gets called to set pc.SaveGameName. We need to set our own instead."""
    save_game_manager = obj.GetWillowGlobals().GetWillowSaveGameManager()
    # print(f"Last loaded file path: {save_game_manager.LastLoadedFilePath}")
    # file_id and next_file_id generated from our own replacement function since this gets hooked.
    in_file_id = save_game_manager.GetHighestSaveIdFromFileList(0, [save_game_manager.LastLoadedFilePath])
    next_file_id = save_game_manager.GetHighestSaveIdFromFileList(0, list(save_game_manager.GetSaveGameList(0, -1, ''))) + 1
    file_id = next_file_id if in_file_id == 0 else in_file_id

    if character_save_option.value:
        file_name = obj.GetSaveGameNameFromid(file_id).replace(".sav", f" - {obj.PlayerPreferredCharacterName}.sav")
        if file_name != save_game_manager.LastLoadedFilePath and file_id == in_file_id:
            file_id = next_file_id
            file_name = obj.GetSaveGameNameFromid(file_id).replace(".sav", f" - {obj.PlayerPreferredCharacterName}.sav")
            old_file_path = os.path.join(save_path_hidden_option.value, save_game_manager.LastLoadedFilePath)
            if os.path.exists(old_file_path) and os.path.isfile(old_file_path):
                try:
                    os.remove(old_file_path)
                except PermissionError:
                    print("Could not delete old save because it is read only.")
    else:
        # Keep same save file if option turned off.
        file_name = obj.GetWillowGlobals().GetWillowSaveGameManager().LastLoadedFilePath

    obj.SaveGameName = file_name
    obj.SaveGameFileId = file_id
    return Block
"""
Load character
1. Load game triggered with a PlayerSaveGame
2. BeginLoadGame, uses result of FixUpLoadString for file name. native function on save manager.
3. FinishSaveGameLoad
    - Set SaveGameFileId
SaveGameFileId not set during load, not available on main menu. LastLoadedFilePath is.

On load into game
1. Apply all save game stuff
2. Apply PlayerUI (char name)
3. Apply Save Game data (file id, file name)

On save
1. Filename from local, but can be overridden
2. Generate SaveGame
3. Save manager save game
"""
@hook("WillowGame.WillowPlayerController:OnLoadSaveGame")
def on_load_save_game(obj: WillowPlayerController,
                         args: WillowPlayerController.OnLoadSaveGame.args,
                         ret: WillowPlayerController.OnLoadSaveGame.ret,
                         func: BoundFunction):
    print('on_load_save_game')

# @hook("WillowGame.WillowPlayerController.ApplyPlayerSaveGameData")
# def apply_player_save_game_data(obj: WillowPlayerController,
#                          args: WillowPlayerController.ApplyPlayerSaveGameData.args,
#                          ret: WillowPlayerController.ApplyPlayerSaveGameData.ret,
#                          func: BoundFunction):
#     char_name = args.SaveGame.PlayerUIPreferences.CharacterName
#     in_save_game_id = args.SaveGame.SaveGameId
#     with prevent_hooking_direct_calls():
#         func(args.SaveGame)




@hook("WillowGame.WillowSaveGameManager:GetHighestSaveIdFromFileList")
def get_highest_save_id(obj: WillowSaveGameManager,
                        args: WillowSaveGameManager.GetHighestSaveIdFromFileList.args,
                        ret: WillowSaveGameManager.GetHighestSaveIdFromFileList.ret,
                        func: BoundFunction):
    for i, file in enumerate(args.RawList):
        match = re.search(r"(Save[0-9A-Fa-f]{4}).*\.sav$", file)
        args.RawList[i] = match.group(1) if match else file

    with prevent_hooking_direct_calls():
        return Block, func(args.ControllerId, args.RawList)
    # print(f"highest: {args.RawList}")



# @hook("WillowGame.WillowPlayerController:SaveGame")
def wpc_save_game(obj: WillowPlayerController,
                  args: WillowPlayerController.SaveGame.args,
                  ret: WillowPlayerController.SaveGame.ret,
                  func: BoundFunction):
    """When we save, need to call our build save game hooked function to set the wpc fields that we need."""
    if not character_save_option.value:
        return

    obj.BuildSaveGameNameFromId(0) # Arg doesn't matter because we hook this function and don't use it.

    with prevent_hooking_direct_calls():
        func('')
    return Block
#
# @hook("WillowGame.WillowPlayerController:SaveGame", Type.POST_UNCONDITIONAL)
# def wpc_save_game_post(obj: WillowPlayerController,
#                   args: WillowPlayerController.SaveGame.args,
#                   ret: WillowPlayerController.SaveGame.ret,
#                   func: BoundFunction):
#





# file_id = next_file_id
# file_name = obj.GetSaveGameNameFromid(file_id).replace(".sav", f" - {obj.PlayerPreferredCharacterName}.sav")


deregister_using_settings_file('named_saves')

mod = build_mod(
    options=[save_path_hidden_option, character_save_option],
    on_enable=_on_enable
)
