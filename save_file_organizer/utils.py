from __future__ import annotations

import os
import re
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
                save_dir = os.path.join(root, dir_name, game_str, 'WillowGame', 'SaveData', save_dir_id)
                if os.path.exists(save_dir):
                    return os.path.normpath(save_dir).replace('\\', '/')

    raise ValueError(f"Could not find save folder for id {save_dir_id}")



register_module(__name__)