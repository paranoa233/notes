param(
    [string]$Url
)

$ErrorActionPreference = "Stop"
$logPath = Join-Path $PSScriptRoot "mdopen.log"

try {
    if ([string]::IsNullOrWhiteSpace($Url)) {
        throw "Empty URL."
    }

    $vaultRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot "..")).Path
    $path = $null

    if ($Url -match "^mdopen://open\?path=(.+)$") {
        $path = [System.Uri]::UnescapeDataString($Matches[1])
    }

    if ([string]::IsNullOrWhiteSpace($path)) {
        throw "URL does not contain a path: $Url"
    }

    $resolved = (Resolve-Path -LiteralPath $path).Path
    $vaultPrefix = $vaultRoot.TrimEnd([char]"\") + "\"

    if (-not $resolved.StartsWith($vaultPrefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to open a path outside the vault: $resolved"
    }

    if ([System.IO.Path]::GetExtension($resolved).ToLowerInvariant() -ne ".md") {
        throw "Refusing to open a non-Markdown file: $resolved"
    }

    $typoraCandidates = @(
        "C:\Program Files\Typora\Typora.exe",
        "C:\Program Files (x86)\Typora\Typora.exe",
        (Join-Path $env:LOCALAPPDATA "Programs\Typora\Typora.exe")
    )
    $typora = $typoraCandidates | Where-Object { Test-Path -LiteralPath $_ } | Select-Object -First 1

    if ($typora) {
        Start-Process -FilePath $typora -ArgumentList "`"$resolved`""
    } else {
        Start-Process -FilePath $resolved
    }
} catch {
    $message = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $_.Exception.Message
    Add-Content -LiteralPath $logPath -Value $message -Encoding UTF8
    exit 1
}
