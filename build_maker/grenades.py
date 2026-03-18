from dataclasses import dataclass
from typing import ClassVar

from build_maker.grenade_parts import *


@dataclass
class Gm_Areaeffect:
    """GD_GrenadeMods.A_Item.GM_AreaEffect."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_AreaEffect"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_A | None = None
    damage: Damage_Grade_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Areaeffect_2_Uncommon:
    """GD_GrenadeMods.A_Item.GM_AreaEffect_2_Uncommon."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_AreaEffect_2_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_B | None = None
    damage: Damage_Grade_B | None = None
    radius: Damageradius_A | None = None
    status_damage: Statusdamage_Grade_B | None = None


@dataclass
class Gm_Areaeffect_3_Rare:
    """GD_GrenadeMods.A_Item.GM_AreaEffect_3_Rare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_AreaEffect_3_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_C | None = None
    damage: Damage_Grade_C | None = None
    radius: Damageradius_A | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Gm_Areaeffect_4_Veryrare:
    """GD_GrenadeMods.A_Item.GM_AreaEffect_4_VeryRare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_AreaEffect_4_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_C | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_B | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Bouncingbetty:
    """GD_GrenadeMods.A_Item.GM_BouncingBetty."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_BouncingBetty"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    child_count: Childcount_Grade_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Bouncingbetty_2_Uncommon:
    """GD_GrenadeMods.A_Item.GM_BouncingBetty_2_Uncommon."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_BouncingBetty_2_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_B | None = None
    child_count: Childcount_Grade_B | None = None
    status_damage: Statusdamage_Grade_B | None = None


@dataclass
class Gm_Bouncingbetty_3_Rare:
    """GD_GrenadeMods.A_Item.GM_BouncingBetty_3_Rare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_BouncingBetty_3_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_F | None = None
    damage: Damage_Grade_C | None = None
    child_count: Childcount_Grade_C | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Gm_Bouncingbetty_4_Veryrare:
    """GD_GrenadeMods.A_Item.GM_BouncingBetty_4_VeryRare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_BouncingBetty_4_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_G | None = None
    damage: Damage_Grade_D | None = None
    child_count: Childcount_Grade_D | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Mirv:
    """GD_GrenadeMods.A_Item.GM_Mirv."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Mirv"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    radius: Damageradius_A | None = None
    child_count: Childcount_Grade_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Mirv_2_Uncommon:
    """GD_GrenadeMods.A_Item.GM_Mirv_2_Uncommon."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Mirv_2_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_B | None = None
    radius: Damageradius_B | None = None
    child_count: Childcount_Grade_B | None = None
    status_damage: Statusdamage_Grade_B | None = None


@dataclass
class Gm_Mirv_3_Rare:
    """GD_GrenadeMods.A_Item.GM_Mirv_3_Rare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Mirv_3_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_F | None = None
    damage: Damage_Grade_C | None = None
    radius: Damageradius_B | None = None
    child_count: Childcount_Grade_E | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Gm_Mirv_4_Veryrare:
    """GD_GrenadeMods.A_Item.GM_Mirv_4_VeryRare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Mirv_4_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_G | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_C | None = None
    child_count: Childcount_Grade_F | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Singularity:
    """GD_GrenadeMods.A_Item.GM_Singularity."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Singularity"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    radius: Damageradius_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Singularity_2_Uncommon:
    """GD_GrenadeMods.A_Item.GM_Singularity_2_Uncommon."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Singularity_2_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_B | None = None
    radius: Damageradius_B | None = None
    status_damage: Statusdamage_Grade_B | None = None


@dataclass
class Gm_Singularity_3_Rare:
    """GD_GrenadeMods.A_Item.GM_Singularity_3_Rare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Singularity_3_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_F | None = None
    damage: Damage_Grade_C | None = None
    radius: Damageradius_B | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Gm_Singularity_4_Veryrare:
    """GD_GrenadeMods.A_Item.GM_Singularity_4_VeryRare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Singularity_4_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_G | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_C | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Standard:
    """GD_GrenadeMods.A_Item.GM_Standard."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Standard"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    radius: Damageradius_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Standard_2_Uncommon:
    """GD_GrenadeMods.A_Item.GM_Standard_2_Uncommon."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Standard_2_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_B | None = None
    radius: Damageradius_B | None = None
    status_damage: Statusdamage_Grade_B | None = None


