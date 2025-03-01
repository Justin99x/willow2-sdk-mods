from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from stat import S_IWRITE

from typing import Any, Callable, Dict, List, TYPE_CHECKING

from mods_base import ButtonOption, hook
from save_file_organizer.utils import get_pc
from save_file_organizer.reloader import register_module
from unrealsdk import load_package, make_struct
from unrealsdk.hooks import Type, prevent_hooking_direct_calls

if TYPE_CHECKING:
    from common import PlayerSaveGame, WillowSaveGameManager


import re

_TEMP_STR = ".temp"

def sanitize_character_name(character_name: str) -> str:
    from save_file_organizer import save_path_hidden_option
    max_length = 255 - 15 - len(save_path_hidden_option.value) # Windows limit less Save#### - .sav and the rest of the abs path

    # Remove reserved characters
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    sanitized = re.sub(invalid_chars, "_", character_name)

    return sanitized[:max_length] if len(sanitized) > max_length else sanitized



# Example usage

def get_all_save_data(callback: Callable[[List[WillowSaveGameManager.PlayerSaveData]], None]) -> None:
    """
    1. Load save games from the save manager in order to be able to get character names
    2. Once we have the save game list, execute the callback
    """
    pc = get_pc()
    save_manager = pc.GetWillowGlobals().GetWillowSaveGameManager()
    # This only works because we overwrite it with a hook
    save_file_list = list(save_manager.GetSaveGameList(pc.GetMyControllerId(), -1, ''))

    save_manager.__OnListLoadComplete__Delegate = save_manager.OnListLoadComplete
    save_manager.BeginGetSaveGameDataFromList(pc.GetMyControllerId(), save_file_list, -1)

    @hook("WillowGame.WillowSaveGameManager:OnListLoadComplete", Type.POST, immediately_enable=True)
    def on_load_list_complete(*_: Any) -> None:
        from save_file_organizer import save_path_hidden_option  # Avoid circular import

        returned_saves = save_manager.EndGetSaveGameDataFromList(pc.GetMyControllerId())
        dedup = list({save.FilePath: save for save in returned_saves}.values())
        # Sort by save_id, keeps rename results consistent
        saves = sorted(dedup, key=lambda x: x.SaveGameFileId)
        save_manager.__OnListLoadComplete__Delegate = None
        on_load_list_complete.disable()
        callback(saves)

@dataclass
class FileInfo:
    char_name: str = ''
    old_save_id: int = 0
    new_save_id: int = 0
    old_file_name: str = ''
    st_mode: int = 0
    restore: bool = False

    def __post_init__(self):
        from save_file_organizer import save_path_hidden_option  # Avoid circular import
        self.user_save_path = save_path_hidden_option.value
        self.st_mode = os.stat(os.path.join(save_path_hidden_option.value, self.old_file_name)).st_mode

    @property
    def new_file_name(self):
        # We want the real version of save game name from id here, not our hooked one.
        with prevent_hooking_direct_calls():
            if self.restore:
                return get_pc().GetSaveGameNameFromid(self.new_save_id)
            return get_pc().GetSaveGameNameFromid(self.new_save_id).replace(".sav", f" - {sanitize_character_name(self.char_name)}.sav")

    @property
    def old_file_path(self) -> str:
        return os.path.join(self.user_save_path, self.old_file_name)

    @property
    def new_file_path(self) -> str:
        return os.path.join(self.user_save_path, self.new_file_name)



