from dataclasses import dataclass
from typing import ClassVar

from build_maker.grenade_parts import *


@dataclass
class Tesla_Gm_Areaeffect:
    """GD_GrenadeMods.A_Item.GM_AreaEffect."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_AreaEffect"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_F | None = None
    damage: Damage_Grade_H | None = None
    status_damage: Statusdamage_Grade_F | None = None


@dataclass
class Fire_Burst_Gm_Areaeffect_2_Uncommon:
    """GD_GrenadeMods.A_Item.GM_AreaEffect_2_Uncommon."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_AreaEffect_2_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_A | None = None
    damage: Damage_Grade_E | None = None
    radius: Damageradius_E | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Tesla_Gm_Areaeffect_3_Rare:
    """GD_GrenadeMods.A_Item.GM_AreaEffect_3_Rare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_AreaEffect_3_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_B | None = None
    damage: Damage_Grade_B | None = None
    radius: Damageradius_E | None = None
    status_damage: Statusdamage_Grade_E | None = None


@dataclass
class Tesla_Gm_Areaeffect_4_Veryrare:
    """GD_GrenadeMods.A_Item.GM_AreaEffect_4_VeryRare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_AreaEffect_4_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_B | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_B | None = None
    damage: Damage_Grade_G | None = None
    radius: Damageradius_C | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Bouncing_Betty_Gm_Bouncingbetty:
    """GD_GrenadeMods.A_Item.GM_BouncingBetty."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_BouncingBetty"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_H | None = None
    child_count: Childcount_Grade_E | None = None
    status_damage: Statusdamage_Grade_F | None = None


@dataclass
class Lectrik_Jumpin_Bitty_Gm_Bouncingbetty_2_Uncommon:
    """GD_GrenadeMods.A_Item.GM_BouncingBetty_2_Uncommon."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_BouncingBetty_2_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_C | None = None
    damage: Damage_Grade_E | None = None
    child_count: Childcount_Grade_H | None = None
    status_damage: Statusdamage_Grade_D | None = None


@dataclass
class Jumpin_Bitty_Gm_Bouncingbetty_3_Rare:
    """GD_GrenadeMods.A_Item.GM_BouncingBetty_3_Rare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_BouncingBetty_3_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_H | None = None
    damage: Damage_Grade_B | None = None
    child_count: Childcount_Grade_C | None = None
    status_damage: Statusdamage_Grade_E | None = None


@dataclass
class Incendiary_Bouncing_Betty_Gm_Bouncingbetty_4_Veryrare:
    """GD_GrenadeMods.A_Item.GM_BouncingBetty_4_VeryRare."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_BouncingBetty_4_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_D | None = None
    damage: Damage_Grade_G | None = None
    child_count: Childcount_Grade_G | None = None
    status_damage: Statusdamage_Grade_C | None = None


@dataclass
class Mirv_Gm_Mirv:
    """GD_GrenadeMods.A_Item.GM_Mirv."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Mirv"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_A | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_E | None = None
    damage: Damage_Grade_H | None = None
    radius: Damageradius_E | None = None
    child_count: Childcount_Grade_E | None = None
    status_damage: Statusdamage_Grade_F | None = None


@dataclass
class Mirv_Gm_Mirv_2_Uncommon:
    """GD_GrenadeMods.A_Item.GM_Mirv_2_Uncommon."""

    path: ClassVar[str] = "GD_GrenadeMods.A_Item.GM_Mirv_2_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    delivery: Delivery_C | None = None
    trigger: Trigger_Grade_G | None = None
    accessory: Accessory_C | None = None
    damage: Damage_Grade_E | None = None
    radius: Damageradius_C | None = None
    child_count: Childcount_Grade_H | None = None
    status_damage: Statusdamage_Grade_D | None = None


