from __future__ import annotations

import copy
import inspect
import os
from typing import Any, TYPE_CHECKING

from mods_base import BoolOption, ButtonOption, HiddenOption, build_mod, hook
from save_file_organizer.actions import SaveListProcessor, get_all_save_data
from save_file_organizer.utils import extract_user_save_path, get_pc
from save_file_organizer.reloader import register_module
from unrealsdk.hooks import Block, Type, log_all_calls, prevent_hooking_direct_calls
from unrealsdk.unreal import BoundFunction

if TYPE_CHECKING:
    from common import FrontendGFxMovie, WillowGFxDialogBox, WillowGFxLobbyLoadCharacter, WillowGFxMenuHelperSaveGame, \
        WillowPlayerController, \
        WillowSaveGameManager

NAME = "Named Saves"
SPACE_REPLACE = "@~"

# TODO: Think we got the new game thing sorted out. Before releasing should probably should go through and make sure
# we really need everything currently being done like setting cached save games and last loaded file paths. Game might
# take care of it for us.



@hook("WillowGame.WillowSaveGameManager:GetSaveGameList")
def get_save_game_list(obj: WillowSaveGameManager,
                       args: WillowSaveGameManager.GetSaveGameList.args,
                       ret: WillowSaveGameManager.GetSaveGameList.ret,
                       func: BoundFunction) -> None:
    print(inspect.currentframe().f_code.co_name)
    print(args)
    """Hooking this to intercept the save files it finds and fill it with our own that grabs all .sav files"""
    save_path = save_path_hidden_option.value
    saves = [file for file in os.listdir(save_path) if file.endswith('.sav')]

    return Block, saves


@hook("WillowGame.WillowGFxMenuHelperSaveGame:SortResults", Type.POST)
def gfx_menu_helper_save_game_sort_results(obj: WillowGFxMenuHelperSaveGame,
                                           args: WillowGFxMenuHelperSaveGame.SortResults.args,
                                           ret: WillowGFxMenuHelperSaveGame.SortResults.ret,
                                           func: BoundFunction) -> None:
    print(inspect.currentframe().f_code.co_name)
    print(args)
    """Reorder the save game list after the fact. How the game actually does this is hidden
    in native code, and not doing this results in odd and seemingly inconsistent behavior (i.e.
    entering the character list twice in a row produces different results)

    We're also setting the SaveGameFileId here to keep the game from thinking that two
    files are active at the same time.
    """
    # Sort save games by last save date
    obj.SaveGames = copy.deepcopy(sorted(obj.SaveGames,
                                         key=lambda x: x.LastSaveDate,
                                         reverse=True))

    # Fixup save_ids to help with which save is active.
    save_manager = get_pc().GetWillowGlobals().GetWillowSaveGameManager()
    seen_ids: list[int] = []
    try:
        cached_id = save_manager.GetCachedPlayerSaveGame(get_pc().GetMyControllerId()).SaveGameId
    except AttributeError:
        cached_id = -1

    # Don't want to do any assigning when cached_id is -1, no files are active, don't want
    # to match any of them to the current Id.
    if cached_id < 0:
        return

    for save_game in obj.SaveGames:

        if save_game.FilePath == save_manager.LastLoadedFilePath:
            save_game.SaveGameFileId = cached_id
            seen_ids.append(cached_id)
        else:
            new_file_id = save_game.SaveGameFileId
            if new_file_id == cached_id:
                new_file_id = cached_id + 1

            while new_file_id in seen_ids:
                new_file_id += 1
            save_game.SaveGameFileId = new_file_id
            seen_ids.append(new_file_id)


def _strip_save_path(save_path: str):
    return os.path.split(save_path)[1].replace(" ", SPACE_REPLACE)


@hook("WillowGame.WillowGFxLobbyLoadCharacter:StripSavePath")
def strip_save_path(obj: WillowGFxLobbyLoadCharacter,
                    args: WillowGFxLobbyLoadCharacter.StripSavePath.args,
                    ret: WillowGFxLobbyLoadCharacter.StripSavePath.ret,
                    func: BoundFunction):
    print(inspect.currentframe().f_code.co_name)
    print(args)
    """Game looks for 'Save' from the right and grabs everything after. We need to intercept to just grab the full filename.
    This is where we're also going to replace spaces with special characters to prevent problems with a later arg parse that looks for spaces."""
    return Block, _strip_save_path(args.Path)


