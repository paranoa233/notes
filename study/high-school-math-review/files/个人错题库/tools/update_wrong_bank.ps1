$ErrorActionPreference = "Stop"

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $Root

Write-Host "Refreshing wrong problem bank..."
python tools\refresh_wrong_bank.py
if ($LASTEXITCODE -ne 0) {
  throw "Wrong problem bank refresh failed."
}

Write-Host ""
Write-Host "Done. Open the Obsidian workbench: 00_控制台\学习工作台.md"
