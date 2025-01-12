from __future__ import annotations

from typing import TYPE_CHECKING

from mods_base import hook
from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import RunCategory, get_pc, get_player_class, get_run_category
from unrealsdk.hooks import Block
from unrealsdk.unreal import BoundFunction
import speedrun_practice.options as srp_options
import speedrun_practice.keybinds as srp_keybinds

if TYPE_CHECKING:
    from bl2 import Actor, WillowGFxMovie, WillowPlayerController



def enable(run_category: RunCategory):
    if run_category == RunCategory.AnyPercentGaige:
        set_catapult_priority.enable()

    block_achievements.enable()
    # set_host_flag.enable()

def disable():
    set_catapult_priority.disable()
    block_achievements.disable()
    # set_host_flag.disable()





# @hook("WillowGame.WillowPlayerController:StartNewPlaySession")
# def set_host_flag(obj: WillowPlayerController,
#                   args: WillowPlayerController.StartNewPlaySession.args,
#                   ret: WillowPlayerController.StartNewPlaySession.ret,
#                   func: BoundFunction) -> None:
#     from speedrun_practice import game_version
#
#     player_class = get_player_class(get_pc())
#     run_category = get_run_category(game_version, player_class)

    # srp_keybinds.host = obj.PlayerReplicationInfo.bIsPartyLeader
    # srp_keybinds.disable()
    # srp_keybinds.enable(game_version, player_class, run_category)
    #
    # srp_options.host = obj.PlayerReplicationInfo.bIsPartyLeader
    # srp_options.disable()
    # srp_options.enable(game_version, run_category)

@hook("Engine.Actor:TriggerGlobalEventClass")
def set_catapult_priority(obj: Actor, args: Actor.TriggerGlobalEventClass.args, ret: Actor.TriggerGlobalEventClass.ret,
                          func: BoundFunction) -> None:
    """When in later parts of game for Any% Gaige, set catapult as first priority"""
    if args.InEventClass.Name == 'WillowSeqEvent_PlayerJoined':
        pc = get_pc()
        if 'PandoraPark' in pc.ActivatedTeleportersList:
            pc.ConsoleCommand(f"set GD_Globals.VehicleSpawnStation.VSSUI_SawBladeTechnical PreferredOrdering 4")
        else:
            pc.ConsoleCommand(f"set GD_Globals.VehicleSpawnStation.VSSUI_SawBladeTechnical PreferredOrdering 0")

@hook("WillowGame.WillowGFxMovie:ShowAchievementsUI")
def block_achievements(obj: WillowGFxMovie, args: WillowGFxMovie.ShowAchievementsUI.args, ret: WillowGFxMovie.ShowAchievementsUI.ret,
                       func: BoundFunction):
    return Block


register_module(__name__)
