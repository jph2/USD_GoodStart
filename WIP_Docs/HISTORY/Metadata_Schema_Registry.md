---
arys_schema_version: '1.2'
id: e9af14d1-09d9-4ea7-becb-43204248a8b0
title: Metadata & Schema Registry (Template)
type: PRACTICAL
status: active
trust_level: 2
visibility: internal
created: '2025-12-11T21:05:19Z'
last_modified: '2025-12-11T21:05:19Z'
---

# Metadata & Schema Registry (Template)

**Purpose:** A lightweight, human-readable registry of what metadata we write into USD, where it lives (which layer/folder), and how it is sourced (authoring vs runtime).

This document exists to prevent “attribute sprawl”: inconsistent prefixes, duplicated meanings, and brittle integrations across teams and tools.

---

## 1) Quick Rules

- **Prefer existing USD schemas first** (e.g. `UsdGeom`, `UsdShade`, `UsdPhysics`). If USD already defines a concept, use it.
- **Use namespaced custom attributes for prototyping** (fast, flexible): `domain:subsystem:property`
- **Promote stable data models to schemas** only when multiple tools/teams need validation, UI, and introspection.
- **Do not duplicate backend truth**: USD should reference backend IDs/links; the backend stores the authoritative business data.
- **Document every new prefix** in this registry before using it broadly.

---

## 2) Prefix Registry

| Prefix | Meaning | Example Properties | Source of Truth | Layer / Folder | Notes |
|--------|---------|-------------------|-----------------|----------------|-------|
| `plm:` | PLM identifiers/links | `plm:id`, `plm:rev`, `plm:url` | PLM/PDM | `060_METADATA_LYR/` | IDs only; no duplicated BOM tables in USD |
| `erp:` | ERP references | `erp:materialId` | ERP | `060_METADATA_LYR/` | Keep minimal |
| `aas:` | Asset Administration Shell mapping | `aas:submodel:identification` | AAS backend | `060_METADATA_LYR/` | Prefer mapping keys; avoid full payload duplication |
| `opcua:` | OPC UA runtime / info-model mapping | `opcua:nodeId`, `opcua:runtime:temperature` | OPC UA server | `060_METADATA_LYR/` (mapping) + runtime adapter | Runtime values should be written at runtime, not baked |
| `catena:` | Catena-X mapping | `catena:dpp:id` | Catena-X/DPP | `060_METADATA_LYR/` | Align with your Catena-X profile |
| `dpp:` | Digital Product Passport fields | `dpp:productId`, `dpp:co2e` | DPP system | `060_METADATA_LYR/` | Keep as references/links where possible |

Add your project-specific prefixes here.

---

## 3) Attribute Registry (Concrete Fields)

Add rows for each concrete attribute you rely on.

| Attribute | Type | Applied To | Meaning | Authoring vs Runtime | Layer / Folder | Validation / Constraints |
|----------|------|------------|---------|----------------------|----------------|--------------------------|
| `plm:id` | `string` | Components/Assets | PLM master id | Authoring | `060_METADATA_LYR/` | Non-empty |
| `opcua:nodeId` | `string` | Sensors/Actuators | OPC UA node mapping | Authoring | `060_METADATA_LYR/` | Must be resolvable in target OPC UA server |
| `opcua:runtime:temperature` | `float` | Sensors | Live temperature | Runtime | Runtime adapter | Units documented; update rate documented |

---

## 4) Where It Lives (Layering Strategy)

- **Authoring mappings** (IDs, links, schema-ish static data): `060_METADATA_LYR/*.usda`
- **Runtime values** (telemetry, commands, state): written by Kit extension / ActionGraph / ROS2 bridge at runtime
- **Simulation logic** (physics, sensors, articulations): `040_SIM_LYR/*.usda`
- **Variants/configurations** (static configuration logic): `050_VARIANTS_LYR/*.usda`
- **Visual/material/layout edits**: `030_USD_LYR/*.usda`

---

## 5) Schema Promotion Checklist (When to create a USD schema)

Create a schema only when most are true:
- Multiple teams/tools consume the data
- You need validation and stable contracts
- You need editor/UI integration
- You need programmatic discovery (e.g., “find all prims with this API schema applied”)

If you create a schema:
- Document it here (name, version, plugin location, migration plan)
- Coordinate with AOUSD if you aim for broader interoperability


