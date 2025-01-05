from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional, TYPE_CHECKING, cast

from speedrun_practice.reloader import register_module
from speedrun_practice.text_input import TextInputBoxSRP
from speedrun_practice.utilities import get_pc, try_parse_int
from unrealsdk import construct_object, find_enum, find_object

if TYPE_CHECKING:
    from bl2 import AttributeModifier, DesignerAttributeDefinition, Object, WillowPlayerController, SkillDefinition, \
        WillowPlayerReplicationInfo


# class Modifier(defaultdict):
#     """Setting up a dict to store our MT_PreAdd and MT_Scale values. We can safely ignore MT_PostAdd because they don't get used
#     on the weapons we're interested in for mass duping. Doing it this way so I can directly access these values with the enum value for
#     EModifierType"""
#
#     def __init__(self, zero: float = 0, one: float = 0):
#         super().__init__(float)
#         self[0] = zero
#         self[1] = one

@dataclass
class Modifier:
    """We have to keep positive and negative scale values separate from each other."""
    scale_pos: float = 0
    scale_neg: float = 0
    pre_add: float = 0

    def add_modifier_value(self, attr_modifier: AttributeModifier) -> None:
        if attr_modifier.Type.value == 0:
            if attr_modifier.Value > 0:
                self.scale_pos += attr_modifier.Value
            elif attr_modifier.Value < 0:
                self.scale_neg += attr_modifier.Value
        elif attr_modifier.Type.value == 1:
            self.pre_add += attr_modifier.Value


@dataclass
class ExternalAttributeModifiers:
    MinValue: Modifier = field(default_factory=Modifier)
    MaxValue: Modifier = field(default_factory=Modifier)
    OnIdleRegenerationRate: Modifier = field(default_factory=Modifier)
    CurrentInstantHitCriticalHitBonus: Modifier = field(default_factory=Modifier)

    def msg(self):
        msg = f"\n\tCrit PreAdd: {self.CurrentInstantHitCriticalHitBonus.pre_add}"
        msg += f"\n\tCrit Scale: {self.CurrentInstantHitCriticalHitBonus.scale_pos}"
        return msg


class HostSkillManager:
    """
    Class for which instances gets created through a network method. Only the host can run these functions.
    """

    def __init__(self, sender_pri: WillowPlayerReplicationInfo):
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
        print(f"Set {skill_path_name.split('.')[-1]} stacks to {target_stacks} for {self.sender_pri.GetHumanReadableName()}")

    def trigger_kill_skills(self) -> None:
        e_instinct_skill_actions: WillowPlayerController.EInstinctSkillActions = find_enum("EInstinctSkillActions")
        self.sender_pc.NotifyInstinctSkillAction(e_instinct_skill_actions.ISA_KilledEnemy)

    def get_attribute_value(self, attr_str: str) -> float:
        attribute_def = cast("AttributeDefinition", find_object("AttributeDefinition", attr_str))
        return attribute_def.GetValue(self.sender_pc)[0]  # SDK returns tuples for out params

    def get_designer_attribute_value(self, designer_attr_str: str) -> float:
        attribute_def: Optional[DesignerAttributeDefinition] = cast("DesignerAttributeDefinition",
                                                                    find_object("DesignerAttributeDefinition", designer_attr_str))
        return attribute_def.GetValue(self.sender_pc)[0]  # SDK returns tuples for out params

    def set_designer_attribute_value(self, target_value: int, designer_attr_str: str) -> None:
        attribute_def = cast("DesignerAttributeDefinition", find_object("DesignerAttributeDefinition", designer_attr_str))
        attribute_def.SetAttributeBaseValue(self.sender_pc, target_value)

    def get_external_attribute_modifier_totals(self, include_srp: bool) -> ExternalAttributeModifiers:
        """Get values for each of accuracy min/max, idle regen rate, and crit bonus"""
        ext_mods = ExternalAttributeModifiers()
        equipped_weapons = cast(List["WillowWeapon"], self.sender_pc.GetPawnInventoryManager().GetEquippedWeapons(
            None, None, None, None)[1:])

        # We're going to exclude any modifiers that the PC's equipped weapons think are applied. We really only want orphaned modifiers.
        exclude_modifiers = []
        for weap in equipped_weapons:
            if weap:
                for applied_attribute_effect in weap.ExternalAttributeModifiers:
                    exclude_modifiers.append(applied_attribute_effect.Modifier)

        def sum_modifiers(stack: List[AttributeModifier], target: Modifier):
            for modifier in stack:
                if modifier.Type.value in [0, 1] and (include_srp or 'SRP_' not in modifier.Name) and modifier not in exclude_modifiers:
                    target.add_modifier_value(modifier)

        sum_modifiers(self.sender_pc.AccuracyPool.Data.MinValueModifierStack, ext_mods.MinValue)
        sum_modifiers(self.sender_pc.AccuracyPool.Data.MaxValueModifierStack, ext_mods.MaxValue)
        sum_modifiers(self.sender_pc.AccuracyPool.Data.OnIdleRegenerationRateModifierStack, ext_mods.OnIdleRegenerationRate)
        sum_modifiers(self.sender_pc.CurrentInstantHitCriticalHitBonusModifierStack, ext_mods.CurrentInstantHitCriticalHitBonus)
        return ext_mods

    def set_external_attribute_modifiers(self, target_modifiers: ExternalAttributeModifiers) -> None:
        """We have current modifier totals and target modifier totals. We're going to get the difference and add a modifier to the stack"""
        # Remove any existing modifiers that we put in
        current_modifiers = self.get_external_attribute_modifier_totals(False)

        def add_trueup_modifiers(target_obj: Object, attr_name: str) -> None:
            """Need two separate modifiers for scale pos and scale neg"""
            for modifier_type, type_name in [(0, 'scale_pos'), (0, 'scale_neg'), (1, 'pre_add')]:
                attr_modifier = cast("AttributeModifier",
                                      construct_object(cls="AttributeModifier", outer=self.sender_pc, name=f"SRP_{attr_name}_{type_name}"))
                attr_modifier.Type = modifier_type
                attr_modifier.Value = getattr(getattr(target_modifiers, attr_name), type_name) - getattr(getattr(current_modifiers, attr_name), type_name)
                if abs(attr_modifier.Value) > 0.0001:
                    target_obj.AddModifier(attr_modifier, attr_name)

        add_trueup_modifiers(self.sender_pc.AccuracyPool.Data, "MinValue")
        add_trueup_modifiers(self.sender_pc.AccuracyPool.Data, "MaxValue")
        add_trueup_modifiers(self.sender_pc.AccuracyPool.Data, "OnIdleRegenerationRate")
        add_trueup_modifiers(self.sender_pc, "CurrentInstantHitCriticalHitBonus")


def text_input_stacks(func: Callable[[int, str], None], title: str, path: str = '') -> None:
    """Handle input box creation for various actions"""
    input_box = TextInputBoxSRP(title)
    pc = get_pc()

    def on_submit(msg: str) -> None:
        if msg:
            target_val = try_parse_int(msg)
            if target_val >= 0:
                func(target_val, path)
            else:
                print("Value must be greater than 0")

    input_box.on_submit = on_submit
    input_box.show()


register_module(__name__)
