from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from stat import S_IWRITE

from typing import Any, Callable, Dict, List, TYPE_CHECKING
from mods_base import HookType, hook
from named_saves.utils import get_pc
from named_saves.reloader import register_module
from unrealsdk import load_package, make_struct
from unrealsdk.hooks import Type

if TYPE_CHECKING:
    from bl2 import PlayerSaveGame, WillowSaveGameManager


def get_all_save_data(callback: Callable[[List[WillowSaveGameManager.PlayerSaveData]], None]) -> None:
    """
    1. Load save games from the save manager in order to be able to get character names
    2. Once we have the save game list, execute the callback
    """
    pc = get_pc()
    save_manager = pc.GetWillowGlobals().GetWillowSaveGameManager()
    save_file_list = list(save_manager.GetSaveGameList(pc.GetMyControllerId(), -1, ''))

    save_manager.__OnListLoadComplete__Delegate = save_manager.OnListLoadComplete
    save_manager.BeginGetSaveGameDataFromList(pc.GetMyControllerId(), save_file_list, -1)

    @hook("WillowGame.WillowSaveGameManager:OnListLoadComplete", Type.POST, immediately_enable=True)
    def on_load_list_complete(*_: Any) -> None:
        returned_saves = save_manager.EndGetSaveGameDataFromList(pc.GetMyControllerId())
        dedup = list({save.FilePath: save for save in returned_saves}.values())
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
    new_file_name: str = ''
    st_mode: int = 0

    def __post_init__(self):
        from named_saves import save_path_hidden_option
        self.user_save_path = save_path_hidden_option.value
        self.new_file_name = get_pc().GetSaveGameNameFromid(self.new_save_id).replace(".sav", f" - {self.char_name}.sav")
        self.st_mode = os.stat(os.path.join(save_path_hidden_option.value, self.old_file_name)).st_mode


    @property
    def old_file_path(self) -> str:
        return os.path.join(self.user_save_path, self.old_file_name)

    @property
    def new_file_path(self) -> str:
        return os.path.join(self.user_save_path, self.new_file_name)


class SaveListProcessor:
    """This is really just here so I can manage state between chained function calls and callbacks.
    It will only exist as an instance during processing. The functions are tightly coupled with each other
    unfortunately."""
    current_player_save_game: PlayerSaveGame

    def __init__(self, save_list: List[WillowSaveGameManager.PlayerSaveData]):

        for i, save in enumerate(save_list):
            print(i, save.FilePath)

        self.pc = get_pc()

        self.save_list = save_list
        self.idx = -1
        self.save_id = -1
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
        """Main controller, this gets called each time we need a new save processed."""
        print("process_next_save")
        self.idx += 1
        self.save_id = self.get_next_numeric_file_id(self.save_id)
        if self.idx >= len(self.save_list):
            print("All save files processed.")
            return

        player_save_data = self.save_list[self.idx]
        print(self.idx)
        self.current_file_info = FileInfo(
            char_name=player_save_data.UICharacterName,
            old_save_id=player_save_data.SaveGameFileId,
            new_save_id=self.save_id,
            old_file_name=os.path.split(player_save_data.FilePath)[1],
        )
        self.save_list_info[self.idx] = self.current_file_info
        self.rename_current_file()
        self.load_player_save_game()

    def rename_current_file(self):
        cfi = self.current_file_info
        os.chmod(cfi.old_file_path, S_IWRITE)
        os.rename(cfi.old_file_path, cfi.new_file_path)
        if cfi.new_file_name != cfi.old_file_name:
            print(f"Renamed save: '{cfi.old_file_name}' -> '{cfi.new_file_name}'")

    def load_player_save_game(self) -> None:
        print("load_player_save_game")
        save_manager = self.pc.GetWillowGlobals().GetWillowSaveGameManager()
        setattr(save_manager, "__OnLoadComplete__Delegate", save_manager.OnLoadComplete)

        @hook("WillowGame.WillowSaveGameManager:OnLoadComplete", Type.POST, immediately_enable=True)
        def on_load_complete(*_: Any) -> None:
            print("on_load_complete")
            on_load_complete.disable()
            player_save_game = save_manager.EndLoadGame(self.pc.GetMyControllerId(), make_struct("LoadInfo"), 0)[0]
            setattr(save_manager, "__OnLoadComplete__Delegate", None)
            self.current_player_save_game = player_save_game
            self.edit_player_save_game()

        save_manager.BeginLoadGame(self.pc.GetMyControllerId(), self.current_file_info.new_file_name, -1)

    def edit_player_save_game(self):
        print("edit_player_save_game")

        self.current_player_save_game.SaveGameId = self.current_file_info.new_save_id
        save_manager = self.pc.GetWillowGlobals().GetWillowSaveGameManager()
        save_manager.SaveGame(self.pc.GetMyControllerId(), self.current_player_save_game, self.current_file_info.new_file_name, -1)
        self.finish_save_processing()

    def finish_save_processing(self):
        print("finish_save_processing")

        save_manager = self.pc.GetWillowGlobals().GetWillowSaveGameManager()

        tick_count = 100  # I dunno just in case it takes forever.
        @hook("WillowGame.WillowGameViewportClient:Tick", Type.POST, immediately_enable=True)
        def wait_ticks(*_: Any) -> None:
            nonlocal tick_count
            tick_count -= 1
            if tick_count > 0 and save_manager.CurrentState[0] != 0:
                # print(self.pc.GetWillowGlobals().GetWillowSaveGameManager().CurrentState)
                return

            wait_ticks.disable()

            os.chmod(self.current_file_info.new_file_path, self.current_file_info.st_mode)
            Path(self.current_file_info.new_file_path).touch(exist_ok=True)
            self.process_next_save()


    @classmethod
    def process_all_saves(cls, _: Any = None) -> None:
        from named_saves import mod
        if not mod.is_enabled:
            print("Need to enable mod before renaming saves.")
            return

        load_package("GD_Tulip_Mechro_Streaming_SF")
        load_package("GD_Lilac_Psycho_Streaming_SF")
        load_package("GD_Assassin_Streaming_SF")
        load_package("GD_Soldier_Streaming_SF")
        load_package("GD_Siren_Streaming_SF")
        load_package("GD_Mercenary_Streaming_SF")

        get_all_save_data(cls)



register_module(__name__)
