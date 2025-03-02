from __future__ import annotations

import os
import re
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
    """Search the user's home directory for our path. This takes a few seconds and
     should only be used once, with result stored in a hidden option."""
    game_str = GAME_LOOKUP.get(Game.get_current().name)
    if not game_str:
        print(f"Could not locate save folder for game {Game.get_current().name}")
        return ""

    pc = get_pc()
    save_path = Path(pc.OnlineSub.ProfileDataDirectory)

    home = Path.home()
    saves = next(home.rglob(game_str))

    return str(next(saves.rglob(save_path.parts[-1])))


register_module(__name__)