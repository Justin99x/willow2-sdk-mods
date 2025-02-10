from dataclasses import dataclass
from typing import Any, Mapping, Sequence

from mods_base import BoolOption, ButtonOption, DropdownOption, HiddenOption, SliderOption, SpinnerOption, ValueOption, get_pc
from save_options.reloader import register_module


def can_save() -> bool:
    pc = get_pc()
    if not pc:
        return False
    cached_save = pc.GetCachedSaveGame()
    if not cached_save or cached_save.SaveGameId == -1:
        return False
    return True

type JSON = Mapping[str, JSON] | Sequence[JSON] | str | int | float | bool | None

class SaveOptionMeta(type(ValueOption)):
    """
    Metaclass to create save option classes. All we're doing is enforcing that SaveOption is paired with a subclass
    of ValueOption.
    """

    def __init__(cls, name, bases, class_dict):
        super().__init__(name, bases, class_dict)

        # Ignore itself
        if cls is SaveOptionMeta:
            return

        # Ensure SaveOption comes before ValueOption in the inheritance, and that ValueOption is used.
        base_names = [base.__name__ for base in bases]
        if "SaveOption" in base_names:
            index_saveoption = base_names.index("SaveOption")

            if not any(issubclass(bases[i], ValueOption) for i in range(index_saveoption + 1, len(bases))):
                raise TypeError(f"Class {name} must inherit from {SaveOption.__name__} before {ValueOption.__name__}")

any_option_changed: bool = False


@dataclass
class SaveOption(metaclass=SaveOptionMeta):
    """
    Mixin class that will disguise the class as a button whenever there is no character save loaded

    ButtonOption implements only on_press and __call__ from BaseOption. We don't need the latter since
    it will be overridden by whatever ValueOption this is mixed with.
    Our version is going to implement a __getattribute__, with the intent that the __class__
    variable is whatever the main class is when it needs to be, and a ButtonOption when we can't save.

    Overriding __setattr__ from ValueOption so that we can set our var to tell if a value has been changed,
    which is then used to save the file when we leave the options menu.
    """


    def __setattr__(self, name: str, value: Any) -> None:
        """This calls the version from ValueOption due to Python's MRO. Our metaclass ensures that we're
        paired with ValueOption"""
        super().__setattr__(name, value)

        # We're editing this var to track if an option has changed since the last time the game was saved
        # Saving when the menu closes instead of on change of each item.
        global any_option_changed
        any_option_changed = True


    def __getattribute__(self, item):
        if can_save():
            return super().__getattribute__(item)
        if item == '__class__':
            return ButtonOption
        if item == 'description':
            return "Per save setting not available without a character loaded"
        if item == 'on_press':
            return None
        return super().__getattribute__(item)


@dataclass
class HiddenSaveOption(SaveOption, HiddenOption):
    """
    A generic save option which is always hidden. Use this to persist arbitrary (JSON-encodable) data
    in the character save file.

    This class is explicitly intended to be modified programmatically, unlike the other options
    which are generally only modified by the mod menu.

    Args:
        identifier: The option's identifier.
    Keyword Args:
        display_name: The option name to use for display. Defaults to copying the identifier.
        description: A short description about the option.
        description_title: The title of the description. Defaults to copying the display name.
    Extra Attributes:
        is_hidden: Always true.
        mod: The mod this option stores it's settings in, or None if not (yet) associated with one.
    """

    def save(self) -> None:
        """Base HiddenOption has a method to save mod settings. We don't want that functionality
        available for a class meant only to work with the save files."""
        raise NotImplementedError


@dataclass
class SliderSaveOption(SaveOption, SliderOption):
    """
    An option selecting a number within a range. Value is stored on a per save basis when using this
    instead of the mod's settings file.

    Args:
        identifier: The option's identifier.
        value: The option's value.
        min_value: The minimum value.
        max_value: The maximum value.
        step: How much the value should move each step of the slider.
        is_integer: If True, the value is treated as an integer.
    Keyword Args:
        display_name: The option name to use for display. Defaults to copying the identifier.
        description: A short description about the option.
        description_title: The title of the description. Defaults to copying the display name.
        is_hidden: If true, the option will not be shown in the options menu.
        on_change: If not None, a callback to run before updating the value. Passed a reference to
                   the option object and the new value. May be set using decorator syntax.
    Extra Attributes:
        mod: The mod this option stores it's settings in, or None if not (yet) associated with one.
        default_value: What the value was originally when registered. Does not update on change.
    """


@dataclass
class SpinnerSaveOption(SaveOption, SpinnerOption):
    """
    An option selecting one of a set of strings. Typically implemented as a spinner. Value is stored on
    a per save basis when using this instead of the mod's settings file.

    Also see DropDownSaveOption, which may be more suitable for larger numbers of choices.

    Args:
        identifier: The option's identifier.
        value: The option's value.
        choices: A list of choices for the value.
        wrap_enabled: If True, allows moving from the last choice back to the first, or vice versa.
    Keyword Args:
        display_name: The option name to use for display. Defaults to copying the identifier.
        description: A short description about the option.
        description_title: The title of the description. Defaults to copying the display name.
        is_hidden: If true, the option will not be shown in the options menu.
        on_change: If not None, a callback to run before updating the value. Passed a reference to
                   the option object and the new value. May be set using decorator syntax.
    Extra Attributes:
        mod: The mod this option stores it's settings in, or None if not (yet) associated with one.
        default_value: What the value was originally when registered. Does not update on change.
    """


@dataclass
class BoolSaveOption(SaveOption, BoolOption):
    """
    An option toggling a boolean value. Typically implemented as an "on/off" spinner. Value is stored on
    a per save basis when using this instead of the mod's settings file.

    Args:
        identifier: The option's identifier.
        value: The option's value.
        true_text: If not None, overwrites the default text used for the True option.
        false_text: If not None, overwrites the default text used for the False option.
    Keyword Args:
        display_name: The option name to use for display. Defaults to copying the identifier.
        description: A short description about the option.
        description_title: The title of the description. Defaults to copying the display name.
        is_hidden: If true, the option will not be shown in the options menu.
        on_change: If not None, a callback to run before updating the value. Passed a reference to
                   the option object and the new value. May be set using decorator syntax.
    Extra Attributes:
        mod: The mod this option stores it's settings in, or None if not (yet) associated with one.
        default_value: What the value was originally when registered. Does not update on change.
    """


register_module(__name__)
