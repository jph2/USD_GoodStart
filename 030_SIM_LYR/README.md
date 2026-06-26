---
arys_schema_version: '1.2'
id: 7fca2858-e6e5-4388-aaf7-cfa2b0a67935
title: 030_SIM_LYR
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-02-18T14:17:04Z'
last_modified: '2026-02-18T14:17:04Z'
---

**Version**: 1.0.0 | **Date**: 16.02.2026 | **Time**: 12:00 | **GlobalID**: 20260216_1200_USD_GoodStart_batch

**Tag block:**
#framework_integration #simulation #layers #stage #construction #openusd #workflow_automation #best_practices #usd_core #composition #deterministic_workflows #usd_start_point #usd_goodstart

# 030_SIM_LYR

**Purpose:** External simulation result overlays (CFD, FEA, Isaac Sim, Ansys). These layers carry *outputs* from simulation tools -- stress maps, thermal fields, deformation caches, replayable simulation outputs -- layered on top of the base asset via `over` opinions.

They do **not** define physics setup (collision shapes, rigid bodies); that lives in `020_BASE_LYR/PHY_LYR.usda`.

They also do **not** carry raw live shopfloor telemetry by default. Latest-value MQTT/OPC UA runtime state belongs in the application session/runtime system or the `035_RUNTIME_LYR/` snapshot slot when persistence is intentional.

See the main README.md for detailed usage instructions.
