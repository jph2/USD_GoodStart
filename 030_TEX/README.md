# 030_TEX

**Version:** 0.9.2-beta  
**Last Updated:** 11.22.2025

## Purpose

This folder contains **global texture files** used across the project.

## Usage

- Place texture files here that are used **globally** across multiple assets
- These textures are accessible from anywhere in the project
- Use relative paths to reference textures in USD files

## Asset-Specific vs Global Textures

- **Asset-specific**: Individual assets in `010_ASS_USD/` may have their own `textures` folder
- **Global**: Use `030_TEX/` when textures are shared across multiple assets

## Organization

Consider organizing by:
- **Type**: Diffuse, Normal, Roughness, etc.
- **Category**: Materials, Environments, etc.
- **Project**: If working on multiple projects

## Texture References in USD

```usda
asset inputs:diffuse_texture = @../030_TEX/texture_name.png@ (
    colorSpace = "sRGB"
)
```

**Always use relative paths** (e.g., `@../030_TEX/texture_name.png@`).

## Best Practices

- Keep texture names descriptive
- Document texture sources
- Use appropriate formats (PNG, EXR, etc.)
- Consider color space (sRGB, linear, etc.)

## Nucleus Server Workflow

**Limitation**: Nucleus Server has difficulty storing texture source files (`.psd`, `.sbsar`, `.spp`).

**Recommended approach**:
- Store final textures (PNG, EXR) on Nucleus Server
- Keep source files locally or on alternative storage (NAS, Anchorpoint, Git LFS)
- Export final textures from source files to Nucleus-compatible formats
