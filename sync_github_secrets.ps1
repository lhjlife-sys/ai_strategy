param(
    [string]$EnvFile = ".env"
)

$ErrorActionPreference = "Stop"
$repo = "lhjlife-sys/ai_strategy"

if (-not (Test-Path $EnvFile)) {
    Write-Error "Missing $EnvFile. Copy .env.example to .env first."
}

Get-Content $EnvFile | ForEach-Object {
    if ($_ -match '^\s*#' -or $_ -match '^\s*$') { return }
    $parts = $_ -split '=', 2
    if ($parts.Count -ne 2) { return }
    $name = $parts[0].Trim()
    $value = $parts[1].Trim()
    if ($value -eq "") { return }
    gh secret set $name --body $value --repo $repo
    Write-Host "Set secret: $name"
}

Write-Host "Done. Verify at https://github.com/$repo/settings/secrets/actions"
