import keyword
import re
from collections import Counter, defaultdict
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Protocol, cast

from unrealsdk import find_all, find_enum

from build_maker import MOD_DIR
from build_maker.common import spawn_item_from_balance

if TYPE_CHECKING:
    from bl2 import (
        ClassModBalanceDefinition,
        EquipableItemDefinition,
        EquipableItemPartDefinition,
        InventoryBalanceDefinition,
        ItemBalanceDefinition,
        ItemPartDefinition,
        ItemPartListCollectionDefinition,
        ItemPartListDefinition,
        WeaponBalanceDefinition,
        WeaponPartDefinition,
        WillowInventory,
        WillowInventoryPartDefinition,
    )

    find_enum_part_replacement_mode = ItemPartListCollectionDefinition.EPartReplacementMode.find_enum
else:
    find_enum_part_replacement_mode = find_enum


def common_prefix(strings: list[str]) -> str:
    """Gets the longest common prefix that all elements share, excluding underscores."""
    prefix: list[str] = []

    for chars in zip(*strings, strict=False):
        if len(set(chars)) == 1:
            prefix.append(chars[0])
        else:
            break

    return "".join(prefix).removesuffix("_")


def get_inv_title(inv: "WillowInventory") -> str:
    """Get main item title from an inventory instance."""
    match inv.Class.Name:
        case "WillowWeapon":
            return inv.DefinitionData.TitlePartDefinition.PartName
        case "WillowShield":
            if not inv.DefinitionData.TitleItemNamePartDefinition:  # Captain Blade's shield
                return inv.ItemName
            return inv.DefinitionData.TitleItemNamePartDefinition.PartName
        case "WillowClassMod":
            return inv.DefinitionData.PrefixItemNamePartDefinition.PartName
        case "WillowArtifact":
            return inv.ItemName
        case "WillowGrenadeMod":
            if not inv.DefinitionData.TitleItemNamePartDefinition:  # Captain Blade's nade
                return inv.ItemName
            return inv.DefinitionData.TitleItemNamePartDefinition.PartName
        case _:
            return ""


class GbxObject(Protocol):
    @property
    def Name(self) -> str: ...  # noqa: D102, N802
    def _path_name(self) -> str: ...


def dedup_balances[T: GbxObject](balances: Sequence[T]) -> list[T]:
    """Deduplicate objects by `.Name`, preferring ones whose `_path_name()` does not contain "Anemone"."""
    groups: defaultdict[str, list[T]] = defaultdict(list)

    for bal in balances:
        groups[bal.Name].append(bal)

    result: list[T] = []

    for group in groups.values():
        preferred = next(
            (b for b in group if "Anemone" not in b._path_name()),  # pyright: ignore[reportPrivateUsage]
            group[0],
        )
        result.append(preferred)

    return result


def to_class_name(name: str, prefix: str = "_") -> str:
    """Convert to valid class name."""
    # Split on non-alphanumeric, keep digits
    parts = re.findall(r"[A-Za-z0-9]+", name)
    pascal = "_".join(p.capitalize() for p in parts if p)

    if not pascal:
        pascal = "Unnamed"

    # Fix invalid identifiers (e.g., starts with digit or is keyword)
    if not pascal.isidentifier() or keyword.iskeyword(pascal):
        pascal = f"{prefix}{pascal}"

    return pascal


@dataclass(frozen=True)
class DumpConfig[TBalance: InventoryBalanceDefinition, TPart: WillowInventoryPartDefinition]:
    balance_class_name: str
    part_class_name: str
    output_file: Path
    parts_output_file: Path
    class_import_line: str
    slot_types: dict[str, str]
    should_skip_balance: Callable[[TBalance], bool]
    get_balance_slot_parts: Callable[[TBalance, dict[str, str]], dict[str, list[TPart]]]


