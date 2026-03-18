# Gear Sets Mod Design

A mod to spawn gear with constrained random parts from YAML configuration.

## Core Concept

Spawn items with **some parts fixed, others random**. For example: "Generate a random Pimpernel with Maliwan grip and Shock element" - other parts (stock, sight, etc.) randomize normally per the game's balance.

## Implementation Approach

### Spawn Random, Then Fix Parts

1. Spawn a random item from a balance definition using `SpawnBalancedInventoryFromInventoryBalanceDefinition`
2. Read its `DefinitionData`
3. Override the constrained parts
4. Delete the old item, create a new one with the modified `DefinitionData`

This guarantees the randomness of non-specified parts exactly as the game intended.

```python
from copy import copy
import unrealsdk

SPAWN_FROM_BAL_DEF = unrealsdk.find_class(
    "ItemPool",
).ClassDefaultObject.SpawnBalancedInventoryFromInventoryBalanceDefinition

CREATE_WEAPON_FROM_DEF = unrealsdk.find_class("WillowWeapon").ClassDefaultObject.CreateWeaponFromDef
CREATE_ITEM_FROM_DEF = unrealsdk.find_class("WillowItem").ClassDefaultObject.CreateItemFromDef

def spawn_constrained_item(balance_path: str, level: int, fixed_parts: dict, owner) -> UObject:
    balance = unrealsdk.find_object("InventoryBalanceDefinition", balance_path)

    # Spawn random base
    _, (item,) = SPAWN_FROM_BAL_DEF(
        InvBalanceDefinition=balance,
        Quantity=1,
        GameStage=level,
        AwesomeLevel=0,
        ContextSource=owner,
        SpawnedInventory=(),
    )

    # Copy and modify definition data
    def_data = copy(item.DefinitionData)

    for slot_name, part in fixed_parts.items():
        setattr(def_data, slot_name, part)

    # Recreate with fixed parts
    is_weapon = item.Class._inherits(unrealsdk.find_class("WillowWeapon"))
    if is_weapon:
        new_item = CREATE_WEAPON_FROM_DEF(
            NewWeaponDef=def_data,
            PlayerOwner=owner,
            bForceSelectNameParts=True,
        )
    else:
        new_item = CREATE_ITEM_FROM_DEF(
            NewItemDef=def_data,
            PlayerOwner=owner,
            NewQuantity=1,
            bForceSelectNameParts=True,
        )

    return new_item
```

## Item Definition Structure

### Weapons (`WeaponDefinitionData`)

| Field | Description |
|-------|-------------|
| `WeaponTypeDefinition` | Base weapon type (Pistol, SMG, etc.) |
| `BalanceDefinition` | Rarity/level balance |
| `ManufacturerDefinition` | Manufacturer |
| `ManufacturerGradeIndex` | Item level |
| `GameStage` | World level when spawned |
| `BodyPartDefinition` | Body part |
| `GripPartDefinition` | Grip part |
| `BarrelPartDefinition` | Barrel part |
| `SightPartDefinition` | Sight part |
| `StockPartDefinition` | Stock part |
| `ElementalPartDefinition` | Element (fire, shock, etc.) |
| `Accessory1PartDefinition` | Primary accessory |
| `Accessory2PartDefinition` | Alt accessory |
| `MaterialPartDefinition` | Skin/material |

### Items (`ItemDefinitionData`)

Uses Greek letter slots that map differently per item type:

| Item Type | Alpha | Beta | Gamma | Delta |
|-----------|-------|------|-------|-------|
| **Shield** | Body | Battery | Capacitor | Accessory |
| **Grenade** | Payload | Delivery | Trigger | Accessory |
| **Class Mod** | Specialization | Primary | Secondary | - |
| **Relic** | - | - | - | - (Eta=Body, Theta=Upgrade) |

## YAML Design

### User-Friendly Format

```yaml
gear_sets:
  shock_sniper:
    name: "Shock Sniper Build"
    items:
      - balance: pimpernel
        level: 72
        parts:
          grip: maliwan
          element: shock

      - balance: lyuda
        level: 72
        parts:
          grip: vladof
          element: shock

      - balance: bee
        level: 72

  allegiance_jakobs:
    name: "Jakobs Allegiance"
    items:
      - balance: maggie
        level: player  # Match player's current level
        parts:
          grip: jakobs

      - balance: skullmasher
        level: player
        parts:
          grip: jakobs
          stock: jakobs
```

### Key Features

- **Balance aliases**: `pimpernel` instead of `GD_Orchid_BossWeapons.Sniper.Sniper_Maliwan_3_Pimpernel`
- **Part keyword matching**: `maliwan` matches `SR_Grip_Maliwan` from valid parts
- **Friendly slot names**: `grip` instead of `GripPartDefinition`
- **`level: player`**: Special keyword for current player level
- **Missing parts = random**: Only specify what you want fixed

## Part Matching Strategy

Query the balance's `RuntimePartListCollection` for valid parts, then keyword match:

```python
def find_part(balance, slot: str, keyword: str) -> UObject:
    """Find a part by keyword from valid parts for a slot."""
    part_list = getattr(balance.RuntimePartListCollection, SLOT_TO_PARTLIST[slot])
    valid_parts = [entry.Part for entry in part_list.WeightedParts if entry.Part is not None]

    keyword = keyword.lower()
    matches = [
        p for p in valid_parts
        if keyword in p._path_name().lower() or keyword in p.Name.lower()
    ]

    if len(matches) == 1:
        return matches[0]
    elif len(matches) > 1:
        raise AmbiguousPartError(keyword, matches)
    else:
        raise PartNotFoundError(keyword, valid_parts)
```

