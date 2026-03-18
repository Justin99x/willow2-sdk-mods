from enum import StrEnum


class Smg_Grip(StrEnum):
    smg_grip_bandit = "GD_Weap_SMG.Grip.SMG_Grip_Bandit"
    smg_grip_dahl = "GD_Weap_SMG.Grip.SMG_Grip_Dahl"
    smg_grip_hyperion = "GD_Weap_SMG.Grip.SMG_Grip_Hyperion"
    smg_grip_maliwan = "GD_Weap_SMG.Grip.SMG_Grip_Maliwan"
    smg_grip_tediore = "GD_Weap_SMG.Grip.SMG_Grip_Tediore"

    _defdata_field = "GripPartDefinition"


class Smg_Sight_A(StrEnum):
    smg_sight_bandit = "GD_Weap_SMG.Sight.SMG_Sight_Bandit"
    smg_sight_dahl = "GD_Weap_SMG.Sight.SMG_Sight_Dahl"
    smg_sight_hyperion = "GD_Weap_SMG.Sight.SMG_Sight_Hyperion"
    smg_sight_maliwan = "GD_Weap_SMG.Sight.SMG_Sight_Maliwan"
    smg_sight_none = "GD_Weap_SMG.Sight.SMG_Sight_None"
    smg_sight_tedior = "GD_Weap_SMG.Sight.SMG_Sight_Tedior"

    _defdata_field = "SightPartDefinition"


class Smg_Stock(StrEnum):
    smg_stock_bandit = "GD_Weap_SMG.Stock.SMG_Stock_Bandit"
    smg_stock_dahl = "GD_Weap_SMG.Stock.SMG_Stock_Dahl"
    smg_stock_hyperion = "GD_Weap_SMG.Stock.SMG_Stock_Hyperion"
    smg_stock_maliwan = "GD_Weap_SMG.Stock.SMG_Stock_Maliwan"
    smg_stock_tediore = "GD_Weap_SMG.Stock.SMG_Stock_Tediore"

    _defdata_field = "StockPartDefinition"


class Smg_Accessory_A(StrEnum):
    smg_accessory_bayonet_1 = "GD_Weap_SMG.Accessory.SMG_Accessory_Bayonet_1"
    smg_accessory_body1_accurate = "GD_Weap_SMG.Accessory.SMG_Accessory_Body1_Accurate"
    smg_accessory_body2_damage = "GD_Weap_SMG.Accessory.SMG_Accessory_Body2_Damage"
    smg_accessory_body3_accelerated = "GD_Weap_SMG.Accessory.SMG_Accessory_Body3_Accelerated"
    smg_accessory_none = "GD_Weap_SMG.Accessory.SMG_Accessory_None"
    smg_accessory_stock1_stabilized = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock1_Stabilized"
    smg_accessory_stock2_reload = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock2_Reload"

    _defdata_field = "Accessory1PartDefinition"


class Pistol_Sight_A(StrEnum):
    pistol_sight_bandit = "GD_Weap_Pistol.Sight.Pistol_Sight_Bandit"
    pistol_sight_dahl = "GD_Weap_Pistol.Sight.Pistol_Sight_Dahl"
    pistol_sight_hyperion = "GD_Weap_Pistol.Sight.Pistol_Sight_Hyperion"
    pistol_sight_jakobs = "GD_Weap_Pistol.Sight.Pistol_Sight_Jakobs"
    pistol_sight_maliwan = "GD_Weap_Pistol.Sight.Pistol_Sight_Maliwan"
    pistol_sight_none = "GD_Weap_Pistol.Sight.Pistol_Sight_None"
    pistol_sight_tediore = "GD_Weap_Pistol.Sight.Pistol_Sight_Tediore"
    pistol_sight_torgue = "GD_Weap_Pistol.Sight.Pistol_Sight_Torgue"
    pistol_sight_vladof = "GD_Weap_Pistol.Sight.Pistol_Sight_Vladof"

    _defdata_field = "SightPartDefinition"


class Pistol_Elemental_A(StrEnum):
    pistol_elemental_corrosive = "GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive"
    pistol_elemental_fire = "GD_Weap_Pistol.elemental.Pistol_Elemental_Fire"
    pistol_elemental_none = "GD_Weap_Pistol.elemental.Pistol_Elemental_None"
    pistol_elemental_shock = "GD_Weap_Pistol.elemental.Pistol_Elemental_Shock"
    pistol_elemental_slag = "GD_Weap_Pistol.elemental.Pistol_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Pistol_Accessory_A(StrEnum):
    pistol_accessory_bayonet_1 = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Bayonet_1"
    pistol_accessory_laser_accuracy = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Accuracy"
    pistol_accessory_laser_double = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Double"
    pistol_accessory_none = "GD_Weap_Pistol.Accessory.Pistol_Accessory_None"
    pistol_accessory_stock_stability = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Stock_Stability"
    pistol_accessory_tech_1_mag = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_1_Mag"
    pistol_accessory_tech_2_damage = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_2_Damage"
    pistol_accessory_tech_3_firerate = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_3_Firerate"

    _defdata_field = "Accessory1PartDefinition"


class Sg_Grip(StrEnum):
    sg_grip_bandit = "GD_Weap_Shotgun.Grip.SG_Grip_Bandit"
    sg_grip_hyperion = "GD_Weap_Shotgun.Grip.SG_Grip_Hyperion"
    sg_grip_jakobs = "GD_Weap_Shotgun.Grip.SG_Grip_Jakobs"
    sg_grip_tediore = "GD_Weap_Shotgun.Grip.SG_Grip_Tediore"
    sg_grip_torgue = "GD_Weap_Shotgun.Grip.SG_Grip_Torgue"

    _defdata_field = "GripPartDefinition"


class Sg_Barrel_A(StrEnum):
    sg_barrel_hyperion = "GD_Weap_Shotgun.Barrel.SG_Barrel_Hyperion"
    sg_barrel_jakobs = "GD_Weap_Shotgun.Barrel.SG_Barrel_Jakobs"
    sg_barrel_tediore = "GD_Weap_Shotgun.Barrel.SG_Barrel_Tediore"

    _defdata_field = "BarrelPartDefinition"


class Sg_Stock(StrEnum):
    sg_stock_bandit = "GD_Weap_Shotgun.Stock.SG_Stock_Bandit"
    sg_stock_hyperion = "GD_Weap_Shotgun.Stock.SG_Stock_Hyperion"
    sg_stock_jakobs = "GD_Weap_Shotgun.Stock.SG_Stock_Jakobs"
    sg_stock_tediore = "GD_Weap_Shotgun.Stock.SG_Stock_Tediore"
    sg_stock_torgue = "GD_Weap_Shotgun.Stock.SG_Stock_Torgue"

    _defdata_field = "StockPartDefinition"


