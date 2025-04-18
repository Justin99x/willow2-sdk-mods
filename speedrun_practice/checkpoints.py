from __future__ import annotations

import stat
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

from mods_base import hook
from unrealsdk import find_object, make_struct
from unrealsdk.hooks import Type

from speedrun_practice.game_state import PLAYER_STATS_MAP, ROTATION_STATS, SCALED_STATS, GameState
from speedrun_practice.reloader import register_module
from speedrun_practice.skills import HostSkillManager
from speedrun_practice.utilities import (
    GameVersion,
    PlayerClass,
    apply_position,
    feedback,
    get_game_version,
    get_pc,
    get_position,
)

if TYPE_CHECKING:
    from bl2 import (
        AttributeDefinition,
        Object,
        WillowPlayerController,
        WillowPlayerReplicationInfo,
        WillowWeapon,
    )
    make_struct_vector = Object.Vector.make_struct
else:
    make_struct_vector = make_struct


class HostGameStateManager:
    """
    Class for getting or loading game states for target players.

    Can only be instantiated/executed by the host, which means this should
    only be instantiated through a host.json_message network function.
    """

    def __init__(
        self,
        target_pri: WillowPlayerReplicationInfo,
    ) -> None:
        self.target_pri = target_pri
        self.target_pc = cast("WillowPlayerController", target_pri.Owner)
        self.game_version = get_game_version()
        self.player_class = PlayerClass.from_str(self.target_pc.PlayerClass.Name)
        self.host_skill_manager = HostSkillManager(target_pri)

    @property
    def clipsize_attr(self) -> AttributeDefinition:  # noqa: D102
        return cast(
            "AttributeDefinition",
            find_object("AttributeDefinition", "D_Attributes.Weapon.WeaponClipSize"),
        )

    @property
    def shotcost_attr(self) -> AttributeDefinition:  # noqa: D102
        return cast(
            "AttributeDefinition",
            find_object("AttributeDefinition", "D_Attributes.Weapon.WeaponShotCost"),
        )

    def get_game_state(self) -> GameState:
        """Get various skill stacks and weapon states for saving as player stats."""

        game_state = GameState()

        # Crit - info only
        game_state.crit = round(self.target_pc.CurrentInstantHitCriticalHitBonus, 2)

        # Buck up, anarchy, and unstoppable force

        game_state.anarchy = int(
            self.host_skill_manager.get_designer_attribute_value(
                "GD_Tulip_Mechromancer_Skills.Misc.Att_Anarchy_NumberOfStacks",
            ),
        )
        game_state.buckup = len(
            self.host_skill_manager.get_skill_definition_stacks(["Skill_ShieldBoost_Player"]),
        )
        game_state.unstoppable_force = self.host_skill_manager.get_skill_stacks_by_grade(
            ["UnstoppableForce"],
        )

        # Expertise
        game_state.expertise = len(
            self.host_skill_manager.get_skill_definition_stacks(["Expertise_MovementSpeed"]),
        )

        # Smasher stacks
        game_state.smasher = len(
            self.host_skill_manager.get_skill_definition_stacks(["Skill_EvilSmasher"]),
        )
        game_state.SMASH = len(
            self.host_skill_manager.get_skill_definition_stacks(["Skill_EvilSmasher_SMASH"]),
        )

        # Free shots: -1 value implies equal to current mag whenever playing on patches that
        # support it.
        if (
            len(self.host_skill_manager.get_skill_definition_stacks(["Skill_VladofHalfAmmo"]))
            == self.target_pc.GetActiveOrBestWeapon().ShotCostBaseValue
            and self.game_version.in_group([GameVersion.v_stack])
        ):
            game_state.freeshot = -1
        else:
            game_state.freeshot = len(
                self.host_skill_manager.get_skill_definition_stacks(["Skill_VladofHalfAmmo"]),
            )

        # Equipped weapons returned from GetEquippedWeapons as out params
        equipped_weapons = cast(tuple["WillowWeapon"],
            self.target_pc.GetPawnInventoryManager().GetEquippedWeapons(None, None, None, None)[1:],
        )

        weapons_temp = [
            0,
            0,
            0,
            0,
            0,
        ]  # Active weapon slot followed by bools for merged weapons or not.
        active_weapon = cast("WillowWeapon", self.target_pc.GetActiveOrBestWeapon())
        weapons_temp[0] = active_weapon.QuickSelectSlot if active_weapon else 1
        for weapon in equipped_weapons:
            if weapon:
                clip_size = int(self.clipsize_attr.GetValue(weapon)[0])
                stored_clip_size = (
                    -1 if clip_size == int(weapon.ReloadCnt) else int(weapon.ReloadCnt)
                )  # -1 is for full clip
                setattr(game_state, f"w{weapon.QuickSelectSlot}_clip", stored_clip_size)
                if len(weapon.ExternalAttributeModifiers) > 0:  # Is the weapon merged?
                    weapons_temp[weapon.QuickSelectSlot] = 1
        game_state.weapons = int("".join([str(val) for val in weapons_temp]))

        game_state.position = get_position(self.target_pc)

        # External Modifiers
        game_state.external_modifiers = (
            self.host_skill_manager.get_external_attribute_modifier_totals(True)
        )

        # Action skill
        game_state.cooldown = self.target_pc.GetSkillCooldownTimeRemaining()
        if self.player_class == PlayerClass.Salvador:
            gunzerk_def = self.target_pc.PlayerSkillTree.GetActionSkill()
            gunzerk_skill = (
                self.host_skill_manager.skill_manager.GetActiveSkillForInstigatorByDefinition(
                    self.target_pc, gunzerk_def,
                )
            )
            if gunzerk_skill:  # Adding 1 for user input lag on saving and loading
                game_state.gunzerk = (
                    self.target_pc.GetActionSkillDuration()
                    - (self.target_pc.WorldInfo.TimeSeconds - gunzerk_skill.StartTime)
                    + 1
                )

        return game_state

    def load_game_state(self, load_state: GameState) -> None:  # noqa: C901
        """Loads the game state by applying glitches and the saved map position."""

        if load_state.X == 0 and load_state.Y == 0:
            feedback(self.target_pri, "No speedrun practice data found in current save file")
            return

        # Cancel Sal's Gunzerk, causes issues with drop reloads later
        if self.player_class == PlayerClass.Salvador:
            from speedrun_practice.keybinds import reset_gunzerk_and_weapons

            reset_gunzerk_and_weapons()

        (
            gaige_msg,
            freeshot_msg,
            smasher_msg,
            merge_msg,
            expertise_msg,
            modifier_msg,
            cooldown_msg,
        ) = "", "", "", "", "", "", ""

        # Equipped weapon and clip sizes
        inventory_manager = self.target_pc.GetPawnInventoryManager()
        weapon = cast("WillowWeapon", inventory_manager.InventoryChain)
        weapons: list[WillowWeapon] = []
        while weapon:
            weapons.append(weapon)
            weapon = cast("WillowWeapon", weapon.Inventory)

        for weapon in weapons:
            # Use drop pickups to get our desired active weapon in place instantly
            if (
                weapon
                and load_state.weapons > 0
                and int(str(load_state.weapons).zfill(5)[0]) != weapon.QuickSelectSlot
            ):
                inventory_manager.RemoveFromInventory(weapon)
                inventory_manager.AddInventory(weapon, False)
        # Now we've messed up drop order, so we're going to reset our InventoryChain to what it was
        # previously
        inventory_manager.InventoryChain = None
        for i in range(len(weapons)):
            if i == 0:
                inventory_manager.InventoryChain = weapons[i]
            else:
                weapons[i - 1].Inventory = weapons[i]
                weapons[i].Inventory = None

        # Remaining gunzerk duration
        # Doing this here so that we get gunzerk started up before setting up ammo in clips
        if load_state.gunzerk > 0 and self.player_class == PlayerClass.Salvador:
            self.target_pc.StartActionSkill()

            # Dumb hack to wait a tick so that GetActionSkillDuration() returns the right value.
            @hook("WillowGame.WillowGameViewportClient:Tick", Type.POST, immediately_enable=True)
            def wait_tick_gunzerk(*_: Any) -> None:
                gunzerk_duration = self.target_pc.GetActionSkillDuration()
                gunzerk_def = self.target_pc.PlayerSkillTree.GetActionSkill()
                gunzerk_skill = (
                    self.host_skill_manager.skill_manager.GetActiveSkillForInstigatorByDefinition(
                        self.target_pc, gunzerk_def,
                    )
                )
                gunzerk_skill.StartTime = self.target_pc.WorldInfo.TimeSeconds - (
                    gunzerk_duration - load_state.gunzerk
                )

                wait_tick_gunzerk.disable()

        for weapon in weapons:
            # Set clip sizes - only for host since it doesn't seem to work correctly on off-host.
            if weapon and self.target_pri.bIsPartyLeader:
                saved_clip = getattr(load_state, f"w{weapon.QuickSelectSlot}_clip")
                if saved_clip <= 0:
                    weapon.ReloadCnt = int(self.clipsize_attr.GetValue(weapon)[0])
                else:
                    weapon.ReloadCnt = saved_clip
                weapon.LastReloadCnt = weapon.ReloadCnt

            # Merge weapon maybe
            if int(str(load_state.weapons).zfill(5)[weapon.QuickSelectSlot]) == 1:
                weapon.ApplyAllExternalAttributeEffects()
                if merge_msg == "":
                    merge_msg = "\nWeapons Merged:"
                merge_msg = merge_msg + "\n\t" + weapon.GetShortHumanReadableName()

        # Buck up, free shots, anarchy, smasher, and expertise. After weapon stuff so no issues with
        # deactivations.
        if load_state.freeshot < 0:
            freeshot_stacks = int(
                self.shotcost_attr.GetBaseValue(self.target_pc.GetActiveOrBestWeapon())[0],
            )
        else:
            freeshot_stacks = load_state.freeshot

        self.host_skill_manager.set_skill_stacks(
            freeshot_stacks, "GD_Weap_Launchers.Skills.Skill_VladofHalfAmmo",
        )
        if freeshot_stacks > 0:
            freeshot_msg = f"\nFree Shot Stacks: {freeshot_stacks}"

        self.host_skill_manager.set_skill_stacks(
            load_state.smasher, "GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher",
        )
        self.host_skill_manager.set_skill_stacks(
            load_state.SMASH, "GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher_SMASH",
        )
        if load_state.smasher > 0 or load_state.SMASH > 0:
            smasher_msg = f"\nSmasher Chance Stacks: {load_state.smasher}"
            smasher_msg += f"\nSmasher SMASH Stacks: {load_state.SMASH}"

        self.host_skill_manager.set_designer_attribute_value(
            load_state.anarchy, "GD_Tulip_Mechromancer_Skills.Misc.Att_Anarchy_NumberOfStacks",
        )

        self.host_skill_manager.set_skill_stacks(
            load_state.buckup, "GD_Tulip_DeathTrap.Skills.Skill_ShieldBoost_Player",
        )
        self.host_skill_manager.set_skill_stacks_by_grade(
            load_state.unstoppable_force,
            "GD_Tulip_Mechromancer_Skills.BestFriendsForever.UnstoppableForce",
        )
        if load_state.buckup > 0:
            gaige_msg += f"\nBuck Up Stacks: {load_state.buckup}"
        if load_state.anarchy > 0:
            gaige_msg += f"\nAnarchy Stacks: {load_state.anarchy}"
        if load_state.un_force > 0:
            gaige_msg += f"{load_state.unstoppable_force_str()}"

        self.host_skill_manager.set_skill_stacks(
            load_state.expertise, "GD_Soldier_Skills.Gunpowder.Expertise_MovementSpeed",
        )
        if load_state.expertise > 0:
            expertise_msg += f"\nExpertise Stacks: {load_state.expertise}"

        # External attribute modifiers
        self.host_skill_manager.set_external_attribute_modifiers(load_state.external_modifiers)
        if (
            load_state.external_modifiers.CurrentInstantHitCriticalHitBonus.pre_add > 0
            or load_state.external_modifiers.CurrentInstantHitCriticalHitBonus.scale_pos > 0
        ):
            modifier_msg += f"\nMass duping bonus:{load_state.external_modifiers.msg()}"

        apply_position(self.target_pc, load_state.position)
        self.target_pc.MyWillowPawn.Velocity = make_struct_vector("Vector", X=0, Y=0, Z=0)

        # Action Skill Cooldown
        if self.target_pc.IsResourcePoolValid(self.target_pc.SkillCooldownPool):
            self.target_pc.SkillCooldownPool.Data.SetCurrentValue(load_state.cooldown)
            if load_state.cooldown > 0:
                cooldown_msg = f"\nCooldown Remaining: {load_state.cooldown}"

        msg = (
            "Game State Loaded\n"
            + gaige_msg
            + freeshot_msg
            + smasher_msg
            + expertise_msg
            + cooldown_msg
            + merge_msg
            + modifier_msg
        )
        feedback(self.target_pri, msg)


