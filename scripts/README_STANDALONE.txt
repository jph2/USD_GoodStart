USD GoodStart Project Setup - Standalone Package
==================================================

This package contains everything you need to set up a new USD_GoodStart project.

CONTENTS:
---------
- setup_usd_project.py      - Main Python script
- setup_usd_project.bat     - Windows batch file wrapper (double-click to run)
- setup_usd_project.ps1     - PowerShell wrapper
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
- Complete folder hierarchy (000_SOURCE through 060_META_LYR)
- Root USD file with proper layer ordering
- All layer files (opinion, variant, material, asset import, simulation, metadata)
- Default assets (cube and shader ball geometry)
- Materials (blue and red OmniPBR)
- Variant sets (cube material variants)
- README files in each folder
- Safe mode setup (all layers locked, session layer for authoring)

For detailed information, see SETUP_STANDALONE.md