class Pistol_Grip_A(StrEnum):
    pistol_grip_bandit = "GD_Weap_Pistol.Grip.Pistol_Grip_Bandit"
    pistol_grip_dahl = "GD_Weap_Pistol.Grip.Pistol_Grip_Dahl"
    pistol_grip_hyperion = "GD_Weap_Pistol.Grip.Pistol_Grip_Hyperion"
    pistol_grip_jakobs = "GD_Weap_Pistol.Grip.Pistol_Grip_Jakobs"
    pistol_grip_maliwan = "GD_Weap_Pistol.Grip.Pistol_Grip_Maliwan"
    pistol_grip_torgue = "GD_Weap_Pistol.Grip.Pistol_Grip_Torgue"
    pistol_grip_vladof = "GD_Weap_Pistol.Grip.Pistol_Grip_Vladof"

    _defdata_field = "GripPartDefinition"


class Pistol_Barrel_A(StrEnum):
    pistol_barrel_bandit = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Bandit"
    pistol_barrel_dahl = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Dahl"
    pistol_barrel_maliwan = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Maliwan"
    pistol_barrel_tediore = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Tediore"
    pistol_barrel_torgue = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Torgue"

    _defdata_field = "BarrelPartDefinition"


class Pistol_Grip_B(StrEnum):
    pistol_grip_bandit = "GD_Weap_Pistol.Grip.Pistol_Grip_Bandit"
    pistol_grip_dahl = "GD_Weap_Pistol.Grip.Pistol_Grip_Dahl"
    pistol_grip_hyperion = "GD_Weap_Pistol.Grip.Pistol_Grip_Hyperion"
    pistol_grip_jakobs = "GD_Weap_Pistol.Grip.Pistol_Grip_Jakobs"
    pistol_grip_maliwan = "GD_Weap_Pistol.Grip.Pistol_Grip_Maliwan"
    pistol_grip_tediore = "GD_Weap_Pistol.Grip.Pistol_Grip_Tediore"
    pistol_grip_torgue = "GD_Weap_Pistol.Grip.Pistol_Grip_Torgue"
    pistol_grip_vladof = "GD_Weap_Pistol.Grip.Pistol_Grip_Vladof"

    _defdata_field = "GripPartDefinition"


class Pistol_Grip_C(StrEnum):
    pistol_grip_dahl = "GD_Weap_Pistol.Grip.Pistol_Grip_Dahl"
    pistol_grip_hyperion = "GD_Weap_Pistol.Grip.Pistol_Grip_Hyperion"
    pistol_grip_jakobs = "GD_Weap_Pistol.Grip.Pistol_Grip_Jakobs"
    pistol_grip_maliwan = "GD_Weap_Pistol.Grip.Pistol_Grip_Maliwan"
    pistol_grip_torgue = "GD_Weap_Pistol.Grip.Pistol_Grip_Torgue"
    pistol_grip_vladof = "GD_Weap_Pistol.Grip.Pistol_Grip_Vladof"

    _defdata_field = "GripPartDefinition"


class Sr_Grip(StrEnum):
    sr_grip_dahl = "GD_Weap_SniperRifles.Grip.SR_Grip_Dahl"
    sr_grip_hyperion = "GD_Weap_SniperRifles.Grip.SR_Grip_Hyperion"
    sr_grip_jakobs = "GD_Weap_SniperRifles.Grip.SR_Grip_Jakobs"
    sr_grip_maliwan = "GD_Weap_SniperRifles.Grip.SR_Grip_Maliwan"
    sr_grip_vladof = "GD_Weap_SniperRifles.Grip.SR_Grip_Vladof"

    _defdata_field = "GripPartDefinition"


class Sr_Stock_A(StrEnum):
    sr_stock_dahl = "GD_Weap_SniperRifles.Stock.SR_Stock_Dahl"
    sr_stock_hyperion = "GD_Weap_SniperRifles.Stock.SR_Stock_Hyperion"
    sr_stock_jakobs = "GD_Weap_SniperRifles.Stock.SR_Stock_Jakobs"
    sr_stock_maliwan = "GD_Weap_SniperRifles.Stock.SR_Stock_Maliwan"
    sr_stock_vladof = "GD_Weap_SniperRifles.Stock.SR_Stock_Vladof"

    _defdata_field = "StockPartDefinition"


class Sr_Elemental_A(StrEnum):
    sr_elemental_corrosive = "GD_Weap_SniperRifles.elemental.SR_Elemental_Corrosive"
    sr_elemental_fire = "GD_Weap_SniperRifles.elemental.SR_Elemental_Fire"
    sr_elemental_none = "GD_Weap_SniperRifles.elemental.SR_Elemental_None"
    sr_elemental_shock = "GD_Weap_SniperRifles.elemental.SR_Elemental_Shock"
    sr_elemental_slag = "GD_Weap_SniperRifles.elemental.SR_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Sniper_A(StrEnum):
    sniper_accessory_bayonet1 = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Bayonet1"
    sniper_accessory_bipod1_accuracy = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Bipod1_Accuracy"
    sniper_accessory_bipod2_critical = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Bipod2_Critical"
    sniper_accessory_foregrip_stability = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Foregrip_Stability"
    sniper_accessory_mount1_mag = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Mount1_Mag"
    sniper_accessory_mount2_firerate = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Mount2_FireRate"
    sniper_accessory_mount3_damage = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Mount3_Damage"
    sniperl_accessory_none = "GD_Weap_SniperRifles.Accessory.Sniperl_Accessory_None"

    _defdata_field = "Accessory1PartDefinition"


class Sg_Sight_A(StrEnum):
    sg_sight_bandit = "GD_Weap_Shotgun.Sight.SG_Sight_Bandit"
    sg_sight_hyperion = "GD_Weap_Shotgun.Sight.SG_Sight_Hyperion"
    sg_sight_jakobs = "GD_Weap_Shotgun.Sight.SG_Sight_Jakobs"
    sg_sight_none = "GD_Weap_Shotgun.Sight.SG_Sight_None"
    sg_sight_tediore = "GD_Weap_Shotgun.Sight.SG_Sight_Tediore"
    sg_sight_torgue = "GD_Weap_Shotgun.Sight.SG_Sight_Torgue"

    _defdata_field = "SightPartDefinition"


class Shotgun_Elemental_A(StrEnum):
    shotgun_elemental_corrosive = "GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive"
    shotgun_elemental_fire = "GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire"
    shotgun_elemental_none = "GD_Weap_Shotgun.elemental.Shotgun_Elemental_None"
    shotgun_elemental_shock = "GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock"
    shotgun_elemental_slag = "GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Sg_Accessory_A(StrEnum):
    sg_accessory_bayonet_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Bayonet_2"
    sg_accessory_moonclip = "GD_Weap_Shotgun.Accessory.SG_Accessory_MoonClip"
    sg_accessory_none = "GD_Weap_Shotgun.Accessory.SG_Accessory_None"
    sg_accessory_shotgunshell = "GD_Weap_Shotgun.Accessory.SG_Accessory_ShotgunShell"
    sg_accessory_tech_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_1"
    sg_accessory_tech_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_2"
    sg_accessory_tech_3 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_3"
    sg_accessory_verticalgrip = "GD_Weap_Shotgun.Accessory.SG_Accessory_VerticalGrip"

    _defdata_field = "Accessory1PartDefinition"


