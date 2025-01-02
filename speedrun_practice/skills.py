from __future__ import annotations

from typing import Callable, List, Optional, TYPE_CHECKING, cast

from networking import host
from speedrun_practice.reloader import register_module
from speedrun_practice.text_input import TextInputBoxSRP
from speedrun_practice.utilities import get_pc, try_parse_int
from unrealsdk import find_enum, find_object

if TYPE_CHECKING:
    from bl2 import AttributeDefinition, DesignerAttributeDefinition, WillowPlayerController, SkillDefinition, PlayerReplicationInfo

""" notes for co-op
Everything in this file needs to be executed on the host. So that's a clear boundary. How do we make sure a client never calls this?
Basically these methods should only be called once we've crossed a network method boundary (even if host calls a host.message function).

The clients of this file are checkpoints and keybinds. Maybe all host request methods should go here too? And all functions become private?

another option would be put all these in a class that gets instantiated through a network method, so the sender pri becomes an instance
attribute. Basically the methods can't be used without an instance created by that.
"""


class HostSkillManager:
    """
    Class for which instances gets created through a network method. Only the host can run these functions.
    """

    def __init__(self, sender_pri: PlayerReplicationInfo):
        self.sender_pri = sender_pri
        self.sender_pc = cast("WillowPlayerController", self.sender_pri.Owner)
        self.pc = get_pc()
        self.skill_manager = self.pc.GetSkillManager()
        assert self.sender_pc is not None

    def get_skill_definition_stacks(self, skill_names: List[str]) -> List[SkillDefinition]:
        """Get SkillDefinition objects for active skills matching the name, plus make sure it matches sender PlayerID"""
        return [skill.Definition for skill in self.skill_manager.ActiveSkills if
                skill.Definition.Name in skill_names and self.sender_pri.PlayerID == skill.SkillInstigator.PlayerReplicationInfo.PlayerID]

    def add_skill_definition_instance(self, skill_path_name: str) -> None:
        """Create new activated instance of skill definition"""
        skill_def = cast("SkillDefinition", find_object('SkillDefinition', skill_path_name))
        self.skill_manager.ActivateSkill(self.sender_pc, skill_def)

    def remove_skill_definition_instance(self, skill_path_name: str) -> None:
        """Remove one instance of skill definition"""
        skill_stacks = self.get_skill_definition_stacks([skill_path_name.split('.')[-1]])
        if skill_stacks:
            self.skill_manager.DeactivateSkill(self.sender_pc, skill_stacks[0])

    def set_skill_stacks(self, target_stacks: int, skill_path_name: str) -> None:
        """Set stacks of skill to desired value"""
        current_stacks = len(self.get_skill_definition_stacks([skill_path_name.split('.')[-1]]))
        for i in range(current_stacks):
            self.remove_skill_definition_instance(skill_path_name)
        for i in range(target_stacks):
            self.add_skill_definition_instance(skill_path_name)
        print(f"Set {skill_path_name.split('.')[-1]} stacks to {target_stacks} for {self.sender_pri.GetHumanReadableName}")

    def trigger_kill_skills(self, pc: WillowPlayerController):
        e_instinct_skill_actions: WillowPlayerController.EInstinctSkillActions = find_enum("EInstinctSkillActions")
        pc.NotifyInstinctSkillAction(e_instinct_skill_actions.ISA_KilledEnemy)


    def get_attribute_value(self, attr_str: str) -> float:
        attribute_def = cast("AttributeDefinition", find_object("AttributeDefinition", attr_str))
        return attribute_def.GetValue(self.sender_pc)[0]  # SDK returns tuples for out params

    def get_designer_attribute_value(self, designer_attr_str: str):
        attribute_def: Optional[DesignerAttributeDefinition] = cast("DesignerAttributeDefinition",
                                                                    find_object("DesignerAttributeDefinition", designer_attr_str))
        return attribute_def.GetValue(self.sender_pc)[0]  # SDK returns tuples for out params

    def set_designer_attribute_value(self, target_value: int, designer_attr_str: str):
        attribute_def = cast("DesignerAttributeDefinition", find_object("DesignerAttributeDefinition", designer_attr_str))
        attribute_def.SetAttributeBaseValue(self.sender_pc, target_value)


@host.json_message
def set_stacks(<callback>, target_stacks, ):
    host_skill_manager = HostSkillManager(sender_pri=set_stacks.sender)
    # Could be
    host_skill_manager.set_skill_stacks(target_stacks, "GD_Tulip_DeathTrap.Skills.Skill_ShieldBoost_Player")
    # or
    host_skill_manager.set_designer_attribute_value(target_stacks, "GD_Tulip_Mechromancer_Skills.Misc.Att_Anarchy_NumberOfStacks")


def text_input_stacks(func: Callable[[WillowPlayerController, int, str], None], title: str, ref: str = '') -> None:
    """Handle input box creation for various actions"""
    input_box = TextInputBoxSRP(title)
    pc = get_pc()

    def on_submit(msg: str) -> None:
        if msg:
            target_val = try_parse_int(msg)
            if target_val >= 0:
                func(pc, target_val, ref)
            else:
                print("Value must be greater than 0")

    input_box.on_submit = on_submit
    input_box.show()


register_module(__name__)
