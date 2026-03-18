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
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Gwen_S_Head_Pistol_Dahl_3_Gwenshead:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensHead."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_GwensHead"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Bad_Touch_Smg_Maliwan_3_Badtouch:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_BadTouch"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Good_Touch_Smg_Maliwan_3_Goodtouch:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_GoodTouch"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Scattergun_Sg_Jakobs:
    """GD_Weap_Shotgun.A_Weapons.SG_Jakobs."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Jakobs"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_A | None = None
    stock: Sg_Stock | None = None


@dataclass
class Widow_Maker_Pistol_Jakobs:
    """GD_Weap_Pistol.A_Weapons.Pistol_Jakobs."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Jakobs"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    barrel: Pistol_Barrel_A | None = None


@dataclass
class Repeater_Pistol_Dahl:
    """GD_Weap_Pistol.A_Weapons.Pistol_Dahl."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Dahl"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_A | None = None


@dataclass
class Tmp_Pistol_Vladof:
    """GD_Weap_Pistol.A_Weapons.Pistol_Vladof."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Vladof"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    barrel: Pistol_Barrel_A | None = None


@dataclass
class Judge_Pistol_Jakobs_3_Judge:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Judge."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Judge"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Fremington_S_Edge_Sniper_Hyperion_3_Fremingtonsedge:
    """GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_FremingtonsEdge"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Dog_Sg_Bandit_3_Dog:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Dog."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Dog"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_A | None = None


@dataclass
class Commerce_Smg_Hyperion_3_Commerce:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Commerce."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Commerce"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Shotgun_Sg_Bandit_5_Sledgesshotgun:
    """GD_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Bandit_5_SledgesShotgun"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_B | None = None


@dataclass
class Nukem_Rl_Torgue_5_Nukem:
    """GD_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons_Legendary.RL_Torgue_5_Nukem"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Bone_Shredder_Smg_Bandit_3_Boneshredder:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_BoneShredder."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Bandit_3_BoneShredder"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_B | None = None


@dataclass
class Bitch_Smg_Hyperion_5_Bitch:
    """GD_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Legendary.SMG_Hyperion_5_Bitch"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Thunderball_Fists_Pistol_Maliwan_5_Thunderballfists:
    """GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Maliwan_5_ThunderballFists."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Maliwan_5_ThunderballFists"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Tinderbox_Pistol_Bandit_3_Tenderbox:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Bandit_3_Tenderbox."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Bandit_3_Tenderbox"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_C | None = None


@dataclass
class Bunny_Rl_Tediore_5_Bunny:
    """GD_Weap_Launchers.A_Weapons_Legendary.RL_Tediore_5_Bunny."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons_Legendary.RL_Tediore_5_Bunny"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Pyrophobia_Rl_Maliwan_5_Pyrophobia:
    """GD_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Pyrophobia."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons_Legendary.RL_Maliwan_5_Pyrophobia"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Emperor_Smg_Dahl_5_Emperor:
    """GD_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Emperor."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Legendary.SMG_Dahl_5_Emperor"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Lyudmila_Sniper_Vladof_5_Lyudmila:
    """GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Lyudmila."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Vladof_5_Lyudmila"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Badaboom_Rl_Bandit_5_Badaboom:
    """GD_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons_Legendary.RL_Bandit_5_BadaBoom"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Hornet_Pistol_Dahl_5_Hornet:
    """GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Hornet."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Dahl_5_Hornet"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Gub_Pistol_Bandit_5_Gub:
    """GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Gub."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Bandit_5_Gub"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_D | None = None


@dataclass
class Baby_Maker_Smg_Tediore_5_Babymaker:
    """GD_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_BabyMaker."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Legendary.SMG_Tediore_5_BabyMaker"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Madhous_Ar_Bandit_5_Madhouse:
    """GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Bandit_5_Madhouse."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Bandit_5_Madhouse"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Hammer_Buster_Ar_Jakobs_5_Hammerbuster:
    """GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBuster."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Jakobs_5_HammerBuster"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Maggie_Pistol_Jakobs_5_Maggie:
    """GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Jakobs_5_Maggie"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Veruc_Ar_Dahl_5_Veruc:
    """GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Dahl_5_Veruc."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Dahl_5_Veruc"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Infinity_Pistol_Vladof_5_Infinity:
    """GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Vladof_5_Infinity."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Vladof_5_Infinity"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_B | None = None
    accessory1: Pistol_Accessory_E | None = None


@dataclass
class Striker_Sg_Jakobs_5_Striker:
    """GD_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Jakobs_5_Striker"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Gunerang_Pistol_Tediore_5_Gunerang:
    """GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Gunerang."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Tediore_5_Gunerang"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Unkempt_Harold_Pistol_Torgue_5_Calla:
    """GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_Calla."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Torgue_5_Calla"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_D | None = None


@dataclass
class Hellfire_Smg_Maliwan_5_Hellfire:
    """GD_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Legendary.SMG_Maliwan_5_HellFire"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Law_Pistol_Jakobs_3_Law:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Law."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Jakobs_3_Law"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    sight: Pistol_Sight_A | None = None


@dataclass
class Mongol_Rl_Vladof_5_Mongol:
    """GD_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons_Legendary.RL_Vladof_5_Mongol"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Skullmasher_Sniper_Jakobs_5_Skullmasher:
    """GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Jakobs_5_Skullmasher"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Hive_Rl_Maliwan_3_Thehive:
    """GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_3_TheHive."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_3_TheHive"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Invader_Sniper_Hyperion_5_Invader:
    """GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Hyperion_5_Invader"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Slagga_Smg_Bandit_5_Slagga:
    """GD_Weap_SMG.A_Weapons_Legendary.SMG_Bandit_5_Slagga."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Legendary.SMG_Bandit_5_Slagga"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_D | None = None


@dataclass
class Teeth_Of_Terramorphous_Sg_Bandit_3_Teeth:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Teeth."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_Teeth"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_A | None = None


@dataclass
class Pitchfork_Sniper_Dahl_5_Pitchfork:
    """GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Dahl_5_Pitchfork"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Deliverance_Sg_Tediore_5_Deliverance:
    """GD_Weap_Shotgun.A_Weapons_Legendary.SG_Tediore_5_Deliverance."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Tediore_5_Deliverance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Norfleet_Rl_Maliwan_Alien_Norfleet:
    """GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_Alien_Norfleet."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons_Unique.RL_Maliwan_Alien_Norfleet"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Kerblaster_Ar_Torgue_5_Kerblaster:
    """GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Torgue_5_KerBlaster."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Torgue_5_KerBlaster"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Volcano_Sniper_Maliwan_5_Volcano:
    """GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Volcano."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Legendary.Sniper_Maliwan_5_Volcano"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Flakker_Sg_Torgue_5_Flakker:
    """GD_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Torgue_5_Flakker"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_B | None = None


@dataclass
class Conference_Call_Sg_Hyperion_5_Conferencecall:
    """GD_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Legendary.SG_Hyperion_5_ConferenceCall"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Logan_S_Gun_Pistol_Hyperion_5_Logansgun:
    """GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Legendary.Pistol_Hyperion_5_LogansGun"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_C | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Mashine_Gun_Ar_Bandit:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Bandit."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Bandit"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_A | None = None
    stock: Ar_Stock | None = None


@dataclass
class Rifle_Ar_Dahl:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Dahl."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Dahl"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_A | None = None
    stock: Ar_Stock | None = None


@dataclass
class Scarab_Ar_Jakobs:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Jakobs."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Jakobs"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_A | None = None
    stock: Ar_Stock | None = None


@dataclass
class Root_Ar_Torgue:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Torgue."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Torgue"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_A | None = None
    stock: Ar_Stock | None = None


@dataclass
class Renegade_Ar_Vladof:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Vladof."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Vladof"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_A | None = None
    stock: Ar_Stock | None = None


@dataclass
class Spinigun_Ar_Bandit_2_Uncommon:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_B | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_C | None = None


@dataclass
class Grenadier_Ar_Dahl_2_Uncommon:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_C | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Gatling_Gun_Ar_Jakobs_2_Uncommon:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Jakobs_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Jakobs_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_D | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Root_Ar_Torgue_2_Uncommon:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Torgue_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Torgue_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_E | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_C | None = None


@dataclass
class Guerrilla_Ar_Vladof_2_Uncommon:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_F | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Carbene_Ar_Bandit_3_Rare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_B | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_C | None = None


@dataclass
class Defender_Ar_Dahl_3_Rare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_3_Rare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_C | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Rifle_Ar_Jakobs_3_Rare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Jakobs_3_Rare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Jakobs_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_D | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Root_Ar_Torgue_3_Rare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Torgue_3_Rare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Torgue_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_E | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_C | None = None


@dataclass
class Guerrilla_Ar_Vladof_3_Rare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_3_Rare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_F | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Mashine_Gun_Ar_Bandit_4_Veryrare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_B | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Minigun_Ar_Dahl_4_Veryrare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_C | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Gatling_Gun_Ar_Jakobs_4_Veryrare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Jakobs_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Jakobs_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_D | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Lance_Ar_Torgue_4_Veryrare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Torgue_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Torgue_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_E | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Guerrilla_Ar_Vladof_4_Veryrare:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_F | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Blasster_Ar_Bandit_5_Alien:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_5_Alien."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_B | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Blaster_Ar_Dahl_5_Alien:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_5_Alien."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Dahl_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_B | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Blaster_Ar_Vladof_5_Alien:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_5_Alien."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Vladof_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_B | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Shredifier_Ar_Vladof_5_Sherdifier:
    """GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Vladof_5_Sherdifier."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Legendary.AR_Vladof_5_Sherdifier"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Zooka_Rl_Bandit:
    """GD_Weap_Launchers.A_Weapons.RL_Bandit."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Bandit"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None


@dataclass
class Bazooka_Rl_Tediore:
    """GD_Weap_Launchers.A_Weapons.RL_Tediore."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Tediore"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None