def make_part_set_enum(name: str, parts: tuple[GbxObject, ...], defdata_field: str) -> str:
    """From class name and set of gearbox objects, use name and path name to create enum definition."""
    output = f"class {to_class_name(name)}(StrEnum):\n"
    for part in parts:
        output += f'    {part.Name.lower().replace("-", "m")} = "{part._path_name()}"\n'

    # Add class level var about what field in DefinitionData this replaces
    output += f'\n    _part_class = "{defdata_field}"\n'
    return output + "\n\n"


def make_balance_class(name: str, slot_prefixes: dict[str, str], path: str, class_name: str) -> str:
    """From name and set of slot and prefix pairs, make class definition."""
    output = f"@dataclass\nclass {to_class_name(name)}:\n"
    output += f'    """{path}."""\n\n'
    output += f'    path: ClassVar[str] = "{path}"\n'
    output += f'    class_name: ClassVar[str] = "{class_name}"\n'
    output += "    levels: list[int]\n"
    for slot, prefix in slot_prefixes.items():
        output += f"    {slot}: {to_class_name(prefix)} | None = None\n"

    return output + "\n\n"


def dump_balance_type[TBalance: InventoryBalanceDefinition, TPart: WillowInventoryPartDefinition](config: DumpConfig[TBalance, TPart]) -> None:  # noqa: C901
    """Dump unique parts for all weapons."""

    all_part_sets: set[frozenset[TPart]] = set()

    balances = dedup_balances(cast(list[TBalance], find_all(config.balance_class_name)))
    balances = [balance for balance in balances if not config.should_skip_balance(balance)]

    # First get the part sets from each balance, these are the distinct sets of possible parts.
    for balance in balances:
        slot_parts = config.get_balance_slot_parts(balance, config.slot_types)

        for parts in slot_parts.values():
            if len(parts) > 1:  # Only want part sets > 1 since those can be changed.
                all_part_sets.add(frozenset(parts))

    # We need to get names for our enums, and to do so we're going to get common prefixes from the part sets.
    # But there're duplicate prefix names, so we'll append those with letters A, B, C, etc.
    final_part_sets: dict[tuple[TPart, ...], str] = {}
    prefixes = [common_prefix([part.Name for part in part_set]) for part_set in all_part_sets if len(part_set) > 1]
    totals = Counter(prefixes)
    counts: defaultdict[str, int] = defaultdict(int)
    for part_set in all_part_sets:
        part_names = [part.Name for part in part_set]
        prefix = common_prefix(part_names)
        if totals[prefix] == 1:
            final_part_sets[tuple(sorted(part_set, key=lambda part: part.Name))] = prefix
        else:
            final_part_sets[tuple(sorted(part_set, key=lambda part: part.Name))] = f"{prefix}_{chr(ord('A') + counts[prefix])}"
        counts[prefix] += 1

    # Now we need to work our way back through the balances to create the classes.
    # We also spawn an item to get at its in-game title for class naming.
    class_output = "from dataclasses import dataclass\n"
    class_output += "from typing import ClassVar\n\n"
    class_output += config.class_import_line
    for balance in balances:
        slots_prefix: dict[str, str] = {}
        slot_parts = config.get_balance_slot_parts(balance, config.slot_types)

        for slot, part_set in slot_parts.items():
            if len(part_set) > 1:  # Only want part sets > 1 since those can be changed.
                prefix = final_part_sets[tuple(sorted(part_set, key=lambda part: part.Name))]
                slots_prefix[slot] = prefix

        item = spawn_item_from_balance(balance, 80)
        if item:
            name = get_inv_title(item) if "ClassMod" not in item.Class.Name else "CM"

            class_output += make_balance_class(name + "_" + balance.Name, slots_prefix, balance._path_name(), balance.Class.Name)

    parts_output = "from enum import StrEnum\n\n\n"
    for part_set, prefix in final_part_sets.items():
        parts_output += make_part_set_enum(prefix, part_set, config.part_class_name)

    (MOD_DIR / config.output_file).write_text(class_output)
    (MOD_DIR / config.parts_output_file).write_text(parts_output)


