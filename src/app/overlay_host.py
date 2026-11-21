"""Main loop that owns the render thread and the game-process handle."""
from __future__ import annotations

from pathlib import Path

from src.core.registry import FeatureRegistry
from src.core.lib.logger import get_logger
from src.infrastructure.wot_driver.process_attach import TankProcess
from src.features.esp_radar.esp_module import EspModule
from src.features.aim_assist.aim_module import AimModule

log = get_logger("overlay_host")


class OverlayHost:
    def __init__(self, registry: FeatureRegistry, dry_run: bool, config_path: Path) -> None:
        self.registry = registry
        self.dry_run = dry_run
        self.config_path = config_path
        self._proc: TankProcess | None = None

    def _attach(self) -> None:
        if self.dry_run:
            log.info("dry-run: skipping game attach")
            return
        self._proc = TankProcess.attach(name="WorldOfTanks.exe")
        log.info("attached to pid=%s", self._proc.pid)

    def run(self) -> None:
        self._attach()
        for module in self.registry.modules():
            if isinstance(module, (EspModule, AimModule)):
                module.on_host_ready(self._proc)
        log.info("overlay loop started")
        while True:
            for module in self.registry.modules():
                module.tick(self._proc)
            # rate limiting handled inside modules