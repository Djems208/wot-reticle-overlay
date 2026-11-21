from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class FeatureModule(Protocol):
    name: str
    enabled: bool

    def tick(self, proc) -> None: ...
    def on_host_ready(self, proc) -> None: ...