@dataclass
class Rpg_Rl_Vladof:
    """GD_Weap_Launchers.A_Weapons.RL_Vladof."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Vladof"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None


@dataclass
class Prowler_Rl_Maliwan:
    """GD_Weap_Launchers.A_Weapons.RL_Maliwan."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Maliwan"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None


@dataclass
class Boom_Rl_Torgue:
    """GD_Weap_Launchers.A_Weapons.RL_Torgue."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Torgue"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None


@dataclass
class Bombabarbardeer_Rl_Bandit_2_Uncommon:
    """GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Bandit_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Launcher_Rl_Tediore_2_Uncommon:
    """GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Tediore_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Rpg_Rl_Vladof_2_Uncommon:
    """GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Vladof_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Panorama_Rl_Maliwan_2_Uncommon:
    """GD_Weap_Launchers.A_Weapons.RL_Maliwan_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Maliwan_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Boom_Rl_Torgue_2_Uncommon:
    """GD_Weap_Launchers.A_Weapons.RL_Torgue_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Torgue_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Zooka_Rl_Bandit_3_Rare:
    """GD_Weap_Launchers.A_Weapons.RL_Bandit_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Bandit_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Launcher_Rl_Tediore_3_Rare:
    """GD_Weap_Launchers.A_Weapons.RL_Tediore_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Tediore_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Glory_Rl_Vladof_3_Rare:
    """GD_Weap_Launchers.A_Weapons.RL_Vladof_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Vladof_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Prowler_Rl_Maliwan_3_Rare:
    """GD_Weap_Launchers.A_Weapons.RL_Maliwan_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Maliwan_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Blaaa_Rl_Torgue_3_Rare:
    """GD_Weap_Launchers.A_Weapons.RL_Torgue_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Torgue_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Zooka_Rl_Bandit_4_Veryrare:
    """GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Bandit_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Dispatch_Rl_Tediore_4_Veryrare:
    """GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Tediore_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Rpg_Rl_Vladof_4_Veryrare:
    """GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Vladof_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Prowler_Rl_Maliwan_4_Veryrare:
    """GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Maliwan_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Deee_Rl_Torgue_4_Veryrare:
    """GD_Weap_Launchers.A_Weapons.RL_Torgue_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Torgue_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    barrel: L_Barrel | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Prazma_Canon_Rl_Bandit_5_Alien:
    """GD_Weap_Launchers.A_Weapons.RL_Bandit_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Bandit_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Launcher_Rl_Tediore_5_Alien:
    """GD_Weap_Launchers.A_Weapons.RL_Tediore_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Tediore_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Topneaa_Rl_Vladof_5_Alien:
    """GD_Weap_Launchers.A_Weapons.RL_Vladof_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Vladof_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Pbfg_Rl_Maliwan_5_Alien:
    """GD_Weap_Launchers.A_Weapons.RL_Maliwan_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons.RL_Maliwan_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Blockhead_Sg_Tediore_3_Blockhead:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Blockhead."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Blockhead"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Longbow_Sniper_Hyperion_3_Longbow:
    """GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Longbow."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Longbow"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_B | None = None


@dataclass
class Pistal_Pistol_Bandit:
    """GD_Weap_Pistol.A_Weapons.Pistol_Bandit."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Bandit"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_A | None = None


@dataclass
class Handgun_Pistol_Tediore:
    """GD_Weap_Pistol.A_Weapons.Pistol_Tediore."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Tediore"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_A | None = None


@dataclass
class Hand_Cannon_Pistol_Torgue:
    """GD_Weap_Pistol.A_Weapons.Pistol_Torgue."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Torgue"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_A | None = None


@dataclass
class Animosity_Pistol_Maliwan:
    """GD_Weap_Pistol.A_Weapons.Pistol_Maliwan."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Maliwan"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_A | None = None
    element: Pistol_Elemental_C | None = None


@dataclass
class Impact_Pistol_Hyperion:
    """GD_Weap_Pistol.A_Weapons.Pistol_Hyperion."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Hyperion"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_A | None = None


@dataclass
class Ass_Beeter_Pistol_Bandit_2_Uncommon:
    """GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Bandit_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_C | None = None


@dataclass
class Handgun_Pistol_Tediore_2_Uncommon:
    """GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Tediore_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Negotiator_Pistol_Dahl_2_Uncommon:
    """GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Dahl_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Assassin_Pistol_Vladof_2_Uncommon:
    """GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Vladof_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Hand_Cannon_Pistol_Torgue_2_Uncommon:
    """GD_Weap_Pistol.A_Weapons.Pistol_Torgue_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Torgue_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_C | None = None


@dataclass
class Animosity_Pistol_Maliwan_2_Uncommon:
    """GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Revolver_Pistol_Jakobs_2_Uncommon:
    """GD_Weap_Pistol.A_Weapons.Pistol_Jakobs_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Jakobs_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    barrel: Pistol_Barrel_C | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Impact_Pistol_Hyperion_2_Uncommon:
    """GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_D | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Pistal_Pistol_Bandit_3_Rare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Bandit_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Bandit_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_C | None = None


@dataclass
class Handgun_Pistol_Tediore_3_Rare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Tediore_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Tediore_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Repeater_Pistol_Dahl_3_Rare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Dahl_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Dahl_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Tmp_Pistol_Vladof_3_Rare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Vladof_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Vladof_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Rod_Pistol_Torgue_3_Rare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Torgue_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Torgue_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_C | None = None


@dataclass
class Animosity_Pistol_Maliwan_3_Rare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Wheelgun_Pistol_Jakobs_3_Rare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Jakobs_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Jakobs_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    barrel: Pistol_Barrel_C | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Apparatus_Pistol_Hyperion_3_Rare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_D | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Ass_Beeter_Pistol_Bandit_4_Veryrare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Bandit_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Bandit_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_D | None = None


@dataclass
class Quickshot_Pistol_Tediore_4_Veryrare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Tediore_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Tediore_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Repeater_Pistol_Dahl_4_Veryrare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Dahl_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Dahl_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Tmp_Pistol_Vladof_4_Veryrare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Vladof_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Vladof_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Injector_Pistol_Torgue_4_Veryrare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Torgue_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Torgue_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_D | None = None


