# USD GoodStart

A clean, organized USD project template for starting new projects, with a focus on **digital twin applications**.

## About OpenUSD and Digital Twins

**OpenUSD** (Universal Scene Description) was originally developed by Pixar Animation Studios as a universal scene description format to be sent to renderers for visual effects and CGI production. However, its powerful composition system, non-destructive workflows, and ability to handle complex 3D data make it an ideal foundation for **digital twin applications**.

This project template adapts OpenUSD's proven VFX industry practices for digital twin use cases, including:
- Building digital twins from existing CAD products
- Integrating with PLM/PDM/ERP systems
- Connecting to Asset Administration Shell (AAS) standards
- Managing industrial and manufacturing digital twins
- Architecture, Engineering, and Construction (AEC) applications

While OpenUSD was designed for rendering, its universal scene description capabilities make it perfect for representing real-world assets, systems, and environments in digital twin contexts.

## Project Structure

This project follows a structured folder organization to maintain clarity and scalability:

```
USD_GoodStart/
├── 000_SOURCE/          # Source files used in the project
├── 010_ASS_USD/         # All USD assets (default + project assets)
├── 020_LYR_USD/         # Layer files for modifications and overrides
├── 030_TEX/             # Global texture files
├── GoodStart_ROOT.usda  # Master root file that references all layers + Assets
├── GoodStart.hiplc      # Houdini file (or .ma/.mb/.max for other DCC tools)
└── README.md            # This file
```

## Quick Start

1. **Assets**: Place your USD assets in `010_ASS_USD/`
2. **Modifications**: Create or edit layers in `020_LYR_USD/` to modify assets
3. **Textures**: Add global textures to `030_TEX/`
4. **Root File**: The `GoodStart_ROOT.usda` file references all layers and serves as the entry point

## Folder Details

Each folder contains its own README with detailed information:

- **[000_SOURCE/](000_SOURCE/README.md)** - Source files and materials
- **[010_ASS_USD/](010_ASS_USD/README.md)** - USD assets and asset organization
- **[020_LYR_USD/](020_LYR_USD/README.md)** - Layer files for modifications
- **[030_TEX/](030_TEX/README.md)** - Global texture files

## Root File

`GoodStart_ROOT.usda` is the master file that:
- References all layer files from `020_LYR_USD/`
- Serves as the entry point for the entire project
- Contains the base scene structure and environment

## DCC Files

DCC (Digital Content Creation) files that work on the USD files are stored in the root directory:

- **Houdini**: `GoodStart.hiplc` (or `.hip` files)
- **Maya**: `.ma` or `.mb` files
- **3ds Max**: `.max` files
- **Other DCC tools**: Place your working files here

These files allow different team members to work on the USD project using their preferred DCC tool. Each DCC file references and modifies the USD files (`GoodStart_ROOT.usda` and assets in `010_ASS_USD/`), but the actual USD files remain the source of truth. Changes are layered on top as opinions within the USD structure.

**Note**: Different team members may use different DCC tools, so you may see multiple DCC file types in the root directory. Each person works with their preferred tool while maintaining the same USD structure. Changes are layered on top as opinions within the USD structure.

## Workflow

### Digital Twin Workflow

1. **Source Files**: CAD files or other source materials in `000_SOURCE/` or external systems (PLM/PDM/ERP)
2. **Convert to USD**: Convert source files to USD format and place in `010_ASS_USD/`
3. **Add Metadata**: Map CAD metadata to USD metadata and connect to external data sources
4. **Apply Modifications**: Use layers in `020_LYR_USD/` to add digital twin-specific modifications, opinions, and connections
5. **Link to Root**: Ensure all assets and modifications are properly linked in `GoodStart_ROOT.usda`
6. **AAS Integration**: Connect USD assets to Asset Administration Shell (AAS) for digital twin management

### DCC Workflow (Optional)

1. **Import Assets**: Export USD files from DCC tools (Maya, Houdini, Blender, etc.) to `010_ASS_USD/`
2. **Reference Assets**: Use layers in `020_LYR_USD/` to reference and modify assets
3. **Apply Modifications**: Add opinions, variants, and material changes through layers
4. **Link to Root**: Ensure all modifications are properly linked in `GoodStart_ROOT.usda`

## Project Planning and Implementation Strategy

Before diving deep into implementation, establish clear project planning and management processes. This is **critical** for successful digital twin projects.

