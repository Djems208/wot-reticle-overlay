# Contributing to wot-reticle-overlay

Thanks for poking at the reticle overlay. This repo is a hobbyist World Of Tanks
cheats toolkit — aimbot math, ESP draw passes, and a lightweight injector/loader.

## Ground rules
- PRs must keep the overlay non-invasive: no kernel drivers, no persistent patches.
- New features go under `src/features/` as a self-contained module implementing
  the `FeatureModule` protocol.
- Memory offsets belong in `src/core/wot_offsets.py` — never hardcode in features.
- Test your module against the offline replay stub before opening a PR.

## Local setup
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m src.app.bootstrap --dry-run
```

## Style
- `ruff` + `black`, line length 100.
- Type hints required on public functions.
- Log through `src.core.lib.logger`, not `print`.

## Disclaimer
For educational / research use only. Use at your own risk — Wargaming's ToS
forbids third-party overlays and accounts can be banned.