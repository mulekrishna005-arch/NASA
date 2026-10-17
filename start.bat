@echo off
title NASA Environmental Hotspot Forecast - Full Stack
cd /d "%~dp0"

echo ==================================================================
echo        NASA Environmental Hotspot Activity Forecast System        
echo                   Starting Full-Stack Environment                  
echo ==================================================================
echo.

IF EXIST "venv\Scripts\python.exe" (
    set "PYTHON_EXE=venv\Scripts\python.exe"
) ELSE IF EXIST ".venv\Scripts\python.exe" (
    set "PYTHON_EXE=.venv\Scripts\python.exe"
) ELSE (
    set "PYTHON_EXE=python"
)

echo [*] Using Python interpreter: %PYTHON_EXE%
"%PYTHON_EXE%" run.py

if errorlevel 1 (
    echo.
    echo [!] An error occurred while running the full-stack launcher.
    pause
)
