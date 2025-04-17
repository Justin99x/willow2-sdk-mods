from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, cast

from unrealsdk import find_all, find_object, load_package
from unrealsdk.hooks import Type, add_hook, prevent_hooking_direct_calls, remove_hook

from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import feedback, get_pc

if TYPE_CHECKING:
    from collections.abc import Callable

    from bl2 import (
        AttributeDefinition,
        AttributeInitializationDefinition,
        ItemPool,
        ItemPoolDefinition,
        WillowPlayerReplicationInfo,
        WillowShield,
        WillowWeapon,
    )


MIN_AMP_DAMAGE = 100

@dataclass
class GearSource:
    map_req: str
    lvl_req: int
    gear_lvl: int
    farm: bool
    map_name: str
    item_pools: list[str]
    loot_variance: str | None = None
    qualifying_func: Callable[[WillowWeapon | WillowShield], bool] = lambda _: True
    sort_func: Callable[[WillowWeapon | WillowShield], float] = lambda _: 1


def is_jakobs_multi_barrel(inv: WillowWeapon | WillowShield) -> bool:
    """Determines if a weapon is a multi-barrel jakobs shotgun."""
    if inv.Class.Name != "WillowWeapon":  # type: ignore
        return False
    barrels = ["SG_Barrel_Bandit", "SG_Barrel_Jakobs", "SG_Barrel_Torgue"]
    return (
        inv.DefinitionData.WeaponTypeDefinition.Name == "WT_Jakobs_Shotgun"
        and inv.DefinitionData.BarrelPartDefinition.Name in barrels
    )


def is_probably_sanctuary_shotgun(inv: WillowWeapon | WillowShield) -> bool:
    """Returns true if a shotguns is likely the one received for a mission turn-in in Sanctuary."""
    if inv.Class.Name != "WillowWeapon":  # type: ignore
        return False
    return (
        inv.DefinitionData.WeaponTypeDefinition.WeaponType == 1
        and inv.DefinitionData.GameStage == 6  # noqa: PLR2004
    )


def get_total_damage(inv: WillowWeapon | WillowShield) -> float:
    """Get total shotgun damage including all projectiles."""
    if inv.Class.Name != "WillowWeapon":  # type: ignore
        return 0
    projectiles_attr = cast(
        "AttributeDefinition",
        find_object("AttributeDefinition", "D_Attributes.Weapon.WeaponProjectilesPerShot"),
    )
    projectiles = projectiles_attr.GetValue(inv)[0]
    return inv.InstantHitDamageBaseValue * projectiles


def is_white_turtle(inv: WillowWeapon | WillowShield) -> bool:
    """Determines if a shield is a white turtle shield."""
    if inv.Class.Name != "WillowShield":  # type: ignore
        return False
    return (
        inv.Class.Name == "WillowShield"  # type: ignore
        and inv.DefinitionData.BalanceDefinition.Name
        == "ItemGrade_Gear_Shield_Juggernaut_01_Common"
    )


def get_impact_damage(inv: WillowWeapon | WillowShield) -> float:
    """Get the damage value for an amp shield."""
    if inv.Class.Name != "WillowShield":  # type: ignore
        return 0
    impact_damage_attr = cast(
        "AttributeDefinition",
        find_object("AttributeDefinition", "D_Attributes.Shield.ImpactShield_DamageBonus"),
    )
    return impact_damage_attr.GetValue(inv)[0]


def is_good_amp(inv: WillowWeapon | WillowShield) -> bool:
    """Determines if an amp shield is worth keeping (or do we need to farm more)."""
    if inv.Class.Name != "WillowShield":  # type: ignore
        return False
    amp_damage = get_impact_damage(inv)
    return not (
        inv.Class.Name != "WillowShield"  # type: ignore
        or inv.DefinitionData.ManufacturerDefinition.Name != "Hyperion"
        or amp_damage < MIN_AMP_DAMAGE
    )


SHOTGUN_SOURCES = [
    GearSource(
        "Sanctuary",
        0,
        6,
        False,
        "Sanctuary",
        ["GD_Itempools.WeaponPools.Pool_Weapons_Shotguns_02_Uncommon"],
        None,
    ),
    GearSource(
        "Sanctuary",
        10,
        10,
        True,
        "Sanctuary",
        [
            "GD_ItemPools_Shop.Items.Shoppool_Weapons_FlatChance",
            "GD_ItemPools_Shop.WeaponPools.Shoppool_FeaturedItem_WeaponMachine",
        ],
        "GD_Economy.VendingMachine.Init_VendingMachine_LootGamestageVariance",
        is_jakobs_multi_barrel,
        get_total_damage,
    ),
    GearSource(
        "Grass_B",
        0,
        16,
        True,
        "Overlook",
        [
            "GD_ItemPools_Shop.Items.Shoppool_Weapons_FlatChance",
            "GD_ItemPools_Shop.WeaponPools.Shoppool_FeaturedItem_WeaponMachine",
        ],
        "GD_Economy.VendingMachine.Init_VendingMachine_LootGamestageVariance",
        is_jakobs_multi_barrel,
        get_total_damage,
    ),
]

