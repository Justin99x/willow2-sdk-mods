from __future__ import annotations

import save_options.hooks
from mods_base import Library, ModType, build_mod
from save_options.reloader import register_module
from save_options.registration import register_save_options, register_save_callback
from save_options.options import SaveOption, HiddenSaveOption, SliderSaveOption, SpinnerSaveOption, BoolSaveOption, DropdownSaveOption

__all__: tuple[str, ...] = (
    "register_save_options",
    "register_save_callback",
    "SaveOption",
    "HiddenSaveOption",
    "SliderSaveOption",
    "SpinnerSaveOption",
    "BoolSaveOption",
    "DropdownSaveOption"
)

"""
This library allows for any arbitrary JSON encodable data to be saved in the character's .sav file. 
You will manage the data that will be written to the save file by storing values in special 
SaveOption objects. These objects all inherit from ValueOption objects as defined in mods_base, but provide
some additional functionality:

- When no player save is available (main menu with no character), the options behave as button options, with a 
message showing that a player needs to be loaded.
- Values from the options will be saved to and loaded from the character save files. If the option is also registered
in the mod as a regular option (i.e., in Mod.options), the options will also save to the mod's settings file. These
values will be loaded for any character that has not had any values saved yet. If you don't want a save option 
to be stored in the mod settings file, make sure it is not added to Mod.options.

Once the SaveOptions are registered, they are used in two places:
1. A hook on WillowSaveGameManager:SaveGame, where the values from the save options are read and written 
to the save file. Optionally, a save callback may be registered that runs before the save file is written. You 
can use this callback to do any just-in-time updates of the save entries (e.g., get data from the WPC that you 
would like saved).
2. A hook on WillowSaveGameManager:EndLoadGame, where the data previously written to the save file is
parsed and applied to the registered save options. If you need a callback here, use the on_change field as defined
by mods_base options.

Additionally, there is a trigger that saves the game whenever we leave the options menu and ANY save option has 
changed. This keeps the save file up to date if a value is changed on the mod options menu. Otherwise the
value would be overwritten by the old value when we load into the game.

Example usage for saving anarchy stacks:
```
anarchy_save_option = HiddenSaveOption("anarchy", 0)
def update_anarchy():
    anarchy_save_option.value = get_anarchy_stacks()

register_save_options(mod, save_options=[anarchy_save_option])
register_save_callback(mod, update_anarchy)
```

"""

mod = build_mod(
    cls=Library,
    mod_type=ModType.Library
)

register_module(__name__)
