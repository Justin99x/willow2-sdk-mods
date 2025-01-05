from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Callable, List, TYPE_CHECKING, cast

from mods_base import KeybindType
from speedrun_practice.checkpoints import CheckpointSaver, request_load_checkpoint, request_save_checkpoint, text_input_checkpoint
from speedrun_practice.gear import GearRandomizer
from speedrun_practice.options import SPOptions
from speedrun_practice.reloader import register_module
from speedrun_practice.skills import request_set_designer_attribute_value, request_set_skill_stacks, \
    request_trigger_kill_skills, text_input_stacks
from speedrun_practice.utilities import GameVersion, PlayerClass, RunCategory, feedback, get_pc, restore_commander_position
from unrealsdk import find_all, find_enum, make_struct
from unrealsdk.hooks import Block

type KeybindBlockSignal = None | Block | type[Block]
type KeybindCallback_NoArgs = Callable[[], KeybindBlockSignal]

if TYPE_CHECKING:
    from bl2 import Object, WillowDeclarations, WillowWeapon


@dataclass
class SPKeybind(KeybindType):
    order: int = 100
    sp_callback: KeybindCallback_NoArgs | None = None


class SPKeybinds:

    def __init__(self, options: SPOptions):
        self.options = options
        self.game_version: GameVersion | None = None
        self.player_class: PlayerClass | None = None
        self.run_category: RunCategory | None = None
        self.host: bool = True

        self.buckup = SPKeybind("Set Buckup Stacks", "None", sp_callback=set_buckup_stacks, is_hidden=True, order=1)
        self.anarchy = SPKeybind("Set Anarchy Stacks", "None", sp_callback=set_anarchy_stacks, is_hidden=True, order=2)

        self.free_shot_stacks = SPKeybind("Set Free Shot Stacks", "None", sp_callback=set_free_shot_stacks, is_hidden=True, order=10)
        self.smasher_chance_stacks = SPKeybind("Set Smasher Chance Stacks", "None", sp_callback=set_smasher_chance_stacks, is_hidden=True,
                                               order=11)
        self.smasher_SMASH_stacks = SPKeybind("Set Smasher SMASH Stacks", "None", sp_callback=set_smasher_SMASH_stacks, is_hidden=True,
                                              order=12)
        self.merge_weapons = SPKeybind("Merge Equipped Weapons", "None", sp_callback=merge_all_equipped_weapons, is_hidden=True, order=13)
        self.randomize_gear = SPKeybind("Randomize Any% Gear", "None", sp_callback=randomize_any_p_gear, is_hidden=True, order=14)

        self.reset_gunzerk = SPKeybind("Reset Gunzerk and Weapons", "None", sp_callback=reset_gunzerk_and_weapons, is_hidden=True, order=30)
        self.reset_and_trigger = SPKeybind("Reset to Commander Position and Trigger Skills", "None",
                                         sp_callback=self.reset_to_position_and_trigger_skills,
                                         is_hidden=True, order=31)

        self.save_checkpoint = SPKeybind("Save New Checkpoint", "None", sp_callback=self.save_checkpoint, order=40)
        self.overwrite_checkpoint = SPKeybind("Save Current Checkpoint", "None", sp_callback=self.overwrite_save, order=41)
        self.load_checkpoint = SPKeybind("Load Checkpoint State", "None", sp_callback=self.load_checkpoint, order=42)
        self.touch_save = SPKeybind("Move Current Save to Top", "None", sp_callback=self.touch_file, order=43)

    @property
    def keybinds(self) -> List[SPKeybind]:
        return [self.buckup, self.anarchy, self.free_shot_stacks, self.smasher_chance_stacks, self.smasher_SMASH_stacks, self.merge_weapons,
                self.randomize_gear, self.reset_gunzerk, self.reset_and_trigger, self.save_checkpoint, self.overwrite_checkpoint,
                self.load_checkpoint, self.touch_save]

    def enable(self, game_version: GameVersion, player_class: PlayerClass, run_category: RunCategory):
        self.game_version = game_version
        self.player_class = player_class
        self.run_category = run_category

        self._enable_keybinds([self.save_checkpoint,self.overwrite_checkpoint, self.load_checkpoint, self.touch_save])

        if self.player_class == PlayerClass.Gaige:
            self._enable_keybinds([self.buckup, self.anarchy])
            if self.run_category == RunCategory.AnyPercentGaige and self.host:
                self._enable_keybinds([self.randomize_gear])

        if self.game_version.in_group([GameVersion.vMerge]):
            self._enable_keybinds([self.free_shot_stacks])
            if self.host:
                self._enable_keybinds([self.merge_weapons])

        if self.game_version.in_group([GameVersion.vStack]):
            self._enable_keybinds([self.smasher_chance_stacks, self.smasher_SMASH_stacks])

        if self.run_category == RunCategory.GearedSal and self.host:
            self._enable_keybinds([self.reset_gunzerk, self.reset_and_trigger])

    def disable(self):
        self.player_class = None
        self.run_category = None
        self._disable_keybinds(self.keybinds)

    def _enable_keybinds(self, keybinds: List[SPKeybind]):
        for kb in keybinds:
            kb.is_hidden = False
            kb.callback = kb.sp_callback
            kb.enable()
            kb.is_enabled = True

    def _disable_keybinds(self, keybinds: List[SPKeybind]):
        for kb in keybinds:
            kb.is_hidden = True
            kb.callback = None
            if kb.is_enabled:
                kb.disable()
                kb.is_enabled = False

    def reset_to_position_and_trigger_skills(self) -> None:
        pc = get_pc()
        reset_gunzerk_and_weapons()
        restore_commander_position()
        pc.Pawn.Velocity: Object.Vector = make_struct("Vector", X=0, Y=0, Z=0)
        if self.options.incite.value:
            request_set_skill_stacks(pc, 1, 'GD_Mercenary_Skills.Brawn.Incite_Active')
        if self.options.locked_and_loaded.value:
            request_set_skill_stacks(pc, 1, 'GD_Mercenary_Skills.Gun_Lust.LockedAndLoaded_Active')
        if self.options.kill_skills.value:
            request_trigger_kill_skills(pc)

    def save_checkpoint(self):
        text_input_checkpoint("Character Save Name")

    def overwrite_save(self):
        request_save_checkpoint('', True)

    def load_checkpoint(self):
        saver = CheckpointSaver(None, self.options.save_game_path.value)
        state_to_load = saver.get_player_stats()
        request_load_checkpoint(asdict(state_to_load))


    def touch_file(self):
        saver = CheckpointSaver(None, self.options.save_game_path.value)
        saver.touch_current_save()