### Error Messages

```
Error in gear set "mobbing_loadout", item 1 (pimpernel):
  Part "vladof" not found for slot "grip"
  Valid options: dahl, hyperion, jakobs, maliwan

Error in gear set "mobbing_loadout", item 1 (pimpernel):
  Part "mali" is ambiguous for slot "element"
  Matches: maliwan_fire, maliwan_shock, maliwan_corrosive, maliwan_slag
```

## Slot Name Mappings

### Weapons

```python
WEAPON_SLOT_MAP = {
    "body": "BodyPartDefinition",
    "grip": "GripPartDefinition",
    "barrel": "BarrelPartDefinition",
    "sight": "SightPartDefinition",
    "stock": "StockPartDefinition",
    "element": "ElementalPartDefinition",
    "accessory": "Accessory1PartDefinition",
    "accessory1": "Accessory1PartDefinition",
    "accessory2": "Accessory2PartDefinition",
    "material": "MaterialPartDefinition",
    "skin": "MaterialPartDefinition",
}

# For RuntimePartListCollection lookups
WEAPON_SLOT_TO_PARTLIST = {
    "body": "BodyPartData",
    "grip": "GripPartData",
    "barrel": "BarrelPartData",
    "sight": "SightPartData",
    "stock": "StockPartData",
    "element": "ElementalPartData",
    "accessory": "Accessory1PartData",
    "accessory1": "Accessory1PartData",
    "accessory2": "Accessory2PartData",
    "material": "MaterialPartData",
}
```

### Shields

```python
SHIELD_SLOT_MAP = {
    "body": "AlphaItemPartDefinition",
    "battery": "BetaItemPartDefinition",
    "capacitor": "GammaItemPartDefinition",
    "accessory": "DeltaItemPartDefinition",
    "material": "MaterialItemPartDefinition",
}
```

## Project Structure

```
gear_sets/
├── __init__.py          # Mod entry point, keybinds, menu
├── pyproject.toml       # Mod metadata
├── aliases.py           # BALANCE_ALIASES dict
├── spawner.py           # Core spawn + fix logic
├── part_matcher.py      # Keyword matching against valid parts
├── yaml_loader.py       # Load/validate YAML config
└── gear_sets.yaml       # Default/example config
```

## Balance Aliases (Starter List)

```python
BALANCE_ALIASES = {
    # Sniper Rifles
    "pimpernel": "GD_Orchid_BossWeapons.Sniper.Sniper_Maliwan_3_Pimpernel",
    "lyuda": "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Lyudmila",
    "skullmasher": "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher",

    # Pistols
    "unkempt harold": "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_Calla",
    "dpuh": "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_Calla",
    "harold": "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_Calla",
    "maggie": "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie",
    "grog nozzle": "GD_Aster_Weapons.Pistols.Pistol_Maliwan_3_GrogNozzle",
    "lady fist": "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist",

    # Shotguns
    "interfacer": "GD_Sage_Weapons.Shotgun.Shotgun_Hyperion_3_Interfacer",
    "conference call": "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall",
    "orphan maker": "GD_Orchid_BossWeapons.Shotgun.Shotgun_Jakobs_3_OrphanMaker",

    # SMGs
    "sandhawk": "GD_Orchid_BossWeapons.SMG.SMG_Dahl_3_SandHawk",
    "sand hawk": "GD_Orchid_BossWeapons.SMG.SMG_Dahl_3_SandHawk",
    "bitch": "GD_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch",
    "slagga": "GD_Weap_SMG.A_Weapons_Legendary.SMG_Bandit_5_Slagga",

    # Shields
    "bee": "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_05_Legendary",
    "sham": "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_Legendary",
    "rough rider": "GD_Sage_Shields.A_Item_Legendary.Shield_Rough_Rider",
    "antagonist": "GD_Aster_Shields.Shields.Shield_Seraph_Antagonist",

    # Grenades
    "storm front": "GD_GrenadeMods.A_Item_Legendary.GrenadeMod_StormFront",
    "fastball": "GD_GrenadeMods.A_Item_Legendary.GrenadeMod_Fastball",
    "chain lightning": "GD_Aster_GrenadeMods.A_Item_Legendary.GrenadeMod_ChainLightning",
    "magic missile": "GD_Aster_GrenadeMods.A_Item_Unique.GrenadeMod_MagicMissileRare",

    # Relics
    "bone of the ancients": "GD_Artifacts.A_Item.Artifact_Elemental_Status",
    "bone": "GD_Artifacts.A_Item.Artifact_Elemental_Status",
    "sheriff's badge": "GD_Artifacts.A_Item_Unique.Artifact_Sheriff",
}
```

## References

- `apple1417-willow2-sdk-mods/vendor_edit/` - Item editing, spawning, definition data handling
- `apple1417-willow2-sdk-mods/vendor_edit/replacement_lists.py` - Part list querying per item type
- `apple1417-willow2-sdk-mods/vendor_edit/item_codes.py` - Serial format documentation
- `apple1417-willow2-sdk-mods/command_extensions/builtins/regen_balance.py` - Balance/part list structure
- `apple1417-willow2-sdk-mods/equip_locker/restrictions/allegiance.py` - Manufacturer handling
