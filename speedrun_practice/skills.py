from __future__ import annotations

from dataclasses import fields
from typing import Any, List, Optional, TYPE_CHECKING, cast

from mods_base import hook
from speedrun_practice.game_state import ExternalAttributeModifiers, GradeStacks, Modifier

from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import feedback, get_pc
from unrealsdk import construct_object, find_enum, find_object, make_struct
from unrealsdk.hooks import Block, Type

if TYPE_CHECKING:
    from bl2 import AttributeModifier, DesignerAttributeDefinition, Inventory, Object, WillowPlayerController, SkillDefinition, \
    WillowPlayerReplicationInfo


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

    def get_skill_stacks_by_grade(self, skill_names: List[str]) -> GradeStacks:
        grade_stacks = GradeStacks()
        for skill in self.skill_manager.ActiveSkills:
            if skill.Definition.Name in skill_names:
                attr = f"G{skill.Grade}"
                setattr(grade_stacks, attr, getattr(grade_stacks, attr) + 1)
        return grade_stacks

    def add_skill_definition_instance(self, skill_path_name: str, grade: int | None = None) -> None:
        """Create new activated instance of skill definition. For unstoppable force, we need to block execution of
        RefreshSkillsForInstigator to keep the grades we saved."""
        try:
            skill_def = cast("SkillDefinition", find_object('SkillDefinition', skill_path_name))
        except ValueError:
            print(f"Could not add instance of {skill_path_name}. Is the right character loaded?")
            return
        is_player_skill, skill_state = self.pc.PlayerSkillTree.GetSkillState(skill_def, make_struct("SkillTreeSkillStateData"))
        if not grade:
            grade = 1 if not is_player_skill else skill_state.SkillGrade
        self.skill_manager.ActivateSkill(self.sender_pc, skill_def, None, grade)


    def remove_all_skill_definition_instances(self, skill_path_name: str) -> None:
        """Remove one instance of skill definition"""
        skill_stacks = self.get_skill_definition_stacks([skill_path_name.split('.')[-1]])
        if skill_stacks:
            for stack in skill_stacks:
                self.skill_manager.DeactivateSkill(self.sender_pc, stack)

    def set_skill_stacks(self, target_stacks: int, skill_path_name: str) -> None:
        """Set stacks of skill to desired value"""
        self.remove_all_skill_definition_instances(skill_path_name)
        if target_stacks > 1000:
            self.add_skill_definition_instance(skill_path_name, target_stacks)
            feedback(self.sender_pri, f"Target stacks > 1000, setting a single skill instance with grade of {target_stacks} to avoid crashing")
            return
        for i in range(target_stacks):
            self.add_skill_definition_instance(skill_path_name)

    def set_skill_stacks_by_grade(self, target_stacks: GradeStacks, skill_path_name: str):
        """Set stacks individually by grade. This is needed just for Unstoppable Force for now."""
        self.remove_all_skill_definition_instances(skill_path_name)
        for field in fields(target_stacks):
            grade = int(field.name[1])           # Seems dirty but I don't really want to specify each field
            for i in range(getattr(target_stacks, field.name)):
                self.add_skill_definition_instance(skill_path_name, grade)

    def trigger_kill_skills(self) -> None:
        e_instinct_skill_actions: WillowPlayerController.EInstinctSkillActions = find_enum("EInstinctSkillActions")
        self.sender_pc.NotifyInstinctSkillAction(e_instinct_skill_actions.ISA_KilledEnemy)

    def get_attribute_value(self, attr_str: str) -> float:
        try:
            attribute_def = cast("AttributeDefinition", find_object("AttributeDefinition", attr_str))
        except ValueError:
            print(f"Could not get attribute value for {attr_str}. Is the right character loaded?")
            return 0
        return attribute_def.GetValue(self.sender_pc)[0]  # SDK returns tuples for out params

    def get_designer_attribute_value(self, designer_attr_str: str) -> float:
        try:
            attribute_def: Optional[DesignerAttributeDefinition] = cast("DesignerAttributeDefinition",
                                                                    find_object("DesignerAttributeDefinition", designer_attr_str))
        except ValueError:
            print(f"Could not get attribute value for {designer_attr_str}. Is the right character loaded?")
            return 0
        return attribute_def.GetValue(self.sender_pc)[0]  # SDK returns tuples for out params

    def set_designer_attribute_value(self, target_value: int, designer_attr_str: str) -> None:
        try:
            attribute_def = cast("DesignerAttributeDefinition", find_object("DesignerAttributeDefinition", designer_attr_str))
        except ValueError:
            print(f"Could not set attribute value for {designer_attr_str}. Is the right character loaded?")
            return
        attribute_def.SetAttributeBaseValue(self.sender_pc, target_value)


    def get_external_attribute_modifier_totals(self, include_srp: bool) -> ExternalAttributeModifiers:
        """Get values for each of accuracy min/max, idle regen rate, and crit bonus"""
        ext_mods = ExternalAttributeModifiers()


        # We're going to exclude any modifiers that are applied from known sources (equipped inventory, active skills, and sprinting)
        # First grab objects we need to check
        equipped_inv: List[Inventory] = []
        inv_chain = self.sender_pc.GetPawnInventoryManager().InventoryChain
        while inv_chain:
            equipped_inv.append(inv_chain)
            inv_chain = inv_chain.Inventory
        item_chain = self.sender_pc.GetPawnInventoryManager().ItemChain
        while item_chain:
            equipped_inv.append(item_chain)
            item_chain = item_chain.Inventory
        active_skills = self.sender_pc.GetSkillManager().ActiveSkills

        # Create the list of modifiers to exclude
        exclude_modifiers: List[AttributeModifier] = []
        for inv in equipped_inv:
            if inv:
                for applied_attribute_effect in inv.ExternalAttributeModifiers:
                    exclude_modifiers.append(applied_attribute_effect.Modifier)
        for skill in active_skills:
            for applied_skill_effect in skill.SkillEffects:
                exclude_modifiers.append(applied_skill_effect.Modifier)
        for applied_attribute_effect in self.sender_pc.SprintModifiers:
            exclude_modifiers.append(applied_attribute_effect.Modifier)

        def sum_modifiers(stack: List[AttributeModifier], target: Modifier):
            for modifier in stack:
                if modifier.Type.value in [0, 1] and (include_srp or 'SRP_' not in modifier.Name) and modifier not in exclude_modifiers:
                    target.add_modifier_value(modifier)

        # Get all the "orphaned" modifiers. These are assumed to be due to mass duping.
        sum_modifiers(self.sender_pc.AccuracyPool.Data.MinValueModifierStack, ext_mods.MinValue)
        sum_modifiers(self.sender_pc.AccuracyPool.Data.MaxValueModifierStack, ext_mods.MaxValue)
        sum_modifiers(self.sender_pc.AccuracyPool.Data.OnIdleRegenerationRateModifierStack, ext_mods.OnIdleRegenerationRate)
        sum_modifiers(self.sender_pc.CurrentInstantHitCriticalHitBonusModifierStack, ext_mods.CurrentInstantHitCriticalHitBonus)
        return ext_mods

    def set_external_attribute_modifiers(self, target_modifiers: ExternalAttributeModifiers) -> None:
        """We have current modifier totals and target modifier totals. We're going to get the difference and add a modifier to the stack"""
        # current_modifiers = self.get_external_attribute_modifier_totals(False)

        def add_trueup_modifiers(target_obj: Object, attr_name: str) -> None:
            """Need two separate modifiers for scale pos and scale neg"""
            for modifier_type, type_name in [(0, 'scale_pos'), (0, 'scale_neg'), (1, 'pre_add')]:
                attr_modifier = cast("AttributeModifier",
                                      construct_object(cls="AttributeModifier", outer=self.sender_pc, name=f"SRP_{attr_name}_{type_name}"))
                attr_modifier.Type = modifier_type
                attr_modifier.Value = getattr(getattr(target_modifiers, attr_name), type_name)
                if abs(attr_modifier.Value) > 0.0001:
                    target_obj.AddModifier(attr_modifier, attr_name)

        add_trueup_modifiers(self.sender_pc.AccuracyPool.Data, "MinValue")
        add_trueup_modifiers(self.sender_pc.AccuracyPool.Data, "MaxValue")
        add_trueup_modifiers(self.sender_pc.AccuracyPool.Data, "OnIdleRegenerationRate")
        add_trueup_modifiers(self.sender_pc, "CurrentInstantHitCriticalHitBonus")


register_module(__name__)