def merge_all_equipped_weapons() -> None:
    """Applies external attribute effects from all weapons currently equipped. Used for crit bonus in runs."""
    pc = get_pc()
    weapons = pc.GetPawnInventoryManager().GetEquippedWeapons(None, None, None, None)[1:]
    msg = ''
    for weapon in weapons:
        if weapon:
            weapon.ApplyAllExternalAttributeEffects()
            msg = msg + '\n' + weapon.GetShortHumanReadableName()
    feedback(pc.PlayerReplicationInfo, f"Bonuses from the following weapons are applied: {msg}")


def set_free_shot_stacks():
    text_input_stacks(request_set_skill_stacks, "Set Free Shot Stacks", "GD_Weap_Launchers.Skills.Skill_VladofHalfAmmo")


def set_smasher_chance_stacks():
    text_input_stacks(request_set_skill_stacks, "Set Smasher Chance Stacks", "GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher")


def set_smasher_SMASH_stacks():
    text_input_stacks(request_set_skill_stacks, "Set Smasher SMASH Stacks", "GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher_SMASH")


def randomize_any_p_gear():
    gear_r = GearRandomizer()
    gear_r.randomize_gear()


def reset_gunzerk_and_weapons():
    pc = get_pc()
    ammo_pools = cast(List["AmmoResourcePool"], find_all('AmmoResourcePool'))
    for pool in ammo_pools:
        if pool.Definition:
            if pool.Definition.Resource.ResourceName == 'Rockets':
                pool.SetCurrentValue(pool.GetMaxValue())

    def _drop_pickup_weapon(weapon):
        inventory_manager.RemoveFromInventory(weapon)
        inventory_manager.AddInventory(weapon, True)

    pc.ResetSkillCooldown()

    inventory_manager = pc.GetPawnInventoryManager()
    weapons: List[WillowWeapon] = inventory_manager.GetEquippedWeapons(None, None, None, None)[1:]
    weapons_by_slot = {int(weapon.QuickSelectSlot): weapon for weapon in weapons if weapon}

    # Canceling gunzerk like this because using a func directly crashes the game sometimes
    for slot in [1, 2, 3, 4]:  # Cancel gunzerk
        if weapons_by_slot.get(slot):
            inventory_manager.RemoveFromInventory(weapons_by_slot[slot])
    for slot in [1, 2, 3, 4]:  # Add weapons back in
        if weapons_by_slot.get(slot):
            inventory_manager.AddInventory(weapons_by_slot[slot], False)
    for slot in [3, 4, 1, 2]:
        if weapons_by_slot.get(slot):
            _drop_pickup_weapon(weapons_by_slot[slot])
    e_quick_weapon_slot: WillowDeclarations.EQuickWeaponSlot = find_enum('EQuickWeaponSlot')
    pc.EquipWeaponFromSlot(e_quick_weapon_slot.QuickSelectLeft)


def set_buckup_stacks():
    text_input_stacks(request_set_skill_stacks, "Set Buckup Stacks", "GD_Tulip_DeathTrap.Skills.Skill_ShieldBoost_Player")


def set_anarchy_stacks():
    text_input_stacks(request_set_designer_attribute_value, "Set Anarchy Stacks",
                      "GD_Tulip_Mechromancer_Skills.Misc.Att_Anarchy_NumberOfStacks")





register_module(__name__)
