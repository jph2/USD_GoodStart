# 020_LYR_USD

## Purpose

This folder contains **USD layer files** that are used to modify and override content in the root file (`GoodStart_ROOT.usda`). 

In digital twin applications, layers enable non-destructive modifications to assets, allowing you to:
- Add digital twin-specific metadata and connections
- Override properties for different digital twin scenarios
- Apply modifications without altering base CAD-converted assets
- Maintain connections to PLM/PDM/ERP systems and Asset Administration Shell (AAS)

## Layer System

USD layers allow you to:
- Override properties and attributes
- Add opinions (changes) to existing prims
- Organize modifications without altering base assets
- Enable collaborative workflows with multiple layers

### USD Composition Arcs: LIVRPS

USD provides six composition arcs (LIVRPS) that work together to create powerful, non-destructive workflows:

- **L** - **Layers** (Sublayers): Stack multiple layers to build up scene descriptions
- **I** - **Inherits**: Inherit properties and structure from other prims
- **V** - **Variants**: Define different versions or configurations of the same asset
- **R** - **References**: Lightweight references to external USD files
- **P** - **Payloads**: Heavy geometry or data loaded on demand
- **S** - **Specializes**: Override specific aspects while inheriting others

**Layers** (this folder) work in combination with the other composition arcs to enable:
- Non-destructive editing workflows
- Collaborative multi-artist pipelines
- Efficient asset organization
- Flexible scene composition

## Current Layers

The following layer files are currently in use:

- `AssetImport_LYR.usda` - Asset import and reference layer
- `Mtl_work_LYR.usda` - Material work and modifications
- `Opinion_xyz_LYR.usda` - General opinion/override layer
- `Variant_LYR.usda` - Variant set definitions and selections

## Usage

### Adding New Layers

1. Create a new `.usda` or `.usd` file with a descriptive name ending in `_LYR`
2. Add the layer to the `subLayers` array in `GoodStart_ROOT.usda`
3. Layer order matters - layers listed later have higher strength (override earlier layers)

### Layer Best Practices

- **Keep layers focused** - Each layer should have a specific purpose
- **Use descriptive names** - Make it clear what each layer modifies
- **Document layer dependencies** - Note if layers depend on each other
- **Test layer combinations** - Ensure layers work together correctly
- **Keep the structure as simple as possible** - Avoid unnecessary complexity when working with layers
- **Do NOT import assets with the Root layer** - Keep the root file (`GoodStart_ROOT.usda`) clean and focused on scene structure
- **Use AssetImport_LYR at the bottom of the stack** - Place asset import layers (like `AssetImport_LYR.usda`) at the bottom of the `subLayers` array so they load first, allowing other layers to override them

## Integration with Root File

All layers in this folder are referenced in `GoodStart_ROOT.usda` via the `subLayers` metadata:

```usda
subLayers = [
    @./020_LYR_USD/Opinion_xyz_LYR.usda@,
    @./020_LYR_USD/Variant_LYR.usda@,
    @./020_LYR_USD/Mtl_work_LYR.usda@,
    @./020_LYR_USD/AssetImport_LYR.usda@
]
```

**Important Layer Ordering Rules:**

- **Asset import layers go at the bottom** - Layers like `AssetImport_LYR.usda` should be placed at the bottom of the `subLayers` array (last in the list)
- **Layer order determines strength** - Layers listed later have higher strength and override earlier layers
- **Root file should NOT import assets** - Keep `GoodStart_ROOT.usda` focused on scene structure and environment; use dedicated import layers instead
- **Bottom-to-top composition** - The layer stack builds from bottom (base assets) to top (modifications and opinions)

## Modifying Assets

When you need to modify assets from `010_ASS_USD/`:

1. Create or modify a layer in this folder
2. Reference the base asset in the layer
3. Add your modifications/opinions
4. The layer will override the base asset when loaded

### Digital Twin Use Cases

Layers are particularly useful for digital twin applications:
- **Scenario variations**: Different configurations or states of the same asset
- **Metadata enrichment**: Adding digital twin-specific metadata without modifying base assets
- **System connections**: Linking assets to external data sources (PLM/PDM/ERP, AAS)
- **Temporal changes**: Representing asset changes over time
- **Multi-disciplinary views**: Different perspectives from various stakeholders (engineering, operations, maintenance)

## Project Planning Considerations

When working with layers in a digital twin project:

### Storage and Version Control

- **Define layer organization rules** before implementation:
  - Which layers go in `020_LYR_USD/` vs. asset-specific layer folders
  - Naming conventions for layer files
  - Version control strategy for layers
  - How layers integrate with PLM/PDM/ERP systems

- **Storage workflows**: If using Nucleus Server or alternative storage:
  - Determine where layer files are stored
  - Plan for layer file versioning
  - Establish backup and recovery procedures
  - Document access permissions and protocols

### Iterative Development

- **Start small**: Begin with simple layers and build complexity iteratively
- **Test layer combinations**: Validate that layers work together correctly
- **Document dependencies**: Track which layers depend on others
- **Continuous improvement**: Refine layer organization based on learnings

### CI/CD Integration

Consider implementing:
- **Automated layer validation**: Scripts to validate layer syntax and structure
- **Layer testing**: Automated tests for layer combinations
- **Version tagging**: Tag layer versions for deployment
- **Rollback capabilities**: Ability to revert to previous layer configurations

## Best Practices Summary

- **Keep layers focused** - Each layer should have a specific purpose
- **Use descriptive names** - Make it clear what each layer modifies
- **Document layer dependencies** - Note if layers depend on each other
- **Test layer combinations** - Ensure layers work together correctly
- **Keep the structure as simple as possible** - Avoid unnecessary complexity when working with layers
- **Do NOT import assets with the Root layer** - Keep `GoodStart_ROOT.usda` clean and focused on scene structure
- **Use AssetImport_LYR at the bottom of the stack** - Place asset import layers at the bottom of the `subLayers` array
- **Plan before implementing** - Define storage, versioning, and organization rules upfront
- **Start small, iterate** - Begin with simple layers and build complexity gradually
- **Leverage LIVRPS** - Use all composition arcs together for maximum flexibility

