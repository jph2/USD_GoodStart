# 010_ASS_USD

**Version:** 0.9.0-beta  
**Last Updated:** 11.21.2025

## Purpose

This folder contains **all USD assets** for the project. These are the converted, render-ready USD files that serve as the building blocks for your scene.

## Default Assets

The following default assets are included:

- `0_CUBE.usda` - Default cube geometry
- `0_Geo_Shader_Ball.usd` - Geoshader ball asset
- `0_Geo_Shader_Ball_Env.usd` - Geoshader environment asset

The `0_` prefix is used for sorting purposes and to distinguish default assets from project-specific assets.

## Usage

### Adding New Assets

- **All other assets** should be placed in this folder
- **Existing USD exports** from other programs should be placed here
  - **Full USD support** (Maya, Houdini, 3ds Max): Can export with full composition support
  - **Limited support** (Blender, Cinema 4D): Can only create endpoint assets (see DCC Tool Limitations below)
- Even if DCC programs are not fully USD-capable, they can still be used as export endpoints, but with limitations

### Asset Sources

Assets in this folder typically come from:

1. **DCC Tool Exports**: Direct USD exports from DCC tools
   - **Full USD support** (Maya, Houdini, 3ds Max): Can export with full composition support
   - **Limited support** (Blender, Cinema 4D): Can only create endpoint assets (see DCC Tool Limitations below)
2. **CAD Conversion**: Converted CAD files (JT, CATIA, Rhino, STEP, etc.) from `000_SOURCE/` or external systems
3. **USD Creation**: Assets created directly in USD format

### DCC Tool Limitations

**Important**: Not all DCC tools support USD's composition features:

**Blender, Cinema 4D, and Similar Tools:**
- ✅ Can **read and write** USD files (`.usd`, `.usda`, `.usdc` formats)
- ❌ **Do NOT support** USD's core composition features:
  - No layering support (cannot work with sublayers)
  - No referencing support (cannot create or maintain references)
  - No composition arcs (LIVRPS) support
  - No non-destructive workflows
- ⚠️ **Work destructively** - These tools modify USD files directly without preserving composition structure
- 📍 **Use case**: Can only be used to create **"endpoint" assets** (the lowest sublayer - the asset itself)
- ❌ **Cannot be used** for modifying layers on top of assets or working with USD's composition system  + **they may break the references for the layers on top of them!!!!**

**Why This Matters:**
- The difference between exporting USD from Blender/C4D vs. exporting FBX/Alembic/OBJ is **minimal** - they're essentially export endpoints
- For USD workflows requiring **layering, referencing, or non-destructive editing**, use **Maya, Houdini, or 3ds Max** instead
- Blender/C4D are suitable for creating base assets but **cannot participate in USD's composition workflows**

**Recommendation:**
- Use **Maya, Houdini, or 3ds Max** for USD workflows that require:
  - Layer-based modifications
  - Asset referencing
  - Non-destructive editing
  - Composition arcs (variants, payloads, inherits, etc.)
- Use **Blender/C4D** only for creating final export assets that will be referenced by other USD files

### CAD to USD Conversion Pipeline

When working with CAD files, the conversion workflow is:

1. **Source Files**: CAD files stored in `000_SOURCE/` or external systems (PLM/PDM/ERP)
2. **Conversion Path**: Convert via defined pipeline (possibly using STEP as intermediate format)
3. **USD Export**: Converted USD files placed in `010_ASS_USD/`

#### CAD Conversion Resources

The USD study group has created conversion scripts and resources:

