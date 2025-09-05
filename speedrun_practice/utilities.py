from __future__ import annotations

import ctypes
from dataclasses import dataclass
from enum import Enum, Flag, auto
from pathlib import Path
from typing import TYPE_CHECKING, cast

from legacy_compat import legacy_compat
from mods_base import MODS_DIR
from mods_base import get_pc as _get_pc
from networking import targeted
from unrealsdk import find_object, make_struct

from speedrun_practice.reloader import register_module

if TYPE_CHECKING:
    from bl2 import (
        LANServerBrowserGFxMovie,
        LocalTrainingMessage,
        Object,
        WillowCoopGameInfo,
        WillowHUDGFxMovie,
        WillowPlayerController,
    )

    make_struct_vector = Object.Vector.make_struct
    make_struct_rotator = Object.Rotator.make_struct
else:
    make_struct_vector = make_struct_rotator = make_struct

DefaultGameInfo: WillowCoopGameInfo = cast(
    "WillowCoopGameInfo",
    find_object("WillowCoopGameInfo", "WillowGame.Default__WillowCoopGameInfo"),
)
MODDIR = Path(MODS_DIR) / "speedrun_practice"
CONFIG_PATH = Path(MODDIR) / "config.json"


class GameVersion(Flag):
    V1_1_0 = auto()
    V1_3_1 = auto()
    V1_8_3 = auto()
    V1_8_5 = auto()
    V2_0_0 = auto()
    Unknown = auto()

    v_current = V1_8_5 | V2_0_0
    v_merge = V1_1_0 | V1_3_1 | V1_8_3
    v_stack = V1_1_0 | V1_3_1

    def in_group(self, groups: list[GameVersion]) -> bool:
        """Check if a game version is in a group of versions."""
        return any(self & group == self for group in groups)

    @staticmethod
    def from_str(version: str) -> GameVersion:
        """Create a GameVersion instance from a string version number."""
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
            case _:
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
        """Create PlayerClass instance from string player class."""
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
            case _:
                return PlayerClass.Unknown


class RunCategory(Enum):
    AnyPercentGaige = auto()
    AnyPercentOther = auto()
    AllQuests = auto()
    GearedSal = auto()
    Other = auto()
    Unknown = auto()


def get_pc() -> WillowPlayerController:
    """Get current player controller with type WillowPlayerController."""
    return cast("WillowPlayerController", _get_pc())


def find_object_safe(cls: str, path: str) -> object | None:
    """Safely find object with handling of ValueError."""
    try:
        obj = find_object(cls, path)
    except ValueError:
        print(f"Could not find object {path}. Is the right character loaded?")
        return None
    return obj


def extract_user_save_path() -> str:
    """Extracts the absolute path where user's save files are stored."""

    game_str = "Borderlands 2"
    if not game_str:
        print("Could not locate save folder!")
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


def get_player_class(pc: WillowPlayerController) -> PlayerClass | None:
    """Get player class of current player controller."""
    if pc and pc.PlayerClass:
        return PlayerClass.from_str(pc.PlayerClass.Name)
    if pc:
        player_standin = pc.GetPlayerStandIn(pc.PlayerReplicationInfo)
        if player_standin and player_standin.SaveGame:
            return PlayerClass.from_str(player_standin.SaveGame.PlayerClassDefinition.Name)
    return None


def get_game_version() -> GameVersion:
    """Get current game version."""
    lan_movie: LANServerBrowserGFxMovie = cast(
        "LANServerBrowserGFxMovie",
        find_object("LANServerBrowserGFxMovie", "WillowGame.Default__LANServerBrowserGFxMovie"),
    )
    version = lan_movie.GetFriendlyGameVersionString()
    return GameVersion.from_str(version)


def get_run_category(game_version: GameVersion, player_class: PlayerClass) -> RunCategory:
    """Get inferred speedrun category based on character and game version."""
    if game_version == GameVersion.V1_1_0 and player_class == PlayerClass.Gaige:
        return RunCategory.AnyPercentGaige
    if game_version == GameVersion.V1_1_0:
        return RunCategory.AnyPercentOther
    if game_version == GameVersion.V1_3_1 and player_class == PlayerClass.Gaige:
        return RunCategory.AllQuests
    if (
        game_version in [GameVersion.V1_8_5, GameVersion.V2_0_0]
        and player_class == PlayerClass.Salvador
    ):
        return RunCategory.GearedSal
    return RunCategory.Other


@dataclass
class Position:
    X: float = 0
    Y: float = 0
    Z: float = 0
    Pitch: int = 0
    Yaw: int = 0
    Roll: int = 0


def get_position(pc: WillowPlayerController) -> Position:
    """Get current map position."""
    location = pc.Pawn.Location
    rotation = pc.Rotation
    return Position(location.X, location.Y, location.Z, rotation.Pitch, rotation.Yaw)


def apply_position(pc: WillowPlayerController, position: Position) -> None:
    """Move a player to the desired map position."""
    location = make_struct_vector(
        "Vector", X=position.X, Y=position.Y, Z=position.Z,
    )
    rotation = make_struct_rotator(
        "Rotator", Pitch=position.Pitch, Yaw=position.Yaw, Roll=0,
    )

    _, vehicle = pc.IsUsingVehicleEx(True, None)
    if vehicle is None:
        pc.NoFailSetPawnLocation(pc.Pawn, location)
    else:
        pawn = vehicle.GetPawnToTeleport()
        pawn.Mesh.SetRBPosition(location)
        pawn.Mesh.SetRBRotation(rotation)
    pc.ClientSetRotation(rotation)


def restore_commander_position() -> None:
    """Move player to currently active commander position."""
    # Support legacy and new implementation of Commander
    pc = get_pc()

    try:
        from Commander import saved_positions
        if position := saved_positions[10]:
            position.teleport_player_pc()
        else:
            feedback(pc.PlayerReplicationInfo, "No saved Commander position found")

    except ImportError:
        with legacy_compat():
            import Mods.Commander.Builtin as Commander  # type: ignore
        map_name = pc.WorldInfo.GetMapName(True)

        try:
            commander_position = Commander.Positions.CurrentValue.get(map_name)[Commander._Position] # type: ignore
        except TypeError:
            commander_position = None
        if commander_position:
            commander_position = cast(dict[str,float], commander_position)
            position = Position(
                X=commander_position["X"],
                Y=commander_position["Y"],
                Z=commander_position["Z"],
                Pitch=int(commander_position["Pitch"]),
                Yaw=int(commander_position["Yaw"]),
            )
            apply_position(pc, position)
        else:
            feedback(pc.PlayerReplicationInfo, "No saved Commander position found")


@targeted.string_message
def feedback(feedback: str) -> None:
    """Presents a "training" message to the user with the given string."""
    pc = get_pc()
    hud_movie = cast("WillowHUDGFxMovie | None", pc.GetHUDMovie())
    if hud_movie is None:
        return

    local_training_message = cast(
        "LocalTrainingMessage",
        find_object("LocalTrainingMessage", "WillowGame.Default__LocalTrainingMessage"),
    )

    duration = (
        3.0 * DefaultGameInfo.GameSpeed
    )  # We will be displaying the message for three *real time* seconds.
    hud_movie.ClearTrainingText()
    hud_movie.AddTrainingText(
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


def try_parse_int(s: str) -> int:
    """Try to parse string as int, return 0 otherwise."""
    try:
        return int(s)
    except ValueError:
        print(f"Unable to parse input {s}, setting value to 0")
        return 0

register_module(__name__)
