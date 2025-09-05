from __future__ import annotations

from collections.abc import Callable
from dataclasses import asdict
from typing import TYPE_CHECKING, cast

from mods_base import KeybindType, keybind
from unrealsdk import find_all, find_enum, make_struct
from unrealsdk.hooks import Block

from speedrun_practice.checkpoints import CheckpointSaver
from speedrun_practice.gear import GearRandomizer
from speedrun_practice.network_funcs import (
    request_game_state,
    request_load_checkpoint,
    request_save_checkpoint,
    request_set_designer_attribute_value,
    request_set_skill_stacks,
    request_trigger_kill_skills,
)
from speedrun_practice.options import incite, kill_skills, locked_and_loaded
from speedrun_practice.reloader import register_module
from speedrun_practice.text_input import TextInputBoxSRP
from speedrun_practice.utilities import (
    RunCategory,
    feedback,
    get_pc,
    restore_commander_position,
    try_parse_int,
)

type KeybindBlockSignal = None | Block | type[Block]
type KeybindCallback_NoArgs = Callable[[], KeybindBlockSignal]

if TYPE_CHECKING:
    from bl2 import AmmoResourcePool, Inventory, Object, WillowDeclarations, WillowWeapon

    make_struct_vector = Object.Vector.make_struct
    find_enum_quick_weapon_slot = WillowDeclarations.EQuickWeaponSlot.find_enum
else:
    make_struct_vector = make_struct
    find_enum_quick_weapon_slot = find_enum

active_keybinds: list[KeybindType] = []
host: bool = True


def text_input_stacks(func: Callable[[int, str], None], title: str, path: str = "") -> None:
    """Handle input box creation for various actions."""
    input_box = TextInputBoxSRP(title)

    def on_submit(msg: str) -> None:
        if msg:
            target_val = try_parse_int(msg)
            if target_val >= 0:
                func(target_val, path)
            else:
                print("Value must be greater than 0")

    input_box.on_submit = on_submit
    input_box.show()


@keybind("Set Unstoppable Force Stacks")
def set_uf_stacks() -> None:  # noqa: D103
    text_input_stacks(
        request_set_skill_stacks,
        "Set Unstoppable Force Stacks",
        "GD_Tulip_Mechromancer_Skills.BestFriendsForever.UnstoppableForce",
    )


@keybind("Set Buckup Stacks")
def set_buckup_stacks() -> None:  # noqa: D103
    text_input_stacks(
        request_set_skill_stacks,
        "Set Buckup Stacks",
        "GD_Tulip_DeathTrap.Skills.Skill_ShieldBoost_Player",
    )


@keybind("Set Anarchy Stacks")
def set_anarchy_stacks() -> None:  # noqa: D103
    text_input_stacks(
        request_set_designer_attribute_value,
        "Set Anarchy Stacks",
        "GD_Tulip_Mechromancer_Skills.Misc.Att_Anarchy_NumberOfStacks",
    )


@keybind("Set Expertise Stacks")
def set_expertise_stacks() -> None:  # noqa: D103
    text_input_stacks(
        request_set_skill_stacks,
        "Set Expertise Stacks",
        "GD_Soldier_Skills.Gunpowder.Expertise_MovementSpeed",
    )


@keybind("Set Free Shot Stacks")
def set_free_shot_stacks() -> None:  # noqa: D103
    text_input_stacks(
        request_set_skill_stacks,
        "Set Free Shot Stacks",
        "GD_Weap_Launchers.Skills.Skill_VladofHalfAmmo",
    )


@keybind("Set Smasher Chance Stacks")
def set_smasher_chance_stacks() -> None:  # noqa: D103
    text_input_stacks(
        request_set_skill_stacks,
        "Set Smasher Chance Stacks",
        "GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher",
    )


@keybind("Set Smasher SMASH stacks")
def set_smasher_SMASH_stacks() -> None:  # noqa: D103, N802
    text_input_stacks(
        request_set_skill_stacks,
        "Set Smasher SMASH Stacks",
        "GD_Weap_AssaultRifle.Skills.Skill_EvilSmasher_SMASH",
    )


