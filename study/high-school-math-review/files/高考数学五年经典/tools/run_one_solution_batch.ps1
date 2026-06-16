param(
  [Parameter(Mandatory=$true)][int]$StartIndex,
  [Parameter(Mandatory=$true)][int]$EndIndex
)

$ErrorActionPreference = "Stop"
$OutputEncoding = [System.Text.UTF8Encoding]::new()
[Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()

$Vault = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$RunRoot = Join-Path $Vault "tools\solution_batch_runs"
$TemplatePath = Join-Path $PSScriptRoot "solution_batch_prompt_template.md"
New-Item -ItemType Directory -Force -Path $RunRoot | Out-Null

$BatchName = "{0:D4}-{1:D4}" -f $StartIndex, $EndIndex
$PromptPath = Join-Path $RunRoot "prompt-$BatchName.md"
$LogPath = Join-Path $RunRoot "claude-$BatchName.log"
$ErrPath = Join-Path $RunRoot "claude-$BatchName.err.log"
$DonePath = Join-Path $RunRoot "done-$BatchName.txt"

$env:DISABLE_AUTOUPDATER = "1"
$env:CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE = "0"

$Prompt = Get-Content -Path $TemplatePath -Raw -Encoding UTF8
$Prompt = $Prompt.Replace("__VAULT__", $Vault)
$Prompt = $Prompt.Replace("__START_INDEX__", [string]$StartIndex)
$Prompt = $Prompt.Replace("__END_INDEX__", [string]$EndIndex)

Set-Content -Path $PromptPath -Value $Prompt -Encoding UTF8
"[$(Get-Date -Format s)] START $BatchName" | Set-Content -Path $LogPath -Encoding UTF8

Push-Location $Vault
try {
  & claude -p $Prompt --permission-mode bypassPermissions --output-format text 1>> $LogPath 2>> $ErrPath
  $exitCode = $LASTEXITCODE
} finally {
  Pop-Location
}

"[$(Get-Date -Format s)] EXIT $exitCode" | Add-Content -Path $LogPath -Encoding UTF8
Set-Content -Path $DonePath -Value $exitCode -Encoding UTF8
exit $exitCode
