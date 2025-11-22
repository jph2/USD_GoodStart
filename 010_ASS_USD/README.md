# 010_ASS_USD

**Version:** 0.9.2-beta  
**Last Updated:** 11.22.2025

## Purpose

This folder contains **all USD assets** for the project. These are the converted, render-ready USD files that serve as the building blocks for your scene.

## Default Assets

- `0_CUBE.usda` - Default cube geometry
- `0_Geo_Shader_Ball.usd` - Geoshader ball asset
- `0_Geo_Shader_Ball_Env.usd` - Geoshader environment asset

The `0_` prefix is used for sorting purposes and to distinguish default assets from project-specific assets.

## Usage

### Adding New Assets

Place all USD assets in this folder:
- USD exports from DCC tools (Maya, Houdini, 3ds Max, Blender, Cinema 4D)
- Converted CAD files (JT, CATIA, Rhino, STEP, etc.)
- Assets created directly in USD format

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

### Complex Assets

For complex assets with DCC starting points:
- Store DCC files (e.g., Houdini `.hiplc`) in the asset folder
- Export USD from the DCC file
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
- Global textures are stored in `030_TEX/` at project root
- Use asset-specific textures when only used by that asset
- Use global textures when shared across multiple assets

## Naming Convention

- Use descriptive names for assets
- `0_` prefix reserved for default/sorting purposes
- Avoid version numbers in filenames - let version control handle versioning

## Workflow

1. Source files in `000_SOURCE/` or external systems
2. Convert to USD via pipeline
3. Place in `010_ASS_USD/`
4. Map metadata and connect to external data sources
5. Use `020_LYR_USD/` layers for modifications
6. Reference in `GoodStart_ROOT.usda` or layer files

**Always use relative paths** when referencing assets from layer files (e.g., `@../010_ASS_USD/asset.usd@`).
