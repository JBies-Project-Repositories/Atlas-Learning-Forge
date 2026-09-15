@echo off
setlocal
cd /d "%~dp0"
where powershell >nul 2>&1
if %ERRORLEVEL%==0 (
  powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "Start-Process -FilePath (Join-Path -Path '%~dp0' -ChildPath '00_CLICK_HERE_TO_BEGIN.html')"
  exit /b 0
)
explorer "%~dp000_CLICK_HERE_TO_BEGIN.html"
