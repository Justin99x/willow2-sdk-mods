from dataclasses import dataclass
from typing import ClassVar

from build_maker.shield_parts import *


@dataclass
class Shield_Itemgrade_Gear_Shield:
    """GD_ItemGrades.Gear.ItemGrade_Gear_Shield."""

    path: ClassVar[str] = "GD_ItemGrades.Gear.ItemGrade_Gear_Shield"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material_A | None = None


@dataclass
class Absorb_Shield_Itemgrade_Gear_Shield_Absorption_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Absorption_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Absorption_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Booster_Shield_Itemgrade_Gear_Shield_Booster_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Booster_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Booster_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Adaptive_Shield_Itemgrade_Gear_Shield_Chimera_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Chimera_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Chimera_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_B | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Impact_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Impact_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Impact_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Impact_Hyperion_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Impact_Hyperion_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Impact_Hyperion_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Juggernaut_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Juggernaut_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Juggernaut_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Turtle_Shield_Itemgrade_Gear_Shield_Juggernaut_Pangolin_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Juggernaut_Pangolin_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Juggernaut_Pangolin_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Acid_Nova_Shield_Itemgrade_Gear_Shield_Novaacid_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaAcid_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaAcid_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Explosive_Nova_Shield_Itemgrade_Gear_Shield_Novaexplosive_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaExplosive_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaExplosive_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Fire_Nova_Shield_Itemgrade_Gear_Shield_Novafire_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaFire_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaFire_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Shock_Nova_Shield_Itemgrade_Gear_Shield_Novashock_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaShock_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_NovaShock_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Maylay_Shield_Itemgrade_Gear_Shield_Roid_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Roid_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Roid_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Corrosive_Spike_Shield_Itemgrade_Gear_Shield_Spikeacid_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_SpikeAcid_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_SpikeAcid_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Explosive_Spike_Shield_Itemgrade_Gear_Shield_Spikeexplosive_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_SpikeExplosive_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_SpikeExplosive_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Fire_Spike_Shield_Itemgrade_Gear_Shield_Spikefire_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_SpikeFire_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_SpikeFire_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Shock_Spike_Shield_Itemgrade_Gear_Shield_Spikeshock_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_SpikeShock_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_SpikeShock_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Shield_Itemgrade_Gear_Shield_Standard_Dahl_02_Uncommon:
    """GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Standard_Dahl_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.MissionRewards.ItemGrade_Gear_Shield_Standard_Dahl_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material2_Uncommon | None = None


@dataclass
class Absorb_Shield_Itemgrade_Gear_Shield_Absorption_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Absorb_Shield_Itemgrade_Gear_Shield_Absorption_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Absorb_Shield_Itemgrade_Gear_Shield_Absorption_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Absorb_Shield_Itemgrade_Gear_Shield_Absorption_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class The_Sham_Itemgrade_Gear_Shield_Absorption_05_Legendarynormal:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryNormal."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryNormal"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_B | None = None
    battery: Battery_B | None = None
    capacitor: Capacitor_G | None = None


@dataclass
class The_Transformer_Itemgrade_Gear_Shield_Absorption_05_Legendaryshock:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryShock."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_05_LegendaryShock"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None


@dataclass
class _1340_Shield_Itemgrade_Gear_Shield_Absorption_1340:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_1340."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_1340"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Aequitas_Itemgrade_Gear_Shield_Absorption_Equitas:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_Equitas."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Absorption_Equitas"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Booster_Shield_Itemgrade_Gear_Shield_Booster_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Booster_Shield_Itemgrade_Gear_Shield_Booster_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Booster_Shield_Itemgrade_Gear_Shield_Booster_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Booster_Shield_Itemgrade_Gear_Shield_Booster_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Whisky_Tango_Foxtrot_Itemgrade_Gear_Shield_Booster_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_C | None = None
    battery: Battery_C | None = None
    capacitor: Capacitor_H | None = None


@dataclass
class Pot_O_Gold_Itemgrade_Gear_Shield_Booster_Potogold:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_PotOGold."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Booster_PotOGold"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_D | None = None
    battery: Battery_D | None = None
    capacitor: Capacitor_I | None = None


@dataclass
class Adaptive_Shield_Itemgrade_Gear_Shield_Chimera_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_B | None = None


@dataclass
class Adaptive_Shield_Itemgrade_Gear_Shield_Chimera_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_B | None = None


@dataclass
class Adaptive_Shield_Itemgrade_Gear_Shield_Chimera_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_B | None = None


@dataclass
class Adaptive_Shield_Itemgrade_Gear_Shield_Chimera_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_B | None = None


@dataclass
class Neogenator_Itemgrade_Gear_Shield_Chimera_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Chimera_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_E | None = None
    battery: Battery_E | None = None
    capacitor: Capacitor_J | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Impact_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Impact_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Impact_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Amplify_Shield_Itemgrade_Gear_Shield_Impact_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class The_Bee_Itemgrade_Gear_Shield_Impact_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Impact_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    battery: Battery_F | None = None
    capacitor: Capacitor_K | None = None


@dataclass
class Turtle_Shield_Itemgrade_Gear_Shield_Juggernaut_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Turtle_Shield_Itemgrade_Gear_Shield_Juggernaut_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Turtle_Shield_Itemgrade_Gear_Shield_Juggernaut_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Turtle_Shield_Itemgrade_Gear_Shield_Juggernaut_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Fabled_Tortoise_Itemgrade_Gear_Shield_Juggernaut_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Juggernaut_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_F | None = None
    battery: Body_F | None = None
    capacitor: Capacitor_L | None = None


@dataclass
class Acid_Nova_Shield_Itemgrade_Gear_Shield_Nova_Acid_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Acid_Nova_Shield_Itemgrade_Gear_Shield_Nova_Acid_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Acid_Nova_Shield_Itemgrade_Gear_Shield_Nova_Acid_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Acid_Nova_Shield_Itemgrade_Gear_Shield_Nova_Acid_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Acid_Nova_Shield_Itemgrade_Gear_Shield_Nova_Acid_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Acid_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Explosive_Nova_Shield_Itemgrade_Gear_Shield_Nova_Explosive_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Explosive_Nova_Shield_Itemgrade_Gear_Shield_Nova_Explosive_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Explosive_Nova_Shield_Itemgrade_Gear_Shield_Nova_Explosive_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Explosive_Nova_Shield_Itemgrade_Gear_Shield_Nova_Explosive_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Deadly_Bloom_Itemgrade_Gear_Shield_Nova_Explosive_Deadlybloom:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_DeadlyBloom."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Explosive_DeadlyBloom"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Fire_Nova_Shield_Itemgrade_Gear_Shield_Nova_Fire_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Fire_Nova_Shield_Itemgrade_Gear_Shield_Nova_Fire_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Fire_Nova_Shield_Itemgrade_Gear_Shield_Nova_Fire_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Fire_Nova_Shield_Itemgrade_Gear_Shield_Nova_Fire_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Fire_Nova_Shield_Itemgrade_Gear_Shield_Nova_Fire_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Fire_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Flame_Of_The_Firehawk_Itemgrade_Gear_Shield_Nova_Phoenix:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Phoenix."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Phoenix"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Shock_Nova_Shield_Itemgrade_Gear_Shield_Nova_Shock_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Shock_Nova_Shield_Itemgrade_Gear_Shield_Nova_Shock_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Shock_Nova_Shield_Itemgrade_Gear_Shield_Nova_Shock_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Shock_Nova_Shield_Itemgrade_Gear_Shield_Nova_Shock_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Shock_Nova_Shield_Itemgrade_Gear_Shield_Nova_Shock_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Shock_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Black_Hole_Itemgrade_Gear_Shield_Nova_Singularity:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Singularity."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Nova_Singularity"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Maylay_Shield_Itemgrade_Gear_Shield_Roid_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Maylay_Shield_Itemgrade_Gear_Shield_Roid_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Maylay_Shield_Itemgrade_Gear_Shield_Roid_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Love_Thumper_Itemgrade_Gear_Shield_Roid_04_Lovethumper:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_04_LoveThumper."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_04_LoveThumper"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Maylay_Shield_Itemgrade_Gear_Shield_Roid_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Maylay_Shield_Itemgrade_Gear_Shield_Roid_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    material: Material_B | None = None


@dataclass
class Order_Itemgrade_Gear_Shield_Roid_Order:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_Order."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_Order"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_C | None = None
    battery: Battery_C | None = None
    capacitor: Capacitor_H | None = None


@dataclass
class Hide_Of_Terramorphous_Itemgrade_Gear_Shield_Roid_Thresherraid:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_ThresherRaid."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Roid_ThresherRaid"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None
    accessory: Accessory9_0 | None = None


@dataclass
class Corrosive_Spike_Shield_Itemgrade_Gear_Shield_Spike_Acid_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Corrosive_Spike_Shield_Itemgrade_Gear_Shield_Spike_Acid_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Corrosive_Spike_Shield_Itemgrade_Gear_Shield_Spike_Acid_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Corrosive_Spike_Shield_Itemgrade_Gear_Shield_Spike_Acid_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Impaler_Itemgrade_Gear_Shield_Spike_Acid_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Acid_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_C | None = None


@dataclass
class Explosive_Spike_Shield_Itemgrade_Gear_Shield_Spike_Explosive_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Explosive_Spike_Shield_Itemgrade_Gear_Shield_Spike_Explosive_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Explosive_Spike_Shield_Itemgrade_Gear_Shield_Spike_Explosive_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Explosive_Spike_Shield_Itemgrade_Gear_Shield_Spike_Explosive_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Explosive_Spike_Shield_Itemgrade_Gear_Shield_Spike_Explosive_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Explosive_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_D | None = None


@dataclass
class Fire_Spike_Shield_Itemgrade_Gear_Shield_Spike_Fire_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Fire_Spike_Shield_Itemgrade_Gear_Shield_Spike_Fire_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Fire_Spike_Shield_Itemgrade_Gear_Shield_Spike_Fire_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Fire_Spike_Shield_Itemgrade_Gear_Shield_Spike_Fire_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Fire_Spike_Shield_Itemgrade_Gear_Shield_Spike_Fire_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Fire_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_E | None = None


@dataclass
class Shock_Spike_Shield_Itemgrade_Gear_Shield_Spike_Shock_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Shock_Spike_Shield_Itemgrade_Gear_Shield_Spike_Shock_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Shock_Spike_Shield_Itemgrade_Gear_Shield_Spike_Shock_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Shock_Spike_Shield_Itemgrade_Gear_Shield_Spike_Shock_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Shock_Spike_Shield_Itemgrade_Gear_Shield_Spike_Shock_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Spike_Shock_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Shield_Itemgrade_Gear_Shield_Standard_01_Common:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_01_Common."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_01_Common"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Shield_Itemgrade_Gear_Shield_Standard_02_Uncommon:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_02_Uncommon."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_02_Uncommon"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Shield_Itemgrade_Gear_Shield_Standard_03_Rare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_03_Rare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_03_Rare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Shield_Itemgrade_Gear_Shield_Standard_04_Veryrare:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_04_VeryRare."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_04_VeryRare"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class The_Cradle_Itemgrade_Gear_Shield_Standard_05_Legendary:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_05_Legendary."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_05_Legendary"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Cracked_Sash_Itemgrade_Gear_Shield_Standard_Crackedsash:
    """GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_CrackedSash."""

    path: ClassVar[str] = "GD_ItemGrades.Shields.ItemGrade_Gear_Shield_Standard_CrackedSash"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_G | None = None
    battery: Battery_G | None = None
    capacitor: Capacitor_M | None = None


@dataclass
class Retainer_Itemgrade_Gear_Shield_Worming:
    """GD_Anemone_Balance_Treasure.Shields.ItemGrade_Gear_Shield_Worming."""

    path: ClassVar[str] = "GD_Anemone_Balance_Treasure.Shields.ItemGrade_Gear_Shield_Worming"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_H | None = None
    battery: Battery_H | None = None


@dataclass
class Easy_Mode_Itemgrade_Gear_Shield_Nova_Singularity_Peak:
    """GD_Anemone_ItemPools.Shields.ItemGrade_Gear_Shield_Nova_Singularity_Peak."""

    path: ClassVar[str] = "GD_Anemone_ItemPools.Shields.ItemGrade_Gear_Shield_Nova_Singularity_Peak"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_F | None = None


@dataclass
class Antagonist_Aster_Seraph_Antagonist_Shield_Balance:
    """GD_Aster_ItemGrades.Shields.Aster_Seraph_Antagonist_Shield_Balance."""

    path: ClassVar[str] = "GD_Aster_ItemGrades.Shields.Aster_Seraph_Antagonist_Shield_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_B | None = None


@dataclass
class Blockade_Aster_Seraph_Blockade_Shield_Balance:
    """GD_Aster_ItemGrades.Shields.Aster_Seraph_Blockade_Shield_Balance."""

    path: ClassVar[str] = "GD_Aster_ItemGrades.Shields.Aster_Seraph_Blockade_Shield_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_B | None = None


@dataclass
class Booster_Shield_Iris_Seraph_Shield_Booster_Balance:
    """GD_Iris_SeraphItems.BigBoomBlaster.Iris_Seraph_Shield_Booster_Balance."""

    path: ClassVar[str] = "GD_Iris_SeraphItems.BigBoomBlaster.Iris_Seraph_Shield_Booster_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Turtle_Shield_Iris_Seraph_Shield_Juggernaut_Balance:
    """GD_Iris_SeraphItems.Hoplite.Iris_Seraph_Shield_Juggernaut_Balance."""

    path: ClassVar[str] = "GD_Iris_SeraphItems.Hoplite.Iris_Seraph_Shield_Juggernaut_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_F | None = None
    battery: Body_F | None = None
    capacitor: Capacitor_L | None = None


@dataclass
class Pun_Chee_Iris_Seraph_Shield_Pun_Chee_Balance:
    """GD_Iris_SeraphItems.Pun-chee.Iris_Seraph_Shield_Pun-chee_Balance."""

    path: ClassVar[str] = "GD_Iris_SeraphItems.Pun-chee.Iris_Seraph_Shield_Pun-chee_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Sponge_Iris_Seraph_Shield_Sponge_Balance:
    """GD_Iris_SeraphItems.Sponge.Iris_Seraph_Shield_Sponge_Balance."""

    path: ClassVar[str] = "GD_Iris_SeraphItems.Sponge.Iris_Seraph_Shield_Sponge_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_A | None = None
    battery: Battery_A | None = None
    capacitor: Capacitor_A | None = None


@dataclass
class Evolution_Orchid_Seraph_Anshin_Shield_Balance:
    """GD_Orchid_RaidWeapons.Shield.Anshin.Orchid_Seraph_Anshin_Shield_Balance."""

    path: ClassVar[str] = "GD_Orchid_RaidWeapons.Shield.Anshin.Orchid_Seraph_Anshin_Shield_Balance"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_E | None = None
    battery: Battery_E | None = None
    capacitor: Capacitor_J | None = None


@dataclass
class Captain_Blade_S_Manly_Man_Shield_S_Bladeshield:
    """GD_Orchid_Shields.A_Item_Custom.S_BladeShield."""

    path: ClassVar[str] = "GD_Orchid_Shields.A_Item_Custom.S_BladeShield"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_I | None = None
    battery: Battery_I | None = None
    capacitor: Capacitor_B | None = None


@dataclass
class The_Rough_Rider_S_Bucklershield:
    """GD_Sage_Shields.A_Item_Custom.S_BucklerShield."""

    path: ClassVar[str] = "GD_Sage_Shields.A_Item_Custom.S_BucklerShield"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]
    body: Body_J | None = None
    battery: Battery_J | None = None
    capacitor: Capacitor_N | None = None


@dataclass
class Shield_Itemgrade_Gear_Shield_Enemy_Standard:
    """GD_ItemGrades.Shields_Enemy.ItemGrade_Gear_Shield_Enemy_Standard."""

    path: ClassVar[str] = "GD_ItemGrades.Shields_Enemy.ItemGrade_Gear_Shield_Enemy_Standard"
    class_name: ClassVar[str] = "InventoryBalanceDefinition"
    levels: list[int]


