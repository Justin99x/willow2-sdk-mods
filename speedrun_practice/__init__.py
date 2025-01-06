from __future__ import annotations

from dataclasses import dataclass

from mods_base import CoopSupport, Mod, SETTINGS_DIR, register_mod
from mods_base.mod_factory import deregister_using_settings_file
from networking import add_network_functions
from speedrun_practice.hooks import SPHooks
from speedrun_practice.keybinds import SPKeybinds
from speedrun_practice.options import SPOptions
from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import GameVersion, PlayerClass, RunCategory, extract_user_save_path, get_game_version, \
    get_pc, get_player_class, get_run_category, feedback
from speedrun_practice.network_funcs import *
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

    def enable(self) -> None:
        """Called to enable the mod. Overwriting base version because I enable/disable keybinds depending on character"""
        if self.enabling_locked:
            return
        if self.is_enabled:
            return

        self.is_enabled = True

        # for keybind in self.keybinds:
        #     keybind.enable()
        for hook in self.hooks:
            hook.enable()
        for command in self.commands:
            command.enable()

        if self.on_enable is not None:
            self.on_enable()

        if self.auto_enable:
            self.save_settings()

    def disable(self, dont_update_setting: bool = False) -> None:
        """
        Called to disable the mod. Overwriting base version because I enable/disable keybinds depending on character
        """
        if self.enabling_locked:
            return
        if not self.is_enabled:
            return

        self.is_enabled = False

        # for keybind in self.keybinds:
        #     keybind.disable()
        for hook in self.hooks:
            hook.disable()
        for command in self.commands:
            command.disable()

        if self.on_disable is not None:
            self.on_disable()

        if self.auto_enable and not dont_update_setting:
            self.save_settings()

    def _on_enable(self) -> None:
        self.disable_all()
        player_class = get_player_class(get_pc())
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
        print(f"{NAME} disabled.")

    def load_character(self, obj: WillowPlayerController, args: WillowPlayerController.FinishSaveGameLoad.args,
                       ret: WillowPlayerController.FinishSaveGameLoad.ret, func: BoundFunction) -> None:
        if not args.SaveGame:
            return
        self.disable_all()
        player_class = PlayerClass.from_str(args.SaveGame.PlayerClassDefinition.Name)
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

add_network_functions(instance)

register_module(__name__)
