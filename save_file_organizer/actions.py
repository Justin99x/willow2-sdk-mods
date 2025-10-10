from __future__ import annotations

import os
import re
from dataclasses import dataclass
from pathlib import Path
from stat import S_IWRITE
from typing import TYPE_CHECKING, Any

from mods_base import ButtonOption, hook
from unrealsdk import find_enum, load_package, make_struct
from unrealsdk.hooks import Type, prevent_hooking_direct_calls

from save_file_organizer.reloader import register_module
from save_file_organizer.utils import get_pc

if TYPE_CHECKING:
    from collections.abc import Callable

    from common import PlayerSaveGame, WillowSaveGameManager

    make_struct_load_info = WillowSaveGameManager.LoadInfo.make_struct
    ELoadPlayerBehavior = WillowSaveGameManager.ELoadPlayerBehavior
else:
    make_struct_load_info = make_struct
    ELoadPlayerBehavior = find_enum("ELoadPlayerBehavior")


_TEMP_STR = ".temp"
_MAX_HEX = 39320


def _sanitize_character_name(character_name: str) -> str:
    """Sanitizes character name to be a valid filename."""
    from save_file_organizer import save_path_hidden_option

    max_length = (
        255 - 15 - len(save_path_hidden_option.value)
    )  # Windows limit less Save#### - .sav and the rest of the abs path

    # Remove reserved characters
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    sanitized = re.sub(invalid_chars, "_", character_name)

    return sanitized[:max_length] if len(sanitized) > max_length else sanitized


def get_all_save_data(
    callback: Callable[[list[WillowSaveGameManager.PlayerSaveData]], Any],
) -> None:
    """
    Loads all save data and triggers a callback.

    This function does not return anything. It is used to trigger the save data
    search so that WillowSaveGameManager has access to an up-to-date list for
    later actions.
    """

    # 1. Load save games from the save manager in order to be able to get character names
    # 2. Once we have the save game list, execute the callback.

    pc = get_pc()
    save_manager = pc.GetWillowGlobals().GetWillowSaveGameManager()
    # This only works because we overwrite it with a hook
    save_file_list = list(save_manager.GetSaveGameList(pc.GetMyControllerId(), -1, ""))

    save_manager.__OnListLoadComplete__Delegate = save_manager.OnListLoadComplete  # type: ignore
    save_manager.BeginGetSaveGameDataFromList(pc.GetMyControllerId(), save_file_list, -1)

    @hook("WillowGame.WillowSaveGameManager:OnListLoadComplete", Type.POST, immediately_enable=True)
    def on_load_list_complete(*_: Any) -> None:
        returned_saves = save_manager.EndGetSaveGameDataFromList(pc.GetMyControllerId())
        dedup = list({save.FilePath: save for save in returned_saves}.values())
        # Sort by save_id, keeps rename results consistent
        saves = sorted(dedup, key=lambda x: x.SaveGameFileId)
        save_manager.__OnListLoadComplete__Delegate = None  # type: ignore
        on_load_list_complete.disable()
        callback(saves)


@dataclass
class FileInfo:
    char_name: str = ""
    old_save_id: int = 0
    new_save_id: int = 0
    old_file_name: str = ""
    st_mode: int = 0
    restore: bool = False

    def __post_init__(self) -> None:
        from save_file_organizer import save_path_hidden_option  # Avoid circular import

        self.user_save_path = save_path_hidden_option.value
        self.st_mode = (Path(save_path_hidden_option.value) / self.old_file_name).stat().st_mode

    @property
    def new_file_name(self) -> str:  # noqa: D102
        # We want the real version of save game name from id here, not our hooked one.
        with prevent_hooking_direct_calls():
            if self.restore:
                return get_pc().GetSaveGameNameFromid(self.new_save_id)
            return (
                get_pc()
                .GetSaveGameNameFromid(self.new_save_id)
                .replace(".sav", f" - {_sanitize_character_name(self.char_name)}.sav")
            )

    @property
    def old_file_path(self) -> str:  # noqa: D102
        return str(Path(self.user_save_path) / self.old_file_name)

    @property
    def new_file_path(self) -> str:  # noqa: D102
        return str(Path(self.user_save_path) / self.new_file_name)


