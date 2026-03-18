from dataclasses import asdict
from enum import StrEnum
from typing import TYPE_CHECKING, cast

from unrealsdk import find_object

from build_maker.common import spawn_item_from_balance
from build_maker.loadouts import krieg



if TYPE_CHECKING:
    from _typeshed import DataclassInstance
    from bl2 import WeaponBalanceDefinition, WillowWeapon


def dc_to_dict(instance: "DataclassInstance") -> dict[str, str]:
    """Convert a dataclass instance to a dict, with conversion of enums to values."""
    d = asdict(instance)

    result: dict[str, str] = {}
    for k, v in d.items():
        if isinstance(v, StrEnum):
            result[k] = v.value
    return result


# def create_weapon()


for item in krieg:

    match item.class_name:
        case "WeaponBalanceDefinition":
            balance = cast("WeaponBalanceDefinition", find_object(item.class_name, item.path))
            spawned_item = spawn_item_from_balance(balance, 80)
        case _:
            balance = cast("WeaponBalanceDefinition", find_object(item.class_name, item.path))
            spawned_item = spawn_item_from_balance(balance, 80)

    def_data = spawned_item.DefinitionData

    fixed_parts = dc_to_dict(item)

    # for 

    # print(def_data)
    # print(dc_to_dict(item))


    # print(item.grip.value)
    # print(spawned_item.DefinitionData.GripPartDefinition)