@dataclass
class Aegis_Pistol_Maliwan_4_Veryrare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Revolver_Pistol_Jakobs_4_Veryrare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Jakobs_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Jakobs_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    barrel: Pistol_Barrel_C | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Apparatus_Pistol_Hyperion_4_Veryrare:
    """GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_D | None = None
    sight: Pistol_Sight_C | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Dart_Pistol_Bandit_5_Alien:
    """GD_Weap_Pistol.A_Weapons.Pistol_Bandit_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Bandit_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_Alien | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_D | None = None


@dataclass
class Dart_Pistol_Dahl_5_Alien:
    """GD_Weap_Pistol.A_Weapons.Pistol_Dahl_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Dahl_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_Alien | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Dart_Pistol_Tediore_5_Alien:
    """GD_Weap_Pistol.A_Weapons.Pistol_Tediore_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Tediore_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_Alien | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Spiker_Pistol_Vladof_5_Alien:
    """GD_Weap_Pistol.A_Weapons.Pistol_Vladof_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Vladof_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    barrel: Pistol_Barrel_Alien | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Spiker_Pistol_Maliwan_5_Alien:
    """GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Maliwan_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_Alien | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Dart_Pistol_Hyperion_5_Alien:
    """GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons.Pistol_Hyperion_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_Alien | None = None
    sight: Pistol_Sight_C | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Longer_Ragne_Kilier_Sg_Bandit:
    """GD_Weap_Shotgun.A_Weapons.SG_Bandit."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Bandit"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_A | None = None
    stock: Sg_Stock | None = None


@dataclass
class Double_Barrels_Sg_Tediore:
    """GD_Weap_Shotgun.A_Weapons.SG_Tediore."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Tediore"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_A | None = None
    stock: Sg_Stock | None = None


@dataclass
class Pounder_Sg_Torgue:
    """GD_Weap_Shotgun.A_Weapons.SG_Torgue."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Torgue"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_A | None = None
    stock: Sg_Stock | None = None


@dataclass
class Face_Time_Sg_Hyperion:
    """GD_Weap_Shotgun.A_Weapons.SG_Hyperion."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Hyperion"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_A | None = None
    stock: Sg_Stock | None = None


@dataclass
class Stret_Sweper_Sg_Bandit_2_Uncommon:
    """GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Bandit_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_B | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_A | None = None


@dataclass
class Home_Security_Sg_Tediore_2_Uncommon:
    """GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Tediore_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_B | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Hulk_Sg_Torgue_2_Uncommon:
    """GD_Weap_Shotgun.A_Weapons.SG_Torgue_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Torgue_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_B | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_A | None = None


@dataclass
class Scattergun_Sg_Jakobs_2_Uncommon:
    """GD_Weap_Shotgun.A_Weapons.SG_Jakobs_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Jakobs_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_B | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Projectile_Diversification_Sg_Hyperion_2_Uncommon:
    """GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Hyperion_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_B | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Stret_Sweper_Sg_Bandit_3_Rare:
    """GD_Weap_Shotgun.A_Weapons.SG_Bandit_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Bandit_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_A | None = None


@dataclass
class Triple_Barrels_Sg_Tediore_3_Rare:
    """GD_Weap_Shotgun.A_Weapons.SG_Tediore_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Tediore_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Pounder_Sg_Torgue_3_Rare:
    """GD_Weap_Shotgun.A_Weapons.SG_Torgue_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Torgue_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_A | None = None


@dataclass
class Bushwack_Sg_Jakobs_3_Rare:
    """GD_Weap_Shotgun.A_Weapons.SG_Jakobs_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Jakobs_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Crowdsourcing_Sg_Hyperion_3_Rare:
    """GD_Weap_Shotgun.A_Weapons.SG_Hyperion_3_Rare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Hyperion_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Longer_Ragne_Kilier_Sg_Bandit_4_Veryrare:
    """GD_Weap_Shotgun.A_Weapons.SG_Bandit_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Bandit_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_B | None = None


@dataclass
class Sportsman_Sg_Tediore_4_Veryrare:
    """GD_Weap_Shotgun.A_Weapons.SG_Tediore_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Tediore_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Hulk_Sg_Torgue_4_Veryrare:
    """GD_Weap_Shotgun.A_Weapons.SG_Torgue_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Torgue_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_B | None = None


@dataclass
class Longrider_Sg_Jakobs_4_Veryrare:
    """GD_Weap_Shotgun.A_Weapons.SG_Jakobs_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Jakobs_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Development_Sg_Hyperion_4_Veryrare:
    """GD_Weap_Shotgun.A_Weapons.SG_Hyperion_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Hyperion_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Splasher_Blashter_Sg_Bandit_5_Alien:
    """GD_Weap_Shotgun.A_Weapons.SG_Bandit_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Bandit_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_B | None = None
    accessory1: Sg_Accessory_E | None = None


@dataclass
class Splatgun_Sg_Tediore_5_Alien:
    """GD_Weap_Shotgun.A_Weapons.SG_Tediore_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Tediore_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_B | None = None
    accessory1: Sg_Accessory_F | None = None


@dataclass
class Splatgun_Sg_Hyperion_5_Alien:
    """GD_Weap_Shotgun.A_Weapons.SG_Hyperion_5_Alien."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons.SG_Hyperion_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_B | None = None
    accessory1: Sg_Accessory_F | None = None


@dataclass
class Smig_Smg_Bandit:
    """GD_Weap_SMG.A_Weapons.SMG_Bandit."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Bandit"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_A | None = None
    stock: Smg_Stock | None = None


@dataclass
class Subcompact_Mg_Smg_Tediore:
    """GD_Weap_SMG.A_Weapons.SMG_Tediore."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Tediore"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_A | None = None
    stock: Smg_Stock | None = None


@dataclass
class Smg_Smg_Dahl:
    """GD_Weap_SMG.A_Weapons.SMG_Dahl."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Dahl"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_A | None = None
    stock: Smg_Stock | None = None


@dataclass
class Vexation_Smg_Maliwan:
    """GD_Weap_SMG.A_Weapons.SMG_Maliwan."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Maliwan"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None


@dataclass
class Projectile_Convergence_Smg_Hyperion:
    """GD_Weap_SMG.A_Weapons.SMG_Hyperion."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Hyperion"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_A | None = None
    stock: Smg_Stock | None = None


@dataclass
class Smig_Smg_Bandit_2_Uncommon:
    """GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Bandit_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_B | None = None


@dataclass
class Special_Smg_Tediore_2_Uncommon:
    """GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Tediore_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Fox_Smg_Dahl_2_Uncommon:
    """GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Dahl_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Submalevolent_Grace_Smg_Maliwan_2_Uncommon:
    """GD_Weap_SMG.A_Weapons.SMG_Maliwan_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Maliwan_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Backburner_Smg_Hyperion_2_Uncommon:
    """GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Hyperion_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Smig_Smg_Bandit_3_Rare:
    """GD_Weap_SMG.A_Weapons.SMG_Bandit_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Bandit_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_B | None = None


@dataclass
class Subcompact_Mg_Smg_Tediore_3_Rare:
    """GD_Weap_SMG.A_Weapons.SMG_Tediore_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Tediore_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Fox_Smg_Dahl_3_Rare:
    """GD_Weap_SMG.A_Weapons.SMG_Dahl_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Dahl_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Provacateur_Smg_Maliwan_3_Rare:
    """GD_Weap_SMG.A_Weapons.SMG_Maliwan_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Maliwan_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    body: Smg_Body_Maliwan_Var | None = None
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Transmurdera_Smg_Hyperion_3_Rare:
    """GD_Weap_SMG.A_Weapons.SMG_Hyperion_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Hyperion_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Acurate_Smgg_Smg_Bandit_4_Veryrare:
    """GD_Weap_SMG.A_Weapons.SMG_Bandit_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Bandit_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_D | None = None


@dataclass
class Subcompact_Mg_Smg_Tediore_4_Veryrare:
    """GD_Weap_SMG.A_Weapons.SMG_Tediore_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Tediore_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Fox_Smg_Dahl_4_Veryrare:
    """GD_Weap_SMG.A_Weapons.SMG_Dahl_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Dahl_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Submalevolent_Grace_Smg_Maliwan_4_Veryrare:
    """GD_Weap_SMG.A_Weapons.SMG_Maliwan_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Maliwan_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Projectile_Convergence_Smg_Hyperion_4_Veryrare:
    """GD_Weap_SMG.A_Weapons.SMG_Hyperion_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Hyperion_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Plasma_Caster_Smg_Bandit_5_Alien:
    """GD_Weap_SMG.A_Weapons.SMG_Bandit_5_Alien."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Bandit_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_E | None = None


