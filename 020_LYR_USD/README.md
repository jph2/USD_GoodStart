# 020_LYR_USD

**Version:** 0.9.2-beta  
**Last Updated:** 11.22.2025

## Purpose

This folder contains **USD layer files** that modify and override content in the root file (`GoodStart_ROOT.usda`). Layers enable non-destructive modifications to assets without altering base CAD-converted assets.

## Current Layers

- `AssetImport_LYR.usda` - Asset import and reference layer (must be at bottom)
- `Mtl_work_LYR.usda` - Material work and modifications
- `Variant_LYR.usda` - Variant set definitions and selections
- `Opinion_xyz_LYR.usda` - General opinion/override layer (top/strongest)

## Usage

### Adding New Layers

1. Create a new `.usda` file with descriptive name ending in `_LYR`
2. Add to `subLayers` array in `GoodStart_ROOT.usda`
3. **Critical**: `AssetImport_LYR.usda` must be last (bottom/weakest) in the array

### Layer Order

The `subLayers` array is ordered from **strongest (first)** to **weakest (last)**:
- First in array = strongest (applied last, overrides others)
- Last in array = weakest (applied first, can be overridden)

**Example:**
```usda
subLayers = [
    @./020_LYR_USD/Opinion_xyz_LYR.usda@,    # First = strongest
    @./020_LYR_USD/Variant_LYR.usda@,
    @./020_LYR_USD/Mtl_work_LYR.usda@,
    @./020_LYR_USD/AssetImport_LYR.usda@     # Last = weakest (CRITICAL)
]
```

## Best Practices

- **Keep layers focused** - Each layer should have a specific purpose
- **Use descriptive names** - Make it clear what each layer modifies
- **Keep structure simple** - Avoid unnecessary complexity
- **Do NOT import assets in root layer** - Keep `GoodStart_ROOT.usda` clean
- **AssetImport_LYR at bottom** - Must be last in `subLayers` array

## Modifying Assets

When modifying assets from `010_ASS_USD/`:
1. Create or modify a layer in this folder
2. Reference the base asset in the layer
3. Add modifications/opinions
4. Layer will override base asset when loaded

## Digital Twin Use Cases

- Scenario variations (different configurations/states)
- Metadata enrichment (digital twin-specific metadata)
- System connections (PLM/PDM/ERP, AAS)
- Temporal changes (asset changes over time)
- Multi-disciplinary views (different stakeholder perspectives)

**Always use relative paths** when referencing assets (e.g., `@../010_ASS_USD/asset.usd@`).
