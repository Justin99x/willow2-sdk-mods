from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

from ui_utils import clipboard_copy, clipboard_paste
from unrealsdk import find_enum
from unrealsdk.hooks import Block, Type, add_hook, remove_hook

from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import get_pc

if TYPE_CHECKING:
    from bl2 import Object, WillowGFxTrainingDialogBox, WillowPlayerController
    from unrealsdk.hooks import _PreHookCallback  # type: ignore

_SubmitKeys = (
    "Enter",
    "LeftMouseButton",
    "XboxTypeS_A",
    "XboxTypeS_Start",
)
_ExitKeys = (
    "Escape",
    "XboxTypeS_B",
)
_KeyMap = {
    # UnrealKeycode -> (ValueIfLower, ValueIfUpper)
    "Add": ("+", "+"),
    "Subtract": ("-", "-"),
    "Multiply": ("*", "*"),
    "Divide": ("/", "/"),
    "One": ("1", "!"),
    "Two": ("2", "@"),
    "Three": ("3", "#"),
    "Four": ("4", "$"),
    "Five": ("5", "%"),
    "Six": ("6", "^"),
    "Seven": ("7", "&amp;"),
    "Eight": ("8", "*"),
    "Nine": ("9", "("),
    "Zero": ("0", ")"),
    "NumPadOne": ("1", "1"),
    "NumPadTwo": ("2", "2"),
    "NumPadThree": ("3", "3"),
    "NumPadFour": ("4", "4"),
    "NumPadFive": ("5", "5"),
    "NumPadSix": ("6", "6"),
    "NumPadSeven": ("7", "7"),
    "NumPadEight": ("8", "8"),
    "NumPadNine": ("9", "9"),
    "NumPadZero": ("0", "0"),
    "Backslash": ("\\", "|"),
    "Comma": (",", "&lt;"),
    "Decimal": (".", "."),
    "Equals": ("=", "+"),
    "LeftBracket": ("[", "{"),
    "Period": (".", "&gt;"),
    "Quote": ("'", '"'),
    "RightBracket": ("]", "}"),
    "Semicolon": (";", ":"),
    "Slash": ("/", "?"),
    "SpaceBar": (" ", " "),
    "Tab": ("\t", "\t"),
    "Tilde": ("`", "~"),
    "Underscore": ("-", "_"),
}

e_back_button_screen = cast(
    "WillowPlayerController.EBackButtonScreen",
    find_enum("EBackButtonScreen"),
)
e_input_event = cast("Object.EInputEvent", find_enum("EInputEvent"))


class TextInputBoxSRP:
    def __init__(self, title: str) -> None:
        self.title = title
        self.message: list[str] = []
        self.cursor_pos: int = 0
        self.training_box: WillowGFxTrainingDialogBox | None = None
        self.is_shift_pressed: bool = False
        self.is_control_pressed: bool = False

    def show(self) -> None:
        """Show the text input box for user input."""
        self.pc: WillowPlayerController = get_pc()
        self.training_box = self.pc.GFxUIManager.ShowTrainingDialog(
            "".join(self.message),
            self.title,
            0,
            e_back_button_screen.CS_None,
            False,
        )
        add_hook(
            "WillowGame.WillowGFxTrainingDialogBox:HandleInputKey",
            Type.PRE,
            "handle_input_key",
            cast("_PreHookCallback", self.handle_input_key),
        )

    def handle_input_key(  # noqa: D102
        self,
        obj: WillowGFxTrainingDialogBox,
        args: WillowGFxTrainingDialogBox.HandleInputKey.args,
        *_: Any,
    ) -> type[Block] | None:
        self.update_message(args.ukey, args.uevent)

        if args.uevent == 1:
            if args.ukey in _SubmitKeys:
                remove_hook(
                    "WillowGame.WillowGFxTrainingDialogBox:HandleInputKey",
                    Type.PRE,
                    "handle_input_key",
                )
                self.on_submit("".join(self.message))

            elif args.ukey in _ExitKeys:
                remove_hook(
                    "WillowGame.WillowGFxTrainingDialogBox:HandleInputKey",
                    Type.PRE,
                    "handle_input_key",
                )
                self.on_submit("")

        use_key = "FAKE"
        if obj.GetPC().PlayerInput is not None:  # type: ignore Unreal properties can be null
            use_key = obj.GetPC().PlayerInput.GetKeyForAction("Use", True)
        if str(args.ukey) == use_key:
            return Block
        return None

    def update_message(self, ukey: str, event: Object.EInputEvent | int) -> None:  # noqa: C901
        """Updates the currently displayed message in the text box."""
        if ukey in ("LeftShift", "RightShift"):
            if event == 0:
                self.is_shift_pressed = True
            elif event == 1:
                self.is_shift_pressed = False
            return

        if ukey in ("LeftControl", "RightControl"):
            if event == 0:
                self.is_control_pressed = True
            elif event == 1:
                self.is_control_pressed = False
            return

        if event not in (0, 2):
            return

        if self.is_control_pressed:
            if ukey == "C":
                clipboard_copy("".join(self.message))
                return
            if ukey == "X":
                clipboard_copy("".join(self.message))
                self.message = []
                self.cursor_pos = 0
            elif ukey == "V":
                if not (clipboard := clipboard_paste()):
                    return
                clipboard = clipboard.replace("\r\n", "\n")
                for character in clipboard:
                    self.message.insert(self.cursor_pos, character)
                    self.cursor_pos += 1
            else:
                return

        if ukey == "Left":
            self.cursor_pos = max(self.cursor_pos - 1, 0)
        elif ukey == "Right":
            self.cursor_pos = min(self.cursor_pos + 1, len(self.message))
        elif ukey == "Home":
            self.cursor_pos = 0
        elif ukey == "End":
            self.cursor_pos = len(self.message)
        elif ukey == "BackSpace":
            if self.cursor_pos != 0:
                del self.message[self.cursor_pos - 1]
                self.cursor_pos -= 1
        elif ukey == "Delete":
            if self.cursor_pos != len(self.message):
                del self.message[self.cursor_pos]
        else:
            if ukey in _KeyMap:
                ukey = _KeyMap[ukey][self.is_shift_pressed]
            elif ukey in "QWERTYUIOPASDFGHJKLZXCVBNM":
                if not self.is_shift_pressed:
                    ukey = ukey.lower()
            else:
                return
            self.message.insert(self.cursor_pos, ukey)
            self.cursor_pos += 1

        message = [*list(self.message), "  "]
        message[self.cursor_pos] = "<u>" + message[self.cursor_pos] + "</u>"

        assert self.training_box is not None
        self.training_box.SetText(self.title, "".join(self.message))
        self.training_box.ApplyLayout()

    def on_submit(self, msg: str) -> None:
        """Logic that occurs once the message is submitted when user finishes."""
        raise NotImplementedError("Need to overwrite to determine what happens on submit.")


register_module(__name__)
