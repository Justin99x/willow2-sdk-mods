from __future__ import annotations

from typing import TYPE_CHECKING

from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import RunCategory, get_pc
from unrealsdk.hooks import Block, Type, add_hook, remove_hook
from unrealsdk.unreal import BoundFunction

if TYPE_CHECKING:
    from bl2 import Actor, WillowGFxMovie


class SPHooks:

    def enable(self, run_category: RunCategory):
        if run_category == RunCategory.AnyPercentGaige:
            add_hook("Engine.Actor:TriggerGlobalEventClass", Type.POST, "catapult", set_catapult_priority)
        add_hook("WillowGame.WillowGFxMovie:ShowAchievementsUI", Type.PRE, 'block_achievements', block_achievements)

    def disable(self):
        remove_hook("WillowGame.WillowGFxMovie:ShowAchievementsUI", Type.PRE, 'block_achievements')
        remove_hook("Engine.Actor:TriggerGlobalEventClass", Type.POST, "catapult")


def set_catapult_priority(obj: Actor, args: Actor.TriggerGlobalEventClass.args, ret: Actor.TriggerGlobalEventClass.ret,
                          func: BoundFunction) -> None:
    """When in later parts of game for Any% Gaige, set catapult as first priority"""
    if args.InEventClass.Name == 'WillowSeqEvent_PlayerJoined':
        pc = get_pc()
        if 'PandoraPark' in pc.ActivatedTeleportersList:
            pc.ConsoleCommand(f"set GD_Globals.VehicleSpawnStation.VSSUI_SawBladeTechnical PreferredOrdering 4")
        else:
            pc.ConsoleCommand(f"set GD_Globals.VehicleSpawnStation.VSSUI_SawBladeTechnical PreferredOrdering 0")


def block_achievements(obj: WillowGFxMovie, args: WillowGFxMovie.ShowAchievementsUI.args, ret: WillowGFxMovie.ShowAchievementsUI.ret,
                       func: BoundFunction):
    return Block


register_module(__name__)
