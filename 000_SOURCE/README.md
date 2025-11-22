# 000_SOURCE

**Version:** 0.9.2-beta  
**Last Updated:** 11.22.2025

## Purpose

This folder contains **source files** used in the USD project. These are the original files that will be converted or referenced to create USD assets for digital twin applications.

**Note on Source File Management:**

- **Small Projects**: This `000_SOURCE/` folder serves as a local source repository for project-specific source materials
- **Large Digital Twin Projects**: In enterprise environments, source files are typically managed by **PLM (Product Lifecycle Management)**, **PDM (Product Data Management)**, **ERP (Enterprise Resource Planning)**, or other enterprise systems
  - These systems push data into the project via automated pipelines
  - Source files may be stored in external databases or systems, not in this local folder
  - The conversion pipeline connects directly to these enterprise systems
  - This folder may serve as a staging area or may be bypassed entirely in favor of direct system integration

## Usage

- **Small Projects**: Place files that are used as source files in this folder
- **Large Projects**: Source files are typically pushed from PLM/PDM/ERP systems via automated pipelines
- This folder serves as a local source repository for small projects or as a staging area for larger projects

## Source File Types

### CAD Files

- **JT files** (JT Open format)
- **CATIA files** (.CATPart, .CATProduct)
- **Rhino files** (.3dm)
- **STEP files** (.step, .stp) - often used as intermediate format for stable conversion
- Other CAD formats exported from various CAD systems

### DCC Source Files

- Original DCC files before USD export (Maya, Houdini, Blender, etc.)
- Working files that will be exported to USD format

## CAD Conversion Pipeline

Typical workflow:
1. Source files stored here or in external systems (PLM/PDM/ERP)
2. Convert via defined pipeline (possibly using STEP as intermediate format)
3. Converted USD files placed in `010_ASS_USD/`

## Storage Options

Source files can be stored in:
- **Local Storage**: In this `000_SOURCE/` folder for project-specific sources
- **Existing File Structure**: Within organization's existing file structure or database
- **PLM/PDM Systems**: Linked to Product Lifecycle Management or Product Data Management systems
- **ERP Systems**: Connected to Enterprise Resource Planning systems

## Version Control

- CAD systems typically have version control embedded in PLM/PDM/ERP systems
- Use **stable file names/paths** as endpoints rather than version numbers in filenames
- Let the version control system handle versioning, not the filename
- Link source files to PLM/PDM/ERP systems so administration is handled by these systems

## Metadata and Data Integration

- Extract metadata from source CAD files during conversion
- Map source file metadata to USD metadata structure
- Connect source file information to Asset Administration Shell (AAS) for digital twin administration

## Workflow

1. Source files stored here or in external systems
2. Convert to USD via pipeline
3. Place converted files in `010_ASS_USD/`
4. Map metadata and connect to external data sources
5. Use `020_LYR_USD/` layers for modifications

## Notes

- Source files are typically referenced or imported into the USD asset structure
- Keep source files organized and documented
- Maintain documentation of source file origins, versions, and conversion processes
- If managed in external systems (PLM/PDM/ERP), document connection and access methods
