from typing import TYPE_CHECKING, Any, cast

from mods_base import get_pc
from unrealsdk import find_object
from unrealsdk.hooks import Type, add_hook, prevent_hooking_direct_calls, remove_hook

if TYPE_CHECKING:
    from bl2 import InventoryBalanceDefinition, ItemPool


def spawn_item_from_balance(
    balance: "InventoryBalanceDefinition",
    game_stage: int,
) -> Any:
    """Spawn inventory from any ItemPoolDefinition."""
    default_item_pool = cast(
        "ItemPool",
        find_object("ItemPool", "WillowGame.Default__ItemPool"),
    )
    spawned_items: list[Any] = []

    def append_inv(
        obj: Any,
        *_: Any,
    ) -> None:
        spawned_items.append(obj)

    add_hook("WillowGame.WillowItem:OnCreate", Type.PRE, "append_inv", append_inv)  # type: ignore
    add_hook("WillowGame.WillowWeapon:OnCreate", Type.PRE, "append_inv", append_inv)  # type: ignore
    with prevent_hooking_direct_calls():
        default_item_pool.SpawnBalancedInventoryFromInventoryBalanceDefinition(
            balance,
            1,
            game_stage,
            game_stage,
            get_pc(),  # type: ignore
            [],
        )
    remove_hook("WillowGame.WillowItem:OnCreate", Type.PRE, "append_inv")
    remove_hook("WillowGame.WillowWeapon:OnCreate", Type.PRE, "append_inv")

    if len(spawned_items) == 1:
        return spawned_items[0]
    if len(spawned_items) > 1:
        raise ValueError("Got multiple items! Help! Debug!")
    print(f"Spawned 0 items for {balance.Name}")
    return None
