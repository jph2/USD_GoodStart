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