def get_weapon_parts(balance: "WeaponBalanceDefinition", _: dict[str, str]) -> dict[str, list["WeaponPartDefinition"]]:
    """Get valid parts per slot from a weapon balance."""
    part_list = balance.RuntimePartListCollection

    slots = {
        "body": part_list.BodyPartData,
        "grip": part_list.GripPartData,
        "barrel": part_list.BarrelPartData,
        "sight": part_list.SightPartData,
        "stock": part_list.StockPartData,
        "element": part_list.ElementalPartData,
        "accessory1": part_list.Accessory1PartData,
    }

    result: dict[str, list[WeaponPartDefinition]] = {}
    for slot_name, part_data in slots.items():
        if not part_data.bEnabled:
            result[slot_name] = []
            continue

        parts = [entry.Part for entry in part_data.WeightedParts if entry.Part]
        result[slot_name] = parts

    return result


def get_item_parts(balance: "ItemBalanceDefinition", slot_types: dict[str, str]) -> dict[str, list["EquipableItemPartDefinition"]]:
    """Get valid parts per slot from an item balance."""
    part_list_collection = cast("ItemPartListCollectionDefinition", balance.PartListCollection)
    inventory_definition = cast("EquipableItemDefinition", balance.InventoryDefinition)

    if part_list_collection:
        mode = part_list_collection.PartReplacementMode
        mode_enum = find_enum_part_replacement_mode("EPartReplacementMode")

    slots: dict[str, list[EquipableItemPartDefinition]] = {}

    for slot_type, greek in slot_types.items():
        parts: set[EquipableItemPartDefinition] = set()

        # Step 1: Get parts from InventoryDefintion
        inv_def_part_list: ItemPartListDefinition = getattr(inventory_definition, f"{greek}Parts")
        if inv_def_part_list:
            for entry in inv_def_part_list.WeightedParts:
                if entry.Part:
                    parts.add(cast("EquipableItemPartDefinition", entry.Part))

        # Step 2: Replace parts from PartListCollection based on replacement mode.
        if part_list_collection:
            collection_part_data: ItemPartListCollectionDefinition.ItemCustomPartTypeData = getattr(part_list_collection, f"{greek}PartData")

            if mode == mode_enum.EPRM_Complete:  # pyright: ignore[reportPossiblyUnboundVariable]
                parts = set()

            if collection_part_data.bEnabled:
                new_parts = cast(set["EquipableItemPartDefinition"], {entry.Part for entry in collection_part_data.WeightedParts if entry.Part})

                if mode == mode_enum.EPRM_Additive:  # pyright: ignore[reportPossiblyUnboundVariable]
                    parts |= new_parts
                else:
                    parts = new_parts

        slots[slot_type] = list(parts)

    return slots


def get_classmod_parts(balance: "ClassModBalanceDefinition", _: dict[str, str]) -> dict[str, list["ItemPartDefinition"]]:
    """Get valid parts per slot from a weapon balance."""
    part_list = balance.RuntimePartListCollection

    slots = {
        "specialization": part_list.AlphaPartData,
        "primary": part_list.BetaPartData,
        "secondary": part_list.GammaPartData,
        "penalty": part_list.MaterialPartData,
    }

    result: dict[str, list[ItemPartDefinition]] = {}
    for slot_name, part_data in slots.items():
        if not part_data.bEnabled:
            result[slot_name] = []
            continue

        parts = [entry.Part for entry in part_data.WeightedParts if entry.Part]
        result[slot_name] = parts

    # Special handling of definitions for classmods, which act kind of like parts in the spawn process.
    def get_cm_defs(balance: "ClassModBalanceDefinition") -> list["ItemPartDefinition"]:
        if balance.ClassModDefinitions:
            return cast(list["ItemPartDefinition"], balance.ClassModDefinitions)
        if balance.BaseDefinition:
            return get_cm_defs(cast("ClassModBalanceDefinition", balance.BaseDefinition))
        return []

    result["definition"] = get_cm_defs(balance)

    return result


