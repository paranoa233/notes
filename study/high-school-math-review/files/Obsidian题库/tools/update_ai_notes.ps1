$ErrorActionPreference = "Stop"
$vault = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $vault
if ($args.Count -eq 0) {
    python .\tools\ai_note_manager.py index
} else {
    python .\tools\ai_note_manager.py @args
}