### Start Small: POC and MVP Approach

**Begin with a small sample project** before scaling to larger implementations:

1. **Proof of Concept (POC)**: Start with a small, focused project to validate:
   - Technical feasibility
   - Workflow concepts
   - Tool integration
   - Team capabilities

2. **Minimum Viable Product (MVP)**: Build a minimal but functional version that:
   - Demonstrates core value
   - Tests key workflows
   - Identifies challenges early
   - Provides learning opportunities

3. **Iterative Learning**: Through POC and MVP, necessary learnings will be discovered:
   - **Within teams**: Technical capabilities and workflow preferences
   - **Among stakeholders**: Requirements and expectations
   - **Across organizations**: Integration points and collaboration patterns

**This is NOT a waterfall project** - adopt an **agile, iterative approach**:
- Incremental development
- Regular feedback loops
- Continuous improvement
- Adapt to discoveries and changing requirements

### Storage and Version Control Planning

**Define rules and workflows BEFORE implementation:**

When storing original files on servers other than Nucleus Server (e.g., NAS, cloud storage, version control systems), establish clear guidelines:

1. **Storage Location Rules**:
   - Define where different file types are stored
   - Document storage hierarchies and naming conventions
   - Establish access permissions and protocols
   - Plan for scalability and growth

2. **Version Control Workflows**:
   - Determine version control strategy for each file type
   - Define branching and merging workflows
   - Establish review and approval processes
   - Document versioning policies

3. **File Organization**:
   - Source files (Photoshop, Substance, etc.) - where stored and how versioned
   - Final textures and assets - Nucleus Server vs. alternative storage
   - CAD source files - integration with PLM/PDM systems
   - USD files - version control approach

4. **Integration Points**:
   - How different storage systems connect
   - Synchronization workflows
   - Backup and recovery procedures
   - Access control and security

**This planning is part of the project planning and project management process** - do this before diving deep into implementation.

### CI/CD and Continuous Improvement

**Apply software development paradigms to production and product development:**

1. **Continuous Integration (CI)**:
   - Automated testing and validation of USD files
   - Asset validation pipelines
   - Automated conversion workflows
   - Quality checks and standards enforcement

2. **Continuous Deployment/Delivery (CD)**:
   - Automated publishing workflows
   - Version management and tagging
   - Deployment to different environments (dev, staging, production)
   - Rollback capabilities

3. **Best Practices from Software Development**:
   - **Version control** - Git-based workflows adapted for 3D assets
   - **Automated testing** - Validation scripts for USD files and assets
   - **Code review** - Asset review and approval processes
   - **Documentation** - Living documentation that evolves with the project
   - **Modular architecture** - Reusable components and assets
   - **Iterative development** - Small, frequent updates rather than big releases

4. **Transfer to Production/Product Development**:
   - These paradigms developed in software development are now being transferred to:
     - **Production development** - Manufacturing and industrial processes
     - **Production planning** - Supply chain and logistics
     - **Product development** - Design and engineering workflows
     - **Product production** - Manufacturing execution

**Key Principle**: Start small, learn fast, iterate continuously, and scale based on validated learnings.

## Learning from VFX Industry Best Practices

OpenUSD was originally developed by Pixar Animation Studios for visual effects and CGI production. The VFX industry has a decade of experience working with USD in production pipelines, and their best practices can serve as a **blueprint** for starting your own USD project.

### Key Resources

**Consider exploring these resources before starting your project:**

