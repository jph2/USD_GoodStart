---
arys_schema_version: '1.2'
id: 7d4b3c3a-97e6-4b98-bd20-6f1c0b9e7a1d
title: 035_RUNTIME_LYR
type: TECHNICAL
status: active
trust_level: 2
visibility: internal
created: '2026-06-26T00:00:00Z'
last_modified: '2026-06-26T00:00:00Z'
---

**Version**: 1.0.0 | **Date**: 26.06.2026 | **GlobalID**: 20260626_RUNTIME_LYR

**Tag block:**
#framework_integration #layers #runtime #mqtt #telemetry #session_layer #digital_twin #openusd #usd_goodstart

# 035_RUNTIME_LYR

**Purpose:** Runtime/session-backed layer slot for live digital twin state such as MQTT, OPC UA, or other shopfloor telemetry.

Use this layer boundary for:

- latest-value transform, visibility, variant, or scalar opinions driven by runtime bindings
- operator-triggered runtime snapshots when a live state must be persisted
- replay or evidence layers that should stay separate from static metadata

Do **not** use this layer for:

- static CAD/Revit/PLM/AAS metadata; use `040_DATA_LYRs/`
- raw high-frequency telemetry history; keep that in the broker, historian, database, or explicit snapshot artifacts
- base geometry, materials, physics setup, or asset imports

Recommended workflow:

1. Keep live telemetry in an application session layer or runtime signal store by default.
2. Use `RUNTIME_LYR.usda` only when a persistent runtime opinion or snapshot is intentionally needed.
3. Promote stable identifiers and static metadata into `040_DATA_LYRs/`; let runtime bindings resolve targets from those IDs.

See the main README.md for detailed usage instructions.