class Sg_Sight_B(StrEnum):
    sg_sight_bandit = "GD_Weap_Shotgun.Sight.SG_Sight_Bandit"
    sg_sight_hyperion = "GD_Weap_Shotgun.Sight.SG_Sight_Hyperion"
    sg_sight_jakobs = "GD_Weap_Shotgun.Sight.SG_Sight_Jakobs"
    sg_sight_tediore = "GD_Weap_Shotgun.Sight.SG_Sight_Tediore"
    sg_sight_torgue = "GD_Weap_Shotgun.Sight.SG_Sight_Torgue"

    _defdata_field = "SightPartDefinition"


class Sg_Accessory_B(StrEnum):
    sg_accessory_bayonet_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Bayonet_2"
    sg_accessory_moonclip = "GD_Weap_Shotgun.Accessory.SG_Accessory_MoonClip"
    sg_accessory_shotgunshell = "GD_Weap_Shotgun.Accessory.SG_Accessory_ShotgunShell"
    sg_accessory_tech_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_1"
    sg_accessory_tech_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_2"
    sg_accessory_tech_3 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_3"
    sg_accessory_verticalgrip = "GD_Weap_Shotgun.Accessory.SG_Accessory_VerticalGrip"

    _defdata_field = "Accessory1PartDefinition"


class L_Grip(StrEnum):
    l_grip_bandit = "GD_Weap_Launchers.Grip.L_Grip_Bandit"
    l_grip_maliwan = "GD_Weap_Launchers.Grip.L_Grip_Maliwan"
    l_grip_tediore = "GD_Weap_Launchers.Grip.L_Grip_Tediore"
    l_grip_torgue = "GD_Weap_Launchers.Grip.L_Grip_Torgue"
    l_grip_vladof = "GD_Weap_Launchers.Grip.L_Grip_Vladof"

    _defdata_field = "GripPartDefinition"


class Rl_Sight(StrEnum):
    rl_sight_bandit = "GD_Weap_Launchers.Sight.RL_Sight_Bandit"
    rl_sight_maliwan = "GD_Weap_Launchers.Sight.RL_Sight_Maliwan"
    rl_sight_tediore = "GD_Weap_Launchers.Sight.RL_Sight_Tediore"
    rl_sight_torgue = "GD_Weap_Launchers.Sight.RL_Sight_Torgue"
    rl_sight_vladof = "GD_Weap_Launchers.Sight.RL_Sight_Vladof"

    _defdata_field = "SightPartDefinition"


class L_Exhaust(StrEnum):
    l_exhaust_bandit = "GD_Weap_Launchers.Exhaust.L_Exhaust_Bandit"
    l_exhaust_maliwan = "GD_Weap_Launchers.Exhaust.L_Exhaust_Maliwan"
    l_exhaust_tediore = "GD_Weap_Launchers.Exhaust.L_Exhaust_Tediore"
    l_exhaust_torgue = "GD_Weap_Launchers.Exhaust.L_Exhaust_Torgue"
    l_exhaust_vladof = "GD_Weap_Launchers.Exhaust.L_Exhaust_Vladof"

    _defdata_field = "StockPartDefinition"


class Rl_Accessory_A(StrEnum):
    rl_accessory_bodymod_1_mag = "GD_Weap_Launchers.Accessory.RL_Accessory_BodyMod_1_Mag"
    rl_accessory_bodymod_2_acc = "GD_Weap_Launchers.Accessory.RL_Accessory_BodyMod_2_Acc"
    rl_accessory_gripper_reload = "GD_Weap_Launchers.Accessory.RL_Accessory_Gripper_Reload"
    rl_accessory_handle_swapspeed = "GD_Weap_Launchers.Accessory.RL_Accessory_Handle_SwapSpeed"
    rl_accessory_stockcover_rocketspeed = "GD_Weap_Launchers.Accessory.RL_Accessory_StockCover_RocketSpeed"
    rl_accessory_stocktube_firerate = "GD_Weap_Launchers.Accessory.RL_Accessory_StockTube_FireRate"
    rl_accessory_tipcover_damage = "GD_Weap_Launchers.Accessory.RL_Accessory_TipCover_Damage"

    _defdata_field = "Accessory1PartDefinition"


class Smg_Elemental_A(StrEnum):
    smg_elemental_corrosive = "GD_Weap_SMG.elemental.SMG_Elemental_Corrosive"
    smg_elemental_fire = "GD_Weap_SMG.elemental.SMG_Elemental_Fire"
    smg_elemental_none = "GD_Weap_SMG.elemental.SMG_Elemental_None"
    smg_elemental_shock = "GD_Weap_SMG.elemental.SMG_Elemental_Shock"
    smg_elemental_slag = "GD_Weap_SMG.elemental.SMG_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Smg_Accessory_B(StrEnum):
    smg_accessory_bayonet_2 = "GD_Weap_SMG.Accessory.SMG_Accessory_Bayonet_2"
    smg_accessory_body1_accurate = "GD_Weap_SMG.Accessory.SMG_Accessory_Body1_Accurate"
    smg_accessory_body2_damage = "GD_Weap_SMG.Accessory.SMG_Accessory_Body2_Damage"
    smg_accessory_body3_accelerated = "GD_Weap_SMG.Accessory.SMG_Accessory_Body3_Accelerated"
    smg_accessory_none = "GD_Weap_SMG.Accessory.SMG_Accessory_None"
    smg_accessory_stock1_stabilized = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock1_Stabilized"
    smg_accessory_stock2_reload = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock2_Reload"

    _defdata_field = "Accessory1PartDefinition"


class Smg_Sight_B(StrEnum):
    smg_sight_bandit = "GD_Weap_SMG.Sight.SMG_Sight_Bandit"
    smg_sight_dahl = "GD_Weap_SMG.Sight.SMG_Sight_Dahl"
    smg_sight_hyperion = "GD_Weap_SMG.Sight.SMG_Sight_Hyperion"
    smg_sight_maliwan = "GD_Weap_SMG.Sight.SMG_Sight_Maliwan"
    smg_sight_tedior = "GD_Weap_SMG.Sight.SMG_Sight_Tedior"

    _defdata_field = "SightPartDefinition"


class Smg_Accessory_C(StrEnum):
    smg_accessory_bayonet_1 = "GD_Weap_SMG.Accessory.SMG_Accessory_Bayonet_1"
    smg_accessory_body1_accurate = "GD_Weap_SMG.Accessory.SMG_Accessory_Body1_Accurate"
    smg_accessory_body2_damage = "GD_Weap_SMG.Accessory.SMG_Accessory_Body2_Damage"
    smg_accessory_body3_accelerated = "GD_Weap_SMG.Accessory.SMG_Accessory_Body3_Accelerated"
    smg_accessory_stock1_stabilized = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock1_Stabilized"
    smg_accessory_stock2_reload = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock2_Reload"

    _defdata_field = "Accessory1PartDefinition"


