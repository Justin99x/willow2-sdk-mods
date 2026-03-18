"""Slot definitions for all inventory types."""

from dataclasses import dataclass
from enum import Enum


@dataclass(frozen=True)
class SlotInfo:
    """Describes a part slot and how to access it."""

    # For reading from PartListCollection: e.g., "BodyPartData", "AlphaPartData"
    part_list_field: str
    # For writing to DefinitionData: e.g., "BodyPartDefinition", "AlphaItemPartDefinition"
    defdata_field: str
    # For items: "Alpha", "Beta", etc. Used for InventoryDefinition lookup. None for weapons.
    greek: str | None = None

    @property
    def inv_def_field(self) -> str | None:
        """Field name on InventoryDefinition, e.g., 'Alpha' -> 'AlphaParts'. None for weapons."""
        if self.greek is None:
            return None
        return f"{self.greek}Parts"


class WeaponSlot(Enum):
    """Weapon part slots."""

    body = SlotInfo("BodyPartData", "BodyPartDefinition")
    grip = SlotInfo("GripPartData", "GripPartDefinition")
    barrel = SlotInfo("BarrelPartData", "BarrelPartDefinition")
    sight = SlotInfo("SightPartData", "SightPartDefinition")
    stock = SlotInfo("StockPartData", "StockPartDefinition")
    element = SlotInfo("ElementalPartData", "ElementalPartDefinition")
    accessory1 = SlotInfo("Accessory1PartData", "Accessory1PartDefinition")
    accessory2 = SlotInfo("Accessory2PartData", "Accessory2PartDefinition")
    material = SlotInfo("MaterialPartData", "MaterialPartDefinition")


class ShieldSlot(Enum):
    """Shield part slots."""

    body = SlotInfo("AlphaPartData", "AlphaItemPartDefinition", "Alpha")
    battery = SlotInfo("BetaPartData", "BetaItemPartDefinition", "Beta")
    capacitor = SlotInfo("GammaPartData", "GammaItemPartDefinition", "Gamma")
    accessory = SlotInfo("DeltaPartData", "DeltaItemPartDefinition", "Delta")
    material = SlotInfo("MaterialPartData", "MaterialItemPartDefinition", "Material")


class GrenadeSlot(Enum):
    """Grenade mod part slots."""

    payload = SlotInfo("AlphaPartData", "AlphaItemPartDefinition", "Alpha")
    delivery = SlotInfo("BetaPartData", "BetaItemPartDefinition", "Beta")
    trigger = SlotInfo("GammaPartData", "GammaItemPartDefinition", "Gamma")
    accessory = SlotInfo("DeltaPartData", "DeltaItemPartDefinition", "Delta")
    damage = SlotInfo("EpsilonPartData", "EpsilonItemPartDefinition", "Epsilon")
    radius = SlotInfo("ZetaPartData", "ZetaItemPartDefinition", "Zeta")
    child_count = SlotInfo("EtaPartData", "EtaItemPartDefinition", "Eta")
    status_damage = SlotInfo("ThetaPartData", "ThetaItemPartDefinition", "Theta")


class ClassModSlot(Enum):
    """Class mod part slots."""

    specialization = SlotInfo("AlphaPartData", "AlphaItemPartDefinition", "Alpha")
    primary = SlotInfo("BetaPartData", "BetaItemPartDefinition", "Beta")
    secondary = SlotInfo("GammaPartData", "GammaItemPartDefinition", "Gamma")
    penalty = SlotInfo("MaterialPartData", "MaterialItemPartDefinition", "Material")


class ArtifactSlot(Enum):
    """Artifact/relic part slots."""

    body = SlotInfo("EtaPartData", "EtaItemPartDefinition", "Eta")
    upgrade = SlotInfo("ThetaPartData", "ThetaItemPartDefinition", "Theta")
    first = SlotInfo("AlphaPartData", "AlphaItemPartDefinition", "Alpha")
    second = SlotInfo("BetaPartData", "BetaItemPartDefinition", "Beta")
    third = SlotInfo("GammaPartData", "GammaItemPartDefinition", "Gamma")
    fourth = SlotInfo("DeltaPartData", "DeltaItemPartDefinition", "Delta")
