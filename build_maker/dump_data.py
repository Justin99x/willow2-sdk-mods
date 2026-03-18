"""Dump balance and part data from the game to generate Python code."""

import keyword
import re
from collections import Counter, defaultdict
from collections.abc import Callable, Sequence
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import TYPE_CHECKING, Protocol, cast

from unrealsdk import find_all, find_enum

from build_maker import MOD_DIR
from build_maker.common import spawn_item_from_balance
from build_maker.slots import (
    ArtifactSlot,
    ClassModSlot,
    GrenadeSlot,
    ShieldSlot,
    SlotInfo,
    WeaponSlot,
)

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
    """Get the longest common prefix that all elements share, excluding underscores."""
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
    """Protocol for Gearbox objects with Name and path."""

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
class PartSetInfo:
    """Info about a part set, including which slot it belongs to."""

    parts: tuple[GbxObject, ...]
    slot: Enum  # The slot enum member (e.g., WeaponSlot.grip)


@dataclass(frozen=True)
class DumpConfig[TBalance: "InventoryBalanceDefinition", TPart: "WillowInventoryPartDefinition", TSlot: Enum]:
    """Configuration for dumping a balance type."""

    balance_class_name: str
    output_file: Path
    parts_output_file: Path
    class_import_line: str
    slots: type[TSlot]
    should_skip_balance: Callable[[TBalance], bool]
    get_balance_slot_parts: Callable[[TBalance, type[TSlot]], dict[TSlot, list[TPart]]]


def make_part_set_enum(name: str, parts: tuple[GbxObject, ...], slot: Enum) -> str:
    """From class name and set of gearbox objects, create enum definition with defdata field info."""
    info: SlotInfo = slot.value
    output = f"class {to_class_name(name)}(StrEnum):\n"
    for part in parts:
        output += f'    {part.Name.lower().replace("-", "m")} = "{part._path_name()}"\n'

    # Add class level var about what field in DefinitionData this replaces
    output += f'\n    _defdata_field = "{info.defdata_field}"\n'
    return output + "\n\n"


def make_balance_class[TSlot: Enum](name: str, slot_prefixes: dict[TSlot, str], path: str, class_name: str) -> str:
    """From name and set of slot and prefix pairs, make class definition."""
    output = f"@dataclass\nclass {to_class_name(name)}:\n"
    output += f'    """{path}."""\n\n'
    output += f'    path: ClassVar[str] = "{path}"\n'
    output += f'    class_name: ClassVar[str] = "{class_name}"\n'
    output += "    levels: list[int]\n"
    for slot, prefix in slot_prefixes.items():
        output += f"    {slot.name}: {to_class_name(prefix)} | None = None\n"

    return output + "\n\n"