@dataclass
class Plasma_Caster_Smg_Tediore_5_Alien:
    """GD_Weap_SMG.A_Weapons.SMG_Tediore_5_Alien."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Tediore_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_E | None = None


@dataclass
class Plasma_Caster_Smg_Dahl_5_Alien:
    """GD_Weap_SMG.A_Weapons.SMG_Dahl_5_Alien."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Dahl_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_E | None = None


@dataclass
class Plasma_Caster_Smg_Maliwan_5_Alien:
    """GD_Weap_SMG.A_Weapons.SMG_Maliwan_5_Alien."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Maliwan_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_E | None = None


@dataclass
class Plasma_Caster_Smg_Hyperion_5_Alien:
    """GD_Weap_SMG.A_Weapons.SMG_Hyperion_5_Alien."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons.SMG_Hyperion_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_E | None = None


@dataclass
class Sniper_Sniper_Dahl:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None


@dataclass
class Droog_Sniper_Vladof:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None


@dataclass
class Snider_Sniper_Maliwan:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None


@dataclass
class Chinook_Sniper_Jakobs:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Jakobs."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Jakobs"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None


@dataclass
class Competition_Sniper_Hyperion:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None


@dataclass
class Terror_Sniper_Dahl_2_Uncommon:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Bratchny_Sniper_Vladof_2_Uncommon:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Snider_Sniper_Maliwan_2_Uncommon:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Chinook_Sniper_Jakobs_2_Uncommon:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Jakobs_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Jakobs_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Transaction_Sniper_Hyperion_2_Uncommon:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_2_Uncommon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Scout_Sniper_Dahl_3_Rare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Horrorshow_Sniper_Vladof_3_Rare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Rakehell_Sniper_Maliwan_3_Rare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Diaub_Sniper_Jakobs_3_Rare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Jakobs_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Jakobs_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Sniper_Rifle_Sniper_Hyperion_3_Rare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_3_Rare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_3_Rare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Sniper_Sniper_Dahl_4_Veryrare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Bratchny_Sniper_Vladof_4_Veryrare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Corinthian_Sniper_Maliwan_4_Veryrare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Muckamuck_Sniper_Jakobs_4_Veryrare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Jakobs_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Jakobs_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Policy_Sniper_Hyperion_4_Veryrare:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_4_VeryRare."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_4_VeryRare"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Railer_Sniper_Dahl_5_Alien:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_5_Alien."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Dahl_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Moloko_Sniper_Vladof_5_Alien:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_5_Alien."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Vladof_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Railer_Sniper_Maliwan_5_Alien:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_5_Alien."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Maliwan_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Hybridfication_Sniper_Hyperion_5_Alien:
    """GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_5_Alien."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons.Sniper_Hyperion_5_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Renegade_Ar_Dahl_1_Gbx:
    """GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Dahl_1_GBX."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Dahl_1_GBX"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_A | None = None
    stock: Ar_Stock | None = None


@dataclass
class Projectile_Convergence_Smg_Gearbox_1:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Gearbox_1."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Gearbox_1"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_A | None = None
    stock: Smg_Stock | None = None


@dataclass
class Chinook_Sniper_Gearbox_1:
    """GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Gearbox_1."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Gearbox_1"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None


@dataclass
class Hail_Ar_Vladof_3_Hail:
    """GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Vladof_3_Hail."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Vladof_3_Hail"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_C | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_B | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Scorpio_Ar_Dahl_3_Scorpio:
    """GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Dahl_3_Scorpio."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Dahl_3_Scorpio"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Mashine_Gun_Ar_Bandit_2_Fire:
    """GD_Weap_AssaultRifle.A_Weapons_Elemental.AR_Bandit_2_Fire."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Elemental.AR_Bandit_2_Fire"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_B | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_C | None = None


@dataclass
class Teapot_Pistol_Dahl_3_Teapot:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Teapot."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Teapot"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Fibber_Pistol_Hyperion_3_Fibber:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_Fibber"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_Bandit_Fibber | None = None
    sight: Pistol_Sight_D | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Creamer_Rl_Torgue_3_Creamer:
    """GD_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons_Unique.RL_Torgue_3_Creamer"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_C | None = None


@dataclass
class Buffalo_Sniper_Jakobs_3_Buffalo:
    """GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Buffalo."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Buffalo"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_B | None = None


@dataclass
class Chulainn_Smg_Maliwan_3_Chulainn:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Chulainn."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Maliwan_3_Chulainn"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Landscaper_Sg_Torgue_3_Landscaper:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Landscaper."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Torgue_3_Landscaper"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_A | None = None


@dataclass
class Trespasser_Sniper_Jakobs_3_Tresspasser:
    """GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Tresspasser."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Jakobs_3_Tresspasser"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Triquetra_Sg_Jakobs_3_Triquetra:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Triquetra."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_Triquetra"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Roaster_Rl_Bandit_3_Roaster:
    """GD_Weap_Launchers.A_Weapons_Unique.RL_Bandit_3_Roaster."""

    path: ClassVar[str] = "GD_Weap_Launchers.A_Weapons_Unique.RL_Bandit_3_Roaster"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_A | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Sloth_Sniper_Dahl_3_Sloth:
    """GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_Sloth."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Dahl_3_Sloth"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Rubi_Pistol_Maliwan_3_Rubi:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Maliwan_3_Rubi"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Heart_Breaker_Sg_Hyperion_3_Heartbreaker:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_HeartBreaker."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_HeartBreaker"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Octo_Sg_Tediore_3_Octo:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Tediore_3_Octo"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Roksalt_Sg_Bandit_3_Roksalt:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_RokSalt."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Bandit_3_RokSalt"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_A | None = None


