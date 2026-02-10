# ASWF Asset Group - Minimal/Production Example Workflow

**Version**: 1.9.2 | **Date**: 10.02.2026 | **Time**: 16:10 | **GlobalID**: 20260210_1320_ASWFAssetGroupWorkflow_001
**Last Updated:** 10.02.2026 16:10
**Framework:** General_Research (Discovery Phase)
**Status:** Discovery - Active
**Context:** AOUSD IEDT Interest Group task assignment

> **Task Origin**: AOUSD IEDT IG (Industrial and Engineering Digital Twin Interest Group)
> **Assignment**: Investigate and share insights from the ASWF asset group's minimal/production example workflow, particularly around their process for structuring minimal and production-ready assets.

**Tags (Keywords)**: — Reference `Master_Rules/master_tag_system.yml` for available tags.

| Category | Tags |
|----------|------|
| environment | `standalone`, `outside_omniverse`, `hybrid` |
| functionality | `analysis`, `validation`, `automation`, `rendering`, `packaging`, `conversion`, `export` |
| use_case | `digital_twin_creation`, `industrial_integration`, `workflow_automation`, `best_practices` |
| complexity | `advanced` |
| dependencies | `usd_core`, `omniverse` |
| research_type | `integration_pattern`, `best_practice`, `case_study`, `industrial_adoption` |
| usd_specific | `openusd`, `composition`, `layers`, `references`, `payloads`, `variants`, `instancing`, `layered_architecture` |
| industry | `digital_twin`, `manufacturing`, `visual_effects` |
| performance | `scalable`, `performance` |
| integration | `version_control`, `ci_cd` |

**Flat tags**: USD, OpenUSD, AOUSD, ASWF, IEDT, Digital Twin, Composition, Layer, LayerStack, Sublayer, Reference, Payload, LOD, Variant, VariantSet, Pipeline, ProjectStructure, NamingConventions, Instancing, LIVRPS, CAD, Manufacturing, Omniverse, Validation, CI/CD, Automation, Alliance for OpenUSD, Industrial Digital Twin Association, STEP, HOOPS, KitExtension, Connectors, Geometry, Robotics, VersionControl, GitLFS, Anchorpoint, Nucleus

**Quick Navigation**:

