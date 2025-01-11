from __future__ import annotations

import os
import stat
from functools import partial

from typing import Any, Callable, List, TYPE_CHECKING

from mods_base import hook
# from named_saves import get_all_save_data, get_pc, mod, save_path_hidden_option
from unrealsdk import make_struct
from unrealsdk.hooks import Type

if TYPE_CHECKING:
    from bl2 import PlayerSaveGame, WillowSaveGameManager

def load_player_save_game(file_name: str, callback: Callable[[PlayerSaveGame], None]) -> None:
    """Load a player save game for callback to process.
    file_name: only the file name, no directory included"""
    pc = get_pc()
    save_manager = pc.GetWillowGlobals().GetWillowSaveGameManager()
    save_manager.__OnLoadComplete__Delegate = save_manager.OnLoadComplete
    print(f'BeginLoadGame file_name: {file_name}')
    save_manager.BeginLoadGame(pc.GetMyControllerId(), file_name, -1)

    @hook("WillowGame.WillowSaveGameManager:OnLoadComplete", Type.POST, immediately_enable=True)
    def on_load_complete(*_: Any) -> None:
        print(f"on_load_complete callback: {callback}")
        on_load_complete.disable()
        player_save_game = save_manager.EndLoadGame(pc.GetMyControllerId(), make_struct("LoadInfo"), 0)[0]
        save_manager.__OnLoadComplete__Delegate = None
        callback(player_save_game)


def save_player_save_game(file_name: str, player_save_game: PlayerSaveGame, callback: [[], None]) -> None:
    pc = get_pc()
    save_manager = pc.GetWillowGlobals().GetWillowSaveGameManager()
    save_manager.__OnSaveComplete__Delegate = save_manager.OnSaveComplete

    @hook("WillowGame.WillowSaveGameManager:OnSaveComplete", Type.POST, immediately_enable=True)
    def on_save_complete(*_: Any) -> None:
        on_save_complete.disable()
        print(f"on_save_complete callback: {callback}")
        save_manager.__OnSaveComplete__Delegate = None
        save_manager.ClearCache()
        callback()

    save_manager.SaveGame(pc.GetMyControllerId(), player_save_game, file_name, -1)


def get_next_numeric_file_id(id: int) -> int:
    """Getting rid of Hex digits because I don't like them."""
    while True:
        id += 1
        hex_str = f"{id:04X}"
        if all(c in "0123456789" for c in hex_str):
            return id


def process_all_saves(_: Any = None) -> None:
    """
    Well this got really ugly. Lots of messing around wtih nested scopes due to needing to wait for results.

    """
    if not mod.is_enabled:
        print("Need to enable mod before renaming saves.")
        return

    pc = get_pc()

    def process_next_save(save_list: List[WillowSaveGameManager.PlayerSaveData], idx: int = 0, file_id: int = 0) -> None:
        """Manage our whole list by recursively calling this function on repeat. """

        if idx >= len(save_list):
            print("All save files processed.")
            return

        def begin_process_save(player_save_game: PlayerSaveGame, idx: int, file_id: int):
            """Given a PlayerSaveGame, PlayerSaveData, and a new file_id, we change the id, save the file, and rename it.
            The save file needs a callback so that we can con complete our process once it finishes."""
            print("begin_process_save")
            def complete_process_save(idx: int, file_id: int):
                """This is called when save is completed. Change file permissions back to original, then kick off the next save loop."""
                print(f"complete_process_save idx: {idx} file_id: {file_id} file_name: {new_file_name}")
                os.chmod(new_file_path, old_st_mode)
                # if new_file_name != old_file_name:
                #     print(f"Renamed save: '{old_file_name}' -> '{new_file_name}'")
                print(f"call process_next_save idx: {idx + 1} file_id: {get_next_numeric_file_id(file_id)}")
                process_next_save(save_list, idx + 1, get_next_numeric_file_id(file_id))

            old_file_name = os.path.split(player_save_data.FilePath)[1]
            old_file_path = os.path.join(save_path_hidden_option.value, old_file_name)
            new_file_name = pc.GetSaveGameNameFromid(file_id).replace(".sav", f" - {player_save_data.UICharacterName}.sav")
            new_file_path = os.path.join(save_path_hidden_option.value, new_file_name)

            old_file_id = player_save_game.SaveGameId
            old_st_mode = os.stat(old_file_path).st_mode  # Store initial permissions

            os.chmod(old_file_path, stat.S_IWRITE)
            player_save_game.SaveGameId = file_id
            os.rename(old_file_path, new_file_path)
            print(f"rename idx: {idx} file_id: {file_id}")
            if file_id != old_file_id:
                save_player_save_game(new_file_name, player_save_game, callback=partial(complete_process_save, idx=idx, file_id=file_id))
            else:
                complete_process_save(idx, file_id)
            # complete_process_save(idx, file_id)

        player_save_data = save_list[idx]
        file_name = os.path.split(player_save_data.FilePath)[1]
        print(f'process_next_save idx: {idx} file_id: {file_id} file_name: {file_name} save_list_len: {len(save_list)}')
        load_player_save_game(file_name, callback=partial(begin_process_save, idx=idx, file_id=file_id))

    get_all_save_data(process_next_save)