classmod_config = DumpConfig["ClassModBalanceDefinition", "ItemPartDefinition"](
    balance_class_name="ClassModBalanceDefinition",
    part_class_name="ClassModPartDefinition",
    output_file=Path(MOD_DIR) / "classmods.py",
    parts_output_file=Path(MOD_DIR) / "classmod_parts.py",
    class_import_line="from build_maker.classmod_parts import *\n\n\n",
    slot_types={},
    should_skip_balance=lambda balance: "Default__" in balance.Name,
    get_balance_slot_parts=get_classmod_parts,
)

dump_balance_type(classmod_config)

weapon_config = DumpConfig["WeaponBalanceDefinition", "WeaponPartDefinition"](
    balance_class_name="WeaponBalanceDefinition",
    part_class_name="WeaponPartDefinition",
    output_file=Path(MOD_DIR) / "weapons.py",
    parts_output_file=Path(MOD_DIR) / "weapon_parts.py",
    class_import_line="from build_maker.weapon_parts import *\n\n\n",
    slot_types={},
    should_skip_balance=lambda balance: "Default__" in balance.Name,
    get_balance_slot_parts=get_weapon_parts,
)

dump_balance_type(weapon_config)

shield_config = DumpConfig["ItemBalanceDefinition", "EquipableItemPartDefinition"](
    balance_class_name="InventoryBalanceDefinition",
    part_class_name="ShieldPartDefinition",
    output_file=Path(MOD_DIR) / "shields.py",
    parts_output_file=Path(MOD_DIR) / "shield_parts.py",
    class_import_line="from build_maker.shield_parts import *\n\n\n",
    slot_types={"body": "Alpha", "battery": "Beta", "capacitor": "Gamma", "accessory": "Delta"},
    should_skip_balance=lambda balance: (
        True if "Default__" in balance.Name else not (balance.InventoryDefinition and balance.InventoryDefinition.Class.Name == "ShieldDefinition")
    ),
    get_balance_slot_parts=get_item_parts,
)

dump_balance_type(shield_config)

artifact_config = DumpConfig["ItemBalanceDefinition", "EquipableItemPartDefinition"](
    balance_class_name="InventoryBalanceDefinition",
    part_class_name="ArtifactPartDefinition",
    output_file=Path(MOD_DIR) / "artifacts.py",
    parts_output_file=Path(MOD_DIR) / "artifact_parts.py",
    class_import_line="from build_maker.artifact_parts import *\n\n\n",
    slot_types={"body": "Eta", "upgrade": "Theta", "alpha": "Alpha", "beta": "Beta", "gamma": "Gamma"},
    should_skip_balance=lambda balance: (
        True if "Default__" in balance.Name else not (balance.InventoryDefinition and balance.InventoryDefinition.Class.Name == "ArtifactDefinition")
    ),
    get_balance_slot_parts=get_item_parts,
)

dump_balance_type(artifact_config)

grenade_config = DumpConfig["ItemBalanceDefinition", "EquipableItemPartDefinition"](
    balance_class_name="InventoryBalanceDefinition",
    part_class_name="GrenadeModPartDefinition",
    output_file=Path(MOD_DIR) / "grenades.py",
    parts_output_file=Path(MOD_DIR) / "grenade_parts.py",
    class_import_line="from build_maker.grenade_parts import *\n\n\n",
    slot_types={
        "payload": "Alpha",
        "delivery": "Beta",
        "trigger": "Gamma",
        "accessory": "Delta",
        "damage": "Epsilon",
        "radius": "Zeta",
        "child_count": "Eta",
        "status_damage": "Theta",
    },
    should_skip_balance=lambda balance: (
        True if "Default__" in balance.Name else not (balance.InventoryDefinition and balance.InventoryDefinition.Class.Name == "GrenadeModDefinition")
    ),
    get_balance_slot_parts=get_item_parts,
)

dump_balance_type(grenade_config)
