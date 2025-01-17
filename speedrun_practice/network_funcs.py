from __future__ import annotations

from dataclasses import asdict
from typing import Dict, TYPE_CHECKING, cast

from networking import host, targeted
from speedrun_practice.game_state import GameState
from speedrun_practice.options import save_game_path
from speedrun_practice.reloader import register_module
from speedrun_practice.checkpoints import CheckpointSaver, HostGameStateManager
from speedrun_practice.skills import HostSkillManager
from speedrun_practice.utilities import feedback, get_pc

if TYPE_CHECKING:
    pass



@targeted.json_message
def client_save_checkpoint(save_name: str, overwrite: bool, game_state_dict: Dict[str, int | float]) -> None:
    """Host now sends request back to client to complete the save and provides the requested information."""
    game_state = GameState(**game_state_dict)
    save_dir: str = save_game_path.value
    saver = CheckpointSaver(save_name, save_dir, game_state)
    saver.save_checkpoint(overwrite)
    feedback(get_pc().PlayerReplicationInfo, f"Saved checkpoint with name {save_name}. See console for details")
    print(game_state)



@host.json_message
def request_save_checkpoint(save_name: str, overwrite: bool) -> None:
    """Sending a request to host to get game state. Also sending requested save name, but this is only as a passthrough."""

    sender_pri = cast("WillowPlayerReplicationInfo", request_save_checkpoint.sender)
    host_game_state_manager = HostGameStateManager(sender_pri)
    game_state = host_game_state_manager.get_game_state()
    client_save_checkpoint(sender_pri, save_name, overwrite, asdict(game_state))


@host.json_message
def request_load_checkpoint(game_state_dict: Dict[str, int | float]) -> None:
    """Sending a request to host to load game state. No need for return trip here."""
    sender_pri = cast("WillowPlayerReplicationInfo", request_load_checkpoint.sender)
    game_state = GameState(**game_state_dict)
    host_game_state_manager = HostGameStateManager(sender_pri)
    host_game_state_manager.load_game_state(game_state)
    game_state.crit = round(host_game_state_manager.target_pc.CurrentInstantHitCriticalHitBonus, 2) # For info only
    client_log_game_state(sender_pri, asdict(game_state))


@targeted.json_message
def client_log_game_state(game_state_dict: Dict[str, int|float]) -> None:
    """Request back to client to log the game state to console."""
    game_state = GameState(**game_state_dict)
    print(game_state)


@host.message
def request_game_state() -> None:
    """Sending a request to host to send back a game state for logging to console"""
    sender_pri = cast("WillowPlayerReplicationInfo", request_game_state.sender)
    host_game_state_manager = HostGameStateManager(sender_pri)
    game_state = host_game_state_manager.get_game_state()
    client_log_game_state(sender_pri, asdict(game_state))


@host.json_message
def request_set_skill_stacks(target_stacks: int, skill_path: str) -> None:
    host_skill_manager = HostSkillManager(sender_pri=request_set_skill_stacks.sender)
    host_skill_manager.set_skill_stacks(target_stacks, skill_path)


@host.json_message
def request_set_designer_attribute_value(target_stacks: int, skill_path: str) -> None:
    host_skill_manager = HostSkillManager(sender_pri=request_set_designer_attribute_value.sender)
    host_skill_manager.set_designer_attribute_value(target_stacks, skill_path)


@host.message
def request_trigger_kill_skills() -> None:
    host_skill_manager = HostSkillManager(sender_pri=request_trigger_kill_skills.sender)
    host_skill_manager.trigger_kill_skills()


# Don't think I need this?
# @host.message
# def request_get_designer_attribute_value(designer_attr_str: str) -> None:
#     host_skill_manager = HostSkillManager(sender_pri=request_get_designer_attribute_value.sender)
#     value = host_skill_manager.get_designer_attribute_value(designer_attr_str)


register_module(__name__)