from dataclasses import dataclass
from typing import ClassVar

from build_maker.shield_parts import *


@dataclass
class Shield_Itemgrade_Gear_Shield:
    """GD_ItemGrades.Gear.ItemGrade_Gear_Shield."""

    path: ClassVar[str] = "GD_ItemGrades.Gear.ItemGrade_Gear_Shield"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_H | None = None


@dataclass
class Absorb_Shield_Itemgrade_Gear_Shield_Absorption_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Absorption_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Absorption_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_H | None = None


@dataclass
class Booster_Shield_Itemgrade_Gear_Shield_Booster_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Booster_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Booster_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_H | None = None


@dataclass
class Adaptive_Shield_Itemgrade_Gear_Shield_Chimera_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Chimera_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Chimera_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Impact_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Impact_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Impact_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_H | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Impact_Hyperion_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Impact_Hyperion_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Impact_Hyperion_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_H | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Juggernaut_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Juggernaut_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Juggernaut_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_H | None = None


@dataclass
class Turtle_Shield_Itemgrade_Gear_Shield_Juggernaut_Pangolin_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Juggernaut_Pangolin_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Juggernaut_Pangolin_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_H | None = None


@dataclass
class Acid_Nova_Shield_Itemgrade_Gear_Shield_Novaacid_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaAcid_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaAcid_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_K | None = None


@dataclass
class Explosive_Nova_Shield_Itemgrade_Gear_Shield_Novaexplosive_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaExplosive_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaExplosive_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_N | None = None


