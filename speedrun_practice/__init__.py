from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from mods_base import CoopSupport, Mod, SETTINGS_DIR, register_mod
from mods_base.mod_factory import deregister_using_settings_file
from speedrun_practice.hooks import SPHooks
from speedrun_practice.keybinds import SPKeybinds
from speedrun_practice.options import SPOptions
from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import GameVersion, PlayerClass, RunCategory, enum_from_value, extract_user_save_path, get_game_version, \
    get_pc, get_player_class, get_run_category
from unrealsdk.hooks import Type, add_hook, remove_hook
from unrealsdk.unreal import BoundFunction
from willow2_mod_menu.data_providers.mod_options import ModOptionsDataProvider
from willow2_mod_menu.options_menu import data_provider_stack, push_mod_options


if TYPE_CHECKING:
    from bl2 import WillowPlayerController, WillowScrollingListDataProviderOptionsBase

__version__: str
__version_info__: tuple[int, ...]

NAME = 'Speedrun Practice'


@dataclass
class SpeedrunPractice(Mod):

    def __post_init__(self):
        self.game_version: GameVersion = get_game_version()
        self.sp_options: SPOptions = SPOptions()
        self.sp_options.register_main_mod(self)

        self.sp_hooks: SPHooks = SPHooks()
        self.sp_keybinds: SPKeybinds = SPKeybinds(self.sp_options)
        self.on_enable = self._on_enable
        self.on_disable = self._on_disable
        self.name = NAME
        self.options = self.sp_options.options
        self.keybinds = self.sp_keybinds.keybinds

        # Implemented my own logic to refresh options menu on change
        remove_hook("WillowGame.WillowScrollingListDataProviderOptionsBase:HandleSpinnerChange",
                    Type.POST_UNCONDITIONAL,
                    self.name)
        add_hook(  # type: ignore
            "WillowGame.WillowScrollingListDataProviderOptionsBase:HandleSpinnerChange",
            Type.POST_UNCONDITIONAL,
            self.name,
            self.handle_spinner_change)

        super().__post_init__()


    def enable_all(self, game_version: GameVersion, player_class: PlayerClass, run_category: RunCategory) -> None:
        self.sp_options.enable(game_version, run_category)
        self.sp_hooks.enable(run_category)
        self.sp_keybinds.enable(game_version, player_class, run_category)

    def disable_all(self):
        self.sp_options.disable()
        self.sp_hooks.disable()
        self.sp_keybinds.disable()

    def _on_enable(self) -> None:
        self.disable_all()
        player_class = get_player_class()
        if player_class:
            run_category = get_run_category(self.game_version, player_class)
            self.enable_all(self.game_version, player_class, run_category)
        else:
            pass  # No action because no character loaded. Hook on FinishSaveGameLoad will take care of the rest.

        add_hook(  # type: ignore
            "WillowGame.WillowPlayerController:FinishSaveGameLoad",
            Type.POST,
            self.name,
            self.load_character)

        # One time only - need to find user save path and store it as a hidden option
        if self.sp_options.save_game_path.value == '':
            print('Attempting to find game saves folder...')
            save_path = extract_user_save_path()
            self.sp_options.save_game_path.value = save_path
            print(f'Successfully found game saves folder at {save_path}')
        print(f"{NAME} enabled!")

    def _on_disable(self) -> None:
        self.disable_all()
        remove_hook("WillowGame.WillowPlayerController:FinishSaveGameLoad", Type.POST, self.name)
        print("SRP disabled :(")

    def load_character(self, obj: WillowPlayerController, args: WillowPlayerController.FinishSaveGameLoad.args,
                       ret: WillowPlayerController.FinishSaveGameLoad.ret, func: BoundFunction) -> None:
        if not args.SaveGame:
            return
        self.disable_all()
        player_class = get_player_class()
        run_category = get_run_category(self.game_version, player_class)
        self.enable_all(self.game_version, player_class, run_category)

    def handle_spinner_change(self, obj: WillowScrollingListDataProviderOptionsBase,
                              args: WillowScrollingListDataProviderOptionsBase.HandleSpinnerChange.args, ret, func):
        """Essentially redrawing the current menu whenever a spinner is changed - covers enabling and setting category of the mod."""
        global data_provider_stack
        if len(data_provider_stack) == 0:
            return
        current_data_provider = data_provider_stack[-1]
        if type(current_data_provider) == ModOptionsDataProvider and current_data_provider.mod is self:
            idx = args.TheList.GetSelectedIndex()
            data_provider_stack.pop(-1)
            args.TheList.DataProviderStack.pop(-1)
            push_mod_options(args.TheList, self)
            args.TheList.SetSelectedIndex(idx)


description = """
Utility mod for practicing speedruns
 
Options and keybinds are available depending on the current version of the game and the player class loaded. If you don't see an option or \
keybind you are expecting, try loading a different character or changing to a different version of the game.
"""


instance = SpeedrunPractice(
    name=NAME,
    settings_file=SETTINGS_DIR / (__package__ + ".json"),
    author="Justin99",
    description=description,
    coop_support=CoopSupport.Incompatible,
    version='2.0'
)

deregister_using_settings_file(instance.settings_file)
register_mod(instance)

register_module(__name__)
