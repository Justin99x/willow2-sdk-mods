from __future__ import annotations

from typing import Callable, List, Optional, TYPE_CHECKING, cast

from speedrun_practice.reloader import register_module
from speedrun_practice.text_input import TextInputBoxSRP
from speedrun_practice.utilities import get_pc, try_parse_int
from unrealsdk import find_enum, find_object

if TYPE_CHECKING:
    from bl2 import AttributeDefinition, DesignerAttributeDefinition, WillowPlayerController, SkillDefinition


""" notes for co-op
Everything in this file needs to be executed on the host. So that's a clear boundary. How do we make sure a client never calls this?
Basically these methods should only be called once we've crossed a network method boundary (even if host calls a host.message function).

The clients of this file are checkpoints and keybinds. Maybe all host request methods should go here too? And all functions become private?

another option would be put all these in a class that gets instantiated through a network method, so the sender pri becomes an instance
attribute. Basically the methods can't be used without an instance created by that.
"""



def get_skill_stacks(pc: WillowPlayerController, skill_names: List[str]) -> List[SkillDefinition]:
    """Get SkillDefinition objects for active skills matching the name"""
    skill_manager = pc.GetSkillManager()
    return [skill.Definition for skill in skill_manager.ActiveSkills if
            skill.Definition.Name in skill_names]


def add_skill_definition_instance(pc: WillowPlayerController, skill_path_name: str) -> None:
    """Create new activated instance of skill definition"""
    skill_def = cast("SkillDefinition", find_object('SkillDefinition', skill_path_name))
    pc.GetSkillManager().ActivateSkill(pc, skill_def)


def remove_skill_definition_instance(pc: WillowPlayerController, skill_path_name: str) -> None:
    """Remove one instance of skill definition"""
    skill_stacks = get_skill_stacks(pc, [skill_path_name.split('.')[-1]])
    if skill_stacks:
        pc.GetSkillManager().DeactivateSkill(pc, skill_stacks[0])



def set_skill_stacks(pc: WillowPlayerController, target_stacks: int, skill_path_name: str) -> None:
    """Set stacks of skill to desired value"""
    current_stacks = len(get_skill_stacks(pc, [skill_path_name.split('.')[-1]]))
    for i in range(current_stacks):
        remove_skill_definition_instance(pc, skill_path_name)
    for i in range(target_stacks):
        add_skill_definition_instance(pc, skill_path_name)
    print(f"Set {skill_path_name.split('.')[-1]} stacks to {target_stacks}")


def get_attribute_value(pc: WillowPlayerController, attr_str: str) -> float:
    attribute_def = cast("AttributeDefinition", find_object("AttributeDefinition", attr_str))
    return attribute_def.GetValue(pc)[0]  # SDK returns tuples for out params


def get_designer_attribute_value(pc: WillowPlayerController, designer_attr_str: str):
    attribute_def: Optional[DesignerAttributeDefinition] = cast("DesignerAttributeDefinition",
                                                                find_object("DesignerAttributeDefinition", designer_attr_str))
    return attribute_def.GetValue(pc)[0]  # SDK returns tuples for out params


def set_designer_attribute_value(pc: WillowPlayerController, target_value: int, designer_attr_str: str):
    attribute_def = cast("DesignerAttributeDefinition", find_object("DesignerAttributeDefinition", designer_attr_str))
    attribute_def.SetAttributeBaseValue(pc, target_value)


def activate_skill(pc: WillowPlayerController, skill_def_str: str) -> None:
    skill_def = cast("SkillDefinition", find_object('SkillDefinition', skill_def_str))
    pc.Behavior_ActivateSkill(skill_def)


def trigger_kill_skills(pc: WillowPlayerController):
    e_instinct_skill_actions: WillowPlayerController.EInstinctSkillActions = find_enum("EInstinctSkillActions")
    pc.NotifyInstinctSkillAction(e_instinct_skill_actions.ISA_KilledEnemy)


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