class CheckpointSaver:
    """Class for saving read only copy of the current game and saving key values as player stats."""

    def __init__(
        self, new_save_name: str | None, save_dir: str, game_state: GameState | None = None,
    ) -> None:
        self.pc = get_pc()
        self.new_save_name = new_save_name
        self.save_dir = save_dir
        self.current_file_name = (
            self.pc.GetWillowGlobals().GetWillowSaveGameManager().LastLoadedFilePath
        )
        self.current_file_path = self.get_current_file_path()
        self.new_filename = self.get_next_open_filename()

        self.game_state = game_state

    def get_current_file_path(self) -> str:
        """
        Current file path based on save directory and game provided filename.

        Will fail if config.json not set correctly.
        """
        current_file_path = Path(self.save_dir) / self.current_file_name
        if not current_file_path.exists() and current_file_path.is_file():
            feedback(self.pc.PlayerReplicationInfo, "Error finding current filepath")
            raise FileNotFoundError("Error finding current filepath")
        return str(current_file_path)

    def get_next_open_filename(self) -> str:
        """
        Finds next available save number based on files in the save directory.

        Increments by 1. Updated to support non Save####.sav formats.
        """
        try:
            path_num = int(self.current_file_name[4:8])
            decimal = True
        except:  # noqa: E722
            try:
                path_num = int(self.current_file_name[4:8], 16)
                decimal = False
            except:  # Adding this for compatibility with saves mod.  # noqa: E722
                path_num = 0
                decimal = True

        while True:
            path_num = path_num + 1
            if decimal:
                filepath = "Save" + f"{path_num}".zfill(4).upper() + ".sav"
            else:
                filepath = "Save" + f"{path_num:x}".zfill(4).upper() + ".sav"
            if not (Path(self.save_dir) / filepath).exists():
                break
        return filepath

    def save_game_copy(self) -> None:
        """Saves a new copy of the game."""
        # Out param returned as return value
        current_save_name: str = self.pc.GetPlayerUINamePreference("")[1]
        if not self.new_save_name:
            raise ValueError("New save name not set.")
        self.pc.SetPlayerUINamePreference(self.new_save_name)
        self.pc.SaveGame(self.new_filename)
        (Path(self.save_dir) / self.new_filename).chmod(stat.S_IREAD)

        self.pc.SetPlayerUINamePreference(current_save_name)
        self.pc.SaveGame(self.current_file_name)

    def overwrite_save(self) -> None:
        """Overwrites current save with new checkpoint."""
        Path(self.current_file_path).chmod(stat.S_IWRITE)
        self.pc.SaveGame(self.current_file_name)
        Path(self.current_file_path).chmod(stat.S_IREAD)

    def set_player_stats(self) -> None:
        """Sets the player stats on the pc, intent is to save game right after."""
        stats = self.pc.PlayerStats
        for stats_name, name in PLAYER_STATS_MAP.items():
            if not name:
                continue
            val = getattr(self.game_state, name)
            if name in SCALED_STATS:
                val = int(val * 100)
            stats.SetIntStat(stats_name, val)

    def get_player_stats(self) -> GameState:
        """Get current player stats from pc."""
        stats = self.pc.PlayerStats
        game_state = GameState()
        for stats_name, name in PLAYER_STATS_MAP.items():
            val = stats.GetIntStat(stats_name)
            if name in SCALED_STATS:
                val = val / 100
            if name in ROTATION_STATS:
                val = int(val)
            if name:
                setattr(game_state, name, val)
        return game_state

    def save_checkpoint(self, overwrite: bool=False) -> None:
        """Saves game and game state."""
        self.set_player_stats()
        if not overwrite:
            self.save_game_copy()
        else:
            self.overwrite_save()

    def touch_current_save(self) -> None:
        """Touch current save so that it moves to top of list in game."""
        Path(self.get_current_file_path()).touch(exist_ok=True)


register_module(__name__)
