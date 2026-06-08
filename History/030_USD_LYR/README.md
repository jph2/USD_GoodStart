---
arys_schema_version: '1.2'
id: 986e8647-049c-45ec-b946-1b346449ad5b
title: 030_LYR_USD
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2025-12-12T00:34:10Z'
last_modified: '2025-12-12T00:34:10Z'
---

# 030_LYR_USD

**Version:** 0.9.4-beta
**Last Updated:** 12.12.2025

## Purpose

This folder contains **general USD layer files** that modify and override content in the root file (`GoodStart_ROOT.usda`). Layers enable non-destructive modifications to assets without altering base CAD-converted assets.

## Current Layers (General / Visual)

- **`your very Personal opinion_LYR.usda`** - **Default authoring layer** (unlocked, for user modifications)
- `Opinion_xyz_LYR.usda` - General opinion/override layer (locked)
- `Opinion_abc_LYR.usda` - Additional opinion layer (locked)
- `Variant_LYR.usda` - Variant set definitions and selections (locked)
- `Mtl_work_LYR.usda` - Material work and modifications (locked)
- `AssetImport_LYR.usda` - Asset import and reference layer (locked, must be at bottom)

## Usage

### Default Authoring Layer

**`your very Personal opinion_LYR.usda`** is the **default authoring layer** set in `GoodStart_ROOT.usda`. This is where you should make your general visual/layout/material modifications and changes.

**All other layers are locked** to prevent accidental modifications. This ensures:
- Base assets remain unchanged
- Layer structure stays intact
- Non-destructive workflow is maintained

### ⚠️ Critical: Do NOT Edit the Root Layer

**Strongly recommended:** Do not put anything in `GoodStart_ROOT.usda` itself. Anything in the root layer becomes **Local** (strongest composition strength in LIV(E)RPS), which means:
- It cannot be overridden by any sublayer
- It breaks the non-destructive workflow
- It makes changes difficult to track and manage

**Always edit in `your very Personal opinion_LYR.usda`** or create new layers instead.

### Adding New General Layers

1. Create a new `.usda` file with descriptive name ending in `_LYR`
2. Add to `subLayers` array in `GoodStart_ROOT.usda`
3. **Critical**: `AssetImport_LYR.usda` must be last (bottom/weakest) in the array
4. Consider locking new layers if they should remain stable

### Layer Order

The `subLayers` array is ordered from **strongest (first)** to **weakest (last)**:
- First in array = strongest (applied last, overrides others)
- Last in array = weakest (applied first, can be overridden)

**Example (updated layout using `030_LYR_USD/`):**
```usda
subLayers = [
    @./030_LYR_USD/your very Personal opinion_LYR.usda@,  # First = strongest (DEFAULT AUTHORING LAYER)
    @./030_LYR_USD/Opinion_xyz_LYR.usda@,                 # Locked
    @./030_LYR_USD/Opinion_abc_LYR.usda@,                 # Locked
    @./030_LYR_USD/Variant_LYR.usda@,                     # Locked
    @./030_LYR_USD/Mtl_work_LYR.usda@,                    # Locked
    @./030_LYR_USD/AssetImport_LYR.usda@                  # Last = weakest (CRITICAL, Locked)
]
```

## Best Practices

- **Use the default authoring layer** - Make changes in `your very Personal opinion_LYR.usda`
- **Do NOT edit the root layer** - Anything in `GoodStart_ROOT.usda` becomes Local (strongest) and cannot be overridden
- **Respect locked layers** - Do not unlock or modify locked layers unless necessary
- **Keep layers focused** - Each layer should have a specific purpose
- **Use descriptive names** - Make it clear what each layer modifies
- **Keep structure simple** - Avoid unnecessary complexity
- **Do NOT import assets in root layer** - Keep `GoodStart_ROOT.usda` clean (only subLayers and metadata)
- **AssetImport_LYR at bottom** - Must be last in `subLayers` array

## Modifying Assets

When modifying assets from `010_ASS_USD/`:
1. **Edit `your very Personal opinion_LYR.usda`** (the default authoring layer)
2. Reference the base asset using `over` statements
3. Add modifications/opinions
4. Layer will override base asset when loaded

**Example:**
```usda
# In your very Personal opinion_LYR.usda
over "AssetName" {
    # Your modifications here
    double3 xformOp:translate = (10, 0, 0)
    string customAttribute = "myValue"
}
```

**Remember:** Do not edit the root layer (`GoodStart_ROOT.usda`) - use the authoring layer instead.

## Digital Twin Use Cases

- Scenario variations (different configurations/states)
- Metadata enrichment (digital twin-specific metadata)
- System connections (PLM/PDM/ERP, AAS)
- Temporal changes (asset changes over time)
- Multi-disciplinary views (different stakeholder perspectives)

**Always use relative paths** when referencing assets (e.g., `@../010_ASS_USD/asset.usd@`).