class SaveListProcessor:
    """This is really a function disguised as a class so I can manage state between chained function calls and callbacks.
    It will only exist as an instance during processing. The functions are tightly coupled with each other unfortunately.
    """
    current_player_save_game: PlayerSaveGame
    last_button_pushed: ButtonOption | None

    def __init__(self, save_list: List[WillowSaveGameManager.PlayerSaveData]):
        """Init kicks off the process of processing all saves. save_list is generally grabbed from a callback from
        the hook of generating the save list."""
        assert not (self.defrag and self.restore)

        self.pc = get_pc()
        self.save_manager = self.pc.GetWillowGlobals().GetWillowSaveGameManager()
        self.loaded_path = self.save_manager.LastLoadedFilePath

        self.save_list = save_list
        self.idx = -1
        self.defrag_save_id = -1
        self.current_file_info = FileInfo
        self.save_list_info: Dict[int, FileInfo] = {}

        self.process_next_save()

    @staticmethod
    def get_next_numeric_file_id(id: int) -> int:
        """Getting rid of Hex digits because I don't like them."""
        if id > 39320:  # Top end of possible 4 digit hex results
            id = -1
        while True:
            id += 1
            hex_str = f"{id:04X}"
            if all(c in "0123456789" for c in hex_str):
                return id


    def process_next_save(self):
        """Start process for a save file. This kicks off chained calls of several functions before coming back here for next save."""
        self.idx += 1
        self.defrag_save_id = self.get_next_numeric_file_id(self.defrag_save_id)
        if self.idx >= len(self.save_list):
            self.finalize_processing()
            return

        # Avoid giving same Save#### filename when two saves happen to have the same SaveGameFileId
        player_save_data = self.save_list[self.idx]
        seen_save_ids = [save.new_save_id for save in self.save_list_info.values()]
        new_save_id = self.defrag_save_id if self.defrag else player_save_data.SaveGameFileId
        while new_save_id in seen_save_ids:
            new_save_id = self.get_next_numeric_file_id(new_save_id)

        self.current_file_info = FileInfo(
            char_name=player_save_data.UICharacterName,
            old_save_id=player_save_data.SaveGameFileId,
            new_save_id=new_save_id,
            old_file_name=os.path.split(player_save_data.FilePath)[1],
            restore=self.restore
        )

        self.save_list_info[self.idx] = self.current_file_info
        self.rename_current_file()
        if self.defrag:
            self.load_player_save_game()
        else:
            self.finish_save_processing()

    def rename_current_file(self):
        """Attempts to rename the current file. If name already exists, increment id by 1 and try again.
        Need to update the save manager LastLoadedFilePath if we're changing the currently active game."""
        cfi = self.current_file_info

        if cfi.new_file_name != cfi.old_file_name:
            os.chmod(cfi.old_file_path, S_IWRITE)
            try:
                os.rename(cfi.old_file_path, cfi.new_file_path)
            except FileExistsError:
                os.rename(cfi.old_file_path, f"{cfi.new_file_path}{_TEMP_STR}")

            # Tracking which file is currently loaded, we'll set on save manager at the end of the process.
            if cfi.old_file_name == self.loaded_path:
                self.loaded_path = cfi.new_file_name
            print(f"Renamed save: '{cfi.old_file_name}' -> '{cfi.new_file_name}'")

    def load_player_save_game(self) -> None:

        setattr(self.save_manager, "__OnLoadComplete__Delegate", self.save_manager.OnLoadComplete)

        @hook("WillowGame.WillowSaveGameManager:OnLoadComplete", Type.POST, immediately_enable=True)
        def on_load_complete(*_: Any) -> None:
            on_load_complete.disable()
            player_save_game = self.save_manager.EndLoadGame(self.pc.GetMyControllerId(), make_struct("LoadInfo"), 0)[0]
            setattr(self.save_manager, "__OnLoadComplete__Delegate", None)
            self.current_player_save_game = player_save_game
            self.edit_player_save_game()

        self.save_manager.BeginLoadGame(self.pc.GetMyControllerId(), self.current_file_info.new_file_name, -1)

    def edit_player_save_game(self):
        self.current_player_save_game.SaveGameId = self.current_file_info.new_save_id
        self.save_manager.SaveGame(self.pc.GetMyControllerId(), self.current_player_save_game, self.current_file_info.new_file_name, -1)
        self.finish_save_processing()

    def finish_save_processing(self):
        tick_count = 100  # I dunno just in case it takes forever.

        @hook("WillowGame.WillowGameViewportClient:Tick", Type.POST, immediately_enable=True)
        def wait_ticks(*_: Any) -> None:
            nonlocal tick_count
            tick_count -= 1
            if tick_count > 0 and self.save_manager.CurrentState[0] != 0:
                return

            wait_ticks.disable()

            os.chmod(self.current_file_info.new_file_path, self.current_file_info.st_mode)
            Path(self.current_file_info.new_file_path).touch(exist_ok=True)
            self.process_next_save()

    def finalize_processing(self):
        # Runs at very end of process.
        from save_file_organizer import save_path_hidden_option
        self.save_manager.LastLoadedFilePath = self.loaded_path
        # Unload character. Too many sync issues occur if we keep this where it was.
        if self.defrag:
            with prevent_hooking_direct_calls():
                self.save_manager.LastLoadedFilePath = ""
                self.save_manager.SetCachedPlayerSaveGame(self.pc.GetMyControllerId(), self.pc.GetWillowGlobals().GetDefaultPlayerSaveGame("Axton"))
                self.pc.LastLoadedSaveGame = None
                self.pc.RefreshPlayerStandIn()
        # For name conflicts earlier we added a .temp, need to remove now.
        for file in os.listdir(save_path_hidden_option.value):
            if file.endswith(_TEMP_STR):
                path = os.path.join(save_path_hidden_option.value, file)
                st_mode = os.stat(os.path.join(save_path_hidden_option.value, file)).st_mode
                os.chmod(path, S_IWRITE)
                os.rename(path, path.removesuffix(_TEMP_STR))
                os.chmod(path, st_mode)

        print("All save files processed.")

    @classmethod
    def process_all_saves(cls, button: ButtonOption = None) -> None:
        cls.last_button_pushed = button
        from save_file_organizer import mod, defrag_saves_button, restore_saves_button
        if not mod.is_enabled:
            print("Need to enable mod before renaming saves.")
            return

        cls.defrag = False
        cls.restore = False
        """Saves don't load properly unless the character packages are loaded."""
        if button == defrag_saves_button:
            cls.defrag = True

            load_package("GD_Tulip_Mechro_Streaming_SF")
            load_package("GD_Lilac_Psycho_Streaming_SF")
            load_package("GD_Assassin_Streaming_SF")
            load_package("GD_Soldier_Streaming_SF")
            load_package("GD_Siren_Streaming_SF")
            load_package("GD_Mercenary_Streaming_SF")
        if button == restore_saves_button:
            cls.restore = True

        # Kicks off save process
        get_all_save_data(cls)


register_module(__name__)