class Pistol_Sight_B(StrEnum):
    pistol_sight_bandit = "GD_Weap_Pistol.Sight.Pistol_Sight_Bandit"
    pistol_sight_dahl = "GD_Weap_Pistol.Sight.Pistol_Sight_Dahl"
    pistol_sight_hyperion = "GD_Weap_Pistol.Sight.Pistol_Sight_Hyperion"
    pistol_sight_jakobs = "GD_Weap_Pistol.Sight.Pistol_Sight_Jakobs"
    pistol_sight_maliwan = "GD_Weap_Pistol.Sight.Pistol_Sight_Maliwan"
    pistol_sight_tediore = "GD_Weap_Pistol.Sight.Pistol_Sight_Tediore"
    pistol_sight_torgue = "GD_Weap_Pistol.Sight.Pistol_Sight_Torgue"
    pistol_sight_vladof = "GD_Weap_Pistol.Sight.Pistol_Sight_Vladof"

    _defdata_field = "SightPartDefinition"


class Pistol_Accessory_B(StrEnum):
    pistol_accessory_bayonet_1 = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Bayonet_1"
    pistol_accessory_laser_accuracy = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Accuracy"
    pistol_accessory_laser_double = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Double"
    pistol_accessory_stock_stability = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Stock_Stability"
    pistol_accessory_tech_1_mag = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_1_Mag"
    pistol_accessory_tech_2_damage = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_2_Damage"
    pistol_accessory_tech_3_firerate = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_3_Firerate"

    _defdata_field = "Accessory1PartDefinition"


class Pistol_Accessory_C(StrEnum):
    pistol_accessory_bayonet_2 = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Bayonet_2"
    pistol_accessory_laser_accuracy = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Accuracy"
    pistol_accessory_laser_double = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Double"
    pistol_accessory_none = "GD_Weap_Pistol.Accessory.Pistol_Accessory_None"
    pistol_accessory_stock_stability = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Stock_Stability"
    pistol_accessory_tech_1_mag = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_1_Mag"
    pistol_accessory_tech_2_damage = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_2_Damage"
    pistol_accessory_tech_3_firerate = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_3_Firerate"

    _defdata_field = "Accessory1PartDefinition"


class Rl_Elemental_A(StrEnum):
    rl_elemental_corrosive = "GD_Weap_Launchers.elemental.RL_Elemental_Corrosive"
    rl_elemental_fire = "GD_Weap_Launchers.elemental.RL_Elemental_Fire"
    rl_elemental_none = "GD_Weap_Launchers.elemental.RL_Elemental_None"
    rl_elemental_shock = "GD_Weap_Launchers.elemental.RL_Elemental_Shock"
    rl_elemental_slag = "GD_Weap_Launchers.elemental.RL_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Sniper_Sight(StrEnum):
    sniper_sight_dahl = "GD_Weap_SniperRifles.Sight.Sniper_Sight_Dahl"
    sniper_sight_hyperion = "GD_Weap_SniperRifles.Sight.Sniper_Sight_Hyperion"
    sniper_sight_jakobs = "GD_Weap_SniperRifles.Sight.Sniper_Sight_Jakobs"
    sniper_sight_maliwan = "GD_Weap_SniperRifles.Sight.Sniper_Sight_Maliwan"
    sniper_sight_vladof = "GD_Weap_SniperRifles.Sight.Sniper_Sight_Vladof"

    _defdata_field = "SightPartDefinition"


class Sniper_Accessory(StrEnum):
    sniper_accessory_bayonet1 = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Bayonet1"
    sniper_accessory_bipod1_accuracy = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Bipod1_Accuracy"
    sniper_accessory_bipod2_critical = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Bipod2_Critical"
    sniper_accessory_foregrip_stability = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Foregrip_Stability"
    sniper_accessory_mount1_mag = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Mount1_Mag"
    sniper_accessory_mount2_firerate = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Mount2_FireRate"
    sniper_accessory_mount3_damage = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Mount3_Damage"

    _defdata_field = "Accessory1PartDefinition"


class Pistol_Accessory_D(StrEnum):
    pistol_accessory_bayonet_2 = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Bayonet_2"
    pistol_accessory_laser_accuracy = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Accuracy"
    pistol_accessory_laser_double = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Double"
    pistol_accessory_stock_stability = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Stock_Stability"
    pistol_accessory_tech_1_mag = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_1_Mag"
    pistol_accessory_tech_2_damage = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_2_Damage"
    pistol_accessory_tech_3_firerate = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_3_Firerate"

    _defdata_field = "Accessory1PartDefinition"


class Ar_Grip(StrEnum):
    ar_grip_bandit = "GD_Weap_AssaultRifle.Grip.AR_Grip_Bandit"
    ar_grip_dahl = "GD_Weap_AssaultRifle.Grip.AR_Grip_Dahl"
    ar_grip_jakobs = "GD_Weap_AssaultRifle.Grip.AR_Grip_Jakobs"
    ar_grip_torgue = "GD_Weap_AssaultRifle.Grip.AR_Grip_Torgue"
    ar_grip_vladof = "GD_Weap_AssaultRifle.Grip.AR_Grip_Vladof"

    _defdata_field = "GripPartDefinition"


class Ar_Sight_A(StrEnum):
    ar_sight_bandit = "GD_Weap_AssaultRifle.Sight.AR_Sight_Bandit"
    ar_sight_dahl = "GD_Weap_AssaultRifle.Sight.AR_Sight_Dahl"
    ar_sight_jakobs = "GD_Weap_AssaultRifle.Sight.AR_Sight_Jakobs"
    ar_sight_torgue = "GD_Weap_AssaultRifle.Sight.AR_Sight_Torgue"
    ar_sight_vladof = "GD_Weap_AssaultRifle.Sight.AR_Sight_Vladof"

    _defdata_field = "SightPartDefinition"


class Ar_Stock(StrEnum):
    ar_stock_bandit = "GD_Weap_AssaultRifle.Stock.AR_Stock_Bandit"
    ar_stock_dahl = "GD_Weap_AssaultRifle.Stock.AR_Stock_Dahl"
    ar_stock_jakobs = "GD_Weap_AssaultRifle.Stock.AR_Stock_Jakobs"
    ar_stock_torgue = "GD_Weap_AssaultRifle.Stock.AR_Stock_Torgue"
    ar_stock_vladof = "GD_Weap_AssaultRifle.Stock.AR_Stock_Vladof"

    _defdata_field = "StockPartDefinition"


class Ar_Elemental_A(StrEnum):
    ar_elemental_corrosive = "GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive"
    ar_elemental_fire = "GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire"
    ar_elemental_none = "GD_Weap_AssaultRifle.elemental.AR_Elemental_None"
    ar_elemental_shock = "GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock"
    ar_elemental_slag = "GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Ar_Accessory_A(StrEnum):
    ar_accessory_banditclamp_damage = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Damage"
    ar_accessory_banditclamp_wild = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Wild"
    ar_accessory_bayonet_2 = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Bayonet_2"
    ar_accessory_box_bulletspeed = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Box_BulletSpeed"
    ar_accessory_foregrip_stability = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Foregrip_Stability"
    ar_accessory_shroud1_magsize = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud1_MagSize"
    ar_accessory_shroud2_accuracy = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud2_Accuracy"

    _defdata_field = "Accessory1PartDefinition"