@dataclass
class Gm_Standard_3_Rare:
    """GD_GrenadeMods.A_Item.GM_Standard_3_Rare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Standard_3_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_F | None = None
    damage: Damage_Grade_C | None = None
    radius: Damageradius_B | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Gm_Standard_4_Veryrare:
    """GD_GrenadeMods.A_Item.GM_Standard_4_VeryRare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Standard_4_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_G | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_C | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Transfusion:
    """GD_GrenadeMods.A_Item.GM_Transfusion."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Transfusion"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    radius: Damageradius_A | None = None
    child_count: Childcount_Grade_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Transfusion_2_Uncommon:
    """GD_GrenadeMods.A_Item.GM_Transfusion_2_Uncommon."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Transfusion_2_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_B | None = None
    radius: Damageradius_B | None = None
    child_count: Childcount_Grade_G | None = None
    status_damage: Statusdamage_Grade_B | None = None


@dataclass
class Gm_Transfusion_3_Rare:
    """GD_GrenadeMods.A_Item.GM_Transfusion_3_Rare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Transfusion_3_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_F | None = None
    damage: Damage_Grade_C | None = None
    radius: Damageradius_B | None = None
    child_count: Childcount_Grade_E | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Gm_Transfusion_4_Veryrare:
    """GD_GrenadeMods.A_Item.GM_Transfusion_4_VeryRare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Transfusion_4_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_G | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_C | None = None
    child_count: Childcount_Grade_F | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Bouncingbetty_Uncommon_Bandit:
    """GD_GrenadeMods.A_Item_Custom.GM_BouncingBetty_Uncommon_Bandit."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Custom.GM_BouncingBetty_Uncommon_Bandit"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_B | None = None
    child_count: Childcount_Grade_B | None = None
    status_damage: Statusdamage_Grade_B | None = None


@dataclass
class Gm_Fustercluck:
    """GD_GrenadeMods.A_Item_Custom.GM_FusterCluck."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Custom.GM_FusterCluck"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    trigger: Trigger_Grade_B | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_C | None = None
    radius: Damageradius_B | None = None
    child_count: Childcount_Grade_A | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Gm_Kissofdeath:
    """GD_GrenadeMods.A_Item_Custom.GM_KissOfDeath."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Custom.GM_KissOfDeath"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    accessory: Accessory_H | None = None
    damage: Damage_Grade_C | None = None
    radius: Damageradius_B | None = None
    child_count: Childcount_Grade_A | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Gm_Mirv_Uncommon_Bandit:
    """GD_GrenadeMods.A_Item_Custom.GM_Mirv_Uncommon_Bandit."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Custom.GM_Mirv_Uncommon_Bandit"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_B | None = None
    radius: Damageradius_B | None = None
    child_count: Childcount_Grade_B | None = None
    status_damage: Statusdamage_Grade_B | None = None


@dataclass
class Gm_Skyrocket:
    """GD_GrenadeMods.A_Item_Custom.GM_SkyRocket."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Custom.GM_SkyRocket"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]


@dataclass
class Gm_Standard_Uncommon_Bandit:
    """GD_GrenadeMods.A_Item_Custom.GM_Standard_Uncommon_Bandit."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Custom.GM_Standard_Uncommon_Bandit"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_B | None = None
    radius: Damageradius_B | None = None
    status_damage: Statusdamage_Grade_B | None = None


@dataclass
class Gm_Bonuspackage:
    """GD_GrenadeMods.A_Item_Legendary.GM_BonusPackage."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_BonusPackage"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_C | None = None
    damage: Damage_Grade_E | None = None
    radius: Damageradius_C | None = None
    child_count: Childcount_Grade_H | None = None


@dataclass
class Gm_Bouncingbonny:
    """GD_GrenadeMods.A_Item_Legendary.GM_BouncingBonny."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_BouncingBonny"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_C | None = None
    accessory: Accessory_G | None = None
    damage: Damage_Grade_D | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Fastball:
    """GD_GrenadeMods.A_Item_Legendary.GM_Fastball."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_Fastball"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    accessory: Accessory_H | None = None
    damage: Damage_Grade_F | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Firebee:
    """GD_GrenadeMods.A_Item_Legendary.GM_FireBee."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_FireBee"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_C | None = None
    accessory: Accessory_Incendiary_Grade_A | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_B | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Flamespurt:
    """GD_GrenadeMods.A_Item_Legendary.GM_FlameSpurt."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_FlameSpurt"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_C | None = None
    accessory: Accessory_Incendiary_Grade_B | None = None
    damage: Damage_Grade_A | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Leech:
    """GD_GrenadeMods.A_Item_Legendary.GM_Leech."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_Leech"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_C | None = None
    accessory: Accessory_C | None = None
    damage: Damage_Grade_D | None = None
    child_count: Childcount_Grade_A | None = None
    status_damage: Statusdamage_Grade_E | None = None


