USD GoodStart Project Setup - Standalone Package
==================================================

This package contains everything you need to set up a new USD_GoodStart project.

VERSION:
--------
See VERSION file or run:  setup_usd_project.bat --version

When creating a release zip, name it: USD_GoodStart_Setup_Standalone_vX.Y.Z.zip

CONTENTS:
---------
- setup_usd_project.py      - Main Python script
- setup_usd_project.bat     - Windows batch file wrapper (double-click to run)
- setup_usd_project.ps1     - PowerShell wrapper
- VERSION                    - Single source of version (X.Y.Z)
- SETUP_STANDALONE.md        - Detailed usage documentation
- README.md                  - Full scripts documentation

QUICK START:
------------
1. Extract this zip file to any location
2. Double-click setup_usd_project.bat
3. Follow the interactive prompts

Or run from command line:
  setup_usd_project.bat "D:\MyProject"

REQUIREMENTS:
-------------
- Python 3.8+ installed and in system PATH
- No additional packages required (uses only Python standard library)

WHAT IT DOES:
-------------
Generates a complete USD_GoodStart project structure with:
- Complete folder hierarchy (000_SOURCE, 010_ASS_USD/USD_Endpoint, 010_ASS_USD/MatLib, 010_ASS_USD/tex, 020_BASE_LYR, 030_SIM_LYR, 040_DATA_LYRs)
- Root USD file with proper layer ordering
- All layer files (opinion, variant, material, asset import, simulation, data/metadata, action, animation)
- Default assets (cube and shader ball geometry) in USD_Endpoint folder
- Material library structure in MatLib folder
- README files in each folder
- Unit system selection (millimeters, centimeters, or meters)
- Layer locking setup (data layer locked by default)

For detailed information, see SETUP_STANDALONE.md