**Discovery & Findings**: [Executive Summary](#executive-summary) | [Discovery Overview](#discovery-overview) | [Key Questions](#key-questions-explored) | [Repository Overview](#repository-overview) | [Finding 1: Fragment Architecture](#finding-1-fragment-based-asset-architecture) | [Finding 2: Purpose-Based LOD](#finding-2-purpose-based-lod-separation-proxy--render) | [Finding 3: Sublayer Composition](#finding-3-purpose-level-composition-via-sublayers) | [Finding 4: Payload Pattern](#finding-4-payload-pattern-for-heavy-geometry) | [Finding 5: Shot Assembly](#finding-5-shot-assembly-architecture) | [Finding 6: Pipeline-as-Code](#finding-6-pipeline-as-code---automated-structure-generation) | [Finding 7: Version Control](#finding-7-version-control-strategy) | [Finding 8: Rendering](#finding-8-rendering-pipeline)

**Comparative Analysis**: [Finding 9: ASWF vs Learn OpenUSD](#finding-9-comparative-analysis---aswf-collectiveproject001-vs-nvidia-learn-openusd-principles) | [Finding 10: Three-Way Comparison](#finding-10-three-way-comparison---goodstart-vs-aswf-collectiveproject001-vs-learn-openusd) | [Finding 11: CAD-to-OpenUSD](#finding-11-cad-to-openusd--the-missing-first-mile-naurava-technologies--openusd-study-group) | [IEDT Nuances: Shots & LOD](#iedt-specific-nuances-shot-assembly-and-proxyrender-in-a-digital-twin-context)

**Summary & Action**: [Summary: Minimal vs Production](#summary-minimal-vs-production-ready-asset-definition) | [IEDT Recommendations](#iedt-specific-recommendations) | [Resume: Key Takeaways](#resume-key-takeaways-for-the-aousd-iedt-interest-group) | [GoodStart Evolution Plan](#goodstart-evolution-plan---closing-the-gaps)

**Reference**: [File Tree Reference](#file-tree-reference-complete) | [Composition Arc Diagram](#composition-arc-diagram) | [References](#references-and-related-resources-updated)

---

## Executive Summary

This discovery analyzes four complementary approaches to structuring and producing OpenUSD assets — the **ASWF collectiveproject001** (VFX production template), **NVIDIA Learn OpenUSD** (canonical principles curriculum), **USD GoodStart** (rapid onboarding for Omniverse), and **nAurava CAD-to-OpenUSD** (STEP→USD conversion pipeline) — to inform the AOUSD IEDT Interest Group's work on minimal production assets for industrial and engineering digital twins.

### Key Findings

1. **Fragment-based asset architecture is the production standard.** The ASWF approach decomposes each asset into independent layers per concern (model, skeleton, surface, binding) nested under purpose scopes (proxy/render). This yields dozens of files per asset but enables parallel workstreams and granular version control. (Findings 1-4)

2. **A "minimal production asset" is structurally complete but content-sparse.** It carries all composition arcs, payload boundaries, kind metadata, and directory conventions of a production asset — but with placeholder or minimal geometry. This makes it simultaneously a learning example, a production template, and a CI/CD validation target. (Finding 5-6, Summary)

3. **All four approaches converge on the same USD composition fundamentals** — sublayers for non-destructive overrides, references/payloads for asset instantiation with deferred loading, and kind metadata for model hierarchy traversal. They diverge in scope (conversion vs. asset vs. scene vs. project), audience (engineers vs. pipeline TDs vs. educators vs. beginners), and philosophy (convert first vs. start complete vs. start correct vs. start simple). (Findings 9-11)

4. **For IEDT, LOD via variant sets with payloads is preferred over purpose-based proxy/render.** The VFX `purpose` mechanism loads both proxy and render geometry into memory; a variant-set approach with payloads loads only the requested LOD, which is critical for memory-constrained industrial scenarios with thousands of parts. (IEDT Nuances)

5. **VFX "shot assembly" maps to IEDT "scenario/configuration assembly."** The same per-element override architecture (animation/lighting/fx per instance) translates directly to digital twin scenarios (state/telemetry/simulation per instance). (IEDT Nuances, Recommendations)

6. **The "first mile" — CAD to USD — is the critical gap for IEDT.** The three structuring approaches all assume USD files already exist. CAD-to-OpenUSD (nAurava / OpenUSD Study Group) provides a concrete STEP→USD pipeline using Kit SDK headlessly, with automatic instancing, deduplication, and configurable tessellation. CAD metadata conversion is the next frontier. (Finding 11)

### Practical Recommendation for the IEDT IG

| Step | What to do | Why |
|------|-----------|-----|
| 1 | **Convert CAD data with CAD-to-OpenUSD** | Get geometry from STEP into USD with proper instancing and tessellation — the first mile for engineering workflows |
| 2 | **Start with GoodStart's philosophy** | Get a working scene fast; place converted assets into a scaffold with proper references |
| 3 | **Structure assets per Learn OpenUSD principles** | Reference/payload pattern with lofting, proper `kind` metadata, parameterization via variant sets, instancing for repeated parts |
| 4 | **Adopt collectiveproject001's assembly pattern for multi-scenario twins** | Per-element overrides scale to inspection, operational, and maintenance scenarios |
| 5 | **Fill the IEDT-specific gaps none of them cover** | CAD metadata mapping, IoT/sensor binding, regulatory versioning, cross-domain data referencing |

A phased **GoodStart Evolution Plan** (6 phases) is included at the end of this document, detailing concrete script-driven improvements to bridge the identified gaps.

**Quick path:** Jump to the [Resume: Key Takeaways](#resume-key-takeaways-for-the-aousd-iedt-interest-group) for the consolidated recommendation with one-sentence-per-approach summaries.

---

## Discovery Overview

**Subject:** ASWF USD Working Group - Collective Project 001 Asset/Shot Structure Analysis

**Purpose:** Analyze the `usd-wg/collectiveproject001` repository to extract insights about how the ASWF (Academy Software Foundation) USD Working Group structures minimal and production-ready OpenUSD assets, with the goal of informing IEDT use case development and CAD-to-USD workflow standardization.

**Source Repository:** https://github.com/usd-wg/collectiveproject001

**Research Framework:**
- **Ruling contract:** `Research_Definition/research_configuration_rules.yml`
- **Location:** `General_Research/070_Proj_RESEARCH/02_Research_WIP/`
- **Next Phase:** Convert to `_RESEARCH.md` when ready for structured analysis, or deliver directly as IEDT IG report

---

## Key Questions Explored

1. How does the ASWF asset group structure minimal USD assets?
2. What is the composition arc strategy (references vs. sublayers)?
3. How are assets made "renderable from day one" with placeholder scaffolding?
4. What role does the pipeline (Python scripts) play in generating the structure?
5. How does the shot-assembly pattern work for multi-element scenes?
6. What can the IEDT IG learn from this for industrial/engineering digital twin use cases?

---

## Repository Overview

### Project Identity

- **Name:** USDWG Collective Project 001
- **Community:** USD Working Group (usd-wg) under ASWF, with major contribution from O3DE community
- **Primary Goal:** Create a short story with the character "Odie" using a proper VFX pipeline structure, rendered offline via `usdrecord` with Pixar's Storm
- **Secondary Goals:** Real-time rendering in O3DE, deliverables in multiple formats, inclusion in DPEL library (https://dpel.aswf.io/)
- **Character:** "Odie" from the O3DE community (https://github.com/o3de/odie-3d-assets)

### Top-Level Structure

```
collectiveproject001/
├── assets/              # Reusable asset definitions
│   ├── odie/            # Character asset
│   └── terrain/         # Environment asset
├── shots/               # Shot assemblies
│   └── s001_001/        # First shot
├── pipeline/            # Python pipeline tools
│   ├── pipe_genesis.py  # Structure generator
│   ├── pipe_globals.py  # Shared utilities
│   ├── render_asset.py  # Asset turntable renderer
│   └── render_shot.py   # Shot renderer
├── .gitattributes
├── .gitignore
└── README.md
```

---

## Finding 1: Fragment-Based Asset Architecture

### The Asset Decomposition Model

Each asset is decomposed into **fragments** - independent, composable layers that represent a specific concern (geometry, materials, skeleton, material-to-geometry binding). This is the core architectural insight.

**Asset fragments defined in the pipeline:**

| Fragment     | Purpose                              | Used In       |
|-------------|--------------------------------------|---------------|
| `model`     | Geometry data (meshes, curves)       | Assets        |
| `skeleton`  | Skeletal rig data (joints, weights)  | Assets        |
| `surface`   | Material/shader definitions          | Assets        |
| `binding`   | Material-to-geometry binding         | Assets        |
| `animation` | Animated transforms / poses          | Shot Elements |
| `lighting`  | Per-element lighting overrides       | Shot Elements |
| `fx`        | Effects data (particles, etc.)       | Shot Elements |
| `rendersettings` | Render configuration            | Shots         |

### Fragment Directory Structure (Example: `assets/odie/render/`)

```
render/
├── index.usda             # Purpose-level aggregator (sublayers all fragments)
├── model/
│   ├── index.usda         # Fragment entry point
│   ├── payload.usda       # Heavy geometry (payload-deferred loading)
│   ├── host_wip/          # DCC working files (e.g., .blend, .ma)
│   └── host_usd_export/   # USD exports from DCC tools
├── skeleton/
│   ├── index.usda
│   ├── host_wip/
│   └── host_usd_export/
├── surface/
│   ├── index.usda
│   ├── payload.usda       # Material definitions
│   ├── host_wip/
│   └── host_usd_export/
└── binding/
    ├── index.usda
    ├── host_wip/
    └── host_usd_export/
```

### Key Takeaway

The `host_wip/` and `host_usd_export/` directories are a practical pattern for production environments: artists work in their DCC tool (Blender, Maya, etc.) and export USD fragments into `host_usd_export/`. The `index.usda` at the fragment level then references or payloads the exported data. This keeps **source files alongside their USD outputs** without polluting the USD composition tree.

---

## Finding 2: Purpose-Based LOD Separation (proxy / render)

### Dual-Purpose Architecture

Each asset has two **purpose** variants:

```
assets/odie/
├── index.usda         # Top-level: references both purposes
├── proxy/             # Lightweight representation
│   └── index.usda     # Same fragment structure (model, skeleton, surface, binding)
└── render/            # Full-quality representation
    └── index.usda     # Same fragment structure (model, skeleton, surface, binding)
```

### The Root Asset File (`assets/odie/index.usda`)

```usda
#usda 1.0
(
    endTimeCode = 1
    framesPerSecond = 24
    metersPerUnit = 0.01
    startTimeCode = 1
    timeCodesPerSecond = 24
    upAxis = "Y"
)

def Xform "main" (
    assetInfo = {
        asset identifier = @assets/odie/index.usda@
        string name = "odie"
        string version = "latest"
    }
    kind = "component"
)
{
    def Scope "proxy" (
        prepend references = @proxy/index.usda@
    )
    {
        uniform token purpose = "proxy"
    }

    def Scope "render" (
        prepend references = @render/index.usda@
    )
    {
        uniform token purpose = "render"
    }
}
```

### Key Takeaways

- **`assetInfo` metadata** is set at the root level with `identifier`, `name`, and `version`
- **`kind = "component"`** identifies this as a leaf-level asset in the Model Hierarchy
- **`uniform token purpose`** on each Scope enables purpose-based rendering (viewers can toggle proxy/render)
- **Both purposes share identical fragment structure**, just with different content quality
- **Version is "latest"** because git history serves as the versioning system

### IEDT Relevance

This proxy/render split maps directly to engineering needs:
- **Proxy:** Simplified geometry for large-scale digital twin visualization (e.g., bounding boxes, low-poly)
- **Render:** Full CAD-quality geometry for detailed inspection, simulation input, or high-fidelity rendering

---

## Finding 3: Purpose-Level Composition via Sublayers

### The Purpose Index File (`render/index.usda`)

```usda
#usda 1.0
(
    defaultPrim = "main"
    subLayers = [
        @binding/index.usda@,
        @surface/index.usda@,
        @skeleton/index.usda@,
        @model/index.usda@
    ]
    upAxis = "Y"
)

def Xform "main"
{
}
```

### Composition Strategy

**SubLayer order is significant** - it defines opinion strength (LIFO stack):

1. `binding/index.usda` - **Strongest** opinions (material assignments override)
2. `surface/index.usda` - Material definitions
3. `skeleton/index.usda` - Skeletal rig
4. `model/index.usda` - **Weakest** opinions (base geometry)

This means:
- Geometry lives in `model` as the base layer
- Skeleton can add joint data on top
- Surface can define materials
- Binding can override which materials apply where

### IEDT Relevance

For engineering digital twins, this sublayer order could be adapted:
1. `binding/index.usda` - Sensor-to-geometry or data-to-geometry bindings
2. `simulation/index.usda` - Simulation overlays (FEA results, CFD visualization)
3. `metadata/index.usda` - Engineering metadata (part numbers, tolerances, BOM data)
4. `model/index.usda` - Base CAD geometry

> **Related research — Semantic Governance and Data Integration:**
> The fragment/sublayer model addresses *structural* composition of USD data, but IEDT also needs a *semantic* layer — how do you give engineering meaning to prims, bind them to live data sources (PLM, ERP, IoT), and govern those connections as systems evolve? This is the domain of **Composable Bindings**, a design pattern introduced by Aaron Luk (NVIDIA) and Christoph Berlin (Microsoft) in their joint whitepaper [*Composable Bindings: Simplified System Integration*](https://aka.ms/ComposableBindings) (November 2025). Composable Bindings replace brittle point-to-point integrations with flexible, context-aware connections between data lakes, visualization engines (OpenUSD/Omniverse), and operational systems — using open standards (OpenTelemetry, CloudEvents) as the transport layer.
>
> A companion research paper, [`AAS_OPC_OpenUSD_RESEARCH_v12.md`](../../AAS_OPC_OpenUSD_INTEGRATION/docs/AAS_OPC_OpenUSD_RESEARCH_v12.md), investigates how to combine this Composable Bindings approach with the German engineering tradition of the **Asset Administration Shell (AAS)** and **OPC UA** — creating a layered architecture where OpenUSD provides the deterministic composition substrate, AAS/ISO 81346 provides identity and governance semantics, and Composable Bindings provide the flexible integration layer that connects them to live industrial systems. This is directly relevant to how the sublayer fragments described above would connect to real-world engineering data.

---

## Finding 4: Payload Pattern for Heavy Geometry

### Model Fragment (`assets/odie/render/model/index.usda`)

```usda
#usda 1.0
(
    defaultPrim = "main"
)

def Xform "main"
{
    def Scope "geo" (
        prepend payload = @payload.usda@
    )
    {
    }
}
```

### Key Takeaway

- Heavy geometry is deferred via `payload` (not `references`)
- The `payload.usda` is a separate file that can be unloaded by viewers to reduce memory
- This is critical for production scenes with many assets - you can browse the scene graph without loading all geometry
- The `geo` Scope acts as the payload boundary

### IEDT Relevance

Payloads are essential for engineering digital twins where:
- CAD assemblies may contain thousands of parts
- Point cloud / LiDAR data can be extremely heavy
- IoT sensor data streams may generate large time-sampled datasets
- Users need to navigate the hierarchy without loading everything

---

## Finding 5: Shot Assembly Architecture

### Shot Structure (`shots/s001_001/`)

```
s001_001/
├── index.usda           # Shot root - the "composited scene"
├── animation/           # Shot-level animation overrides
├── lighting/            # Shot-level lighting
├── fx/                  # Shot-level effects
├── rendersettings/      # Render configuration
├── odie01/              # Character element instance
│   ├── index.usda       # Sublayers: fx, lighting, animation + asset reference
│   ├── animation/       # Per-element animation
│   ├── fx/              # Per-element effects
│   └── lighting/        # Per-element lighting
├── terrain01/           # Environment element instance
├── renderCam/           # Camera element
├── envLights/           # Environment lights
├── lightRig01/          # Light rig (sublayered)
├── renderPasses/        # Render passes (sublayered)
└── usdrecord_renders/   # Output renders
```

### The Shot Root File (`shots/s001_001/index.usda`)

```usda
#usda 1.0
(
    endTimeCode = 1480
    framesPerSecond = 24
    metersPerUnit = 0.01
    startTimeCode = 1000
    subLayers = [
        @rendersettings/index.usda@,
        @fx/index.usda@,
        @lighting/index.usda@,
        @animation/index.usda@,
        @renderPasses/index.usda@,
        @lightRig01/index.usda@
    ]
    timeCodesPerSecond = 24
    upAxis = "Y"
)

def Xform "World" (kind = "group")
{
    def Xform "characters" (kind = "group")
    {
        def Xform "odie01" (
            kind = "component"
            prepend references = @odie01/index.usda@
        ) { }
    }
    def Xform "environments" (kind = "group")
    {
        def Xform "terrain01" (
            kind = "component"
            prepend references = @terrain01/index.usda@
        ) { }
    }
    def Xform "cameras" (kind = "group")
    {
        def Xform "renderCam" (
            kind = "component"
            prepend references = @renderCam/index.usda@
        ) { }
    }
    def Xform "lights" (kind = "group")
    {
        def Xform "envLights" (
            kind = "component"
            prepend references = @envLights/index.usda@
        ) { }
    }
}
```

### Dual Composition Strategy

The shot uses **two different composition arcs** strategically:

| Arc Type | Used For | Rationale |
|----------|----------|-----------|
| **Reference** | Characters, environments, cameras, lights | Positional elements that need their own transform in the scene hierarchy |
| **SubLayer** | Animation, lighting, FX, render settings, light rigs, render passes | Data overrides that modify existing prims across the entire scene |

### Element Instance Pattern (`shots/s001_001/odie01/index.usda`)

```usda
#usda 1.0
(
    defaultPrim = "main"
    subLayers = [
        @fx/index.usda@,
        @lighting/index.usda@,
        @animation/index.usda@,
        @../../../assets/odie/index.usda@
    ]
    timeCodesPerSecond = 24
    upAxis = "Y"
)
```

This is a powerful pattern:
- The **base asset** (`../../../assets/odie/index.usda`) is the weakest sublayer
- Shot-specific **animation**, **lighting**, and **fx** overrides are layered on top
- The element can be referenced into the shot hierarchy while keeping its own override stack

### IEDT Relevance

This shot assembly pattern maps to digital twin scenarios:
- **"World"** = The digital twin environment (factory floor, building, infrastructure)
- **"characters"** = Movable equipment, robots, vehicles
- **"environments"** = Static structure (building shell, terrain, roads)
- **"cameras"** = Inspection viewpoints, security cameras, virtual sensors
- **"lights"** = Environmental lighting conditions
- **Element overrides** = Per-instance configuration (robot arm positions, valve states, sensor readings)

---

## Finding 6: Pipeline-as-Code - Automated Structure Generation

### `pipe_genesis.py` - The Scaffold Generator

The most significant architectural insight is that the **entire project structure is generated programmatically**. The `pipe_genesis.py` script:

1. **Creates all directories** (assets, shots, and their subdirectories)
2. **Generates all placeholder `index.usda` files** with correct composition arcs
3. **Sets up `host_wip/` and `host_usd_export/` directories** with `.keep` files
4. **Configures metadata** (metersPerUnit, upAxis, timeCode ranges, fps)
5. **Establishes composition relationships** (references, sublayers, payloads)
6. **Assigns Model Hierarchy kinds** ("component", "group")
7. **Sets `assetInfo`** (identifier, name, version)

### Configuration-Driven Design

Assets and shots are defined as simple Python data structures:

```python
ASSETS = ["odie", "terrain"]

SHOTS = [
    {
        "name": "s001_001",
        "startTimeCode": 1000.0,
        "endTimeCode": 1480.0,
        "framesPerSecond": 24.0,
        "elements": [
            {"name": "odie01",     "type": "characters",    "asset": "odie",    "arc": "reference"},
            {"name": "terrain01",  "type": "environments",  "asset": "terrain", "arc": "reference"},
            {"name": "renderCam",  "type": "cameras",       "asset": None,      "arc": "reference"},
            {"name": "envLights",  "type": "lights",        "asset": None,      "arc": "reference"},
            {"name": "lightRig01", "type": "lights",        "asset": None,      "arc": "sublayer"},
            {"name": "renderPasses","type": "lights",       "asset": None,      "arc": "sublayer"},
        ]
    },
]
```

### "Always Renderable" Philosophy

The scaffold creates a **valid, renderable USD scene from the very beginning** - even before any artist contributes content. All placeholder files are valid USDA with proper `defaultPrim` and metadata. Artists then fill in the fragments as their work progresses. This means:

- The shot file is always loadable in `usdview`
- Validation and CI/CD can run at any point in the process
- Multiple artists can work on different fragments in parallel without conflicts
- New assets or shots can be added by extending the configuration and re-running genesis

### IEDT Relevance

This pipeline-as-code approach is directly applicable to IEDT:
- **CAD-to-USD conversion pipelines** could use similar scaffold generators
- **Digital twin onboarding** could auto-generate the USD structure from BOM/assembly data
- **CI/CD validation** could verify structural compliance at every commit
- **Template-based project creation** for common IEDT scenarios (factory, building, infrastructure)

---

## Finding 7: Version Control Strategy

### Git as the Single Source of Truth

The project deliberately avoids USD-level versioning in favor of **git-based versioning**:

- Asset version is always `"latest"` in `assetInfo`
- Previous versions are older git commits
- `CHANGELOG.md` files per asset function as publishing version history
- No version-numbered directories or files

### Implications

- Simplifies the file structure significantly
- Version comparison is done via `git diff`
- Branching enables parallel development of different "versions"
- Merge conflicts are handled at the git level, not the USD level

### IEDT Relevance

For digital twins, this simplicity is attractive but may need augmentation:
- Engineering data often requires explicit version tracking (revision numbers, ECN/ECO references)
- Regulatory compliance may require versioned snapshots (e.g., as-built vs. as-designed)
- Consider hybrid approach: git for file versioning + USD metadata for engineering revision IDs

### Beyond Standard Git: Anchorpoint as a Git-Based Alternative for Engineers and Artists

Standard git works well for text-based USD files (`.usda`) and small projects, but **binary assets** (`.usdc`, `.usd`, textures, CAD source files) and **non-technical team members** (engineers, designers) quickly hit git's usability and scalability limits. [Anchorpoint](https://www.anchorpoint.app/) is a git-based version control solution that addresses these gaps:

| Challenge | Standard Git | Anchorpoint |
|-----------|-------------|-------------|
| **Binary file handling** | Requires manual Git LFS configuration | Automatic LFS handling, no configuration needed |
| **TB-scale repositories** | Slow clones, full history download | Sparse checkout + shallow clone — download only what you need |
| **Non-technical users** | Command-line or complex GUI clients | Two-button UX designed for artists and engineers |
| **File locking** | Not natively supported | Built-in file locking (prevents overwrite conflicts on binary assets) |
| **Visual review** | External tools needed | Inline review, annotation, and approval for images, 3D, video, audio |
| **Asset management** | Separate tooling | Integrated tagging, search, and organization |
| **DCC integration** | Manual workflows | Unreal, Unity, Blender plugins; thumbnail previews for DCC files |

**Why this matters for IEDT and Omniverse workflows:**

1. **Post-Nucleus world.** With NVIDIA opening Omniverse beyond Nucleus-only workflows, teams need alternative collaboration backends. A git-based approach (with Anchorpoint's binary handling) could serve as a viable file management layer for USD projects that don't use Nucleus — especially in engineering environments where IT infrastructure favors standard git servers (GitHub, GitLab, Azure DevOps) over proprietary solutions.

2. **Engineering team adoption.** The collectiveproject001 pattern (dozens of files per asset, fragment-per-artist) only works if every contributor can version-control reliably. For mixed teams of engineers, CAD specialists, and visualization artists, Anchorpoint's simplified UX and file locking remove the "git is too hard" barrier.

3. **Audit trail for regulated industries.** IEDT scenarios in manufacturing, aerospace, and construction often require provenance tracking. Git provides commit history; Anchorpoint adds visual review/approval workflows on top — approaching the auditability that PLM systems offer, but with git's openness and ecosystem.

4. **Python API for pipeline integration.** Anchorpoint exposes a Python API, enabling automated workflows — for example, triggering a `cad2usd` conversion on commit, running USD validation on push, or auto-tagging converted assets.

> **Note:** Anchorpoint is a commercial product (German company, Anchorpoint Software GmbH). It is not open-source, but builds on open-source git. Evaluate it alongside alternatives like GitHub Desktop, SourceTree, or GitKraken — but its binary-first, artist/engineer-friendly design makes it particularly relevant for USD/IEDT workflows where large files and non-developer users are the norm.

---

## Finding 8: Rendering Pipeline

### Asset Rendering (`render_asset.py`)

- Generates turntable animations automatically
- Creates camera rig programmatically (focal length, clipping, aperture)
- Renders both proxy and render purposes separately
- Creates a "reviewer" USD file with textured quads for comparing results in `usdview`
- Uses `usdrecord` with Pixar's Storm render delegate

### Shot Rendering (`render_shot.py`)

- Reads shot metadata (frame range, FPS) from the USD stage
- Supports multiple renderers (Storm/GL, RenderMan RIS)
- Creates snapshot files for render settings overrides when none exist in the shot
- Renders per-purpose (proxy/render) into timestamped output directories
- Supports a `--makefinal` flag for non-timestamped "final" renders

### IEDT Relevance

Automated rendering pipelines are valuable for:
- Generating visual documentation of digital twin states
- Creating inspection reports with automated viewpoint captures
- Time-lapse visualization of digital twin evolution
- QA validation of CAD-to-USD conversion quality

---

## Summary: Minimal vs. Production-Ready Asset Definition

### What Makes This a "Minimal" Example

1. **Only 2 assets** (odie, terrain) - enough to demonstrate patterns, not overwhelming
2. **1 shot** (s001_001) - shows the assembly pattern without production complexity
3. **Placeholder files** - many fragments are empty `index.usda` files (especially binding, surface)
4. **No textures in repo** - keeps the repo lightweight
5. **Simple pipeline** - 4 Python scripts total, no external dependencies beyond `pxr`
6. **Git-only versioning** - no complex asset management system

### What Makes It "Production-Ready" (Patterns)

1. **Full fragment decomposition** - model, skeleton, surface, binding per asset per purpose
2. **Proper composition arcs** - references for positional, sublayers for overrides
3. **Payload deferral** - heavy geometry behind payload arcs for scalability
4. **Model Hierarchy** - `kind` metadata ("component", "group") for proper model traversal
5. **Purpose separation** - proxy/render split for viewport performance
6. **Asset metadata** - `assetInfo` with identifier, name, version
7. **Pipeline automation** - programmatic structure generation, automated rendering
8. **Per-element shot overrides** - animation/lighting/fx per element instance
9. **host_wip / host_usd_export** - production workflow for DCC integration
10. **CHANGELOG per asset** - version tracking at the asset level

### The Insight: "Minimal Production Asset" Means...

A minimal production asset is **structurally complete but content-sparse**. It has:
- All the directories, files, and composition arcs that a production asset would have
- Proper metadata, kinds, purposes, and payload boundaries
- But minimal or placeholder content in the actual geometry/material/animation data

This allows the structure to serve as both:
- A **learning example** (developers can study the patterns)
- A **production template** (teams can fork and fill with real content)
- A **validation target** (CI/CD can verify structural compliance)

---

## IEDT-Specific Recommendations

### 1. Adapt the Fragment Model for Engineering Data

```
assets/robot_arm/
├── index.usda                    # Root asset
├── proxy/                        # Simplified representation
│   ├── model/                    # Low-poly geometry
│   └── metadata/                 # Basic identification
└── render/                       # Full-detail representation
    ├── model/                    # Full CAD geometry
    ├── metadata/                 # Engineering metadata (part numbers, tolerances)
    ├── kinematics/               # Joint definitions, motion limits
    ├── sensor_points/            # IoT sensor attachment points
    └── binding/                  # Metadata-to-geometry bindings
```

### 2. Propose an IEDT-Specific Shot Assembly

Instead of "shots" (VFX term), IEDT could use "scenarios" or "configurations":

```
scenarios/
└── factory_inspection_001/
    ├── index.usda                # Scenario root
    ├── robot01/                  # Robot instance (references asset)
    │   ├── state/                # Current joint positions
    │   └── telemetry/            # Live IoT data overlay
    ├── conveyor01/               # Conveyor instance
    ├── inspection_cam/           # Virtual inspection camera
    └── simulation_overlay/       # FEA/CFD results overlay
```

### 3. Consider a `pipe_genesis.py` for IEDT

An IEDT scaffold generator could:
- Accept a CAD assembly BOM as input
- Generate the full USD structure with proper hierarchy
- Create placeholder files for each engineering fragment
- Set engineering-specific metadata (units, coordinate system, part references)

### 4. Establish a "Minimal IEDT Asset" Definition

Based on the ASWF pattern, a minimal IEDT asset should include:
- At minimum: `model/` with geometry and `metadata/` with engineering identification
- Proper `assetInfo` with engineering identifiers (part number, revision, source CAD system)
- `kind` hierarchy for assembly navigation
- Payload boundaries for heavy geometry
- Proxy/render purpose split

---

## References and Related Resources

| Resource | URL | Relevance |
|----------|-----|-----------|
| USDWG Collective Project 001 | https://github.com/usd-wg/collectiveproject001 | Primary analysis target |
| O3DE Odie Assets | https://github.com/o3de/odie-3d-assets | Source character asset |
| AOUSD Interest Groups | https://aousd.org/community/interest-groups/ | IEDT IG home |
| AOUSD IEDT IG Charter | https://aousd.org/community/interest-groups/ | Group charter and scope |
| DPEL Library (ASWF) | https://dpel.aswf.io/ | Target distribution platform |
| USD Assets Working Group | (referenced in project README) | Asset structure standards |
| NVIDIA CAD-to-USD Resources | (referenced in IEDT discussions) | Production-ready asset examples |
| ALab (Animal Logic) | (referenced in IEDT discussions) | Full production example |

---

## Next Steps

1. **Present findings to IEDT IG** - Share this analysis in the next IEDT IG meeting
2. **Propose IEDT fragment taxonomy** - Define engineering-specific fragments (metadata, kinematics, telemetry, simulation)
3. **Create IEDT scaffold generator** - Adapt `pipe_genesis.py` for engineering use cases
4. **Map to collected use cases** - Apply these structural patterns to the 7+ use cases collected by the group
5. **Coordinate with ASWF USD Assets WG** - Share IEDT requirements and learn from their evolving standards
6. **Explore CAD-to-USD pipeline integration** - Specifically how OnShape/SolidWorks exports map to this fragment structure
7. **Consider promoting to _RESEARCH.md** - If deeper analysis of specific patterns (e.g., payload strategies for engineering data) is needed

---

## File Tree Reference (Complete)

```
collectiveproject001/
├── .gitattributes
├── .gitignore
├── README.md
├── assets/
│   ├── README.md (empty)
│   ├── odie/
│   │   ├── CHANGELOG.md
│   │   ├── index.usda
│   │   ├── usdrecord_renders/
│   │   ├── proxy/
│   │   │   ├── index.usda
│   │   │   ├── binding/
│   │   │   │   ├── index.usda
│   │   │   │   ├── host_wip/
│   │   │   │   └── host_usd_export/
│   │   │   ├── model/
│   │   │   │   ├── index.usda
│   │   │   │   ├── host_wip/
│   │   │   │   └── host_usd_export/
│   │   │   ├── skeleton/
│   │   │   │   ├── index.usda
│   │   │   │   ├── host_wip/
│   │   │   │   └── host_usd_export/
│   │   │   └── surface/
│   │   │       ├── index.usda
│   │   │       ├── host_wip/
│   │   │       └── host_usd_export/
│   │   └── render/
│   │       ├── index.usda
│   │       ├── binding/
│   │       │   ├── index.usda
│   │       │   ├── host_wip/
│   │       │   └── host_usd_export/
│   │       ├── model/
│   │       │   ├── index.usda
│   │       │   ├── payload.usda
│   │       │   ├── host_wip/
│   │       │   └── host_usd_export/
│   │       ├── skeleton/
│   │       │   ├── index.usda
│   │       │   ├── host_wip/
│   │       │   └── host_usd_export/
│   │       └── surface/
│   │           ├── index.usda
│   │           ├── payload.usda
│   │           ├── host_wip/
│   │           └── host_usd_export/
│   └── terrain/
│       ├── index.usda
│       ├── proxy/
│       │   └── (same fragment structure)
│       └── render/
│           └── (same fragment structure)
├── shots/
│   ├── README.md (empty)
│   └── s001_001/
│       ├── index.usda
│       ├── usdrecord_renders/
│       ├── animation/
│       │   └── index.usda
│       ├── lighting/
│       │   └── index.usda
│       ├── fx/
│       │   └── index.usda
│       ├── rendersettings/
│       │   └── index.usda
│       ├── lightRig01/
│       │   └── index.usda
│       ├── renderPasses/
│       │   └── index.usda
│       ├── odie01/
│       │   ├── index.usda
│       │   ├── animation/
│       │   ├── fx/
│       │   └── lighting/
│       ├── terrain01/
│       │   └── index.usda + fragments
│       ├── renderCam/
│       │   └── index.usda + fragments
│       └── envLights/
│           └── index.usda + fragments
└── pipeline/
    ├── README.md (empty)
    ├── pipe_genesis.py
    ├── pipe_globals.py
    ├── render_asset.py
    └── render_shot.py
```

---

## Composition Arc Diagram

```
SHOT (index.usda)
├── [SubLayer] rendersettings/index.usda     ← strongest shot-level opinions
├── [SubLayer] fx/index.usda
├── [SubLayer] lighting/index.usda
├── [SubLayer] animation/index.usda
├── [SubLayer] renderPasses/index.usda
├── [SubLayer] lightRig01/index.usda         ← weakest shot-level opinions
│
└── /World  (Xform, kind="group")
    ├── /characters (Xform, kind="group")
    │   └── /odie01 (Xform, kind="component")
    │       └── [Reference] odie01/index.usda
    │           ├── [SubLayer] fx/index.usda
    │           ├── [SubLayer] lighting/index.usda
    │           ├── [SubLayer] animation/index.usda
    │           └── [SubLayer] ../../assets/odie/index.usda
    │               └── /main (Xform, kind="component")
    │                   ├── /proxy [Reference] proxy/index.usda  (purpose="proxy")
    │                   │   ├── [SubLayer] binding/index.usda
    │                   │   ├── [SubLayer] surface/index.usda
    │                   │   ├── [SubLayer] skeleton/index.usda
    │                   │   └── [SubLayer] model/index.usda
    │                   │       └── /geo [Payload] payload.usda
    │                   │
    │                   └── /render [Reference] render/index.usda (purpose="render")
    │                       ├── [SubLayer] binding/index.usda
    │                       ├── [SubLayer] surface/index.usda
    │                       ├── [SubLayer] skeleton/index.usda
    │                       └── [SubLayer] model/index.usda
    │                           └── /geo [Payload] payload.usda
    │
    ├── /environments (Xform, kind="group")
    │   └── /terrain01 → [Reference] terrain01/index.usda → asset
    ├── /cameras (Xform, kind="group")
    │   └── /renderCam → [Reference] renderCam/index.usda
    └── /lights (Xform, kind="group")
        └── /envLights → [Reference] envLights/index.usda
```

---

## Finding 9: Comparative Analysis — ASWF collectiveproject001 vs. NVIDIA Learn OpenUSD Principles

This section compares the ASWF collectiveproject001 patterns against the **canonical asset structure principles** documented in NVIDIA's [Learn OpenUSD: Asset Structure Principles and Content Aggregation](https://docs.nvidia.com/learn-openusd/latest/asset-structure/asset-structure-principles/index.html).

The Learn OpenUSD curriculum codifies six core architectural concepts:
1. **Asset Interface** (entry point, encapsulation, prim hierarchy)
2. **Workstreams** (layer stacks modeling parallel work)
3. **Asset Parameterization** (variant sets, primvars)
4. **Reference/Payload Pattern** (lofting, deferred loading)
5. **Model Hierarchy** (kinds: component, assembly, group, subcomponent)
6. **Asset Modularity and Instancing** (scenegraph instancing, point instancing)

### Convergences (Where They Agree)

| Principle | ASWF collectiveproject001 | Learn OpenUSD | Assessment |
|-----------|--------------------------|---------------|------------|
| **Asset Entry Point** | `index.usda` at every level acts as the single entry point | Recommends a clear entry-point file (the "interface") that consumers reference | **Full convergence.** The `index.usda` convention is a clean implementation of the asset interface principle. |
| **Workstreams via Sublayers** | Fragments (model, surface, skeleton, binding) are sublayered in purpose-level `index.usda` | Recommends sublayer stacks to model parallel user/computational workstreams | **Full convergence.** Each fragment = one workstream. Artists can work on `model/` while others work on `surface/` without conflicts. |
| **Payload for Heavy Data** | `model/index.usda` uses `payload = @payload.usda@` for geometry | Reference/Payload pattern recommends payloading heavy data, referencing the interface | **Partial convergence.** The project uses payloads correctly but lacks the "lofting" discipline (see divergences). |
| **Model Hierarchy (kind)** | Uses `kind = "component"` for assets, `kind = "group"` for organizational scopes in shots | Recommends component (leaf assets), assembly (aggregate assets), group (organizational) | **Partial convergence.** Correct use of component and group, but no use of `assembly` kind for shot-level aggregation. |
| **Encapsulation** | Assets are self-contained: `assets/odie/index.usda` references `proxy/` and `render/` internally | Encapsulation principle: consumers should only interact with the entry point, not internal structure | **Full convergence.** Internal fragment structure is hidden behind the `index.usda` entry point. |
| **Operational Assets** | Assets include all fragments (geo + materials + skeleton + binding) so they're renderable | Model hierarchy should be "operational" — component models include all dependencies | **Full convergence.** The "always renderable" philosophy directly implements the operational principle. |
| **Purpose Separation** | `proxy/` and `render/` as separate purpose scopes | USD `purpose` attribute is a standard mechanism for LOD/complexity management | **Full convergence.** Standard USD purpose pattern correctly applied. |

### Divergences (Where They Differ)

| Principle | ASWF collectiveproject001 | Learn OpenUSD | Gap Assessment |
|-----------|--------------------------|---------------|----------------|
| **Lofting** | Not implemented. The `index.usda` entry point has no lofted fields above the payload. No `extentsHint`, no lofted variant sets, no `UsdMediaAssetPreviewsAPI`. | Recommends "lofting" — elevating important, inexpensive fields (variant sets, extentsHint, asset thumbnails) above the payload boundary so they're accessible without loading heavy data. | **Significant gap.** In a production scenario with many assets, the lack of lofting means loading all payloads just to query variant options or compute scene bounding boxes. For IEDT with thousands of parts, this is critical. |
| **Reference/Payload Split** | The asset `index.usda` directly references purpose `index.usda` files. The payload sits deeper, inside `model/index.usda`. There's no single interface-vs-contents split at the asset root level. | Recommends a clear two-file pattern: an **interface layer** (referenced by consumers) and a **contents layer** (payloaded by the interface). The interface contains lofted fields; the payload contains the heavy data. | **Structural divergence.** The collectiveproject001 has a multi-level reference chain (asset index → purpose index → fragment sublayers → payload). The Learn OpenUSD pattern is flatter: one interface file + one payload. The multi-level approach offers more granularity but adds composition depth. |
| **Asset Parameterization** | No variant sets or primvars on any asset entry point. No parameterization mechanism. | Recommends variant sets and primvars on the asset entry point for downstream customization (color variants, material switches, LOD selection). | **Missing entirely.** The project has no parameterization. For IEDT, this matters: engineering assets often need configuration variants (material grades, finish options, operating states). |
| **Assembly Kind** | Not used. Shots use `World` with `kind="group"` as the top-level container. | Recommends `assembly` kind for aggregate assets (e.g., a neighborhood containing house components). Assemblies are "important groups" corresponding to aggregate assets. | **Minor gap.** The shot `World` prim could be `kind="assembly"` to distinguish it from organizational groups. For IEDT, `assembly` maps naturally to CAD assembly hierarchies. |
| **Instancing** | Not used. Each element instance (e.g., `odie01`) is a full reference, not a scenegraph instance. | Provides detailed guidance on scenegraph instancing (instanceable flag) and point instancing for repeated assets. | **Not applicable yet** — the project only has one instance of each asset. But for IEDT scenarios (e.g., 500 identical bolts in a factory), instancing would be critical. |
| **Shallow Hierarchy** | Deep composition chain: shot → element → asset → purpose → fragment → payload. That's 6 levels of composition. | Recommends shallow model hierarchies to minimize composition overhead. "A gprim tagged as a component is a sign that a model hierarchy is deep." | **Design trade-off.** The deep structure enables fine-grained parallel work but adds composition cost. Learn OpenUSD warns this can become expensive at scale. |
| **Kind Extensibility** | Uses only built-in kinds (component, group). | Notes that extending the Kind library is possible but risky. Recommends custom properties or schemas over kind extensions for taxonomies. | **Convergence on caution.** Neither over-extends kinds. Good discipline for IEDT where the temptation to create `kind="sensor"` or `kind="robot"` would be strong — better to use custom schemas. |

### Advantages of the ASWF collectiveproject001 Approach

1. **Pipeline-as-Code Reproducibility**
   - The `pipe_genesis.py` scaffold generator creates a fully valid, renderable scene from scratch. The Learn OpenUSD curriculum teaches principles but doesn't provide an equivalent automation tool. For teams starting new projects, this is a massive accelerator.

2. **DCC Integration Pattern (host_wip / host_usd_export)**
   - The explicit `host_wip/` and `host_usd_export/` directories per fragment acknowledge the reality that artists work in DCC tools. Learn OpenUSD focuses on the USD-level patterns but doesn't address where .blend, .ma, or .max files live. The collectiveproject001 pattern keeps source files co-located with their USD outputs.

3. **Shot Assembly as First-Class Pattern**
   - The project demonstrates a complete shot-assembly workflow with per-element overrides (animation, lighting, fx). Learn OpenUSD's curriculum focuses on asset structure but doesn't cover shot/scene assembly in the same depth.

4. **"Always Renderable" Scaffold**
   - Empty placeholders that still form valid USD is a practical production pattern. The Learn OpenUSD curriculum discusses final-state assets but doesn't explicitly address the bootstrapping/scaffolding phase.

5. **Git-Based Simplicity**
   - Using git for versioning instead of USD-level version management reduces cognitive overhead. Learn OpenUSD notes that layer stacks "are not a replacement for asset versioning systems" but doesn't prescribe a specific versioning approach.

### Advantages of the Learn OpenUSD Approach

1. **Lofting for Performance at Scale**
   - The lofting pattern is essential for production scenes with thousands of assets. Without it, loading a scene overview requires loading all payloads. For IEDT with complex factory models, this is a hard requirement.

2. **Reference/Payload Pattern Clarity**
   - The clean two-file split (interface + contents) is more intuitive than the collectiveproject001's multi-level chain. It's easier to explain to new team members and easier to validate.

3. **Asset Parameterization for Reuse**
   - Variant sets and primvars on the entry point enable downstream customization without modifying the asset. For IEDT: configurable equipment states, material grade selections, or operating mode switches.

4. **Instancing for Scale**
   - Scenegraph and point instancing are critical for industrial scenes (repetitive hardware: bolts, brackets, pipes). The collectiveproject001 doesn't address this because it only has unique assets, but the Learn OpenUSD guidance is essential for IEDT.

5. **Model Hierarchy Depth Awareness**
   - The explicit guidance on keeping hierarchies shallow, with the warning about composition cost, is valuable architectural wisdom that the collectiveproject001 doesn't document.

6. **Formal Schema Guidance**
   - The recommendation to use custom schemas over kind extensions for taxonomies is important for IEDT where domain-specific metadata is prevalent (part numbers, tolerances, material certifications).

### Synthesis: Recommended Hybrid for IEDT

For the AOUSD IEDT Interest Group, the optimal approach combines both:

| Aspect | Recommendation | Source |
|--------|---------------|--------|
| **Project scaffolding** | Use `pipe_genesis.py`-style automation | ASWF collectiveproject001 |
| **Asset interface** | Adopt the clean reference/payload pattern with lofting | Learn OpenUSD |
| **Workstreams** | Use fragment-based sublayer stacks | Both (converge) |
| **DCC integration** | Include `host_wip/` and `host_usd_export/` directories | ASWF collectiveproject001 |
| **Parameterization** | Add variant sets for engineering configurations | Learn OpenUSD |
| **Model hierarchy** | Use component + assembly + group; keep shallow | Learn OpenUSD |
| **Instancing** | Plan for scenegraph instancing from the start | Learn OpenUSD |
| **Shot/scenario assembly** | Adapt the element + override pattern for digital twin scenarios | ASWF collectiveproject001 |
| **Versioning** | Git for file versioning + USD metadata for engineering revision IDs | Hybrid |
| **Purpose separation** | Maintain proxy/render split; extend with engineering-specific purposes if needed | Both (converge) |

---

## Finding 10: Three-Way Comparison — GoodStart vs. ASWF collectiveproject001 vs. Learn OpenUSD

This section brings in the **USD GoodStart** approach (https://github.com/jph2/USD_GoodStart) as a third reference point, comparing all three philosophies of structuring OpenUSD projects.

### Identity and Audience of Each Approach

| Aspect | USD GoodStart | ASWF collectiveproject001 | NVIDIA Learn OpenUSD |
|--------|--------------|--------------------------|----------------------|
| **Primary Audience** | 3D artists, tech artists, CAD modelers, non-programmers entering USD | VFX pipeline developers, USD working group contributors | Software engineers, pipeline TDs, USD certification candidates |
| **Heritage** | Digital twin / Omniverse / CAD-to-USD | VFX production pipeline (film/animation) | Canonical USD specification / computer science |
| **Philosophy** | "Just start! Structure comes with you." | "Build the full scaffold, fill in over time." | "Understand the principles, then apply them correctly." |
| **Entry Barrier** | Low — download zip, run setup script, open in Omniverse | Medium — requires Python + pxr SDK to run `pipe_genesis.py` | High — curriculum requires understanding composition theory first |
| **Scope** | Single scene/digital twin setup | Multi-asset, multi-shot VFX project | Individual asset structure principles (no project-level scope) |
| **Primary Host** | Omniverse Kit / Composer | `usdview` / `usdrecord` (any USD runtime) | Host-agnostic (pure USD specification) |

### Structural Comparison

#### Layer Stack Philosophy

| Aspect | USD GoodStart | ASWF collectiveproject001 | Learn OpenUSD |
|--------|--------------|--------------------------|---------------|
| **Root file** | `USD_GoodStart_ROOT.usda` — single root with 11 sublayers for a complete scene | `shots/s001_001/index.usda` — shot root with 6 sublayers + referenced elements | No project root prescribed — focuses on individual asset interface files |
| **Layer naming** | Human-readable suffixes: `OPIN_LYR`, `MTL_LYR`, `ASS_LYR`, `SIM_LYR`, `DATA_LYRs` | Generic: `index.usda` everywhere (context from folder path) | No naming convention prescribed |
| **Layer intent** | Each layer has one clear purpose (opinion, material, asset, animation, simulation, data, etc.) | Layers grouped by concern (fragments within asset, overrides within shot) | Recommends "workstreams" — each layer = one parallel work contribution |
| **Strongest → Weakest** | OPIN → CAM → ENV → SIM → DATA → ACTGR → ANIM → VAR → MTL → PHY → ASS | rendersettings → fx → lighting → animation → renderPasses → lightRig (shot-level) | Not prescribed at project level — principle: "sublayer order = opinion strength" |

#### Where GoodStart Excels

**1. Omniverse-Native Integration**
GoodStart ships with `customLayerData` containing Omniverse camera settings, `omni_layer` metadata for lock/mute states, render settings, and environment/lighting that "just works" when opened in Omniverse Kit. Neither collectiveproject001 nor Learn OpenUSD addresses Omniverse-specific metadata.

**2. "Safe Mode" — Layer Locking as Default**
All persistent layers are locked by default; the session layer is the authoring layer. This prevents accidental edits in the wrong layer — a practical production guard that neither of the other two approaches includes.

**3. Digital Twin Data Layers (`040_DATA_LYRs/`)**
GoodStart has first-class support for PLM/ERP/AAS/OPC UA data integration as a dedicated layer group. The collectiveproject001 is purely VFX (no data integration). Learn OpenUSD doesn't address external data systems.

**4. Source File Management (`000_SOURCE/`)**
A dedicated directory for original CAD/DCC source files, separate from USD outputs. This is similar to collectiveproject001's `host_wip/` concept but elevated to project level.

**5. CAD Workflow Focus (USD_Startpoint)**
The `010_ASS_USD/USD_Startpoint/` pattern provides stable, named entry points for DCC exports. The name doesn't change even when the asset is updated, giving upstream references stability. collectiveproject001 has `host_usd_export/` at the fragment level (deeper, per-fragment). Learn OpenUSD doesn't address DCC export workflow.

**6. Explicit Anti-Pattern Documentation**
GoodStart documents the "Root Layer Trap" (putting geometry/transforms in the root file, making them un-overridable), the "Inline Geometry" anti-pattern, and the "Direct References bypassing Payloads" anti-pattern. This teaching-by-warning approach is unique.

**7. Session Layer Workflow**
GoodStart explicitly teaches the session-layer-as-scratchpad pattern: "work in session layer, then promote stable edits to persistent layers." This is a practical Omniverse workflow not covered by the others.

**8. Setup Script Automation**
The `setup_usd_project.py` / `.bat` generates the complete project from a few questions (default prim name, unit system, include samples?). collectiveproject001 has `pipe_genesis.py` for a similar purpose but requires Python/pxr knowledge. Learn OpenUSD has no generation tooling.

#### Where GoodStart Has Gaps (Relative to the Others)

**1. No Per-Asset Fragment Decomposition**
GoodStart uses scene-level layers (one `MTL_LYR.usda` for all materials, one `ASS_LYR.usda` for all asset imports). The collectiveproject001 has per-asset, per-purpose, per-fragment layers (`assets/odie/render/surface/index.usda`). For multi-asset projects with teams, GoodStart's single-layer-per-concern can become a merge bottleneck.

**2. No Multi-Asset / Multi-Shot Structure**
GoodStart is scoped to a single scene. There's no concept of `assets/` vs `shots/` as separate hierarchies, no element-level override stacks, no shot assembly pattern. collectiveproject001 provides the full VFX shot-assembly architecture.

**3. No Purpose Separation (proxy/render)**
GoodStart doesn't implement the proxy/render purpose split. For large digital twin scenes, this means no way to have a lightweight representation for navigation and a heavy one for rendering. collectiveproject001 and Learn OpenUSD both address this.

**4. Model Hierarchy (`kind`) Not Emphasized**
GoodStart's root file uses `def Xform "World"` without `kind` metadata. The collectiveproject001 sets `kind="component"` and `kind="group"` properly. Learn OpenUSD teaches the full component/assembly/group/subcomponent taxonomy. For scene traversal performance at scale, this matters.

**5. Lofting Documented but Not Implemented in Structure**
GoodStart's README documents the reference/payload pattern with lofting, but the actual project files (e.g., `USD_GoodStart_m_ROOT.usda`) have inline geometry (a Cube mesh, Environment with ground plane, lights, and materials all in the root file). This contradicts the "thin root" principle that GoodStart itself documents. The README acknowledges this is a learning template, but the gap between documented principle and actual file content is notable.

**6. Heavy Root File**
`USD_GoodStart_m_ROOT.usda` contains ~410 lines including: a cube mesh, environment with dome light + distant light + ground mesh + materials, render products/settings, and camera overrides. The README explicitly says "Root File Must Be Thin" and "NO geometry, references, payloads, or attribute values" — this is a known teaching vs. template tension. The collectiveproject001's root files are genuinely thin.

### Convergence Points (All Three Agree)

| Principle | GoodStart | collectiveproject001 | Learn OpenUSD |
|-----------|-----------|---------------------|---------------|
| **Sublayers for workstreams** | 11 sublayers, one per concern | Fragments sublayered per purpose | Recommends sublayer stacks for parallel work |
| **Payloads for heavy data** | Documented pattern: interface + payload | Implemented: `model/index.usda` → `payload.usda` | Core teaching: reference/payload pattern |
| **Relative paths** | All sublayer references are relative | All USD references are relative | Recommends relative paths for portability |
| **Setup automation** | `setup_usd_project.py` | `pipe_genesis.py` | Not provided (teaches principles, not tooling) |
| **"Start structured"** | Explicit philosophy | Implicit in scaffold design | Explicit in curriculum design |
| **Composition strength awareness** | LIV(E)RPS documented + anti-pattern warnings | Sublayer order deliberately chosen | Full LIVERPS curriculum |

### Divergence Points (Three Different Answers)

| Question | GoodStart | collectiveproject001 | Learn OpenUSD |
|----------|-----------|---------------------|---------------|
| **How many layers per scene?** | 11 named layers (flat) | Dozens (deep, nested per asset/purpose/fragment) — see [File Tree Reference](#file-tree-reference-complete) and [Composition Arc Diagram](#composition-arc-diagram) for the full per-asset layer depth | As few as needed; don't let stacks grow procedurally |
| **Where does geometry live?** | `ASS_LYR.usda` references `010_ASS_USD/USD_Startpoint/` | `assets/*/render/model/payload.usda` | Behind a payload arc in the asset's contents layer |
| **How are materials managed?** | `MTL_LYR.usda` references `MatLib/` | `surface/index.usda` per purpose per asset | Not specifically addressed at project level |
| **How is the project versioned?** | No explicit versioning strategy | Git-only, version = "latest" | Not addressed (asset-level concern) |
| **What about the host DCC?** | `000_SOURCE/` for originals, `USD_Startpoint/` for exports | `host_wip/` + `host_usd_export/` per fragment | Not addressed |
| **What about digital twin data?** | `040_DATA_LYRs/` — first-class layer group | Not addressed (VFX focus) | Not addressed (asset-level focus) |
| **Multi-user collaboration?** | Session layer isolation + layer locking | Git branches + fragment-per-artist | Layer stacks model parallel workstreams |

> **Layer Depth Detail:** The collectiveproject001 per-asset composition depth is visualized in two places in this document: the **[File Tree Reference (Complete)](#file-tree-reference-complete)** (line ~626) shows every file in the hierarchy, and the **[Composition Arc Diagram](#composition-arc-diagram)** (line ~721) traces the full chain from shot root through element → asset → purpose → fragment → payload — 6 composition levels deep.

### IEDT-Specific Nuances: Shot Assembly and Proxy/Render in a Digital Twin Context

#### "Shots" Don't Exist in IEDT — But the Pattern Does

The VFX concept of a "shot" (a camera angle in a sequence with a time range) has no direct equivalent in industrial digital twins. However, the **structural pattern underneath** is highly transferable:

| VFX Concept | IEDT Equivalent | Why It Matters |
|------------|----------------|----------------|
| Shot | **Scenario / Configuration** | A factory inspection scenario, an operational monitoring view, a maintenance training scene — each is a "configured view" of the same assets with different overrides |
| Shot element (e.g., `odie01`) | **Asset instance with state overrides** | A robot arm in a specific pose, a valve in open/closed state, a conveyor at a specific speed — each is the base asset + scenario-specific overrides |
| Per-element animation layer | **Per-instance telemetry / state layer** | IoT sensor data, joint positions, operating parameters — layered on top of the base asset per instance |
| Shot-level lighting | **Environment conditions** | Day/night, weather, seasonal lighting — scenario-level overrides |
| renderPasses / renderSettings | **Visualization presets** | Thermal overlay, stress visualization, normal operation view — different rendering configurations |

The key insight: **the shot-assembly pattern is not about VFX storytelling — it's about composing a configured instance of shared assets with context-specific overrides.** That is exactly what a digital twin scenario needs. The terminology is different, the architecture is the same.

**Recommendation for IEDT:** Adopt the element-override-stack pattern (asset reference + sublayered overrides per instance), but use IEDT vocabulary: "scenario" instead of "shot", "configuration" instead of "element", "state" instead of "animation".

#### Proxy/Render Purpose: The LOD Reality for Engineering Scenes

The VFX proxy/render split works in film because:
- **Proxy** = simplified geometry for viewport navigation (low-poly stand-in)
- **Render** = full geometry for final frame rendering
- Both are loaded but only one is visible at a time, controlled by the `purpose` attribute

For IEDT digital twins, this pattern has a **critical limitation**: USD's `purpose` mechanism does not provide true LOD (Level of Detail) switching. Both proxy and render geometry are **always loaded into memory** — the viewer simply chooses which to display. This means:

| Proxy Strategy | Memory Impact | Visual Quality | Practical Use |
|----------------|--------------|----------------|---------------|
| **Bounding box** (pure bbox extent) | Minimal — just the `extentsHint` above the payload, no geometry needed | Rectangle only | Best for large-scale overview (1000+ parts). Use `extentsHint` lofted above payload — no proxy geometry file needed at all |
| **Simplified mesh** (decimated CAD) | Full mesh still loaded — defeats the purpose of "lightweight" | Recognizable shape | Only useful if the proxy is dramatically smaller than render (e.g., 100 triangles vs 100,000). For typical CAD parts the ratio is often not dramatic enough |
| **LOD system** (multiple detail levels) | All LOD levels loaded unless behind separate payloads | Scalable quality | Best approach: use **variant sets** with LOD options, each behind its own payload, so only the selected LOD is loaded |

**Recommended IEDT approach — use payloads, not purposes, for LOD:**

```
{asset_name}/
├── {asset_name}.usda              # Interface with lofted extentsHint + LOD variant set
├── lod_high/
│   └── payload.usdc               # Full CAD geometry
├── lod_medium/
│   └── payload.usdc               # Simplified geometry
└── lod_low/
    └── payload.usdc               # Minimal geometry (or omit — use extentsHint bbox)
```

The asset interface lofts the LOD variant set above the payload:

```usda
def Xform "RobotArm" (
    assetInfo = { ... }
    kind = "component"
    variantSets = ["lod"]
    variants = { string lod = "high" }
)
{
    variantSet "lod" = {
        "high" {
            def Scope "geo" ( payload = @./lod_high/payload.usdc@ ) { }
        }
        "medium" {
            def Scope "geo" ( payload = @./lod_medium/payload.usdc@ ) { }
        }
        "low" {
            def Scope "geo" ( payload = @./lod_low/payload.usdc@ ) { }
        }
    }
}
```

**Why this is better than proxy/render for IEDT:**
- Only the **selected** LOD variant's payload is loaded — the others don't consume memory
- LOD selection can be changed per-instance in the scenario layer
- `extentsHint` is available without loading any payload (for overview/bbox mode)
- No wasted memory from a proxy mesh that's always loaded alongside the render mesh
- Works with any USD viewer, not just those that implement purpose filtering

**When to still use the proxy/render purpose pattern:**
- If your viewer specifically optimizes for `purpose` (e.g., Omniverse Storm can skip render-purpose prims in interactive mode)
- If you need proxy for physics/collision (different geometry that's always available for simulation regardless of visual LOD)
- If your proxy is truly trivial (e.g., generated bounding box mesh — essentially zero overhead)

---

### When to Use Which

#### Use **USD GoodStart** when:
- You're new to OpenUSD and need to get started fast
- Your project is a single digital twin scene (one product, one factory floor, one building)
- Omniverse is your primary runtime / viewer
- You're coming from a CAD/artist background, not a VFX pipeline background
- You need PLM/ERP/AAS/OPC UA data integration from the start
- Your team is small (1-3 people) and merge conflicts aren't a major concern
- You want a working scene in Omniverse in minutes, not days
- You want to learn USD composition by example in a safe, locked-down environment

#### Use **ASWF collectiveproject001** when:
- You're building a multi-asset, multi-shot/scenario project
- Multiple artists need to work on different fragments of the same asset in parallel
- You need the VFX production pipeline pattern (shot assembly + element overrides)
- You want a programmatic scaffold generator that can be adapted to any project shape
- You need purpose-based rendering (proxy vs. render) for large scenes
- You're building a USD pipeline for a studio or organization, not a single project
- Render-delegate portability matters (not tied to Omniverse)

#### Use **NVIDIA Learn OpenUSD** principles when:
- You need to design a production asset structure from scratch
- You're building tooling that creates or consumes assets (converters, validators)
- You need to understand *why* a pattern works, not just *how*
- Performance at scale is critical (lofting, instancing, shallow hierarchies)
- Interoperability is a hard requirement (your assets must work in any USD-capable tool)
- You're defining asset standards for an organization or industry group (like IEDT IG)

#### Combine all three when:
- You're building an IEDT digital twin pipeline: use **GoodStart** for rapid prototyping and Omniverse integration, apply **Learn OpenUSD** principles for the asset-level structure, and adopt **collectiveproject001's** shot-assembly pattern for multi-scenario digital twin configurations.

### What Each Can Learn from the Others

#### GoodStart can learn from collectiveproject001:
1. **Per-asset fragment decomposition** — Break out of single-layer-per-concern to enable per-asset parallel work
2. **Purpose separation (proxy/render)** — Add LOD management for large scenes
3. **Model hierarchy discipline** — Add `kind` metadata to enable efficient traversal
4. **Thin root files** — Align practice with documented principle (move inline geometry out)
5. **Element-level override stacks** — For multi-instance digital twin scenarios

#### GoodStart can learn from Learn OpenUSD:
1. **Lofting implementation** — Move from documenting lofting to implementing it in the actual asset structure
2. **Asset parameterization** — Add variant set and primvar patterns to asset entry points
3. **Shallow hierarchy awareness** — Monitor composition depth as projects grow
4. **Instancing patterns** — Add scenegraph instancing guidance for repeated equipment
5. **Kind extensibility caution** — Use custom schemas for engineering taxonomy instead of kind extensions

#### collectiveproject001 can learn from GoodStart:
1. **Omniverse-native metadata** — Add `customLayerData` for Omniverse compatibility
2. **Layer locking ("Safe Mode")** — Protect layers from accidental edits
3. **Digital twin data layers** — Add first-class support for PLM/ERP/IoT data
4. **Source file management** — Elevate `host_wip/` to a more visible pattern
5. **Session layer workflow** — Document session-layer-as-scratchpad for interactive authoring
6. **Anti-pattern documentation** — Teach what NOT to do, not just what to do
7. **DCC export workflow clarity** — Better document how CAD/DCC tools feed into the pipeline

#### collectiveproject001 can learn from Learn OpenUSD:
1. **Lofting above payloads** — Add `extentsHint`, lofted variant sets, `UsdMediaAssetPreviewsAPI`
2. **Asset parameterization** — Add variant sets to asset entry points
3. **Assembly kind** — Use `kind="assembly"` for aggregate assets and shots
4. **Instancing** — Plan for scenegraph and point instancing in the scaffold generator
5. **Hierarchy depth awareness** — Document the composition cost trade-off of the deep fragment chain

#### Learn OpenUSD can learn from both GoodStart and collectiveproject001:
1. **Project-level scope** — The curriculum stops at asset structure; real users need project/scene/shot patterns too
2. **Setup automation** — A scaffold generator would dramatically lower the entry barrier for the curriculum
3. **DCC integration patterns** — Where do artist working files live? Where do DCC exports go?
4. **Digital twin / IEDT patterns** — The curriculum is VFX-centric; engineering use cases need coverage
5. **"Safe Mode" concept** — Teaching protective workflow habits alongside structural principles
6. **Practical anti-patterns** — The "Root Layer Trap" is a common mistake worth including in the curriculum

---

## Finding 11: CAD-to-OpenUSD — The Missing First Mile (nAurava Technologies / OpenUSD Study Group)

> **Repository:** https://github.com/nAurava-Technologies/CAD-to-OpenUSD
> **Authors:** Matias Codesal (NVIDIA), Nandu (nAurava Technologies), OpenUSD Study Group contributors
> **License:** Apache-2.0
> **Context:** This repo emerged from the same AOUSD / OpenUSD study group ecosystem that the IEDT IG participates in. Nandu (a fellow IEDT IG member) is directly involved.

### What It Is

CAD-to-OpenUSD is a **STEP-to-USD conversion pipeline** that wraps the NVIDIA HOOPS-based CAD converter (`omni.services.convert.cad`) inside a standalone Kit application. It takes a STEP file (the lingua franca of CAD interchange) and produces a `.usd` file via an automated, scriptable process.

### Architecture Overview

```
CAD-to-OpenUSD/
├── src/cad2usd/
│   └── __init__.py          # Python CLI entry point (uv run cad2usd)
├── kit/
│   ├── source/apps/
│   │   └── ovcommunity.converter.kit  # Kit app definition (loads omni.kit.converter.cad)
│   ├── premake5.lua         # Build system (defines "ovcommunity.converter.kit")
│   ├── repo.toml            # Kit SDK build configuration (v108.1.0)
│   ├── repo.bat / repo.sh   # Build scripts
│   └── templates/           # Kit template scaffolding
├── prod/lib/actors/
│   └── nova_carter/         # Production asset library (STEP source)
├── config.json              # HOOPS converter configuration
├── nova_carter_full.step    # Sample input (NVIDIA Nova Carter robot)
├── pyproject.toml           # Python project (uv, usd-core>=25.8)
└── docs/                    # Sphinx documentation skeleton
```

### Technical Analysis

#### The Conversion Pipeline

The converter follows a straightforward chain:

1. **Input:** `.step` file (CAD assembly)
2. **Engine:** HOOPS Exchange via `omni.services.convert.cad` Kit extension
3. **Orchestration:** `cad2usd` Python CLI wraps Kit headless execution
4. **Configuration:** `config.json` controls tessellation, instancing, materials, and axis
5. **Output:** Single `.usd` file

**Key `config.json` parameters and what they mean for IEDT:**

| Parameter | Value | IEDT Significance |
|-----------|-------|-------------------|
| `tessLOD` | `2` | Tessellation detail level — controls mesh density from CAD NURBS |
| `instancingStyle` | `2` | Enables USD instancing for repeated parts (critical for assemblies) |
| `dedup` | `true` | Deduplicates identical geometry (reduces file size) |
| `useMaterials` | `true` | Preserves CAD material assignments |
| `useNormals` | `true` | Preserves surface normals |
| `convertMetadata` | `false` | **Currently off** — CAD metadata (part names, properties) not carried over |
| `convertHidden` | `false` | Hidden parts skipped |
| `dMetersPerUnit` | `0.0` | Auto-detect units from CAD |
| `bOptimize` | `true` | Mesh optimization enabled |

#### The Kit Application Pattern

The `.kit` file (`ovcommunity.converter.kit`) defines a **full headless Kit application** based on Kit SDK 108.1.0. It pulls in:
- `omni.kit.converter.cad` — the core CAD conversion extension (HOOPS-based)
- A full set of Omniverse extensions (hydra, RTX, physics, materials, viewport)
- Version-locked dependencies for reproducibility

This is a **Kit-as-a-tool** pattern — using the Kit SDK not as a visual application but as a headless conversion engine. The CLI entry point (`src/cad2usd/__init__.py`) finds the built Kit executable, locates the HOOPS conversion script dynamically, and invokes it with the STEP input.

#### The Production Library Pattern

The `prod/lib/actors/nova_carter/` directory hints at a production asset library structure:
```
prod/
└── lib/
    └── actors/
        └── nova_carter/
            └── nova_carter_full.step
```
This is an early-stage library structure where source CAD files are organized by type (`actors` = movable/robotic assets) — a pattern that could grow into a full asset library with categories like `structures/`, `equipment/`, `sensors/`.

### What This Adds to the Four-Way Comparison

The three approaches analyzed so far (GoodStart, collectiveproject001, Learn OpenUSD) all **start with USD files already existing**. None of them address the critical question: **how does geometry get from CAD into USD in the first place?**

CAD-to-OpenUSD fills this gap — it is the **"first mile"** of the IEDT pipeline.

| Dimension | GoodStart | collectiveproject001 | Learn OpenUSD | **CAD-to-OpenUSD** |
|-----------|-----------|---------------------|---------------|-------------------|
| **Starting point** | Empty USD scene | DCC exports (Blender/Maya) | Conceptual asset | **STEP file (CAD)** |
| **Primary concern** | Scene composition & layers | Multi-asset production workflow | Asset structure principles | **Geometry conversion** |
| **Automation** | `setup_usd_project.py` | `pipe_genesis.py` | (conceptual) | **`uv run cad2usd`** |
| **Runtime** | Omniverse | Any USD viewer | Any USD viewer | **Kit SDK (headless)** |
| **Instancing** | Not addressed | Manual (in fragments) | Documented principle | **Automatic (`instancingStyle=2`)** |
| **Metadata preservation** | Omniverse-native metadata | Asset-level `assetInfo` | Principle-level guidance | **Configurable (currently off)** |
| **Output** | Project scaffold | Per-asset layer tree | N/A (educational) | **Single .usd file** |

### Key Insights for the IEDT IG

#### 1. The CAD→USD Gap Is Real and Critical

For the IEDT IG's "focal use case" goal, the pipeline must start from CAD data (OnShape, SolidWorks, CATIA, etc.), not from artist-created meshes. CAD-to-OpenUSD provides a concrete, working solution for STEP→USD conversion. This is the piece that makes the entire GoodStart → Learn OpenUSD → collectiveproject001 chain practical for engineering workflows.

#### 2. Metadata Conversion Is the Next Frontier

The `convertMetadata: false` setting is telling. Today, the converter focuses on geometry fidelity — getting the meshes right with proper tessellation, instancing, and deduplication. But for IEDT, **CAD metadata is as valuable as geometry**: part numbers, assembly hierarchy names, material certifications, tolerance annotations, and custom properties. Turning this on and mapping it to USD `customData` or `assetInfo` would be a significant IEDT advancement.

#### 3. Tessellation LOD Creates a Natural Entry Point for LOD Variant Sets

The `tessLOD` parameter (currently `2`) controls mesh density. Running the converter at multiple tessLOD settings and packaging the results as variant sets would directly implement the LOD-via-variant-sets pattern recommended in Finding 2 and the IEDT Nuances section:

```
# Hypothetical multi-LOD pipeline
uv run cad2usd --tess-lod 3 --output robot_arm_lod_high.usd
uv run cad2usd --tess-lod 2 --output robot_arm_lod_medium.usd
uv run cad2usd --tess-lod 1 --output robot_arm_lod_low.usd
# → Package into variant set with payloads per LOD
```

#### 4. The Kit-as-a-Tool Pattern Is Reusable

Using Kit SDK headlessly as a conversion engine (not a visual app) is a powerful pattern for IEDT automation. The same approach could power:
- Automated validation pipelines (load USD, run checks, report)
- Batch rendering (load scene, render product shots, export EXR)
- Metrics collection (load assembly, measure poly count / composition depth)

#### 5. The Production Library Structure Needs Growth

The `prod/lib/actors/` structure is embryonic but directional. For IEDT, this could evolve into:

```
prod/
└── lib/
    ├── actors/          # Robots, AGVs, moving equipment
    ├── structures/      # Buildings, cells, workstations
    ├── equipment/       # Conveyors, presses, CNC machines
    ├── sensors/         # Cameras, LiDAR, IoT devices
    └── environments/    # Factory floors, warehouses
```

### IEDT Relevance

**Direct relevance: HIGH.** This is the only repo in the comparison that addresses the CAD→USD conversion problem, which is the first step in every engineering digital twin pipeline. For the IEDT IG's work:

- **Nandu's involvement** means direct feedback loop between IEDT IG requirements and converter development
- The **STEP→USD** path covers the most common CAD interchange format
- The **Kit-headless pattern** enables CI/CD integration (convert on commit, validate on merge)
- The **`config.json`** approach makes conversion reproducible and auditable

### What CAD-to-OpenUSD Can Learn from the Others

1. **From GoodStart:** Post-conversion, the output USD needs to land inside a proper scene structure. A pipeline that runs `cad2usd` → then places the output into a GoodStart scaffold (with proper references/payloads) would be the ideal end-to-end flow.
2. **From collectiveproject001:** The output could be decomposed into fragments (model, surface, binding) rather than a single monolithic USD file — enabling parallel refinement of materials vs. geometry.
3. **From Learn OpenUSD:** The converted assets should have proper `kind` metadata, `assetInfo`, and `extentsHint` lofted above payloads. Currently, the converter likely doesn't add these.

### What the Others Can Learn from CAD-to-OpenUSD

1. **GoodStart:** Should document (or script) a recommended CAD import workflow — "run cad2usd, place output in `010_ASS_USD/`, reference from `ASS_LYR.usda`".
2. **collectiveproject001:** The `host_wip/` → `host_usd_export/` pattern could be extended with a `cad_source/` + `cad_converted/` convention for engineering assets.
3. **Learn OpenUSD:** The curriculum should include a "CAD to USD" section addressing tessellation quality, metadata preservation, and assembly hierarchy mapping.

### Forward Reference: OpenUSD GoodStart ComfyUI Nodes — A Visual "First Mile" Alternative

> **Repository:** https://github.com/jph2/OpenUSD_GoodStart_ComfyUI_nodes (by Jan Haluszka, AOUSD IEDT IG member)
> **Status:** v1.0.4, implemented but **not yet tested end-to-end** — planned for integration into the USD GoodStart ecosystem.

While CAD-to-OpenUSD provides a **CLI-driven STEP→USD pipeline**, the OpenUSD GoodStart ComfyUI Nodes project takes a fundamentally different approach: **visual, node-based USD workflows** built on top of [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

**What it provides:**

- **82-83 ComfyUI nodes** for USD operations, organized into 19 categories covering the full USD lifecycle:
  - Core: Stage management, prim operations, transforms, materials, variants, metadata
  - Advanced: Composition arcs, LOD management, asset pipeline, geometry operations, scene decomposition, animation, lighting, physics, batch processing
  - Import/Conversion: Direct DCC import nodes for **Blender, Maya, 3ds Max, Rhino, Cinema 4D** (headless background conversion)
  - Multi-Export integration: Dedicated loader nodes for the **Blender USD MultiExport** and **Rhino USD MultiExport** addons (push-model with full traceability)

**Two conversion models for the "first mile":**

| Approach | How It Works | Best For |
|----------|-------------|----------|
| **Direct conversion** (nodes `19_01`-`19_06`) | Launches DCC tool headlessly, runs USD export operator, loads result | Quick one-off conversions from native DCC formats |
| **Multi-Export loader** (nodes `19_01b`, `19_05b`) | Reads export endpoint definitions from CAD file, loads pre-exported USD files with origin metadata | Production pipelines where the DCC addon defines what gets exported and where |

**Why this matters for IEDT:**

1. **Visual pipeline building** — Non-programmers (engineers, designers) can construct CAD→USD→scene workflows by connecting nodes, lowering the barrier to entry dramatically
2. **Multi-DCC coverage** — While CAD-to-OpenUSD focuses on STEP (via HOOPS), ComfyUI nodes cover Blender, Maya, Max, Rhino, and Cinema 4D directly, catching the DCC tools commonly used for CAD visualization
3. **Post-conversion operations in the same workflow** — After import, the same visual pipeline can apply materials (OpenPBR/MaterialX), set up composition arcs, manage LODs, add metadata — all without scripting
4. **Traceability** — The Multi-Export loader nodes preserve full provenance (source file, timestamp, user, export endpoint ID) — critical for engineering audit trails
5. **ComfyUI as workflow engine** — ComfyUI is data-agnostic; it's effectively a visual scripting environment. Using it for USD means the same tool that drives AI/generative workflows can also drive engineering USD pipelines

**Relationship to CAD-to-OpenUSD:**

These are complementary, not competing approaches:
- **CAD-to-OpenUSD** = headless CLI for automated STEP→USD in CI/CD pipelines
- **ComfyUI Nodes** = visual node graph for interactive, multi-step DCC→USD→scene workflows
- A future integration could have a ComfyUI node that wraps `cad2usd` as a step in a visual pipeline

---

## Resume: Key Takeaways for the AOUSD IEDT Interest Group

> **Quick path:** For the short version, see the [Executive Summary](#executive-summary) at the top of this document.

### The Big Picture

All four approaches implement or feed into the same fundamental OpenUSD composition mechanics (sublayers, references, payloads, kinds). They diverge in **scope** (conversion vs. asset vs. scene vs. project), **audience** (engineers vs. artists vs. pipeline developers), and **philosophy** (convert first vs. start simple vs. start complete vs. start correct).

### The Practical Recommendation

For the IEDT Interest Group's goal of creating a focal use case and minimal production asset:

1. **Convert CAD data with CAD-to-OpenUSD** — Get geometry from STEP into USD with proper instancing and tessellation. This is the first mile that makes everything else possible for engineering workflows. Enable metadata conversion when available.

2. **Start with GoodStart's philosophy** — Get a working scene fast. Place converted assets into a GoodStart scaffold with proper references. The digital twin data layer integration (`040_DATA_LYRs/`) is directly relevant to IEDT. The "just start" mentality gets prototypes into stakeholders' hands early.

3. **Structure assets per Learn OpenUSD principles** — Each engineering asset should follow the reference/payload pattern with lofting. Use `kind` metadata properly. Implement parameterization for configuration variants. Plan instancing for repeated parts.

4. **Adopt collectiveproject001's assembly pattern for scenarios** — When the IEDT group moves from a single use case to multi-scenario digital twins (inspection scenario, operational scenario, maintenance scenario), the shot-assembly pattern with per-element overrides is the right architecture.

5. **Fill the gaps none of them cover** — IEDT needs engineering-specific patterns not addressed by any of the four:
   - CAD metadata mapping to USD properties (part numbers, tolerances, material certifications)
   - IoT/sensor data binding to USD prims
   - Regulatory compliance versioning (as-designed vs. as-built vs. as-maintained)
   - Cross-domain data referencing (USD metadata pointing to external BOM/PLM systems)
   - Semantic governance and data integration — how to give USD prims engineering meaning and connect them to live systems. The [Composable Bindings whitepaper](https://aka.ms/ComposableBindings) (NVIDIA/Microsoft, 2025) defines the integration pattern; the companion research [`AAS_OPC_OpenUSD_RESEARCH_v12.md`](../../AAS_OPC_OpenUSD_INTEGRATION/docs/AAS_OPC_OpenUSD_RESEARCH_v12.md) investigates how to combine it with AAS (Asset Administration Shell) and OPC UA for a full governance-to-visualization architecture

### One-Sentence Per Approach

- **CAD-to-OpenUSD**: "The first mile — get geometry from CAD into USD with proper tessellation, instancing, and (soon) metadata."
- **GoodStart**: "The fastest path from zero to a working digital twin scene in Omniverse — start here, grow beyond it."
- **collectiveproject001**: "The VFX production pattern that proves multi-asset, multi-scenario USD workflows work — adopt its assembly architecture."
- **Learn OpenUSD**: "The canonical principles that ensure your asset structure scales, performs, and interoperates — let it be your quality standard."

---

## GoodStart Evolution Plan — Closing the Gaps

This plan identifies concrete improvements to the USD GoodStart project, informed by the three-way comparison above. Improvements are grouped into phases. Each phase builds on the previous one and maintains GoodStart's core strength: **any team member can run the setup script (`setup_usd_project.py`) and get a valid, working project instantly**.

All changes described below are modifications or extensions to the existing `setup_usd_project.py` script and its generated output. The script remains the single source of truth for project generation.

### Design Principles for the Evolution

1. **Backward compatible** — Existing GoodStart projects must not break. New features are opt-in via script flags or menu choices.
2. **Script-first** — Every structural improvement must be expressible through `setup_usd_project.py`. If it can't be automated, it shouldn't be in the template.
3. **Incremental adoption** — Users can start with Phase 0 (current) and progressively opt into more advanced features as their project grows.
4. **Omniverse-native** — All generated USD must open correctly in Omniverse Kit without modification.

---

### Phase 0: Current State (v0.9.5.1)

**What exists today:**
- Setup script generates folder structure + 11 sublayers + root file
- Single-scene scope with named layers (OPIN, CAM, ENV, SIM, DATA, ACTGR, ANIM, VAR, MTL, PHY, ASS)
- Omniverse metadata (camera settings, layer locking, render settings)
- Safe Mode defaults (all layers locked, session layer as authoring layer)
- Scale choice (m, cm, mm)
- Optional sample content (cube, environment, camera)

**Known gaps** (from Finding 10):
- [ ] Root file contains inline geometry (contradicts documented "thin root" principle)
- [ ] No `kind` metadata on prims
- [ ] No per-asset fragment structure
- [ ] No proxy/render purpose split
- [ ] No lofting implementation
- [ ] No asset parameterization (variant sets / primvars on entry points)
- [ ] No multi-asset / multi-scene architecture
- [ ] No instancing patterns

---

### Phase 1: Thin Root + Kind Discipline (Low Effort, High Impact)

**Goal:** Align generated files with GoodStart's own documented best practices.

**REQ-GS-1.1: Thin Root File**
- Modify `_get_root_template_content()` in `setup_usd_project.py` to generate a root file containing ONLY:
  - `customLayerData` (Omniverse metadata)
  - `defaultPrim`, `metersPerUnit`, `upAxis`, `timeCodesPerSecond`
  - `subLayers` array
  - `def Xform "{default_prim}"` — empty, no geometry
- Move the sample cube geometry into `ASS_LYR.usda` (where it belongs per GoodStart's own layer intent)
- Move Environment (dome light, distant light, ground plane, materials) into `ENV_LYR.usda`
- The root file should be under 50 lines

**REQ-GS-1.2: Kind Metadata**
- Add `kind = "group"` to the root prim (`def Xform "{default_prim}"`)
- Add `kind = "component"` to sample assets when generated
- Document kind usage in the generated `020_BASE_LYR/README.md`

**REQ-GS-1.3: Setup Script Flag**
- Add `--thin-root` flag (or make it the default in v1.0+)
- Preserve current behavior as `--legacy-root` for backward compatibility

**Impact:** Fixes the principle-vs-practice tension. Makes the generated output a genuine teaching example.

---

### Phase 2: Per-Asset Structure + Reference/Payload Pattern (Medium Effort, High Impact)

**Goal:** Enable assets to be self-contained, payloaded, and lofted.

**REQ-GS-2.1: Asset Directory Convention**
- When the user adds an asset via the script (or a future `add_asset.py` helper), generate:

```
010_ASS_USD/USD_Startpoint/{asset_name}/
├── {asset_name}.usda           # Asset interface (entry point, lightweight)
├── {asset_name}_payload.usdc   # Heavy geometry (payload target)
└── host_wip/                   # DCC working files (optional, .keep)
```

- The `{asset_name}.usda` interface file contains:
  - `assetInfo` (identifier, name, version)
  - `kind = "component"`
  - `payload = @./{asset_name}_payload.usdc@`
  - Lofted fields: `extentsHint`, variant sets (if any), primvars (if any)

**REQ-GS-2.2: Lofting Helper**
- Add `scripts/loft_asset.py` that reads a payload file and generates/updates the interface file with:
  - `extentsHint` computed from payload geometry bounds
  - Variant set stubs mirrored from payload variant sets
  - Any primvars prefixed with `asset_` promoted to the interface
- This can be run as a post-process after DCC export, or integrated into CI

**REQ-GS-2.3: ASS_LYR.usda Update**
- Modify the `ASS_LYR.usda` template to reference asset interface files (not payload files directly):

```usda
over "{default_prim}"
{
    def Xform "AssetA" (
        kind = "component"
        prepend references = @../010_ASS_USD/USD_Startpoint/AssetA/AssetA.usda@
    )
    {
    }
}
```

**REQ-GS-2.4: Setup Script Integration**
- Add interactive prompt: "How many assets do you want to set up?" (default: 2 placeholders, A and B)
- Generate the per-asset directory structure for each
- Update `ASS_LYR.usda` with references to each asset interface file

**Impact:** Brings GoodStart into alignment with the Learn OpenUSD reference/payload pattern. Enables payload unloading for large scenes. Provides the lofting infrastructure.

---

### Phase 3: LOD via Variant Sets + Payloads (Medium Effort, Medium Impact)

**Goal:** Enable lightweight scene browsing for large digital twin scenes without the memory overhead of the VFX proxy/render pattern.

> **Design Decision:** The VFX proxy/render `purpose` split (as used in collectiveproject001) is **not recommended as the primary LOD mechanism for IEDT**. USD `purpose` does not unload geometry — both proxy and render meshes are always in memory. For engineering scenes with thousands of parts, this is wasteful. Instead, use **LOD variant sets with per-variant payloads**, so only the active LOD consumes memory. See the detailed analysis in the [IEDT-Specific Nuances: Proxy/Render Purpose](#proxy-render-purpose-the-lod-reality-for-engineering-scenes) section.

**REQ-GS-3.1: LOD Variant Set Pattern**
- Add `--with-lod` flag to setup script
- When enabled, each asset directory becomes:

```
010_ASS_USD/USD_Startpoint/{asset_name}/
├── {asset_name}.usda              # Interface with lofted extentsHint + LOD variant set
├── lod_high/
│   └── payload.usdc               # Full CAD geometry
├── lod_medium/
│   └── payload.usdc               # Simplified geometry (auto-decimated or manually created)
├── lod_low/
│   └── payload.usdc               # Minimal geometry (optional — bbox via extentsHint may suffice)
└── host_wip/
```

- The `{asset_name}.usda` interface lofts the LOD variant set above the payloads:

```usda
def Xform "main" (
    assetInfo = { ... }
    kind = "component"
    variantSets = ["lod"]
    variants = { string lod = "high" }
)
{
    variantSet "lod" = {
        "high" {
            def Scope "geo" ( payload = @./lod_high/payload.usdc@ ) { }
        }
        "medium" {
            def Scope "geo" ( payload = @./lod_medium/payload.usdc@ ) { }
        }
        "low" {
            def Scope "geo" ( payload = @./lod_low/payload.usdc@ ) { }
        }
    }
}
```

**REQ-GS-3.2: Optional Purpose Split (VFX Compatibility)**
- Add `--with-purposes` flag as a separate option for teams that need the VFX proxy/render pattern (e.g., when the viewer specifically optimizes for `purpose`, or when proxy geometry is needed for physics/collision alongside visual geometry)
- This is secondary to the LOD variant approach

**REQ-GS-3.3: Backward Compatibility**
- Without `--with-lod` or `--with-purposes`, assets use the flat Phase 2 structure (single payload)
- LOD and purpose are upgrade paths, not requirements

**Impact:** Only the active LOD variant's payload is loaded — dramatic memory savings for large scenes. `extentsHint` provides bbox visualization without loading any geometry at all. LOD selection can be overridden per-instance in scenario layers.

---

### Phase 4: Asset Parameterization (Low-Medium Effort, High IEDT Value)

**Goal:** Enable configurable assets with variant sets and primvars on the entry point.

**REQ-GS-4.1: Variant Set Scaffolding**
- Add `scripts/add_variant_set.py` that:
  - Takes an asset name + variant set name + variant options
  - Creates the variant set on the asset entry point (lofted, above payload)
  - Creates stub layers per variant in a `variants/` subdirectory

```
010_ASS_USD/USD_Startpoint/{asset_name}/
├── {asset_name}.usda              # Lofted variant set defined here
├── {asset_name}_payload.usdc
└── variants/
    └── {variant_set_name}/
        ├── option_a.usda
        └── option_b.usda
```

**REQ-GS-4.2: Primvar Convention**
- Document a `primvars:asset_*` naming convention for entry-point primvars
- Generate stub primvars in the asset interface when `--with-primvars` is used:

```usda
color3f primvars:asset_base_color = (0.8, 0.8, 0.8) (
    doc = "Primary surface color"
)
token primvars:asset_state = "default" (
    doc = "Operating state identifier"
)
```

**Impact:** Directly addresses IEDT requirements for engineering configuration variants (material grades, operating states, inspection results).

---

### Phase 5: Multi-Scene / Scenario Architecture (Higher Effort, IEDT-Critical)

**Goal:** Enable GoodStart projects to contain multiple scenarios that share the same assets.

**REQ-GS-5.1: Project Mode Flag**
- Add `--project-mode` flag to setup script that generates:

```
{project_name}/
├── assets/                              # Shared asset library
│   └── {asset_name}/                    # Per-asset structure (Phase 2/3)
├── scenarios/                           # Multiple scene configurations
│   ├── scenario_001/                    # Scenario = equivalent of collectiveproject001 "shot"
│   │   ├── USD_GoodStart_ROOT.usda      # Scene root (current GoodStart structure)
│   │   ├── 020_BASE_LYR/               # Scene-level layers
│   │   ├── 030_SIM_LYR/
│   │   ├── 040_DATA_LYRs/
│   │   └── elements/                    # Per-element overrides
│   │       └── {asset_instance}/
│   │           ├── index.usda           # References asset + sublayers overrides
│   │           └── overrides/           # Per-instance animation, state, telemetry
│   └── scenario_002/
│       └── ...
├── 000_SOURCE/                          # Shared source files
└── scripts/                             # Shared tooling
```

**REQ-GS-5.2: Add-Scenario Script**
- Add `scripts/add_scenario.py` that:
  - Creates a new scenario directory with full GoodStart layer stack
  - Links to shared assets via relative references
  - Generates element instances for selected assets with override stubs

**REQ-GS-5.3: Single-Scene Remains Default**
- Without `--project-mode`, the setup script generates the current flat structure
- `--project-mode` is the upgrade path for teams growing beyond a single scene

**Impact:** Unlocks multi-scenario digital twin workflows (inspection, operation, maintenance, training) sharing the same asset library. Bridges GoodStart's simplicity with collectiveproject001's assembly power.

---

### Phase 6: Validation + CI/CD (Medium Effort, Production Value)

**Goal:** Automated structural compliance checking.

**REQ-GS-6.1: Extended Validation Script**
- Extend `scripts/validate_scene.py` to check:
  - [ ] Root file is "thin" (no geometry in root layer)
  - [ ] All prims in model hierarchy have `kind` metadata
  - [ ] Asset interfaces have `assetInfo` set
  - [ ] Payload files are referenced via `payload` arcs (not `references`)
  - [ ] Lofted fields exist on asset entry points (`extentsHint` at minimum)
  - [ ] Layer lock metadata matches expected pattern
  - [ ] No absolute file paths in any layer (portability check)

**REQ-GS-6.2: CI Integration Template**
- Update `.github/workflows/validate.yml` to run the extended validation
- Add structural compliance report to PR checks

**Impact:** Ensures generated projects stay healthy as teams modify them. Catches anti-patterns before they become problems.

---

### Phase Summary and Priority Matrix

| Phase | Effort | Impact | IEDT Relevance | Script Changes |
|-------|--------|--------|---------------|----------------|
| **Phase 1: Thin Root + Kind** | Low | High | Medium | Modify `_get_root_template_content()`, move env/samples into proper layers |
| **Phase 2: Per-Asset + Payload** | Medium | High | High | Add `add_asset.py`, `loft_asset.py`, modify `ASS_LYR.usda` template |
| **Phase 3: LOD Variants + Payloads** | Medium | Medium | High | Add `--with-lod` flag, LOD variant set scaffolding, optional `--with-purposes` for VFX compat |
| **Phase 4: Parameterization** | Low-Medium | High | Critical | Add `add_variant_set.py`, primvar convention, variant scaffolding |
| **Phase 5: Multi-Scene** | Higher | High | Critical | Add `--project-mode`, `add_scenario.py`, shared asset library |
| **Phase 6: Validation + CI** | Medium | Medium | High | Extend `validate_scene.py`, update `.github/workflows/validate.yml` |

**Recommended order:** Phase 1 → Phase 2 → Phase 4 → Phase 6 → Phase 3 → Phase 5

Rationale: Phase 1 is a quick win that fixes the principle-practice gap. Phase 2 unlocks the reference/payload pattern. Phase 4 adds parameterization (critical for IEDT use cases). Phase 6 ensures quality as complexity grows. Phase 3 and 5 are higher-effort features needed only when projects scale.

---

## References and Related Resources (Updated)

| Resource | URL | Relevance |
|----------|-----|-----------|
| USDWG Collective Project 001 | https://github.com/usd-wg/collectiveproject001 | Primary analysis target |
| USD GoodStart | https://github.com/jph2/USD_GoodStart | Minimal digital twin USD template |
| NVIDIA Learn OpenUSD: Asset Structure Principles | https://docs.nvidia.com/learn-openusd/latest/asset-structure/asset-structure-principles/index.html | Canonical asset structure guidance |
| NVIDIA Learn OpenUSD: Workstreams | https://docs.nvidia.com/learn-openusd/latest/asset-structure/workstreams/index.html | Layer stack workstream patterns |
| NVIDIA Learn OpenUSD: Reference/Payload Pattern | https://docs.nvidia.com/learn-openusd/latest/asset-structure/reference-payload-pattern/what-is-ref-payload-pattern.html | Lofting and payload best practices |
| NVIDIA Learn OpenUSD: Model Hierarchy | https://docs.nvidia.com/learn-openusd/latest/asset-structure/model-hierarchy/what-are-model-kinds.html | Kind system and hierarchy design |
| NVIDIA Learn OpenUSD: Model Hierarchy Considerations | https://docs.nvidia.com/learn-openusd/latest/asset-structure/model-hierarchy/model-hierarchy-considerations.html | Operational, shallow, consistent, extensible |
| NVIDIA Learn OpenUSD: Asset Parameterization | https://docs.nvidia.com/learn-openusd/latest/asset-structure/asset-parameterization/what-is-asset-parameterization.html | Variant sets and primvars for reuse |
| O3DE Odie Assets | https://github.com/o3de/odie-3d-assets | Source character asset |
| AOUSD Interest Groups | https://aousd.org/community/interest-groups/ | IEDT IG home |
| DPEL Library (ASWF) | https://dpel.aswf.io/ | Target distribution platform |
| nAurava CAD-to-OpenUSD | https://github.com/nAurava-Technologies/CAD-to-OpenUSD | STEP→USD conversion pipeline (Kit headless + HOOPS) |
| OpenUSD GoodStart ComfyUI Nodes | https://github.com/jph2/OpenUSD_GoodStart_ComfyUI_nodes | Visual node-based USD workflows (82+ nodes, DCC import, composition) |
| Anchorpoint | https://www.anchorpoint.app/ | Git-based version control for artists/engineers (binary handling, file locking, visual review) |
| Composable Bindings Whitepaper (NVIDIA/Microsoft) | https://aka.ms/ComposableBindings | Integration pattern for connecting data lakes, visualization engines, and operational systems (Aaron Luk, Christoph Berlin, Nov 2025) |
| AAS/OPC UA/OpenUSD Research (v12) | [AAS_OPC_OpenUSD_RESEARCH_v12.md](../../AAS_OPC_OpenUSD_INTEGRATION/docs/AAS_OPC_OpenUSD_RESEARCH_v12.md) | Layered architecture combining Composable Bindings with AAS governance and OpenUSD composition for living digital twins |

---

**End of Discovery**