class SaveListProcessor:
    """
    Class responsible for executing save file changes.

    This is really a function disguised as a class so I can manage state between chained function
    calls and callbacks. It will only exist as an instance during processing. The functions are
    tightly coupled with each other unfortunately.
    """

    current_player_save_game: PlayerSaveGame
    last_button_pushed: ButtonOption | None

    def __init__(self, save_list: list[WillowSaveGameManager.PlayerSaveData]) -> None:
        # Init kicks off the process of processing all saves. save_list is generally grabbed from a
        # callback from the hook of generating the save list.
        assert not (self.defrag and self.restore)

        self.pc = get_pc()
        self.save_manager = self.pc.GetWillowGlobals().GetWillowSaveGameManager()
        self.loaded_path = self.save_manager.LastLoadedFilePath

        self.save_list = save_list
        self.idx = -1
        self.defrag_save_id = -1
        self.current_file_info = FileInfo
        self.save_list_info: dict[int, FileInfo] = {}

        self._process_next_save()

    @staticmethod
    def _get_next_numeric_file_id(file_id: int) -> int:
        # Getting rid of Hex digits because I don't like them.
        if file_id > _MAX_HEX:  # Top end of possible 4 digit hex results
            file_id = -1
        while True:
            file_id += 1
            hex_str = f"{file_id:04X}"
            if all(c in "0123456789" for c in hex_str):
                return file_id

    def _process_next_save(self) -> None:
        # Start process for a save file.
        # This kicks off chained calls of several functions before coming back here for next save.

        self.idx += 1
        self.defrag_save_id = self._get_next_numeric_file_id(self.defrag_save_id)
        if self.idx >= len(self.save_list):
            self._finalize_processing()
            return

        # Avoid giving same Save#### filename when two saves happen to have the same SaveGameFileId
        player_save_data = self.save_list[self.idx]
        seen_save_ids = [save.new_save_id for save in self.save_list_info.values()]
        new_save_id = self.defrag_save_id if self.defrag else player_save_data.SaveGameFileId
        while new_save_id in seen_save_ids:
            new_save_id = self._get_next_numeric_file_id(new_save_id)

        self.current_file_info = FileInfo(
            char_name=player_save_data.UICharacterName,
            old_save_id=player_save_data.SaveGameFileId,
            new_save_id=new_save_id,
            old_file_name=os.path.split(player_save_data.FilePath)[1],
            restore=self.restore,
        )

        self.save_list_info[self.idx] = self.current_file_info
        self._rename_current_file()
        if self.defrag:
            self._load_player_save_game()
        else:
            self._finish_save_processing()

    def _rename_current_file(self) -> None:
        # Attempts to rename the current file.

        # If name already exists, increment id by 1 and try again. Need to update the save manager
        # LastLoadedFilePath if we're changing the currently active name.

        cfi = self.current_file_info

        if cfi.new_file_name != cfi.old_file_name:
            Path(cfi.old_file_path).chmod(S_IWRITE)  # pyright: ignore[reportArgumentType]
            try:
                Path(cfi.old_file_path).rename(cfi.new_file_path)  # pyright: ignore[reportArgumentType]
            except FileExistsError:
                Path(cfi.old_file_path).rename(f"{cfi.new_file_path}{_TEMP_STR}")  # pyright: ignore[reportArgumentType]

            # Tracking which file is currently loaded, we'll set on save manager at the end of the
            # process.
            if cfi.old_file_name == self.loaded_path:
                self.loaded_path = cfi.new_file_name
            print(f"Renamed save: '{cfi.old_file_name}' -> '{cfi.new_file_name}'")

    def _load_player_save_game(self) -> None:
        setattr(self.save_manager, "__OnLoadComplete__Delegate", self.save_manager.OnLoadComplete)

        @hook("WillowGame.WillowSaveGameManager:OnLoadComplete", Type.POST, immediately_enable=True)
        def on_load_complete(*_: Any) -> None:
            on_load_complete.disable()
            player_save_game = self.save_manager.EndLoadGame(
                self.pc.GetMyControllerId(),
                make_struct_load_info("LoadInfo"),
                ELoadPlayerBehavior.ELPB_LoadOnly,
            )[0]
            setattr(self.save_manager, "__OnLoadComplete__Delegate", None)
            self.current_player_save_game = player_save_game
            self._edit_player_save_game()

        self.save_manager.BeginLoadGame(
            self.pc.GetMyControllerId(),
            self.current_file_info.new_file_name,
            -1,  # pyright: ignore[reportArgumentType]
        )

    def _edit_player_save_game(self) -> None:
        self.current_player_save_game.SaveGameId = self.current_file_info.new_save_id
        self.save_manager.SaveGame(
            self.pc.GetMyControllerId(),
            self.current_player_save_game,
            self.current_file_info.new_file_name,  # pyright: ignore[reportArgumentType]
            -1,
        )
        self._finish_save_processing()

    def _finish_save_processing(self) -> None:
        tick_count = 100  # I dunno just in case it takes forever.

        @hook("WillowGame.WillowGameViewportClient:Tick", Type.POST, immediately_enable=True)
        def wait_ticks(*_: Any) -> None:
            nonlocal tick_count
            tick_count -= 1
            if tick_count > 0 and self.save_manager.CurrentState[0] != 0:
                return

            wait_ticks.disable()

            Path(self.current_file_info.new_file_path).chmod(self.current_file_info.st_mode)  # pyright: ignore[reportArgumentType]
            Path(self.current_file_info.new_file_path).touch(exist_ok=True)  # pyright: ignore[reportArgumentType]
            self._process_next_save()

    def _finalize_processing(self) -> None:
        # Runs at very end of process.
        from save_file_organizer import save_path_hidden_option

        self.save_manager.LastLoadedFilePath = self.loaded_path  # pyright: ignore[reportAttributeAccessIssue]
        # Unload character. Too many sync issues occur if we keep this where it was.
        if self.defrag:
            with prevent_hooking_direct_calls():
                self.save_manager.LastLoadedFilePath = ""
                self.save_manager.SetCachedPlayerSaveGame(
                    self.pc.GetMyControllerId(),
                    self.pc.GetWillowGlobals().GetDefaultPlayerSaveGame(""),
                )
                self.pc.LastLoadedSaveGame = None
                self.pc.RefreshPlayerStandIn()
        # For name conflicts earlier we added a .temp, need to remove now.
        for file in os.listdir(save_path_hidden_option.value):
            if file.endswith(_TEMP_STR):
                path = Path(save_path_hidden_option.value) / file
                st_mode = path.stat().st_mode
                path.chmod(S_IWRITE)
                new_path = path.with_name(path.name.removesuffix(_TEMP_STR))
                path.rename(new_path)
                new_path.chmod(st_mode)

        print("All save files processed.")

    @classmethod
    def process_all_saves(cls, button: ButtonOption | None = None) -> None:
        """
        Process all saves according to the specific button option passed in.

        Will search for all saves in the save folder, and do one of three things:
        1. Rename all saves -> renames them according to the character name
        2. Restore all saves -> renames saves back to supported Save####.sav format
        3. Defrag all saves -> renames and sets ids such that saves start from 0001
            and increment up.
        """

        cls.last_button_pushed = button
        from save_file_organizer import defrag_saves_button, mod, restore_saves_button

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
