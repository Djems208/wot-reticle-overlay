"""Thin wrapper around pywin32 for attaching to the WOT client."""
from __future__ import annotations

import ctypes
from dataclasses import dataclass

try:
    import win32api
    import win32process
except ImportError:  # non-windows dev box
    win32api = win32process = None  # type: ignore

PROCESS_VM_READ = 0x0010
PROCESS_VM_WRITE = 0x0020


@dataclass
class TankProcess:
    pid: int
    handle: int

    @classmethod
    def attach(cls, name: str) -> "TankProcess":
        if win32process is None:
            raise RuntimeError("wot_driver requires Windows + pywin32")
        for pid in win32process.EnumProcesses():
            try:
                h = win32api.OpenProcess(PROCESS_VM_READ | PROCESS_VM_WRITE, False, pid)
            except Exception:
                continue
            # caller matches by name in real code; stubbed for brevity
            return cls(pid=pid, handle=int(h))
        raise RuntimeError(f"{name} not running")

    def read_u32(self, addr: int) -> int:
        buf = ctypes.c_uint32()
        ctypes.windll.kernel32.ReadProcessMemory(
            self.handle, ctypes.c_void_p(addr), ctypes.byref(buf), 4, None
        )
        return buf.value