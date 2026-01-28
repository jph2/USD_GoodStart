# 060_LYR_METADATA

**Version:** 0.9.4-beta
**Last Updated:** 12.12.2025

## Purpose

This folder contains **metadata-focused USD layer files**.  
Use it to attach **enterprise and digital-twin metadata** to assets without touching geometry, materials, or simulation.

Typical metadata includes:

- PLM / PDM / ERP identifiers  
- CAD metadata (part numbers, materials, revisions)  
- Digital twin standards (AAS, OPC UA, Catena-X, etc.)  
- IoT runtime metadata (sensor status, last values)  
- Documentation links and annotations

## Typical Layers

- `Metadata_LYR.usda` – General metadata (PLM/CAD/ERP, digitalTwin IDs)  
- `AAS_LYR.usda` – Asset Administration Shell (AAS) mappings  
- `OPCUA_LYR.usda` – OPC UA runtime values  
- `CatenaX_LYR.usda` – Catena-X specific metadata

These follow the patterns described in Chapter 10 (Metadata Strategy) and the standards integration examples.

## Usage

1. Create a new `.usda` file in this folder with a descriptive name ending in `_LYR`.
2. Use `over` prims to attach metadata to existing prims loaded from lower layers (e.g., from `010_ASS_USD/` via `030_LYR_USD/AssetImport_LYR.usda`).
3. Add the metadata layer to the `subLayers` array in `Asset_ROOT.usda` / `GoodStart_ROOT.usda`:
   - Typically **above** `030_LYR_USD/AssetImport_LYR.usda` but **below** strong visual/opinion layers.
4. Author metadata using:
   - **Custom attributes** (e.g., `plm:id`, `cad:partNumber`, `digitalTwin:assetId`), and/or
   - **`customData` dictionaries** for descriptive/archival info.

## Best Practices

- Keep metadata and standards logic separate from:
  - Geometry payloads (`010_ASS_USD/`),
  - General visual layers (`030_LYR_USD/`),
  - Simulation (`040_LYR_SIM/`),
  - Variants (`050_LYR_VARIANTS/`).
- Use clear namespaces (e.g., `plm:*`, `cad:*`, `erp:*`, `aas:*`, `opcua:*`, `dt:*`, `semantic:*`).
- Follow the recommendations from:
  - [USD Custom Data & Namespaces](https://graphics.pixar.com/usd/release/api/usd_page_front.html#Usd_Page_CustomData)
  - [Learn OpenUSD — Metadata](https://docs.nvidia.com/learn-openusd/latest/stage-setting/metadata.html)
  - [Assembling Digital Twins — Asset Metadata Review](https://docs.nvidia.com/learning/physical-ai/assembling-digital-twins/latest/getting-started/asset-metadata-review.html)
- Keep layers **modular** by domain (e.g., separate AAS and OPC UA layers) to enable enable/disable and override patterns.
- Always use **relative paths** when referencing assets from this folder.


