$ErrorActionPreference = "Stop"

$protocol = "mdopen"
$scriptPath = Join-Path $PSScriptRoot "open_markdown_url.ps1"
$command = "powershell.exe -WindowStyle Hidden -NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`" `"%1`""
$baseKey = "HKCU:\Software\Classes\$protocol"
$commandKey = "$baseKey\shell\open\command"

New-Item -Path $baseKey -Force | Out-Null
Set-Item -Path $baseKey -Value "URL:Markdown Opener"
New-ItemProperty -Path $baseKey -Name "URL Protocol" -Value "" -PropertyType String -Force | Out-Null

New-Item -Path $commandKey -Force | Out-Null
Set-Item -Path $commandKey -Value $command

Write-Host "mdopen protocol registered."
