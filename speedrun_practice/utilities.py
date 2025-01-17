from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass
from enum import Enum, Flag, auto
from typing import List, TYPE_CHECKING, cast

from legacy_compat import legacy_compat
from mods_base import MODS_DIR, get_pc as _get_pc
from networking import targeted
from speedrun_practice.reloader import register_module
from unrealsdk import find_object, make_struct

with (legacy_compat()):
    import Mods.Commander.Builtin as commander

if TYPE_CHECKING:
    from bl2 import LANServerBrowserGFxMovie, WillowCoopGameInfo, WillowPlayerController, Object

    make_struct_vector = Object.Vector._make_struct
    make_struct_rotator = Object.Rotator._make_struct
else:
    make_struct_vector = make_struct_rotator = make_struct

DefaultGameInfo: WillowCoopGameInfo = cast("WillowCoopGameInfo",
                                           find_object("WillowCoopGameInfo", "WillowGame.Default__WillowCoopGameInfo"))
MODDIR = os.path.join(MODS_DIR, 'speedrun_practice')
CONFIG_PATH = os.path.join(MODDIR, 'config.json')


class GameVersion(Flag):
    V1_1_0 = auto()
    V1_3_1 = auto()
    V1_8_3 = auto()
    V1_8_5 = auto()
    V2_0_0 = auto()
    Unknown = auto()

    vCurrent = V1_8_5 | V2_0_0
    vMerge = V1_1_0 | V1_3_1 | V1_8_3
    vStack = V1_1_0 | V1_3_1

    def in_group(self, groups: List[GameVersion]):
        return any(self & group == self for group in groups)

    @staticmethod
    def from_str(version: str) -> GameVersion:
        match version:
            case "Version 1.1.0":
                return GameVersion.V1_1_0
            case "Version 1.3.1":
                return GameVersion.V1_3_1
            case "Version 1.8.3":
                return GameVersion.V1_8_3
            case "Version 1.8.5":
                return GameVersion.V1_8_5
            case "Version 2.0.0":
                return GameVersion.V2_0_0
        return GameVersion.Unknown


class PlayerClass(Enum):
    Gaige = auto()
    Salvador = auto()
    Axton = auto()
    Zero = auto()
    Krieg = auto()
    Maya = auto()
    Unknown = auto()

    @staticmethod
    def from_str(char_class: str) -> PlayerClass:
        match char_class:
            case "CharClass_Mechromancer":
                return PlayerClass.Gaige
            case "CharClass_Mercenary":
                return PlayerClass.Salvador
            case "CharClass_Soldier":
                return PlayerClass.Axton
            case "CharClass_Assassin":
                return PlayerClass.Zero
            case "CharClass_LilacPlayerClass":
                return PlayerClass.Krieg
            case "CharClass_Siren":
                return PlayerClass.Maya
        return PlayerClass.Unknown


class RunCategory(Enum):
    AnyPercentGaige = auto()
    AnyPercentOther = auto()
    AllQuests = auto()
    GearedSal = auto()
    Other = auto()


def get_pc() -> WillowPlayerController:
    return cast("WillowPlayerController", _get_pc())


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


def get_player_class(pc: WillowPlayerController) -> PlayerClass | None:
    if pc and pc.PlayerClass:
        return PlayerClass.from_str(pc.PlayerClass.Name)
    elif pc:
        player_standin = pc.GetPlayerStandIn(pc.PlayerReplicationInfo)
        if player_standin and player_standin.SaveGame:
            return PlayerClass.from_str(player_standin.SaveGame.PlayerClassDefinition.Name)
    return


def get_game_version() -> GameVersion:
    lan_movie: LANServerBrowserGFxMovie = cast("LANServerBrowserGFxMovie", find_object("LANServerBrowserGFxMovie", "WillowGame.Default__LANServerBrowserGFxMovie"))
    version = lan_movie.GetFriendlyGameVersionString()
    return GameVersion.from_str(version)


def get_run_category(game_version: GameVersion, player_class: PlayerClass) -> RunCategory:
    if game_version == GameVersion.V1_1_0 and player_class == PlayerClass.Gaige:
        return RunCategory.AnyPercentGaige
    if game_version == GameVersion.V1_1_0:
        return RunCategory.AnyPercentOther
    if game_version == GameVersion.V1_3_1 and player_class == PlayerClass.Gaige:
        return RunCategory.AllQuests
    if game_version in [GameVersion.V1_8_5, GameVersion.V2_0_0] and player_class == PlayerClass.Salvador:
        return RunCategory.GearedSal
    return RunCategory.Other


def get_save_dir_from_config(config_path: str) -> str:
    with open(config_path, "r") as f:
        config = json.load(f)
    return config["LocalGameSaves"]


@dataclass
class Position:
    X: float = 0
    Y: float = 0
    Z: float = 0
    Pitch: int = 0
    Yaw: int = 0
    Roll: int = 0


def get_position(PC: WillowPlayerController) -> Position:
    location = PC.Pawn.Location
    rotation = PC.Rotation
    return Position(
        location.X,
        location.Y,
        location.Z,
        rotation.Pitch,
        rotation.Yaw
    )


def apply_position(pc: WillowPlayerController, position: Position):
    location = make_struct_vector('Core.Object.Vector', True, X=position.X, Y=position.Y, Z=position.Z)
    rotation = make_struct_rotator("Core.Object.Rotator", True, Pitch=position.Pitch, Yaw=position.Yaw, Roll=0)

    _, vehicle = pc.IsUsingVehicleEx(True, None)
    if vehicle is None:
        pc.NoFailSetPawnLocation(pc.Pawn, location)
    else:
        pawn = vehicle.GetPawnToTeleport()
        pawn.Mesh.SetRBPosition(location)
        pawn.Mesh.SetRBRotation(rotation)
    pc.ClientSetRotation(rotation)


def restore_commander_position():
    pc = get_pc()
    map_name = pc.WorldInfo.GetMapName(True)
    try:
        commander_position = commander.Positions.CurrentValue.get(map_name)[commander._Position]
    except TypeError:
        commander_position = None
    if commander_position:
        position = Position(
            X=commander_position['X'],
            Y=commander_position['Y'],
            Z=commander_position['Z'],
            Pitch=commander_position['Pitch'],
            Yaw=commander_position['Yaw'],
        )
        apply_position(pc, position)
    else:
        feedback(pc.PlayerReplicationInfo, f"No saved Commander position found")

@targeted.string_message
def feedback(feedback: str) -> None:
    """Presents a "training" message to the user with the given string"""
    pc = get_pc()
    HUDMovie = pc.GetHUDMovie()
    if HUDMovie is None:
        return

    local_training_message = cast("LocalTrainingMessage", find_object("LocalTrainingMessage", "WillowGame.Default__LocalTrainingMessage"))

    duration = 3.0 * DefaultGameInfo.GameSpeed  # We will be displaying the message for three *real time* seconds.
    HUDMovie.ClearTrainingText()
    HUDMovie.AddTrainingText(
        feedback,
        "Speedrun Practice",
        duration,
        local_training_message.DefaultTrainingMessageColor,
        "",
        False,
        0,
        pc.PlayerReplicationInfo,
        True,
    )


def try_parse_int(s: str):
    try:
        return int(s)
    except ValueError:
        print(f"Unable to parse input {s}, setting value to 0")
        return 0



register_module(__name__)