@dataclass
class Gm_Nastysurprise:
    """GD_GrenadeMods.A_Item_Legendary.GM_NastySurprise."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_NastySurprise"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    trigger: Trigger_Grade_B | None = None
    accessory: Accessory_G | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_C | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Pandemic:
    """GD_GrenadeMods.A_Item_Legendary.GM_Pandemic."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_Pandemic"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_C | None = None
    accessory: Accessory_Corrosive_Grade | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_B | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Quasar:
    """GD_GrenadeMods.A_Item_Legendary.GM_Quasar."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_Quasar"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_C | None = None
    accessory: Accessory_Shock_Grade_A | None = None
    damage: Damage_Grade_D | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Rollingthunder:
    """GD_GrenadeMods.A_Item_Legendary.GM_RollingThunder."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_RollingThunder"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    trigger: Trigger_Grade_D | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_D | None = None
    child_count: Childcount_Grade_E | None = None


@dataclass
class Gm_Stormfront:
    """GD_GrenadeMods.A_Item_Legendary.GM_StormFront."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item_Legendary.GM_StormFront"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_C | None = None
    accessory: Accessory_Shock_Grade_B | None = None
    damage: Damage_Grade_D | None = None
    radius: Damageradius_B | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Areaeffect_1_Nointerp:
    """GD_Population_Marauder.ItemBalance.GM_AreaEffect_1_NoInterp."""

    path: ClassVar[str] = "GD_Population_Marauder.ItemBalance.GM_AreaEffect_1_NoInterp"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_A | None = None
    damage: Damage_Grade_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Bouncingbetty_1_Nointerp:
    """GD_Population_Marauder.ItemBalance.GM_BouncingBetty_1_NoInterp."""

    path: ClassVar[str] = "GD_Population_Marauder.ItemBalance.GM_BouncingBetty_1_NoInterp"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    child_count: Childcount_Grade_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Mirv_1_Nointerp:
    """GD_Population_Marauder.ItemBalance.GM_Mirv_1_NoInterp."""

    path: ClassVar[str] = "GD_Population_Marauder.ItemBalance.GM_Mirv_1_NoInterp"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    radius: Damageradius_A | None = None
    child_count: Childcount_Grade_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Singularity_1_Nointerp:
    """GD_Population_Marauder.ItemBalance.GM_Singularity_1_NoInterp."""

    path: ClassVar[str] = "GD_Population_Marauder.ItemBalance.GM_Singularity_1_NoInterp"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    radius: Damageradius_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Standard_1_Nointerp:
    """GD_Population_Marauder.ItemBalance.GM_Standard_1_NoInterp."""

    path: ClassVar[str] = "GD_Population_Marauder.ItemBalance.GM_Standard_1_NoInterp"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    radius: Damageradius_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Transfusion_1_Nointerp:
    """GD_Population_Marauder.ItemBalance.GM_Transfusion_1_NoInterp."""

    path: ClassVar[str] = "GD_Population_Marauder.ItemBalance.GM_Transfusion_1_NoInterp"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_A | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_A | None = None
    radius: Damageradius_A | None = None
    child_count: Childcount_Grade_A | None = None
    status_damage: Statusdamage_Grade_A | None = None


@dataclass
class Gm_Standard_3_Rare_Flamer:
    """GD_Anemone_GrenadeMods.A_Item.GM_Standard_3_Rare_Flamer."""

    path: ClassVar[str] = "GD_Anemone_GrenadeMods.A_Item.GM_Standard_3_Rare_Flamer"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    trigger: Trigger_Grade_E | None = None
    accessory: Accessory_Incendiary | None = None
    damage: Damage_Grade_G | None = None
    radius: Damageradius_E | None = None
    status_damage: Statusdamage_Grade_F | None = None


@dataclass
class Gm_Antifection:
    """GD_Anemone_GrenadeMods.A_Item_Legendary.GM_Antifection."""

    path: ClassVar[str] = "GD_Anemone_GrenadeMods.A_Item_Legendary.GM_Antifection"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    trigger: Trigger_Grade_F | None = None
    accessory: Accessory_Incendiary_Grade_C | None = None
    damage: Damage_Grade_H | None = None
    radius: Damageradius_E | None = None
    status_damage: Statusdamage_Grade_G | None = None


@dataclass
class Gm_Antifection_Turret:
    """GD_Anemone_GrenadeMods.A_Item_Legendary.GM_Antifection_Turret."""

    path: ClassVar[str] = "GD_Anemone_GrenadeMods.A_Item_Legendary.GM_Antifection_Turret"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    trigger: Trigger_Grade_F | None = None
    accessory: Accessory_Incendiary_Grade_C | None = None
    damage: Damage_Grade_H | None = None
    radius: Damageradius_E | None = None
    status_damage: Statusdamage_Grade_G | None = None


@dataclass
class Gm_Chainlightning:
    """GD_Aster_GrenadeMods.A_Item.GM_ChainLightning."""

    path: ClassVar[str] = "GD_Aster_GrenadeMods.A_Item.GM_ChainLightning"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    damage: Damage_Grade_C | None = None
    status_damage: Statusdamage_Grade_H | None = None


@dataclass
class Gm_Fireball:
    """GD_Aster_GrenadeMods.A_Item.GM_Fireball."""

    path: ClassVar[str] = "GD_Aster_GrenadeMods.A_Item.GM_Fireball"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    damage: Damage_Grade_C | None = None
    status_damage: Statusdamage_Grade_H | None = None


@dataclass
class Gm_Firestorm:
    """GD_Aster_GrenadeMods.A_Item.GM_FireStorm."""

    path: ClassVar[str] = "GD_Aster_GrenadeMods.A_Item.GM_FireStorm"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    damage: Damage_Grade_C | None = None
    status_damage: Statusdamage_Grade_H | None = None


@dataclass
class Gm_Lightningbolt:
    """GD_Aster_GrenadeMods.A_Item.GM_LightningBolt."""

    path: ClassVar[str] = "GD_Aster_GrenadeMods.A_Item.GM_LightningBolt"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    damage: Damage_Grade_C | None = None
    status_damage: Statusdamage_Grade_H | None = None


@dataclass
class Gm_Magicmissile:
    """GD_Aster_GrenadeMods.A_Item.GM_MagicMissile."""

    path: ClassVar[str] = "GD_Aster_GrenadeMods.A_Item.GM_MagicMissile"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    damage: Damage_Grade_C | None = None
    status_damage: Statusdamage_Grade_H | None = None


@dataclass
class Gm_Magicmissilerare:
    """GD_Aster_GrenadeMods.A_Item.GM_MagicMissileRare."""

    path: ClassVar[str] = "GD_Aster_GrenadeMods.A_Item.GM_MagicMissileRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    damage: Damage_Grade_C | None = None
    status_damage: Statusdamage_Grade_H | None = None


@dataclass
class Iris_Seraph_Grenademod_Crossfire_Balance:
    """GD_Iris_SeraphItems.Crossfire.Iris_Seraph_GrenadeMod_Crossfire_Balance."""

    path: ClassVar[str] = "GD_Iris_SeraphItems.Crossfire.Iris_Seraph_GrenadeMod_Crossfire_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_C | None = None
    accessory: Accessory_G | None = None
    damage: Iris_Seraph_Grenademod_Crossfire_Part_Damage | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Iris_Seraph_Grenademod_Meteorshower_Balance:
    """GD_Iris_SeraphItems.MeteorShower.Iris_Seraph_GrenadeMod_MeteorShower_Balance."""

    path: ClassVar[str] = "GD_Iris_SeraphItems.MeteorShower.Iris_Seraph_GrenadeMod_MeteorShower_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_G | None = None
    damage: Iris_Seraph_Grenademod_Meteorshower_Part_Damage | None = None
    radius: Damageradius_C | None = None
    child_count: Childcount_Grade_H | None = None


@dataclass
class Iris_Seraph_Grenademod_Onegative_Balance:
    """GD_Iris_SeraphItems.ONegative.Iris_Seraph_GrenadeMod_ONegative_Balance."""

    path: ClassVar[str] = "GD_Iris_SeraphItems.ONegative.Iris_Seraph_GrenadeMod_ONegative_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_H | None = None
    accessory: Accessory_G | None = None
    damage: Iris_Seraph_Grenademod_Onegative_Part_Damage | None = None
    radius: Damageradius_C | None = None
    child_count: Childcount_Grade_F | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Gm_Blade:
    """GD_Orchid_GrenadeMods.A_Item_Custom.GM_Blade."""

    path: ClassVar[str] = "GD_Orchid_GrenadeMods.A_Item_Custom.GM_Blade"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    trigger: Trigger_Grade_I | None = None
    damage: Damage_Grade_C | None = None
    radius: Damageradius_B | None = None
    child_count: Childcount_Grade_F | None = None
    status_damage: Statusdamage_Grade_C | None = None


