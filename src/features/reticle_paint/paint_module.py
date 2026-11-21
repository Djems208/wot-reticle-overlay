"""Cosmetic reticle paint — recolors the aiming reticle via overlay draw calls."""
from __future__ import annotations

from src.core.models.feature_module import FeatureModule


class PaintModule(FeatureModule):
    name = "reticle_paint"
    enabled = False

    def __init__(self, color: tuple[int, int, int] = (255, 40, 40)) -> None:
        self.color = color

    def on_host_ready(self, proc) -> None:
        pass

    def tick(self, proc) -> None:
        if not self.enabled:
            return
        # emits a draw command into the shared overlay buffer