@hook("WillowGame.WillowPlayerController:FixUpLoadString")
def fix_up_load_string(obj: WillowPlayerController,
                       args: WillowPlayerController.FixUpLoadString.args,
                       ret: WillowPlayerController.FixUpLoadString.ret,
                       func: BoundFunction):
    print(inspect.currentframe().f_code.co_name)
    print(args)
    """Here the game tries to pad the save name to match Save#### format. We just need to block it and return the input, but
     with spaces restored.
    NOTE: Relies on this function only being called to create an arg to LoadGame. Something to keep an eye on.
    """
    return Block, args.InLoadString.replace(SPACE_REPLACE, " ")


@hook("WillowGame.WillowPlayerController:GetSaveGameNameFromid")
def get_save_game_name_from_id(obj: WillowPlayerController,
                               args: WillowPlayerController.GetSaveGameNameFromid.args,
                               ret: WillowPlayerController.GetSaveGameNameFromid.ret,
                               func: BoundFunction):
    """Game uses this a few times to figure out what file to save to. We want to intercept
     to set our own save game name"""
    # When id is -1, we want to go through normal process, and also set LastLoadedFilePath
    # to empty. This function gets called twice on new game load, so we need this here
    # to avoid overwriting another file on the second pass.
    print(inspect.currentframe().f_code.co_name)
    print(args)
    if args.SaveGameId < 0:
        save_manager = obj.GetWillowGlobals().GetWillowSaveGameManager()
        save_manager.LastLoadedFilePath = ""
        return
    # Use LastLoadedFilePath if there is one
    save_name = obj.GetWillowGlobals().GetWillowSaveGameManager().LastLoadedFilePath
    print(save_name)
    if not save_name:
        return

    return Block, save_name

# @hook("WillowGame.WillowPlayerController:GetSaveGameNameFromid", Type.POST_UNCONDITIONAL)
# def get_save_game_name_from_id_post(obj: WillowPlayerController,
#                                args: WillowPlayerController.GetSaveGameNameFromid.args,
#                                ret: WillowPlayerController.GetSaveGameNameFromid.ret,
#                                func: BoundFunction):
#     """Set a few values to default/empty when we've loaded a default character."""
#     pass
    # print(obj.SaveGameFileId, obj.SaveGameName)
    # if args.SaveGameId < 0:
    #     save_manager = obj.GetWillowGlobals().GetWillowSaveGameManager()
    #     save_manager.LastLoadedFilePath = ""
    #     # save_manager.SetCachedPlayerSaveGame(obj.GetMyControllerId(), None)



# @hook("WillowGame.WillowPlayerController:BuildSaveGameNameFromId", Type.POST)
# def BuildSaveGameNameFromId(obj: WillowPlayerController,
#                             args: WillowPlayerController.GetSaveGameNameFromid.args,
#                             ret: WillowPlayerController.GetSaveGameNameFromid.ret,
#                             func: BoundFunction):
#     """Game uses this a few times to figure out what file to save to. We want to intercept
#      to set our own save game name"""
#     pass


@hook("WillowGame.WillowPlayerController:GetHighestSaveGameId")
def get_highest_save_id(obj: WillowPlayerController,
                        args: WillowPlayerController.GetHighestSaveGameId.args,
                        ret: WillowPlayerController.GetHighestSaveGameId.ret,
                        func: BoundFunction):
    print(inspect.currentframe().f_code.co_name)
    print(args)
    """On new games this is called to figure out what the new save ID should be. It won't
    recognize our saves and try to set an ID that's the same as one of ours."""

    @hook("WillowGame.WillowSaveGameManager:GetLastSaveGame", immediately_enable=True)
    def get_last_save_game(obj: WillowSaveGameManager,
                           args: WillowSaveGameManager.GetLastSaveGame.args,
                           ret: WillowSaveGameManager.GetLastSaveGame.ret,
                           func: BoundFunction):
        print(inspect.currentframe().f_code.co_name)
        print(args)
        get_last_save_game.disable()
        last_save = max(save_data.SaveGameFileId for save_data in obj.SaveDataLoadedFromList)
        return Block, last_save


@hook("WillowGame.WillowSaveGameManager:SaveGame", Type.POST_UNCONDITIONAL)
def sgm_save_game(obj: WillowSaveGameManager,
                  args: WillowSaveGameManager.SaveGame.args,
                  ret: WillowSaveGameManager.SaveGame.ret,
                  func: BoundFunction) -> None:
    """This is for when a save is generated programmatically, need to get the LastLoadedFilePath in sync.
    Seems to also be needed for saving a brand new character."""
    print(inspect.currentframe().f_code.co_name)
    print(args)
    if args.Filename.endswith('.sav'):
        obj.LastLoadedFilePath = args.Filename
        # obj.SetCachedPlayerSaveGame(get_pc().GetMyControllerId(), args.SaveGame)


