from __future__ import annotations

import os
import stat
from pathlib import Path
from typing import Dict, List, TYPE_CHECKING, Optional, Tuple, cast

from speedrun_practice.reloader import register_module
from speedrun_practice.skills import get_designer_attribute_value, get_skill_stacks, set_designer_attribute_value, set_skill_stacks
from speedrun_practice.text_input import TextInputBoxSRP
from speedrun_practice.utilities import PlayerClass, GameVersion
from speedrun_practice.utilities import CONFIG_PATH, Position, apply_position, feedback, get_position, get_save_dir_from_config, get_pc
from unrealsdk import find_object, make_struct
from dataclasses import dataclass

if TYPE_CHECKING:
    from bl2 import AttributeDefinition, Object, WillowWeapon, WillowPlayerController
    from speedrun_practice import SpeedrunPractice

SCALED_STATS = ("X", "Y", "Z", "Pitch", "Yaw")
ROTATION_STATS = ("Pitch", "Yaw")

PLAYER_STATS_MAP = {
    "STAT_PLAYER_ZRESERVED_DLC_INT_BZ": "anarchy_stacks",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CA": "buckup_stacks",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CB": "freeshot_stacks",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CC": "weapons",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CD": None,  # Used to have active_weapon, but deprecated.
    "STAT_PLAYER_ZRESERVED_DLC_INT_CE": "smasher_stacks",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CF": "X",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CG": "Y",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CH": "Z",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CI": "Pitch",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CJ": "Yaw",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CK": "weapon1_clip",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CL": "weapon2_clip",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CM": "weapon3_clip",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CN": "weapon4_clip",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CO": "SMASH_stacks",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CP": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CQ": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CR": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CS": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CT": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CU": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CV": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CW": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CX": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CY": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_CZ": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DA": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DB": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DC": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DD": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DE": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DF": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DG": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DH": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DI": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DJ": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DK": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DL": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DM": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DN": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DO": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DP": None,
}


@dataclass
class GameState:
    anarchy_stacks: int = 0
    buckup_stacks: int = 0
    freeshot_stacks: int = 0
    weapons: int = 0
    smasher_stacks: int = 0
    X: float = 0
    Y: float = 0
    Z: float = 0
    Pitch: int = 0
    Yaw: int = 0
    weapon1_clip: int = 0
    weapon2_clip: int = 0
    weapon3_clip: int = 0
    weapon4_clip: int = 0
    SMASH_stacks: int = 0

    @property
    def position(self) -> Position:
        return Position(
            X=self.X,
            Y=self.Y,
            Z=self.Z,
            Pitch=self.Pitch,
            Yaw=self.Yaw,
        )

    @position.setter
    def position(self, input: Position) -> None:
        self.X = input.X
        self.Y = input.Y
        self.Z = input.Z
        self.Pitch = input.Pitch
        self.Yaw = input.Yaw


