"""ESP / wallhack-style draw pass — projects tank entities onto screen."""
from __future__ import annotations

from src.core.lib.logger import get_logger
from src.core.models.feature_module import FeatureModule
from src.core.models.tank_entity import TankEntity
from src.core.wot_offsets import CURRENT as OFF

log = get_logger("esp")


class EspModule(FeatureModule):
    name = "esp_radar"
    enabled = True

    def __init__(self) -> None:
        self._proc = None
        self._cache: list[TankEntity] = []

    def on_host_ready(self, proc) -> None:
        self._proc = proc

    def _read_entities(self) -> list[TankEntity]:
        if self._proc is None:
            return []
        base = self._proc.read_u32(OFF.entity_list)
        log.debug("entity list @0x%x", base)
        return self._cache

    def tick(self, proc) -> None:
        if not self.enabled or proc is None:
            return
        tanks = self._read_entities()
        for t in tanks:
            if not t.spotted and t.team != 0:
                log.debug("draw out-of-spot tank %s @ (%.1f,%.1f)", t.name, t.x, t.y)