@dataclass
class Veritas_Pistol_Vladof_3_Veritas:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Vladof_3_Veritas."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Vladof_3_Veritas"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    sight: Pistol_Sight_A | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Bane_Smg_Hyperion_3_Bane:
    """GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Bane."""

    path: ClassVar[str] = "GD_Weap_SMG.A_Weapons_Unique.SMG_Hyperion_3_Bane"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Evil_Smasher_Ar_Torgue_3_Evilsmasher:
    """GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Torgue_3_EvilSmasher."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Torgue_3_EvilSmasher"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_C | None = None


@dataclass
class Stomper_Ar_Jakobs_3_Stomper:
    """GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Jakobs_3_Stomper."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons_Unique.AR_Jakobs_3_Stomper"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Morningstar_Sniper_Hyperion_3_Morningstar:
    """GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Morningstar."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Hyperion_3_Morningstar"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Dahlminator_Pistol_Dahl_3_Dahlminator:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Dahlminator."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Dahl_3_Dahlminator"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Shotgun_1340_Sg_Hyperion_3_Shotgun1340:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_Shotgun1340."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Hyperion_3_Shotgun1340"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_C | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Ch_Re_Amie_Sniper_Maliwan_3_Chereamie:
    """GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie."""

    path: ClassVar[str] = "GD_Weap_SniperRifles.A_Weapons_Unique.Sniper_Maliwan_3_ChereAmie"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Lady_Fist_Pistol_Hyperion_3_Ladyfist:
    """GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Unique.Pistol_Hyperion_3_LadyFist"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_D | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Tidal_Wave_Sg_Jakobs_3_Tidalwave:
    """GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_TidalWave."""

    path: ClassVar[str] = "GD_Weap_Shotgun.A_Weapons_Unique.SG_Jakobs_3_TidalWave"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Aegis_Pistol_Maliwan_2_Corrosive:
    """GD_Weap_Pistol.A_Weapons_Elemental.Pistol_Maliwan_2_Corrosive."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Elemental.Pistol_Maliwan_2_Corrosive"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Aegis_Pistol_Maliwan_2_Fire:
    """GD_Weap_Pistol.A_Weapons_Elemental.Pistol_Maliwan_2_Fire."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Elemental.Pistol_Maliwan_2_Fire"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Aegis_Pistol_Maliwan_2_Shock:
    """GD_Weap_Pistol.A_Weapons_Elemental.Pistol_Maliwan_2_Shock."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Elemental.Pistol_Maliwan_2_Shock"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Phobia_Pistol_Maliwan_2_Slag:
    """GD_Weap_Pistol.A_Weapons_Elemental.Pistol_Maliwan_2_Slag."""

    path: ClassVar[str] = "GD_Weap_Pistol.A_Weapons_Elemental.Pistol_Maliwan_2_Slag"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Blasster_Ar_Bandit_3_Rare_Alien:
    """GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare_Alien."""

    path: ClassVar[str] = "GD_Weap_AssaultRifle.A_Weapons.AR_Bandit_3_Rare_Alien"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_C | None = None


@dataclass
class Aegis_Weapon_Jabberslagweapon:
    """GD_Allium_TG_Plot_M01Data.Weapons.Weapon_JabberSlagWeapon."""

    path: ClassVar[str] = "GD_Allium_TG_Plot_M01Data.Weapons.Weapon_JabberSlagWeapon"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Hector_S_Paradise_Pistol_Dahl_5_Hector_Hornet:
    """GD_Anemone_Weapons.A_Weapons_Legendary.Pistol_Dahl_5_Hector_Hornet."""

    path: ClassVar[str] = "GD_Anemone_Weapons.A_Weapons_Legendary.Pistol_Dahl_5_Hector_Hornet"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None


@dataclass
class M2828_Thumpson_Ar_Jakobs_5_Brothers:
    """GD_Anemone_Weapons.AssaultRifle.Brothers.AR_Jakobs_5_Brothers."""

    path: ClassVar[str] = "GD_Anemone_Weapons.AssaultRifle.Brothers.AR_Jakobs_5_Brothers"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Fire_Drill_Pistol_Vladof_5_Infinity_Dd:
    """GD_Anemone_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Infinity_DD."""

    path: ClassVar[str] = "GD_Anemone_Weapons.A_Weapons_Legendary.Pistol_Vladof_5_Infinity_DD"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_E | None = None


@dataclass
class Unicornsplosion_Sg_Torgue_3_Swordsplosion_Unico:
    """GD_Anemone_Weapons.Shotguns.SG_Torgue_3_SwordSplosion_Unico."""

    path: ClassVar[str] = "GD_Anemone_Weapons.Shotguns.SG_Torgue_3_SwordSplosion_Unico"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_B | None = None


@dataclass
class Norfleet_Rl_Maliwan_Alien_Norfleet_Fire_100:
    """GD_Anemone_Weapons.A_Weapons_Unique.RL_Maliwan_Alien_Norfleet_Fire_100."""

    path: ClassVar[str] = "GD_Anemone_Weapons.A_Weapons_Unique.RL_Maliwan_Alien_Norfleet_Fire_100"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    element: Rl_Elemental_B | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Droog_Sniper_Vladof_4_Veryrare_Hoffman:
    """GD_Anemone_Lt_Hoffman.A_Weapons.Sniper_Vladof_4_VeryRare_Hoffman."""

    path: ClassVar[str] = "GD_Anemone_Lt_Hoffman.A_Weapons.Sniper_Vladof_4_VeryRare_Hoffman"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Hot_Mama_Sniper_Jakobs_6_Chaude_Mama:
    """GD_Anemone_Weapons.sniper.Sniper_Jakobs_6_Chaude_Mama."""

    path: ClassVar[str] = "GD_Anemone_Weapons.sniper.Sniper_Jakobs_6_Chaude_Mama"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    stock: Sr_Stock_B | None = None


@dataclass
class Infection_Cleaner_Smg_Tediore_6_Infection_Cleaner:
    """GD_Anemone_Weapons.SMG.SMG_Tediore_6_Infection_Cleaner."""

    path: ClassVar[str] = "GD_Anemone_Weapons.SMG.SMG_Tediore_6_Infection_Cleaner"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Amigo_Sincero_Sniper_Jakobs_3_Morde_Lt:
    """GD_Anemone_Weapons.A_Weapons_Unique.Sniper_Jakobs_3_Morde_Lt."""

    path: ClassVar[str] = "GD_Anemone_Weapons.A_Weapons_Unique.Sniper_Jakobs_3_Morde_Lt"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    stock: Sr_Stock_A | None = None


@dataclass
class Overcompensator_Sg_Hyperion_6_Overcompensator:
    """GD_Anemone_Weapons.Shotgun.Overcompensator.SG_Hyperion_6_Overcompensator."""

    path: ClassVar[str] = "GD_Anemone_Weapons.Shotgun.Overcompensator.SG_Hyperion_6_Overcompensator"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None


@dataclass
class Peak_Opener_Ar_Torgue_5_Peakopener:
    """GD_Anemone_Weapons.AssaultRifle.PeakOpener.AR_Torgue_5_PeakOpener."""

    path: ClassVar[str] = "GD_Anemone_Weapons.AssaultRifle.PeakOpener.AR_Torgue_5_PeakOpener"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None


@dataclass
class Fire_Infinity_100_Fire:
    """GD_Anemone_Weapons.Testing_Resist_100.100_Fire."""

    path: ClassVar[str] = "GD_Anemone_Weapons.Testing_Resist_100.100_Fire"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_E | None = None


@dataclass
class Toothpick_Ar_Dahl_6_Toothpick:
    """GD_Anemone_Weapons.AssaultRifle.AR_Dahl_6_Toothpick."""

    path: ClassVar[str] = "GD_Anemone_Weapons.AssaultRifle.AR_Dahl_6_Toothpick"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class World_Burn_Rl_Torgue_5_Worldburn:
    """GD_Anemone_Weapons.Rocket_Launcher.WorldBurn.RL_Torgue_5_WorldBurn."""

    path: ClassVar[str] = "GD_Anemone_Weapons.Rocket_Launcher.WorldBurn.RL_Torgue_5_WorldBurn"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Bangstick_Sg_Torgue_7_Effervecemt:
    """GD_Anemone_Weapons.A_Weapons.SG_Torgue_7_Effervecemt."""

    path: ClassVar[str] = "GD_Anemone_Weapons.A_Weapons.SG_Torgue_7_Effervecemt"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_B | None = None


@dataclass
class Rifle_Ar_Peakopener:
    """GD_Anemone_Weapons.AssaultRifle.PeakOpener.AR_PeakOpener."""

    path: ClassVar[str] = "GD_Anemone_Weapons.AssaultRifle.PeakOpener.AR_PeakOpener"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None


@dataclass
class Ogre_Ar_Bandit_3_Ogre:
    """GD_Aster_Weapons.AssaultRifles.AR_Bandit_3_Ogre."""

    path: ClassVar[str] = "GD_Aster_Weapons.AssaultRifles.AR_Bandit_3_Ogre"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Grog_Nozzle_Pistol_Maliwan_3_Grognozzle:
    """GD_Aster_Weapons.Pistols.Pistol_Maliwan_3_GrogNozzle."""

    path: ClassVar[str] = "GD_Aster_Weapons.Pistols.Pistol_Maliwan_3_GrogNozzle"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Crit_Smg_Maliwan_3_Crit:
    """GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit."""

    path: ClassVar[str] = "GD_Aster_Weapons.SMGs.SMG_Maliwan_3_Crit"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    body: Smg_Body_Maliwan_Var | None = None
    grip: Smg_Grip | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Omen_Aster_Seraph_Omen_Balance:
    """GD_Aster_RaidWeapons.Shotguns.Aster_Seraph_Omen_Balance."""

    path: ClassVar[str] = "GD_Aster_RaidWeapons.Shotguns.Aster_Seraph_Omen_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_F | None = None


@dataclass
class Stinger_Aster_Seraph_Stinger_Balance:
    """GD_Aster_RaidWeapons.Pistols.Aster_Seraph_Stinger_Balance."""

    path: ClassVar[str] = "GD_Aster_RaidWeapons.Pistols.Aster_Seraph_Stinger_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Seeker_Aster_Seraph_Seeker_Balance:
    """GD_Aster_RaidWeapons.AssaultRifles.Aster_Seraph_Seeker_Balance."""

    path: ClassVar[str] = "GD_Aster_RaidWeapons.AssaultRifles.Aster_Seraph_Seeker_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Florentine_Aster_Seraph_Florentine_Balance:
    """GD_Aster_RaidWeapons.SMGs.Aster_Seraph_Florentine_Balance."""

    path: ClassVar[str] = "GD_Aster_RaidWeapons.SMGs.Aster_Seraph_Florentine_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_E | None = None


@dataclass
class Slapper_Pistol_Torgue_4_Rock:
    """GD_Aster_Weapons.Pistols.Pistol_Torgue_4_Rock."""

    path: ClassVar[str] = "GD_Aster_Weapons.Pistols.Pistol_Torgue_4_Rock"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_D | None = None


@dataclass
class Pounder_Sg_Torgue_4_Rock:
    """GD_Aster_Weapons.Shotguns.SG_Torgue_4_Rock."""

    path: ClassVar[str] = "GD_Aster_Weapons.Shotguns.SG_Torgue_4_Rock"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_B | None = None


@dataclass
class Root_Ar_Torgue_4_Rock:
    """GD_Aster_Weapons.AssaultRifles.AR_Torgue_4_Rock."""

    path: ClassVar[str] = "GD_Aster_Weapons.AssaultRifles.AR_Torgue_4_Rock"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_E | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Mashine_Gun_Ar_Bandit_4_Quartz:
    """GD_Aster_Weapons.AssaultRifles.AR_Bandit_4_Quartz."""

    path: ClassVar[str] = "GD_Aster_Weapons.AssaultRifles.AR_Bandit_4_Quartz"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_B | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Defender_Ar_Dahl_4_Emerald:
    """GD_Aster_Weapons.AssaultRifles.AR_Dahl_4_Emerald."""

    path: ClassVar[str] = "GD_Aster_Weapons.AssaultRifles.AR_Dahl_4_Emerald"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_C | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Rifle_Ar_Vladof_4_Garnet:
    """GD_Aster_Weapons.AssaultRifles.AR_Vladof_4_Garnet."""

    path: ClassVar[str] = "GD_Aster_Weapons.AssaultRifles.AR_Vladof_4_Garnet"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_F | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Rifle_Ar_Jakobs_4_Citrine:
    """GD_Aster_Weapons.AssaultRifles.AR_Jakobs_4_Citrine."""

    path: ClassVar[str] = "GD_Aster_Weapons.AssaultRifles.AR_Jakobs_4_Citrine"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    barrel: Ar_Barrel_D | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Ratatater_Pistol_Bandit_4_Quartz:
    """GD_Aster_Weapons.Pistols.Pistol_Bandit_4_Quartz."""

    path: ClassVar[str] = "GD_Aster_Weapons.Pistols.Pistol_Bandit_4_Quartz"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_D | None = None


@dataclass
class Aimshot_Pistol_Tediore_4_Cubiczerconia:
    """GD_Aster_Weapons.Pistols.Pistol_Tediore_4_CubicZerconia."""

    path: ClassVar[str] = "GD_Aster_Weapons.Pistols.Pistol_Tediore_4_CubicZerconia"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Magnum_Pistol_Dahl_4_Emerald:
    """GD_Aster_Weapons.Pistols.Pistol_Dahl_4_Emerald."""

    path: ClassVar[str] = "GD_Aster_Weapons.Pistols.Pistol_Dahl_4_Emerald"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Tmp_Pistol_Vladof_4_Garnet:
    """GD_Aster_Weapons.Pistols.Pistol_Vladof_4_Garnet."""

    path: ClassVar[str] = "GD_Aster_Weapons.Pistols.Pistol_Vladof_4_Garnet"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Aegis_Pistol_Maliwan_4_Aquamarine:
    """GD_Aster_Weapons.Pistols.Pistol_Maliwan_4_Aquamarine."""

    path: ClassVar[str] = "GD_Aster_Weapons.Pistols.Pistol_Maliwan_4_Aquamarine"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Revolver_Pistol_Jakobs_4_Citrine:
    """GD_Aster_Weapons.Pistols.Pistol_Jakobs_4_Citrine."""

    path: ClassVar[str] = "GD_Aster_Weapons.Pistols.Pistol_Jakobs_4_Citrine"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    barrel: Pistol_Barrel_C | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Apparatus_Pistol_Hyperion_4_Diamond:
    """GD_Aster_Weapons.Pistols.Pistol_Hyperion_4_Diamond."""

    path: ClassVar[str] = "GD_Aster_Weapons.Pistols.Pistol_Hyperion_4_Diamond"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    barrel: Pistol_Barrel_D | None = None
    sight: Pistol_Sight_C | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Longer_Ragne_Kilier_Sg_Bandit_4_Quartz:
    """GD_Aster_Weapons.Shotguns.SG_Bandit_4_Quartz."""

    path: ClassVar[str] = "GD_Aster_Weapons.Shotguns.SG_Bandit_4_Quartz"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_B | None = None


@dataclass
class Triple_Barrels_Sg_Tediore_4_Cubiczerconia:
    """GD_Aster_Weapons.Shotguns.SG_Tediore_4_CubicZerconia."""

    path: ClassVar[str] = "GD_Aster_Weapons.Shotguns.SG_Tediore_4_CubicZerconia"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Longrider_Sg_Jakobs_4_Citrine:
    """GD_Aster_Weapons.Shotguns.SG_Jakobs_4_Citrine."""

    path: ClassVar[str] = "GD_Aster_Weapons.Shotguns.SG_Jakobs_4_Citrine"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Face_Time_Sg_Hyperion_4_Diamond:
    """GD_Aster_Weapons.Shotguns.SG_Hyperion_4_Diamond."""

    path: ClassVar[str] = "GD_Aster_Weapons.Shotguns.SG_Hyperion_4_Diamond"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    barrel: Sg_Barrel_C | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Smig_Smg_Bandit_4_Quartz:
    """GD_Aster_Weapons.SMGs.SMG_Bandit_4_Quartz."""

    path: ClassVar[str] = "GD_Aster_Weapons.SMGs.SMG_Bandit_4_Quartz"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_D | None = None


@dataclass
class Subcompact_Mg_Smg_Tediore_4_Cubiczerconia:
    """GD_Aster_Weapons.SMGs.SMG_Tediore_4_CubicZerconia."""

    path: ClassVar[str] = "GD_Aster_Weapons.SMGs.SMG_Tediore_4_CubicZerconia"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Fox_Smg_Dahl_4_Emerald:
    """GD_Aster_Weapons.SMGs.SMG_Dahl_4_Emerald."""

    path: ClassVar[str] = "GD_Aster_Weapons.SMGs.SMG_Dahl_4_Emerald"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Revenant_Smg_Maliwan_4_Aquamarine:
    """GD_Aster_Weapons.SMGs.SMG_Maliwan_4_Aquamarine."""

    path: ClassVar[str] = "GD_Aster_Weapons.SMGs.SMG_Maliwan_4_Aquamarine"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_B | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Projectile_Convergence_Smg_Hyperion_4_Diamond:
    """GD_Aster_Weapons.SMGs.SMG_Hyperion_4_Diamond."""

    path: ClassVar[str] = "GD_Aster_Weapons.SMGs.SMG_Hyperion_4_Diamond"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    barrel: Smg_Barrel_B | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Sniper_Sr_Dahl_4_Emerald:
    """GD_Aster_Weapons.Snipers.SR_Dahl_4_Emerald."""

    path: ClassVar[str] = "GD_Aster_Weapons.Snipers.SR_Dahl_4_Emerald"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Pooshka_Sr_Vladof_4_Garnet:
    """GD_Aster_Weapons.Snipers.SR_Vladof_4_Garnet."""

    path: ClassVar[str] = "GD_Aster_Weapons.Snipers.SR_Vladof_4_Garnet"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Corinthian_Sr_Maliwan_4_Aquamarine:
    """GD_Aster_Weapons.Snipers.SR_Maliwan_4_Aquamarine."""

    path: ClassVar[str] = "GD_Aster_Weapons.Snipers.SR_Maliwan_4_Aquamarine"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Diaub_Sr_Jakobs_4_Citrine:
    """GD_Aster_Weapons.Snipers.SR_Jakobs_4_Citrine."""

    path: ClassVar[str] = "GD_Aster_Weapons.Snipers.SR_Jakobs_4_Citrine"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Transaction_Sr_Hyperion_4_Diamond:
    """GD_Aster_Weapons.Snipers.SR_Hyperion_4_Diamond."""

    path: ClassVar[str] = "GD_Aster_Weapons.Snipers.SR_Hyperion_4_Diamond"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    barrel: Sr_Barrel | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Swordsplosion_Sg_Torgue_3_Swordsplosion:
    """GD_Aster_Weapons.Shotguns.SG_Torgue_3_SwordSplosion."""

    path: ClassVar[str] = "GD_Aster_Weapons.Shotguns.SG_Torgue_3_SwordSplosion"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_B | None = None


@dataclass
class Orc_Smg_Bandit_3_Orc:
    """GD_Aster_Weapons.SMGs.SMG_Bandit_3_Orc."""

    path: ClassVar[str] = "GD_Aster_Weapons.SMGs.SMG_Bandit_3_Orc"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_B | None = None


@dataclass
class Unforgiven_Pistol_Jakobs_6_Unforgiven:
    """GD_Gladiolus_Weapons.Pistol.Pistol_Jakobs_6_Unforgiven."""

    path: ClassVar[str] = "GD_Gladiolus_Weapons.Pistol.Pistol_Jakobs_6_Unforgiven"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Stalker_Pistol_Vladof_6_Stalker:
    """GD_Gladiolus_Weapons.Pistol.Pistol_Vladof_6_Stalker."""

    path: ClassVar[str] = "GD_Gladiolus_Weapons.Pistol.Pistol_Vladof_6_Stalker"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_C | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_A | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Sawbar_Ar_Bandit_6_Sawbar:
    """GD_Gladiolus_Weapons.AssaultRifle.AR_Bandit_6_Sawbar."""

    path: ClassVar[str] = "GD_Gladiolus_Weapons.AssaultRifle.AR_Bandit_6_Sawbar"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_A | None = None


@dataclass
class Bearcat_Ar_Dahl_6_Bearcat:
    """GD_Gladiolus_Weapons.AssaultRifle.AR_Dahl_6_Bearcat."""

    path: ClassVar[str] = "GD_Gladiolus_Weapons.AssaultRifle.AR_Dahl_6_Bearcat"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Avenger_Smg_Tediore_6_Avenger:
    """GD_Gladiolus_Weapons.SMG.SMG_Tediore_6_Avenger."""

    path: ClassVar[str] = "GD_Gladiolus_Weapons.SMG.SMG_Tediore_6_Avenger"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Butcher_Sg_Hyperion_6_Butcher:
    """GD_Gladiolus_Weapons.Shotgun.SG_Hyperion_6_Butcher."""

    path: ClassVar[str] = "GD_Gladiolus_Weapons.Shotgun.SG_Hyperion_6_Butcher"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Storm_Sniper_Maliwan_6_Storm:
    """GD_Gladiolus_Weapons.sniper.Sniper_Maliwan_6_Storm."""

    path: ClassVar[str] = "GD_Gladiolus_Weapons.sniper.Sniper_Maliwan_6_Storm"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Tunguska_Rl_Torgue_6_Tunguska:
    """GD_Gladiolus_Weapons.Launchers.RL_Torgue_6_Tunguska."""

    path: ClassVar[str] = "GD_Gladiolus_Weapons.Launchers.RL_Torgue_6_Tunguska"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Slow_Hand_Sg_Hyperion_3_Slowhand:
    """GD_Iris_Weapons.Shotguns.SG_Hyperion_3_SlowHand."""

    path: ClassVar[str] = "GD_Iris_Weapons.Shotguns.SG_Hyperion_3_SlowHand"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_B | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Pocket_Rocket_Pistol_Torgue_3_Pocketrocket:
    """GD_Iris_Weapons.Pistols.Pistol_Torgue_3_PocketRocket."""

    path: ClassVar[str] = "GD_Iris_Weapons.Pistols.Pistol_Torgue_3_PocketRocket"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_C | None = None


@dataclass
class Cobra_Sniper_Jakobs_3_Cobra:
    """GD_Iris_Weapons.SniperRifles.Sniper_Jakobs_3_Cobra."""

    path: ClassVar[str] = "GD_Iris_Weapons.SniperRifles.Sniper_Jakobs_3_Cobra"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Boom_Puppy_Ar_Torgue_3_Boompuppy:
    """GD_Iris_Weapons.AssaultRifles.AR_Torgue_3_BoomPuppy."""

    path: ClassVar[str] = "GD_Iris_Weapons.AssaultRifles.AR_Torgue_3_BoomPuppy"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_C | None = None


@dataclass
class Kitten_Ar_Vladof_3_Kitten:
    """GD_Iris_Weapons.AssaultRifles.AR_Vladof_3_Kitten."""

    path: ClassVar[str] = "GD_Iris_Weapons.AssaultRifles.AR_Vladof_3_Kitten"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_B | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Carnage_Sg_Torgue_6_Carnage:
    """GD_Lobelia_Weapons.Shotguns.SG_Torgue_6_Carnage."""

    path: ClassVar[str] = "GD_Lobelia_Weapons.Shotguns.SG_Torgue_6_Carnage"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_G | None = None


@dataclass
class Wanderlust_Pistol_Maliwan_6_Wanderlust:
    """GD_Lobelia_Weapons.Pistol.Pistol_Maliwan_6_Wanderlust."""

    path: ClassVar[str] = "GD_Lobelia_Weapons.Pistol.Pistol_Maliwan_6_Wanderlust"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    element: Pistol_Elemental_C | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Godfinger_Sniper_Jakobs_6_Godfinger:
    """GD_Lobelia_Weapons.sniper.Sniper_Jakobs_6_Godfinger."""

    path: ClassVar[str] = "GD_Lobelia_Weapons.sniper.Sniper_Jakobs_6_Godfinger"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Bekah_Ar_Jakobs_6_Bekah:
    """GD_Lobelia_Weapons.AssaultRifles.AR_Jakobs_6_Bekah."""

    path: ClassVar[str] = "GD_Lobelia_Weapons.AssaultRifles.AR_Jakobs_6_Bekah"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Greed_Pistol_Jakobs_Scarletsgreed:
    """GD_Orchid_BossWeapons.Pistol.Pistol_Jakobs_ScarletsGreed."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.Pistol.Pistol_Jakobs_ScarletsGreed"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class _12_Pounder_Rl_Torgue_3_12pounder:
    """GD_Orchid_BossWeapons.Launcher.RL_Torgue_3_12Pounder."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.Launcher.RL_Torgue_3_12Pounder"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Little_Evie_Pistol_Maliwan_3_Littleevie:
    """GD_Orchid_BossWeapons.Pistol.Pistol_Maliwan_3_LittleEvie."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.Pistol.Pistol_Maliwan_3_LittleEvie"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Stinkpot_Ar_Jakobs_3_Stinkpot:
    """GD_Orchid_BossWeapons.AssaultRifle.AR_Jakobs_3_Stinkpot."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.AssaultRifle.AR_Jakobs_3_Stinkpot"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_D | None = None


@dataclass
class Devastator_Orchid_Seraph_Devastator_Balance:
    """GD_Orchid_RaidWeapons.Pistol.Devastator.Orchid_Seraph_Devastator_Balance."""

    path: ClassVar[str] = "GD_Orchid_RaidWeapons.Pistol.Devastator.Orchid_Seraph_Devastator_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_D | None = None


@dataclass
class Tattler_Orchid_Seraph_Tattler_Balance:
    """GD_Orchid_RaidWeapons.SMG.Tattler.Orchid_Seraph_Tattler_Balance."""

    path: ClassVar[str] = "GD_Orchid_RaidWeapons.SMG.Tattler.Orchid_Seraph_Tattler_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None


@dataclass
class Retcher_Orchid_Seraph_Spitter_Balance:
    """GD_Orchid_RaidWeapons.Shotgun.Spitter.Orchid_Seraph_Spitter_Balance."""

    path: ClassVar[str] = "GD_Orchid_RaidWeapons.Shotgun.Spitter.Orchid_Seraph_Spitter_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_B | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Actualizer_Orchid_Seraph_Actualizer_Balance:
    """GD_Orchid_RaidWeapons.SMG.Actualizer.Orchid_Seraph_Actualizer_Balance."""

    path: ClassVar[str] = "GD_Orchid_RaidWeapons.SMG.Actualizer.Orchid_Seraph_Actualizer_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Seraphim_Orchid_Seraph_Seraphim_Balance:
    """GD_Orchid_RaidWeapons.AssaultRifle.Seraphim.Orchid_Seraph_Seraphim_Balance."""

    path: ClassVar[str] = "GD_Orchid_RaidWeapons.AssaultRifle.Seraphim.Orchid_Seraph_Seraphim_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_A | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Patriot_Orchid_Seraph_Patriot_Balance:
    """GD_Orchid_RaidWeapons.sniper.Patriot.Orchid_Seraph_Patriot_Balance."""

    path: ClassVar[str] = "GD_Orchid_RaidWeapons.sniper.Patriot.Orchid_Seraph_Patriot_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Ahab_Orchid_Seraph_Ahab_Balance:
    """GD_Orchid_RaidWeapons.RPG.Ahab.Orchid_Seraph_Ahab_Balance."""

    path: ClassVar[str] = "GD_Orchid_RaidWeapons.RPG.Ahab.Orchid_Seraph_Ahab_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    sight: Rl_Sight | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_A | None = None


@dataclass
class Error_Message_Error_Message_Orchid_Boss_Ahab_Balance_Nodrop:
    """GD_Orchid_BossWeapons.RPG.Ahab.Orchid_Boss_Ahab_Balance_NODROP."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.RPG.Ahab.Orchid_Boss_Ahab_Balance_NODROP"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    stock: L_Exhaust | None = None


