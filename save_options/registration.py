from collections import defaultdict
from typing import Callable

from mods_base import Mod
from save_options.reloader import register_module
from save_options.options import SaveOption

ModSaveOptions = dict[str, SaveOption]
registered_save_options: defaultdict[str, ModSaveOptions] = defaultdict(dict)

SaveCallback = Callable[[], None]
save_callbacks: dict[str, SaveCallback] = {}

def register_save_options(mod: Mod, save_options: list[SaveOption] = None) -> None:
    """Store a reference to the option object by its mod name and its identifier."""
    mod_data = registered_save_options[mod.settings_file.stem]

    if save_options:
        for save_option in save_options:
            if isinstance(save_option, SaveOption):
                mod_data[save_option.identifier] = save_option
            else:
                print(f"Could not register {save_option.identifier} as save option. All save options must inherit from SaveOption.")


def register_save_callback(mod: Mod, callback: SaveCallback) -> None:
    """
    Registers a callback to run whenever the game is saved. The callback is run before the save
    game function is called, allowing for mods to update save data at that time.

    SaveCallbacks take no args.

    Args:
        mod: The instance of the mod
        callback: The callback to run before the game is saved.
    """
    if not mod.settings_file.stem:
        raise ValueError(f"Could not register save callback for {mod.name} due to missing settings_file attribute")
    save_callbacks[mod.settings_file.stem] = callback

register_module(__name__)
