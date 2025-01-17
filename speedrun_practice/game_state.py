from __future__ import annotations

from dataclasses import dataclass, field, fields
from typing import TYPE_CHECKING, cast

from speedrun_practice.utilities import Position, get_pc
from speedrun_practice.reloader import register_module

if TYPE_CHECKING:
    from bl2 import AttributeModifier

SCALED_STATS = (
    "X", "Y", "Z", "Pitch", "Yaw", "a_min_sc_pos", "a_min_sc_neg", "a_min_pre", "a_max_sc_pos",
    "a_max_sc_neg", "a_max_pre", "a_idle_sc_pos", "a_idle_sc_neg",
    "a_idle_pre", "c_sc_pos", "c_sc_neg", 'c_pre', 'cooldown', 'gunzerk')
ROTATION_STATS = ("Pitch", "Yaw")
PLAYER_STATS_MAP = {
    "STAT_PLAYER_ZRESERVED_DLC_INT_BZ": "anarchy",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CA": "buckup",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CB": "freeshot",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CC": "weapons",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CD": "expertise",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CE": "smasher",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CF": "X",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CG": "Y",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CH": "Z",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CI": "Pitch",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CJ": "Yaw",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CK": "w1_clip",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CL": "w2_clip",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CM": "w3_clip",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CN": "w4_clip",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CO": "SMASH",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CP": "a_min_sc_pos",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CQ": "a_min_sc_neg",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CR": "a_min_pre",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CS": "a_max_sc_pos",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CT": "a_max_sc_neg",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CU": "a_max_pre",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CV": "a_idle_sc_pos",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CW": "a_idle_sc_neg",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CX": "a_idle_pre",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CY": "c_sc_pos",
    "STAT_PLAYER_ZRESERVED_DLC_INT_CZ": "c_sc_neg",
    "STAT_PLAYER_ZRESERVED_DLC_INT_DA": "c_pre",
    "STAT_PLAYER_ZRESERVED_DLC_INT_DB": "un_force",
    "STAT_PLAYER_ZRESERVED_DLC_INT_DC": "cooldown",
    "STAT_PLAYER_ZRESERVED_DLC_INT_DD": "gunzerk",
    "STAT_PLAYER_ZRESERVED_DLC_INT_DE": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DF": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DG": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DH": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DI": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DJ": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DK": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DL": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DM": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DN": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DO": None,
    "STAT_PLAYER_ZRESERVED_DLC_INT_DP": None,
}


@dataclass
class GradeStacks:
    """Skill stacks tracked by grade. Needed for Unstoppable Force Glitch.
    Not going past grade 5 since UF is only known current use, and we won't have a boosting class mod.
    DON'T CHANGE NAMING SCHEME. A FUNCTION USES field.name[1] TO GET THE GRADE"""
    G1: int = 0
    G2: int = 0
    G3: int = 0
    G4: int = 0
    G5: int = 0


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


