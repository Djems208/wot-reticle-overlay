"""Entry point for the wot-reticle-overlay runtime."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from src.app.overlay_host import OverlayHost
from src.core.lib.logger import get_logger
from src.core.registry import build_default_registry

log = get_logger("bootstrap")


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(prog="wot-reticle-overlay")
    p.add_argument("--dry-run", action="store_true", help="simulate without attaching")
    p.add_argument("--config", type=Path, default=Path("config/default.toml"))
    p.add_argument("--feature", action="append", default=[], help="enable only these features")
    return p.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    registry = build_default_registry()
    if args.feature:
        registry.filter_to(args.feature)
    log.info("loaded %d feature modules", len(registry))
    host = OverlayHost(registry=registry, dry_run=args.dry_run, config_path=args.config)
    try:
        host.run()
    except KeyboardInterrupt:
        log.info("shutdown requested")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())