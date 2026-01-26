# USD GoodStart Project Setup - PowerShell Wrapper
# Standalone launcher for setup_usd_project.py

param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Arguments
)

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonScript = Join-Path $ScriptDir "setup_usd_project.py"

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Using: $pythonVersion" -ForegroundColor Gray
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Python 3.8+ and ensure it's in your system PATH." -ForegroundColor Yellow
    exit 1
}

# Run the Python script with all arguments passed through
if ($Arguments.Count -gt 0) {
    python $PythonScript $Arguments
} else {
    python $PythonScript
}
