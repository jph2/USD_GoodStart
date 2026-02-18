**Version**: 1.0.0 | **Date**: 16.02.2026 | **Time**: 12:00 | **GlobalID**: 20260216_1200_USD_GoodStart_batch

**Tag block:**
#framework_integration #simulation #layers #stage #construction #openusd #workflow_automation #best_practices #usd_core #composition #deterministic_workflows #usd_start_point #usd_goodstart

# 030_SIM_LYR

**Purpose:** External simulation result overlays (CFD, FEA, Isaac Sim, Ansys). These layers carry *outputs* from simulation tools -- stress maps, thermal fields, deformation caches -- layered on top of the base asset via `over` opinions. They do **not** define physics setup (collision shapes, rigid bodies); that lives in `020_BASE_LYR/PHY_LYR.usda`.

See the main README.md for detailed usage instructions.