class CheckpointSaver:
    """Class for saving read only copy of the current game and saving key values as player stats"""

    def __init__(self, new_save_name: str | None,
                 save_dir: str,
                 game_version: Optional[GameVersion] = None,
                 player_class: Optional[PlayerClass] = None
                 ):
        self.pc = get_pc()
        self.new_save_name = new_save_name
        self.save_dir = save_dir
        self.current_file_name = self.pc.GetWillowGlobals().GetWillowSaveGameManager().LastLoadedFilePath
        self.current_file_path = self.get_current_file_path()
        self.new_filename = self.get_next_open_filename()
        self.player_class = player_class
        self.game_version = game_version
        self.clipsize_attr: AttributeDefinition = cast("AttributeDefinition",
                                                       find_object("AttributeDefinition", "D_Attributes.Weapon.WeaponClipSize"))
        self.shotcost_attr: AttributeDefinition = cast("AttributeDefinition",
                                                       find_object("AttributeDefinition", "D_Attributes.Weapon.WeaponShotCost"))

    def get_current_file_path(self) -> str:
        """Current file path based on save directory and game provided filename. Will fail if config.json not
        set correctly."""
        current_file_path = os.path.join(self.save_dir, self.current_file_name)
        if not (os.path.exists(current_file_path) and os.path.isfile(current_file_path)):
            feedback(self.pc, "Error finding current filepath")
            raise FileNotFoundError("Error finding current filepath")
        return current_file_path

    def get_next_open_filename(self) -> str:
        """Finds next available save number based on files in the save directory. Increments by 1."""
        try:
            path_num = int(self.current_file_name[4:8])
            decimal = True
        except:
            path_num = int(self.current_file_name[4:8], 16)
            decimal = False
        while True:
            path_num = path_num + 1
            if decimal:
                filepath = "Save" + f"{path_num}".zfill(4).upper() + ".sav"
            else:
                filepath = "Save" + f"{path_num:x}".zfill(4).upper() + ".sav"
            if not os.path.exists(os.path.join(self.save_dir, filepath)):
                break
        return filepath

    def save_game_copy(self) -> None:
        current_save_name: str = self.pc.GetPlayerUINamePreference('')[1]  # Out param returned as return value
        self.pc.SetPlayerUINamePreference(self.new_save_name)
        self.pc.SaveGame(self.new_filename)
        os.chmod(os.path.join(self.save_dir, self.new_filename), stat.S_IREAD)

        self.pc.SetPlayerUINamePreference(current_save_name)
        self.pc.SaveGame(self.current_file_name)

    def overwrite_save(self) -> None:
        os.chmod(self.current_file_path, stat.S_IWRITE)
        self.pc.SaveGame(self.current_file_name)
        os.chmod(self.current_file_path, stat.S_IREAD)

    def set_player_stats(self, game_state: GameState) -> None:
        """Sets the player stats on the pc, intent is to save game right after"""
        stats = self.pc.PlayerStats
        for stats_name, name in PLAYER_STATS_MAP.items():
            if not name:
                continue
            val = getattr(game_state, name)
            if name in SCALED_STATS:
                val = int(val * 100)
            stats.SetIntStat(stats_name, val)

    def get_player_stats(self) -> GameState:
        stats = self.pc.PlayerStats
        game_state = GameState()
        for (stats_name, name) in PLAYER_STATS_MAP.items():
            val = stats.GetIntStat(stats_name)
            if name in SCALED_STATS:
                val = val / 100
            if name in ROTATION_STATS:
                val = int(val)
            if name:
                setattr(game_state, name, val)
        return game_state

    def get_game_state(self) -> GameState:
        """Get various skill stacks and weapon states for saving as player stats. No need to filter based on game version or character
        since it will just return 0 for those stats anyway."""

        game_state = GameState()

        # Buck up and anarchy
        if self.player_class == PlayerClass.Gaige:
            game_state.buckup_stacks = len(get_skill_stacks(self.pc, ["Skill_ShieldBoost_Player"]))
            game_state.anarchy_stacks = int(
                get_designer_attribute_value(self.pc, "GD_Tulip_Mechromancer_Skills.Misc.Att_Anarchy_NumberOfStacks")
            )

        # Smasher stacks
        game_state.smasher_stacks = len(get_skill_stacks(self.pc, ["Skill_EvilSmasher"]))
        game_state.SMASH_stacks = len(get_skill_stacks(self.pc, ["Skill_EvilSmasher_SMASH"]))

        # Free shots: -1 value implies equal to current mag whenever playing on patches that support it.
        if (len(get_skill_stacks(self.pc, ["Skill_VladofHalfAmmo"])) ==
                int(self.shotcost_attr.GetBaseValue(self.pc.GetActiveOrBestWeapon())[0])
                and self.game_version.in_group([GameVersion.vStack])):
            game_state.freeshot_stacks = -1
        else:
            game_state.freeshot_stacks = len(get_skill_stacks(self.pc, ["Skill_VladofHalfAmmo"]))

        # Equipped weapons returned from GetEquippedWeapons as out params
        equipped_weapons: Tuple[WillowWeapon] = self.pc.GetPawnInventoryManager().GetEquippedWeapons(None, None, None, None)[1:]

        weapons_temp = [0, 0, 0, 0, 0]  # Active weapon slot followed by bools for merged weapons or not.
        active_weapon = cast("WillowWeapon", self.pc.GetActiveOrBestWeapon())
        weapons_temp[0] = active_weapon.QuickSelectSlot
        for weapon in equipped_weapons:
            if weapon:
                clip_size = int(self.clipsize_attr.GetValue(weapon)[0])
                stored_clip_size = -1 if clip_size == int(weapon.ReloadCnt) else int(weapon.ReloadCnt)  # -1 is for full clip
                setattr(game_state, f"weapon{weapon.QuickSelectSlot}_clip", stored_clip_size)
                if len(weapon.ExternalAttributeModifiers) > 0:  # Is the weapon merged?
                    weapons_temp[weapon.QuickSelectSlot] = 1
        game_state.weapons = int("".join([str(val) for val in weapons_temp]))

        game_state.position = get_position(self.pc)
        return game_state

    def load_game_state(self) -> None:
        """Loads the game state by applying glitches and the saved map position."""
        load_state = self.get_player_stats()
        if load_state.X == 0 and load_state.Y == 0:
            feedback(self.pc, "No game state data found for this save file")
            return

        gaige_msg, freeshot_msg, smasher_msg, merge_msg = '', '', '', ''

        # Equipped weapon and clip sizes
        inventory_manager = self.pc.GetPawnInventoryManager()
        weapons: Tuple[WillowWeapon] = inventory_manager.GetEquippedWeapons(None, None, None, None)[1:]
        for weapon in weapons:
            # Use drop pickups to get our desired active weapon in place
            #TODO: Str conversion needs to pad 0s
            if weapon and load_state.weapons > 0 and int(str(load_state.weapons).zfill(5)[0]) != weapon.QuickSelectSlot:
                inventory_manager.RemoveFromInventory(weapon)
                inventory_manager.AddInventory(weapon, False)
                # Merge weapon maybe
                if int(str(load_state.weapons).zfill(5)[weapon.QuickSelectSlot]) == 1:
                    weapon.ApplyAllExternalAttributeEffects()
                    if merge_msg == '':
                        merge_msg = f"\nWeapons Merged:"
                    merge_msg = merge_msg + '\n\t' + weapon.GetShortHumanReadableName()

            # Set clip sizes
            if weapon:
                saved_clip = getattr(load_state, f'weapon{weapon.QuickSelectSlot}_clip')
                if saved_clip <= 0:
                    weapon.ReloadCnt = int(self.clipsize_attr.GetValue(weapon)[0])
                else:
                    weapon.ReloadCnt = saved_clip
                weapon.LastReloadCnt = weapon.ReloadCnt

        # Buck up, free shots, anarchy, and smasher. After weapon stuff so no issues with deactivations.
        if load_state.freeshot_stacks < 0:
            freeshot_stacks = int(self.shotcost_attr.GetBaseValue(self.pc.GetActiveOrBestWeapon())[0])
        else:
            freeshot_stacks = load_state.freeshot_stacks

        set_skill_stacks(self.pc, freeshot_stacks, 'GD_Weap_Launchers.Skills.Skill_VladofHalfAmmo')
        if freeshot_stacks > 0:
            freeshot_msg = f"\nFree Shot Stacks: {freeshot_stacks}"

        set_skill_stacks(self.pc, load_state.smasher_stacks, 'GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher')
        set_skill_stacks(self.pc, load_state.SMASH_stacks, 'GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher_SMASH')
        if load_state.smasher_stacks > 0 or load_state.SMASH_stacks > 0:
            smasher_msg = f"\nSmasher Chance Stacks: {load_state.smasher_stacks}"
            smasher_msg += f"\nSmasher SMASH Stacks: {load_state.SMASH_stacks}"

        if self.player_class == PlayerClass.Gaige:
            set_skill_stacks(self.pc, load_state.buckup_stacks, 'GD_Tulip_DeathTrap.Skills.Skill_ShieldBoost_Player')
            set_designer_attribute_value(self.pc, load_state.anarchy_stacks,
                                         'GD_Tulip_Mechromancer_Skills.Misc.Att_Anarchy_NumberOfStacks')
            gaige_msg += f"\nBuck Up Stacks: {load_state.buckup_stacks}"
            gaige_msg += f"\nAnarchy Stacks: {load_state.anarchy_stacks}"

        apply_position(self.pc, load_state.position)
        self.pc.MyWillowPawn.Velocity = make_struct("Vector", X=0, Y=0, Z=0)

        msg = f"Game State Loaded" + gaige_msg + freeshot_msg + smasher_msg + merge_msg
        feedback(self.pc, msg)

    def save_checkpoint(self, overwrite=False):
        """Saves game and game state"""
        state = self.get_game_state()
        self.set_player_stats(state)
        if not overwrite:
            self.save_game_copy()
        else:
            self.overwrite_save()

    def touch_current_save(self):
        Path(self.get_current_file_path()).touch(exist_ok=True)




def text_input_checkpoint(title: str, save_dir: str, player_class: PlayerClass, game_version: GameVersion) -> None:
    """Handle input box creation for various actions"""
    input_box = TextInputBoxSRP(title)

    def on_submit(msg: str) -> None:
        if msg:
            saver = CheckpointSaver(msg, save_dir, game_version, player_class)
            saver.save_checkpoint()

    input_box.on_submit = on_submit
    input_box.show()


register_module(__name__)
