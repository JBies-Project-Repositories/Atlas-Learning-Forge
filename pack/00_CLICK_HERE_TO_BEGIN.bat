@echo off
setlocal
cd /d "%~dp0"
where python >nul 2>&1
if %ERRORLEVEL%==0 (
  echo Starting local server in a new window: http://127.0.0.1:8765/
  echo Close that window to stop the server. Progress then shares across pages.
  start "Atlas of the Build Loop" cmd /k "cd /d "%~dp0" && python -m http.server 8765"
  timeout /t 2 /nobreak >nul
  start "" "http://127.0.0.1:8765/00_CLICK_HERE_TO_BEGIN.html"
  exit /b 0
)
echo Python was not found. Opening as a file.
echo Warning: file:// may isolate progress so the quiz and dashboard do not share keys.
where powershell >nul 2>&1
if %ERRORLEVEL%==0 (
  powershell -NoProfile -ExecutionPolicy Bypass -Command ^
    "Start-Process -FilePath (Join-Path -Path '%~dp0' -ChildPath '00_CLICK_HERE_TO_BEGIN.html')"
  exit /b 0
)
explorer "%~dp000_CLICK_HERE_TO_BEGIN.html"
