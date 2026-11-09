---
arys_schema_version: '1.2'
id: ed7b7ec4-33b5-4829-914f-4a09d1bac435
title: Scripts
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-17T09:24:41Z'
last_modified: '2026-02-17T09:24:41Z'
---

# Scripts

**Version:** 0.9.5.3 (see `VERSION` or `python setup_usd_project.py --version`)
**Last Updated:** 29.01.2026 16:00
**Tag block:**
#framework_integration #api_integration #conversion #directrl #validation #post_production #ide #automation #layers #stage #openusd #workflow_automation #best_practices #usd_core #omniverse #hybrid #references #analysis #variants #composition

This directory contains utility scripts for USD GoodStart project management and validation.

## Setup Script

### setup_usd_project.py

**Interactive project setup script** that generates a complete USD_GoodStart folder structure with configurable templates.

**Features:**
- Interactive questions for project configuration
- Multiple project types (simple product, complex product, production line, production side)
- Automatic folder structure generation
- USD file template generation (root, layers, sub-assemblies)
- Sample scene option for learning
- README generation for each folder

**Usage:**

**Option 1: Direct Python (requires Python in PATH)**
```bash
# Run in current directory
python scripts/setup_usd_project.py

# Run in specific directory
python scripts/setup_usd_project.py /path/to/new/project
```

**Option 2: Standalone Wrappers (recommended)**
```bash
# In a repository checkout:
#   download and unpack `scripts/USD_GoodStart_Setup_Standalone_v0.9.5.3.zip`
#   when you want the standalone package.

# Windows Batch file from a repository checkout
scripts\setup_usd_project.bat [target_directory]

# PowerShell script from a repository checkout
.\scripts\setup_usd_project.ps1 [target_directory]

# Linux/macOS POSIX shell script from the unpacked standalone package
sh setup_usd_project.sh [target_directory]

# Or simply double-click setup_usd_project.bat in Windows Explorer
```

**Interactive Questions:**
1. **Default Prim Name**: Name for the default prim (defaults to "World")
   - Note: Root file is always named `USD_GoodStart_ROOT.usda`
   - Only the default prim name changes based on your input
   - The default prim is **defined in the root layer** so references using "\<Default Prim\>" resolve correctly (e.g. Omniverse, usdview)

2. **Include Samples**: Option to include sample scene files for learning

3. **Unit System**: Choose millimeters, centimeters, or meters (affects scene scale and camera settings)

**Generated Structure:**
- Complete folder hierarchy (000_SOURCE, 010_ASS_USD/USD_Startpoint, 010_ASS_USD/USD_Wrappers, 010_ASS_USD/MatLib, 010_ASS_USD/tex, 010_ASS_USD/Envs, 020_BASE_LYR, 035_RUNTIME_LYR, 030_SIM_LYR, 040_DATA_LYRs, _contracts, _pipeline_reports, _comfyui_workflows)
- Asset-package template under `010_ASS_USD/USD_Wrappers/_asset_package_template/{layers,payloads,data}`
- Root USD file (`USD_GoodStart_ROOT.usda` - always this name)
- Layer files (opinion, variant, material, asset import, simulation, data/metadata, action, animation)
- Sub-assembly files (for complex products)
- README files in each folder
- Sample assets (if samples enabled)

**Requirements:**
- Python 3.8+
- USD libraries optional (script works without them, but cannot validate USD syntax)

## Validation Scripts

### validate_usd.py (Convenience Script - Recommended)

**Auto-detecting validation script** that determines whether to validate as an asset or scene:
- Automatically detects file type based on structure and naming
- Single command for all USD files
- Falls back to asset validation if uncertain

**Usage:**
```bash
python scripts/validate_usd.py path/to/file.usd
python scripts/validate_usd.py 010_ASS_USD/asset.usda
python scripts/validate_usd.py GoodStart_ROOT.usda
```

### validate_asset.py

Validates individual USD asset files for common issues:
- File syntax errors
- Missing references
- Invalid layer composition
- Metadata completeness

**Usage:**
```bash
python scripts/validate_asset.py path/to/asset.usd
python scripts/validate_asset.py 010_ASS_USD/asset.usd
```

### validate_scene.py

Validates the entire USD scene (root file and all layers):
- Layer composition correctness
- Asset references
- Missing files
- Layer ordering

**Usage:**
```bash
python scripts/validate_scene.py GoodStart_ROOT.usda
```

## Requirements

Both scripts require:
- Python 3.8+
- `usd-core` package: `pip install usd-core`

## CI/CD Integration

These scripts are automatically run in the GitHub Actions workflow (`.github/workflows/validate.yml`) on:
- Push to main/develop branches
- Pull requests to main branch
- Manual workflow dispatch

## Extending Validation

You can extend these scripts to add:
- Custom schema validation
- Material validation
- Texture path checking
- Metadata completeness checks
- Performance metrics

## Example: Adding Custom Validation

### Checking USD Prim Paths

```python
from pxr import Sdf

def check_prim_path_type(path_str):
    """Check if a USD prim path is absolute or relative."""
    path = Sdf.Path(path_str)
    if path.IsAbsolutePath():
        return "Absolute Path"
    else:
        return "Relative Path"

# Example usage
prim_path = "/World/Child"
print(f"Path '{prim_path}' is a {check_prim_path_type(prim_path)}")
# Output: Path '/World/Child' is a Absolute Path
```

**Use Cases:**
- Validating prim path naming conventions
- Checking scene graph structure
- Ensuring consistent path usage

### Checking File Paths in References/Sublayers

The validation scripts automatically check for absolute file paths in references and sublayers and warn about them. You can extend this:

```python
import os

def check_file_path_type(file_path):
    """Check if a file path is absolute or relative."""
    if os.path.isabs(file_path) or (len(file_path) > 1 and file_path[1] == ":"):
        return "Absolute Path"
    else:
        return "Relative Path"

# Example usage
file_path1 = "C:/Projects/USD_GoodStart/010_ASS_USD/asset.usd"
file_path2 = "../010_ASS_USD/asset.usd"
print(f"Path '{file_path1}' is a {check_file_path_type(file_path1)}")
print(f"Path '{file_path2}' is a {check_file_path_type(file_path2)}")
```

### Digital Twin Metadata Validation

```python
# Add to validate_asset.py
def validate_digital_twin_metadata(prim):
    """Check for required digital twin metadata."""
    required_attrs = ['digitalTwin:assetId', 'digitalTwin:plmId']
    missing = []
    for attr in required_attrs:
        if not prim.HasAttribute(attr):
            missing.append(attr)
    return missing
```