def dump_balance_type[  # noqa: C901
    TBalance: "InventoryBalanceDefinition",
    TPart: "WillowInventoryPartDefinition",
    TSlot: Enum,
](config: DumpConfig[TBalance, TPart, TSlot]) -> None:
    """Dump unique parts for all balances of a type."""
    # Track part sets along with their slot info
    all_part_sets: dict[frozenset[TPart], TSlot] = {}

    balances = dedup_balances(cast(list[TBalance], find_all(config.balance_class_name)))
    balances = [balance for balance in balances if not config.should_skip_balance(balance)]

    # First get the part sets from each balance, these are the distinct sets of possible parts.
    for balance in balances:
        slot_parts = config.get_balance_slot_parts(balance, config.slots)

        for slot, parts in slot_parts.items():
            if len(parts) > 1:  # Only want part sets > 1 since those can be changed.
                part_set = frozenset(parts)
                if part_set not in all_part_sets:
                    all_part_sets[part_set] = slot

    # We need to get names for our enums, and to do so we're going to get common prefixes from the part sets.
    # But there're duplicate prefix names, so we'll append those with letters A, B, C, etc.
    final_part_sets: dict[tuple[TPart, ...], tuple[str, TSlot]] = {}
    prefixes = [common_prefix([part.Name for part in part_set]) for part_set in all_part_sets if len(part_set) > 1]
    totals = Counter(prefixes)
    counts: defaultdict[str, int] = defaultdict(int)
    for part_set, slot in all_part_sets.items():
        part_names = [part.Name for part in part_set]
        prefix = common_prefix(part_names)
        if totals[prefix] == 1:
            final_part_sets[tuple(sorted(part_set, key=lambda part: part.Name))] = (prefix, slot)
        else:
            final_part_sets[tuple(sorted(part_set, key=lambda part: part.Name))] = (
                f"{prefix}_{chr(ord('A') + counts[prefix])}",
                slot,
            )
        counts[prefix] += 1

    # Now we need to work our way back through the balances to create the classes.
    # We also spawn an item to get at its in-game title for class naming.
    class_output = "from dataclasses import dataclass\n"
    class_output += "from typing import ClassVar\n\n"
    class_output += config.class_import_line
    for balance in balances:
        slots_prefix: dict[TSlot, str] = {}
        slot_parts = config.get_balance_slot_parts(balance, config.slots)

        for slot, part_set in slot_parts.items():
            if len(part_set) > 1:  # Only want part sets > 1 since those can be changed.
                prefix, _ = final_part_sets[tuple(sorted(part_set, key=lambda part: part.Name))]
                slots_prefix[slot] = prefix

        item = spawn_item_from_balance(balance, 80)
        if item:
            name = get_inv_title(item) if "ClassMod" not in item.Class.Name else "CM"

            class_output += make_balance_class(
                name + "_" + balance.Name,
                slots_prefix,
                balance._path_name(),
                balance.Class.Name,
            )

    parts_output = "from enum import StrEnum\n\n\n"
    for part_set, (prefix, slot) in final_part_sets.items():
        parts_output += make_part_set_enum(prefix, part_set, slot)

    (MOD_DIR / config.output_file).write_text(class_output)
    (MOD_DIR / config.parts_output_file).write_text(parts_output)


def get_weapon_parts(
    balance: "WeaponBalanceDefinition",
    slots: type[WeaponSlot],
) -> dict[WeaponSlot, list["WeaponPartDefinition"]]:
    """Get valid parts per slot from a weapon balance."""
    part_list = balance.RuntimePartListCollection

    result: dict[WeaponSlot, list[WeaponPartDefinition]] = {}
    for slot in slots:
        info: SlotInfo = slot.value
        part_data = getattr(part_list, info.part_list_field, None)

        if part_data is None or not part_data.bEnabled:
            result[slot] = []
            continue

        parts = [entry.Part for entry in part_data.WeightedParts if entry.Part]
        result[slot] = parts

    return result


def get_item_parts[TSlot: Enum](  # noqa: C901
    balance: "ItemBalanceDefinition",
    slots: type[TSlot],
) -> dict[TSlot, list["EquipableItemPartDefinition"]]:
    """Get valid parts per slot from an item balance, handling InventoryDefinition + PartListCollection merging."""
    part_list_collection = cast("ItemPartListCollectionDefinition | None", balance.PartListCollection)
    inventory_definition = cast("EquipableItemDefinition | None", balance.InventoryDefinition)

    mode = None
    mode_enum = None
    if part_list_collection:
        mode = part_list_collection.PartReplacementMode
        mode_enum = find_enum_part_replacement_mode("EPartReplacementMode")

    result: dict[TSlot, list[EquipableItemPartDefinition]] = {}

    for slot in slots:
        info: SlotInfo = slot.value
        parts: set[EquipableItemPartDefinition] = set()

        # Step 1: Get parts from InventoryDefinition
        if inventory_definition and info.inv_def_field:
            inv_def_part_list: ItemPartListDefinition | None = getattr(
                inventory_definition,
                info.inv_def_field,
                None,
            )
            if inv_def_part_list:
                for entry in inv_def_part_list.WeightedParts:
                    if entry.Part:
                        parts.add(cast("EquipableItemPartDefinition", entry.Part))

        # Step 2: Apply PartListCollection based on replacement mode
        if part_list_collection:
            collection_part_data = getattr(part_list_collection, info.part_list_field, None)

            if mode == mode_enum.EPRM_Complete: # pyright: ignore[reportOptionalMemberAccess]
                parts = set()

            if collection_part_data and collection_part_data.bEnabled:
                new_parts = cast(
                    set["EquipableItemPartDefinition"],
                    {entry.Part for entry in collection_part_data.WeightedParts if entry.Part},
                )

                if mode == mode_enum.EPRM_Additive: # pyright: ignore[reportOptionalMemberAccess]
                    parts |= new_parts
                else:
                    parts = new_parts

        result[slot] = list(parts)

    return result


