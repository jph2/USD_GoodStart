---
arys_schema_version: '1.2'
id: 39c3699c-ef47-468e-aca0-269575fe235d
title: USD GoodStart Setup Script - Automation Prompt
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-17T09:43:32Z'
last_modified: '2026-02-17T09:43:32Z'
---

**Version**: 1.0.0 | **Date**: 16.02.2026 | **Time**: 12:00 | **GlobalID**: 20260216_1200_USD_GoodStart_batch

**Tag block:**
#automation #specialization #creative #prim #reference #usda #openusd #workflow_automation #best_practices #usd_core #references #analysis #layers #composition #export #framework_integration #ai_coding_agents #deterministic_workflows #usd_start_point #usd_goodstart #isaac_sim

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
├── 035_RUNTIME_LYR/README.md      ← README template
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
├── 035_RUNTIME_LYR/
│   ├── README.md
│   └── RUNTIME_LYR.usda               ← Minimal
└── 040_DATA_LYRs/
    ├── README.md
    └── DATA_LYRs.usda                 ← Minimal
```

Additional generated folders required by the current GoodStart structure:

```text
010_ASS_USD/USD_Wrappers/
010_ASS_USD/USD_Wrappers/_asset_package_template/layers/
010_ASS_USD/USD_Wrappers/_asset_package_template/payloads/
010_ASS_USD/USD_Wrappers/_asset_package_template/data/
_contracts/
_pipeline_reports/
_comfyui_workflows/
```

---

## Interactive Prompts

### 1. Scale Selection

Default is **Centimeters** (option 1), matching Omniverse Composer. Isaac Sim / Isaac Lab use meters.

The dialog must show:

```
Select scale (root file metersPerUnit):

Please note!
- Isaac Sim and Isaac Lab have a default scene scale of 1 meter
- Omniverse Composer has a default scale of 1 centimeter

  [1] (Composer default)		  -> Centimeters (cm)	– metersPerUnit = 0.01 [default]

  [2] (IsaacSim / Lab default)		  -> Meters (m)	– metersPerUnit = 1.0

  [3] (are you nuts? / special interest!) -> Millimeters (mm)	– metersPerUnit = 0.001

Special Note:
The starter cube, ground, lights, and camera guides are authored in the selected stage
unit so their physical size stays consistent across meters, centimeters, and millimeters.

Omniverse may still show transform scale as 1 because scale is a multiplier on the authored
geometry, not the same thing as the stage unit. Debug physical size via metersPerUnit plus
authored point/translate values, not by xformOp:scale alone.

Enter choice (1–3, default: 1 = Centimeters):
```

**Confirmation:** After the user enters 1, 2, or 3, require them to type the unit suffix (`cm`, `m`, or `mm`) to confirm, or `q` to choose again. This ensures deliberate scale choice (important for Composer vs Isaac Sim/Lab).

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
4. `./035_RUNTIME_LYR/RUNTIME_LYR.usda` – Runtime/session-backed live state and snapshots
5. `./030_SIM_LYR/SIM_LYR.usda` – Simulation results
6. `./040_DATA_LYRs/DATA_LYRs.usda` – Static data/metadata
7. `./020_BASE_LYR/ACTGR_LYR.usda` – Action Graphs
8. `./020_BASE_LYR/ANIM_LYR.usda` – Animation
9. `./020_BASE_LYR/VAR_LYR.usda` – Variants
10. `./020_BASE_LYR/MTL_LYR.usda` – Materials
11. `./020_BASE_LYR/PHY_LYR.usda` – Physics simulation
12. `./020_BASE_LYR/ASS_LYR.usda` – Assets (weakest)

---

## Script Features

1. **Standalone operation:** No external dependencies (Python standard library only)
2. **Version flag:** `--version` or `-v` prints version and exits
3. **Target directory:** Optional CLI argument, defaults to current directory
4. **Script folder detection:** If run from scripts folder, creates project in parent
5. **Non-empty directory warning:** Asks for confirmation before proceeding
6. **Wrapper scripts:** Include `.bat` (Windows CMD) and `.ps1` (PowerShell) wrappers
7. **Asset package convention:** Generate `010_ASS_USD/USD_Wrappers/_asset_package_template/{layers,payloads,data}` and keep this convention aligned with README.md and ComfyUI bootstrap contract policy.

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

**ZIP naming:** `USD_GoodStart_Setup_Standalone_v{X.Y.Z}.zip` (e.g. `USD_GoodStart_Setup_Standalone_v0.9.5.2.zip`)

**When to regenerate:** After any change to the setup script or the files above, regenerate the zip and update the version in `VERSION` and `setup_usd_project.py` (`__version__`). Update the README link to the new zip (e.g. `scripts/USD_GoodStart_Setup_Standalone_v0.9.5.2.zip`).

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

- **0.9.5.3** - Adds `USD_Wrappers` asset-package template plus `_contracts`, `_pipeline_reports`, and `_comfyui_workflows` to the generated baseline.

- **0.9.5.2** – Patch release after generated-package content change: consistent physical starter-scene scaling across m/cm/mm, regenerated standalone zip with new filename. Zip: `USD_GoodStart_Setup_Standalone_v0.9.5.2.zip`
- **0.9.5.1** – Scale dialog: Composer/Isaac Sim/Lab labels, default Centimeters, physical starter-scene scaling across m/cm/mm, double-confirm (type cm/m/mm). Superseded by `0.9.5.2` because the package content changed after the original filename was published.
- **0.9.4** – (previous)
- **0.9.3** – Custom default prim name, root file renamed to `{DefaultPrim}_{scale}_ROOT.usda`
- **0.9.2** – Added PHY_LYR.usda, fixed README templates
- **0.9.1** – Added missing subfolders (MatLib, tex, Envs)
- **0.9.0** – Initial rewrite with scale selection, minimal sublayers, embedded root template

---

*This prompt can be used to regenerate or modify the setup script. Reference the actual USD files in the repo for exact content.*
