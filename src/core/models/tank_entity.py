from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TankEntity:
    id: int
    name: str
    team: int
    x: float
    y: float
    z: float
    hp: int = 0
    spotted: bool = False
    tags: list[str] = field(default_factory=list)

    def world_distance_to(self, other: "TankEntity") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2) ** 0.5