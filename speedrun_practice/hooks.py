from __future__ import annotations

from typing import TYPE_CHECKING

from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import RunCategory, get_pc, get_player_class, get_run_category
from unrealsdk.hooks import Block, Type, add_hook, remove_hook
from unrealsdk.unreal import BoundFunction

if TYPE_CHECKING:
    from bl2 import Actor, WillowGFxMovie, WillowPlayerController


class SPHooks:

    def enable(self, run_category: RunCategory):
        if run_category == RunCategory.AnyPercentGaige:
            add_hook("Engine.Actor:TriggerGlobalEventClass", Type.POST, "catapult", set_catapult_priority)
        add_hook("WillowGame.WillowGFxMovie:ShowAchievementsUI", Type.PRE, 'block_achievements', block_achievements)
        add_hook("WillowGame.WillowPlayerController:StartNewPlaySession", Type.POST, 'set_host_flag', set_host_flag)

    def disable(self):
        remove_hook("WillowGame.WillowGFxMovie:ShowAchievementsUI", Type.PRE, 'block_achievements')
        remove_hook("Engine.Actor:TriggerGlobalEventClass", Type.POST, "catapult")
        remove_hook("WillowGame.WillowPlayerController:StartNewPlaySession", Type.POST, 'set_host_flag')


def set_host_flag(obj: WillowPlayerController,
                  args: WillowPlayerController.StartNewPlaySession.args,
                  ret: WillowPlayerController.StartNewPlaySession.ret,
                  func: BoundFunction) -> None:
    from speedrun_practice import instance  # Avoid circular import
    kbs = instance.sp_keybinds
    options = instance.sp_options
    game_version = instance.game_version
    player_class = get_player_class(get_pc())
    run_category = get_run_category(game_version, player_class)

    kbs.host = obj.PlayerReplicationInfo.bIsPartyLeader
    kbs.disable()
    kbs.enable(game_version, player_class, run_category)

    options.host = obj.PlayerReplicationInfo.bIsPartyLeader
    options.disable()
    options.enable(game_version, run_category)


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
