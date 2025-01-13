from __future__ import annotations

import speedrun_practice.hooks as srp_hooks
import speedrun_practice.keybinds as srp_keybinds
import speedrun_practice.options as srp_options
from mods_base import hook
from mods_base.mod_factory import build_mod, deregister_using_settings_file
from networking import add_network_functions
from speedrun_practice.network_funcs import *
from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import GameVersion, PlayerClass, RunCategory, extract_user_save_path, feedback, get_game_version, get_pc, \
    get_player_class, get_run_category
from unrealsdk.hooks import Type
from unrealsdk.unreal import BoundFunction

if TYPE_CHECKING:
    from bl2 import WillowPlayerController

__version__: str
__version_info__: tuple[int, ...]

NAME = 'Speedrun Practice'

game_version: GameVersion = get_game_version()
player_class: PlayerClass
run_category: RunCategory



def _on_enable() -> None:
    global player_class, run_category
    player_class = get_player_class(get_pc())
    if player_class:
        run_category = get_run_category(game_version, player_class)
    else:
        pass  # No action because no character loaded. Hook on FinishSaveGameLoad will take care of the rest.
    print(f"{NAME} enabled!")

def _on_disable() -> None:
    print(f"{NAME} disabled.")


@hook("WillowGame.WillowPlayerController:FinishSaveGameLoad", Type.POST, immediately_enable=True)
def load_character(obj: WillowPlayerController, args: WillowPlayerController.FinishSaveGameLoad.args,
                   ret: WillowPlayerController.FinishSaveGameLoad.ret, func: BoundFunction) -> None:
    if not args.SaveGame:
        return
    global player_class, run_category
    player_class = PlayerClass.from_str(args.SaveGame.PlayerClassDefinition.Name)
    run_category = get_run_category(game_version, player_class)




deregister_using_settings_file('speedrun_practice')

mod_instance = build_mod(
    on_enable=_on_enable,
    on_disable=_on_disable,
    options=srp_options.options,
    keybinds=srp_keybinds.all_keybinds
)

add_network_functions(mod_instance)

# Will only happen one time
if srp_options.save_game_path.value == '':
    print('Attempting to find game saves folder...')
    save_path = extract_user_save_path()
    srp_options.save_game_path.value = extract_user_save_path()
    print(f'Successfully found game saves folder at {save_path}')

register_module(__name__)
