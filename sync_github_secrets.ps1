# Sync .env secrets to GitHub Actions
# Auth: run `gh auth login` OR set env GH_TOKEN to a PAT with repo scope
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if ($env:GH_TOKEN -and -not $env:GITHUB_TOKEN) {
    $env:GITHUB_TOKEN = $env:GH_TOKEN
}

$gh = "C:\Program Files\GitHub CLI\gh.exe"
if (-not (Test-Path $gh)) {
    $ghCmd = Get-Command gh -ErrorAction SilentlyContinue
    if ($ghCmd) { $gh = $ghCmd.Source } else {
        Write-Host "Install GitHub CLI and run: gh auth login"
        Write-Host "Or add secrets manually: see GITHUB_SETUP.md"
        exit 1
    }
}

$repo = "lhjlife-sys/ai_strategy"
$envFile = Join-Path $PSScriptRoot ".env"
if (-not (Test-Path $envFile)) { throw ".env not found. Copy .env.example to .env first." }

$vars = @{}
Get-Content $envFile | ForEach-Object {
    if ($_ -match '^\s*#' -or $_ -notmatch '=') { return }
    $k, $v = $_.Split('=', 2)
    $vars[$k.Trim()] = $v.Trim()
}

$secretKeys = @('OPENAI_API_KEY', 'SMTP_USER', 'SMTP_PASSWORD', 'EMAIL_FROM', 'EMAIL_TO')
if ($vars['GITHUB_TOKEN']) { $secretKeys += 'GITHUB_TOKEN' }

foreach ($key in $secretKeys) {
    if (-not $vars[$key]) { Write-Warning "Skip $key (empty)"; continue }
    & $gh secret set $key --body $vars[$key] --repo $repo
    Write-Host "Set secret: $key"
}

Write-Host "Done. Verify at https://github.com/$repo/settings/secrets/actions"
Write-Host "Run workflow: gh workflow run daily-strategy.yml --repo $repo"