SHIELD_SOURCES = [
    GearSource(
        "SouthernShelfTown",
        0,
        3,
        True,
        "Southern Shelf",
        ["GD_Itempools.ShieldPools.Pool_Shields_Standard_01_Common"],
    ),
    GearSource(
        "IceCanyon",
        0,
        8,
        True,
        "Frostburn",
        ["GD_ItemPools_Shop.HealthShop.HealthShop_Items"],
        None,
        is_white_turtle,
    ),
    GearSource(
        "Outwash",
        0,
        15,
        True,
        "The Fridge",
        [
            "GD_ItemPools_Shop.HealthShop.HealthShop_Items",
            "GD_ItemPools_Shop.HealthShop.HealthShop_FeaturedItem",
        ],
        "GD_Economy.VendingMachine.Init_VendingMachine_LootGamestageVariance",
        is_good_amp,
        get_impact_damage,
    ),
    GearSource(
        "Grass_C",
        0,
        18,
        False,
        "Hyperion Bridge",
        [
            "GD_ItemPools_Shop.HealthShop.HealthShop_Items",
            "GD_ItemPools_Shop.HealthShop.HealthShop_FeaturedItem",
        ],
        "GD_Economy.VendingMachine.Init_VendingMachine_LootGamestageVariance",
        is_good_amp,
        get_impact_damage,
    ),
    GearSource(
        "PandoraPark",
        0,
        19,
        False,
        "WEP",
        [
            "GD_ItemPools_Shop.HealthShop.HealthShop_Items",
            "GD_ItemPools_Shop.HealthShop.HealthShop_FeaturedItem",
        ],
        "GD_Economy.VendingMachine.Init_VendingMachine_LootGamestageVariance",
        is_good_amp,
        get_impact_damage,
    ),
    GearSource(
        "Cliffs",
        0,
        20,
        False,
        "Thousand Cuts",
        [
            "GD_ItemPools_Shop.HealthShop.HealthShop_Items",
            "GD_ItemPools_Shop.HealthShop.HealthShop_FeaturedItem",
        ],
        "GD_Economy.VendingMachine.Init_VendingMachine_LootGamestageVariance",
        is_good_amp,
        get_impact_damage,
    ),
]

LASCAUX_SOURCE = GearSource(
    "IceCanyon", 0, 8, True, "Frostburn", ["Env_IceCanyon.WeaponPools.Pool_Weapon_CaveGun"],
)


