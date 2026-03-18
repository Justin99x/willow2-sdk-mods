"""Development script to spawn/edit items from loadouts."""

from copy import copy
from dataclasses import Field, fields
from enum import Enum, StrEnum
from typing import TYPE_CHECKING, Any, ClassVar, Protocol, cast

from mods_base import get_pc
from unrealsdk import find_object

from build_maker.artifacts import *
from build_maker.classmods import *
from build_maker.common import spawn_item_from_balance
from build_maker.grenades import *
from build_maker.loadouts import krieg
from build_maker.shields import *
from build_maker.slots import (
    ArtifactSlot,
    ClassModSlot,
    GrenadeSlot,
    ShieldSlot,
    WeaponSlot,
)
from build_maker.weapons import *

if TYPE_CHECKING:
    from bl2 import InventoryBalanceDefinition, WillowInventory, WillowItem, WillowWeapon


# Map spawned item class names to their slot enums
INVENTORY_SLOT_ENUMS: dict[str, type[Enum]] = {
    "WillowWeapon": WeaponSlot,
    "WillowShield": ShieldSlot,
    "WillowGrenadeMod": GrenadeSlot,
    "WillowArtifact": ArtifactSlot,
    "WillowClassMod": ClassModSlot,
}


class ItemSpec(Protocol):
    class_name: str
    path: str
    __dataclass_fields__: ClassVar[dict[str, Field[Any]]]


def spawn_and_edit_item(item_spec: ItemSpec) -> None:
    """Spawn an item from a loadout spec and apply fixed parts."""
    balance = cast(
        "InventoryBalanceDefinition",
        find_object(item_spec.class_name, item_spec.path),
    )

    level = 80
    spawned_item = cast("WillowInventory", spawn_item_from_balance(balance, level))
    if not spawned_item:
        print(f"Failed to spawn {item_spec.path} at level {level}")
        return

    # Determine slot enum based on spawned item type
    inv_class_name = spawned_item.Class.Name
    if inv_class_name not in INVENTORY_SLOT_ENUMS:
        print(f"Unknown inventory class: {inv_class_name}")
        return
    slot_enum = INVENTORY_SLOT_ENUMS[inv_class_name]
    is_weapon = inv_class_name == "WillowWeapon"

    # Copy the definition data so we can modify it
    def_data = copy(spawned_item.DefinitionData)

    # Iterate over dataclass fields to find the ones that are set
    for field in fields(item_spec):
        value = getattr(item_spec, field.name)

        # Skip non-part fields and None values
        if field.name in ("levels", "path", "class_name") or value is None:
            continue

        # Look up the defdata field name from the slot enum
        try:
            slot = slot_enum[field.name]
            defdata_field = slot.value.defdata_field
        except KeyError:
            print(f"Unknown slot: {field.name}")
            continue

        # Get the part object from the enum value (which is the path)
        if isinstance(value, StrEnum):
            part = find_object("Object", value.value)
            setattr(def_data, defdata_field, part)
            print(f"  Set {defdata_field} = {value.value}")

    # Create the new item with modified parts
    if is_weapon:
        new_item = cast("WillowWeapon", spawned_item).CreateWeaponFromDef(
            NewWeaponDef=def_data,
            PlayerOwner=get_pc().Pawn,
            bForceSelectNameParts=True,
        )
    else:
        new_item = cast("WillowItem", spawned_item).CreateItemFromDef(
            NewItemDef=def_data,
            PlayerOwner=get_pc().Pawn,
            NewQuantity=1,
            bForceSelectNameParts=True,
        )

    # Add to inventory
    get_pc().Pawn.InvManager.AddInventoryToBackpack(new_item)
    print(f"Spawned {item_spec.path} at level {level}")


def spawn_loadout(loadout: list[Any]) -> None:
    """Spawn all items in a loadout."""
    for item_spec in loadout:
        spawn_and_edit_item(item_spec)


# Run it
krieg = [
    Pimpernel_Sniper_Maliwan_3_Pimpernel(levels=[27], element=Sr_Elemental_B.sr_elemental_slag, grip=Sr_Grip.sr_grip_maliwan),
    Badaboom_Rl_Bandit_5_Badaboom(levels=[50, 80, 83, 86, 88, 90], element=Rl_Elemental_A.rl_elemental_none, grip=L_Grip.l_grip_bandit),
    The_Rough_Rider_S_Bucklershield(levels=[50, 80, 83, 86, 90]),
    The_Bee_Itemgrade_Gear_Shield_Impact_05_Legendary(levels=[50, 80, 82, 84, 86, 88, 90]),
    Gm_Areaeffect_2_Uncommon(levels=[50, 80, 82, 84, 86, 88, 90]),
    Blood_Of_The_Ancients_A_Vitalitystockpile_Veryrare(levels=[80], second=Enablesecond_Effect_E.enablesecond_effect5, third=Enablethird_Effect_C.enablethird_effect5),
    Topneaa_Rl_Vladof_5_Alien(levels=[80, 82, 84, 86, 88, 90], element=Rl_Elemental_B.rl_elemental_corrosive),
]

spawn_loadout(krieg)
