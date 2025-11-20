# Scripts

This directory contains utility scripts for USD GoodStart project management and validation.

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

