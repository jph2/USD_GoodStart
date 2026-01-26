# Scripts

**Version:** 0.9.4-beta
**Last Updated:** 12.12.2025

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
# Windows Batch file (double-click or run from command line)
scripts\setup_usd_project.bat [target_directory]

# PowerShell script
.\scripts\setup_usd_project.ps1 [target_directory]

# Or simply double-click setup_usd_project.bat in Windows Explorer
```

**Interactive Questions:**
1. **Project Type**: Choose from 4 templates:
   - Simple Product (single product setup)
   - Complex Product (car-like with sub-assemblies: Interior, Exterior, Drivetrain, Technology)
   - Production Line (multiple products/processes)
   - Production Side (factory/plant level)

2. **Product Name**: Used for root file name and default prim

3. **Default Prim**: Defaults to product name or "World"

4. **Include Samples**: Option to include sample scene files for learning

5. **Sub-Assemblies** (for complex products): Customize sub-assembly names

**Generated Structure:**
- Complete folder hierarchy (000_SOURCE through 060_META_LYR)
- Root USD file (`{ProductName}_ROOT.usda`)
- Layer files (opinion, variant, material, asset import, simulation, metadata)
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

