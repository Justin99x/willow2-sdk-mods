from __future__ import annotations

from typing import List, TYPE_CHECKING, cast

from mods_base import BaseOption, BoolOption, GroupedOption, HiddenOption, NestedOption, hook
from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import GameVersion, RunCategory, get_pc
from unrealsdk import find_all, find_object
from unrealsdk.hooks import Type, add_hook, remove_hook

if TYPE_CHECKING:
    from bl2 import Actor


options: List[BaseOption]
host: bool = True


#
# def enable(game_version: GameVersion, run_category: RunCategory) -> None:
#     enable_options([travel_portal_disabled])
#     handle_travel_portal(None, travel_portal_disabled.value)
#
#     if any(game_version & group for group in [GameVersion.vStack, GameVersion.vMerge]):
#         handle_jakobs_auto(None, jakobs_auto_fire.value)
#         enable_options([jakobs_auto_fire])
#
#     if run_category == RunCategory.GearedSal and host:
#         enable_options([kill_skills, incite, locked_and_loaded])
#
# def disable():
#     handle_jakobs_auto(None, False)
#     handle_travel_portal(None, False)
#
#     disable_options(options)

# def enable_options(options: List[BaseOption]):
#     for option in options:
#         option.is_hidden = False
#
# def disable_options(options: List[BaseOption]):
#     for option in options:
#         option.is_hidden = True



def handle_jakobs_auto(option_ref: BoolOption | None, new_value: bool) -> None:
    """Turns automatic Jakobs shotguns on or off. Used to mimic functionality of free scroll macro.
    First arg is needed to be able to use this as an on_change callback in the option"""
    pc = get_pc()
    weapons = cast(List["WillowWeapon"], find_all("WillowWeapon"))
    autoburst_attribute_def = cast("AttributeDefinition",
                                   find_object("AttributeDefinition", "D_Attributes.Weapon.WeaponAutomaticBurstCount"))
    jakobs_shotguns = [
        weapon for weapon in weapons
        if weapon.DefinitionData.WeaponTypeDefinition is not None and weapon.DefinitionData.WeaponTypeDefinition.Name == "WT_Jakobs_Shotgun"
    ]
    if new_value:
        pc.ConsoleCommand(f"set WeaponTypeDefinition'GD_Weap_Shotgun.A_Weapons.WT_Jakobs_Shotgun' AutomaticBurstCount 0")
        for js in jakobs_shotguns:
            autoburst_attribute_def.SetAttributeBaseValue(js, 0)
    else:
        pc.ConsoleCommand(f"set WeaponTypeDefinition'GD_Weap_Shotgun.A_Weapons.WT_Jakobs_Shotgun' AutomaticBurstCount 1")
        for js in jakobs_shotguns:
            autoburst_attribute_def.SetAttributeBaseValue(js, 1)


def handle_travel_portal(option_ref: BoolOption | None, disable_portal: bool) -> None:
    """Disable travel animation for faster practice
    First arg is needed to be able to use this as an on_change callback in the option"""

    @hook("Engine.Actor:TriggerGlobalEventClass", Type.POST)
    def disable_portal_hook(obj: Actor, args: Actor.TriggerGlobalEventClass.args, ret: Actor.TriggerGlobalEventClass.ret,
            func: Actor.TriggerGlobalEventClass):
        try:
            holding = cast("HoldingAreaDestination",
                           find_object("HoldingAreaDestination", "Loader.TheWorld:PersistentLevel.HoldingAreaDestination_1"))
            holding.ExitPointsCounter = -99
        except ValueError:
            pass

    if disable_portal:
        disable_portal_hook.enable()
    else:
        disable_portal_hook.disable()



save_game_path = HiddenOption(
    identifier="Save Game Filepath",
    value=''
)
jakobs_auto_fire = BoolOption(
    identifier="Automatic Jakobs Shotguns",
    value=False,
    description="Makes Jakobs shotguns automatic to mimic freescroll macro functionality",
    on_change=handle_jakobs_auto
)
kill_skills = BoolOption(
    identifier="Trigger Kill Skills on Reset",
    value=False,
    description="When Reset to Position and Trigger Skills is pressed, trigger kill skills",
)
incite = BoolOption(
    identifier="Trigger Incite on Reset",
    description="When Reset to Position and Trigger Skills is pressed, trigger Incite",
    value=False,
)
locked_and_loaded = BoolOption(
    identifier="Trigger Locked and Loaded on Reset",
    description="When Reset to Position and Trigger Skills is pressed, trigger Locked and Loaded",
    value=False,
)
travel_portal_disabled = BoolOption(
    identifier="Disable Travel Portal",
    description="Disables blue tunnel animation when loading into a map",
    value=False,
    on_change=handle_travel_portal
)

geared_sal_options = GroupedOption(
    identifier="Geared Sal",
    children=[kill_skills, incite, locked_and_loaded]
)



options = [
    save_game_path,
    jakobs_auto_fire,
    # kill_skills,
    # incite,
    # locked_and_loaded,
    travel_portal_disabled,

    geared_sal_options
]


register_module(__name__)
