from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, TYPE_CHECKING, cast

from speedrun_practice.reloader import register_module
from speedrun_practice.utilities import get_pc
from unrealsdk import construct_object, find_enum, find_object

if TYPE_CHECKING:
    from bl2 import AttributeModifier, DesignerAttributeDefinition, Inventory, Object, WillowPlayerController, SkillDefinition, \
    WillowPlayerReplicationInfo, WillowInventory, WillowEquipableItem, WillowWeapon


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
        # print(f"Set {skill_path_name.split('.')[-1]} stacks to {target_stacks} for {self.sender_pri.GetHumanReadableName()}")

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
