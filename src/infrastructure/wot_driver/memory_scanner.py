"""Signature scanner used by the injector loader to locate offsets after patches."""
from __future__ import annotations

import re

from src.core.lib.logger import get_logger

log = get_logger("memscan")


class SignatureScanner:
    def __init__(self, proc) -> None:
        self.proc = proc

    @staticmethod
    def compile_pattern(pattern: str) -> re.Pattern[bytes]:
        # "48 8B ?? ?? 89" -> regex
        tokens = pattern.strip().split()
        parts = [b"." if t == "??" else re.escape(bytes([int(t, 16)])) for t in tokens]
        return re.compile(b"".join(parts), re.DOTALL)

    def find_module_base(self, module_name: str = "WorldOfTanks.exe") -> int:
        # delegate to psutil-style walker in real build
        log.debug("locating module base for %s", module_name)
        return 0x00400000