def get_classmod_parts(
    balance: "ClassModBalanceDefinition",
    slots: type[ClassModSlot],
) -> dict[ClassModSlot, list["ItemPartDefinition"]]:
    """Get valid parts per slot from a class mod balance."""
    part_list = balance.RuntimePartListCollection

    result: dict[ClassModSlot, list[ItemPartDefinition]] = {}
    for slot in slots:
        info: SlotInfo = slot.value
        part_data = getattr(part_list, info.part_list_field, None)

        if part_data is None or not part_data.bEnabled:
            result[slot] = []
            continue

        parts = [entry.Part for entry in part_data.WeightedParts if entry.Part]
        result[slot] = parts

    return result


# === Config definitions ===

classmod_config = DumpConfig["ClassModBalanceDefinition", "ItemPartDefinition", ClassModSlot](
    balance_class_name="ClassModBalanceDefinition",
    output_file=Path("classmods.py"),
    parts_output_file=Path("classmod_parts.py"),
    class_import_line="from build_maker.classmod_parts import *\n\n\n",
    slots=ClassModSlot,
    should_skip_balance=lambda balance: "Default__" in balance.Name,
    get_balance_slot_parts=get_classmod_parts,
)

weapon_config = DumpConfig["WeaponBalanceDefinition", "WeaponPartDefinition", WeaponSlot](
    balance_class_name="WeaponBalanceDefinition",
    output_file=Path("weapons.py"),
    parts_output_file=Path("weapon_parts.py"),
    class_import_line="from build_maker.weapon_parts import *\n\n\n",
    slots=WeaponSlot,
    should_skip_balance=lambda balance: "Default__" in balance.Name,
    get_balance_slot_parts=get_weapon_parts,
)

shield_config = DumpConfig["ItemBalanceDefinition", "EquipableItemPartDefinition", ShieldSlot](
    balance_class_name="InventoryBalanceDefinition",
    output_file=Path("shields.py"),
    parts_output_file=Path("shield_parts.py"),
    class_import_line="from build_maker.shield_parts import *\n\n\n",
    slots=ShieldSlot,
    should_skip_balance=lambda balance: (
        "Default__" in balance.Name
        or not (balance.InventoryDefinition and balance.InventoryDefinition.Class.Name == "ShieldDefinition")
    ),
    get_balance_slot_parts=get_item_parts,
)

artifact_config = DumpConfig["ItemBalanceDefinition", "EquipableItemPartDefinition", ArtifactSlot](
    balance_class_name="InventoryBalanceDefinition",
    output_file=Path("artifacts.py"),
    parts_output_file=Path("artifact_parts.py"),
    class_import_line="from build_maker.artifact_parts import *\n\n\n",
    slots=ArtifactSlot,
    should_skip_balance=lambda balance: (
        "Default__" in balance.Name
        or not (balance.InventoryDefinition and balance.InventoryDefinition.Class.Name == "ArtifactDefinition")
    ),
    get_balance_slot_parts=get_item_parts,
)

grenade_config = DumpConfig["ItemBalanceDefinition", "EquipableItemPartDefinition", GrenadeSlot](
    balance_class_name="InventoryBalanceDefinition",
    output_file=Path("grenades.py"),
    parts_output_file=Path("grenade_parts.py"),
    class_import_line="from build_maker.grenade_parts import *\n\n\n",
    slots=GrenadeSlot,
    should_skip_balance=lambda balance: (
        "Default__" in balance.Name
        or not (balance.InventoryDefinition and balance.InventoryDefinition.Class.Name == "GrenadeModDefinition")
    ),
    get_balance_slot_parts=get_item_parts,
)



dump_balance_type(classmod_config)
dump_balance_type(weapon_config)
dump_balance_type(shield_config)
dump_balance_type(artifact_config)
dump_balance_type(grenade_config)
