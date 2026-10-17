:<<"::CMDLITERAL"
@echo off
title NASA Environmental Hotspot Forecast - Full Stack
cd /d "%~dp0"

IF EXIST "venv\Scripts\python.exe" (
    set "PYTHON_EXE=venv\Scripts\python.exe"
) ELSE IF EXIST ".venv\Scripts\python.exe" (
    set "PYTHON_EXE=.venv\Scripts\python.exe"
) ELSE (
    set "PYTHON_EXE=python"
)

echo [*] Using Python interpreter: %PYTHON_EXE%
"%PYTHON_EXE%" run.py
exit /b %ERRORLEVEL%
::CMDLITERAL
#!/usr/bin/env bash
export PYTHONUNBUFFERED=1
python backend/server.py
