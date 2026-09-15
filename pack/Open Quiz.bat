@echo off
cd /d "%~dp0"
powershell -NoProfile -ExecutionPolicy Bypass -Command "Start-Process (Join-Path '%~dp0' 'decks.html')"
