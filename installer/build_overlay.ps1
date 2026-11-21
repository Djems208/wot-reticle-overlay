# Builds the reticle overlay into a one-dir PyInstaller bundle
param([string]$Config = "Release")
pip install -r requirements.txt
pyinstaller --noconfirm --onedir --windowed `
  --name wot-reticle-overlay `
  --add-data "config;config" `
  --add-data "payloads;payloads" `
  src/app/bootstrap.py
Write-Host "Built $Config bundle at dist/wot-reticle-overlay"