class Ar_Accessory_B(StrEnum):
    ar_accessory_banditclamp_damage = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Damage"
    ar_accessory_banditclamp_wild = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Wild"
    ar_accessory_bayonet_1 = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Bayonet_1"
    ar_accessory_box_bulletspeed = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Box_BulletSpeed"
    ar_accessory_foregrip_stability = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Foregrip_Stability"
    ar_accessory_shroud1_magsize = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud1_MagSize"
    ar_accessory_shroud2_accuracy = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud2_Accuracy"

    _defdata_field = "Accessory1PartDefinition"


class Pistol_Elemental_B(StrEnum):
    pistol_elemental_corrosive = "GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive"
    pistol_elemental_fire = "GD_Weap_Pistol.elemental.Pistol_Elemental_Fire"
    pistol_elemental_none = "GD_Weap_Pistol.elemental.Pistol_Elemental_None"
    pistol_elemental_shock = "GD_Weap_Pistol.elemental.Pistol_Elemental_Shock"

    _defdata_field = "ElementalPartDefinition"


class Pistol_Accessory_E(StrEnum):
    pistol_accessory_bayonet_1 = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Bayonet_1"
    pistol_accessory_laser_accuracy = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Accuracy"
    pistol_accessory_laser_double_dvainfinity = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Laser_Double_DvaInfinity"
    pistol_accessory_none = "GD_Weap_Pistol.Accessory.Pistol_Accessory_None"
    pistol_accessory_stock_stability = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Stock_Stability"
    pistol_accessory_tech_1_mag = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_1_Mag"
    pistol_accessory_tech_2_damage = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_2_Damage"
    pistol_accessory_tech_3_firerate = "GD_Weap_Pistol.Accessory.Pistol_Accessory_Tech_3_Firerate"

    _defdata_field = "Accessory1PartDefinition"


class Sg_Accessory_C(StrEnum):
    sg_accessory_bayonet_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Bayonet_1"
    sg_accessory_moonclip = "GD_Weap_Shotgun.Accessory.SG_Accessory_MoonClip"
    sg_accessory_shotgunshell = "GD_Weap_Shotgun.Accessory.SG_Accessory_ShotgunShell"
    sg_accessory_tech_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_1"
    sg_accessory_tech_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_2"
    sg_accessory_tech_3 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_3"
    sg_accessory_verticalgrip = "GD_Weap_Shotgun.Accessory.SG_Accessory_VerticalGrip"

    _defdata_field = "Accessory1PartDefinition"


class Rl_Accessory_B(StrEnum):
    rl_accessory_bodymod_1_mag = "GD_Weap_Launchers.Accessory.RL_Accessory_BodyMod_1_Mag"
    rl_accessory_bodymod_2_acc = "GD_Weap_Launchers.Accessory.RL_Accessory_BodyMod_2_Acc"
    rl_accessory_gripper_reload = "GD_Weap_Launchers.Accessory.RL_Accessory_Gripper_Reload"
    rl_accessory_handle_swapspeed = "GD_Weap_Launchers.Accessory.RL_Accessory_Handle_SwapSpeed"
    rl_accessory_none = "GD_Weap_Launchers.Accessory.RL_Accessory_None"
    rl_accessory_stockcover_rocketspeed = "GD_Weap_Launchers.Accessory.RL_Accessory_StockCover_RocketSpeed"
    rl_accessory_stocktube_firerate = "GD_Weap_Launchers.Accessory.RL_Accessory_StockTube_FireRate"
    rl_accessory_tipcover_damage = "GD_Weap_Launchers.Accessory.RL_Accessory_TipCover_Damage"

    _defdata_field = "Accessory1PartDefinition"


class Smg_Accessory_D(StrEnum):
    smg_accessory_bayonet_2 = "GD_Weap_SMG.Accessory.SMG_Accessory_Bayonet_2"
    smg_accessory_body1_accurate = "GD_Weap_SMG.Accessory.SMG_Accessory_Body1_Accurate"
    smg_accessory_body2_damage = "GD_Weap_SMG.Accessory.SMG_Accessory_Body2_Damage"
    smg_accessory_body3_accelerated = "GD_Weap_SMG.Accessory.SMG_Accessory_Body3_Accelerated"
    smg_accessory_stock1_stabilized = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock1_Stabilized"
    smg_accessory_stock2_reload = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock2_Reload"

    _defdata_field = "Accessory1PartDefinition"


class Rl_Elemental_B(StrEnum):
    rl_elemental_corrosive = "GD_Weap_Launchers.elemental.RL_Elemental_Corrosive"
    rl_elemental_fire = "GD_Weap_Launchers.elemental.RL_Elemental_Fire"
    rl_elemental_shock = "GD_Weap_Launchers.elemental.RL_Elemental_Shock"
    rl_elemental_slag = "GD_Weap_Launchers.elemental.RL_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Pistol_Sight_C(StrEnum):
    pistol_sight_bandit = "GD_Weap_Pistol.Sight.Pistol_Sight_Bandit"
    pistol_sight_dahl = "GD_Weap_Pistol.Sight.Pistol_Sight_Dahl"
    pistol_sight_hyperion = "GD_Weap_Pistol.Sight.Pistol_Sight_Hyperion"
    pistol_sight_jakobs = "GD_Weap_Pistol.Sight.Pistol_Sight_Jakobs"
    pistol_sight_maliwan = "GD_Weap_Pistol.Sight.Pistol_Sight_Maliwan"
    pistol_sight_tediore = "GD_Weap_Pistol.Sight.Pistol_Sight_Tediore"
    pistol_sight_torgue = "GD_Weap_Pistol.Sight.Pistol_Sight_Torgue"

    _defdata_field = "SightPartDefinition"


class Ar_Barrel_A(StrEnum):
    ar_barrel_bandit = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Bandit"
    ar_barrel_dahl = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Dahl"
    ar_barrel_vladof = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof"

    _defdata_field = "BarrelPartDefinition"


class Ar_Barrel_B(StrEnum):
    ar_barrel_bandit = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Bandit"
    ar_barrel_dahl = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Dahl"
    ar_barrel_jakobs = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Jakobs"
    ar_barrel_torgue_bandit = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Torgue_Bandit"
    ar_barrel_vladof = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof"
    ar_barrel_vladof_minigun = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof_Minigun"

    _defdata_field = "BarrelPartDefinition"