_from_in_game: bool = False


@hook("WillowGame.FrontendGFxMovie:NotifyAtMainMenu")
def notify_at_main_menu(obj: FrontendGFxMovie,
                        args: FrontendGFxMovie.NotifyAtMainMenu.args,
                        ret: FrontendGFxMovie.NotifyAtMainMenu.ret,
                        func):
    """This is for our auto save option. Any time we enter main menu we run this.
    Adding in functionality to show our buttons again that are not in game"""
    print(inspect.currentframe().f_code.co_name)
    print(args)
    global _from_in_game

    if obj.MyFrontendDefinition.Name == "Frontend_DEF" and _from_in_game:
        # log_all_calls(True)
        if auto_update_saves_option.value:
            SaveListProcessor.process_all_saves()

        # When we get to main menu, we want to do this just once until we've gone into the game
        # and back. Don't want this happening from title screen.
        _from_in_game = False
        update_saves_button.is_hidden = False
        restore_saves_button.is_hidden = False
        defrag_saves_button.is_hidden = False


@hook("WillowGame.WillowPlayerController:StartNewPlaySession")
def start_new_play_session(obj, args, ret, func) -> None:
    """Auto rename logic can run next time in main menu"""
    print(inspect.currentframe().f_code.co_name)
    print(args)
    global _from_in_game
    _from_in_game = True
    update_saves_button.is_hidden = True
    restore_saves_button.is_hidden = True
    defrag_saves_button.is_hidden = True


@hook("WillowGame.WillowPlayerController:OnLoadLastSaveGame")
def on_load_last_save_game(obj: WillowPlayerController,
                           args: WillowPlayerController.OnLoadLastSaveGame.args,
                           ret: WillowPlayerController.OnLoadLastSaveGame.ret,
                           func: BoundFunction):
    print(inspect.currentframe().f_code.co_name)
    print(args)
    """Function is only called on initial load into the main menu. If the file trying to
    be loaded isn't in our save list, we intercept and load most recent. This is to prevent
    .bak files from being loaded or default character - happens in both cases because the
    game doesn't recognize our saves when it tries to load the latest."""
    save_manager = obj.GetWillowGlobals().GetWillowSaveGameManager()
    last_path = save_manager.LastLoadedFilePath
    print(last_path)
    print(save_manager.SaveDataLoadedFromList)
    if last_path in save_manager.GetSaveGameList(obj.GetMyControllerId(), -1, ""):
        return

    most_recent_save: WillowSaveGameManager.PlayerSaveData = max(save_manager.SaveDataLoadedFromList,
                           key=lambda save_data: save_data.LastSaveDate,
                           default=None)
    if most_recent_save:
        obj.LoadGame(_strip_save_path(most_recent_save.FilePath), None)
    else:
        func(obj.DefaultSaveGameString, None)

    return Block


@hook("WillowGame.WillowGFxDialogBox:DisplayOkBox", Type.POST)
def display_ok_box(obj: WillowGFxDialogBox,
                   args: WillowGFxDialogBox.DisplayOkBox.args,
                   ret: WillowGFxDialogBox.DisplayOkBox.ret,
                   func: BoundFunction):
    print(inspect.currentframe().f_code.co_name)
    print(args)
    """Really hate this, but I can't figure out another way to suppress the incorrect message that TPS loads."""
    if args.File == "WillowMenu" and args.Section in ("dlgCorruptLastLoadedSaveData", "dlgLoadedFromBackupSave"):
        obj.Close()


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
    if save_path_hidden_option.value:
        get_all_save_data(lambda x: None)  # Need save manager to have this handy otherwise the game won't load.


mod = build_mod(
    deregister_same_settings=True,
    options=[save_path_hidden_option, auto_update_saves_option, update_saves_button, restore_saves_button, defrag_saves_button],
    on_enable=_on_enable
)

if not save_path_hidden_option.value:
    print('Attempting to find game saves folder...')
    save_path = extract_user_save_path()
    if save_path:
        save_path_hidden_option.value = save_path
        mod.save_settings()
        get_all_save_data(lambda x: None)  # Need save manager to have this handy otherwise the game won't load.
        print(f'Successfully found game saves folder at {save_path}')

register_module(__name__)