1. **[USDWG Collective Project 001](https://github.com/usd-wg/collectiveproject001)** - A collaborative project demonstrating VFX/CGI best practices:
   - Shows how to structure USD projects for production workflows
   - Demonstrates non-destructive workflows using USD composition arcs
   - Provides examples of asset organization, shots, and pipeline scripts
   - Uses git for version tracking with CHANGELOG files for publishing history
   - Includes validation and rendering pipeline scripts

2. **[Alliance for OpenUSD (AOUSD)](https://aousd.org/)** - The official standardization body:
   - Provides written specifications for OpenUSD functionality
   - Coordinates development of new OpenUSD functionality
   - Offers repository for new OpenUSD functionality
   - Hosts working groups and interest groups for collaboration
   - Maintains standards and schemas for the OpenUSD ecosystem

3. **[Industrial Digital Twin Association (IDTA)](https://industrialdigitaltwin.org/)** - Industry-specific digital twin standards:
   - Focuses on Industry 4.0 and digital twin applications
   - Provides guidance for industrial use cases
   - Connects to Asset Administration Shell (AAS) standards

4. **[First Steps to Becoming an OpenUSD Developer](https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/first_steps.html)** - NVIDIA's comprehensive getting started guide:
   - Navigate OpenUSD learning resources
   - Free Learn OpenUSD learning path
   - Get OpenUSD (source code, pre-built binaries, or usd-core from PyPI)
   - Technical references (Python API, C++ API, code samples)
   - OpenUSD Study Group on Discord (meets Tuesdays at 2:00 PM PT)
   - OpenUSD Development Certification information
   - Links to forums and community resources

5. **[Awesome OpenUSD](https://github.com/matiascodesal/awesome-openusd)** - Curated list of awesome OpenUSD resources and projects:
   - Libraries and tools
   - Sample assets from Pixar, NVIDIA, Disney, and others
   - Learning resources (non-technical and technical)
   - References and documentation
   - Integrations and plugins
   - Hand-picked resources for developers and artists

6. **[Haluszka OpenUSD Tutorials](https://haluszka.com/#tutorials)** - Practical OpenUSD tutorials and learning content:
   - Step-by-step tutorials for OpenUSD development
   - Practical examples and use cases
   - Learning resources for tech artist becoming pipelinedevelopers

7. **[CAD-to-OpenUSD](https://github.com/nAurava-Technologies/CAD-to-OpenUSD)** - CAD to OpenUSD conversion scripts from the USD study group:
   - Python scripts for converting CAD files (STEP, JT, CATIA, etc.) to USD format
   - Example STEP file conversion workflows
   - Uses uv for dependency management
   - Provides foundation for building custom CAD conversion pipelines
   - Work in progress (as of November 2024) - actively developed by the OpenUSD community

### Why VFX Practices Matter for Digital Twins

While OpenUSD was developed for rendering, the VFX industry's refined USD workflows translate excellently to digital twin applications:

**VFX Industry Practices:**
- **Large-scale production pipelines** with hundreds of artists
- **Non-destructive workflows** using composition arcs (references, payloads, variants, etc.)
- **Version control** and asset management at scale
- **Multi-DCC workflows** where different tools work on the same assets
- **Structured organization** ensuring assets are always ready for use

**Digital Twin Adaptations:**
- **CAD integration** - Converting CAD files to USD for digital twin representation
- **Metadata enrichment** - Adding real-world asset information and connections
- **System integration** - Connecting to PLM/PDM/ERP systems and Asset Administration Shell (AAS)
- **Lifecycle management** - Tracking asset changes over time
- **Multi-disciplinary collaboration** - Different teams (engineering, operations, maintenance) working on the same digital twin

These practices are particularly valuable for:
- **Digital twins** and industrial applications
- Architecture, Engineering, and Construction (AEC)
- Automotive and manufacturing
- Any project requiring 3D data interoperability with real-world systems

**Recommendation**: Review the [USDWG Collective Project 001](https://github.com/usd-wg/collectiveproject001) repository structure and workflow as a starting point, then adapt it to your specific needs.

### NVIDIA Digital Twin Resources

NVIDIA provides comprehensive resources for building digital twins with OpenUSD:

- **[NVIDIA Digital Twins Learning Path](https://www.nvidia.com/en-us/learn/learning-path/digital-twins/)** - Structured learning path covering:
  - Digital twin fundamentals
  - OpenUSD for digital twins
  - Industrial automation and robotics
  - Synthetic data generation
  - AI agents and multimodal models

- **[Assembling Digital Twins Documentation](https://docs.nvidia.com/learning/physical-ai/assembling-digital-twins/latest/index.html)** - Technical documentation on:
  - Building digital twins with OpenUSD
  - Asset organization and management
  - Integration with industrial systems
  - Best practices and workflows

- **[NVIDIA Digital Twins YouTube Live](https://www.youtube.com/live/tbnDlDe9iFA)** - Live sessions and tutorials on digital twin development

These resources provide practical guidance for implementing digital twin workflows with OpenUSD assets.

## Best Practices for Digital Twins and CAD Integration

When implementing this workflow with existing CAD systems and building digital twins from existing products, follow these best practices:

### CAD File Conversion Pipeline

When working with CAD files from various sources (JT, CATIA, Rhino, STEP, etc.), you need to define an **export pipeline** or **conversion pipeline** from the CAD file to USD:

1. **Source Files**: CAD files (JT, CATIA, Rhino, etc.) are typically stored within an existing file structure or database, or exported directly from CAD systems
2. **Conversion Path**: You may Consider using STEP files as an intermediate format for stable conversion
3. **USD Export**: Convert to USD format and place in `010_ASS_USD/`

**CAD Conversion Resources:**

- **[CAD-to-OpenUSD Repository](https://github.com/nAurava-Technologies/CAD-to-OpenUSD)** - Open-source conversion scripts from the USD study group:
  - Python-based CAD to USD conversion tools
  - Example workflows for STEP file conversion
  - Foundation for building custom conversion pipelines
  - Uses modern Python tooling (uv for dependency management)
  - Actively maintained by the OpenUSD community

### Connectors vs. Stable Conversion

- **Live Links**: Some connectors exist for live links and coordination with CAD systems. These are useful for real-time collaboration but may not provide stable, long-term connections.
- **Stable Connections**: For production workflows, **convert to USD** rather than relying solely on live connectors. This ensures:
  - Stable file references
  - Version independence
  - Better performance
  - Cross-platform compatibility

### Metadata and Data Integration

When converting CAD files to USD, consider:

1. **Metadata Extraction**: Extract relevant metadata from the source CAD file
2. **Data Source Connections**: Define how to connect USD files to other data sources (databases, APIs, etc.)
3. **USD Metadata**: Write appropriate metadata into the USD file structure
4. **Asset Administration Shell (AAS)**: Connect to **Asset Administration Shell (AAS)**, also known as Verwaltungsschale, for digital twin administration and lifecycle management

### Schema Standards and Coordination

**Before creating custom schemas:**

1. **Review Existing Schemas**: Familiarize yourself with schemas defined by the **Alliance for OpenUSD (AOUSD)**
2. **Research Industry Schemas**: Look at what other organizations and projects are using
3. **Coordinate with AOUSD**: If introducing new schemas, **coordinate with the AOUSD group** to ensure they fit into the bigger picture and align with industry standards
4. **Documentation**: Document any custom schemas and their relationship to standard schemas

### Version Control and File Naming

**Best Practices:**

1. **Use Stable Paths**: CAD systems typically have version control embedded in PLM (Product Lifecycle Management), PDM (Product Data Management), or ERP systems. Use **stable file names/paths** as endpoints rather than version numbers in filenames (avoid `version1`, `version2`, `final`, etc.)

2. **System Integration**: Link USD files to PLM/PDM/ERP systems so that the **administration layer is handled by these systems**

3. **Version Control Tools**: If no version control system exists:
   - **Introduce version control** in your USD workflow
   - For design and DCC teams, consider tools like **[Anchorpoint](https://www.anchorpoint.app/)**, a Git-based version control solution designed for artists and creative teams:
     - **Git with binary support**: No repository limits, works with TB-sized projects without slowdowns
     - **Made for artists**: Simple two-button interface, fail-safe operations
     - **File locking**: Prevents team members from overwriting files
     - **Art asset management**: Review, approve, and organize art assets within the tool
     - **Selective checkout**: Work with large repositories by downloading only what you need
     - **DCC integration**: Supports Blender, ZBrush, Photoshop, Substance, and other DCC tools
     - **Game engine support**: Works with Unreal Engine, Unity, and Godot
     - **Python API**: Automate workflows with Python-based actions
     - **Git server compatibility**: Works with GitHub, GitLab, Azure DevOps, Gitea, and others
     - **File sync integration**: Can be used alongside Google Drive, Dropbox, or NAS for non-versioned files
     - Good starting point for version control and file administration for creative teams

### Workflow Integration

1. **CAD Export**: Export from CAD systems (with version control handled by PLM/PDM)
2. **Conversion**: Convert to USD via defined pipeline (possibly through STEP)
3. **Metadata Mapping**: Map CAD metadata to USD metadata and connect to external data sources
4. **Layer Management**: Use `020_LYR_USD/` layers to add modifications and opinions
5. **AAS Integration**: Connect USD assets to Asset Administration Shell for digital twin management

## Notes

- This is a clean starting template - customize as needed for your project
- The `0_` prefix in asset names is used for sorting default assets
- Layers are loaded in order - later layers override earlier ones
- Asset-specific textures can be stored within asset folders, while global textures go in `030_TEX/`

