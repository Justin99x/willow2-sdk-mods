from __future__ import annotations

from typing import TYPE_CHECKING, Any

from mods_base import hook
from unrealsdk.hooks import Block

from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import get_pc

if TYPE_CHECKING:
    from bl2 import Actor
    from mods_base.hook import HookType, PreHookRet


@hook("Engine.Actor:TriggerGlobalEventClass")  # type: ignore
def set_catapult_priority(
    _1: Any,
    args: Actor.TriggerGlobalEventClass.args,
    *_: Any,
) -> PreHookRet:
    """When in later parts of game for Any% Gaige, set catapult as first priority."""
    if args.InEventClass.Name == "WillowSeqEvent_PlayerJoined":  # type: ignore
        pc = get_pc()
        if "PandoraPark" in pc.ActivatedTeleportersList:
            pc.ConsoleCommand(
                "set GD_Globals.VehicleSpawnStation.VSSUI_SawBladeTechnical PreferredOrdering 4",
            )
        else:
            pc.ConsoleCommand(
                "set GD_Globals.VehicleSpawnStation.VSSUI_SawBladeTechnical PreferredOrdering 0",
            )


@hook("WillowGame.WillowGFxMovie:ShowAchievementsUI")
def block_achievements(*_: Any) -> PreHookRet:
    """Block Achievements button from opening up Steam/Epic achievements tab."""
    return Block


hooks: list[HookType] = [set_catapult_priority, block_achievements]

register_module(__name__)