@dataclass
class Rapier_Ar_Vladof_3_Rapier:
    """GD_Orchid_BossWeapons.AssaultRifle.AR_Vladof_3_Rapier."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.AssaultRifle.AR_Vladof_3_Rapier"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_C | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_E | None = None


@dataclass
class Jolly_Roger_Sg_Bandit_3_Jollyroger:
    """GD_Orchid_BossWeapons.Shotgun.SG_Bandit_3_JollyRoger."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.Shotgun.SG_Bandit_3_JollyRoger"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_A | None = None


@dataclass
class Orphan_Maker_Sg_Jakobs_3_Orphanmaker:
    """GD_Orchid_BossWeapons.Shotgun.SG_Jakobs_3_OrphanMaker."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.Shotgun.SG_Jakobs_3_OrphanMaker"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Sand_Hawk_Smg_Dahl_3_Sandhawk:
    """GD_Orchid_BossWeapons.SMG.SMG_Dahl_3_SandHawk."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.SMG.SMG_Dahl_3_SandHawk"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_A | None = None
    stock: Smg_Stock | None = None
    element: Smg_Elemental_A | None = None
    accessory1: Smg_Accessory_A | None = None


@dataclass
class Pimpernel_Sniper_Maliwan_3_Pimpernel:
    """GD_Orchid_BossWeapons.SniperRifles.Sniper_Maliwan_3_Pimpernel."""

    path: ClassVar[str] = "GD_Orchid_BossWeapons.SniperRifles.Sniper_Maliwan_3_Pimpernel"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    element: Sr_Elemental_B | None = None
    accessory1: Sniper_A | None = None


