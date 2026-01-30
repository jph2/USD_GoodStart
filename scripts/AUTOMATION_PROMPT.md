# USD GoodStart Setup Script - Automation Prompt

**Purpose:** This document describes the complete specification for generating the `setup_usd_project.py` script. Use this prompt to recreate, modify, or extend the script.

---

## Goal

Create a Python script (`setup_usd_project.py`) that generates a complete USD GoodStart project structure with customizable default prim name and scale selection.

---

## Reference Files (Blueprints)

The script should use these existing files as templates when available:

```
USD_GoodStart/
├── USD_GoodStart_m_ROOT.usda      ← Root template for Meters (metersPerUnit = 1)
├── USD_GoodStart_cm_ROOT.usda     ← Root template for Centimeters (metersPerUnit = 0.01)
├── USD_GoodStart_mm_ROOT.usda     ← Root template for Millimeters (metersPerUnit = 0.001)
├── 020_BASE_LYR/
│   ├── ASS_LYR.usda               ← Asset layer template (over "World" with placeholder refs)
│   ├── CAM_LYR.usda               ← Camera layer template (over "World" with default camera)
│   └── README.md                  ← README template for 020_BASE_LYR
├── 000_SOURCE/README.md           ← README template
├── 010_ASS_USD/README.md          ← README template
├── 030_SIM_LYR/README.md          ← README template
└── 040_DATA_LYRs/README.md        ← README template
```

---

## Output Structure

The script generates this folder/file hierarchy:

```
{target_directory}/
├── {DefaultPrim}_{scale}_ROOT.usda    ← Root file (named after default prim + scale)
├── 000_SOURCE/
│   └── README.md
├── 010_ASS_USD/
│   ├── README.md
│   ├── USD_Startpoint/                ← Geometry assets from CAD/DCC exports
│   ├── MatLib/                        ← Material libraries
│   ├── tex/                           ← Textures
│   └── Envs/                          ← Environments
├── 020_BASE_LYR/
│   ├── README.md
│   ├── ASS_LYR.usda                   ← over "{DefaultPrim}" with placeholder Xform refs
│   ├── CAM_LYR.usda                   ← over "{DefaultPrim}" with default Camera
│   ├── OPIN_LYR.usda                  ← Minimal (#usda 1.0)
│   ├── ENV_LYR.usda                   ← Minimal
│   ├── MTL_LYR.usda                   ← Minimal
│   ├── VAR_LYR.usda                   ← Minimal
│   ├── ACTGR_LYR.usda                 ← Minimal
│   ├── ANIM_LYR.usda                  ← Minimal
│   └── PHY_LYR.usda                   ← Minimal
├── 030_SIM_LYR/
│   ├── README.md
│   └── SIM_LYR.usda                   ← Minimal
└── 040_DATA_LYRs/
    ├── README.md
    └── DATA_LYRs.usda                 ← Minimal
```

---

## Interactive Prompts

### 1. Scale Selection
```
Select scale (root file metersPerUnit):
  [1] Meters (m) – metersPerUnit = 1
  [2] Centimeters (cm) – metersPerUnit = 0.01
  [3] Millimeters (mm) – metersPerUnit = 0.001
Enter choice (1–3, default: 1): 
```

### 2. Default Prim Name
```
Default prim name (the root Xform that holds your scene):
  This name will be used in the root file and all layer files.
  Examples: World, MyProduct, Scene, Assembly
Enter default prim name (default: World): 
```

**Validation:**
- Must start with a letter
- Invalid characters (spaces, special chars) replaced with underscores
- Empty input defaults to "World"

---

## File Content Specifications

### Root File (`{DefaultPrim}_{scale}_ROOT.usda`)

**If reference root exists in repo:** Copy from `USD_GoodStart_{scale}_ROOT.usda` and:
1. Update `authoring_layer` to point to new filename
2. Replace `defaultPrim = "World"` with `defaultPrim = "{DefaultPrim}"`
3. Replace `def Xform "World"` with `def Xform "{DefaultPrim}"`

