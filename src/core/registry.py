"""Feature registry — every cheat module registers here."""
from __future__ import annotations

from typing import Iterable

from src.core.models.feature_module import FeatureModule
from src.features.aim_assist.aim_module import AimModule
from src.features.esp_radar.esp_module import EspModule
from src.features.reticle_paint.paint_module import PaintModule
from src.features.injector_loader.loader_module import LoaderModule

_ALL = (AimModule, EspModule, PaintModule, LoaderModule)


class FeatureRegistry:
    def __init__(self, modules: Iterable[FeatureModule]) -> None:
        self._modules = list(modules)

    def modules(self) -> list[FeatureModule]:
        return list(self._modules)

    def filter_to(self, names: list[str]) -> None:
        wanted = {n.lower() for n in names}
        self._modules = [m for m in self._modules if m.name.lower() in wanted]

    def __len__(self) -> int:
        return len(self._modules)


def build_default_registry() -> FeatureRegistry:
    return FeatureRegistry(cls() for cls in _ALL)