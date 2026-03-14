---
arys_schema_version: '1.2'
id: a67f51c8-30ef-44d8-a769-67345672d8f1
title: 020_BASE_LYR
type: TECHNICAL
status: active
trust_level: 2
created: '2026-02-18T14:17:18Z'
last_modified: '2026-02-18T14:17:18Z'
---

**Version**: 1.0.0 | **Date**: 16.02.2026 | **Time**: 12:00 | **GlobalID**: 20260216_1200_USD_GoodStart_batch

**Tag block:**
#framework_integration #layers #opinions #import #material #variant #animation #usda #reference #payloads #camera #materials #openusd #workflow_automation #best_practices #usd_core #references #analysis #variants #composition

# 020_BASE_LYR

**Purpose:** Base USD layers that define the scene's visual, interactive, and structural setup. These live *above* the raw asset geometry (`ASS_LYR`) and *below* external simulation results (`030_SIM_LYR`).

| File | Content |
|------|---------|
| `ACTGR_LYR.usda` | Action Graphs (OmniGraph logic) |
| `ANIM_LYR.usda` | Animation tracks & keyframes |
| `ASS_LYR.usda` | Asset import (references & payloads to `010_ASS_USD/`) |
| `CAM_LYR.usda` | Cameras |
| `ENV_LYR.usda` | Environment & lighting |
| `MTL_LYR.usda` | Material libraries & local material bindings |
| `OPIN_LYR.usda` | Manual artist overrides (strongest opinions) |
| `PHY_LYR.usda` | Physics *setup* -- collision shapes, rigid body flags, mass properties (not sim results) |
| `VAR_LYR.usda` | Variant sets & configurations |

See the main README.md for detailed usage instructions.
