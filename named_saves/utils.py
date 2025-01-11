from __future__ import annotations

import os
import re
from typing import TYPE_CHECKING, cast

import mods_base
from named_saves.reloader import register_module

if TYPE_CHECKING:
    from bl2 import WillowPlayerController


def get_pc() -> WillowPlayerController:
    return cast("WillowPlayerController", mods_base.get_pc())


def extract_user_save_path() -> str:
    """Search the user's home directory for our path. This takes a few seconds and
     should only be used once, with result stored in a hidden option."""

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
                save_dir = os.path.join(root, dir_name, 'Borderlands 2', 'WillowGame', 'SaveData', save_dir_id)
                if os.path.exists(save_dir):
                    return os.path.normpath(save_dir).replace('\\', '/')

    raise ValueError(f"Could not find save folder for id {save_dir_id}")



register_module(__name__)