**If no reference:** Generate from embedded template with:
- `customLayerData` (cameraSettings, omni_layer with locked layers, renderSettings)
- `defaultPrim = "{DefaultPrim}"`
- `metersPerUnit` based on scale choice
- `subLayers` array referencing all layer files
- `def Xform "{DefaultPrim}"` containing a Cube mesh
- `def Xform "Environment"` with DomeLight, DistantLight, Looks/Grid material, ground mesh, groundCollider
- `def "Render"` with OmniverseKit render settings

### ASS_LYR.usda (Asset Layer)
```usda
#usda 1.0

over "{DefaultPrim}"
{
    def Xform "A" (
        references = <>
    )
    {
        double3 xformOp:rotateXYZ = (0, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }

    def Xform "B" (
        references = <>
    )
    {
        double3 xformOp:rotateXYZ = (0, 0, 0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 0, 0)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateXYZ", "xformOp:scale"]
    }
}
```

### CAM_LYR.usda (Camera Layer)
```usda
#usda 1.0

over "{DefaultPrim}"
{
    def Camera "Camera"
    {
        float2 clippingRange = (1, 10000000)
        float focalLength = 18.147562
        float focusDistance = 400
        double3 xformOp:rotateYXZ = (0, -0, -0)
        double3 xformOp:scale = (1, 1, 1)
        double3 xformOp:translate = (0, 270, 360)
        uniform token[] xformOpOrder = ["xformOp:translate", "xformOp:rotateYXZ", "xformOp:scale"]
    }
}
```

### All Other Layer Files
Minimal content only:
```usda
#usda 1.0
```

### README Files
Use templates matching the actual repo README.md files for each folder.

---

## Sublayer Order (in root file)

Strongest to weakest (first in array = strongest):
1. `./020_BASE_LYR/OPIN_LYR.usda` – Opinions (strongest)
2. `./020_BASE_LYR/CAM_LYR.usda` – Cameras
3. `./020_BASE_LYR/ENV_LYR.usda` – Environment
4. `./030_SIM_LYR/SIM_LYR.usda` – Simulation
5. `./040_DATA_LYRs/DATA_LYRs.usda` – Data/Metadata
6. `./020_BASE_LYR/ACTGR_LYR.usda` – Action Graphs
7. `./020_BASE_LYR/ANIM_LYR.usda` – Animation
8. `./020_BASE_LYR/VAR_LYR.usda` – Variants
9. `./020_BASE_LYR/MTL_LYR.usda` – Materials
10. `./020_BASE_LYR/PHY_LYR.usda` – Physics simulation
11. `./020_BASE_LYR/ASS_LYR.usda` – Assets (weakest)

---

## Script Features

1. **Standalone operation:** No external dependencies (Python standard library only)
2. **Version flag:** `--version` or `-v` prints version and exits
3. **Target directory:** Optional CLI argument, defaults to current directory
4. **Script folder detection:** If run from scripts folder, creates project in parent
5. **Non-empty directory warning:** Asks for confirmation before proceeding
6. **Wrapper scripts:** Include `.bat` (Windows CMD) and `.ps1` (PowerShell) wrappers

---

## Packaging

Create standalone ZIP containing:
- `setup_usd_project.py`
- `setup_usd_project.bat`
- `setup_usd_project.ps1`
- `VERSION`
- `SETUP_STANDALONE.md`
- `README.md`
- `README_STANDALONE.txt`

ZIP naming: `USD_GoodStart_Setup_Standalone_v{X.Y.Z}.zip`

---

## Usage Examples

```bash
# Interactive mode (current directory)
python setup_usd_project.py

# Specify target directory
python setup_usd_project.py "D:\MyProject"

# Windows batch
setup_usd_project.bat "D:\MyProject"

# PowerShell
.\setup_usd_project.ps1 "D:\MyProject"
```

---

## Version History

- **0.9.3** – Custom default prim name, root file renamed to `{DefaultPrim}_{scale}_ROOT.usda`
- **0.9.2** – Added PHY_LYR.usda, fixed README templates
- **0.9.1** – Added missing subfolders (MatLib, tex, Envs)
- **0.9.0** – Initial rewrite with scale selection, minimal sublayers, embedded root template

---

*This prompt can be used to regenerate or modify the setup script. Reference the actual USD files in the repo for exact content.*
