import argparse
import copy
import importlib
import sys

from mods_base import command

import_order: dict[str, list[str]] = {}


def register_module(module_name: str) -> None:
    """Register current module on load to enable correctly ordered reloads."""
    base_module = module_name.split(".")[0]
    if not import_order.get(base_module):
        import_order[base_module] = []
    if module_name not in import_order[base_module]:
        import_order[base_module].append(module_name)


@command
def sfo(args: argparse.Namespace) -> None:  # noqa: ARG001
    """
    Utility to automatically reload modules in the correct order.

    Requires that they all implement register_module
    """

    mod_to_reload: str = "save_file_organizer"

    import_order_copy = copy.copy(import_order.get(mod_to_reload, []))
    import_order[mod_to_reload] = []
    for module_name in import_order_copy:
        module = sys.modules.get(module_name)
        if module:
            importlib.reload(module)
            print(f"Reloaded module {module_name}")


sfo.enable()
