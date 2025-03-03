from __future__ import annotations

import ctypes
from pathlib import Path
from typing import TYPE_CHECKING, cast

import mods_base
from mods_base import Game
from save_file_organizer.reloader import register_module

if TYPE_CHECKING:
    from common import WillowPlayerController


def get_pc() -> WillowPlayerController:
    return cast("WillowPlayerController", mods_base.get_pc())


GAME_LOOKUP = {"BL2": "Borderlands 2", "TPS": "Borderlands The Pre-Sequel"}


def extract_user_save_path() -> str:
    game_str = GAME_LOOKUP.get(Game.get_current().name)
    if not game_str:
        print(f"Could not locate save folder for game {Game.get_current().name}")
        return ""

    # Game folder - stripped version is WillowGame/SaveData/<Steam/Epic Id>
    pc = get_pc()
    save_path = Path(pc.OnlineSub.ProfileDataDirectory)
    save_path_stripped = Path(*[part for part in save_path.parts[-3:] if part != ".."])

    # Get documents folder using ctypes
    path_buf = ctypes.create_unicode_buffer(260)
    ctypes.windll.shell32.SHGetFolderPathW(0, 5, 0, 0, path_buf)

    final_path = Path(path_buf.value) / "My Games" / game_str / save_path_stripped
    return str(final_path)


register_module(__name__)
