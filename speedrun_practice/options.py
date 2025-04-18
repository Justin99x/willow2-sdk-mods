from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from mods_base import BaseOption, BoolOption, GroupedOption, HiddenOption, hook
from unrealsdk import find_all, find_object
from unrealsdk.hooks import Type

from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import get_pc

if TYPE_CHECKING:
    from bl2 import AttributeDefinition, HoldingAreaDestination, WillowWeapon


options: list[BaseOption]
host: bool = True


def handle_jakobs_auto(option_ref: BoolOption, jakobs_auto: bool) -> None:
    """
    Turns automatic Jakobs shotguns on or off.

    Used to mimic functionality of free scroll macro.
    """
    if option_ref.mod is None or not option_ref.mod.is_enabled:
        jakobs_auto = False

    pc = get_pc()
    weapons = cast(list["WillowWeapon"], find_all("WillowWeapon"))
    autoburst_attribute_def = cast(
        "AttributeDefinition",
        find_object("AttributeDefinition", "D_Attributes.Weapon.WeaponAutomaticBurstCount"),
    )
    jakobs_shotguns = [
        weapon for weapon in weapons
        if weapon.DefinitionData.WeaponTypeDefinition is not None  # type: ignore
        and weapon.DefinitionData.WeaponTypeDefinition.Name == "WT_Jakobs_Shotgun"
    ]
    if jakobs_auto:
        pc.ConsoleCommand(
            "set WeaponTypeDefinition'GD_Weap_Shotgun.A_Weapons.WT_Jakobs_Shotgun' "
            "AutomaticBurstCount 0",
        )
        for js in jakobs_shotguns:
            autoburst_attribute_def.SetAttributeBaseValue(js, 0)
    else:
        pc.ConsoleCommand(
            "set WeaponTypeDefinition'GD_Weap_Shotgun.A_Weapons.WT_Jakobs_Shotgun' "
            "AutomaticBurstCount 1",
        )
        for js in jakobs_shotguns:
            autoburst_attribute_def.SetAttributeBaseValue(js, 1)


def handle_travel_portal(option_ref: BoolOption, disable_portal: bool) -> None:
    """Disable travel animation for faster practice."""
    if option_ref.mod is None or not option_ref.mod.is_enabled:
        disable_portal = False

    @hook("Engine.Actor:TriggerGlobalEventClass", Type.POST)
    def disable_portal_hook(*_: Any) -> None:
        try:
            holding = cast(
                "HoldingAreaDestination",
                find_object(
                    "HoldingAreaDestination",
                    "Loader.TheWorld:PersistentLevel.HoldingAreaDestination_1",
                ),
            )
            holding.ExitPointsCounter = -99
        except ValueError:
            pass

    if disable_portal:
        disable_portal_hook.enable()
    else:
        disable_portal_hook.disable()


save_game_path = HiddenOption(identifier="Save Game Filepath", value="")
jakobs_auto_fire = BoolOption(
    identifier="Automatic Jakobs Shotguns",
    value=False,
    description="Makes Jakobs shotguns automatic to mimic freescroll macro functionality",
    on_change=handle_jakobs_auto,
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
    on_change=handle_travel_portal,
)

geared_sal_options = GroupedOption(
    identifier="Geared Sal", children=[kill_skills, incite, locked_and_loaded],
)


options = [
    save_game_path,
    jakobs_auto_fire,
    travel_portal_disabled,
    geared_sal_options,
]


register_module(__name__)
