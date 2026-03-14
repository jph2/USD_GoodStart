---
arys_schema_version: '1.2'
id: 203ee757-b6c1-41cd-86dc-2a6256eef9d5
title: 010_ASS_USD
type: TECHNICAL
status: active
trust_level: 2
created: '2025-12-12T00:33:52Z'
last_modified: '2025-12-12T00:33:52Z'
---

# 010_ASS_USD

**Version:** 0.9.4-beta
**Last Updated:** 12.12.2025

## Purpose

This folder contains **all USD assets** for the project. These are the converted, render-ready USD files that serve as the building blocks for your scene.

## Folder Structure

- **`geo/`** - Geometry assets (USD files containing geometry, meshes, and 3D models)
- **`mat/`** - Material libraries (MaterialX files, USD material definitions, and shader networks)
- **Root level** - DCC source files (Houdini `.hiplc` files, etc.) that generate USD assets

## Default Assets

**Geometry (`geo/` folder):**
- `0_CUBE_GEO.usda` - Default cube geometry
- `0_Shader_Ball_GEO.usd` - Geoshader ball asset

**Note:** The `0_` prefix is used for sorting purposes and to distinguish default assets from project-specific assets.

## Usage

### Adding New Assets

**Geometry Assets (`geo/` folder):**
- USD geometry exports from DCC tools (Maya, Houdini, 3ds Max, Blender, Cinema 4D)
- Converted CAD files (JT, CATIA, Rhino, STEP, etc.)
- Geometry assets created directly in USD format

**Material Libraries (`mat/` folder):**
- MaterialX files wrapped in USD format (MaterialX content inside USD files)
- USD material definitions and shader networks
- Material libraries exported from DCC tools
- **Houdini**: Can generate MaterialX files wrapped in USD (`.hiplc` files in root can export to `mat/`)
- **Other applications**: MaterialX files from other sources (testing recommended)
- **Note**: Compatibility with pure MaterialX files (`.mtlx` standalone format) has **not been tested**. Only MaterialX content wrapped inside USD files has been tested and verified.

### Asset Sources

Assets typically come from:
1. **DCC Tool Exports**: Direct USD exports from DCC tools
2. **CAD Conversion**: Converted CAD files from `000_SOURCE/` or external systems (PLM/PDM/ERP)
3. **USD Creation**: Assets created directly in USD format

### CAD to USD Conversion

Workflow:
1. Source files in `000_SOURCE/` or external systems
2. Convert via defined pipeline
3. Place converted USD files in `010_ASS_USD/`

**CAD Conversion Resources:**
- [CAD-to-OpenUSD Repository](https://github.com/nAurava-Technologies/CAD-to-OpenUSD) - Conversion scripts (Work in Progress)

### Asset Modification Workflow

If an asset needs modifications or layers:
- **Option 1**: Create a subfolder within the asset directory for layers
- **Option 2**: Create a new asset folder with its own root file and link to `GoodStart_ROOT.usda`

### Material Library Generation

**Houdini Workflow:**
- Store Houdini `.hiplc` files in the root of `010_ASS_USD/` (e.g., `MatLib_a.hiplc`)
- Houdini can generate MaterialX content wrapped in USD format and export them to the `mat/` folder
- MaterialX content is always wrapped inside USD files (not standalone `.mtlx` format)
- **Note**: Omniverse is compatible with MaterialX files, but creating good, clean MaterialX files directly in Omniverse currently lacks a polished UI/UX. Creating MaterialX files in Houdini is a valid and recommended option for material library generation.

**Other DCC Applications:**
- **Maya and 3ds Max**: Creating MaterialX files in Maya or Max is also a valid option
- **Cinema 4D and other DCCs**: Exporting MaterialX files from Cinema 4D and other DCC tools has **not been tested** in this project
- MaterialX content from DCC tools should be wrapped in USD format
- **Testing recommended** - Verify compatibility and workflow with your specific tools if using untested DCC applications
- Place generated MaterialX-wrapped USD files in the `mat/` folder
- **Important**: Pure MaterialX files (`.mtlx` standalone format) have **not been tested**. Only MaterialX content inside USD files has been verified.

### Complex Assets

For complex assets with DCC starting points:
- Store DCC files (e.g., Houdini `.hiplc`) in the root of `010_ASS_USD/` or asset-specific folders
- Export geometry USD files to `geo/` folder
- Export material libraries to `mat/` folder
- Apply layers through `020_LYR_USD/` or asset-specific layer folders

## Metadata and Data Integration

- Extract metadata from source files
- Connect to external data sources (databases, APIs)
- Write metadata into USD file structure
- Connect to Asset Administration Shell (AAS) for digital twin management

### Schema Standards

Before creating custom schemas:
1. Review existing schemas from [Alliance for OpenUSD (AOUSD)](https://aousd.org/)
2. Research industry schemas
3. Coordinate with AOUSD if introducing new schemas
4. Document custom schemas and their relationship to standards

## Texture Organization

- Individual assets may have their own `textures` folder
- Global textures are stored in `020_TEX/` at project root
- Use asset-specific textures when only used by that asset
- Use global textures when shared across multiple assets

## Naming Convention

- Use descriptive names for assets
- `0_` prefix reserved for default/sorting purposes
- Avoid version numbers in filenames - let version control handle versioning

## Workflow

**Geometry Assets:**
1. Source files in `000_SOURCE/` or external systems
2. Convert to USD via pipeline
3. Place geometry USD files in `geo/` folder
4. Map metadata and connect to external data sources
5. Use `020_LYR_USD/` layers for modifications
6. Reference in `GoodStart_ROOT.usda` or layer files

**Material Libraries:**
1. Generate MaterialX files using Houdini (`.hiplc` files in root) or other DCC tools
2. Export MaterialX files to `mat/` folder
3. Reference materials in USD assets or layer files
4. Test compatibility if using non-Houdini sources

**Path Examples:**
- Geometry: `@../010_ASS_USD/geo/asset.usd@`
- Materials: `@../010_ASS_USD/mat/material_library.usda@`

**Always use relative paths** when referencing assets from layer files.
