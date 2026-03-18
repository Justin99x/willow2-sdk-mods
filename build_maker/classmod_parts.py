from enum import StrEnum


class Spec(StrEnum):
    spec_as1 = "GD_ClassMods.Specialization.Spec_AS1"
    spec_as1_mbs2_cs3 = "GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3"
    spec_as1_bs2 = "GD_ClassMods.Specialization.Spec_AS1_BS2"
    spec_as1_bs2_mcs3 = "GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3"
    spec_as1_bs2_cs3 = "GD_ClassMods.Specialization.Spec_AS1_BS2_CS3"
    spec_as1_bs3 = "GD_ClassMods.Specialization.Spec_AS1_BS3"
    spec_as2 = "GD_ClassMods.Specialization.Spec_AS2"
    spec_as2_mbs1_cs3 = "GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3"
    spec_as2_bs1 = "GD_ClassMods.Specialization.Spec_AS2_BS1"
    spec_as2_bs1_mcs3 = "GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3"
    spec_as2_bs1_cs3 = "GD_ClassMods.Specialization.Spec_AS2_BS1_CS3"
    spec_as2_bs3 = "GD_ClassMods.Specialization.Spec_AS2_BS3"
    spec_as3 = "GD_ClassMods.Specialization.Spec_AS3"
    spec_as3_mbs1_cs2 = "GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2"
    spec_as3_bs1 = "GD_ClassMods.Specialization.Spec_AS3_BS1"
    spec_as3_bs1_mcs2 = "GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2"
    spec_as3_bs1_cs2 = "GD_ClassMods.Specialization.Spec_AS3_BS1_CS2"
    spec_as3_bs2 = "GD_ClassMods.Specialization.Spec_AS3_BS2"
    spec_noskill = "GD_ClassMods.Specialization.Spec_NoSkill"

    _defdata_field = "AlphaItemPartDefinition"


class Primarystat_A(StrEnum):
    primarystat_a0_b0_c0 = "GD_ClassMods.StatPrimary.PrimaryStat_A0_B0_C0"
    primarystat_a1_b0_c0 = "GD_ClassMods.StatPrimary.PrimaryStat_A1_B0_C0"
    primarystat_a2_b0_c0 = "GD_ClassMods.StatPrimary.PrimaryStat_A2_B0_C0"
    primarystat_a3_b0_c0 = "GD_ClassMods.StatPrimary.PrimaryStat_A3_B0_C0"
    primarystat_a4_b0_c0 = "GD_ClassMods.StatPrimary.PrimaryStat_A4_B0_C0"
    primarystat_a5_b0_c0 = "GD_ClassMods.StatPrimary.PrimaryStat_A5_B0_C0"

    _defdata_field = "BetaItemPartDefinition"


class Primarystat02_A0_B(StrEnum):
    primarystat02_a0_b0_c0 = "GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B0_C0"
    primarystat02_a0_b1_c0 = "GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B1_C0"
    primarystat02_a0_b2_c0 = "GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B2_C0"
    primarystat02_a0_b3_c0 = "GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B3_C0"
    primarystat02_a0_b4_c0 = "GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B4_C0"
    primarystat02_a0_b5_c0 = "GD_ClassMods.StatPrimary02.PrimaryStat02_A0_B5_C0"

    _defdata_field = "GammaItemPartDefinition"


class Statpenalty_A0_B0_C(StrEnum):
    statpenalty_a0_b0_c0 = "GD_ClassMods.StatPenalty.StatPenalty_A0_B0_C0"
    statpenalty_a0_b0_c1 = "GD_ClassMods.StatPenalty.StatPenalty_A0_B0_C1"
    statpenalty_a0_b0_c2 = "GD_ClassMods.StatPenalty.StatPenalty_A0_B0_C2"
    statpenalty_a0_b0_c3 = "GD_ClassMods.StatPenalty.StatPenalty_A0_B0_C3"
    statpenalty_a0_b0_c4 = "GD_ClassMods.StatPenalty.StatPenalty_A0_B0_C4"
    statpenalty_a0_b0_c5 = "GD_ClassMods.StatPenalty.StatPenalty_A0_B0_C5"

    _defdata_field = "MaterialItemPartDefinition"


class Spec_As_A(StrEnum):
    spec_as1 = "GD_ClassMods.Specialization.Spec_AS1"
    spec_as2 = "GD_ClassMods.Specialization.Spec_AS2"
    spec_as3 = "GD_ClassMods.Specialization.Spec_AS3"

    _defdata_field = "AlphaItemPartDefinition"


class Spec_As_B(StrEnum):
    spec_as1_bs2 = "GD_ClassMods.Specialization.Spec_AS1_BS2"
    spec_as1_bs3 = "GD_ClassMods.Specialization.Spec_AS1_BS3"
    spec_as2_bs1 = "GD_ClassMods.Specialization.Spec_AS2_BS1"
    spec_as2_bs3 = "GD_ClassMods.Specialization.Spec_AS2_BS3"
    spec_as3_bs1 = "GD_ClassMods.Specialization.Spec_AS3_BS1"
    spec_as3_bs2 = "GD_ClassMods.Specialization.Spec_AS3_BS2"

    _defdata_field = "AlphaItemPartDefinition"


class Spec_As_C(StrEnum):
    spec_as1_mbs2_cs3 = "GD_ClassMods.Specialization.Spec_AS1_-BS2_CS3"
    spec_as1_bs2_mcs3 = "GD_ClassMods.Specialization.Spec_AS1_BS2_-CS3"
    spec_as1_bs2_cs3 = "GD_ClassMods.Specialization.Spec_AS1_BS2_CS3"
    spec_as2_mbs1_cs3 = "GD_ClassMods.Specialization.Spec_AS2_-BS1_CS3"
    spec_as2_bs1_mcs3 = "GD_ClassMods.Specialization.Spec_AS2_BS1_-CS3"
    spec_as2_bs1_cs3 = "GD_ClassMods.Specialization.Spec_AS2_BS1_CS3"
    spec_as3_mbs1_cs2 = "GD_ClassMods.Specialization.Spec_AS3_-BS1_CS2"
    spec_as3_bs1_mcs2 = "GD_ClassMods.Specialization.Spec_AS3_BS1_-CS2"
    spec_as3_bs1_cs2 = "GD_ClassMods.Specialization.Spec_AS3_BS1_CS2"

    _defdata_field = "AlphaItemPartDefinition"


