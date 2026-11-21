"""WOT memory offsets used by ESP / aim modules. Updated per patch."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class WotOffsets:
    patch: str
    entity_list: int
    local_player: int
    view_matrix: int
    reticle_state: int
    turret_yaw: int


# 2026.03 live client
CURRENT = WotOffsets(
    patch="2026.03",
    entity_list=0x2A4F1C0,
    local_player=0x2A4F1D8,
    view_matrix=0x2A51A40,
    reticle_state=0x2A4E8B0,
    turret_yaw=0x30,
)