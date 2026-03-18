from dataclasses import dataclass
from typing import ClassVar

from build_maker.weapon_parts import *


@dataclass
class Repeater_Pistol_Dahl_Starter:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_Starter."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_Starter"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]


@dataclass
class Lascaux_Smg_Dahl_3_Lascaux:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Lascaux."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Lascaux"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_E | None = None


@dataclass
class Gwen_S_Head_Pistol_Dahl_3_Gwenshead:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensHead."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensHead"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    sight: Pistol_Sight_C | None = None
    element: Pistol_Elemental_B | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Bad_Touch_Smg_Maliwan_3_Badtouch:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_E | None = None


@dataclass
class Good_Touch_Smg_Maliwan_3_Goodtouch:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_E | None = None


@dataclass
class Coach_Gun_Sg_Jakobs:
    """GD_Weap_Shotgun.A_Weapons.SG_Jakobs."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Jakobs"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_A | None = None
    stock: Sg_Stock | None = None


@dataclass
class Revolver_Pistol_Jakobs:
    """GD_Weap_Pistol.A_Weapons.Pistol_Jakobs."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Jakobs"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    barrel: Pistol_Barrel_C | None = None


@dataclass
class Repeater_Pistol_Dahl:
    """GD_Weap_Pistol.A_Weapons.Pistol_Dahl."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Dahl"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_C | None = None


@dataclass
class Troublemaker_Pistol_Vladof:
    """GD_Weap_Pistol.A_Weapons.Pistol_Vladof."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Vladof"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    barrel: Pistol_Barrel_C | None = None


@dataclass
class Judge_Pistol_Jakobs_3_Judge:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Judge."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Judge"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    sight: Pistol_Sight_C | None = None
    accessory1: Pistol_Accessory_A | None = None