@dataclass
class Boom_Sage_Harpoongun_Balance:
    """GD_Sage_HarpoonGun.Balance.Sage_HarpoonGun_Balance."""

    path: ClassVar[str] = "GD_Sage_HarpoonGun.Balance.Sage_HarpoonGun_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: L_Grip | None = None
    stock: L_Exhaust | None = None
    accessory1: Rl_Accessory_B | None = None


@dataclass
class Hawk_Eye_Sage_Seraph_Hawkeye_Balance:
    """GD_Sage_RaidWeapons.sniper.Sage_Seraph_HawkEye_Balance."""

    path: ClassVar[str] = "GD_Sage_RaidWeapons.sniper.Sage_Seraph_HawkEye_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    sight: Sniper_Sight | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_Accessory | None = None


@dataclass
class Infection_Sage_Seraph_Infection_Balance:
    """GD_Sage_RaidWeapons.Pistol.Sage_Seraph_Infection_Balance."""

    path: ClassVar[str] = "GD_Sage_RaidWeapons.Pistol.Sage_Seraph_Infection_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_B | None = None
    sight: Pistol_Sight_B | None = None
    accessory1: Pistol_Accessory_B | None = None


@dataclass
class Interfacer_Sage_Seraph_Interfacer_Balance:
    """GD_Sage_RaidWeapons.Shotgun.Sage_Seraph_Interfacer_Balance."""

    path: ClassVar[str] = "GD_Sage_RaidWeapons.Shotgun.Sage_Seraph_Interfacer_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    stock: Sg_Stock | None = None
    element: Shotgun_Elemental_A | None = None
    accessory1: Sg_Accessory_C | None = None


