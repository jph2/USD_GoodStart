# 050_LYR_VARIANTS

**Version:** 0.9.3-beta  
**Last Updated:** 10.12.2025

## Purpose

This folder contains **USD layer files dedicated to variants and configuration logic**.  
Use it to organize:

- LOD choices,
- Product options (e.g., Motor_A vs Motor_B),
- Tooling / attachment choices,
- Damage states, color themes, and other **discrete states**.

## Typical Layers

- `Variant_LYR.usda` – Scene-level variant sets and selections  
- `Config_LYR.usda` – Mappings from PLM/3DEXPERIENCE/Configurator options to USD variants  
- `LOD_LYR.usda` – LOD variant sets for performance control

> Asset-local variants (inside `Asset_ROOT.usda` for a specific asset) are still valid.  
> `050_LYR_VARIANTS/` is for **scene or cross-asset variant logic** layered on top.

## Usage

1. Create a new `.usda` file in this folder with a descriptive name ending in `_LYR`.
2. Author `variantSet` definitions and variant selections at the prims you want to control.
3. Add the new layer to the `subLayers` array in `Asset_ROOT.usda` / `GoodStart_ROOT.usda`:
   - Above `030_LYR_USD/Mtl_work_LYR.usda` and `030_LYR_USD/AssetImport_LYR.usda`.
4. Keep variants **lofted above payloads** where possible (see Chapter 2 and 5 of the Best Practices Guide).

## Best Practices

- Use variants for **discrete choices** (A/B/C), not for continuously changing values (use primvars for that).
- Avoid huge variant sets (5–10 options per set is ideal).
- Do not put heavy geometry directly inside variants; reference/payload lighter or pre-baked variant payloads.
- Combine:
  - **Jan’s payload pattern** for heavy geometry (payloads in `010_ASS_USD/`), and
  - **Thomas’s property declaration technique** for variant-driven properties.
- Always use **relative paths** when referencing assets from this folder.


