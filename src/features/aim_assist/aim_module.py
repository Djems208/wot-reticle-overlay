"""Aimbot-style reticle assist — snaps the in-game reticle to nearest target."""
from __future__ import annotations

import math

from src.core.lib.logger import get_logger
from src.core.models.feature_module import FeatureModule
from src.core.wot_offsets import CURRENT as OFF

log = get_logger("aim")


class AimModule(FeatureModule):
    name = "aim_assist"
    enabled = True

    def __init__(self, smoothing: float = 0.35, max_turn_deg: float = 45.0) -> None:
        self.smoothing = smoothing
        self.max_turn_deg = max_turn_deg
        self._proc = None

    def on_host_ready(self, proc) -> None:
        self._proc = proc

    def _best_target_angle(self) -> float:
        if self._proc is None:
            return 0.0
        yaw = self._proc.read_u32(OFF.local_player + OFF.turret_yaw)
        return math.radians((yaw & 0xFFFF) / 65535.0 * 360.0)

    def tick(self, proc) -> None:
        if not self.enabled or proc is None:
            return
        target = self._best_target_angle()
        delta = target * self.smoothing
        log.debug("aim delta=%.3f rad", delta)