from __future__ import annotations

from dataclasses import asdict
from typing import TYPE_CHECKING, Any, cast

from networking import host, targeted

from speedrun_practice.checkpoints import CheckpointSaver, HostGameStateManager
from speedrun_practice.game_state import GameState
from speedrun_practice.options import save_game_path
from speedrun_practice.reloader import register_module
from speedrun_practice.skills import HostSkillManager
from speedrun_practice.utilities import feedback, get_pc

if TYPE_CHECKING:
    from bl2 import WillowPlayerReplicationInfo


@targeted.json_message
def client_save_checkpoint(
    save_name: str,
    overwrite: bool,
    game_state_dict: dict[str, Any],
) -> None:
    """Send message to client to trigger save of game state info."""
    game_state = GameState(**game_state_dict)
    save_dir: str = save_game_path.value
    saver = CheckpointSaver(save_name, save_dir, game_state)
    saver.save_checkpoint(overwrite)
    feedback(
        get_pc().PlayerReplicationInfo,
        f"Saved checkpoint with name {save_name}. See console for details",
    )
    print(game_state)


@host.json_message
def request_save_checkpoint(save_name: str, overwrite: bool) -> None:
    """Request a checkpoint save from host."""
    sender_pri = cast("WillowPlayerReplicationInfo", request_save_checkpoint.sender)
    host_game_state_manager = HostGameStateManager(sender_pri)
    game_state = host_game_state_manager.get_game_state()
    client_save_checkpoint(sender_pri, save_name, overwrite, asdict(game_state))


@host.json_message
def request_load_checkpoint(game_state_dict: dict[str, Any]) -> None:
    """Request a load checkpoint from host."""
    sender_pri = cast("WillowPlayerReplicationInfo", request_load_checkpoint.sender)
    game_state = GameState(**game_state_dict)
    host_game_state_manager = HostGameStateManager(sender_pri)
    host_game_state_manager.load_game_state(game_state)
    game_state.crit = round(
        host_game_state_manager.target_pc.CurrentInstantHitCriticalHitBonus,
        2,
    )  # For info only
    client_log_game_state(sender_pri, asdict(game_state))


@targeted.json_message
def client_log_game_state(game_state_dict: dict[str, Any]) -> None:
    """Request client log game state."""
    game_state = GameState(**game_state_dict)
    print(game_state)


@host.message
def request_game_state() -> None:
    """Request host send back a game state for logging to console."""
    sender_pri = cast("WillowPlayerReplicationInfo", request_game_state.sender)
    host_game_state_manager = HostGameStateManager(sender_pri)
    game_state = host_game_state_manager.get_game_state()
    client_log_game_state(sender_pri, asdict(game_state))


@host.json_message
def request_set_skill_stacks(target_stacks: int, skill_path: str) -> None:
    """Request host set skill stacks to a given value."""
    host_skill_manager = HostSkillManager(
        sender_pri=cast("WillowPlayerReplicationInfo", request_set_skill_stacks.sender),
    )
    host_skill_manager.set_skill_stacks(target_stacks, skill_path)


@host.json_message
def request_set_designer_attribute_value(target_stacks: int, skill_path: str) -> None:
    """Request host set designer attribute value for player."""
    host_skill_manager = HostSkillManager(
        sender_pri=cast("WillowPlayerReplicationInfo", request_set_designer_attribute_value.sender),
    )
    host_skill_manager.set_designer_attribute_value(target_stacks, skill_path)


@host.message
def request_trigger_kill_skills() -> None:
    """Request host trigger kill skills for player."""
    host_skill_manager = HostSkillManager(
        sender_pri=cast("WillowPlayerReplicationInfo", request_trigger_kill_skills.sender),
    )
    host_skill_manager.trigger_kill_skills()


register_module(__name__)