class Ar_Sight_B(StrEnum):
    ar_sight_bandit = "GD_Weap_AssaultRifle.Sight.AR_Sight_Bandit"
    ar_sight_dahl = "GD_Weap_AssaultRifle.Sight.AR_Sight_Dahl"
    ar_sight_jakobs = "GD_Weap_AssaultRifle.Sight.AR_Sight_Jakobs"
    ar_sight_none = "GD_Weap_AssaultRifle.Sight.AR_Sight_None"
    ar_sight_torgue = "GD_Weap_AssaultRifle.Sight.AR_Sight_Torgue"
    ar_sight_vladof = "GD_Weap_AssaultRifle.Sight.AR_Sight_Vladof"

    _defdata_field = "SightPartDefinition"


class Ar_Accessory_C(StrEnum):
    ar_accessory_banditclamp_damage = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Damage"
    ar_accessory_banditclamp_wild = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Wild"
    ar_accessory_bayonet_2 = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Bayonet_2"
    ar_accessory_box_bulletspeed = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Box_BulletSpeed"
    ar_accessory_foregrip_stability = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Foregrip_Stability"
    ar_accessory_none = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_None"
    ar_accessory_shroud1_magsize = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud1_MagSize"
    ar_accessory_shroud2_accuracy = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud2_Accuracy"

    _defdata_field = "Accessory1PartDefinition"


class Ar_Barrel_C(StrEnum):
    ar_barrel_bandit = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Bandit"
    ar_barrel_dahl = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Dahl"
    ar_barrel_jakobs = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Jakobs"
    ar_barrel_torgue_dahl = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Torgue_Dahl"
    ar_barrel_vladof = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof"
    ar_barrel_vladof_minigun = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof_Minigun"

    _defdata_field = "BarrelPartDefinition"


class Ar_Accessory_D(StrEnum):
    ar_accessory_banditclamp_damage = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Damage"
    ar_accessory_banditclamp_wild = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Wild"
    ar_accessory_bayonet_1 = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Bayonet_1"
    ar_accessory_box_bulletspeed = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Box_BulletSpeed"
    ar_accessory_foregrip_stability = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Foregrip_Stability"
    ar_accessory_none = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_None"
    ar_accessory_shroud1_magsize = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud1_MagSize"
    ar_accessory_shroud2_accuracy = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud2_Accuracy"

    _defdata_field = "Accessory1PartDefinition"


class Ar_Barrel_D(StrEnum):
    ar_barrel_bandit = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Bandit"
    ar_barrel_dahl = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Dahl"
    ar_barrel_jakobs = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Jakobs"
    ar_barrel_torgue_jakobs = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Torgue_Jakobs"
    ar_barrel_vladof = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof"
    ar_barrel_vladof_minigun = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof_Minigun"

    _defdata_field = "BarrelPartDefinition"


class Ar_Barrel_E(StrEnum):
    ar_barrel_bandit = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Bandit"
    ar_barrel_dahl = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Dahl"
    ar_barrel_jakobs = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Jakobs"
    ar_barrel_torgue_torgue = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Torgue_Torgue"
    ar_barrel_vladof = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof"
    ar_barrel_vladof_minigun = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof_Minigun"

    _defdata_field = "BarrelPartDefinition"


class Ar_Barrel_F(StrEnum):
    ar_barrel_bandit = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Bandit"
    ar_barrel_dahl = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Dahl"
    ar_barrel_jakobs = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Jakobs"
    ar_barrel_torgue_vladof = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Torgue_Vladof"
    ar_barrel_vladof = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof"
    ar_barrel_vladof_minigun = "GD_Weap_AssaultRifle.Barrel.AR_Barrel_Vladof_Minigun"

    _defdata_field = "BarrelPartDefinition"


class Ar_Elemental_B(StrEnum):
    ar_elemental_corrosive = "GD_Weap_AssaultRifle.elemental.AR_Elemental_Corrosive"
    ar_elemental_fire = "GD_Weap_AssaultRifle.elemental.AR_Elemental_Fire"
    ar_elemental_shock = "GD_Weap_AssaultRifle.elemental.AR_Elemental_Shock"
    ar_elemental_slag = "GD_Weap_AssaultRifle.elemental.AR_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class L_Barrel(StrEnum):
    l_barrel_bandit = "GD_Weap_Launchers.Barrel.L_Barrel_Bandit"
    l_barrel_maliwan = "GD_Weap_Launchers.Barrel.L_Barrel_Maliwan"
    l_barrel_tediore = "GD_Weap_Launchers.Barrel.L_Barrel_Tediore"
    l_barrel_torgue = "GD_Weap_Launchers.Barrel.L_Barrel_Torgue"
    l_barrel_vladof = "GD_Weap_Launchers.Barrel.L_Barrel_Vladof"

    _defdata_field = "BarrelPartDefinition"


class Sg_Accessory_D(StrEnum):
    sg_accessory_bayonet_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Bayonet_1"
    sg_accessory_moonclip = "GD_Weap_Shotgun.Accessory.SG_Accessory_MoonClip"
    sg_accessory_none = "GD_Weap_Shotgun.Accessory.SG_Accessory_None"
    sg_accessory_shotgunshell = "GD_Weap_Shotgun.Accessory.SG_Accessory_ShotgunShell"
    sg_accessory_tech_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_1"
    sg_accessory_tech_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_2"
    sg_accessory_tech_3 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_3"
    sg_accessory_verticalgrip = "GD_Weap_Shotgun.Accessory.SG_Accessory_VerticalGrip"

    _defdata_field = "Accessory1PartDefinition"


class Sniper_B(StrEnum):
    sniper_accessory_bayonet1 = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Bayonet1"
    sniper_accessory_bipod1_accuracy = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Bipod1_Accuracy"
    sniper_accessory_bipod2_critical = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Bipod2_Critical"
    sniper_accessory_foregrip_stability = "GD_Weap_SniperRifles.Accessory.Sniper_Accessory_Foregrip_Stability"
    sniperl_accessory_none = "GD_Weap_SniperRifles.Accessory.Sniperl_Accessory_None"

    _defdata_field = "Accessory1PartDefinition"


class Pistol_Elemental_C(StrEnum):
    pistol_elemental_corrosive = "GD_Weap_Pistol.elemental.Pistol_Elemental_Corrosive"
    pistol_elemental_fire = "GD_Weap_Pistol.elemental.Pistol_Elemental_Fire"
    pistol_elemental_shock = "GD_Weap_Pistol.elemental.Pistol_Elemental_Shock"
    pistol_elemental_slag = "GD_Weap_Pistol.elemental.Pistol_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Pistol_Barrel_B(StrEnum):
    pistol_barrel_bandit = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Bandit"
    pistol_barrel_dahl = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Dahl"
    pistol_barrel_hyperion = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Hyperion"
    pistol_barrel_jakobs = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Jakobs"
    pistol_barrel_maliwan = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Maliwan"
    pistol_barrel_tediore = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Tediore"
    pistol_barrel_torgue = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Torgue"
    pistol_barrel_vladof = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Vladof"

    _defdata_field = "BarrelPartDefinition"


