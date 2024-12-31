from __future__ import annotations

from typing import TYPE_CHECKING, cast

from mods_base import get_pc
from speedrun_practice.reloader import register_module
from ui_utils import clipboard_copy, clipboard_paste
from unrealsdk import find_enum
from unrealsdk.hooks import Block, Type, add_hook, remove_hook
from unrealsdk.unreal import BoundFunction

if TYPE_CHECKING:
    from bl2 import WillowPlayerController, WillowGFxTrainingDialogBox, Object

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
    # UnrealKeycode: (ValueIfLower, ValueIfUpper)
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
    "Quote": ("'", "\""),
    "RightBracket": ("]", "}"),
    "Semicolon": (";", ":"),
    "Slash": ("/", "?"),
    "SpaceBar": (" ", " "),
    "Tab": ("\t", "\t"),
    "Tilde": ("`", "~"),
    "Underscore": ("-", "_"),
}

EBackButtonScreen = cast("WillowPlayerController.EBackButtonScreen", find_enum("EBackButtonScreen"))
EInputEvent = cast("Object.EInputEvent", find_enum("EInputEvent"))


class TextInputBoxSRP:

    def __init__(self, title: str):
        self.title = title
        self.message = []
        self.cursor_pos = 0
        self.training_box = None
        self.is_shift_pressed = False
        self.is_control_pressed = False

    def show(self) -> None:
        self.pc: WillowPlayerController = get_pc()
        self.training_box = self.pc.GFxUIManager.ShowTrainingDialog(
            ''.join(self.message),
            self.title,
            0,
            EBackButtonScreen.CS_None,
            False
        )
        add_hook("WillowGame.WillowGFxTrainingDialogBox:HandleInputKey", Type.PRE, "handle_input_key", self.handle_input_key)

    def handle_input_key(self, obj: WillowGFxTrainingDialogBox, args: WillowGFxTrainingDialogBox.HandleInputKey.args,
                         ret: WillowGFxTrainingDialogBox.HandleInputKey.ret, func: BoundFunction):
        self.update_message(args.ukey, args.uevent)

        if args.uevent == 1:
            if args.ukey in _SubmitKeys:
                remove_hook("WillowGame.WillowGFxTrainingDialogBox:HandleInputKey", Type.PRE, "handle_input_key")
                self.on_submit("".join(self.message))

            elif args.ukey in _ExitKeys:
                remove_hook("WillowGame.WillowGFxTrainingDialogBox:HandleInputKey", Type.PRE, "handle_input_key")
                self.on_submit("")

        use_key = "FAKE"
        if obj.GetPC().PlayerInput is not None:
            use_key = obj.GetPC().PlayerInput.GetKeyForAction("Use", True)
        if str(args.ukey) == use_key:
            return Block

    def update_message(self, ukey: str, event: EInputEvent):
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
            elif ukey == "X":
                clipboard_copy("".join(self.message))
                self.message = []
                self.cursor_pos = 0
            elif ukey == "V":
                clipboard = clipboard_paste().replace("\r\n", "\n")
                if clipboard is None or clipboard == "":
                    return
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

        message = list(self.message) + ["  "]
        message[self.cursor_pos] = "<u>" + message[self.cursor_pos] + "</u>"

        self.training_box.SetText(self.title, ''.join(self.message))
        self.training_box.ApplyLayout()

    def on_submit(self, msg: str) -> None:
        raise NotImplementedError("Need to overwrite to determine what happens on submit.")


register_module(__name__)