@keybind("Merge Equipped Weapons")
def merge_all_equipped_weapons() -> None:
    """Applies external attribute effects from all weapons currently equipped."""
    pc = get_pc()
    weapons = pc.GetPawnInventoryManager().GetEquippedWeapons(None, None, None, None)[1:]
    msg = ""
    for weapon in weapons:
        if weapon:
            weapon.ApplyAllExternalAttributeEffects()
            msg = msg + "\n" + weapon.GetShortHumanReadableName()
    feedback(pc.PlayerReplicationInfo, f"Bonuses from the following weapons are applied: {msg}")


@keybind("Randomize Any% Gear")
def randomize_any_p_gear() -> None:  # noqa: D103
    from speedrun_practice import run_category
    if run_category == RunCategory.AnyPercentGaige:
        gear_r = GearRandomizer()
        gear_r.randomize_gear()


@keybind("Reset Gunzerk and Weapons")
def reset_gunzerk_and_weapons_kb() -> None:  # noqa: D103
    reset_gunzerk_and_weapons()


def reset_gunzerk_and_weapons() -> None:
    """Reset gunzerk, weapon drop order, and ammo."""
    pc = get_pc()
    ammo_pools = cast(list["AmmoResourcePool"], find_all("AmmoResourcePool"))
    for pool in ammo_pools:
        if pool.Definition and pool.Definition.Resource.ResourceName == "Rockets":
            pool.SetCurrentValue(pool.GetMaxValue())

    def _drop_pickup_weapon(weapon: Inventory) -> None:
        inventory_manager.RemoveFromInventory(weapon)
        inventory_manager.AddInventory(weapon, True)

    inventory_manager = pc.GetPawnInventoryManager()
    weapons = cast(
        list["WillowWeapon"], inventory_manager.GetEquippedWeapons(None, None, None, None)[1:],
    )
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

    e_quick_weapon_slot = find_enum_quick_weapon_slot("EQuickWeaponSlot")
    pc.EquipWeaponFromSlot(e_quick_weapon_slot.QuickSelectLeft)
    pc.ResetSkillCooldown()


@keybind("Reset to Commander Position and Trigger Skills")
def reset_to_position_and_trigger_skills() -> None:  # noqa: D103
    pc = get_pc()
    reset_gunzerk_and_weapons()
    restore_commander_position()
    pc.Pawn.Velocity = make_struct_vector("Vector", X=0, Y=0, Z=0)
    if incite.value:
        request_set_skill_stacks(1, "GD_Mercenary_Skills.Brawn.Incite_Active")
    if locked_and_loaded.value:
        request_set_skill_stacks(1, "GD_Mercenary_Skills.Gun_Lust.LockedAndLoaded_Active")
    if kill_skills.value:
        request_trigger_kill_skills()


@keybind("Log Current Stats")
def log_current_state() -> None:  # noqa: D103
    request_game_state()


@keybind("Save New Checkpoint")
def save_checkpoint() -> None:
    """Open text input box and save a new checkpoint based on user input."""
    input_box = TextInputBoxSRP("Character Save Name")

    def on_submit(msg: str) -> None:
        if msg:
            request_save_checkpoint(msg, False)

    input_box.on_submit = on_submit
    input_box.show()


@keybind("Overwrite Current Save")
def overwrite_save() -> None:  # noqa: D103
    request_save_checkpoint("", True)


@keybind("Load Checkpoint State")
def load_checkpoint() -> None:  # noqa: D103
    from speedrun_practice.options import save_game_path

    saver = CheckpointSaver(None, save_game_path.value)
    state_to_load = saver.get_player_stats()
    request_load_checkpoint(asdict(state_to_load))


@keybind("Move Current Save to Top")
def touch_file() -> None:  # noqa: D103
    from speedrun_practice.options import save_game_path

    saver = CheckpointSaver(None, save_game_path.value)
    saver.touch_current_save()


all_keybinds = [
    set_buckup_stacks,
    set_anarchy_stacks,
    set_uf_stacks,
    set_expertise_stacks,
    set_free_shot_stacks,
    set_smasher_chance_stacks,
    set_smasher_SMASH_stacks,
    merge_all_equipped_weapons,
    randomize_any_p_gear,
    reset_gunzerk_and_weapons_kb,
    reset_to_position_and_trigger_skills,
    save_checkpoint,
    overwrite_save,
    load_checkpoint,
    touch_file,
    log_current_state,
]

register_module(__name__)