class Pistol_Barrel_C(StrEnum):
    pistol_barrel_bandit = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Bandit"
    pistol_barrel_dahl = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Dahl"
    pistol_barrel_hyperion = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Hyperion"
    pistol_barrel_jakobs = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Jakobs"
    pistol_barrel_maliwan = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Maliwan"
    pistol_barrel_tediore = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Tediore"
    pistol_barrel_torgue = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Torgue"

    _defdata_field = "BarrelPartDefinition"


class Pistol_Sight_D(StrEnum):
    pistol_sight_bandit = "GD_Weap_Pistol.Sight.Pistol_Sight_Bandit"
    pistol_sight_dahl = "GD_Weap_Pistol.Sight.Pistol_Sight_Dahl"
    pistol_sight_hyperion = "GD_Weap_Pistol.Sight.Pistol_Sight_Hyperion"
    pistol_sight_jakobs = "GD_Weap_Pistol.Sight.Pistol_Sight_Jakobs"
    pistol_sight_maliwan = "GD_Weap_Pistol.Sight.Pistol_Sight_Maliwan"
    pistol_sight_none = "GD_Weap_Pistol.Sight.Pistol_Sight_None"
    pistol_sight_tediore = "GD_Weap_Pistol.Sight.Pistol_Sight_Tediore"
    pistol_sight_torgue = "GD_Weap_Pistol.Sight.Pistol_Sight_Torgue"

    _defdata_field = "SightPartDefinition"


class Pistol_Barrel_D(StrEnum):
    pistol_barrel_alien = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Alien"
    pistol_barrel_alien_homing = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Alien_Homing"
    pistol_barrel_bandit = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Bandit"
    pistol_barrel_dahl = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Dahl"
    pistol_barrel_hyperion = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Hyperion"
    pistol_barrel_jakobs = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Jakobs"
    pistol_barrel_maliwan = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Maliwan"
    pistol_barrel_tediore = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Tediore"
    pistol_barrel_torgue = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Torgue"
    pistol_barrel_vladof = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Vladof"

    _defdata_field = "BarrelPartDefinition"


class Pistol_Barrel_Alien(StrEnum):
    pistol_barrel_alien = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Alien"
    pistol_barrel_alien_homing = "GD_Weap_Pistol.Barrel.Pistol_Barrel_Alien_Homing"

    _defdata_field = "BarrelPartDefinition"


class Sg_Barrel_B(StrEnum):
    sg_barrel_bandit = "GD_Weap_Shotgun.Barrel.SG_Barrel_Bandit"
    sg_barrel_hyperion = "GD_Weap_Shotgun.Barrel.SG_Barrel_Hyperion"
    sg_barrel_jakobs = "GD_Weap_Shotgun.Barrel.SG_Barrel_Jakobs"
    sg_barrel_tediore = "GD_Weap_Shotgun.Barrel.SG_Barrel_Tediore"

    _defdata_field = "BarrelPartDefinition"


class Sg_Barrel_C(StrEnum):
    sg_barrel_bandit = "GD_Weap_Shotgun.Barrel.SG_Barrel_Bandit"
    sg_barrel_hyperion = "GD_Weap_Shotgun.Barrel.SG_Barrel_Hyperion"
    sg_barrel_jakobs = "GD_Weap_Shotgun.Barrel.SG_Barrel_Jakobs"
    sg_barrel_tediore = "GD_Weap_Shotgun.Barrel.SG_Barrel_Tediore"
    sg_barrel_torgue = "GD_Weap_Shotgun.Barrel.SG_Barrel_Torgue"

    _defdata_field = "BarrelPartDefinition"


class Shotgun_Elemental_B(StrEnum):
    shotgun_elemental_corrosive = "GD_Weap_Shotgun.elemental.Shotgun_Elemental_Corrosive"
    shotgun_elemental_fire = "GD_Weap_Shotgun.elemental.Shotgun_Elemental_Fire"
    shotgun_elemental_shock = "GD_Weap_Shotgun.elemental.Shotgun_Elemental_Shock"
    shotgun_elemental_slag = "GD_Weap_Shotgun.elemental.Shotgun_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Sg_Accessory_E(StrEnum):
    sg_accessory_bayonet_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Bayonet_2"
    sg_accessory_moonclip = "GD_Weap_Shotgun.Accessory.SG_Accessory_MoonClip"
    sg_accessory_shotgunshell = "GD_Weap_Shotgun.Accessory.SG_Accessory_ShotgunShell"
    sg_accessory_tech_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_1"
    sg_accessory_tech_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_2"
    sg_accessory_tech_3 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_3"

    _defdata_field = "Accessory1PartDefinition"


class Sg_Accessory_F(StrEnum):
    sg_accessory_bayonet_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Bayonet_1"
    sg_accessory_moonclip = "GD_Weap_Shotgun.Accessory.SG_Accessory_MoonClip"
    sg_accessory_shotgunshell = "GD_Weap_Shotgun.Accessory.SG_Accessory_ShotgunShell"
    sg_accessory_tech_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_1"
    sg_accessory_tech_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_2"
    sg_accessory_tech_3 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_3"

    _defdata_field = "Accessory1PartDefinition"


class Smg_Barrel_A(StrEnum):
    smg_barrel_bandit = "GD_Weap_SMG.Barrel.SMG_Barrel_Bandit"
    smg_barrel_maliwan = "GD_Weap_SMG.Barrel.SMG_Barrel_Maliwan"
    smg_barrel_tediore = "GD_Weap_SMG.Barrel.SMG_Barrel_Tediore"

    _defdata_field = "BarrelPartDefinition"


class Smg_Elemental_B(StrEnum):
    smg_elemental_corrosive = "GD_Weap_SMG.elemental.SMG_Elemental_Corrosive"
    smg_elemental_fire = "GD_Weap_SMG.elemental.SMG_Elemental_Fire"
    smg_elemental_shock = "GD_Weap_SMG.elemental.SMG_Elemental_Shock"
    smg_elemental_slag = "GD_Weap_SMG.elemental.SMG_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Smg_Barrel_B(StrEnum):
    smg_barrel_bandit = "GD_Weap_SMG.Barrel.SMG_Barrel_Bandit"
    smg_barrel_dahl = "GD_Weap_SMG.Barrel.SMG_Barrel_Dahl"
    smg_barrel_hyperion = "GD_Weap_SMG.Barrel.SMG_Barrel_Hyperion"
    smg_barrel_maliwan = "GD_Weap_SMG.Barrel.SMG_Barrel_Maliwan"
    smg_barrel_tediore = "GD_Weap_SMG.Barrel.SMG_Barrel_Tediore"

    _defdata_field = "BarrelPartDefinition"


class Smg_Body_Maliwan_Var(StrEnum):
    smg_body_maliwan_varb = "GD_Weap_SMG.Body.SMG_Body_Maliwan_VarB"
    smg_body_maliwan_varc = "GD_Weap_SMG.Body.SMG_Body_Maliwan_VarC"

    _defdata_field = "BodyPartDefinition"


