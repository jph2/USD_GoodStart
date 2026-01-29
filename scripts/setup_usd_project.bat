@echo off
REM USD GoodStart Project Setup - Windows Batch Wrapper
REM Standalone launcher for setup_usd_project.py
REM Version: see setup_usd_project.py --version or VERSION file

setlocal

REM Get the directory where this batch file is located
set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT=%SCRIPT_DIR%setup_usd_project.py

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.8+ and ensure it's in your system PATH.
    echo.
    pause
    exit /b 1
)

REM Check if the Python script exists
if not exist "%PYTHON_SCRIPT%" (
    echo ERROR: Python script not found: %PYTHON_SCRIPT%
    echo.
    pause
    exit /b 1
)

REM Run the Python script with all arguments passed through
echo Running USD GoodStart Project Setup...
echo.
python "%PYTHON_SCRIPT%" %*

REM Capture the exit code
set EXIT_CODE=%ERRORLEVEL%

REM If there was an error, show it
if %EXIT_CODE% neq 0 (
    echo.
    echo Script exited with error code: %EXIT_CODE%
)

REM Keep window open so user can see the output
echo.
pause

endlocal
exit /b %EXIT_CODE%
