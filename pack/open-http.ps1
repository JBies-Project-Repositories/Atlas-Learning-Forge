param(
  [Parameter(Mandatory = $true)]
  [string]$Page
)
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $root
$base = "http://127.0.0.1:8765"
function Test-Server {
  try {
    Invoke-WebRequest -UseBasicParsing -Uri $base -TimeoutSec 1 | Out-Null
    return $true
  } catch {
    return $false
  }
}
if (-not (Test-Server)) {
  $py = Get-Command python -ErrorAction SilentlyContinue
  if ($py) {
    Start-Process -FilePath "cmd.exe" -ArgumentList "/k", "cd /d `"$root`" && python -m http.server 8765"
    $n = 0
    while (-not (Test-Server) -and $n -lt 20) {
      Start-Sleep -Milliseconds 400
      $n++
    }
  } else {
    Write-Host "Python not found. Install Python or run 00_CLICK_HERE_TO_BEGIN.bat so progress can share over HTTP."
  }
}
$rel = $Page.Replace("\", "/")
Start-Process "$base/$rel"
