from __future__ import annotations

import os
import stat
from pathlib import Path
from typing import TYPE_CHECKING, Tuple, cast

from speedrun_practice.reloader import register_module
from speedrun_practice.skills import ExternalAttributeModifiers, HostSkillManager, Modifier
from speedrun_practice.utilities import PlayerClass, GameVersion, RunCategory, get_game_version
from speedrun_practice.utilities import Position, apply_position, feedback, get_position, get_pc
from unrealsdk import find_object, make_struct
from dataclasses import dataclass, fields

if TYPE_CHECKING:
    from bl2 import AttributeDefinition, WillowPlayerReplicationInfo, WillowWeapon, WillowPlayerController

SCALED_STATS = (
    "X", "Y", "Z", "Pitch", "Yaw", "acc_min_scale_pos", "acc_min_scale_neg", "acc_min_pre", "acc_max_scale_pos",
    "acc_max_scale_neg", "acc_max_pre", "acc_idle_scale_pos", "acc_idle_scale_neg",
    "acc_idle_pre", "crit_scale_pos", "crit_scale_neg", 'crit_pre')
ROTATION_STATS = ("Pitch", "Yaw")

PLAYER_STATS_MAP = {
    "STAT_PLAYER_ZRESERVED_DLC_INT_BZ": "anarchy_stacks",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CA": "buckup_stacks",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CB": "freeshot_stacks",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CC": "weapons",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CD": "expertise_stacks",  # NEW
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
    "STAT_PLAYER_ZRESERVED_DLC_INT_CP": "acc_min_scale_pos",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CQ": "acc_min_scale_neg",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CR": "acc_min_pre",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CS": "acc_max_scale_pos",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CT": "acc_max_scale_neg",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CU": "acc_max_pre",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CV": "acc_idle_scale_pos",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CW": "acc_idle_scale_neg",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CX": "acc_idle_pre",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CY": "crit_scale_pos",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CZ": "crit_scale_neg",
    "STAT_PLAYER_ZRESERVED_DLC_INT_DA": "crit_pre",
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
    critical_bonus: float = 0  # Not needed for saving/loading, just for logging game state
    anarchy_stacks: int = 0
    buckup_stacks: int = 0
    freeshot_stacks: int = 0
    weapons: int = 0
    expertise_stacks: int = 0
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
    # Mass duping bonuses
    crit_scale_pos: float = 0
    crit_scale_neg: float = 0
    crit_pre: float = 0
    acc_min_scale_pos: float = 0
    acc_min_scale_neg: float = 0
    acc_min_pre: float = 0
    acc_max_scale_pos: float = 0
    acc_max_scale_neg: float = 0
    acc_max_pre: float = 0
    acc_idle_scale_pos: float = 0
    acc_idle_scale_neg: float = 0
    acc_idle_pre: float = 0



    def __str__(self):

        result = f"{self.__class__.__name__}:\n"
        for field in fields(self):
            if field.name not in ['weapons','X', 'Y', 'Z', 'Pitch', 'Yaw', 'weapon1_clip', 'weapon2_clip', 'weapon3_clip', 'weapon4_clip']\
                    and field.name[:4] != 'acc_' and field.name[:5] != 'crit_':
                value = getattr(self, field.name)
                if field.name == 'freeshot_stacks' and value == -1:
                    weap = cast("WillowWeapon", get_pc().GetActiveOrBestWeapon())
                    value = weap.ShotCostBaseValue
                result += f"  {field.name}: {value}\n"
        mass_result = "\n  Mass duping bonuses (off host):\n"
        include = False
        for field in fields(self):
            if field.name[:4] == 'acc_' or field.name[:5] == 'crit_':
                value = getattr(self, field.name)
                mass_result += f"    {field.name}: {value}\n"
                if abs(value) > .0001:
                    include = True
        if include:
            result += mass_result
        return result


    @property
    def external_modifiers(self) -> ExternalAttributeModifiers:
        return ExternalAttributeModifiers(
            MinValue=Modifier(self.acc_min_scale_pos, self.acc_min_scale_neg, self.acc_min_pre),
            MaxValue=Modifier(self.acc_max_scale_pos, self.acc_max_scale_neg, self.acc_max_pre),
            OnIdleRegenerationRate=Modifier(self.acc_idle_scale_pos, self.acc_idle_scale_neg,
                                            self.acc_idle_pre),
            CurrentInstantHitCriticalHitBonus=Modifier(self.crit_scale_pos, self.crit_scale_neg, self.crit_pre)
        )

    @external_modifiers.setter
    def external_modifiers(self, ext_modifiers: ExternalAttributeModifiers) -> None:
        self.acc_min_scale_pos = round(ext_modifiers.MinValue.scale_pos, 4)
        self.acc_min_scale_neg = round(ext_modifiers.MinValue.scale_neg, 4)
        self.acc_min_pre = round(ext_modifiers.MinValue.pre_add, 4)

        self.acc_max_scale_pos = round(ext_modifiers.MaxValue.scale_pos, 4)
        self.acc_max_scale_neg = round(ext_modifiers.MaxValue.scale_neg, 4)
        self.acc_max_pre = round(ext_modifiers.MaxValue.pre_add, 4)

        self.acc_idle_scale_pos = round(ext_modifiers.OnIdleRegenerationRate.scale_pos, 4)
        self.acc_idle_scale_neg = round(ext_modifiers.OnIdleRegenerationRate.scale_neg, 4)
        self.acc_idle_pre = round(ext_modifiers.OnIdleRegenerationRate.pre_add, 4)

        self.crit_scale_pos = round(ext_modifiers.CurrentInstantHitCriticalHitBonus.scale_pos, 4)
        self.crit_scale_neg = round(ext_modifiers.CurrentInstantHitCriticalHitBonus.scale_neg, 4)
        self.crit_pre = round(ext_modifiers.CurrentInstantHitCriticalHitBonus.pre_add, 4)

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
        self.X = round(input.X, 4)
        self.Y = round(input.Y, 4)
        self.Z = round(input.Z, 4)
        self.Pitch = round(input.Pitch, 4)
        self.Yaw = round(input.Yaw, 4)


class HostGameStateManager:
    """
    Class for getting or loading game states for target players. Can only be instantiated/executed by the host, which means this should
    only be instantiated through a host.json_message network function.
    """

    def __init__(self,
                 target_pri: WillowPlayerReplicationInfo,
                 ):
        self.target_pri = target_pri
        self.target_pc = cast("WillowPlayerController", target_pri.Owner)
        self.game_version = get_game_version()
        self.player_class = PlayerClass.from_str(self.target_pc.PlayerClass.Name)
        self.host_skill_manager = HostSkillManager(target_pri)

    @property
    def clipsize_attr(self) -> AttributeDefinition:
        return cast("AttributeDefinition", find_object("AttributeDefinition", "D_Attributes.Weapon.WeaponClipSize"))

    @property
    def shotcost_attr(self) -> AttributeDefinition:
        return cast("AttributeDefinition", find_object("AttributeDefinition", "D_Attributes.Weapon.WeaponShotCost"))

    def get_game_state(self) -> GameState:
        """Get various skill stacks and weapon states for saving as player stats."""

        game_state = GameState()

        # Crit - info only
        game_state.critical_bonus = round(self.target_pc.CurrentInstantHitCriticalHitBonus, 2)

        # Buck up and anarchy
        if self.player_class == PlayerClass.Gaige:
            game_state.buckup_stacks = len(self.host_skill_manager.get_skill_definition_stacks(["Skill_ShieldBoost_Player"]))
            game_state.anarchy_stacks = int(
                self.host_skill_manager.get_designer_attribute_value("GD_Tulip_Mechromancer_Skills.Misc.Att_Anarchy_NumberOfStacks")
            )

        # Expertise
        if self.player_class == PlayerClass.Axton:
            game_state.expertise_stacks = len(self.host_skill_manager.get_skill_definition_stacks(["Expertise_MovementSpeed"]))

        # Smasher stacks
        game_state.smasher_stacks = len(self.host_skill_manager.get_skill_definition_stacks(["Skill_EvilSmasher"]))
        game_state.SMASH_stacks = len(self.host_skill_manager.get_skill_definition_stacks(["Skill_EvilSmasher_SMASH"]))

        # Free shots: -1 value implies equal to current mag whenever playing on patches that support it.
        if (len(self.host_skill_manager.get_skill_definition_stacks(["Skill_VladofHalfAmmo"])) ==
                self.target_pc.GetActiveOrBestWeapon().ShotCostBaseValue and self.game_version.in_group([GameVersion.vStack])):
            game_state.freeshot_stacks = -1
        else:
            game_state.freeshot_stacks = len(self.host_skill_manager.get_skill_definition_stacks(["Skill_VladofHalfAmmo"]))

        # Equipped weapons returned from GetEquippedWeapons as out params
        equipped_weapons: Tuple[WillowWeapon] = self.target_pc.GetPawnInventoryManager().GetEquippedWeapons(None, None, None, None)[1:]

        weapons_temp = [0, 0, 0, 0, 0]  # Active weapon slot followed by bools for merged weapons or not.
        active_weapon = cast("WillowWeapon", self.target_pc.GetActiveOrBestWeapon())
        weapons_temp[0] = active_weapon.QuickSelectSlot if active_weapon else 1
        for weapon in equipped_weapons:
            if weapon:
                clip_size = int(self.clipsize_attr.GetValue(weapon)[0])
                stored_clip_size = -1 if clip_size == int(weapon.ReloadCnt) else int(weapon.ReloadCnt)  # -1 is for full clip
                setattr(game_state, f"weapon{weapon.QuickSelectSlot}_clip", stored_clip_size)
                if len(weapon.ExternalAttributeModifiers) > 0:  # Is the weapon merged?
                    weapons_temp[weapon.QuickSelectSlot] = 1
        game_state.weapons = int("".join([str(val) for val in weapons_temp]))

        game_state.position = get_position(self.target_pc)

        # External modifiers (off host only)
        # if not self.target_pri.bIsPartyLeader:
        game_state.external_modifiers = self.host_skill_manager.get_external_attribute_modifier_totals(True)

        return game_state

    def load_game_state(self, load_state: GameState) -> None:
        """Loads the game state by applying glitches and the saved map position."""

        if load_state.X == 0 and load_state.Y == 0:
            feedback(self.target_pri, "No speedrun practice data found in current save file")
            return

        from speedrun_practice import run_category
        if run_category == RunCategory.GearedSal:
            from speedrun_practice.keybinds import _reset_gunzerk_and_weapons
            apply_position(self.target_pc, load_state.position)
            self.target_pc.MyWillowPawn.Velocity = make_struct("Vector", X=0, Y=0, Z=0)
            _reset_gunzerk_and_weapons()
            return

        gaige_msg, freeshot_msg, smasher_msg, merge_msg, expertise_msg, modifier_msg = '', '', '', '', '', ''

        # Equipped weapon and clip sizes
        inventory_manager = self.target_pc.GetPawnInventoryManager()
        weapons: Tuple[WillowWeapon] = inventory_manager.GetEquippedWeapons(None, None, None, None)[1:]
        for weapon in weapons:
            # Use drop pickups to get our desired active weapon in place
            if weapon and load_state.weapons > 0 and int(str(load_state.weapons).zfill(5)[0]) != weapon.QuickSelectSlot:
                inventory_manager.RemoveFromInventory(weapon)
                inventory_manager.AddInventory(weapon, False)
                # Merge weapon maybe
                if int(str(load_state.weapons).zfill(5)[weapon.QuickSelectSlot]) == 1:
                    weapon.ApplyAllExternalAttributeEffects()
                    if merge_msg == '':
                        merge_msg = f"\nWeapons Merged:"
                    merge_msg = merge_msg + '\n\t' + weapon.GetShortHumanReadableName()

            # Set clip sizes - only for host since it doesn't seem to work correctly on off-host.
            if weapon and self.target_pri.bIsPartyLeader:
                saved_clip = getattr(load_state, f'weapon{weapon.QuickSelectSlot}_clip')
                if saved_clip <= 0:
                    weapon.ReloadCnt = int(self.clipsize_attr.GetValue(weapon)[0])
                else:
                    weapon.ReloadCnt = saved_clip
                weapon.LastReloadCnt = weapon.ReloadCnt

        # Buck up, free shots, anarchy, smasher, and expertise. After weapon stuff so no issues with deactivations.
        if load_state.freeshot_stacks < 0:
            freeshot_stacks = int(self.shotcost_attr.GetBaseValue(self.target_pc.GetActiveOrBestWeapon())[0])
        else:
            freeshot_stacks = load_state.freeshot_stacks

        self.host_skill_manager.set_skill_stacks(freeshot_stacks, 'GD_Weap_Launchers.Skills.Skill_VladofHalfAmmo')
        if freeshot_stacks > 0:
            freeshot_msg = f"\nFree Shot Stacks: {freeshot_stacks}"

        self.host_skill_manager.set_skill_stacks(load_state.smasher_stacks, 'GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher')
        self.host_skill_manager.set_skill_stacks(load_state.SMASH_stacks, 'GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher_SMASH')
        if load_state.smasher_stacks > 0 or load_state.SMASH_stacks > 0:
            smasher_msg = f"\nSmasher Chance Stacks: {load_state.smasher_stacks}"
            smasher_msg += f"\nSmasher SMASH Stacks: {load_state.SMASH_stacks}"

        if self.player_class == PlayerClass.Gaige:
            self.host_skill_manager.set_skill_stacks(load_state.buckup_stacks, 'GD_Tulip_DeathTrap.Skills.Skill_ShieldBoost_Player')
            self.host_skill_manager.set_designer_attribute_value(load_state.anarchy_stacks,
                                                                 'GD_Tulip_Mechromancer_Skills.Misc.Att_Anarchy_NumberOfStacks')
            if load_state.buckup_stacks > 0:
                gaige_msg += f"\nBuck Up Stacks: {load_state.buckup_stacks}"
            if load_state.anarchy_stacks > 0:
                gaige_msg += f"\nAnarchy Stacks: {load_state.anarchy_stacks}"

        self.host_skill_manager.set_skill_stacks(load_state.expertise_stacks, 'GD_Soldier_Skills.Gunpowder.Expertise_MovementSpeed')
        if load_state.expertise_stacks > 0:
            expertise_msg += f"\nExpertise Stacks: {load_state.expertise_stacks}"

        # External attribute modifiers
        self.host_skill_manager.set_external_attribute_modifiers(load_state.external_modifiers)
        if (load_state.external_modifiers.CurrentInstantHitCriticalHitBonus.pre_add > 0 or
            load_state.external_modifiers.CurrentInstantHitCriticalHitBonus.scale_pos > 0):
            modifier_msg += f"\nMass duping bonus:{load_state.external_modifiers.msg()}"

        apply_position(self.target_pc, load_state.position)
        self.target_pc.MyWillowPawn.Velocity = make_struct("Vector", X=0, Y=0, Z=0)

        msg = f"Game State Loaded\n" + gaige_msg + freeshot_msg + smasher_msg + merge_msg + expertise_msg + modifier_msg
        feedback(self.target_pri, msg)


class CheckpointSaver:
    """Class for saving read only copy of the current game and saving key values as player stats. """

    def __init__(self,
                 new_save_name: str | None,
                 save_dir: str,
                 game_state: GameState | None = None
                 ):
        self.pc = get_pc()
        self.new_save_name = new_save_name
        self.save_dir = save_dir
        self.current_file_name = self.pc.GetWillowGlobals().GetWillowSaveGameManager().LastLoadedFilePath
        self.current_file_path = self.get_current_file_path()
        self.new_filename = self.get_next_open_filename()

        self.game_state = game_state

    def get_current_file_path(self) -> str:
        """Current file path based on save directory and game provided filename. Will fail if config.json not
        set correctly."""
        current_file_path = os.path.join(self.save_dir, self.current_file_name)
        if not (os.path.exists(current_file_path) and os.path.isfile(current_file_path)):
            feedback(self.pc.PlayerReplicationInfo, "Error finding current filepath")
            raise FileNotFoundError("Error finding current filepath")
        return current_file_path

    def get_next_open_filename(self) -> str:
        """Finds next available save number based on files in the save directory. Increments by 1.
        Updated to support non Save####.sav formats."""
        try:
            path_num = int(self.current_file_name[4:8])
            decimal = True
        except:
            try:
                path_num = int(self.current_file_name[4:8], 16)
                decimal = False
            except:     # Adding this for compatibility with saves mod.
                path_num = 0
                decimal = True

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

    def set_player_stats(self) -> None:
        """Sets the player stats on the pc, intent is to save game right after"""
        stats = self.pc.PlayerStats
        for stats_name, name in PLAYER_STATS_MAP.items():
            if not name:
                continue
            val = getattr(self.game_state, name)
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

    def save_checkpoint(self, overwrite=False):
        """Saves game and game state"""
        self.set_player_stats()
        if not overwrite:
            self.save_game_copy()
        else:
            self.overwrite_save()

    def touch_current_save(self):
        Path(self.get_current_file_path()).touch(exist_ok=True)


register_module(__name__)
