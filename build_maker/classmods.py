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


@dataclass
class Cm_Baldef_Classmod_Assassin_01_Common:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_01_Common"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Assassin_02_Uncommon:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_02_Uncommon"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_A | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Assassin_03_Rare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_03_Rare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_B | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Assassin_04_Veryrare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Assassin_04_VeryRare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_C | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


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


@dataclass
class Cm_Baldef_Classmod_Mercenary_01_Common:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_01_Common"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mercenary_02_Uncommon:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_02_Uncommon"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_A | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mercenary_03_Rare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_03_Rare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_B | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mercenary_04_Veryrare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_04_VeryRare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_C | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mercenary_05_Legendary:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mercenary_06_Slayerofterramorphous:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_06_SlayerOfTerramorphous."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Mercenary_06_SlayerOfTerramorphous"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Siren:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Siren_01_Common:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_01_Common"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Siren_02_Uncommon:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_02_Uncommon"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_A | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Siren_03_Rare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_03_Rare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_B | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Siren_04_Veryrare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_04_VeryRare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_C | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Siren_05_Legendary:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Siren_06_Slayerofterramorphous:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_06_SlayerOfTerramorphous."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Siren_06_SlayerOfTerramorphous"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Soldier:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Soldier_01_Common:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_01_Common"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Soldier_02_Uncommon:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_02_Uncommon"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_A | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Soldier_03_Rare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_03_Rare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_B | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Soldier_04_Veryrare:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_04_VeryRare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_C | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Soldier_05_Legendary:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Soldier_06_Slayerofterramorphous:
    """GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_06_SlayerOfTerramorphous."""

    path: ClassVar[str] = "GD_ItemGrades.ClassMods.BalDef_ClassMod_Soldier_06_SlayerOfTerramorphous"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Psycho:
    """GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho."""

    path: ClassVar[str] = "GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Psycho_01_Common:
    """GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_01_Common."""

    path: ClassVar[str] = "GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_01_Common"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Psycho_02_Uncommon:
    """GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_02_Uncommon."""

    path: ClassVar[str] = "GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_02_Uncommon"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_A | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Psycho_03_Rare:
    """GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_03_Rare."""

    path: ClassVar[str] = "GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_03_Rare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_B | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Psycho_04_Veryrare:
    """GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_04_VeryRare."""

    path: ClassVar[str] = "GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_04_VeryRare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_C | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Psycho_05_Legendary:
    """GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_05_Legendary."""

    path: ClassVar[str] = "GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Psycho_06_Slayerofterramorphous:
    """GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_06_SlayerOfTerramorphous."""

    path: ClassVar[str] = "GD_Lilac_ClassMods.BalanceDefs.BalDef_ClassMod_Psycho_06_SlayerOfTerramorphous"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mechromancer:
    """GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer."""

    path: ClassVar[str] = "GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mechromancer_01_Common:
    """GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_01_Common."""

    path: ClassVar[str] = "GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_01_Common"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mechromancer_02_Uncommon:
    """GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_02_Uncommon."""

    path: ClassVar[str] = "GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_02_Uncommon"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_A | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mechromancer_03_Rare:
    """GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_03_Rare."""

    path: ClassVar[str] = "GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_03_Rare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_B | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mechromancer_04_Veryrare:
    """GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_04_VeryRare."""

    path: ClassVar[str] = "GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_04_VeryRare"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec_As_C | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mechromancer_05_Legendary:
    """GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_05_Legendary."""

    path: ClassVar[str] = "GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Mechromancer_06_Slayerofterramorphous:
    """GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_06_SlayerOfTerramorphous."""

    path: ClassVar[str] = "GD_Tulip_ItemGrades.ClassMods.BalDef_ClassMod_Mechromancer_06_SlayerOfTerramorphous"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Aster_Assassin:
    """GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin."""

    path: ClassVar[str] = "GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Assassin"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Aster_Mechromancer:
    """GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer."""

    path: ClassVar[str] = "GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Mechromancer"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Aster_Merc:
    """GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc."""

    path: ClassVar[str] = "GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Merc"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Aster_Psycho:
    """GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho."""

    path: ClassVar[str] = "GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Psycho"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Aster_Siren:
    """GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren."""

    path: ClassVar[str] = "GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Siren"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Aster_Soldier:
    """GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier."""

    path: ClassVar[str] = "GD_Aster_ItemGrades.ClassMods.BalDef_ClassMod_Aster_Soldier"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Lobelia_Assassin_05_Legendary:
    """GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Assassin_05_Legendary."""

    path: ClassVar[str] = "GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Assassin_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Lobelia_Mechromancer_05_Legendary:
    """GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Mechromancer_05_Legendary."""

    path: ClassVar[str] = "GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Mechromancer_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Lobelia_Psycho_05_Legendary:
    """GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Psycho_05_Legendary."""

    path: ClassVar[str] = "GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Psycho_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Lobelia_Siren_05_Legendary:
    """GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Siren_05_Legendary."""

    path: ClassVar[str] = "GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Siren_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Lobelia_Soldier_05_Legendary:
    """GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Soldier_05_Legendary."""

    path: ClassVar[str] = "GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Soldier_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Torgue_Common:
    """GD_Iris_ItemPools.BalDefs.BalDef_ClassMod_Torgue_Common."""

    path: ClassVar[str] = "GD_Iris_ItemPools.BalDefs.BalDef_ClassMod_Torgue_Common"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    specialization: Spec | None = None
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


@dataclass
class Cm_Baldef_Classmod_Lobelia_Merc_05_Legendary:
    """GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Merc_05_Legendary."""

    path: ClassVar[str] = "GD_Lobelia_ItemGrades.ClassMods.BalDef_ClassMod_Lobelia_Merc_05_Legendary"
    class_name: ClassVar[str] = "ClassModBalanceDefinition"
    levels: list[int]
    primary: Primarystat_A | None = None
    secondary: Primarystat02_A0_B | None = None
    penalty: Statpenalty_A0_B0_C | None = None


