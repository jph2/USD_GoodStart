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
- Folder hierarchy: 000_SOURCE, 010_ASS_USD/USD_Startpoint, 010_ASS_USD/MatLib, 010_ASS_USD/tex, 010_ASS_USD/Envs, 020_BASE_LYR, 030_SIM_LYR, 040_DATA_LYRs
- One root file by scale: USD_GoodStart_m_ROOT.usda, _cm_, or _mm_ (metersPerUnit 1, 0.01, 0.001)
- Minimal layer files (OPIN_LYR, CAM_LYR, ENV_LYR, SIM_LYR, DATA_LYRs, ACTGR_LYR, ANIM_LYR, VAR_LYR, MTL_LYR, ASS_LYR)
- README files in each folder
- Scale selection: meters, centimeters, or millimeters

For detailed information, see SETUP_STANDALONE.md
