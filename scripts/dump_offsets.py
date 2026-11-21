"""Scan the running WOT client and dump fresh offsets to src/core/wot_offsets.py."""
from src.infrastructure.wot_driver.memory_scanner import SignatureScanner
from src.infrastructure.wot_driver.process_attach import TankProcess


def main() -> None:
    proc = TankProcess.attach(name="WorldOfTanks.exe")
    scanner = SignatureScanner(proc)
    base = scanner.find_module_base()
    print(f"module base: 0x{base:x}")
    # TODO: emit dataclass block once sigs are verified per patch


if __name__ == "__main__":
    main()