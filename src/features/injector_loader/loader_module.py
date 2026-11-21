"""Manual-map injector helper used to load feature DLLs into the game process."""
from __future__ import annotations

from pathlib import Path

from src.core.lib.logger import get_logger
from src.core.models.feature_module import FeatureModule

log = get_logger("loader")


class LoaderModule(FeatureModule):
    name = "injector_loader"
    enabled = False

    def __init__(self, dll_path: Path = Path("payloads/reticle.dll")) -> None:
        self.dll_path = dll_path

    def on_host_ready(self, proc) -> None:
        if not self.enabled or proc is None:
            return
        log.info("manual-mapping %s into pid=%s", self.dll_path.name, proc.pid)

    def tick(self, proc) -> None:
        pass