- **[CAD-to-OpenUSD Repository](https://github.com/nAurava-Technologies/CAD-to-OpenUSD)** - Conversion scripts for CAD to OpenUSD conversion (Work in Progress as of November 25, 2024)
  - Contains Python scripts for converting CAD files to USD format
  - Includes example STEP file conversion workflows
  - Provides a foundation for building custom CAD conversion pipelines

### Connectors vs. Stable Conversion

- **Live Links**: Some connectors exist for live links with CAD systems, but these may not provide stable, long-term connections
- **Stable Connections**: For production workflows, **convert to USD** rather than relying solely on live connectors. This ensures:
  - Stable file references
  - Version independence
  - Better performance
  - Cross-platform compatibility

### Asset Modification Workflow

If an asset needs to be modified or have layers/opinions applied:

1. **Option 1: Add a layer folder**
   - Create a subfolder within this asset's directory to handle layers and modifications

2. **Option 2: Create a new asset folder**
   - Create a completely new folder for the asset
   - This allows you to handle the asset with its changes, opinions, and layers separately
   - Create a new root file that:
     - Holds the asset
     - Contains opinions on top of the base asset
   - **Link this root file to the master file** (`GoodStart_ROOT.usda`)

### Complex Assets with DCC Starting Points

For complex assets that require significant modifications and layering:

- **DCC File as Starting Point**: Complex assets may have a DCC file (e.g., Houdini `.hiplc`) as the starting point
- **Example Structure**: `Complex_Asset_that_got_changed_and_Layered/`
  - Contains the Houdini file (or other DCC file) that serves as the working file
  - Contains USD files that reference or are derived from the DCC file
  - Contains layer files for modifications and opinions
  - The DCC file allows artists to work in their preferred tool while maintaining USD as the source of truth
- **Workflow**: 
  1. Start with DCC file (e.g., Houdini) in the asset folder
  2. Export or reference USD from the DCC file
  3. Apply layers and modifications through `020_LYR_USD/` or asset-specific layer folders
  4. Link the final asset to the master file (`GoodStart_ROOT.usda`)

### Non-Destructive Workflows

USD enables non-destructive workflows through composition arcs:
- **References**: Lightweight scene composition
- **Payloads**: Heavy geometry or data (loaded on demand)
- **Variants**: Different versions of the same asset
- **Layers**: Modifications and opinions applied through `020_LYR_USD/` layers

## Metadata and Data Integration

When working with USD assets:

1. **Metadata Extraction**: Assets should include relevant metadata extracted from source files
2. **Data Source Connections**: Define how assets connect to other data sources (databases, APIs, etc.)
3. **USD Metadata**: Write appropriate metadata into the USD file structure
4. **Asset Administration Shell (AAS)**: Connect assets to **Asset Administration Shell (AAS)**, also known as Verwaltungsschale, for digital twin administration and lifecycle management

### Schema Standards

**Before creating custom schemas for assets:**

1. **Review Existing Schemas**: Familiarize yourself with schemas defined by the **[Alliance for OpenUSD (AOUSD)](https://aousd.org/)**
2. **Research Industry Schemas**: Look at what other organizations and projects are using
3. **Coordinate with AOUSD**: If introducing new schemas, **coordinate with the AOUSD group** to ensure they fit into the bigger picture and align with industry standards
4. **Documentation**: Document any custom schemas and their relationship to standard schemas

## Version Control and File Naming

### Best Practices

1. **Use Stable Paths**: Use **stable file names/paths** as endpoints rather than version numbers in filenames (avoid `version1`, `version2`, `final`, etc.)
   - CAD systems typically have version control embedded in PLM/PDM/ERP systems
   - Let the version control system handle versioning, not the filename

2. **System Integration**: Link USD assets to PLM/PDM/ERP systems so that the **administration layer is handled by these systems**

3. **Version Control Tools**: If no version control system exists:
   - **Introduce version control** in your USD workflow
   - For design and DCC teams, consider tools like **[Anchorpoint](https://www.anchorpoint.app/)**, a Git-based version control solution designed for artists:
     - **Git with binary support**: No repository limits, works with TB-sized projects
     - **Made for artists**: Simple interface, fail-safe operations
     - **File locking**: Prevents team members from overwriting assets
     - **Art asset management**: Review, approve, and organize assets
     - **Selective checkout**: Download only what you need from large repositories
     - **DCC integration**: Supports Blender, ZBrush, Photoshop, Substance, and other DCC tools
     - **Python API**: Automate asset workflows with Python-based actions
     - **Git server compatibility**: Works with GitHub, GitLab, Azure DevOps, Gitea, and others

## Digital Twin Ready Organization

Assets should be organized to be **always ready for digital twin use**:

- Assets should be in a state where they can be loaded and used in digital twin applications immediately
- Even if initially empty or minimal, the structure should be complete
- Over time, assets will be populated with full geometry, materials, metadata, and connections to external data sources
- This ensures assets are always ready for digital twin integration, visualization, and analysis
- Assets should maintain connections to source CAD systems, PLM/PDM/ERP systems, and Asset Administration Shell (AAS) where applicable

## Texture Organization

- Individual assets may have their own `textures` folder within their asset directory
- Global textures are stored in `030_TEX/` at the project root
- Use asset-specific textures when textures are only used by that asset
- Use global textures when textures are shared across multiple assets

## Naming Convention

- Use descriptive names for assets
- The `0_` prefix is reserved for default/sorting purposes
- Keep asset names consistent and clear
- Avoid version numbers in filenames - let version control handle versioning

## Workflow Integration

The typical workflow for assets:

1. **Source**: Original files in `000_SOURCE/` or external systems
2. **Conversion**: Convert to USD via defined pipeline
3. **Placement**: Place converted USD files in `010_ASS_USD/`
4. **Metadata Mapping**: Map source metadata to USD metadata and connect to external data sources
5. **Layer Management**: Use `020_LYR_USD/` layers to add modifications and opinions
6. **Root Integration**: Reference assets in `GoodStart_ROOT.usda` or through layer files
7. **AAS Integration**: Connect assets to Asset Administration Shell for digital twin management

**Important: Use Relative Paths**

When referencing assets from layer files, always use **relative paths**:
- ✅ `@../010_ASS_USD/asset.usd@` - Correct relative path from layer file
- ❌ `@C:/Projects/USD_GoodStart/010_ASS_USD/asset.usd@` - Wrong absolute path (breaks when project is moved)
- See main README "Path Best Practices" section for detailed guidance

## Learning from VFX Industry

While OpenUSD was originally developed for rendering in VFX, its proven practices translate excellently to digital twin applications:

- **Large-scale production pipelines** - VFX workflows scale to hundreds of artists, similar to large digital twin projects
- **Non-destructive workflows** - USD composition arcs enable non-destructive modifications perfect for digital twin iterations
- **Version control** - VFX asset management practices work well for digital twin versioning
- **Multi-DCC workflows** - Different tools working on the same assets mirrors multi-disciplinary digital twin teams
- **Structured organization** - VFX asset organization ensures digital twin assets are always ready for use

**Digital Twin Adaptation**: While VFX focuses on render-ready assets, digital twins focus on:
- **Data integration** - Connecting to PLM/PDM/ERP systems and AAS
- **Metadata richness** - Capturing real-world asset information
- **Stable references** - Maintaining connections to source CAD systems
- **Lifecycle management** - Tracking asset changes over time

Consider reviewing the **[USDWG Collective Project 001](https://github.com/usd-wg/collectiveproject001)** repository for examples of asset organization and workflow best practices that can be adapted for digital twins.



