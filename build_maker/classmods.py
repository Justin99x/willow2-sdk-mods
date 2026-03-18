from dataclasses import dataclass
from typing import ClassVar

from build_maker.classmod_parts import *


@dataclass
class Cm_Baldef_Classmod_Assassin:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None
    definition: Classmod_Assassin | None = None


@dataclass
class Cm_Baldef_Classmod_Assassin_01_Common:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_01_Common"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None
    definition: Classmod_Assassin | None = None


@dataclass
class Cm_Baldef_Classmod_Assassin_02_Uncommon:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_02_Uncommon"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_C | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None
    definition: Classmod_Assassin | None = None


@dataclass
class Cm_Baldef_Classmod_Assassin_03_Rare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_03_Rare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_A | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None
    definition: Classmod_Assassin | None = None


@dataclass
class Cm_Baldef_Classmod_Assassin_04_Veryrare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_04_VeryRare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_B | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None
    definition: Classmod_Assassin | None = None


@dataclass
class Cm_Baldef_Classmod_Assassin_05_Legendary:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Assassin_06_Slayerofterramorphous:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_06_SlayerOfTerramorphous."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_06_SlayerOfTerramorphous"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mercenary:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None
    definition: Classmod_Merc_A | None = None


@dataclass
class Cm_Baldef_Classmod_Mercenary_01_Common:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_01_Common"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None
    definition: Classmod_Merc_A | None = None


