# 030_TEX

## Purpose

This folder contains **global texture files** used across the project.

## Usage

- Place texture files here that are used **globally** across multiple assets
- These textures are accessible from anywhere in the project
- Use relative paths or absolute paths to reference these textures in USD files

## Asset-Specific Textures

- Individual assets in `010_ASS_USD/` may have their own `textures` folder
- Use asset-specific texture folders when textures are only used by that specific asset
- Use this global folder when textures are shared across multiple assets

## Organization

Consider organizing textures by:
- **Type**: Diffuse, Normal, Roughness, etc.
- **Category**: Materials, Environments, etc.
- **Project**: If working on multiple projects

## Best Practices

- **Keep texture names descriptive** - Use clear naming conventions
- **Document texture sources** - Note where textures come from
- **Maintain texture versions** - Consider versioning if textures change frequently
- **Use appropriate formats** - USD supports various texture formats (PNG, EXR, etc.)
- **Consider color space** - Document color space requirements (sRGB, linear, etc.)

## Texture References in USD

Textures are typically referenced in USD material definitions:

```usda
asset inputs:diffuse_texture = @../030_TEX/texture_name.png@ (
    colorSpace = "sRGB"
)
```

## Working with Nucleus Server

**Nucleus Server** (Omniverse Nucleus) provides many advantages for collaborative USD workflows, including:
- Centralized asset management
- Real-time collaboration
- Version control and synchronization
- Multi-user access

### Texture Source Files Limitation

However, **Nucleus Server has limitations when working with texture source files**:

- **Difficult to store source files** - Files like Photoshop (`.psd`), Substance Designer (`.sbsar`), Substance Painter (`.spp`), and other DCC source formats can be challenging to work with on Nucleus Server
- **Workflow considerations** - These source files may not integrate well with Nucleus Server's file management system

### Recommended Workflow

When working with Nucleus Server and texture sources:

1. **Store final textures on Nucleus** - Place final exported texture files (PNG, EXR, etc.) in Nucleus Server for use in USD files
2. **Keep source files locally or on alternative storage** - Store Photoshop, Substance, and other source files in:
   - Local file systems
   - Network drives (NAS)
   - Version control systems (like Anchorpoint) that handle binary files well
   - Cloud storage solutions (Google Drive, Dropbox) for non-versioned source files
3. **Export workflow** - Export final textures from source files to formats compatible with Nucleus Server
4. **Documentation** - Document where source files are stored and how to access them for updates

### Hybrid Approach

Consider a **hybrid approach**:
- **Nucleus Server**: Final USD files and exported textures (PNG, EXR, etc.)
- **Alternative Storage**: Source files (`.psd`, `.sbsar`, `.spp`, etc.) stored separately
- **Version Control**: Use tools like Anchorpoint or Git LFS for source file versioning if needed

This approach leverages Nucleus Server's strengths while avoiding its limitations with source file formats.