class Smg_Accessory_E(StrEnum):
    smg_accessory_body1_accurate = "GD_Weap_SMG.Accessory.SMG_Accessory_Body1_Accurate"
    smg_accessory_body2_damage = "GD_Weap_SMG.Accessory.SMG_Accessory_Body2_Damage"
    smg_accessory_body3_accelerated = "GD_Weap_SMG.Accessory.SMG_Accessory_Body3_Accelerated"
    smg_accessory_stock1_stabilized = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock1_Stabilized"
    smg_accessory_stock2_reload = "GD_Weap_SMG.Accessory.SMG_Accessory_Stock2_Reload"

    _defdata_field = "Accessory1PartDefinition"


class Sr_Barrel(StrEnum):
    sr_barrel_dahl = "GD_Weap_SniperRifles.Barrel.SR_Barrel_Dahl"
    sr_barrel_hyperion = "GD_Weap_SniperRifles.Barrel.SR_Barrel_Hyperion"
    sr_barrel_jakobs = "GD_Weap_SniperRifles.Barrel.SR_Barrel_Jakobs"
    sr_barrel_maliwan = "GD_Weap_SniperRifles.Barrel.SR_Barrel_Maliwan"
    sr_barrel_vladof = "GD_Weap_SniperRifles.Barrel.SR_Barrel_Vladof"

    _defdata_field = "BarrelPartDefinition"


class Sr_Elemental_B(StrEnum):
    sr_elemental_corrosive = "GD_Weap_SniperRifles.elemental.SR_Elemental_Corrosive"
    sr_elemental_fire = "GD_Weap_SniperRifles.elemental.SR_Elemental_Fire"
    sr_elemental_shock = "GD_Weap_SniperRifles.elemental.SR_Elemental_Shock"
    sr_elemental_slag = "GD_Weap_SniperRifles.elemental.SR_Elemental_Slag"

    _defdata_field = "ElementalPartDefinition"


class Ar_Sight_C(StrEnum):
    ar_sight_none = "GD_Weap_AssaultRifle.Sight.AR_Sight_None"
    ar_sight_torgue = "GD_Weap_AssaultRifle.Sight.AR_Sight_Torgue"
    ar_sight_vladof = "GD_Weap_AssaultRifle.Sight.AR_Sight_Vladof"

    _defdata_field = "SightPartDefinition"


class Pistol_Barrel_Bandit_Fibber(StrEnum):
    pistol_barrel_bandit_fibber_1 = "GD_Weap_Pistol.Barrel.Fibber.Pistol_Barrel_Bandit_Fibber_1"
    pistol_barrel_bandit_fibber_2 = "GD_Weap_Pistol.Barrel.Fibber.Pistol_Barrel_Bandit_Fibber_2"
    pistol_barrel_bandit_fibber_3 = "GD_Weap_Pistol.Barrel.Fibber.Pistol_Barrel_Bandit_Fibber_3"

    _defdata_field = "BarrelPartDefinition"


class Rl_Accessory_C(StrEnum):
    rl_accessory_bodymod_1_mag = "GD_Weap_Launchers.Accessory.RL_Accessory_BodyMod_1_Mag"
    rl_accessory_bodymod_2_acc = "GD_Weap_Launchers.Accessory.RL_Accessory_BodyMod_2_Acc"
    rl_accessory_gripper_reload = "GD_Weap_Launchers.Accessory.RL_Accessory_Gripper_Reload"
    rl_accessory_handle_swapspeed = "GD_Weap_Launchers.Accessory.RL_Accessory_Handle_SwapSpeed"
    rl_accessory_none = "GD_Weap_Launchers.Accessory.RL_Accessory_None"
    rl_accessory_stocktube_firerate = "GD_Weap_Launchers.Accessory.RL_Accessory_StockTube_FireRate"
    rl_accessory_tipcover_damage = "GD_Weap_Launchers.Accessory.RL_Accessory_TipCover_Damage"

    _defdata_field = "Accessory1PartDefinition"


class Sg_Sight_C(StrEnum):
    sg_sight_hyperion = "GD_Weap_Shotgun.Sight.SG_Sight_Hyperion"
    sg_sight_jakobs = "GD_Weap_Shotgun.Sight.SG_Sight_Jakobs"
    sg_sight_torgue = "GD_Weap_Shotgun.Sight.SG_Sight_Torgue"

    _defdata_field = "SightPartDefinition"


class Sr_Stock_B(StrEnum):
    sr_stock_dahl = "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Dahl"
    sr_stock_hyperion = "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Hyperion"
    sr_stock_jakobs = "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Jakobs"
    sr_stock_maliwan = "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Maliwan"
    sr_stock_vladof = "GD_Anemone_Weap_SniperRifles.Stock.SR_Stock_Vladof"

    _defdata_field = "StockPartDefinition"


class Sg_Accessory_G(StrEnum):
    sg_accessory_bayonet_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Bayonet_2"
    sg_accessory_moonclip = "GD_Weap_Shotgun.Accessory.SG_Accessory_MoonClip"
    sg_accessory_shotgunshell = "GD_Weap_Shotgun.Accessory.SG_Accessory_ShotgunShell"
    sg_accessory_tech_1 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_1"
    sg_accessory_tech_2 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_2"
    sg_accessory_tech_3 = "GD_Weap_Shotgun.Accessory.SG_Accessory_Tech_3"
    sg_accessory_verticalgrip_carnage = "GD_Lobelia_Weapons.Shotguns.SG_Accessory_VerticalGrip_Carnage"

    _defdata_field = "Accessory1PartDefinition"


class Ar_Accessory_E(StrEnum):
    ar_accessory_banditclamp_damage = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Damage"
    ar_accessory_banditclamp_wild = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Wild"
    ar_accessory_box_bulletspeed = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Box_BulletSpeed"
    ar_accessory_foregrip_stability = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Foregrip_Stability"
    ar_accessory_none = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_None"
    ar_accessory_shroud1_magsize = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud1_MagSize"
    ar_accessory_shroud2_accuracy = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud2_Accuracy"

    _defdata_field = "Accessory1PartDefinition"


class Ar_Sight_D(StrEnum):
    ar_sight_dahl = "GD_Weap_AssaultRifle.Sight.AR_Sight_Dahl"
    ar_sight_none = "GD_Weap_AssaultRifle.Sight.AR_Sight_None"
    ar_sight_torgue = "GD_Weap_AssaultRifle.Sight.AR_Sight_Torgue"
    ar_sight_vladof = "GD_Weap_AssaultRifle.Sight.AR_Sight_Vladof"

    _defdata_field = "SightPartDefinition"


class Ar_Accessory_F(StrEnum):
    ar_accessory_banditclamp_damage = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Damage"
    ar_accessory_banditclamp_wild = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_BanditClamp_Wild"
    ar_accessory_bayonet_1 = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Bayonet_1"
    ar_accessory_foregrip_stability = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Foregrip_Stability"
    ar_accessory_none = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_None"
    ar_accessory_shroud1_magsize = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud1_MagSize"
    ar_accessory_shroud2_accuracy = "GD_Weap_AssaultRifle.Accessory.AR_Accessory_Shroud2_Accuracy"

    _defdata_field = "Accessory1PartDefinition"