class GearRandomizer:
    def __init__(self) -> None:
        self.pc = get_pc()
        self.maps = self.pc.ActivatedTeleportersList
        pri = cast("WillowPlayerReplicationInfo", self.pc.PlayerReplicationInfo)
        self.level = pri.ExpLevel
        self.min_amp_damage = MIN_AMP_DAMAGE
        load_package("Sanctuary_P")  # Needed for maps that don't have gun vendors.
        self.game_stage_variance = cast(
            "AttributeInitializationDefinition",
            find_object(
                "AttributeInitializationDefinition",
                "GD_Economy.VendingMachine.Init_VendingMachine_LootGamestageVariance",
            ),
        )

    def get_items_from_pool(
        self,
        pool: ItemPoolDefinition,
        game_stage: int,
        game_stage_variance_def: AttributeInitializationDefinition | None = None,
    ) -> list[WillowWeapon | WillowShield]:
        """Spawn inventory from any ItemPoolDefinition."""
        default_item_pool = cast(
            "ItemPool", find_object("ItemPool", "WillowGame.Default__ItemPool"),
        )
        spawned_items: list[WillowWeapon | WillowShield] = []

        def append_inv(
            obj: WillowWeapon | WillowShield, *_: Any,
        ) -> None:
            spawned_items.append(obj)

        add_hook("WillowGame.WillowItem:OnCreate", Type.PRE, "append_inv", append_inv) # type: ignore
        add_hook("WillowGame.WillowWeapon:OnCreate", Type.PRE, "append_inv", append_inv) # type: ignore
        with prevent_hooking_direct_calls():
            default_item_pool.SpawnBalancedInventoryFromPool(
                pool, game_stage, game_stage, self.pc, [], game_stage_variance_def,
            )
        remove_hook("WillowGame.WillowItem:OnCreate", Type.PRE, "append_inv")
        remove_hook("WillowGame.WillowWeapon:OnCreate", Type.PRE, "append_inv")

        return spawned_items

    def get_game_stage(self, item: WillowShield | WillowWeapon) -> int:
        """Get game stage of inventory."""
        return item.DefinitionData.GameStage

    def spawn_from_gear_source(self, gear_source: GearSource) -> WillowWeapon | WillowShield | None:
        """Spawn an item from a GearSource instance."""
        if gear_source.loot_variance:
            game_stage_variance = cast(
                "AttributeInitializationDefinition",
                find_object("AttributeInitializationDefinition", gear_source.loot_variance),
            )
        else:
            game_stage_variance = None
        qualifying_items: list[WillowShield | WillowWeapon] = []

        for pool_str in gear_source.item_pools:
            pool = cast("ItemPoolDefinition", find_object("ItemPoolDefinition", pool_str))
            qualifying_items.extend(
                self.get_items_from_pool(pool, gear_source.gear_lvl, game_stage_variance),
            )
        qualifying_items = [item for item in qualifying_items if gear_source.qualifying_func(item)]
        if len(qualifying_items) > 0:
            return max(qualifying_items, key=gear_source.sort_func)
        if gear_source.farm:
            return self.spawn_from_gear_source(gear_source)
        return None

    def is_lascaux(self, weapon: WillowWeapon) -> bool:
        """Determines if the provided weapon is a Lascaux."""
        return (
            weapon.DefinitionData.BalanceDefinition
            == "GD_Weap_SMG.A_Weapons_Unique.SMG_Dahl_3_Lascaux"
        ) # type: ignore

    def throw_old_gear(self) -> None:
        """Tosses previous gear to the ground."""
        inventory_manager = self.pc.GetPawnInventoryManager()
        all_weapons = cast(list["WillowWeapon"], find_all("WillowWeapon"))
        for weapon in all_weapons:
            if weapon.Owner == self.pc.Pawn and (
                is_jakobs_multi_barrel(weapon)
                or is_probably_sanctuary_shotgun(weapon)
                or self.is_lascaux(weapon)
            ):
                if weapon in inventory_manager.GetEquippedWeapons(None, None, None, None):
                    self.pc.Pawn.TossInventory(weapon)
                else:
                    # TossInventory sometimes dupes backpack weapons, have to use this
                    inventory_manager.ThrowBackpackInventory(weapon)
        all_shields = cast(list["WillowShield"], find_all("WillowShield"))
        for shield in all_shields:
            if (
                shield.Owner == self.pc.Pawn
                and shield.DefinitionData.ManufacturerDefinition.Name in ["Pangolin", "Hyperion"]
            ):
                self.pc.Pawn.TossInventory(shield)

    def filter_gear(
        self, items: list[WillowWeapon | WillowShield | None],
    ) -> tuple[WillowWeapon | WillowShield | None, list[WillowWeapon | WillowShield]]:
        """
        Filters gear to only highest usable items plus any over-level gear.

        Returns:
            Tuple of an item to equip now and a list of overlevel items.
        """
        usable_items = [item for item in items if item and self.get_game_stage(item) <= self.level]
        overlevel_items = [
            item for item in items if item and self.get_game_stage(item) > self.level
        ]

        item_to_equip = None
        if usable_items:
            item_to_equip = max(usable_items, key=lambda x: self.get_game_stage(x))

        return item_to_equip, list(overlevel_items)

    def randomize_gear(self) -> None:
        """Randomize gear for current Any% Gaige player."""
        try:
            holding_shotgun = (
                self.pc.Pawn.Weapon.DefinitionData.WeaponTypeDefinition.WeaponType == 1
            )
        except:  # noqa: E722
            holding_shotgun = False

        try:
            holding_lascaux = self.is_lascaux(cast("WillowWeapon", self.pc.Pawn.Weapon))
        except:  # noqa: E722
            holding_lascaux = False

        shotguns = [
            self.spawn_from_gear_source(source)
            for source in SHOTGUN_SOURCES
            if source.map_req in self.maps and source.lvl_req <= self.level
        ]
        shields = [
            self.spawn_from_gear_source(source)
            for source in SHIELD_SOURCES
            if source.map_req in self.maps and source.lvl_req <= self.level
        ]
        lascaux = (
            self.spawn_from_gear_source(LASCAUX_SOURCE)
            if LASCAUX_SOURCE.map_req in self.maps and self.level < 10  # noqa: PLR2004
            else None
        )

        self.throw_old_gear()

        equip_shotgun, overlevel_shotguns = self.filter_gear(shotguns)
        equip_shield, overlevel_shields = self.filter_gear(shields)
        equip_lascaux, _ = self.filter_gear([lascaux])

        inv_manager = self.pc.GetPawnInventoryManager()
        if lascaux:
            inv_manager.AddInventory(equip_lascaux, holding_lascaux)
        if equip_shotgun:
            inv_manager.AddInventory(equip_shotgun, holding_shotgun)
        if equip_shield:
            inv_manager.AddInventory(equip_shield, True)
        for sg in overlevel_shotguns:
            inv_manager.AddInventory(sg, False)
        for sh in overlevel_shields:
            inv_manager.AddInventory(sh, False)

        feedback(
            self.pc.PlayerReplicationInfo,
            "Guns and shields randomized! Check backback for new gear.",
        )


register_module(__name__)
