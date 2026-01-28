# Standalone Setup Script Usage

**Version:** 1.0.0 | **Date:** 26.01.2026

## Quick Start

The setup script can be run in multiple ways:

### Method 1: Double-Click (Windows)
1. Navigate to `scripts/` folder
2. Double-click `setup_usd_project.bat`
3. Follow the interactive prompts

### Method 2: Command Line (Windows)
```cmd
# From any directory
scripts\setup_usd_project.bat "D:\MyProject"

# Or from scripts directory
cd scripts
setup_usd_project.bat "D:\MyProject"
```

### Method 3: PowerShell
```powershell
# From any directory
.\scripts\setup_usd_project.ps1 "D:\MyProject"

# Or from scripts directory
cd scripts
.\setup_usd_project.ps1 "D:\MyProject"
```

### Method 4: Direct Python (if Python is in PATH)
```bash
python scripts\setup_usd_project.py "D:\MyProject"
```

## Requirements

- **Python 3.8+** installed and in system PATH
- No additional Python packages required (uses only standard library)

## What It Does

The setup script interactively generates a complete USD_GoodStart project structure:

1. **Asks questions** about default prim name, unit system, and configuration
2. **Creates folder structure** (000_SOURCE, 010_ASS_USD/USD_Endpoint, 010_ASS_USD/MatLib, 010_ASS_USD/tex, 020_BASE_LYR, 030_SIM_LYR, 040_DATA_LYRs)
3. **Generates USD files** programmatically:
   - Root file with proper layer ordering
   - All layer files (opinion, variant, material, asset import, simulation, data/metadata, action, animation)
   - Default assets (cube and shader ball geometry) in USD_Endpoint folder
   - Material library structure in MatLib folder
4. **Creates README files** in each folder
5. **Sets up layer locking** (data layer locked by default, others unlocked for editing)

## Output

After running, you'll have:
- Complete project structure ready for Omniverse Composer
- Working scene with default assets (cube and ball at origin)
- Properly organized layers (base layers, simulation, data layers)
- All files following USD_GoodStart best practices
- Unit system selection (millimeters, centimeters, or meters)

## Troubleshooting

**"Python is not installed or not in PATH"**
- Install Python 3.8+ from [python.org](https://www.python.org/)
- During installation, check "Add Python to PATH"
- Or manually add Python to your system PATH

**Script doesn't run**
- Make sure you're using the correct wrapper for your shell (`.bat` for CMD, `.ps1` for PowerShell)
- Check that Python is accessible: `python --version`

**Permission errors**
- Run PowerShell as Administrator if needed
- Check that target directory is writable
