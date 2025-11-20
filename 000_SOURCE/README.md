# 000_SOURCE

## Purpose

This folder contains **source files** used in the USD project. These are the original files that will be converted or referenced to create USD assets for digital twin applications.

In digital twin workflows, source files typically come from CAD systems, PLM/PDM systems, or other enterprise systems that represent real-world products, systems, or environments.

## Usage

- Place files that are used as source files in this folder
- If you're working in a bigger context (e.g., a larger pipeline or multi-project setup), handle your sources in a different way appropriate to that context
- This folder serves as a local source repository for project-specific source materials

## Source File Types

### CAD Files

When working with CAD files from various sources, source files may include:

- **JT files** (JT Open format)
- **CATIA files** (.CATPart, .CATProduct)
- **Rhino files** (.3dm)
- **STEP files** (.step, .stp) - often used as intermediate format for stable conversion
- **Other CAD formats** exported from various CAD systems

### DCC Source Files

- Original DCC files before USD export (Maya, Houdini, Blender, etc.)
- Working files that will be exported to USD format

**Important: DCC Tool Limitations**

Not all DCC tools support USD's composition features:

- **Maya, Houdini, 3ds Max**: Full USD support with layering and referencing
- **Blender, Cinema 4D**: Limited support - can only read/write USD files but do NOT support layering, referencing, or composition arcs. These tools work destructively and can only create endpoint assets. See main README for detailed limitations.

## CAD Conversion Pipeline

When working with CAD files, the typical workflow is:

1. **Source Files**: CAD files are typically stored within an existing file structure or database, or exported directly from CAD systems
2. **Conversion Path**: You may consider using STEP files as an intermediate format for stable conversion
3. **USD Export**: Convert to USD format and place in `010_ASS_USD/`

### Storage Options

Source files can be stored in different ways depending on your infrastructure:

- **Local Storage**: In this `000_SOURCE/` folder for project-specific sources
- **Existing File Structure**: Within your organization's existing file structure or database
- **PLM/PDM Systems**: Linked to Product Lifecycle Management (PLM) or Product Data Management (PDM) systems
- **ERP Systems**: Connected to Enterprise Resource Planning systems

## Version Control Considerations

### Stable Paths

- CAD systems typically have version control embedded in PLM, PDM, or ERP systems
- Use **stable file names/paths** as endpoints rather than version numbers in filenames
- Avoid version numbers in filenames (e.g., `version1`, `version2`, `final`, etc.)
- Let the version control system handle versioning, not the filename

### System Integration

- Link source files to PLM/PDM/ERP systems so that the **administration layer is handled by these systems**
- If no version control system exists, consider introducing version control in your workflow
- For design and DCC teams, consider **[Anchorpoint](https://www.anchorpoint.app/)**, a Git-based version control solution designed for artists and creative teams:
  - **Git with binary support**: No repository limits, works with TB-sized projects without slowdowns
  - **Made for artists**: Simple two-button interface, fail-safe operations
  - **File locking**: Prevents team members from overwriting source files
  - **Art asset management**: Review, approve, and organize source files and assets
  - **Selective checkout**: Work with large repositories by downloading only what you need
  - **DCC integration**: Supports Blender, ZBrush, Photoshop, Substance, and other DCC tools commonly used for source file creation
  - **Python API**: Automate conversion workflows and file management with Python-based actions
  - **Git server compatibility**: Works with GitHub, GitLab, Azure DevOps, Gitea, and others
  - **File sync integration**: Can be used alongside Google Drive, Dropbox, or NAS for non-versioned source files
  - Provides version control over file structures with flexible organization

## Metadata and Data Integration

When working with source files:

1. **Metadata Extraction**: Extract relevant metadata from source CAD files during conversion
2. **Data Source Connections**: Define how source files connect to other data sources (databases, APIs, etc.)
3. **USD Metadata Mapping**: Map source file metadata to USD metadata structure
4. **Asset Administration Shell (AAS)**: Connect source file information to Asset Administration Shell (AAS) for digital twin administration

## Workflow Integration

The typical workflow from source files to USD assets:

1. **Source Files**: Original CAD or DCC files stored here or in external systems
2. **Conversion**: Convert to USD via defined pipeline (possibly through STEP as intermediate format)
3. **USD Assets**: Converted files placed in `010_ASS_USD/`
4. **Metadata Mapping**: Map source metadata to USD metadata and connect to external data sources
5. **Layer Management**: Use `020_LYR_USD/` layers to add modifications and opinions

## Notes

- Source files here are typically referenced or imported into the USD asset structure
- Keep source files organized and documented for easy reference
- Maintain clear documentation of source file origins, versions, and conversion processes
- If source files are managed in external systems (PLM/PDM/ERP), document the connection and access methods

