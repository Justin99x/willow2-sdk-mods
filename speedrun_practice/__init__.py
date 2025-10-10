from __future__ import annotations

from typing import TYPE_CHECKING, Any

from mods_base import hook
from mods_base.mod_factory import build_mod
from networking import add_network_functions
from unrealsdk.hooks import Type

import speedrun_practice.hooks as srp_hooks
import speedrun_practice.keybinds as srp_keybinds
import speedrun_practice.options as srp_options
from speedrun_practice.network_funcs import *  # noqa: F403
from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import (
    GameVersion,
    PlayerClass,
    RunCategory,
    extract_user_save_path,
    get_game_version,
    get_pc,
    get_player_class,
    get_run_category,
)

if TYPE_CHECKING:
    from bl2 import WillowPlayerController

__version__: str
__version_info__: tuple[int, ...]

NAME = "Speedrun Practice"

game_version: GameVersion = get_game_version()
player_class: PlayerClass | None
run_category: RunCategory


def _on_enable() -> None:
    global player_class, run_category
    player_class = get_player_class(get_pc())
    if player_class:
        run_category = get_run_category(game_version, player_class)
    else:
        run_category = RunCategory.Unknown

    srp_options.handle_jakobs_auto(srp_options.jakobs_auto_fire, srp_options.jakobs_auto_fire.value)
    srp_options.handle_travel_portal(
        srp_options.travel_portal_disabled,
        srp_options.travel_portal_disabled.value,
    )
    if run_category != RunCategory.AnyPercentGaige:
        srp_hooks.set_catapult_priority.disable()  # type: ignore
    print(f"{NAME} enabled!")


def _on_disable() -> None:
    srp_options.handle_jakobs_auto(srp_options.jakobs_auto_fire, False)
    srp_options.handle_travel_portal(srp_options.travel_portal_disabled, False)
    print(f"{NAME} disabled.")


@hook("WillowGame.WillowPlayerController:FinishSaveGameLoad", Type.POST, immediately_enable=True)  # type: ignore
def load_character(  # noqa: D103
    _1: Any,
    args: WillowPlayerController.FinishSaveGameLoad.args,
    *_: Any,
) -> None:
    if not args.SaveGame:
        return
    global player_class, run_category
    player_class = PlayerClass.from_str(args.SaveGame.PlayerClassDefinition.Name)
    run_category = get_run_category(game_version, player_class)


mod_instance = build_mod(
    on_enable=_on_enable,
    on_disable=_on_disable,
    options=srp_options.options,
    keybinds=srp_keybinds.all_keybinds,
    hooks=srp_hooks.hooks,
)

add_network_functions(mod_instance)

# Will only happen one time
if srp_options.save_game_path.value == "":
    print("Attempting to find game saves folder...")
    save_path = extract_user_save_path()
    srp_options.save_game_path.value = extract_user_save_path()
    print(f"Successfully found game saves folder at {save_path}")

register_module(__name__)