@dataclass
class Lead_Storm_Sage_Seraph_Leadstorm_Balance:
    """GD_Sage_RaidWeapons.AssaultRifle.Sage_Seraph_LeadStorm_Balance."""

    path: ClassVar[str] = "GD_Sage_RaidWeapons.AssaultRifle.Sage_Seraph_LeadStorm_Balance"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_D | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_B | None = None


@dataclass
class Rex_Pistol_Jakobs_3_Rex:
    """GD_Sage_Weapons.Pistols.Pistol_Jakobs_3_Rex."""

    path: ClassVar[str] = "GD_Sage_Weapons.Pistols.Pistol_Jakobs_3_Rex"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Pistol_Grip_A | None = None
    sight: Pistol_Sight_A | None = None
    accessory1: Pistol_Accessory_A | None = None


@dataclass
class Hydra_Sg_Jakobs_3_Hydra:
    """GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Hydra."""

    path: ClassVar[str] = "GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Hydra"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


@dataclass
class Damned_Cowboy_Ar_Jakobs_3_Damnedcowboy:
    """GD_Sage_Weapons.AssaultRifle.AR_Jakobs_3_DamnedCowboy."""

    path: ClassVar[str] = "GD_Sage_Weapons.AssaultRifle.AR_Jakobs_3_DamnedCowboy"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    accessory1: Ar_Accessory_F | None = None


@dataclass
class Elephant_Gun_Sniper_Jakobs_3_Elephantgun:
    """GD_Sage_Weapons.SniperRifles.Sniper_Jakobs_3_ElephantGun."""

    path: ClassVar[str] = "GD_Sage_Weapons.SniperRifles.Sniper_Jakobs_3_ElephantGun"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sr_Grip | None = None
    stock: Sr_Stock_A | None = None
    accessory1: Sniper_B | None = None


@dataclass
class Chopper_Ar_Bandit_3_Chopper:
    """GD_Sage_Weapons.AssaultRifle.AR_Bandit_3_Chopper."""

    path: ClassVar[str] = "GD_Sage_Weapons.AssaultRifle.AR_Bandit_3_Chopper"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Ar_Grip | None = None
    sight: Ar_Sight_B | None = None
    stock: Ar_Stock | None = None
    element: Ar_Elemental_A | None = None
    accessory1: Ar_Accessory_C | None = None


@dataclass
class Yellow_Jacket_Smg_Hyperion_3_Yellowjacket:
    """GD_Sage_Weapons.SMG.SMG_Hyperion_3_YellowJacket."""

    path: ClassVar[str] = "GD_Sage_Weapons.SMG.SMG_Hyperion_3_YellowJacket"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Smg_Grip | None = None
    sight: Smg_Sight_B | None = None
    stock: Smg_Stock | None = None
    accessory1: Smg_Accessory_C | None = None


@dataclass
class Twister_Sg_Jakobs_3_Twister:
    """GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Twister."""

    path: ClassVar[str] = "GD_Sage_Weapons.Shotgun.SG_Jakobs_3_Twister"
    class_name: ClassVar[str] = "WeaponBalanceDefinition"
    levels: list[int]
    grip: Sg_Grip | None = None
    sight: Sg_Sight_A | None = None
    stock: Sg_Stock | None = None
    accessory1: Sg_Accessory_D | None = None