@dataclass
class GameState:
    crit: float = 0  # Not needed for saving/loading, just for logging game state
    anarchy: int = 0
    buckup: int = 0
    freeshot: int = 0
    weapons: int = 0
    expertise: int = 0
    smasher: int = 0
    un_force: int = 0
    cooldown: float = 0
    gunzerk: float = 0  # 0 means not active
    X: float = 0
    Y: float = 0
    Z: float = 0
    Pitch: int = 0
    Yaw: int = 0
    w1_clip: int = 0
    w2_clip: int = 0
    w3_clip: int = 0
    w4_clip: int = 0
    SMASH: int = 0
    # Mass duping bonuses
    c_sc_pos: float = 0
    c_sc_neg: float = 0
    c_pre: float = 0
    a_min_sc_pos: float = 0
    a_min_sc_neg: float = 0
    a_min_pre: float = 0
    a_max_sc_pos: float = 0
    a_max_sc_neg: float = 0
    a_max_pre: float = 0
    a_idle_sc_pos: float = 0
    a_idle_sc_neg: float = 0
    a_idle_pre: float = 0

    def __str__(self):

        result = f"{self.__class__.__name__}:"
        for field in fields(self):
            # Exclude stuff we really don't care about logging
            if field.name not in ['weapons', 'X', 'Y', 'Z', 'Pitch', 'Yaw', 'w1_clip', 'w2_clip', 'w3_clip', 'w4_clip', 'un_force'] \
                    and field.name[:2] not in ('a_', 'c_'):
                value = getattr(self, field.name)
                if field.name == 'freeshot' and value == -1:
                    weap = cast("WillowWeapon", get_pc().GetActiveOrBestWeapon())
                    value = weap.ShotCostBaseValue
                result += f"\n  {field.name}: {value}"

        # Unstoppable force
        result += self.unstoppable_force_str()

        mass_result = "\n  Mass duping bonuses (off host):\n"
        mass_include = False
        # Mass duping stuff, include if any values > 0
        for field in fields(self):
            if field.name[:2] in ('a_', 'c_'):
                value = getattr(self, field.name)
                mass_result += f"    {field.name}: {value}\n"
                if abs(value) > .0001:
                    mass_include = True
        if mass_include:
            result += mass_result

        return result

    def unstoppable_force_str(self) -> str:
        result = ''
        if self.un_force > 0:
            result += "\nUF Stacks by Grade:"
            stacks = self.unstoppable_force
            for field in fields(self.unstoppable_force):
                result += f"\n  {field.name[1]}: {getattr(stacks, field.name)}"
        return result

    @property
    def unstoppable_force(self) -> GradeStacks:
        packed = self.un_force
        un_force = GradeStacks()
        un_force.G1 = (packed & 0b111111)
        un_force.G2 = (packed >> 6) & 0b111111
        un_force.G3 = (packed >> 12) & 0b111111
        un_force.G4 = (packed >> 18) & 0b111111
        un_force.G5 = (packed >> 24) & 0b111111
        return un_force

    @unstoppable_force.setter
    def unstoppable_force(self, uf_stacks: GradeStacks) -> None:
        for field in fields(uf_stacks):
            value = getattr(uf_stacks, field.name)
            if value > 63:
                setattr(uf_stacks, field.name, 63)
                print(f"Capping Unstoppable Force grade {field.name} at 63 stacks. Tried to set {value} stacks.")
        packed = (uf_stacks.G1 & 0b111111)
        packed |= (uf_stacks.G2 & 0b111111) << 6
        packed |= (uf_stacks.G3 & 0b111111) << 12
        packed |= (uf_stacks.G4 & 0b111111) << 18
        packed |= (uf_stacks.G5 & 0b111111) << 24
        self.un_force = packed

    @property
    def external_modifiers(self) -> ExternalAttributeModifiers:
        return ExternalAttributeModifiers(
            MinValue=Modifier(self.a_min_sc_pos, self.a_min_sc_neg, self.a_min_pre),
            MaxValue=Modifier(self.a_max_sc_pos, self.a_max_sc_neg, self.a_max_pre),
            OnIdleRegenerationRate=Modifier(self.a_idle_sc_pos, self.a_idle_sc_neg,
                                            self.a_idle_pre),
            CurrentInstantHitCriticalHitBonus=Modifier(self.c_sc_pos, self.c_sc_neg, self.c_pre)
        )

    @external_modifiers.setter
    def external_modifiers(self, ext_modifiers: ExternalAttributeModifiers) -> None:
        self.a_min_sc_pos = round(ext_modifiers.MinValue.scale_pos, 4)
        self.a_min_sc_neg = round(ext_modifiers.MinValue.scale_neg, 4)
        self.a_min_pre = round(ext_modifiers.MinValue.pre_add, 4)

        self.a_max_sc_pos = round(ext_modifiers.MaxValue.scale_pos, 4)
        self.a_max_sc_neg = round(ext_modifiers.MaxValue.scale_neg, 4)
        self.a_max_pre = round(ext_modifiers.MaxValue.pre_add, 4)

        self.a_idle_sc_pos = round(ext_modifiers.OnIdleRegenerationRate.scale_pos, 4)
        self.a_idle_sc_neg = round(ext_modifiers.OnIdleRegenerationRate.scale_neg, 4)
        self.a_idle_pre = round(ext_modifiers.OnIdleRegenerationRate.pre_add, 4)

        self.c_sc_pos = round(ext_modifiers.CurrentInstantHitCriticalHitBonus.scale_pos, 4)
        self.c_sc_neg = round(ext_modifiers.CurrentInstantHitCriticalHitBonus.scale_neg, 4)
        self.c_pre = round(ext_modifiers.CurrentInstantHitCriticalHitBonus.pre_add, 4)

    @property
    def position(self) -> Position:
        return Position(
            X=self.X,
            Y=self.Y,
            Z=self.Z,
            Pitch=self.Pitch,
            Yaw=self.Yaw,
        )

    @position.setter
    def position(self, input: Position) -> None:
        self.X = round(input.X, 4)
        self.Y = round(input.Y, 4)
        self.Z = round(input.Z, 4)
        self.Pitch = round(input.Pitch, 4)
        self.Yaw = round(input.Yaw, 4)

register_module(__name__)
