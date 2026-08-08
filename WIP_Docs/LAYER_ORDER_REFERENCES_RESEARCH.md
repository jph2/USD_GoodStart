---
arys_schema_version: "1.3"
id: "d3c443b0-4ef4-4bf4-8c4a-40031bc1e356"
kanban_id: null
title: "USD Layer Order — Published References and Pipeline Comparisons"
document_version: "1.9.0"
type: PRACTICAL
status: draft
trust_level: 2
visibility: internal
created: "2026-06-10T12:00:00Z"
last_modified: "2026-08-08T15:47:38+02:00"
origin_domain: "Domain020"
author: "Jan Haluszka"
provenance:
  git_repo: "USD_GoodStart"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "WIP_Docs/LAYER_ORDER_REFERENCES_RESEARCH.md"
agent_index:
  context: "Comparative OpenUSD research on layer order, composition paradigms, reusable asset structures, Isaac Sim Asset Structure 3.0, NVIDIA VFI factory structuring, deployment packaging, and digital-twin implications."
  maturation: 2
  routing:
    executive_summary: "#executive-summary"
    architecture_assurance_map: "#composition-architecture-and-assurance-are-orthogonal"
    introduction: "#introduction--from-film-pipelines-to-digital-twins"
    composition_foundations: "#composition-foundations"
    diagram_guide: "#how-to-read-the-diagrams"
    paradigm_comparison: "#composition-paradigms-compared"
    decision_matrix: "#decision-matrix--choosing-a-composition-paradigm"
    me_shot_refinement_baseline: "#1-me-shot-stack--internal-practitioner-synthesis"
    proposed_goodstart_order: "#8-proposed-usd-goodstart-layer-order--digital-twin--omniverse-template"
    simready_addendum: "#15-nvidia-simready--physical-ai-addendum---rules-that-affect-the-proposed-usd-goodstart-layer-order"
    isaac_asset_structure_3: "#16-nvidia-isaac-sim-60---asset-structure-30"
    digital_twin_implications: "#161-digital-twin-implications"
    engineering_to_twin_reconciliation: "#1611-engineering-to-twin-hierarchy-reconciliation"
    workcell_case_study: "#162-case-study-workcell-digitaltwin-to-asset-structure-30"
    simready_foundation: "#17-nvidia-simready-foundation-capability-contracts-validation-and-standardization"
    dsx_conclusions: "#18-nvidia-dsx-blueprint--evidence-based-conclusions-and-goodstart-corrections"
    dsx_isaac_comparison: "#breakout--dsx-equipment-assets-versus-isaac-sim-asset-structure-30"
    digital_twin_robotics_breakout: "#breakout--why-this-architecture-matters-for-digital-twins-robotics-and-omniverse"
    vfi_factory_structuring: "#19-nvidia-vfi--factory-scale-authoring-composition-and-deployment-structure"
    vfi_authoring_deployment_breakout: "#breakout--authoring-structure-is-not-deployment-structure"
    revision_history: "#revision-history"
tags: [openusd, layers, composition, sublayers, livrps, composition_arcs, layer_order, asset_structure, vfx, digital_twin, robotics, isaac_sim, omniverse, dsx, vfi, ai_factory, dataprep, deployment_packaging, instancing, value_clips, point_instancer, best_practices, pipeline, pipeline_architecture, usd_goodstart, research, case_study, workcell, cad_conversion, simready_foundation, validation, standardization, capability_profiles, relationships, relocates, namespace_editing, source_identifiers, presentation_hierarchy, multi_bom, plm, reimport]
---

# USD Layer Order — Published References and Pipeline Comparisons

**Version**: 1.9.0 | **Date**: 08.08.2026 | **Time**: 15:47 | **GlobalID**: 20260808_1547_Layer_Order_References_v1.9.0

**Last Updated:** 08.08.2026 15:47<br>
**Framework:** USD GoodStart / Studio Framework<br>
**Status:** draft<br>
**Origin Domain:** Domain020<br>
**Git:** Repo: USD_GoodStart | Branch: main | Path: WIP_Docs/LAYER_ORDER_REFERENCES_RESEARCH.md | Commit: pending

**Purpose:** Collect documented USD sublayer-order conventions and **LIV(E)RPS / composition-arc strategies** from public industry sources; compare them to the [**proposed USD GoodStart layer order**](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read) and an author-created **M&E practitioner synthesis**; record trade-offs and diagrams for discussion.

**Related**: [README.md — Quick Structure & Layer Stack Order](../README.md#quick-structure)

**Tag block:**
#openusd #layers #composition #sublayers #livrps #composition_arcs #layer_order #asset_structure #vfx #digital_twin #robotics #isaac_sim #omniverse #dsx #vfi #ai_factory #dataprep #deployment_packaging #instancing #value_clips #point_instancer #best_practices #pipeline #pipeline_architecture #usd_goodstart #research #case_study #workcell #cad_conversion #simready_foundation #validation #standardization #capability_profiles #relationships #relocates #namespace_editing #source_identifiers #presentation_hierarchy #multi_bom #plm #reimport

---

## Executive Summary

> **Publication and affiliation status:** This is independent author research. Its externally verifiable evidence base consists of publicly accessible documentation and repositories; the M&E comparison also includes an anonymized author synthesis informed by internal practitioner discussions, without reproducing private records or attributing participants. It is not an [Alliance for OpenUSD (AOUSD)](https://aousd.org/) publication, Interest Group recommendation, approved deliverable, certification, or endorsement. References to AOUSD describe only publicly documented organizational scope and standards activity.

OpenUSD does **not** prescribe one universal layer order or asset structure. This research identifies four complementary composition paradigms: **departmental shot refinement**, **scene/digital-twin ownership lanes**, **published reusable assets**, and **configurable simulation products**. They answer different questions and often belong at different scales of the same project.

[NVIDIA Isaac Sim Asset Structure 3.0](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/robot_setup/asset_structure.html) is the clearest configurable-product example in this paper. It combines a stable public asset identity with shared base data, deferred payloads, and variant-selected physics, controller, and end-effector features. Its significance is not the robot-specific filenames, but the deliberate use of composition arcs according to their native purposes. See the [detailed Asset Structure 3.0 case study](#16-nvidia-isaac-sim-60---asset-structure-30).

For digital twins, the strongest conclusion is to combine paradigms rather than force every concern into one stack. The [**proposed USD GoodStart layer order**](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read) can define scene-level ownership for assets, metadata, simulation, and runtime state, while factories, lines, cells, machines, and robots expose recursively composed public asset interfaces below that boundary. Dataprep must transform source-oriented CAD, BIM, plant, and robotics hierarchies into those simulation-oriented packages and validate them against explicit, versioned requirements. The hierarchy-reconciliation rule is to preserve source identity and mapping evidence, use relationships or collections for alternate non-transform views, use references and authored transforms for placement, and reserve relocates for deliberate composed-namespace edits. See [Section 16.1 - Digital Twin Implications](#161-digital-twin-implications), [Dataprep pipeline as the transformation boundary](#dataprep-pipeline-as-the-transformation-boundary), and [Section 16.1.1 - Engineering-to-twin hierarchy reconciliation](#1611-engineering-to-twin-hierarchy-reconciliation).

The [Workcell-DigitalTwin conversion case study](#162-case-study-workcell-digitaltwin-to-asset-structure-30) turns that conclusion into a concrete migration design. It compares the inspected mixed-authoring stage with three publishable target envelopes: a pure Asset Structure 3.0-inspired product, a minimal three-layer scene around 3.0-ready assets, and the full proposed USD GoodStart layer order around the same asset packages.

[NVIDIA SimReady Foundation](https://github.com/NVIDIA/simready-foundation) adds a separate but complementary axis: versioned capability contracts and executable validation. Its requirement/capability/feature/profile hierarchy states what an asset must support for a declared simulation use case, while its standardization workflow governs how a new capability progresses from domain definition and data mapping through specifications, validators, reference pipelines, and sample content. See [Section 17](#17-nvidia-simready-foundation-capability-contracts-validation-and-standardization). Asset Structure 3.0, SimReady, and the proposed USD GoodStart layer order are deliberately kept distinct here so their eventual integration can assign each one a clear responsibility.

The [NVIDIA DSX Blueprint](https://docs.omniverse.nvidia.com/dsx/latest/index.html) and its public [Generic CDU reference asset](https://github.com/NVIDIA-Omniverse/aif-pipeline-samples/blob/main/assets/Generic_CDU/Generic_CDU.usda) provide concrete digital-twin evidence for that responsibility split. They show one public asset interface, intrinsic product properties and connection points as asset-local sublayers, and internal/external geometry behind selectively loaded payloads. They do **not** prescribe the full proposed USD GoodStart scene order. [Section 18](#18-nvidia-dsx-blueprint--evidence-based-conclusions-and-goodstart-corrections) records the resulting corrections and explains why this composition model matters for long-lived digital twins, robotics, and Omniverse applications compared with classic flattened interchange workflows.

The [NVIDIA Virtual Facility Integration Guide](https://docs.omniverse.nvidia.com/vfi/latest/index.html) adds a lifecycle and deployment dimension that the earlier comparisons did not make explicit enough. It separates modular, instancing-friendly **authoring structure** from measured **deployment packaging**: fine-grained asset interfaces, payload boundaries, material libraries, animation clips, domain layers, and reusable subcomponents can remain the maintained source of truth while a governed build consolidates selected components into fewer runtime layers for lower open/stat overhead. This is not a fifth composition paradigm and not permission to flatten the authoring source. It is a cross-cutting rule: choose composition boundaries for ownership and reuse, then generate and benchmark deployment artifacts for the target resolver, storage, network, memory, and interaction envelope. See [Section 19](#19-nvidia-vfi--factory-scale-authoring-composition-and-deployment-structure).

### Composition architecture and assurance are orthogonal

The four composition paradigms organize **where and how opinions are composed**. SimReady evaluates a different dimension: **which capabilities a declared simulation use case requires and what executable evidence proves conformance**. It is therefore a cross-cutting assurance axis, not a fifth composition paradigm.

```mermaid
flowchart TB
    Foundation["COMMON OPENUSD<br/>BUILDING BLOCKS<br/>subLayers · references<br/>payloads · variants · schemas"]

    subgraph Architecture["COMPOSITION ARCHITECTURE — choose per boundary and design question"]
        direction TB

        subgraph SceneBoundary["SCENE / PROJECT BOUNDARY"]
            direction LR
            Departmental["A · Departmental<br/>shot refinement<br/>Question: Which peer<br/>opinion wins?<br/>Center: ordered subLayers"]
            Ownership["B · Scene / digital-twin<br/>ownership lanes<br/>Question: Who owns<br/>this opinion?<br/>Center: lifecycle +<br/>write-target contracts"]
        end

        subgraph AssetBoundary["ASSET / PRODUCT BOUNDARY"]
            direction LR
            Published["C · Published<br/>reusable asset<br/>Question: What remains<br/>stable and reusable?<br/>Center: public interface<br/>+ references + payloads"]
            Configurable["D · Configurable<br/>simulation product<br/>Question: What is<br/>selected or loaded?<br/>Center: variant sets +<br/>deferred payloads"]
        end
    end

    subgraph Assurance["SIMREADY ASSURANCE — applies across all four paradigms"]
        direction TB
        subgraph AssuranceRow1[" "]
            direction LR
            AssuranceQuestion["What must it support?<br/>How is that proven?"]
            Profile["Declared<br/>profile"]
            Capability["Capabilities<br/>+ features"]
            AssuranceQuestion --> Profile --> Capability
        end
        subgraph AssuranceRow2[" "]
            direction LR
            Requirement["Requirements"]
            Validator["Validators"]
            Evidence["Executable<br/>evidence"]
            Requirement --> Validator --> Evidence
        end
        Capability --> Requirement
    end

    Foundation --> Departmental
    Foundation --> Ownership
    Foundation --> Published
    Foundation --> Configurable
    Departmental --> Assurance
    Ownership --> Assurance
    Published --> Assurance
    Configurable --> Assurance

    classDef foundation fill:#e8eef5,stroke:#52697d,color:#17212b,stroke-width:2px
    classDef scene fill:#dceeff,stroke:#2167ae,color:#10243a,stroke-width:2px
    classDef asset fill:#fff0d6,stroke:#d97706,color:#3b2305,stroke-width:2px
    classDef assurance fill:#e9ddf7,stroke:#7048b6,color:#25133f,stroke-width:3px
    class Foundation foundation
    class Departmental,Ownership scene
    class Published,Configurable asset
    class AssuranceQuestion,Profile,Capability,Requirement,Validator,Evidence assurance
    style Architecture fill:#f8fafc,stroke:#64748b,stroke-width:1px
    style SceneBoundary fill:#eef7ff,stroke:#2167ae,stroke-width:1px
    style AssetBoundary fill:#fff8eb,stroke:#d97706,stroke-width:1px
    style Assurance fill:#f5f0fb,stroke:#7048b6,stroke-width:2px
    style AssuranceRow1 fill:none,stroke:none
    style AssuranceRow2 fill:none,stroke:none
```

**Figure ES.1 — Architecture choice versus capability assurance.** The vertical flow is intentional: common OpenUSD mechanics enable several valid composition architectures; SimReady can then define and verify capability contracts across any of them. The two scene-scale paradigms primarily govern opinion ownership and strength, while the two asset-scale paradigms primarily govern publication, reuse, configuration, and loading.

### Authoring topology and deployment topology are also distinct

VFI introduces a third question after composition architecture and capability assurance: **how should the accepted authored graph be packaged for a particular runtime?** A highly modular asset library may be correct for lifecycle management and still create excessive layer-resolution overhead in a remote or cloud deployment. Conversely, a compact runtime package may load quickly while being a poor authoring source because it hides ownership and regeneration boundaries. The maintained authoring graph, its composed semantics, and its generated deployment representation must therefore be evaluated separately and connected by reproducible build evidence.

Use the [Decision Matrix](#decision-matrix--choosing-a-composition-paradigm) to select a primary paradigm for each composition boundary. The proposed USD GoodStart layer order remains a **work-in-progress proposal**, not an OpenUSD or NVIDIA standard; this paper is a comparative research base for evaluating how it should evolve.

---

## Introduction — From Film Pipelines to Digital Twins

### Research purpose and thesis

The purpose of this research is not merely to catalogue layer orders or reconstruct the history of NVIDIA robot packages. It traces how **composable asset structures evolve when a stable set of OpenUSD building blocks is applied to changing requirements**. Layers, references, payloads, variants, inherits, schemas, and published prim interfaces each provide a defined behavior; their larger value comes from how deliberately they can be combined. The progression from a largely coupled robot import to Asset Structure 3.0 makes that process visible. Developers, designers, and engineers discover what must be independently owned, loaded, configured, validated, or replaced—and then redraw the package boundaries without having to discard the underlying composition model.

That adaptability connects domains that initially appear far apart. OpenUSD emerged at Pixar to solve large-scale collaborative scene assembly for animation and visual effects. The same system can now address robot configuration, multi-physics simulation, industrial asset publication, and recursively composed digital twins. This is not simply a graphics format being reused outside film. It is evidence that the underlying composition model captures more general problems: stable identity, distributed ownership, non-destructive refinement, optional loading, controlled configuration, and collaboration across tools and organizations.

The central lesson of the comparisons in this paper is that **OpenUSD's versatility does not come from one universal layer stack, folder tree, or asset template**. It comes from separating stable composition mechanics from domain-specific policy. A film pipeline may organize layers around departments and shot refinement; a robot package may organize them around physics backends, controllers, and end effectors; a digital twin may organize them around asset identity, engineering metadata, simulation state, operational telemetry, and independently loadable facility subsets. The composition arcs remain consistent while the contracts and architectural boundaries change.

This flexibility must not be confused with an “anything goes” architecture. The more adaptable the composition graph becomes, the more important its **public interfaces, ownership rules, variant semantics, payload policy, versioned requirements, provenance, and validation** become. In this sense, dataprep is not only format conversion: it acts as an architectural compiler that transforms source-oriented CAD, BIM, and robotics hierarchies into simulation-oriented asset packages while preserving evidence and stable downstream reference targets. The evolution documented here is therefore both a history of asset structures and a record of practitioners discovering their domain requirements. OpenUSD is valuable precisely because those requirements can mature without forcing the entire system to be reinvented each time.

### Why this matters

- **This is what distinguishes OpenUSD from a conventional interchange format.** It does not merely transfer a flattened result between applications; it preserves composition, stable asset identity, non-destructive opinions, optional loading, and controlled variation. The architecture can evolve without every participating tool having to invent a new scene-assembly model.
- **This is the platform leverage behind NVIDIA Omniverse.** NVIDIA explicitly describes [Omniverse as being built on OpenUSD](https://docs.omniverse.nvidia.com/dev-overview/latest/introduction.html), using it for interoperability, connectivity, and collaboration across content creation, product design, manufacturing, and simulation platforms. OpenUSD supplies the shared composition and data foundation; Omniverse adds application services, RTX rendering, physics, runtime systems, and deployment capabilities above it.
- **Unreal Engine already exposes an expanding but explicitly qualified OpenUSD integration.** Epic's current public documentation lists [USD Core as a Beta feature](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/USDCore) and [Interchange OpenUSD as Experimental](https://dev.epicgames.com/documentation/unreal-engine/API/PluginIndex/InterchangeOpenUSD). These sources establish present implementation direction only. This paper makes no claim about unannounced features, future major-version architecture, or an Epic product roadmap.
- **The strategic consequence is larger than any single platform.** Film/VFX, games, CAD/BIM, robotics, and digital twins can share composition semantics while retaining domain-specific schemas, runtime systems, and ownership policies. OpenUSD does not provide every domain with its final architecture; it provides a durable framework in which those architectures can be discovered, compared, and evolved without surrendering interoperability.

### Scope and status

This paper compares published guidance and practical examples rather than asserting one universal answer. Its **M&E practitioner synthesis** was developed by the author from internal discussions with experienced visual-effects practitioners and cross-checked against the cited public ASWF, SideFX, Pixar, and NVIDIA materials. It preserves the resulting architectural reasoning without identifying participants, linking member-only channels, reproducing confidential records, or presenting the synthesis as a studio or AOUSD standard. The [**proposed USD GoodStart layer order**](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read) is one possible digital-twin/Omniverse approach that separates live/session-backed **RUNTIME** state from static **DATA** metadata and identifiers. It is actively under discussion and is evaluated here alongside published alternatives—not presented as a finished standard.

---

## Composition Foundations

OpenUSD defines composition **mechanics**, not one global “correct” sublayer order:

| Mechanism | Rule |
|-----------|------|
| **`subLayers` array** | First entry = **strongest** opinion; last = **weakest** |
| **Root layer (Local)** | Stronger than **all** sublayers — keep root **thin** |
| **LIV(E)RPS** | Resolves conflicts **between composition arc types** (Local > Inherits > Variants > rElocates > References > Payloads > Specializes) |

Every pipeline selects an order so that later disciplines or stronger ownership lanes can refine earlier work non-destructively. That policy depends on the domain: **feature-film shot**, **asset authoring**, **robot package**, or **operational digital twin**.

### Two axes you must not confuse

Most layer-order debates mix up **two separate mechanisms**:

| Axis | Question it answers | Where it is documented |
|------|---------------------|-------------------------|
| **1. Sublayer order** (`subLayerPaths`) | Among **peer department or ownership layers** at a shot, scene, or asset root, who wins? | SideFX, the M&E practitioner synthesis in Section 1, da Vinci, Omniverse Layers, [proposed USD GoodStart layer order](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read) |
| **2. LIV(E)RPS arc strength** | Among **composition arc types** on a prim, who wins? | [Pixar glossary](https://openusd.org/release/glossary.html), [Learn OpenUSD — LIVERPS](https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/strength-ordering/what-is-liverps.html), [USD Survival Guide](https://lucascheller.github.io/VFX-UsdSurvivalGuide/pages/core/composition/livrps.html) |

A separate hierarchy-design question appears when engineering content becomes a digital twin: **which transform/model namespace is canonical, which groupings are presentation-only, and when is an actual composed-namespace edit required?** That is not another strength-order axis. It is an identity and structure decision addressed in [Section 16.1.1](#1611-engineering-to-twin-hierarchy-reconciliation).

**Key clarifications from sources:**

- **Local (L)** includes opinions authored in the **root layer and its ordered sublayer stack** — not a separate “sublayer arc” in the Pixar sense. NVIDIA Learn OpenUSD groups “Local + sublayers” when teaching LIV(E)RPS; [Learn OpenUSD glossary](https://docs.nvidia.com/learn-openusd/latest/glossary.html) wording can read differently from [Pixar’s glossary](https://openusd.org/release/glossary.html) — both agree on *behavior*, not always on *mnemonics*.
- **References (R) and Payloads (P)** are how **assets and heavy geometry** usually enter a stage — typically **on prims in a weak base layer**, not as unlimited sublayer merges ([ASWF](https://github.com/usd-wg/assets/blob/main/docs/asset-structure-guidelines.md), [USD Survival Guide](https://lucascheller.github.io/VFX-UsdSurvivalGuide/pages/core/composition/livrps.html)).
- **Any direct Local opinion in the root layer beats opinions in its sublayers.** This universal strength behavior motivates the project-policy recommendation to keep scene roots thin; an asset interface root can still author the lightweight public fields and composition arcs that define its contract ([Pixar SIGGRAPH 2019](https://openusd.org/files/Siggraph2019_USD%20Composition.pdf), [NVIDIA scalable asset-structure principles](https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/independent/asset-structure-principles.html)).

### How to Read the Diagrams

All stack diagrams below reuse the layout from [README.md — Quick Structure](../README.md#quick-structure):

- **Left**: **Full** LIV(E)RPS reference (L → I → V → E → R → P → S, strongest at top) — **same in every diagram**; universal OpenUSD mechanics, not source-specific
- **Right**: `subLayers` stack (**strongest at top**, **weakest at bottom**) — Section 1 uses two author-created analytical views: per-shot pillars, then sequence-level defaults with shot refinements above
- **Arrow**: LIV(E)RPS governs *how* opinions combine; sublayer order governs *who wins* among peer layers
> **Mermaid note:** Labels containing `(E)` in LIV(E)RPS must stay quoted in Mermaid source. Nested `subgraph` titles may sit close to the next row in the analytical Section 1 diagrams; do not add spacer/header-node workarounds there.

---

## Composition Paradigms Compared

The sources in this paper do not merely recommend different filenames or layer orders. They represent several **composition paradigms** that answer different pipeline questions. Treating all of them as competing sublayer stacks hides the main architectural distinction.

| Paradigm | Primary question | Dominant OpenUSD mechanisms | Representative cases |
|----------|------------------|-----------------------------|----------------------|
| **Departmental / shot refinement** | Which peer contribution should win when departments refine the same shot? | Ordered `subLayers`; thin root; stronger downstream disciplines above weaker foundations | M&E practitioner synthesis in Section 1, SideFX shot examples, ASWF production guidance |
| **Scene and digital-twin ownership lanes** | Which system owns static assets, metadata, runtime state, simulation, cameras, and overrides? | Ordered `subLayers`, references/payloads at the asset boundary, explicit write targets and contracts | [Proposed USD GoodStart layer order](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read), Omniverse digital-twin structures |
| **Published reusable asset** | How can one asset expose a stable public identity while hiding heavy or private implementation details? | Public interface layer, references, payloads, asset-local sublayers | ASWF reference-first assets, NVIDIA scalable asset structure, SimReady packages |
| **Configurable simulation product** | How can one published asset support selectable physics engines and optional behaviors without duplicating the asset? | References, payloads, variant sets, and bounded internal sublayers used together | NVIDIA Isaac Sim Asset Structure 3.0 |

```mermaid
flowchart LR
    subgraph Classic["A · Classic scene / shot ordered sublayer stack"]
        direction TB
        ClassicQuestion["Order answers:<br/>Who wins?"]
        ClassicScope["Scene / shot<br/>composition boundary<br/>independently authored<br/>department layers"]
        ClassicRoot["Thin root layer<br/>ordered subLayers array"]
        Strong["STRONGEST peer opinion"]
        LGT["LGT · Lighting"]
        SIM["SIM · Simulation"]
        ANIM["ANIM · Animation"]
        CAM["CAM · Camera"]
        MTL["MTL · Materials"]
        ASS["ASS · Asset assembly"]
        Weak["WEAKEST peer opinion"]
        ClassicResult["Resolved result<br/>strongest authored<br/>peer opinion wins"]

        ClassicQuestion -.-> ClassicScope
        ClassicScope --> ClassicRoot
        ClassicRoot -->|"subLayers"| Strong
        Strong --> LGT --> SIM --> ANIM --> CAM --> MTL --> ASS --> Weak --> ClassicResult
    end

    subgraph Isaac["B · NVIDIA Isaac Sim Asset Structure 3.0"]
        direction TB
        IsaacQuestion["Composition arcs answer:<br/>What is reused, selected,<br/>or loaded?"]
        SceneASS["Scene ASS_LYR.usda"]
        Public["robot_name.usda<br/>one public asset identity"]

        subgraph Shared["Stable shared asset"]
            direction TB
            SharedStructure["base.usda<br/>composes → instances.usda<br/>instances.usda:<br/>prim reference → geometries.usd<br/>reference → materials.usda<br/>sublayer → robot.usda · schema"]
        end

        Variants{"Variant sets<br/>Which configuration?"}

        subgraph Choices["Selectable feature branches"]
            direction TB
            FeatureBranches["physics variant → Physics<br/>PhysX · MuJoCo · other<br/><br/>controller variant<br/>→ Controller<br/>sensor · ROS graph<br/><br/>end-effector variant<br/>→ End effector<br/>gripper · robot hand"]
        end

        Payloads["Payloads<br/>load optional or heavy data<br/>on demand"]

        IsaacQuestion -.-> SceneASS
        SceneASS -->|"reference"| Public
        Public -->|"reference"| SharedStructure
        SharedStructure ~~~ Variants
        Public --> Variants
        Variants -->|"variant selections"| FeatureBranches
        FeatureBranches -.->|"payloads"| Payloads
    end

    Classic ~~~ Isaac

    style Classic fill:#e3f2fd,stroke:#1565c0,stroke-width:3px,color:#000
    style Isaac fill:#fff8e1,stroke:#ef6c00,stroke-width:3px,color:#000
    style Shared fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000
    style Choices fill:#ede7f6,stroke:#5e35b1,stroke-width:2px,color:#000
    style ClassicRoot fill:#bbdefb,stroke:#0d47a1,stroke-width:2px,color:#000
    style Strong fill:#1565c0,stroke:#0d47a1,stroke-width:2px,color:#fff
    style Weak fill:#90a4ae,stroke:#455a64,stroke-width:2px,color:#000
    style ASS fill:#cfd8dc,stroke:#455a64,stroke-width:2px,color:#000
    style ClassicQuestion fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000
    style ClassicScope fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000
    style ClassicResult fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000
    style Public fill:#ffcc80,stroke:#e65100,stroke-width:3px,color:#000
    style Variants fill:#ffe082,stroke:#f57f17,stroke-width:3px,color:#000
    style Payloads fill:#f8bbd0,stroke:#ad1457,stroke-width:2px,color:#000
    style IsaacQuestion fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#000
```

*Paradigm comparison — Both panels retain their full internal structure. The classic side shows the complete peer-opinion stack from strongest to weakest. The Isaac Sim side shows the scene reference, public asset identity, stable shared asset files, variant-selected feature branches, and deferred payload path. The layouts are normalized for direct side-by-side comparison; Section 16 provides the source evidence and detailed interpretation.*

### Sublayer-order paradigms

The M&E and proposed USD GoodStart diagrams mainly visualize **peer opinion strength**. Their vertical order answers who wins when multiple layers author an opinion at the same composed location. M&E commonly organizes the stack by downstream shot refinement, while the proposed USD GoodStart layer order organizes it by digital-twin ownership, update frequency, and operational responsibility. These are valid domain-specific policies, but they remain policies built on the same `subLayers` mechanism.

In this paradigm, changing the order can change the resolved result. The root should remain thin because local root opinions are stronger than every sublayer. References and payloads normally enter through an asset or assembly layer; they are not substitutes for defining the ownership and strength of peer scene contributions.

### Asset-publication paradigms

A reusable asset package asks a different question. It needs a stable downstream reference target even while its geometry, materials, metadata, or payload organization evolves internally. The public asset layer acts as a contract. Consumers reference that interface rather than sublayering or referencing its private implementation files individually.

Here the important boundary is **public versus internal**, not simply strongest versus weakest. References preserve reusable asset identity and namespace; payloads add load control for heavy data; internal sublayers allow independently authored but package-owned opinions to participate in the asset's layer stack.

### Why the Isaac Sim paradigm is special

Isaac Sim extends the published-asset model into a **configurable simulation product**. Its `robot_name.usda` interface keeps a single asset identity, while the package combines several composition strategies:

- A **reference** brings in the stable base asset stack.
- **Prim references** reuse geometry and material resources in the instances/assembly layer.
- **Sublayers** add compatible package-owned contributions such as robot schema or shared physics foundations.
- **Payloads** defer optional or backend-specific feature data until it is required.
- **Variant sets** expose controlled choices such as PhysX versus MuJoCo, controller configurations, or alternative end effectors.

This matters because a variant set expresses **configuration**, not chronological authorship and not department priority. Creating separate top-level scene layers for every physics engine, controller, and gripper would mix configuration with scene ownership and make the public asset path unstable. Isaac Sim instead keeps shared geometry and identity constant while selecting only the feature branches needed for a particular simulation context.

The pattern can be summarized as:

```text
scene ownership stack
  -> ASS_LYR references one public robot interface
       -> reference composes the shared base asset
       -> variant set selects a physics implementation
       -> variant set selects controller / ROS features
       -> variant set selects an end effector
       -> payloads load optional or heavy implementation data
```

The crucial lesson for the proposed USD GoodStart layer order is not to replace its scene-level ownership stack with the Isaac structure. The proposal should use the two paradigms **at different scales**: ordered scene layers define project ownership and strength, while Isaac-style composition below `ASS_LYR.usda` defines the reusable asset's identity, loading behavior, and supported configurations. Section 16 develops this case in detail and maps it onto the proposed USD GoodStart package boundary.

---

## Decision Matrix — Choosing a Composition Paradigm

Use this matrix **for one composition boundary at a time**: the project/scene root, a published asset package, or a configurable feature package. Do not force one answer onto the entire pipeline. A digital-twin scene can use **B** at the project root, **C** for its reusable machines, and **D** inside robots or other configurable simulation assets.

| Profile | Paradigm | Primary design question | Typical OpenUSD center of gravity |
|---------|----------|-------------------------|-----------------------------------|
| **A** | **Departmental / shot refinement** | Which peer contribution wins as departments refine the same shot or sequence? | Ordered `subLayers`; thin root; explicit strongest-to-weakest policy |
| **B** | **Scene / digital-twin ownership lanes** | Which system owns assets, metadata, simulation, cameras, runtime state, and overrides in a long-lived scene? | Ordered scene-level `subLayers`; write-target and lifecycle contracts; references/payloads at asset boundaries |
| **C** | **Published reusable asset** | How does an asset keep one stable public identity while its internal implementation and heavy data evolve? | Public interface layer; references; payloads; bounded asset-internal layers |
| **D** | **Configurable simulation product** | How does one asset identity expose controlled physics, controller, behavior, or equipment configurations? | Public interface + shared base; variant sets; references; payloads; optional feature stacks |

### Questions and scoring

Answer each question with **Yes**, **Partly**, or **No**. For **Yes**, add the displayed points; for **Partly**, add half the points; for **No**, add zero. A dash means the question is not a useful signal for that profile.

| # | Question | A | B | C | D |
|---|----------|--:|--:|--:|--:|
| 1 | Is the main production unit a **shot or sequence** refined by several departments? | +3 | — | — | — |
| 2 | Is the central conflict-resolution question **which peer layer should override another**? | +3 | +1 | — | — |
| 3 | Is the result a **long-lived scene or operational world**, rather than primarily a shot publish? | — | +3 | +1 | +1 |
| 4 | Must multiple tools or teams own separate scene concerns such as assets, metadata, simulation, cameras, and overrides? | +1 | +3 | — | — |
| 5 | Must live/latest runtime state remain separate from stable authored facts and configuration? | — | +3 | — | +1 |
| 6 | Will the same asset be reused by several scenes, projects, customers, or simulation contexts? | — | +1 | +3 | +2 |
| 7 | Must downstream users keep one **stable reference target** while asset internals change? | — | — | +3 | +2 |
| 8 | Is heavy or optional content required only on demand? | — | +1 | +2 | +2 |
| 9 | Does the asset expose a finite set of **supported configurations**, rather than arbitrary downstream edits? | — | — | +1 | +3 |
| 10 | Must users select physics backends, controllers, sensors, behaviors, end effectors, or equivalent feature families? | — | — | — | +3 |
| 11 | Must those configurations preserve the same public asset identity and downstream path? | — | — | +2 | +3 |
| 12 | Are reusable or configurable asset packages nested below a larger project/scene ownership stack? | — | +2 | +2 | +1 |

Because the profiles intentionally contain different numbers of relevant signals, compare **normalized scores**, not raw totals:

```text
A score = A raw total / 7  × 100
B score = B raw total / 14 × 100
C score = C raw total / 14 × 100
D score = D raw total / 18 × 100
```

### Validity gates

A high score is meaningful only when the profile's minimum condition is also true:

| Profile | Minimum condition before selecting it |
|---------|---------------------------------------|
| **A** | At least one of Questions **1–2** is Yes, and multiple peer contributions genuinely need an override order. |
| **B** | At least one of Questions **3–5** is Yes, and the scene has more than one ownership or lifecycle lane. |
| **C** | Questions **6 or 7** are Yes. There must be a real reuse or stable-interface requirement. |
| **D** | Question **9** is Yes and at least one of Questions **10–11** is Yes. A configurable product also requires the stable public interface of **C**. |

### Reading the result

1. Discard profiles that fail their validity gate.
2. The highest remaining **normalized percentage** is the **primary paradigm for the boundary being evaluated**.
3. Valid profiles within **10 percentage points** of each other indicate a likely hybrid—not an error.
4. Apply the paradigms at their natural scale instead of merging all of their files into one root stack.

| Result | Recommended starting architecture |
|--------|-----------------------------------|
| **A wins** | Thin shot/sequence root with an explicitly ordered departmental sublayer stack. |
| **B wins** | Thin project root with contracted ownership lanes, declared write targets, and separate treatment of authored versus runtime state. |
| **C wins** | One published asset interface referenced by consumers; hide implementation details and heavy content behind internal layers and payloads. |
| **D wins** | Start with **C**, then add controlled variant sets and optional payloaded feature stacks around a shared asset base. |
| **B + C** | Scene-level ownership stack containing reusable published asset packages—the common digital-twin pattern. |
| **B + C + D** | Scene-level ownership stack containing reusable, configurable simulation products—the factory/robot pattern developed in Section 16.1. |
| **A + C** | Departmental shot stack consuming stable published assets—the common M&E production pattern. |

> **Decision principle:** Choose `subLayers` when the question is primarily **“who owns or overrides this opinion?”** Choose a public asset interface with references/payloads when the question is **“what reusable thing is this?”** Add variant sets when the question is **“which supported configuration of that thing is active?”**

---

## 1. M&E Shot Stack — Internal Practitioner Synthesis

**Status and provenance:** Based on internal discussions with experienced visual-effects practitioners, the author developed the synthesis below and cross-checked it against the [ASWF Guidelines for Structuring USD Assets](https://github.com/usd-wg/assets/blob/main/docs/asset-structure-guidelines.md), the [SideFX Sublayer LOP shot example](https://www.sidefx.com/docs/houdini20.5/nodes/lop/sublayer.html), and Pixar's public [USD Composition — SIGGRAPH 2019](https://openusd.org/files/Siggraph2019_USD%20Composition.pdf). The section preserves the technical conclusions without identifying participants, linking private channels, quoting confidential discussions, or claiming endorsement by a studio, AOUSD, or an AOUSD Interest Group.

The synthesis describes how **Media & Entertainment (M&E)** pipelines often reason about layer resolution: departments refine the shot in passes; **ASS_LYR is the lowest (weakest) opinion** and serves as the base asset-import layer.

**Practitioner-informed principles:**

- **LGT on top** — you light *to the camera*
- **SIM above ANIM** — simulation consumes animation and must be able to override it
- **CAM below ANIM** — you animate *to the camera* (camera animation often lives with or below anim in the stack)
- **MAT above ASS** — materials/shading override imported asset defaults
- **ASS at bottom** — references, payloads, geometry import (weakest sublayer)

The resulting synthesis uses **two related sketches**: both show **three parallel shot pillars** on a **shared MAT+ASS base**, while the second adds **sequence-wide SIM and LGT** bands below the shot-specific refinements. These are author-redrawn analytical diagrams, not reproduced meeting artifacts.

**Two views of the same rules:**

| View | Structure | Use when |
|------|-----------|----------|
| **Single-shot collapse** | One vertical stack: LGT → SIM → ANIM → CAM → MTL → ASS | Teaching dept strength order for one shot root |
| **Sketch 1 (upper)** | **Three pillars** (LGT→SIM→ANIM→CAM each) + **shared** MTL + ASS | Multi-shot tracks; each pillar carries full dept stack |
| **Sketch 2 (lower)** | **Global SIM + global LGT** (sequence-wide) → **three shot pillars on top** → shared MTL + ASS | Sequence defaults first; per-shot CAM/ANIM/SIM/LGT refine and override |

**Per-pillar stack (strong → weak, top → bottom):**

| # | Layer | Role |
|---|-------|------|
| 1 | **LGT** | Lighting — strongest opinion in that pillar (overrides global LGT) |
| 2 | **SIM** | Simulation (CFX, effects, etc.) — overrides global SIM |
| 3 | **ANIM** | Animation |
| 4 | **CAM** | Cameras — bottom of pillar, rests on global / shared layers |

**Sketch 2 — sequence-wide bands (strong → weak, between pillars and MAT):**

| # | Layer | Role |
|---|-------|------|
| 5 | **LGT (global)** | Sequence-wide lighting defaults — weaker than per-shot LGT |
| 6 | **SIM (global)** | Sequence-wide simulation setup — weaker than per-shot SIM |

**Shared base (strong → weak):**

| # | Layer | Role |
|---|-------|------|
| 7 | **MTL** | Materials & shading — overrides imported asset defaults |
| 8 | **ASS** | Asset import — references & payloads (weakest) |

**How the sketches might be realized in USD — interpretive mapping:**

- **Shared foundation:** sequence root sublayers **MTL** then **ASS** (ASS weakest / last in `subLayers`).
- **Sketch 2 middle:** sequence root also sublayers **global SIM** then **global LGT** above MAT (still below per-shot stacks).
- **Per pillar:** shot root sublayers **CAM → ANIM → SIM → LGT** (weak→strong in file; diagram shows strong at top), composed on the sequence stage.
- **Override rule:** per-shot LGT/SIM in a pillar **wins over** the global LGT/SIM bands; global provides defaults before shot-specific finish.

**Not a published specification:** this is the author's practitioner-informed synthesis. It aligns with public VFX examples such as SideFX and openusd.work but is not authored or endorsed by Pixar, ASWF, AOUSD, or any participating organization as a normative standard.

#### Sketch 1

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["Author synthesis · illustrative M&E sequence · 3 shot pillars"]
        direction TB

        subgraph Pillars["Parallel pillars · per shot / track · strong at top"]
            direction LR
            subgraph PillarA["Pillar A"]
                direction TB
                LgtA["LGT · Lighting"]
                SimA["SIM · Simulation"]
                AnimA["ANIM · Animation"]
                CamA["CAM · Cameras"]
                LgtA --> SimA --> AnimA --> CamA
            end
            subgraph PillarB["Pillar B"]
                direction TB
                LgtB["LGT · Lighting"]
                SimB["SIM · Simulation"]
                AnimB["ANIM · Animation"]
                CamB["CAM · Cameras"]
                LgtB --> SimB --> AnimB --> CamB
            end
            subgraph PillarC["Pillar C"]
                direction TB
                LgtC["LGT · Lighting"]
                SimC["SIM · Simulation"]
                AnimC["ANIM · Animation"]
                CamC["CAM · Cameras"]
                LgtC --> SimC --> AnimC --> CamC
            end
        end

        Mtl["MTL · Materials & Shading · shared base"]
        Ass["ASS · References & Payloads · Asset Import · weakest"]

        CamA --> Mtl
        CamB --> Mtl
        CamC --> Mtl
        Mtl --> Ass
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style Pillars fill:#fffde7,stroke:#f9a825,stroke-width:2px,color:#000
    style PillarA fill:#fff8e1,stroke:#ff8f00,stroke-width:1px,color:#000
    style PillarB fill:#fff8e1,stroke:#ff8f00,stroke-width:1px,color:#000
    style PillarC fill:#fff8e1,stroke:#ff8f00,stroke-width:1px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style LgtA fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
    style LgtB fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
    style LgtC fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
    style SimA fill:#64b5f6,stroke:#0d47a1,stroke-width:2px,color:#000
    style SimB fill:#64b5f6,stroke:#0d47a1,stroke-width:2px,color:#000
    style SimC fill:#64b5f6,stroke:#0d47a1,stroke-width:2px,color:#000
    style AnimA fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style AnimB fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style AnimC fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style CamA fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style CamB fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style CamC fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style Mtl fill:#f48fb1,stroke:#880e4f,stroke-width:2px,color:#000
    style Ass fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
```

#### Sketch 2

Sequence-wide **SIM** and **LGT** are defined once (shared bands). Each **shot pillar** stacks on that foundation; per-shot **LGT/SIM** override the global layers.

```mermaid
flowchart LR
    subgraph LeftColumn2[" "]
        direction TB
        subgraph LIVRPSBox2["Composition Arc Strength"]
            direction TB
            LIVHdr2["LIVRPS · LIV(E)RPS"]
            ArcL2["L Local"]
            ArcI2["I Inherits"]
            ArcV2["V Variants"]
            ArcE2["E rElocates"]
            ArcR2["R References"]
            ArcP2["P Payloads"]
            ArcS2["S Specializes"]
            LIVHdr2 --> ArcL2 --> ArcI2 --> ArcV2 --> ArcE2 --> ArcR2 --> ArcP2 --> ArcS2
        end
    end

    subgraph RootContainer2["Author synthesis · illustrative M&E sequence · 3 shot pillars"]
        direction TB

        subgraph Pillars2["Parallel pillars · per shot / track · strong at top"]
            direction LR
            subgraph PillarA2["Pillar A"]
                direction TB
                LgtA2["LGT · shot"]
                SimA2["SIM · shot"]
                AnimA2["ANIM · Animation"]
                CamA2["CAM · Cameras"]
                LgtA2 --> SimA2 --> AnimA2 --> CamA2
            end
            subgraph PillarB2["Pillar B"]
                direction TB
                LgtB2["LGT · shot"]
                SimB2["SIM · shot"]
                AnimB2["ANIM · Animation"]
                CamB2["CAM · Cameras"]
                LgtB2 --> SimB2 --> AnimB2 --> CamB2
            end
            subgraph PillarC2["Pillar C"]
                direction TB
                LgtC2["LGT · shot"]
                SimC2["SIM · shot"]
                AnimC2["ANIM · Animation"]
                CamC2["CAM · Cameras"]
                LgtC2 --> SimC2 --> AnimC2 --> CamC2
            end
        end

        GlobalLgt["LGT · sequence · global"]
        GlobalSim["SIM · sequence · global"]
        Mtl2["MTL · Materials & Shading · shared base"]
        Ass2["ASS · References & Payloads · Asset Import · weakest"]

        CamA2 --> GlobalLgt
        CamB2 --> GlobalLgt
        CamC2 --> GlobalLgt
        GlobalLgt --> GlobalSim
        GlobalSim --> Mtl2
        Mtl2 --> Ass2
    end

    LIVRPSBox2 -.-> RootContainer2

    style LeftColumn2 fill:none,stroke:none,color:#000
    style RootContainer2 fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style Pillars2 fill:#fffde7,stroke:#f9a825,stroke-width:2px,color:#000
    style PillarA2 fill:#fff8e1,stroke:#ff8f00,stroke-width:1px,color:#000
    style PillarB2 fill:#fff8e1,stroke:#ff8f00,stroke-width:1px,color:#000
    style PillarC2 fill:#fff8e1,stroke:#ff8f00,stroke-width:1px,color:#000
    style GlobalLgt fill:#fff59d,stroke:#f57f17,stroke-width:3px,color:#000
    style GlobalSim fill:#90caf9,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox2 fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr2 fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL2 fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI2 fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV2 fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE2 fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR2 fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP2 fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS2 fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style LgtA2 fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
    style LgtB2 fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
    style LgtC2 fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
    style SimA2 fill:#64b5f6,stroke:#0d47a1,stroke-width:2px,color:#000
    style SimB2 fill:#64b5f6,stroke:#0d47a1,stroke-width:2px,color:#000
    style SimC2 fill:#64b5f6,stroke:#0d47a1,stroke-width:2px,color:#000
    style AnimA2 fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style AnimB2 fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style AnimC2 fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style CamA2 fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style CamB2 fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style CamC2 fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style Mtl2 fill:#f48fb1,stroke:#880e4f,stroke-width:2px,color:#000
    style Ass2 fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
```

**Advantages**

- Matches how VFX artists think: **light last, assets first**
- **Three pillars** express multi-shot / NLE-track work without flattening into one misleading linear stack
- **Sketch 2** separates sequence-wide SIM/LGT defaults from per-shot refinement
- SIM above ANIM matches physical sim pipelines (cloth, hair, FX take anim as input)
- Shared MAT+ASS base keeps lookdev and asset import consistent across pillars
- Thin conceptual model — easy to teach once single-shot vs multi-pillar views are separated

**Disadvantages**

- No standard names or file layout — every studio implements differently
- No slot for **runtime/digital-twin data** (OPC UA, MQTT, PLM)
- **CAM below ANIM** conflicts with layouts that lock cameras early (previz, twin monitoring views)
- Combines **environment lighting** and **shot lighting** in one LGT bucket

---

## 2. ASWF / USD Working Group — Asset Timeline Principle

**Source:** [Guidelines for Structuring USD Assets](https://github.com/usd-wg/assets/blob/main/docs/asset-structure-guidelines.md) · [ASWF Wiki](https://lf-aswf.atlassian.net/wiki/spaces/WGUSD/pages/11273723/Guidelines+for+Structuring+USD+Assets)

**What it says:** Layer order follows **workflow timeline** — later contributors override earlier ones. Explicit quote:

> *“…geometry is at the bottom, then materials. And is why **lighting is usually one of the last layers** to contribute to USD assets/shots.”*

**Typical asset contribution order (weak → strong / bottom → top):**

| Bottom (weak) | → | Top (strong) |
|---------------|---|--------------|
| Geometry (payload) | Materials | Rigging / FX / … | **Lighting** |

Layers are often **referenced into payload**, not only sublayered — ASWF recommends referencing for predictable LIV(E)RPS “R” strength.

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["ASWF asset · workflow-timeline principle"]
        direction TB
        Lgt[LGT · Lighting · usually last]
        Mid[Dept layers · rigging FX etc.]
        Mtl[MTL · Materials]
        Geo[GEO · Geometry · payload · weakest]
        Lgt --> Mid --> Mtl --> Geo
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style Geo fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
    style Mtl fill:#f48fb1,stroke:#880e4f,stroke-width:2px,color:#000
    style Lgt fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
```

**Advantages**

- Industry-neutral, ASWF-backed starting point
- Explains **why** order matters, not just **what** to name layers
- Applies to **assets** and **shots**
- Encourages payloads + references — good for performance

**Disadvantages**

- **Not a fixed layer list** — “rigging, FX, etc.” is intentionally vague
- Per-asset vs per-shot stacking still requires studio decisions
- Does not address Omniverse live/session layers or digital-twin data feeds

---

## 3. SideFX Houdini — Shot Sublayer Example

**Source:** [Sublayer LOP documentation](https://www.sidefx.com/docs/houdini20.5/nodes/lop/sublayer.html)

Canonical teaching example for **shot-level** sublayers:

```usda
subLayers = [
    @shotLighting.usd@,
    @shotFX.usd@,
    @shotAnimation.usd@,
    @shotSetDressing.usd@,
    @sequence.usd@
]
```

**Order (strong → weak):** Lighting → FX → Animation → Set dressing → Sequence

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["Houdini shot root · SideFX example"]
        direction TB
        Lgt[shotLighting.usd]
        Fx[shotFX.usd]
        Anim[shotAnimation.usd]
        Dress[shotSetDressing.usd]
        Seq[sequence.usd · weakest]
        Lgt --> Fx --> Anim --> Dress --> Seq
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style Lgt fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
    style Fx fill:#64b5f6,stroke:#0d47a1,stroke-width:2px,color:#000
    style Seq fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
```

**Advantages**

- **Concrete, copy-paste** shot stack from a major DCC
- Separates **FX** from **ANIM** explicitly, supporting the analytical FX/SIM-above-animation baseline
- **Sequence** at bottom preserves seq-wide layout as weak base
- Documents sublayer **replacement/reorder** in LOP networks

**Disadvantages**

- VFX-specific — no materials layer in this minimal example (often on assets)
- No camera layer called out
- Assumes Houdini LOP “strongest empty root” authoring model

---

## 4. Pixar — SIGGRAPH 2019 Composition (Teaching Shot)

**Source:** [USD Composition — SIGGRAPH 2019 (PDF)](https://openusd.org/files/Siggraph2019_USD%20Composition.pdf)

Pixar's teaching example uses `shot.usd` with sublayers such as **`shot_layout.usd`** and **`shot_sets.usd`**. It demonstrates **merge + override**, not a full department stack:

- Layout positions characters and sets
- Stronger layers (root or earlier sublayers) **non-destructively override** layout transforms
- **LIV(E)RPS** introduced as the cross-arc strength rubric

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local · thin root wins"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["shot.usd · Pixar teaching example"]
        direction TB
        RootLocal[shot.usd · thin root · Local overrides]
        Layout[shot_layout.usd]
        Sets[shot_sets.usd · weakest]
        RootLocal --> Layout --> Sets
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style RootLocal fill:#ffb74d,stroke:#e65100,stroke-width:3px,color:#000
    style Sets fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
```

**Advantages**

- **Authoritative** on composition mechanics (layer stack, strength, non-destructive override)
- Shows why **root must stay thin**
- Foundation for all other conventions

**Disadvantages**

- **Does not prescribe** LGT / ANIM / SIM ordering
- Shot examples are simplified vs real Presto pipelines
- PDF age — rElocates now in LIV(E)RPS spec

---

## 5. NVIDIA Omniverse — Explorer / Conductor Stage Layers

**Source:** [Omniverse Layers Extension](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html) · [Data Aggregation Best Practices](https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/independent/best-practices.html)

Omniverse documents **named stage layers** for digital-twin / conductor workflows. UI stacks layers **bottom-up**: higher in the panel = **stronger**.

**Documented work layers (typical strength high → low):**

| Strong | → | Weak |
|--------|---|------|
| Animation | Layout | Material | Lighting | Camera | Simulation | **Assets** |

Plus: Session layer (strongest during live edit), thin ROOT, optional Locked / Markup / Waypoint layers.

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["Omniverse stage · Explorer layers"]
        direction TB
        Anim[Animation Layer]
        Layout[Layout Layer]
        Mtl[Material Layer]
        Lgt[Lighting Layer]
        Cam[Camera Layer]
        Sim[Simulation Layer]
        Ass[Assets Layer · CAD imports · weakest]
        Anim --> Layout --> Mtl --> Lgt --> Cam --> Sim --> Ass
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style Ass fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
    style Anim fill:#9e9e9e,stroke:#424242,stroke-width:2px,color:#000
    style Sim fill:#64b5f6,stroke:#0d47a1,stroke-width:2px,color:#000
```

**Advantages**

- **Closest public doc** to the [proposed USD GoodStart layer order](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read) and related digital-twin use cases
- Explicit **Assets layer** at bottom (like ASS_LYR)
- Session + live merge workflow documented
- Material vs Layout ordering explained for **edit protection**

**Disadvantages**

- Layer order in UI is **reorderable** — doc is guidance, not enforcement
- Material vs Layout strength notes can read contradictory without hands-on Kit experience
- VFX-style “LGT always on top” is **not** the Omniverse default narrative

---

## 6. NVIDIA DLI — Asset-Internal Layer Stack

**Source:** [NVIDIA Omniverse DLI workshop PDF](https://hprc.tamu.edu/files/events/workshops/NVIDIA_Omniverse%E2%80%93TAMU_HPRC_DLI_Session.pdf)

Training materials show **per-asset** data layer stacks (not shot roots):

**Order (strong → weak):** FX → Rigging → Shading → **Geometry**

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["Single asset root · NVIDIA DLI example"]
        direction TB
        Fx[FX]
        Rig[Rigging]
        Shd[Shading]
        Geo[Geometry · weakest]
        Fx --> Rig --> Shd --> Geo
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style Geo fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
```

**Advantages**

- Clear **geometry-at-bottom** rule for assets
- Matches ASWF timeline principle at asset granularity
- Good for explaining payload + department references

**Disadvantages**

- **Asset-scoped**, not shot-scoped — a different problem from the Section 1 shot-refinement baseline
- Not tied to Omniverse Explorer layer names 1:1

---

## 7. openusd.work — Minimal Three-Layer Shot

**Source:** [openusd.work — Production Shot Assembly](https://openusd.work/)

Teaching shorthand:

```usda
subLayers = [
    @./layers/lighting.usd@,
    @./layers/animation.usd@,
    @./layers/layout.usd@
]
```

**Order (strong → weak):** Lighting → Animation → Layout

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["shot_010.usda · openusd.work example"]
        direction TB
        Lgt[lighting.usd]
        Anim[animation.usd]
        Lay[layout.usd · weakest]
        Lgt --> Anim --> Lay
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style Lgt fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
    style Lay fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
```

**Advantages**

- Minimal teaching stack — easy entry point
- **LGT on top** aligns with the Section 1 practitioner synthesis and the public SideFX example
- Includes payload/reference patterns in same article

**Disadvantages**

- Community/educational site — **not** Pixar/ASWF normative
- No FX/SIM/CAM/MTL slots

---

## 8. Proposed USD GoodStart Layer Order — Digital Twin + Omniverse Template

**Source:** [Proposed USD GoodStart layer order — TL;DR](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read) · [local USD_GoodStart README](../README.md) · this repo's `USD_GoodStart_ROOT.usda`

**Order (strong → weak):** OPIN → CAM → ENV → RUNTIME → SIM → DATA → ACTGR → ANIM → VAR → MTL → PHY → **ASS**

Full diagram (folder structure + layer stack) lives in the README:

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
        subgraph DiskSources["Folder structure (on disk)"]
            direction TB
            Source[000_SOURCE/<br/>CAD/DCC Sources]
            Assets[010_ASS_USD/<br/>USD Assets]
            MatLib[MatLib/<br/>Material Libraries]
            Tex[tex/<br/>Textures]
            Startpoint[USD_Startpoint/<br/>Stable DCC Startpoints]
            Source --> Assets
            Assets --> MatLib
            Assets --> Tex
            Assets --> Startpoint
        end
    end

    subgraph RootContainer["USD_GoodStart_ROOT.usda · Main Container"]
        direction TB
        Opinion[OPIN_LYR.usda<br/>Overrides & Opinions]
        Camera[CAM_LYR.usda<br/>Cameras]
        Env[ENV_LYR.usda<br/>Environment & Lighting]
        Runtime[RUNTIME_LYR.usda<br/>Live Runtime Opinions<br/>MQTT / OPC UA Snapshots]
        Sim[SIM_LYR.usda<br/>External Simulation Results]
        Data[DATA_LYRs.usda<br/>Project / Instance Data<br/>Mappings & Identifiers]
        Actgr[ACTGR_LYR.usda<br/>Action Graph / Logic]
        Anim[ANIM_LYR.usda<br/>Animation]
        Variant[VAR_LYR.usda<br/>Variants & Configurations]
        Material[MTL_LYR.usda<br/>Materials & Shading]
        Physics[PHY_LYR.usda<br/>Physics Setup & Collision Shapes]
        Asset[ASS_LYR.usda<br/>References & Payloads · Asset Import]
        Opinion --> Camera
        Camera --> Env
        Env --> Runtime
        Runtime --> Sim
        Sim --> Data
        Data --> Actgr
        Actgr --> Anim
        Anim --> Variant
        Variant --> Material
        Material --> Physics
        Physics --> Asset
    end

    LIVRPSBox -.-> RootContainer
    DiskSources --> RootContainer
    MatLib -.->|feeds MTL_LYR| RootContainer
    Tex -.->|feeds MTL_LYR| RootContainer
    Startpoint -.->|feeds ASS_LYR| RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style DiskSources fill:#fafafa,stroke:#424242,stroke-width:2px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style Asset fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
    style Opinion fill:#ffb74d,stroke:#e65100,stroke-width:3px,color:#000
    style Material fill:#f48fb1,stroke:#880e4f,stroke-width:3px,color:#000
    style Runtime fill:#ffd54f,stroke:#f57f17,stroke-width:2px,color:#000
    style Sim fill:#64b5f6,stroke:#0d47a1,stroke-width:2px,color:#000
    style Data fill:#a1887f,stroke:#3e2723,stroke-width:2px,color:#000
    style Env fill:#c5e1a5,stroke:#558b2f,stroke-width:2px,color:#000
    style Startpoint fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000
    style MatLib fill:#fce4ec,stroke:#880e4f,stroke-width:2px,color:#000
    style Tex fill:#fff3e0,stroke:#e65100,stroke-width:2px,color:#000
```

**Advantages**

- **ASS at bottom** — agrees with the Section 1 practitioner synthesis, ASWF guidance, and the Omniverse Assets layer
- **RUNTIME layer** for live/session-backed operational state and explicit MQTT/OPC UA snapshots
- **DATA layer** for project- or instance-owned PLM, ERP, AAS, OPC UA mappings, source identifiers, placement context, and cross-asset relationships; intrinsic reusable product properties remain in the asset package
- **SIM above ANIM** — agrees with the Section 1 practitioner synthesis and the public SideFX FX-over-animation pattern
- **OPIN on top** — explicit override layer for reviews and emergencies
- Documented folder ↔ layer feed paths (Startpoint → ASS, MatLib/tex → MTL)
- Validation scripts and README per folder

**Disadvantages**

- **CAM high in stack** — opposite the Section 1 practitioner synthesis in which CAM sits below ANIM
- **ENV mid-stack** — merges environment + lighting unlike dedicated top LGT
- **PHY vs SIM vs RUNTIME** split may confuse Isaac/Ansys/IoT users if the project does not document which layer owns setup, result overlays, and live latest-value state
- The exact position of `DATA_LYRs` and `RUNTIME_LYR` is a proposed GoodStart ownership policy; the DSX Blueprint supports separating validated asset definitions from runtime and operational data, but does not prescribe this scene-level order
- **Beta / not fully hardened** — order not battle-tested across all Omniverse Kit versions
- More layers than minimal stacks — higher authoring discipline required

---

## 9. NVIDIA Learn OpenUSD — Skyscraper exercise (shading over geometry)

**Source:** [Working with Sublayers](https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/sublayers/working-with-sublayers.html) · [Value Resolution](https://docs.nvidia.com/learn-openusd/latest/beyond-basics/value-resolution.html)

**Pattern:** Two workstreams (`geometry.usd`, `shading.usd`) merged at a shot/building root. Teaching code lists **shading first** (stronger), **geometry second** (weaker):

```python
root_layer.subLayerPaths.append("./contents/shading.usd")
root_layer.subLayerPaths.append("./contents/geometry.usd")
```

**Why:** Material bindings and lookdev must **override** base geometry without editing the geo file — same principle as ASWF “materials above geometry,” but expressed as **sublayer order** instead of asset payload references.

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local · sublayer stack"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["my_skyscraper.usda · Learn OpenUSD exercise"]
        direction TB
        Shd[shading.usd · materials]
        Geo[geometry.usd · base geo · weakest]
        Shd --> Geo
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style Geo fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
    style Shd fill:#f48fb1,stroke:#880e4f,stroke-width:2px,color:#000
```

**Advantages:** Clear teaching example; separates workstreams; matches “lookdev wins over model” in practice.

**Disadvantages:** Not a full shot stack (no anim/light/cam); easy to mis-read if you assume geometry should always be listed first in code.

---

## 10. NVIDIA da Vinci Workshop — delta layers (film production sample)

**Source:** [da Vinci’s Workshop — Omniverse USD](https://docs.omniverse.nvidia.com/usd/latest/usd_content_samples/davinci_workshop.html)

**Pattern:** Shot/sequence `_base.usd` aggregates **`pub/*/_delta.usda`** contributions in **production-process order**. Diagram is **strength order** — read **chronologically from the bottom**.

**Shot stack (strong → weak):**

| # | Delta layer | Role |
|---|-------------|------|
| 1 | **OVERRIDE** | Emergency / review overrides (rare; strongest) |
| 2 | **finish** | Look, lighting, material tweaks, sky, audio, final notes |
| 3 | **anim** | Deformation / transform caches |
| 4 | **camera** | Shot camera |
| 5 | **assembly** | Asset references + layout (weakest base) |

**Inside `finish`:** `_finish_light.usd`, `_finish_material.usd`, `_finish_sky.usd`, etc. — **lighting and material passes grouped**, similar in spirit to the Section 1 practitioner synthesis with strong **LGT** and **MTL** contributions, but as nested composition, not only sublayer names.

**Assets** use **references + payloads** at the asset interface (`.usd`), with contributions under `pub/geometry`, `pub/material`, `pub/rig` — **not** one flat sublayer list per mesh.

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References · P Payloads on prims"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["rt_010_base.usda · da Vinci shot pattern"]
        direction TB
        Ovr[OVERRIDE_delta]
        Fin[finish_delta · light mtl sky]
        Anim[anim_delta]
        Cam[camera_delta]
        Ass[assembly_delta · asset install · weakest]
        Ovr --> Fin --> Anim --> Cam --> Ass
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style Ass fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
    style Fin fill:#fff9c4,stroke:#f57f17,stroke-width:2px,color:#000
```

**Advantages:** Production-scale NVIDIA sample; combines sublayers **and** references/payloads/variants; documents OVERRIDE + finish passes; aligns with the Section 1 practitioner synthesis on **assembly at bottom** and **look/light high**.

**Disadvantages:** Complex nested files; not a minimal template; **camera above anim** here, opposite the Section 1 practitioner synthesis.

---

## 11. Remedy — Book of USD / per-asset layer stack (games)

**Source:** [Layer Stack — USDBook](https://remedy-entertainment.github.io/USDBook/terminology/layer_stacks.html)

**Pattern:** A single asset root (`furniture_workbench01.usda`) sublayers **modelling → surfacing → rigging**. The layer’s **own opinions sit above all sublayers** (strongest).

**Interpretation:** Department contributions stack on the asset; **surfacing/rigging must override modelling** for materials and skeleton data — same override intent as Learn OpenUSD’s shading-over-geometry, extended to rigging.

```mermaid
flowchart LR
    subgraph LeftColumn[" "]
        direction TB
        subgraph LIVRPSBox["Composition Arc Strength"]
            direction TB
            LIVHdr["LIVRPS · LIV(E)RPS"]
            ArcL["L Local · root opinions strongest"]
            ArcI["I Inherits"]
            ArcV["V Variants"]
            ArcE["E rElocates"]
            ArcR["R References"]
            ArcP["P Payloads"]
            ArcS["S Specializes"]
            LIVHdr --> ArcL --> ArcI --> ArcV --> ArcE --> ArcR --> ArcP --> ArcS
        end
    end

    subgraph RootContainer["furniture_workbench01.usda · Remedy example"]
        direction TB
        RootLocal[Root local opinions · strongest]
        Rig[furniture_workbench01_rigging.usda]
        Surf[furniture_workbench01_surfacing.usda]
        Mod[furniture_workbench01_modelling.usda · weakest sublayer]
        RootLocal --> Rig --> Surf --> Mod
    end

    LIVRPSBox -.-> RootContainer

    style LeftColumn fill:none,stroke:none,color:#000
    style RootContainer fill:#e3f2fd,stroke:#0d47a1,stroke-width:3px,color:#000
    style LIVRPSBox fill:#78909c,stroke:#263238,stroke-width:3px,color:#000
    style LIVHdr fill:#eceff1,stroke:#263238,stroke-width:2px,color:#000
    style ArcL fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcI fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcV fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcE fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcR fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcP fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style ArcS fill:#eceff1,stroke:#455a64,stroke-width:1px,color:#000
    style Mod fill:#81c784,stroke:#1b5e20,stroke-width:3px,color:#000
```

**Advantages:** Shows **asset-scoped** stacks (not shot roots); reminds that root local edits beat sublayers.

**Disadvantages:** Does not spell `subLayerPaths` order explicitly; games-centric; must validate order against your DCC export tooling.

---

## 12. Luca Scheller — USD Survival Guide (VFX / Houdini)

**Source:** [Composition Strength Ordering (LIVRPS)](https://lucascheller.github.io/VFX-UsdSurvivalGuide/pages/core/composition/livrps.html) · SIGGRAPH 2023 Houdini Hive

**Pattern — architectural rules, not one fixed stack:**

| Mechanism | Use for | Avoid for |
|-----------|---------|-----------|
| **Sublayers** | Stage / shot **root layer stack**; department-sized USD files in shared namespace | Loading all heavy shot geometry |
| **References** | Modular assets, material libraries, shot assembly | — |
| **Payloads** | Heavy renderable geometry, lazy load | — |
| **Inherits** | Instanceable overrides across many referenced assets | — |

**Houdini LOP mental model:** LOP networks author into the **strongest new sublayer** on a mostly empty root — aligns with SideFX shot example (§3).

**Advantages:** Production-hardened VFX framing; explicit “**heavy lifting via R/P, not sublayers**”; matches the proposed USD GoodStart rule that **ASS_LYR uses references/payloads**.

**Disadvantages:** Does not prescribe LGT vs ANIM ordering; Houdini-specific authoring flow.

---

## 13. ASWF — reference-first asset contributions

**Source:** [ASWF asset structure guidelines](https://github.com/usd-wg/assets/blob/main/docs/asset-structure-guidelines.md)

**Pattern:** Department layers on a component are **referenced or sublayered** into the asset root; ASWF **prefers referencing** because each file enters as **R** in LIV(E)RPS — predictable strength vs arbitrary sublayer merge order.

**Timeline principle (unchanged):** geometry **weak**, materials next, **lighting usually last** — often implemented as **payload + referenced contribution files**, not necessarily six named shot sublayers.

**Advantages:** Interoperability focus; separates **asset structure** from **shot structure**; supports this paper's independent comparisons within the publicly documented scope of industrial digital twins.

**Disadvantages:** Leaves shot-level ordering to each studio; no standard layer filenames.

---

## 14. Omniverse — session & live layers (strongest of all)

**Source:** [Omniverse Layers Extension](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)

**Pattern:** During live collaboration, **Session layer** (and temporary Live Session sublayers) sit **above** persistent ROOT — strongest opinions in the stack UI. Merge workflow promotes deltas into named persistent layers (Layout, Material, etc.).

**Stack context (persistent work below session):** see §5 — Animation / Layout / Material / … / Assets.

**Advantages:** Explains Omniverse-specific “why did my edit win?”; critical for digital twin ops rooms.

**Disadvantages:** Session semantics differ from plain USDA on disk; easy to pollute ROOT if merges go to wrong target.

---

## Cross-source synthesis — needs vs typical pattern

| Need / domain | Sublayer stack? | R/P on prims? | Typical strong→weak theme | Primary sources |
|---------------|-----------------|---------------|---------------------------|-----------------|
| **VFX shot finishing** | Yes — dept USD files | Assets referenced from weak assembly/layout layer | LGT/FX/finish high; layout/seq low | Section 1 practitioner synthesis, SideFX, openusd.work, da Vinci |
| **Lookdev over model (same namespace)** | Yes — shading above geometry | Optional | Materials strong, geo weak | Learn OpenUSD skyscraper, ASWF timeline |
| **Published assets** | Sometimes | **Preferred** — geo in payload | Geo weak; surf/rig/light later | ASWF, da Vinci assets, Remedy |
| **Heavy CAD / twin plant** | Thin root + dept layers | **Payloads** in ASS/base layer | Twin data & sim override anim; assets at bottom | [Proposed USD GoodStart layer order](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read), Omniverse, Survival Guide |
| **Factory-scale authoring and deployment** | Scene lanes where ownership conflicts require them | **References, payloads, instancing, value clips, and packaged component libraries** | Modular authoring first; measured deployment consolidation second | [NVIDIA VFI factory structuring](https://docs.omniverse.nvidia.com/vfi/latest/guide/factory-level-structuring.html), [VFI structure examples](https://docs.omniverse.nvidia.com/vfi/latest/guide/usd-structure-example.html), [VFI packaging tradeoffs](https://docs.omniverse.nvidia.com/vfi/latest/guide/asset-structure-optimizations-and-tradeoffs.html) |
| **Teaching mechanics only** | Minimal 2-layer examples | Demonstrate separately | Override demo | Pixar SIGGRAPH 2019 |
| **Live multi-user** | Persistent layers + **session** on top | Same as above | Session strongest | Omniverse Layers Extension |
| **Houdini / Solaris** | LOP-generated sublayer stack | Payloads per shot asset | Lighting → FX → Anim → … | SideFX LOP docs, Survival Guide |

### LIV(E)RPS handling — source comparison

| Source | How LIV(E)RPS is taught | Sublayers vs R/P |
|--------|-------------------------|------------------|
| [Pixar glossary](https://openusd.org/release/glossary.html) | L = Local prim specs in layer stack order | subLayers arc merges whole layers |
| [Learn OpenUSD LIVERPS module](https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/strength-ordering/what-is-liverps.html) | L includes ordered sublayer stack; adds **E** rElocates → **LIVERPS** | Same |
| [USD Survival Guide](https://lucascheller.github.io/VFX-UsdSurvivalGuide/pages/core/composition/livrps.html) | L + sublayers for stage stack; R/P for assets | **Do not** load all geo via sublayers |
| [Omniverse USD Book (community)](https://omniverseusd.github.io/chapter3/composition_arcs.html) | “Local (and Sublayers)” first in search order | Photoshop analogy for sublayers |
| [**Proposed USD GoodStart layer order**](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read) | LIV(E)RPS for arc conflicts; **subLayers** for department/ownership order | **ASS_LYR** = References + Payloads only |

---

## Master Comparison Table

**Strongest → weakest (top → bottom).** ✓ = aligned with the Section 1 practitioner synthesis; ✗ = deliberate difference; ~ = partial.

| Layer role | M&E synthesis | SideFX shot | da Vinci shot | Learn OpenUSD | Omniverse stage | Proposed USD GoodStart layer order |
|------------|-------------|-------------|---------------|---------------|-----------------|-----------|
| Overrides / review | — | — | **OVERRIDE** | — | Session / Markup | **OPIN** ✓ |
| Lighting / finish | **LGT** (top) ✓ | **LGT** (top) ✓ | **finish** (top) ✓ | — | LGT (mid) | ENV (mid) ~ |
| Simulation | **SIM** ✓ | FX ✓ | (in anim/finish) | — | Simulation | **SIM** ✓ |
| Animation | **ANIM** ✓ | **ANIM** ✓ | **anim** ✓ | — | Animation (top) | ANIM ✓ |
| Camera | **CAM** (below anim) | — | **camera** (above assembly) | — | Camera | **CAM** (high) ✗ |
| Materials | **MTL** ✓ | (on assets) | **finish/material** ✓ | **shading** (strong) ✓ | Material | **MTL** ✓ |
| Runtime latest-value state | — | — | — | — | Session / live edits | **RUNTIME** |
| Static twin metadata / identifiers | — | — | — | — | — | **DATA** |
| Assets / layout base | **ASS** (bottom) ✓ | sequence (base) | **assembly** (bottom) ✓ | **geometry** (weak) ✓ | **Assets** (bottom) ✓ | **ASS** (bottom) ✓ |

---

## Choosing an Approach — Decision Guide

| If your priority is… | Lean toward… |
|----------------------|--------------|
| Feature-film shot finishing | Section 1 practitioner synthesis / SideFX / da Vinci / openusd.work (finish/LGT high, assembly low) |
| Lookdev merging with layout geo | Learn OpenUSD pattern — **shading sublayer above geometry sublayer** |
| Published asset interchange | ASWF + da Vinci asset interface — **references/payloads**, geo in payload |
| Omniverse conductor / factory twin | Omniverse Explorer layers + the [**proposed USD GoodStart layer order**](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read) (`RUNTIME_LYR` or session layer for live/latest-value state; `DATA_LYRs` for project/instance mappings and identifiers; intrinsic product properties remain asset-local) |
| Houdini / Solaris production | SideFX LOP stack + **USD Survival Guide** (R/P for assets) |
| Factory-scale reusable authoring | NVIDIA VFI modular asset boundaries, stable interfaces, payloads, instancing, material libraries, externalized animation, and domain layers |
| Cloud, remote, or latency-sensitive deployment | Preserve modular authoring truth, then generate and benchmark a VFI-style packaged representation; do not choose layer count from a diagram alone |
| Teaching composition mechanics only | Pixar SIGGRAPH 2019 PDF + Learn OpenUSD sublayer exercises |
| Minimal layer count | openusd.work 3-layer shot |
| Live multi-user + session merges | Omniverse Layers Extension session workflow |

VFI is intentionally not another column in the scene-sublayer comparison above. It does not publish one fixed departmental stack. Its factory guidance primarily governs assetization, recursive aggregation, instancing granularity, optional payload boundaries, externalized animation, domain-specific enrichment, and later packaging of the accepted authoring graph for a measured deployment target.

**Hybrid pattern (common in the compared production examples):** Keep **ASS (or Assets) as a weak scene-level base** and place intentional departmental or ownership refinements above it. This is a defensible pipeline policy, not a universal OpenUSD rule. Different asset categories and consuming applications can require different structures; the required invariant is that the chosen strength order and write ownership are explicit and validated.

---

## OpenUSD Learning & Ecosystem Resources

Curated links for **deeper context** on composition, layers, and pipeline design — useful alongside the layer-order comparison above. Grouped by role; not an exhaustive list ([Awesome OpenUSD](https://github.com/matiascodesal/awesome-openusd) remains the best meta-index).

### Official & standards

| Resource | URL |
|----------|-----|
| **Alliance for OpenUSD (AOUSD)** | https://aousd.org/ |
| AOUSD Core Specification 1.0 announcement | https://aousd.org/blog/foundations-of-open-3d-development-introducing-aousd-core-specification-1-0/ |
| **OpenUSD — Pixar documentation hub** | https://openusd.org/ |
| Introduction to USD (26.x docs) | https://openusd.org/release/intro.html |
| USD Terms & Concepts (LayerStack, LIV(E)RPS) | https://openusd.org/release/glossary.html |

### NVIDIA — Learn OpenUSD & Omniverse

| Resource | URL |
|----------|-----|
| **Learn OpenUSD** (updated learning path) | https://docs.nvidia.com/learn-openusd/latest/index.html |
| Learn OpenUSD — source repo | https://github.com/NVIDIA-Omniverse/LearnOpenUSD/tree/main |
| NVIDIA OpenUSD learning path | https://www.nvidia.com/en-us/learn/learning-path/openusd/ |
| OpenUSD on-demand sessions (NVIDIA) | https://www.nvidia.com/en-us/on-demand/search/?facet.mimetype[]=event%20session&layout=list&page=1&q=OpenUSD&sort=date&sortDir=desc |
| What Is OpenUSD? (NVIDIA Glossary) | https://www.nvidia.com/en-us/glossary/openusd/ |
| OpenUSD code samples (Omniverse Developer Guide) | https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd/usd.html |
| Omniverse Kit — modules overview | https://docs.omniverse.nvidia.com/kit/docs/kit-manual/latest/guide/modules.html |
| Data aggregation best practices | https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/independent/best-practices.html |
| NVIDIA Omniverse documentation and Blueprints/Workflows hub | https://docs.nvidia.com/omniverse/index.html#nvidiatab-blueprints-workflows |
| NVIDIA Virtual Facility Integration Guide | https://docs.omniverse.nvidia.com/vfi/latest/index.html |
| NVIDIA VFI script samples | https://github.com/NVIDIA-Omniverse/vfi-samples |
| NVIDIA AI Factory digital-twin pipeline samples | https://github.com/NVIDIA-Omniverse/aif-pipeline-samples |
| NVIDIA Data Aggregation and Navigation Guide | https://docs.omniverse.nvidia.com/dang/latest/index.html |
| OpenUSD Development Certification — study guide (community) | https://medium.com/@chaubenz/your-complete-guide-to-passing-the-nvidia-certified-professional-openusd-development-b129777b0ed6 |
| Learn OpenUSD community highlight (LinkedIn) | https://www.linkedin.com/posts/austin-hwang18_learn-openusd-activity-7351753987999559680-1YW_/ |

### Books, courses & practical guides

| Resource | URL |
|----------|-----|
| **OpenUSD in One Weekend** (Zhang, Green, Zhao) | https://learn-usd.github.io/ |
| **USD Survival Guide** (Luca Scheller) | https://lucascheller.github.io/VFX-UsdSurvivalGuide/ |
| Cave Academy — Introduction to OpenUSD (2025) | https://caveacademy.com/courses/introduction-to-openusd-2025/ |
| **Jan Haluszka — OpenUSD tutorials** | https://haluszka.com/#tutorials |

### Community & meta-lists

| Resource | URL |
|----------|-----|
| **Awesome OpenUSD** (Matias Codesal) | https://github.com/matiascodesal/awesome-openusd |
| ASWF USD Working Group — asset guidelines | https://github.com/usd-wg/assets/blob/main/docs/asset-structure-guidelines.md |
| OpenUSD Study Group (Discord — see NVIDIA Learn OpenUSD “First Steps”) | https://docs.nvidia.com/learn-openusd/latest/first-steps/first-steps.html |

### This project

| Resource | URL |
|----------|-----|
| [**Proposed USD GoodStart layer order**](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read) (this repo) | https://github.com/jph2/USD_GoodStart |
| Layer order comparison (this document) | [LAYER_ORDER_REFERENCES_RESEARCH.md](./LAYER_ORDER_REFERENCES_RESEARCH.md) |
| USD GoodStart README | [../README.md](../README.md) |

---

## Canonical Reference Links

| Topic | URL |
|-------|-----|
| Sublayers (strength order) | https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/sublayers/what-are-sublayers.html |
| LIV(E)RPS / strength ordering | https://docs.nvidia.com/learn-openusd/latest/composition-basics/strength-ordering.html |
| OpenUSD glossary — LayerStack, LIVERPS | https://openusd.org/release/glossary.html |
| Pixar SIGGRAPH 2019 Composition | https://openusd.org/files/Siggraph2019_USD%20Composition.pdf |
| ASWF asset structure guidelines | https://github.com/usd-wg/assets/blob/main/docs/asset-structure-guidelines.md |
| SideFX Sublayer LOP | https://www.sidefx.com/docs/houdini20.5/nodes/lop/sublayer.html |
| Omniverse Layers Extension | https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html |
| Omniverse data aggregation BP | https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/independent/best-practices.html |
| da Vinci’s Workshop (NVIDIA sample) | https://docs.omniverse.nvidia.com/usd/latest/usd_content_samples/davinci_workshop.html |
| Learn OpenUSD — sublayer exercise | https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/sublayers/working-with-sublayers.html |
| Learn OpenUSD — LIVERPS | https://docs.nvidia.com/learn-openusd/latest/creating-composition-arcs/strength-ordering/what-is-liverps.html |
| OpenUSD — Relationships | https://openusd.org/release/api/class_usd_relationship.html |
| OpenUSD — Collections (`UsdCollectionAPI`) | https://openusd.org/release/user_guides/collections_and_patterns.html |
| OpenUSD — Relocates | https://openusd.org/release/glossary.html#relocates |
| OpenUSD — Namespace editing | https://openusd.org/release/user_guides/namespace_editing.html |
| OpenUSD — Model asset identity (`assetInfo`) | https://openusd.org/release/api/class_usd_model_a_p_i.html |
| AOUSD Core Specification 1.0.1 | https://aousd.org/usd-core-specification/ |
| NVIDIA Learn OpenUSD — hierarchy transformation | https://docs.nvidia.com/learn-openusd/latest/data-exchange/data-transformation/transformation-hierarchy.html |
| NVIDIA VFI — CAD conversion considerations | https://docs.omniverse.nvidia.com/vfi/latest/guide/cad-conversion-considerations.html |
| NVIDIA VFI — factory-level structuring | https://docs.omniverse.nvidia.com/vfi/latest/guide/factory-level-structuring.html |
| NVIDIA DSX — SimReady asset journey | https://docs.omniverse.nvidia.com/dsx/latest/simready-assets.html |
| USD Survival Guide — LIVRPS | https://lucascheller.github.io/VFX-UsdSurvivalGuide/pages/core/composition/livrps.html |
| Remedy USDBook — layer stacks | https://remedy-entertainment.github.io/USDBook/terminology/layer_stacks.html |
| NVIDIA VFI complete asset-structure examples | https://docs.omniverse.nvidia.com/vfi/latest/guide/usd-structure-example.html |
| NVIDIA VFI authoring and deployment packaging tradeoffs | https://docs.omniverse.nvidia.com/vfi/latest/guide/asset-structure-optimizations-and-tradeoffs.html |
| NVIDIA VFI script samples (pinned review revision) | https://github.com/NVIDIA-Omniverse/vfi-samples/tree/2b11331c63694be791320cfee8b4b76aaace9473 |
| NVIDIA AI Factory pipeline samples (pinned review revision) | https://github.com/NVIDIA-Omniverse/aif-pipeline-samples/tree/41038967ef0a2459b128a225161f8d59beb3b424 |
| NVIDIA Data Aggregation and Navigation project assembly | https://docs.omniverse.nvidia.com/dang/latest/guide/assembly.html |
| NVIDIA Omniverse Blueprints and Workflows discovery hub | https://docs.nvidia.com/omniverse/index.html#nvidiatab-blueprints-workflows |
| OpenUSD in One Weekend | https://learn-usd.github.io/ |
| openusd.work shot example | https://openusd.work/ |
| USD GoodStart README | ../README.md |

---

## Public Discussion Reply Snippet (copy-paste)

> There isn’t one official OpenUSD layer-order spec — Pixar/ASWF/NVIDIA document the **mechanism** (first sublayer = strongest, thin root, LIV(E)RPS). Each pipeline picks order by workflow.
>
> **Public refs:** ASWF asset guidelines (geo bottom, lighting usually last), SideFX shot example (LGT→FX→ANIM→set dress→seq), Pixar SIGGRAPH 2019 composition PDF, Omniverse Layers Extension (Assets weakest), plus our comparison doc: `WIP_Docs/LAYER_ORDER_REFERENCES_RESEARCH.md`.
>
> The Section 1 practitioner synthesis uses: (1) three LGT→SIM→ANIM→CAM pillars on shared MAT+ASS; and (2) global SIM+LGT with shot pillars on top. Collapsed to one shot, this becomes LGT→SIM→ANIM→CAM→MTL→ASS. The proposed USD GoodStart layer order diverges on purpose for digital twins (RUNTIME, DATA, ACTGR, CAM high) but keeps ASS at the bottom and SIM above ANIM.

---

## 15. NVIDIA SimReady / Physical AI Addendum - rules that affect the proposed USD GoodStart layer order

This section records additional NVIDIA sources that are not primarily "layer order" documents, but they affect how the proposed USD GoodStart layer order should structure updateable digital twin assets. The common theme is that reusable assets need an explicit public interface, heavy content should sit behind payloads, and simulation metadata should be authored as separate, validated contributions rather than mixed into source geometry or root layers.

This addendum extracts **asset- and scene-architecture implications** from those sources. [Section 17](#17-nvidia-simready-foundation-capability-contracts-validation-and-standardization) treats the current SimReady Foundation separately as a versioned specification, capability, validation, and standardization system. The distinction prevents SimReady validation from being reduced to a folder convention or layer-order recommendation.

### Sources

| Source | Relevant scope |
|--------|----------------|
| [Principles of Scalable Asset Structure in OpenUSD](https://docs.omniverse.nvidia.com/usd/latest/learn-openusd/independent/asset-structure-principles.html) | Asset interface layers, workstream layers, reference-payload pattern, public vs internal asset roles |
| [Assembling Digital Twins With Omniverse and OpenUSD](https://docs.nvidia.com/learning/physical-ai/assembling-digital-twins/latest/getting-started/overview.html) | Digital twin workspace organization, asset metadata review, validation, asset organization fundamentals |
| [SimReady Assets for DSX Digital Twins](https://docs.omniverse.nvidia.com/dsx/latest/simready-assets.html) | CAD-to-USD, geometry validation/optimization, separate metadata and connection-point layers, internal/external payloads |
| [The SimReady Standardization Workflow](https://docs.omniverse.nvidia.com/simready/latest/simready-standards/standardization_workflow.html) | Domain specifications, data mapping, gap analysis, validators, reference pipelines |
| [NVIDIA-Omniverse/aif-pipeline-samples](https://github.com/NVIDIA-Omniverse/aif-pipeline-samples) | Sample scripts and presets for CAD ingestion, optimization, and SimReady USD asset production |
| [NVIDIA skills: omniverse-cad-to-simready](https://github.com/NVIDIA/skills/tree/main/skills/omniverse-cad-to-simready) | Agent-facing CAD-to-SimReady workflow skill reference |
| [NVIDIA/simready-foundation](https://github.com/NVIDIA/simready-foundation) | Central SimReady foundation repository for runtime-driven simulation content specifications |

### Rule 1 - Treat the asset root as an interface, not as storage

NVIDIA's scalable asset structure guidance frames an asset root layer as the way downstream users interact with the asset. The root/defaultPrim and other advertised public prims are the asset interface; expensive geometry and internal authoring details can live below that interface.

**Proposed USD GoodStart derivation:**

- Scene root remains thin: project metadata, `defaultPrim`, and ordered sublayers only.
- Reusable assets under `010_ASS_USD` should increasingly follow an asset-interface pattern: `<asset>.usd` as the reference target, with heavy contents in payloads.
- `ASS_LYR.usda` should reference or payload asset interface files, not reach into private internal payload files unless a contract explicitly declares that path public.
- Stable, queryable fields such as default prim, units, up axis, `kind`, `assetInfo`, supported variants, extents hints, and public semantic hooks should be available without requiring full payload loading when practical.

### Rule 2 - Model workstreams as bounded layers, not as version history

NVIDIA's asset-structure guidance supports using layer stacks to model user and computational workstreams, but it also warns that layer stacks should stay manageable and should not replace asset versioning. Each layer has an open/compose cost, and unbounded procedural layer growth becomes a pipeline liability.

**Proposed USD GoodStart derivation:**

- Proposed USD GoodStart layer names are ownership lanes, not a chronological change log.
- `APPROVAL_OVERRIDE_LYR`, `OV_DELTA_LYR`, `RUNTIME_LYR`, and similar lanes should be bounded by purpose and lifecycle rules.
- Version history belongs in Git, asset management, publish folders, or explicit bake/snapshot artifacts, not by endlessly prepending dated sublayers.
- Validators should reject unknown or unbounded layer lanes unless the layer contract declares them.

### Rule 3 - Use reference-payload structure for heavy or selectively loaded content

The reference-payload pattern keeps the downstream interaction simple: consumers reference the asset interface, while the asset internally payloads heavy content. NVIDIA's DSX SimReady example also splits internal and external geometry into separate payloads to enable selective loading.

**Proposed USD GoodStart derivation:**

- Imported CAD/Revit/Creo/startpoint files should be normalized into stable startpoints or wrapper/interface assets before scene assembly.
- Heavy geometry belongs behind payloads where possible; scene-level sublayers should not become the main mechanism for loading all CAD geometry.
- Internal/external geometry split is a useful pattern for industrial assets: external shell for navigation/render, internal detail on demand.
- `USD_Wrappers` can evolve from transform-only wrappers into asset interface layers when they expose public metadata, variants, or payload routing.

### Rule 4 - Keep simulation metadata as a separate authored contribution

The DSX SimReady asset journey describes visual geometry and SimReady metadata as parallel tracks that converge into a validated OpenUSD asset. Metadata is authored as separate USD layers and composed non-destructively onto the geometry.

**Proposed USD GoodStart derivation:**

- Asset-local property layers own **intrinsic reusable product facts** such as manufacturer, model, dimensions, weight, ratings, asset version, and asset-generation tool provenance. This follows the DSX `aif:core:*` and `aif:spec:*` pattern.
- `DATA_LYRs.usda` owns **project- or instance-scoped facts** such as source-system identifiers, placement-specific mappings, AAS/ERP/PLM bindings, project classifications, cross-asset relationships, and scene-level provenance.
- The same semantic property should not be authored independently in both locations. Any project-level override of an intrinsic asset fact requires a declared reason, owner, and strength policy.
- Runtime/latest values still belong in `RUNTIME_LYR.usda`, not in `DATA_LYRs.usda`.
- SimReady-style domain metadata should be generated from mapping tables or normalized property packages and then composed as authored USD opinions, not edited into imported source geometry.
- The contract should record which layer owns which metadata namespace, for example `aif:core:*`, `aif:spec:*`, `revit:*`, `aas:*`, or project-specific namespaces.

### Rule 5 - Treat connection points as first-class authored assets

The DSX SimReady example models equipment interfaces such as cooling, electrical, airflow, or piping ports as explicit connection-point prims, often with `guide` purpose so they are available to simulation runtimes without becoming render geometry.

**Proposed USD GoodStart derivation:**

- Digital twin assets should carry their reusable physical ports in a dedicated asset-local connection-point layer alongside geometry and metadata. The published DSX workflow composes this contribution as a sublayer; treating it as a payload would be a separate project design that requires its own loading rationale.
- Connection points should not be hand-authored into the project root.
- Reusable port definitions belong in `layers/<asset>_ConnectionPoints.usd`. A scene- or assembly-level `PHY_LYR` or future `CONN_LYR` may own the **topology between placed asset instances**—for example, which rack port connects to which facility pipe—but should not duplicate the asset's port geometry or intrinsic port metadata.
- Validators should check naming, purpose, placement, and required metadata for connection points when a project declares SimReady-style expectations.

### Rule 6 - Make validation part of the asset structure, not an afterthought

The Physical AI digital twin course and SimReady workflow both put asset inspection, metadata review, and validation into the expected workflow. SimReady standardization also calls for specifications, data mapping, gap analysis, validators, reference pipelines, and samples.

**Proposed USD GoodStart derivation:**

- `_contracts/layer_contract.json` is not optional decoration; it is the machine-readable statement of layer ownership, strength order, write targets, optional lanes, and validator policy.
- `_pipeline_reports` should record conversion, optimization, metadata enrichment, asset validation, layer validation, and final assembly validation.
- A project using the proposed USD GoodStart layer order should be able to prove which source files, specs, mapping rules, and validators produced the current USD output.
- Pipeline nodes should emit deterministic reports so a ComfyUI build, Omniverse edit pass, or headless bake can be compared later.

### Rule 7 - Separate asset-level package structure from scene-level layer order

The DSX SimReady delivered asset layout uses a main asset interface file, `layers/`, `payloads/`, and `data/`. The proposed USD GoodStart layer order uses scene-level folders such as `020_BASE_LYR`, `035_RUNTIME_LYR`, and `040_DATA_LYRs`. These are compatible but not identical scales.

**Proposed USD GoodStart derivation:**

- Scene-level root stack: controls project composition and ownership lanes.
- Asset-level package: controls one reusable asset's public interface, payloads, metadata layers, connection points, and raw data.
- `ASS_LYR.usda` is the boundary where the scene-level proposed USD GoodStart structure references asset-level packages.
- Do not flatten asset package internals into the scene-level layer stack unless the project explicitly promotes those contributions.

### Proposed USD GoodStart alignment table

| NVIDIA / SimReady concept | Proposed USD GoodStart scene-level owner | Asset-package owner |
|---------------------------|-----------------------------|---------------------|
| Main asset interface file | Referenced/payloaded by `ASS_LYR.usda` | `<asset>.usd` |
| Heavy visual geometry | Below `ASS_LYR` via payloads | `payloads/internal.usd`, `payloads/external.usd`, or equivalent |
| Intrinsic reusable product properties | No duplicate scene owner by default; explicit overrides only | `layers/<asset>_Properties.usda` |
| Project / instance identifiers and mappings | `040_DATA_LYRs/DATA_LYRs.usda` | Optional source identity or package manifest fields only |
| Reusable physical ports | No duplicate scene owner by default | `layers/<asset>_ConnectionPoints.usd` |
| Connections between placed asset instances | `PHY_LYR` or a declared future scene topology layer | Public port interface consumed by the assembly |
| Runtime latest values | `035_RUNTIME_LYR/RUNTIME_LYR.usda` | Usually not asset package-owned |
| Validation outputs | `_pipeline_reports` | asset validation report / package manifest |
| Mapping and gap analysis | `_contracts`, `_pipeline_reports`, Requirements/Spec artifacts | `data/`, manifest, mapping profile |

### Practical next rule for the proposed USD GoodStart layer order

The proposed USD GoodStart layer order should keep its current scene-level thin-root stack, but adopt a clearer **asset package convention** for imported industrial assets:

```text
010_ASS_USD/
  USD_Startpoint/
    <raw_or_imported_startpoint>.usd
  USD_Wrappers/
    <asset_id>/
      <asset_id>.usd               # public asset interface / wrapper
      layers/
        <asset_id>_Properties.usda
        <asset_id>_ConnectionPoints.usda
      payloads/
        internal.usd
        external.usd
      data/
        source_manifest.json
        mapping_profile.json
        <asset_id>.json            # optimizer preset when applicable
```

This atomic folder keeps the interface and its anchored dependencies together, matches the DSX delivery shape more closely, and keeps the proposed USD GoodStart scene assembly simple without forcing every small project to use the full structure. `source_manifest.json` and `mapping_profile.json` are GoodStart provenance extensions; the DSX example specifically documents the model-named JSON file as the Scene Optimizer preset.

### Impact on the proposed USD GoodStart Minimal Layer Setup

The NVIDIA / SimReady material changes the **generated folder and contract structure**, not the default scene-level root stack.

**Do not change by default:**

- Do not add `CONN_LYR`, `PROPERTIES_LYR`, or similar scene-level root sublayers just because one asset has connection points or metadata.
- Do not place asset payload routing, source mapping data, or one asset's public interface directly in the project root.
- Do not turn sublayers into a version-history mechanism.

**Do change in projects generated from the proposed USD GoodStart layer order:**

- Generate `010_ASS_USD/USD_Wrappers` as a first-class sibling of `USD_Startpoint`.
- Generate an atomic asset-package template under `010_ASS_USD/USD_Wrappers/_asset_package_template/` containing a public interface file plus `{layers,payloads,data}` so users see the intended package shape.
- Generate `_contracts`, `_pipeline_reports`, and `_comfyui_workflows` in the baseline because contracts, reports, and build workflows are part of the updateable structure.
- Record the asset-package convention in `layer_contract.json` so downstream nodes and validators read the same paths.
- Put short setup notes into generated ComfyUI workflow metadata so a visual operator sees the thin-root, startpoint, wrapper, assembly, data, and runtime boundaries.

**Problem this avoids:** without an asset-package convention, metadata, connection points, internal/external payload split, and mapping evidence tend to leak into the scene root, `ASS_LYR`, or ad-hoc side folders. That makes CAD/Revit updates and ComfyUI rebuilds unsafe because there is no stable boundary between imported evidence, generated wrappers, reusable asset data, and scene assembly.

**Optimization:** keep the scene-level layer stack stable and small, then move per-asset complexity below a public asset interface file:

```text
ASS_LYR.usda
  -> references 010_ASS_USD/USD_Wrappers/<asset_id>/<asset_id>.usd

010_ASS_USD/USD_Wrappers/<asset_id>/<asset_id>.usd
  -> payloads private heavy geometry
  -> composes asset-local properties / connection points
  -> points to mapping evidence under data/
```

This gives projects based on the proposed USD GoodStart layer order a SimReady-style update path without forcing every minimal project to become a full SimReady asset pipeline.

---

## 16. NVIDIA Isaac Sim 6.0 - Asset Structure 3.0

Isaac Sim 6.0 provides a concrete production example for the asset-package principles derived above. NVIDIA calls this layout **USD Asset Structure 3.0** and uses it as the standard organization for Isaac Sim 6.0 robot assets. Its purpose is to keep geometry, materials, collision/instances, robot schema, and physics implementations independently maintainable while presenting one stable asset to downstream scenes.

This is an **asset-internal composition model**, not a new scene-level sublayer order. In terms of the [proposed USD GoodStart layer order](https://github.com/jph2/USD_GoodStart#tldr-too-long-didnt-read), the complete Isaac Sim package sits below the public asset interface consumed by `ASS_LYR.usda`; its internal files should not automatically become peer layers in the project root stack.

### Breakout - Reconstructed evolution from importer 1.x to Asset Structure 3.0

> **Evidence status:** NVIDIA explicitly names and documents **Asset Structure 3.0**, but no standalone NVIDIA specifications titled “Asset Structure 1.0” or “Asset Structure 2.0” were found. The earlier generations below are reconstructed from NVIDIA's archived URDF Importer changelog, tagged test outputs, versioned Isaac Sim documentation, and the 6.0 migration language. Therefore, **1.x** and **2.x** below identify evidenced importer/asset-structure generations; they should not be presented as formally published NVIDIA standards unless a primary source with those exact titles emerges.

| Date / generation | Direct evidence | Reconstructed structure and significance |
|-------------------|-----------------|------------------------------------------|
| **Importer 1.x, before 1.17** | The Isaac Sim 4.0-tagged importer is version 1.14.1 and its committed test output contains one `test_basic.usd`. Importer 1.15 later added internal mesh references and made imported meshes instanceable. | Predominantly one robot USD entry with geometry, hierarchy, joints, and PhysX-oriented simulation data much more tightly coupled than in 3.0. Mesh reuse improved over time, but there was not yet a published multi-file feature composition contract. |
| **Importer 1.17, September 2024** | The archived changelog states that export changed to multiple USD files: `base` for meshes, `physics` for joints and physical attributes, and `sensor` for sensor attributes. | Transitional multi-file generation. It introduced explicit domain separation but did not yet describe the final Reference + Payload + Variant interface used by the next generation. |
| **Importer 2.0.1, October 2024** | The changelog states that final asset composition changed to **Reference + Payloads with variants** so sensor and physics features could be enabled or disabled. | This is the strongest evidence for the 2.x asset-composition generation: one final asset interface, a base contribution, referenced physics, payloaded optional features, and variants for configuration. |
| **Isaac Sim 4.5-5.1 documented pattern** | NVIDIA documents `asset_base.usd`, `parts.usd`, `materials.usd`, an optional `asset_sim_optimized.usd`, feature files such as `asset_physics.usd`, `asset_sensors.usd`, `asset_control.usd`, and a final `asset.usd`. | Mature predecessor to 3.0. The optimized/base asset supplies structure and visuals; physics is referenced; sensors and controls are payloaded; variants can switch feature sets. The structure is modular, but its physics organization is still primarily one simulation feature rather than a neutral multi-backend stack. |
| **Asset Structure 3.0, Isaac Sim 6.0** | NVIDIA 6.0 release notes explicitly name Asset Structure 3.0 and the URDF/MJCF Importer 3.0. NVIDIA also supplies an Asset Transformer for converting legacy robots. | Geometry, materials, instances, base hierarchy, robot schema, neutral physics, and backend-specific PhysX/MuJoCo layers are isolated. The public interface selects physics and optional behaviors through variants and payloads while preserving one asset identity. |

#### Visual evolution at a glance

```mermaid
flowchart TB
    subgraph G1["1.x · coupled"]
        direction LR
        OneFile["robot.usd"]
        Coupled["geometry + hierarchy<br/>joints + PhysX"]
        OneFile --> Coupled
    end

    subgraph G117["1.17 · separated files"]
        direction LR
        Export117["robot export"]
        Files117["base.usd<br/>physics.usd<br/>sensor.usd"]
        Export117 --> Files117
    end

    subgraph G2["2.0.1 · configurable"]
        direction LR
        Public2["final asset interface"]
        Arcs2["reference + payloads<br/>+ variants"]
        Features2["base + switchable<br/>physics / sensors"]
        Public2 --> Arcs2 --> Features2
    end

    subgraph G45["4.5–5.1 · mature modular"]
        direction LR
        Public45["asset.usd"]
        Base45["base / optimized asset"]
        Features45["physics referenced<br/>sensors + control payloaded"]
        Variants45["feature variants"]
        Public45 --> Base45 --> Features45 --> Variants45
    end

    subgraph G3["3.0 · multi-backend product"]
        direction LR
        Public3["robot_name.usda"]
        Shared3["shared asset stack"]
        Neutral3["neutral physics"]
        Select3["backend + behavior<br/>variants / payloads"]
        Public3 --> Shared3 --> Neutral3 --> Select3
    end

    G1 -.->|"split concerns"| G117
    G117 -.->|"compose"| G2
    G2 -.->|"mature"| G45
    G45 -.->|"generalize"| G3

    classDef interface fill:#ffcc80,stroke:#e65100,stroke-width:2px,color:#000
    classDef structure fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000
    classDef composition fill:#ede7f6,stroke:#5e35b1,stroke-width:2px,color:#000
    classDef feature fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000
    classDef coupled fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000

    class OneFile,Export117,Public2,Public45,Public3 interface
    class Files117,Base45,Shared3 structure
    class Arcs2,Variants45,Select3 composition
    class Features2,Features45,Neutral3 feature
    class Coupled coupled

    style G1 fill:#fff5f5,stroke:#c62828,stroke-width:2px,color:#000
    style G117 fill:#fff8e1,stroke:#ef6c00,stroke-width:2px,color:#000
    style G2 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style G45 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000
    style G3 fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#000
```

*Figure 16.A — Conceptual comparison, deliberately reduced to the architectural change in each generation. Five horizontal mini-structures are stacked from top to bottom so every generation can use the available page width while coupling, separation, composition, modularization, and multi-backend generalization remain visible in one continuous view. The evolution arrows connect the version containers rather than their internal nodes; this preserves each container's left-to-right layout. This is not a literal file-dependency specification.*

The evolution is therefore not simply “one file, then more files.” Each step assigns composition arcs a more deliberate role: **coupled content → separated domains → composed optional features → mature modular package → neutral multi-backend asset product**.

**What 3.0 improves over the documented predecessor:**

- It treats **multi-physics support as an asset-structure requirement**, not as an after-the-fact override.
- Neutral physics data can remain shared while PhysX, MuJoCo, Newton, or other runtime-specific tuning stays isolated.
- Geometry can remain efficient binary USD while the files most often reviewed and tuned are readable USDA and easier to diff.
- A stable interface can offer “no physics,” generic physics, or a specific backend without duplicating the robot asset or changing its downstream reference path.
- The Asset Transformer makes the boundary actionable by providing a migration path for legacy assets.

**Trade-off:** 3.0 is not automatically better for every asset. It adds files, composition arcs, validation requirements, and configuration choices. Its benefits become decisive when an asset is reused, independently updated, selectively loaded, or required to operate across multiple simulation backends.

Primary historical evidence:

- [Archived Isaac Sim URDF Importer changelog](https://github.com/isaac-sim/urdf-importer-extension/blob/4.5/source/extensions/isaacsim.asset.importer.urdf/docs/CHANGELOG.md)
- [Isaac Sim 4.0 importer test output](https://github.com/isaac-sim/urdf-importer-extension/tree/4.0/source/extensions/omni.importer.urdf/data/urdf/tests/tests_out)
- [Isaac Sim 5.1 Asset Structure](https://docs.isaacsim.omniverse.nvidia.com/5.1.0/robot_setup/asset_structure.html)
- [Isaac Sim 6.0 release notes](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/overview/release_notes.html)
- [Isaac Sim 6.0 announcement - legacy assets and multi-backend structure](https://github.com/isaac-sim/IsaacSim/discussions/538)

### Composition overview

```mermaid
flowchart TB
    SceneRoot["Proposed USD GoodStart scene root"]
    ASS["ASS_LYR.usda<br/>scene-level asset owner"]

    subgraph Package["Isaac-style robot asset package"]
        direction TB
        Public["robot_name.usda<br/>public asset interface"]

        subgraph AssetStack["Shared asset stack"]
            direction TB
            Base["base.usda<br/>structural assembly"]
            Instances["instances.usda<br/>visual + collision assembly"]
            Geometry["geometries.usd<br/>mesh geometry"]
            Materials["materials.usda<br/>material definitions"]
            Robot["robot.usda<br/>robot schema contribution"]

            Base -->|"composes"| Instances
            Instances -->|"prim references"| Geometry
            Instances -->|"references"| Materials
            Base -->|"sublayers"| Robot
        end

        subgraph PhysicsStack["Physics variant stack"]
            direction LR
            Physics["physics.usda<br/>shared / neutral physics"]
            PhysX["physx.usda"]
            MuJoCo["mujoco.usda"]
            Other["other_engine.usda"]

            PhysX -->|"builds on"| Physics
            MuJoCo -->|"builds on"| Physics
            Other -->|"builds on"| Physics
        end

        subgraph OptionalStacks["Optional feature stacks"]
            direction LR
            Controller["Controller / sensor / ROS graph"]
            EndEffector["Gripper / robot hand"]
        end

        Public -->|"references"| Base
        Public -.->|"physics variant"| PhysX
        Public -.->|"physics variant"| MuJoCo
        Public -.->|"physics variant"| Other
        Public -.->|"controller variant / payload"| Controller
        Public -.->|"end-effector variant / payload"| EndEffector
    end

    SceneRoot -->|"sublayers"| ASS
    ASS -->|"references public interface only"| Public

    style SceneRoot fill:#e3f2fd,stroke:#0d47a1,stroke-width:2px,color:#000
    style ASS fill:#bbdefb,stroke:#1565c0,stroke-width:2px,color:#000
    style Package fill:#f5f5f5,stroke:#424242,stroke-width:2px,color:#000
    style Public fill:#ffcc80,stroke:#e65100,stroke-width:3px,color:#000
    style AssetStack fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000
    style PhysicsStack fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#000
    style OptionalStacks fill:#ede7f6,stroke:#5e35b1,stroke-width:2px,color:#000
```

*Figure 16.1 - The proposed USD GoodStart layer order references one public robot interface through `ASS_LYR.usda`. The interface composes the shared asset stack and exposes physics, controller, and end-effector choices through variants and payloads.*

### Evidence and source status

The screenshots below capture the Isaac Sim 6.0.1 documentation shown during the 14 July 2026 discussion. They are retained as research evidence. The linked NVIDIA documentation is the normative source:

- [Isaac Sim 6.0.0 - Asset Structure](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/robot_setup/asset_structure.html)
- [Isaac Sim 6.0.1 - Tutorial 2: USD Asset Structure](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/openusd_tuning_tutorials/tutorial_02_asset_structure.html)
- [Isaac Sim 6.0.1 - Robot Schema](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/omniverse_usd/robot_schema.html)

![Isaac Sim 6.0.1 base asset and physics structure](Pics/IsaacSim_Asset_Structure/isaacsim_6_0_1_base_asset_structure_01.png)

*Figure 16.2 - Isaac Sim separates the reusable asset stack from a selectable physics stack. Meeting capture of the NVIDIA documentation.*

[Alternate capture of the base structure](Pics/IsaacSim_Asset_Structure/isaacsim_6_0_1_base_asset_structure_02.png)

### Base asset stack

The public asset, represented in the diagram as `robot_name.usda`, references a composed base asset rather than embedding all robot data in one file. The package separates concerns as follows:

| File / contribution | Primary responsibility | Composition role shown or described by NVIDIA |
|---------------------|------------------------|-----------------------------------------------|
| `robot_name.usda` | Stable downstream entry point for the finished robot asset | References the asset stack and exposes/selects feature variants |
| `base.usda` | Structural hierarchy and base assembly | Referenced by the public asset; composes the asset-local contributions |
| `geometries.usd` | Reusable mesh geometry | Referenced at prim level by the instances/assembly contribution |
| `materials.usda` | Material definitions | Referenced by the instances/assembly contribution |
| `instances.usda` | Visual and collision assembly using geometry and materials | Composed into the base asset |
| `robot.usda` | Robot schema/API contribution and robot-specific metadata | Kept in a separate layer and sublayered into the asset |
| `physics.usda` | Physics representation shared across or neutral to backends | Acts as the common physics foundation |
| `physx.usda`, `mujoco.usda`, other backend layer | Backend-specific physics opinions | Built on the common physics layer and selected through a physics variant |

The important architectural boundary is that consumers reference **one published asset**, while asset authors retain multiple independently owned files below that interface. This reduces duplication and prevents backend-specific physics data from colliding with shared geometry, materials, and metadata.

### Expanded feature stacks

NVIDIA extends the same package without modifying the source asset stack. Optional capabilities are isolated into feature stacks and exposed through variant sets and payloads.

![Isaac Sim 6.0.1 expanded asset structure](Pics/IsaacSim_Asset_Structure/isaacsim_6_0_1_expanded_asset_structure_01.png)

*Figure 16.3 - End-effector, controller, and physics feature stacks are selected above the stable asset stack. Meeting capture of the NVIDIA documentation.*

[Alternate capture of the expanded structure](Pics/IsaacSim_Asset_Structure/isaacsim_6_0_1_expanded_asset_structure_02.png)

The expanded diagram shows four bounded areas:

1. **Asset stack** - instances, materials, geometries, base hierarchy, and robot schema.
2. **Physics stack** - a common physics definition plus PhysX, MuJoCo, or another engine implementation.
3. **Controller stack** - sensors, controllers, and ROS graph integration.
4. **End-effector stack** - alternatives such as a gripper or robot hand.

The public `robot_name.usda` remains the consumption point. Variant sets select alternatives such as the physics backend, controller setup, or end effector; payloads allow optional/heavy feature content to remain unloaded until required.

### What the composition arcs mean here

The example is useful because it assigns distinct jobs to composition arcs instead of treating them as interchangeable:

- **References** establish the reusable asset identity and bring the published base asset into the final robot.
- **Sublayers** combine compatible authored opinions that belong to one package or feature implementation, such as a schema contribution or a common physics foundation.
- **Payloads** defer optional or heavy feature content while preserving the public interface.
- **Variant sets** select a named alternative, for example PhysX versus MuJoCo, without requiring separate downstream asset paths.

A variant selection does not create a global scene-layer order. It chooses which authored branch contributes opinions at the variant's composition site. Likewise, `physx.usda` is not automatically stronger than a project `SIM_LYR.usda`; the result depends on the complete composition graph and the site where the asset is referenced.

### 16.1 Digital Twin Implications

At factory scale, the Isaac Sim pattern becomes more interesting, not less. A factory can be understood as a **system of systems**: it has a stable structural hierarchy, physical bodies, interfaces, sensors, controllers, operating configurations, and nested machines or robots. In that architectural sense, a factory behaves like a very large and heterogeneous robot whose “links” are areas, lines, cells, machines, utilities, and material-flow systems.

The analogy is useful but not literal. A robot normally has one bounded kinematic tree and a relatively coherent control/physics model. A factory combines many independently owned hierarchies, update cycles, coordinate systems, simulation domains, and live-data authorities. The correct conclusion is therefore not “store the whole factory like one robot,” but **apply the Asset Structure 3.0 principles recursively** at factory, line, cell, equipment, and robot boundaries.

#### Dataprep pipeline as the transformation boundary

An Asset Structure 3.0-inspired factory package does not emerge from a file-format conversion alone. CAD, BIM, plant-design, electrical, and robotics applications organize their source data for the needs of construction and engineering authoring. Their hierarchies may follow assemblies, drawing sets, CAD bodies, manufacturing parts, discipline files, product revisions, or tool-specific containers. That structure can be meaningful and must remain traceable, but it is not automatically the structure required for simulation, live-data binding, selective loading, or digital-twin operation.

The **dataprep pipeline is therefore responsible for translating between two valid but different models**:

```text
engineering source structure
  -> preserved source/startpoint
  -> parse and classify components, assemblies, machines, robots, and buildings
  -> normalize units, coordinates, names, materials, identifiers, and geometry
  -> restructure according to the digital-twin package contract
  -> generate public interfaces, payloads, variants, semantics, topology, and feature layers
  -> validate against declared simulation requirements
  -> publish the reproducible digital-twin asset packages
```

This transformation must preserve evidence rather than destructively “clean up” the source. Original files, source hierarchy, source identifiers, conversion versions, mapping decisions, rejected elements, and generated outputs must remain traceable through manifests and pipeline reports. If the CAD assembly tree contains useful engineering meaning, the pipeline can retain it as metadata or an alternate view while still generating a simulation-oriented hierarchy.

At minimum, the dataprep pipeline must be able to:

1. **Ingest heterogeneous sources without declaring one CAD tool authoritative for the final twin.** Revit, Creo, SolidWorks, NX, STEP, IFC, URDF, MJCF, point clouds, and supplier USD packages may contribute different parts of the result.
2. **Discover and preserve stable identity.** Components, assemblies, machines, robots, buildings, connection points, and functional systems need durable IDs that survive file renames, hierarchy changes, and re-imports whenever the source permits it.
3. **Normalize technical foundations.** Units, up axis, handedness, coordinate frames, pivots, materials, naming, instancing, geometry quality, and source-relative paths must meet one declared project contract.
4. **Rebuild hierarchy for the intended simulation.** Construction assemblies may need to become site/area/line/cell/equipment packages; nested rigid bodies may need flattening; visual meshes may need separate collision representations; repeated equipment may need instancing.
5. **Route authored concerns into owned outputs.** Geometry, materials, stable metadata, connection topology, neutral physics, backend-specific physics, controls, sensors, safety zones, and optional features must land in their declared layers or payloads rather than in a monolithic converted USD.
6. **Generate composition, not only files.** The output must expose stable public interfaces and author the correct references, payloads, variants, sublayers, default selections, and package-relative dependencies.
7. **Validate and report.** Geometry closure, composition dependencies, coordinates, naming, required metadata, physics readiness, topology, performance budgets, and source-to-output mappings need deterministic quality gates.
8. **Support incremental regeneration.** A changed CAD assembly, simulation profile, or mapping rule should rebuild only the affected packages while preserving stable public paths and downstream overrides.

The pipeline cannot perform this work safely unless the **simulation requirements are explicit inputs**. Those requirements should define, for example:

| Requirement area | Questions the profile must answer |
|------------------|-----------------------------------|
| Scope and hierarchy | Which buildings, areas, lines, cells, machines, links, or components must be independently addressable? |
| Geometry fidelity | Which visual LOD, collision representation, proxy, extent, and instancing rules are required? |
| Physics and behavior | Which simulation domains and backends are supported, and which attributes are neutral versus backend-specific? |
| Semantics and topology | Which IDs, classifications, ports, networks, relationships, and connection-point schemas are mandatory? |
| Loading and performance | Which subsets must be payloaded, streamed, instanced, or available without heavy geometry? |
| Data integration | Which prims bind to PLC, OPC UA, MES, SCADA, AAS, ERP, ROS, or time-series identifiers? |
| Validation | Which rules make a package publishable, and which deficiencies are warnings versus blocking errors? |

These requirements must be **versioned and adaptable**, not hard-coded as one frozen factory definition. A robust implementation uses machine-readable capability profiles, mapping tables, schema versions, optional feature declarations, and migration rules. New simulation needs should extend or replace profiles without invalidating unchanged source packages. The pipeline should record which profile and rule versions produced each output, compare old and new results, and provide controlled migrations when a package contract changes.

This leads to a key architectural principle: **the digital-twin structure is a generated product of requirements, mappings, and validated source evidence**. The CAD structure remains an authoritative engineering input; the simulation-oriented USD package becomes the authoritative published interface for the digital twin.

#### 16.1.1 Engineering-to-twin hierarchy reconciliation

An engineering hierarchy and a digital-twin hierarchy are not competing versions of the same model. A CAD or PLM tree answers questions about design assemblies, part definitions, occurrences, revisions, and engineering ownership. A digital twin instead needs functional package boundaries, independently loadable units, stable simulation frames, connection topology, and operational grouping. Both structures can be valid; the pipeline must make their relationship explicit rather than repeatedly exporting and manually rearranging files.

> **Evidence boundary:** A related internal Discovery paper supplied the use case and the questions in this subsection. The technical conclusions below are re-derived from public OpenUSD and NVIDIA documentation. They are not a claim that a source-identifier schema, a multi-BOM representation, or a particular runtime implementation is already standardized.

NVIDIA's current factory guidance independently supports this framing: CAD conversion, structuring, and optimization/deployment are distinct phases, and asset boundaries should follow lifecycle, ownership, validation scope, instancing, and selective-loading needs rather than the incidental shape of a CAD tree. See [CAD conversion considerations](https://docs.omniverse.nvidia.com/vfi/latest/guide/cad-conversion-considerations.html), [factory-level structuring](https://docs.omniverse.nvidia.com/vfi/latest/guide/factory-level-structuring.html), and the [three-phase pipeline pattern](https://docs.omniverse.nvidia.com/vfi/latest/guide/asset-structure-optimizations-and-tradeoffs.html#three-phase-pipeline-pattern).

The transformation therefore produces two complementary outputs:

1. A **canonical operational hierarchy**: one transform/model tree and a set of published asset interfaces that simulations and downstream scenes can compose reliably.
2. **Traceable alternate views**: design-BOM, manufacturing-BOM, station, maintenance, or reporting groupings that refer to the canonical content without claiming a second transform hierarchy.

##### Mechanism boundaries: identity, composition, views, and runtime

| Need | Appropriate mechanism | Verified boundary and rule |
|------|-----------------------|----------------------------|
| Publish a reusable machine, robot, or workcell | Public wrapper/interface plus **references** and optional **payloads** | A reference composes a reusable subtree at a chosen anchor; the wrapper's authored transform performs spatial placement. A reference is the normal asset-composition mechanism, not a relocate. [OpenUSD References](https://openusd.org/release/glossary.html#references) |
| Place equipment in a cell or line | Reference the public interface below a placement `Xform` and author the required transform | **Relocates do not author transforms or preserve world space automatically.** They remap namespace; placement and coordinate conversion remain explicit pipeline work. |
| Show design BOM, station BOM, maintenance group, or another non-transform view | Namespaced **relationships** or [`UsdCollectionAPI`](https://openusd.org/release/user_guides/collections_and_patterns.html) | Relationships are uniform, list-editable path pointers. They do not create, move, or reparent prims in the composed namespace. Collections are the stock set-membership abstraction; a consumer/schema must define what the grouping means. [UsdRelationship](https://openusd.org/release/api/class_usd_relationship.html) |
| Rename, reparent, or delete a referenced/provider prim in the local composed namespace | **Relocate**, authored deliberately through a controlled namespace-edit workflow | Relocates are a composition arc for non-destructive namespace adaptation across an ancestral composition arc. They apply to prim paths, not property paths. The supplier layer remains unchanged, but the old path is no longer simultaneously available in the composed stage. [Relocates](https://openusd.org/release/glossary.html#relocates) |
| Re-import a changed CAD/PLM export | Versioned **identity ledger** plus mapping/regeneration rules | USD can store model-level `assetInfo`, but neither `assetInfo` nor a custom ID automatically rebinds a replacement prim. Reconciliation is pipeline behavior. Use separate definition and occurrence/instance IDs where repeated parts require it. [UsdModelAPI](https://openusd.org/release/api/class_usd_model_a_p_i.html) |
| Pick, carry, or place a part over time | Runtime/physics/constraint implementation, time-sampled transforms, or an instancing strategy | A normal USD relationship is always **uniform** and cannot contain time samples. It can express a static association, but not animate a changing parent. NVIDIA's factory guidance uses time-sampled transforms or PointInstancers for dynamic material flow. [OpenUSD relationship API](https://openusd.org/release/api/class_usd_relationship.html), [NVIDIA object handling](https://docs.omniverse.nvidia.com/vfi/latest/guide/factory-level-structuring.html#step-7-object-handling) |
| Choose an approved authored configuration | **Variant set** | Variants select discrete authored alternatives. They are not a high-frequency operational state machine. |

This distinction resolves a common ambiguity in digital-twin proposals: **relationships, relocates, and source identifiers are not competing answers to one question.** They operate on different concerns. Identity supports reconciliation; references and authored transforms establish the canonical operational structure; relationships and collections provide semantic views; relocates are a narrow namespace-editing tool.

```mermaid
flowchart TB
    S["Engineering sources<br/>CAD · PLM · supplier USD"]
    I["Immutable source snapshot<br/>identity ledger · revisions · hashes"]
    R["Target profile<br/>simulation · loading · consumers"]
    C["Classify boundaries<br/>asset · assembly · operational group"]
    H["Canonical twin hierarchy<br/>one transform and model tree"]
    P["Published packages<br/>public interfaces · references · payloads"]
    V["Alternate views<br/>relationships · collections"]
    N["Optional namespace adaptation<br/>relocates only when required"]
    Q["Retarget and validate<br/>paths · transforms · bindings · joints"]
    O["Atomic publication<br/>USD packages · mapping · reports"]

    S --> I --> R --> C --> H --> P
    P --> V --> Q
    P --> N --> Q
    P --> Q
    Q --> O

    style S fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000
    style I fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#000
    style R fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#000
    style C fill:#e0f2f1,stroke:#00796b,stroke-width:2px,color:#000
    style H fill:#e3f2fd,stroke:#1565c0,stroke-width:3px,color:#000
    style P fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#000
    style V fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style N fill:#fff8e1,stroke:#f9a825,stroke-width:2px,color:#000
    style Q fill:#fce4ec,stroke:#ad1457,stroke-width:2px,color:#000
    style O fill:#dcedc8,stroke:#558b2f,stroke-width:3px,color:#000
```

*Figure 16.4 - Engineering-to-twin transformation. The canonical operational hierarchy is generated once. Semantic views and any exceptional namespace adaptation are separate, validated contributions; neither replaces the source evidence or becomes a second transform tree.*

##### Identity ledger and mapping contract

The bridge between source and published twin should be a versioned pipeline artifact, not an informal collection of renamed prim paths. File names below are illustrative; the contract matters more than the serialization:

| Artifact | Minimum record | Purpose |
|----------|----------------|---------|
| Source manifest | Source system, document, export tool/version, hash, original hierarchy, units, and revision | Makes the engineering input reproducible and auditable. |
| Identity ledger | `definitionId`, `occurrenceId`, source revision, source path, and provenance | Distinguishes the identity of a part design from the identity of one installed occurrence. Avoids treating a prim path as the only key. |
| Mapping plan | Source identity/path -> target asset package -> public prim path -> transformation-rule version | Makes hierarchy restructuring deterministic and supports incremental regeneration. |
| View map | BOM/station/group identifiers -> relationship or collection paths -> consumer meaning | Records semantic groupings without introducing a second transform hierarchy. |
| Namespace-edit record | Relocate source/target, rationale, target runtime, dependent-path result, and validation outcome | Makes every exceptional composed-namespace edit reviewable and reversible in the pipeline. |
| Publication report | Profile/version, payload/variant matrix, validation results, approved exceptions, and package hash | Proves what was actually published and against which contract. |

`assetInfo` is useful for model-level asset identity, name, version, and provenance. For per-part CAD/PLM identity, however, a project should use a documented typed, namespaced attribute or schema when interoperability is required, together with the external ledger. Ad-hoc `customData` can be a transitional implementation detail, not a substitute for a defined contract.

##### Re-import and namespace-edit rules

1. **Freeze and classify the source before changing it.** Preserve the raw/startpoint source and capture both the engineering hierarchy and the source identifiers that are actually available.
2. **Match by durable identity, not by path alone.** A new export path with the same verified occurrence ID should update source provenance without forcing a new public twin path. Missing, duplicated, or ambiguous IDs must be reported rather than guessed.
3. **Generate the canonical hierarchy through references and package interfaces.** Use functional/lifecycle boundaries, not every CAD body, as the decision for a reusable asset package.
4. **Represent alternate views separately.** A design BOM and a station BOM can point to the same canonical prims through relationships or collections, provided their consumer semantics, membership rules, and ordering requirements are explicitly defined.
5. **Use relocates only for a real namespace requirement.** Before authoring one, test whether a wrapper/reference arrangement achieves the requirement more transparently. If a relocate is justified, validate the new namespace, any compensating transforms, and all path-bearing opinions.
6. **Retarget through tooling, not text replacement.** Material bindings, attribute connections, joint targets, relationships, overrides, and references require composition-aware updates. [`UsdNamespaceEditor`](https://openusd.org/release/user_guides/namespace_editing.html) can assist, but its current OpenUSD documentation explicitly marks it as work in progress and not feature-complete; pin and test the exact OpenUSD/Kit/Isaac runtime.
7. **Validate every composition state that matters.** Namespace-edit dependency discovery cannot see unloaded payloads, unselected variants, inactive prims, or load-masked content. Test the supported payload and variant matrix, and treat unresolved relationship/connection targets as publication failures.

The official NVIDIA DSX asset journey illustrates the same separation in a concrete pipeline: conversion preserves source hierarchy, materials, and geometry; optimization restructures and packages content; metadata and connection points are authored as separate layers; the final composed asset is validated before delivery. [NVIDIA DSX SimReady asset journey](https://docs.omniverse.nvidia.com/dsx/latest/simready-assets.html).

The Isaac Sim structure strengthens the distinction introduced in Section 15:

| Isaac Sim concept | Proposed USD GoodStart interpretation |
|-------------------|--------------------------|
| `robot_name.usda` | Public `<asset_id>.usd` wrapper/interface referenced by `ASS_LYR.usda` |
| `base.usda` plus geometry/material/instances files | Private asset-package assembly below the public wrapper |
| `robot.usda` | Asset-local schema/semantic contribution; do not author it into source geometry |
| Common plus backend-specific physics layers | Asset-local physics implementations; project `SIM_LYR` remains responsible for scene/shot simulation opinions |
| Controller, ROS, sensor, or end-effector stacks | Optional feature packages selected by variants and/or loaded by payloads |
| Variant selections | Stable configuration interface for downstream users and automation |

**Recommended rule for the proposed USD GoodStart layer order:** `ASS_LYR.usda` should reference only the published interface of an Isaac-style asset package. It should not reach directly into `geometries.usd`, `physx.usda`, controller graphs, or other package internals. Project-level layers may override declared public properties, but internal paths remain implementation details unless the asset contract explicitly promotes them.

#### What transfers directly to a factory digital twin

- **One public interface per reusable unit:** the factory, each production line, each cell, each machine, and each robot can expose a stable USD entry point.
- **Shared base separated from optional features:** spatial hierarchy, geometry, materials, and stable semantics remain independent from physics, control, sensor, process, or maintenance features.
- **Nested references:** a factory references line interfaces; a line references cell and equipment interfaces; a cell references machine and robot interfaces. Internal files remain private to their package.
- **Payload granularity:** buildings, line internals, detailed machines, collision meshes, and simulation-only features can load on demand.
- **Variants as bounded configuration:** variants can select approved layout alternatives, equipment options, physics backends, fidelity levels, or commissioned configurations without changing the public asset path.
- **Backend isolation:** rigid-body, logistics/material-flow, thermal, airflow, robotics, and other domain-specific simulation opinions should not overwrite shared geometry or stable metadata.

#### What must be adapted

| Robot-oriented 3.0 concept | Factory digital-twin adaptation |
|----------------------------|---------------------------------|
| One kinematic `base.usda` | Site/building/area/line/cell hierarchy assembled from nested public asset interfaces |
| `robot.usda` schema contribution | Stable semantics, asset identity, classification, topology, connection points, source IDs, and lifecycle metadata |
| `instances.usda` | Equipment placement, repeated-machine instancing, visual/collision assembly, and layout instances |
| Physics backend variant | Domain/fidelity profile such as rigid-body, logistics, thermal, airflow, or robotics backend; only where alternatives are genuinely exclusive |
| Controller / ROS stack | PLC, OPC UA, ROS, MES, SCADA, or simulation control adapters, kept separate from stable asset truth |
| End-effector variant | Tooling, fixture, product format, machine module, or robot tool-center-point configuration |
| Robot sensors | Factory sensors and logical measurement points with stable identities; live values remain external/session-backed |
| Robot package validation | Hierarchy, units, coordinates, connection topology, metadata, source provenance, payload closure, and domain-specific simulation validation |

The most important adaptation is **time semantics**. Variant sets describe discrete authored configurations; they should not be used as a high-frequency state machine for a running plant. Current temperatures, PLC bits, joint positions, work orders, alarms, and material locations belong in `RUNTIME_LYR.usda`, a session layer, Fabric, or an external time-series/data system. Intrinsic reusable product properties belong in asset-local property layers; project- and instance-scoped identifiers, mappings, and engineering context belong in `DATA_LYRs.usda`. Simulation scenarios and predicted states belong in `SIM_LYR.usda` or explicitly published scenario packages.

#### Recursive factory composition model

```mermaid
flowchart TB
    Root["Proposed USD GoodStart<br/>project root<br/>scene-level ownership stack"]
    ASS["ASS_LYR.usda<br/>references published<br/>asset interfaces"]
    DATA["DATA_LYRs.usda<br/>project / instance IDs<br/>mappings + context"]
    SIM["SIM_LYR.usda<br/>scenario + project<br/>simulation opinions"]
    RUN["RUNTIME_LYR.usda / session<br/>live values + latest state"]

    Factory["factory.usda<br/><b>public factory interface</b>"]

    subgraph FactoryPackage["Factory asset package"]
        direction TB
        FactoryBase["base.usda<br/>site + building + area hierarchy"]
        FactorySem["semantics.usda<br/>classification + source identity"]
        FactoryTopo["topology.usda<br/>ports + networks + material flow"]
        FactoryVariants{"Approved configuration variants<br/>layout · fidelity · commissioned option"}

        FactoryBase -->|"sublayer / reference"| FactorySem
        FactoryBase -->|"sublayer / reference"| FactoryTopo
    end

    subgraph NestedAssets["Recursively composed asset interfaces"]
        direction LR
        Line["line_A.usda<br/>production line"]
        Cell["cell_01.usda<br/>work cell"]
        Machine["machine.usda<br/>equipment package"]
        Robot["robot.usda<br/>Asset Structure 3.0 package"]
        Mobile["amr.usda<br/>mobile robot package"]

        Line -->|"references"| Cell
        Cell -->|"references"| Machine
        Cell -->|"references"| Robot
        Line -->|"references"| Mobile
    end

    subgraph FeatureDomains["Optional / selectively loaded feature domains"]
        direction LR
        Physics["physics<br/>rigid body + collision"]
        Process["process<br/>material flow + cycle logic"]
        Controls["controls<br/>PLC · OPC UA · ROS · MES adapters"]
        Sensors["sensors<br/>measurement-point definitions"]
        Safety["safety<br/>zones + constraints"]
    end

    Root --> ASS
    Root --> DATA
    Root --> SIM
    Root --> RUN
    ASS -->|"references public interface"| Factory
    Factory -->|"references"| FactoryBase
    FactoryBase -->|"references / payloads"| Line
    Factory --> FactoryVariants
    FactoryVariants -.->|"variant / payload"| Physics
    FactoryVariants -.->|"variant / payload"| Process
    Factory -.->|"payload"| Controls
    Factory -.->|"payload"| Sensors
    Factory -.->|"payload"| Safety
    DATA -.->|"stable metadata opinions"| Factory
    SIM -.->|"scenario overrides"| Factory
    RUN -.->|"live state; never asset source"| Factory

    style Root fill:#e3f2fd,stroke:#0d47a1,stroke-width:2px,color:#000
    style ASS fill:#bbdefb,stroke:#1565c0,stroke-width:2px,color:#000
    style DATA fill:#dcedc8,stroke:#558b2f,stroke-width:2px,color:#000
    style SIM fill:#ffe0b2,stroke:#ef6c00,stroke-width:2px,color:#000
    style RUN fill:#f8bbd0,stroke:#ad1457,stroke-width:2px,color:#000
    style Factory fill:#ffcc80,stroke:#e65100,stroke-width:3px,color:#000
    style FactoryPackage fill:#fff8e1,stroke:#f9a825,stroke-width:2px,color:#000
    style NestedAssets fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000
    style FeatureDomains fill:#ede7f6,stroke:#5e35b1,stroke-width:2px,color:#000
    style FactoryVariants fill:#ffe082,stroke:#f57f17,stroke-width:2px,color:#000
```

*Figure 16.5 - Proposed recursive factory adaptation. The proposed USD GoodStart layer order retains scene-level ownership lanes while the factory and its subsets expose nested public asset interfaces. Authored configurations use variants/payloads; runtime state remains a separate contribution.*

#### Proposed factory package profile

```text
010_ASS_USD/USD_Wrappers/<factory_id>/
  <factory_id>.usda                 # public factory interface
  payloads/
    base.usda                       # site/building/area hierarchy
    geometries.usd                  # package-owned geometry where applicable
    instances.usda                  # placements and reusable instances
    materials.usda
    semantics.usda                  # classification and stable asset identity
    topology.usda                   # ports, networks, adjacency, material flow
    areas/
      <line_id>.usda                # references public line/cell interfaces
  features/
    physics/
      neutral.usda
      physx.usda
      other_backend.usda
    process/
      material_flow.usda
      cycle_logic.usda
    controls/
      plc_interface.usda
      opcua_interface.usda
      ros_interface.usda
    sensors/
      measurement_points.usda
    safety/
      zones.usda
      constraints.usda
  data/
    source_manifest.json
    mapping_profile.json
    package_contract.json

010_ASS_USD/USD_Wrappers/<line_or_cell_id>/
  <line_or_cell_id>.usda            # independently reusable nested package

010_ASS_USD/USD_Wrappers/<machine_or_robot_id>/
  <machine_or_robot_id>.usda        # machine profile or robot Asset Structure 3.0
```

This is intentionally a **profile**, not a mandatory folder explosion. A small static factory model may need only a public interface, a base payload, materials, and metadata. Additional feature folders should be created only when a real ownership, loading, configuration, or simulation boundary exists.

#### Resulting USD GoodStart proposal

The proposed USD GoodStart layer order should consider Asset Structure 3.0 as the basis for an optional **recursive Digital Twin Asset Package profile**:

1. Keep the existing thin project root and scene-level layer-strength contract.
2. Make `ASS_LYR.usda` the boundary to public factory/equipment interfaces.
3. Allow the same interface/payload/variant pattern to repeat at factory, line, cell, machine, and robot scale.
4. Keep stable semantics and topology loadable independently from heavy geometry.
5. Keep runtime telemetry and latest operational state outside the authored configuration variants.
6. Validate every package boundary and record source/mapping evidence in its contract and reports.

The approach is therefore suitable for digital twins, but only after separating **recursive asset composition** from **project ownership layers** and **live operational state**. That separation is the part that prevents a factory-scale application of Asset Structure 3.0 from becoming an unmanageable robot package with thousands of unrelated responsibilities.

### 16.2 Case Study: Workcell-DigitalTwin to Asset Structure 3.0

This case study applies the preceding principles to the **nAurava Technologies Workcell-DigitalTwin project** and a locally inspected working copy. The purpose is not to criticize a functioning demonstration stage. It is to identify what a reproducible dataprep and publication pipeline must do when a composed engineering/simulation scene becomes a reusable 3.0-ready asset product.

> **Work-in-progress and independent case-study status:** The nAurava Technologies asset is still under development. Its GitHub repository is therefore intentionally not linked from this paper at this time; a direct repository reference can be added once the asset is finished and ready to serve as a public case-study source. The migration assessment, target structures, diagrams, and recommendations are the author's independent work. This section is not an AOUSD or IEDT Interest Group case study, publication, recommendation, validation result, or endorsement. This paper analyzes package structure only; it does not relicense or redistribute project or third-party assets.

#### Evidence boundary and terminology

The project's canonical assembly is `workcell_digitaltwin.usd`. The detailed counts below come from the local ASCII inspection copy `workcell_digitaltwin.usda` on **2026-07-16**; that inspection copy was untracked in the local Workcell working copy and is therefore evidence for this case-study snapshot, not a claim about an additional published source file. The canonical binary stage, evolving project source, and generated ASCII inspection copy must be treated as different artifacts in provenance records.

“Asset Structure 3.0-ready” is used here as an **architectural target**, not as a claim that NVIDIA publishes a factory-specific conformance certificate. The official Isaac Sim pattern is robot-oriented. This case study adapts its stable public interface, shared base, payload, and variant principles recursively to a workcell while preserving the distinction between asset-local packaging and scene-level ownership.

#### Initial state: useful content with mixed ownership

The inspected project snapshot already contains two different maturity levels:

1. **UR10 and Robotiq are already close to the 3.0 pattern.** Their public `.usda` files reference `payloads/base.usda`, expose physics variant sets, and load backend-specific physics with payloads. They should be validated and reused, not flattened and rebuilt into the workcell.
2. **Most CAD-derived equipment remains single-file or lightly packaged.** Table, bin, robot base, wall, X-ray scanner, battery pack, and related items pair engineering source files such as STEP/STP with processed USD assets, but do not yet expose the same uniform public-interface contract.
3. **The workcell root is simultaneously an assembly, lookdev layer, physics integration layer, environment, runtime snapshot, and viewport/render document.** In the inspected ASCII copy, the 4,550-line stage contains 19 payload mentions, 73 `def` declarations, 729 `over` declarations, seven embedded materials, extensive physics/PhysX opinions, environment content, camera metadata, and render settings. It composes component files with payloads and authors many deep overrides below their imported prims.

```mermaid
flowchart TB
    Sources["Engineering + supplier sources<br/>STEP · STP · URDF · MJCF<br/>supplier USD"]
    CadAssets["CAD-derived components<br/>table · bin · base · wall<br/>scanner · battery · conveyor"]
    ReadyAssets["Already 3.0-like packages<br/>UR10 · Robotiq<br/>public interface + base<br/>variants + physics payloads"]
    MixedRoot["workcell_digitaltwin.usd<br/>one mixed-authoring stage"]
    Assembly["Assembly placements<br/>component payloads + transforms"]
    Looks["Embedded Looks<br/>bindings + remote<br/>MDL dependencies"]
    Physics["Physics integration<br/>colliders + joints<br/>deep overrides"]
    Scene["Environment + ground + cameras<br/>render settings + runtime values"]

    Sources --> CadAssets
    Sources --> ReadyAssets
    CadAssets --> MixedRoot
    ReadyAssets --> MixedRoot
    MixedRoot --> Assembly
    MixedRoot --> Looks
    MixedRoot --> Physics
    MixedRoot --> Scene

    style Sources fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000
    style CadAssets fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#000
    style ReadyAssets fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000
    style MixedRoot fill:#ffcdd2,stroke:#c62828,stroke-width:3px,color:#000
    style Assembly fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000
    style Looks fill:#fce4ec,stroke:#ad1457,stroke-width:2px,color:#000
    style Physics fill:#ede7f6,stroke:#5e35b1,stroke-width:2px,color:#000
    style Scene fill:#f1f8e9,stroke:#558b2f,stroke-width:2px,color:#000
```

*Figure 16.6 - Inspected initial state. The red box is not “bad USD”; it is a useful integration stage whose responsibilities must be classified before it can become a reusable asset publication.*

The conversion must therefore preserve the working composition while moving each opinion to an explicit owner. A naive “save every prim into a new folder” operation would break deep override paths, joint relationships, material bindings, source traceability, or all four.

#### Target invariant: package once, wrap as needed

The three requested outcomes should not be maintained as three separately converted workcells. They share one canonical 3.0-ready workcell package:

```text
canonical reusable product
  = Workcell Asset Structure 3.0-ready package

delivery A
  = canonical package opened directly

delivery B
  = minimal root + ENV + MTL + ASS around the canonical package

delivery C
  = proposed USD GoodStart ownership stack around the canonical package
```

The package owns reusable defaults and internal implementation. The envelope owns project-, scenario-, review-, or runtime-specific opinions. This avoids three copies drifting apart and makes migration from the minimal envelope to USD GoodStart a scene-governance change rather than another CAD conversion.

#### Required dataprep and publication pipeline

```mermaid
flowchart TB
    P0["0 · Declare target profile<br/>public prims · variants · loading<br/>simulation requirements"]
    P1["1 · Freeze + manifest inputs<br/>definition/occurrence IDs · hashes<br/>tool versions"]
    P2["2 · Inspect + classify stage<br/>assembly · geometry · materials<br/>physics · environment · runtime"]
    P3["3 · Define package boundaries<br/>workcell · robot · gripper · conveyor<br/>scanner · table · bin · product"]
    P4["4 · Normalize + map<br/>units · Z-up · pivots · names<br/>instances · identity ledger"]
    P5["5 · Build / retain packages<br/>public interface · base · materials<br/>semantics · feature payloads"]
    P6["6 · Build workcell package<br/>instances reference component<br/>public interfaces only"]
    P7["7 · Retarget authored opinions<br/>relationships · bindings · joints<br/>sensors · configuration · environment"]
    P8["8 · Validate closure + equivalence<br/>composition · transforms · appearance<br/>physics · paths · performance"]
    P9["9 · Publish atomically<br/>versioned package + manifest<br/>reports + chosen envelope"]

    P0 --> P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P7 --> P8 --> P9

    style P0 fill:#fff3e0,stroke:#ef6c00,stroke-width:2px,color:#000
    style P1 fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000
    style P2 fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#000
    style P3 fill:#e8eaf6,stroke:#3949ab,stroke-width:2px,color:#000
    style P4 fill:#e0f2f1,stroke:#00796b,stroke-width:2px,color:#000
    style P5 fill:#e8f5e9,stroke:#2e7d32,stroke-width:2px,color:#000
    style P6 fill:#e3f2fd,stroke:#1565c0,stroke-width:2px,color:#000
    style P7 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#000
    style P8 fill:#fff8e1,stroke:#f9a825,stroke-width:2px,color:#000
    style P9 fill:#dcedc8,stroke:#558b2f,stroke-width:3px,color:#000
```

*Figure 16.7 - Conversion pipeline. File conversion occurs inside steps 4-6; requirements, ownership mapping, retargeting, validation, and publication are equally important deliverables.*

The steps have the following Workcell-specific responsibilities:

1. **Declare the product contract before restructuring.** Decide which prim paths are public, which subsets load independently, which physics/controller/sensor variants are supported, which component placements are addressable, and whether the environment belongs to the reusable workcell or to the consuming scene.
2. **Create a source manifest and identity ledger.** Record the STEP/STP, URDF, MJCF, supplier USD, textures, validation JSON, licenses, Git commit, conversion settings, hashes, original source hierarchy, definition IDs, occurrence IDs, and source revisions where available. Preserve the existing source folders; generated packages must not replace their evidence.
3. **Inventory the composed stage and create the mapping plan.** Traverse prims and composition arcs, classify every authored field, and generate a source-identity/path-to-target-owner/public-path mapping. Explicitly distinguish canonical hierarchy, presentation relationship/collection membership, and any genuine namespace edit. Flag stale `delete payload` edits, absolute/external paths, remote material URLs, and overrides into package-private prims.
4. **Define reusable boundaries.** The workcell, UR10, Robotiq gripper, conveyor, scanner, robot base, tables, bins, battery pack, and wall/guarding should each have a stable public entry point when they are independently reusable or replaceable. Do not create a package merely because a CAD body exists; use functional and lifecycle boundaries.
5. **Normalize without erasing provenance.** Enforce meters and Z-up, establish stable pivots and local frames, sanitize names, preserve source identity through a documented typed contract and the identity ledger, detect repeated parts, and produce visual/collision representations according to the selected capability profile. A path change alone must never be treated as proof of a new component identity.
6. **Retain mature packages.** UR10 and Robotiq already demonstrate the desired public-interface/base/physics-variant pattern. Validate their defaults and dependencies, then reference their public files. Repacking their internal geometry into the workcell would destroy the boundary this migration is trying to create.
7. **Package the remaining components.** Generate a public `<asset_id>.usda`, a stable base, geometry/instance/material/semantic contributions, optional collision or backend physics payloads, and validation reports. Static props need only the features they actually support; they do not need empty robot/controller folders.
8. **Author the workcell assembly through public interfaces.** `instances.usda` or the equivalent assembly contribution owns component placement and references the published component roots. Scene code must not reference `geometries.usd`, internal links, or private material prims directly.
9. **Retarget integration opinions and views.** Move material bindings, fixed joints, collision overrides, conveyor behavior, grasp guides, sensors, connections, and alternate BOM/station groupings to package-local feature layers or declared scene layers. Deep `over` paths, relationship targets, attribute connections, and collection membership must be mapped to stable public prims or promoted connection points; textual path replacement is not sufficient. Any relocate is an exceptional, separately recorded namespace edit rather than a default layout operation.
10. **Separate discrete configuration from runtime state.** Layout, physics backend, robot tool, product format, and fidelity can be bounded variants. Belt velocity, live joint state, current battery position, PLC values, alarms, and measurements belong in runtime/session infrastructure, not in asset variants.
11. **Validate equivalence before publishing.** Compare transforms, extents, material assignments, loaded/unloaded payload behavior, collision coverage, joints, default variant selections, articulation behavior, and visual output against the accepted initial stage. A structurally cleaner stage that changes the working simulation is a failed conversion.
12. **Publish atomically.** Version the public package, dependency lock, source manifest, mapping report, validation results, and envelope together. Downstream consumers switch one published interface only after all gates pass.

#### Workcell concern-routing map

| Inspected initial concern | Canonical 3.0-ready owner | Minimal envelope override | Proposed USD GoodStart owner |
|---------------------------|---------------------------|---------------------------|----------------------------------|
| Component payloads and placements | `workcell/payloads/instances.usda`, referencing component public interfaces | `ASS_LYR.usda` references `workcell.usda` | `ASS_LYR.usda` references `workcell.usda` |
| UR10 and Robotiq package internals | Existing component packages; validate, do not copy | No direct access | No direct access |
| Workcell-owned geometry | Workcell base/geometry payload or a dedicated wall/ground asset | No geometry authored in root | No geometry authored in root |
| Reusable default materials | Asset-local `materials.usda` | Project look overrides in `MTL_LYR.usda` | Project look overrides in `MTL_LYR.usda` |
| Ground, lights, scene environment | Optional workcell environment feature only for self-contained delivery A | `ENV_LYR.usda` | `ENV_LYR.usda` |
| Reusable component collision/physics | Component-local neutral/backend feature payloads | Asset defaults remain active | Asset defaults remain active; `PHY_LYR.usda` authors project integration overrides |
| Fixed joints and connections between assets | Workcell-local topology/physics feature using promoted attachment points | Remains in workcell package unless project-specific | `PHY_LYR.usda` or `SIM_LYR.usda` only when scenario-specific |
| Layout or backend alternatives | Declared variant sets on the public workcell/component interface | Select public variants in `ASS` or a small configuration layer | Select public variants in `VAR_LYR.usda` |
| Stable source IDs and engineering metadata | Asset-local semantics plus manifest | Not duplicated | `DATA_LYRs.usda` adds project/system mappings without replacing asset identity |
| Conveyor speed, joint values, current product positions | Not authored as reusable asset truth | External/session state | `RUNTIME_LYR.usda` or session/Fabric/external data system |
| Cameras and viewport/render settings | Preview defaults only if deliberately part of the asset product | Root metadata or `ENV_LYR` by documented minimal policy | `CAM_LYR.usda`; review/render overrides may use `OPIN_LYR.usda` |
| Validation JSON and migration evidence | Package `data/` and publication reports | Referenced by release metadata, not composed as scene opinions | Same; project QA may aggregate results outside the USD stage |

#### Delivery A: pure Asset Structure 3.0-inspired workcell product

This is the reusable product without a project layer stack. It is appropriate when the workcell itself is the deliverable and must open directly with sensible defaults.

```text
Workcell_AS3/
  workcell.usda                       # stable public interface + default variants
  payloads/
    base.usda                         # stable hierarchy / package assembly
    instances.usda                    # placements; references component public roots
    geometries.usdc                   # only geometry genuinely owned by the workcell
    materials.usda                    # reusable default materials and bindings
    semantics.usda                    # stable IDs, classifications, attachment points
    Physics/
      physics.usda                    # neutral/shared physics contribution
      physx.usda                      # optional backend implementation
  features/
    environment/environment.usda      # optional self-contained preview environment
    process/material_flow.usda
    controls/controller_interfaces.usda
    sensors/measurement_points.usda
  data/
    source_manifest.json
    mapping_report.json
    package_contract.json
    validation/
  dependencies/
    dependency_lock.json              # UR10, Robotiq, conveyor, props, etc.
```

`workcell.usda` references the stable base, exposes only supported variants, and payloads optional/heavy features. `instances.usda` references `ur10.usda`, `Robotiq_2F_85.usda`, and every other component's public interface. The workcell package must not reach into their `payloads/` folders. If environment or process behavior is not part of the reusable product contract, omit those features rather than publishing empty placeholders.

#### Delivery B: thin three-layer scene plus 3.0-ready assets

This is the smallest governed scene envelope. The root contains metadata and the ordered sublayer list only. Strong-to-weak order is **ENV → MTL → ASS** so scene environment and look overrides can refine the referenced asset defaults.

```text
Workcell_Minimal/
  Workcell_ROOT.usda                  # thin root; subLayers only
  020_LYR/
    ENV_LYR.usda                      # ground, lights, scene environment
    MTL_LYR.usda                      # project-specific look overrides
    ASS_LYR.usda                      # references Workcell_AS3/workcell.usda
  010_ASS_USD/
    Workcell_AS3/                     # canonical package; not a copied rewrite
```

```usda
#usda 1.0
(
    defaultPrim = "World"
    metersPerUnit = 1
    upAxis = "Z"
    subLayers = [
        @./020_LYR/ENV_LYR.usda@,
        @./020_LYR/MTL_LYR.usda@,
        @./020_LYR/ASS_LYR.usda@
    ]
)
```

Physics defaults remain inside the 3.0-ready component/workcell packages. If project-specific physics, runtime state, animation, or data integration becomes necessary, do not overload these three layers indefinitely; graduate to delivery C.

#### Delivery C: proposed USD GoodStart layer order plus 3.0-ready assets

This is the operational digital-twin envelope. It uses the same canonical workcell package, but distributes scene-level authorship across explicit ownership lanes.

```text
Workcell_USDGoodStart/
  Workcell_ROOT.usda
  000_SOURCE/                        # preserved engineering sources / manifests
  010_ASS_USD/
    Workcell_AS3/workcell.usda       # canonical public workcell interface
  020_BASE_LYR/
    OPIN_LYR.usda
    CAM_LYR.usda
    ENV_LYR.usda
    ACTGR_LYR.usda
    ANIM_LYR.usda
    VAR_LYR.usda
    MTL_LYR.usda
    PHY_LYR.usda
    ASS_LYR.usda                     # references only workcell.usda
  030_SIM_LYR/SIM_LYR.usda
  035_RUNTIME_LYR/RUNTIME_LYR.usda
  040_DATA_LYRs/DATA_LYRs.usda
```

The proposed strong-to-weak order remains **OPIN → CAM → ENV → RUNTIME → SIM → DATA → ACTGR → ANIM → VAR → MTL → PHY → ASS**. The important constraint is that these project layers do not duplicate asset-package ownership:

- `ASS_LYR` places the public workcell interface; it does not rebuild the workcell.
- `PHY_LYR` owns scene/project integration overrides; reusable component physics remains asset-local.
- `VAR_LYR` selects declared public variants; it does not author private variant internals.
- `MTL_LYR` provides project look overrides; reusable default materials remain in their asset packages.
- `DATA_LYRs` maps project systems and identifiers; it does not replace source identity or package manifests.
- `RUNTIME_LYR` carries latest/live state; it never becomes the source for the next asset publication.

#### Comparing the three final states

| Decision | A - Pure 3.0-ready product | B - Thin layers + 3.0 | C - Proposed USD GoodStart + 3.0 |
|----------|----------------------------|-----------------------|----------------------------------|
| Canonical asset package | Yes | Same package | Same package |
| Scene-level layers | None | `ENV`, `MTL`, `ASS` | Full ownership stack |
| Opens as self-contained workcell | Yes, if preview environment is included | Yes | Yes |
| Best fit | Reusable library/product delivery | Small project, review, demonstration | Operational twin, simulation programs, multi-system collaboration |
| Runtime/live-state lane | External only | External only | Explicit `RUNTIME`/session lane |
| Project simulation lane | Asset defaults/features | Not explicit | Explicit `SIM` and `PHY` responsibilities |
| Static system-data lane | Package semantics/manifest | Not explicit | Explicit `DATA` aggregation/mapping |
| Authoring overhead | Lowest scene governance; strong package discipline | Low | Highest, justified only by real ownership needs |
| Migration relationship | Foundation | Wraps A | Wraps A; can replace B without reconverting A |

**Recommended sequence for this project:** build and validate delivery A as the canonical publication; adopt delivery B as the immediate replacement for the mixed demonstration root; introduce delivery C when the Workcell becomes an operational twin with live state, scenario simulation, system mappings, multiple authoring roles, or persistent project overrides.

#### Acceptance gates for this case study

The conversion is complete only when all of the following are demonstrated:

- One stable public workcell path and one public path per reusable component.
- All assembly dependencies target public interfaces and resolve package-relatively or through a versioned resolver policy.
- No scene layer authors opinions against undocumented package-private prim paths.
- Meters, Z-up, time codes, pivots, and default prims are declared and validated consistently.
- Every supported variant has a documented meaning, valid default, complete dependency closure, and successful load test.
- The stage opens with all payloads loaded, with optional payloads unloaded, and under each supported configuration.
- Remote materials and third-party content have reproducible dependency and license records.
- Source-to-target prim mappings, removed/stale edits, and manually approved exceptions are recorded.
- Definition and occurrence identities are unique where required; a changed source path with the same verified identity preserves the intended published contract, while missing or ambiguous identities block automated reconciliation.
- Relationship and collection targets resolve in every supported payload/variant state. Each relocate has a documented rationale, target-runtime compatibility check, and namespace/transform-equivalence result.
- Visual placement, material appearance, collision coverage, joints, articulation, conveyor behavior, and task behavior match the accepted initial-state baseline within declared tolerances.
- Re-importing one changed CAD component can regenerate and republish that component without changing unrelated public paths or rebuilding the entire workcell.

The final state is therefore not defined by a prettier folder tree. It is defined by **stable public contracts, explicit ownership, reproducible transformation, controlled configuration, selective loading, and proven behavioral equivalence**.

### Optional Isaac-style robot package profile

For robot and multi-physics assets, the generic proposed USD GoodStart asset-package template can support an Isaac-aligned profile such as:

```text
010_ASS_USD/USD_Wrappers/<robot_id>/
  <robot_id>.usda              # public asset interface
  layers/
    base.usda                  # structural assembly
    geometries.usd
    materials.usda
    instances.usda
    robot.usda                 # robot schema contribution
    physics/
      physics.usda             # shared / neutral physics
      physx.usda
      mujoco.usda
    controllers/
    end_effectors/
  data/
    source_manifest.json
    mapping_profile.json
```

This profile should be **optional**, because a static industrial asset does not need empty robot, controller, or multi-backend physics files. The package contract should declare supported variants, payloads, default selections, public prims, and which internal contributions are required. The proposed USD GoodStart scene root and its existing layer-strength policy remain unchanged.

### Research conclusion

Isaac Sim Asset Structure 3.0 is a strong reference implementation for the proposed USD GoodStart reusable asset boundary. It confirms that complex simulation assets scale by combining a thin public interface with purpose-specific internal layers, deferred payloads, and explicit variants. The transferable lesson is not the literal robot filenames; it is the stable separation of shared asset data, backend-specific simulation data, optional behavior stacks, and the single downstream reference target.

## 17. NVIDIA SimReady Foundation: Capability Contracts, Validation, and Standardization

**Primary sources:** [NVIDIA SimReady Foundation repository](https://github.com/NVIDIA/simready-foundation) · [SimReady Standardization Workflow](https://docs.omniverse.nvidia.com/simready/latest/simready-standards/standardization_workflow.html) · [Validation Workflow](https://github.com/NVIDIA/simready-foundation/blob/main/nv_core/sr_specs/docs/guides/validate_workflow.md) · [Profiles Validation Workflow](https://github.com/NVIDIA/simready-foundation/blob/main/nv_core/sr_specs/docs/guides/profiles_validation_workflow.md) · [Repository Acceptance Workflow](https://github.com/NVIDIA/simready-foundation/blob/main/nv_core/sr_specs/docs/guides/acceptance_workflow.md)

SimReady belongs in this research as a **separate architectural axis**. Asset Structure 3.0 is primarily a composition and packaging pattern: it determines how a reusable product can expose one public identity while organizing shared data, variants, and payloaded features. SimReady Foundation defines what a declared asset capability means, which requirements prove it, how validators execute those requirements, and how specifications mature into reproducible industry workflows.

The distinction can be summarized as follows:

| Concern | Main question | Primary mechanism |
|---------|---------------|-------------------|
| Asset Structure 3.0 | How is one configurable asset product composed, loaded, and published? | Public interface, references, payloads, variants, package-local layers |
| SimReady Foundation | What must an asset support for a named simulation use case, and how is that claim verified? | Versioned profiles, features, requirements, rules, reports, validation metadata |
| Proposed USD GoodStart layer order | Who owns scene/project opinions and which peer contribution wins? | Thin root and ordered scene-level ownership layers |
| Dataprep/publication pipeline | How are source models transformed into a package that satisfies the selected contracts? | Mapping, conversion, enrichment, validation, provenance, atomic publication |

These systems can reinforce one another, but none is a substitute for the others. A well-organized 3.0 package can fail its selected SimReady profile. A SimReady-validated asset can still be placed in a poorly governed scene. A clean USD GoodStart stack cannot repair missing collision, invalid units, or an incomplete articulation.

### The SimReady specification hierarchy

The current Foundation repository operationalizes SimReady through four interlocking specification surfaces. Profiles select features; features bundle requirements and dependencies; capabilities organize requirement domains; executable rules enforce the individual requirements.

```mermaid
flowchart TB
    Profile["Profile<br/>named + versioned<br/>simulation-use-case contract"]
    Features["Features<br/>queryable asset behaviors<br/>and properties"]
    Capabilities["Capabilities<br/>domains that organize<br/>related requirements"]
    Requirements["Requirements<br/>single testable statements<br/>with stable IDs"]
    Rules["Validator rules<br/>executable checks<br/>against the USD asset"]
    Result["Validation result<br/>per requirement + feature<br/>+ overall profile"]
    Evidence["Publication evidence<br/>JSON report + optional<br/>validation metadata stamp"]

    Profile -->|"selects exact feature versions"| Features
    Features -->|"collect requirements + dependencies"| Requirements
    Capabilities -->|"organize requirement domains"| Requirements
    Requirements -->|"are enforced by"| Rules
    Rules --> Result
    Result --> Evidence

    style Profile fill:#ffcc80,stroke:#e65100,stroke-width:3px,color:#000
    style Features fill:#d1c4e9,stroke:#5e35b1,stroke-width:2px,color:#000
    style Capabilities fill:#b2dfdb,stroke:#00796b,stroke-width:2px,color:#000
    style Requirements fill:#bbdefb,stroke:#1565c0,stroke-width:2px,color:#000
    style Rules fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px,color:#000
    style Result fill:#fff9c4,stroke:#f9a825,stroke-width:2px,color:#000
    style Evidence fill:#eceff1,stroke:#546e7a,stroke-width:2px,color:#000
```

*Figure 17.1 - SimReady's validation hierarchy. A profile claim is meaningful only when its pinned features, transitive requirements, executable rules, and results can be resolved for the declared versions.*

| Level | Role | Repository realization | Example from official guidance |
|-------|------|------------------------|--------------------------------|
| **Requirement** | One testable rule with an identifier | Requirement documentation and validation code under `nv_core/sr_specs/docs/capabilities/` | A stage must define a default prim |
| **Capability** | Domain/category that organizes related requirements | Capability folders such as Sample, Visualization/Geometry, or Units | Units, hierarchy, geometry, materials |
| **Feature** | Versioned bundle of requirements and feature dependencies describing a behavior/property | Feature JSON plus documentation under `nv_core/sr_specs/docs/features/` | Minimal placeable visual, rigid-body physics, driven joints |
| **Profile** | Named, versioned bundle of exact feature versions for one complete simulation scenario | `nv_core/sr_specs/docs/profiles/profiles.toml` and profile documentation | `Prop-Robotics-Neutral`, `Prop-Robotics-Physx`, `Robot-Body-Neutral`, `Robot-Body-Runnable` |

The profile is the producer/consumer contract. Validation resolves its exact feature versions, includes transitive feature dependencies, collects the associated requirement IDs, executes the backing rules, and reports results at requirement, feature, and profile level. This is substantially stronger than calling an asset “simulation ready” based on visual inspection or the presence of a physics API.

### What SimReady does and does not decide

SimReady can define and validate facts such as units, default prims, hierarchy properties, geometry readiness, materials, rigid-body behavior, articulations, joints, or other runtime-facing capabilities. It can also provide transformation and validation workflows between profiles, for example from a neutral asset toward a PhysX- or Isaac-oriented result.

SimReady does **not by itself prescribe one universal repository tree, sublayer order, or Asset Structure 3.0 package**. Individual requirements may constrain composition or prim organization when a capability depends on it, but a profile is fundamentally a capability contract, not a complete project architecture. It also does not define ownership of live telemetry, shot/scene overrides, review opinions, or project-level simulation results.

This matters for the Workcell case study. A table can pass a prop profile without using the same internal package layout as a robot. Conversely, a workcell may use the 3.0 interface/reference/payload/variant pattern and still lack a profile that proves material-flow, controller, sensor, safety, or workcell-topology capabilities.

### The SimReady standardization workflow

The published standardization workflow is not merely an asset-validation checklist. It is a process for defining a new simulation capability and making it adoptable:

```mermaid
flowchart TB
    subgraph Phase1["Phase 1 · Definition and alignment"]
        direction LR
        Domain["Domain + experts + partners"]
        UseCase["Scoped MVP use case"]
        Mapping["Conceptual data mapping"]
        Gap["OpenUSD gap analysis"]
        Domain --> UseCase --> Mapping --> Gap
    end

    subgraph Phase2["Phase 2 · Development and iteration"]
        direction LR
        Viability["Standardizable vs<br/>runtime-specific"]
        Draft["Specification +<br/>schema prototypes"]
        Build["Requirements + validators<br/>+ samples"]
        Beta["QA + internal/external beta"]
        Viability --> Draft --> Build --> Beta
    end

    subgraph Phase3["Phase 3 · Package deliveries"]
        direction LR
        Candidate["Candidate specification"]
        Pipeline["Converter + transformations<br/>+ validators"]
        Docs["Creator/runtime<br/>workflow documentation"]
        Samples["Sample content +<br/>end-to-end runtime evidence"]
        Candidate --> Pipeline --> Docs --> Samples
    end

    Phase1 --> Phase2 --> Phase3

    style Phase1 fill:#e3f2fd,stroke:#1565c0,stroke-width:3px,color:#000
    style Phase2 fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px,color:#000
    style Phase3 fill:#fff3e0,stroke:#ef6c00,stroke-width:3px,color:#000
```

*Figure 17.2 - Condensed SimReady Standardization Workflow. The output is not just a document: it includes specifications, validators, transformations, reference pipelines, workflow guidance, and sample content tested into target runtimes.*

#### Phase 1 - Definition and alignment

- Identify the domain, domain expert, OpenUSD expertise, QA/content/engineering responsibilities, stakeholders, and partners.
- Specify a deliberately bounded MVP use case, asset class, runtime interfaces, inputs, and outputs.
- Map existing standards or de facto domain data models to OpenUSD.
- Perform gap analysis where required data or behaviors have no suitable OpenUSD representation.

For a factory workcell, this phase must answer whether the target is only placeable visualization, rigid-body manipulation, robot execution, material-flow simulation, controller integration, sensor/synthetic-data generation, or a combination. “Digital twin” is too broad to serve as a single profile definition.

#### Phase 2 - Development and iteration

- Separate capabilities that are broadly standardizable from solver-, runtime-, or product-specific behavior that is not yet ready for standardization.
- Prototype content specifications, attributes, schemas, sample assets, and runtime connections.
- Define testable requirements and implement validators.
- Build creator workflows and iterate through QA, internal beta, and external beta against declared acceptance criteria.

This phase prevents a current project convention from being presented prematurely as an industry standard. A useful project-local workcell profile can exist before it is accepted as an official SimReady profile, provided its provenance and maturity are explicit.

#### Phase 3 - Package deliveries

- Publish the candidate specification and its versioned contracts.
- Provide converter/data-mapping implementation, post-export or pre-ingest transformations, validators, and runtime test procedures.
- Provide creator documentation showing how to author, validate, and exercise the capability.
- Supply sample content or datasets that demonstrate the capability and continuously exercise its validators.

The official workflow explicitly treats non-file sources such as streams and databases as valid pipeline inputs. That aligns with digital twins: the standardization problem is not limited to CAD-to-USD conversion, although authored runtime values must still be separated from stable asset truth.

### Where SimReady enters the dataprep pipeline

The Case Study pipeline in Section 16.2 should be extended with two separate kinds of contracts:

1. **Package contract:** public prims, private paths, dependencies, payload policy, variant interface, ownership, and versioning.
2. **Capability profile:** features and requirements the published entry point claims to satisfy for a named simulation scenario.

```text
source evidence
  -> conceptual data mapping
  -> conversion and normalization
  -> 3.0-ready package composition
  -> profile-specific enrichment / transformation
  -> requirement validation
  -> runtime acceptance tests
  -> publish package + profile/version claim + reports
```

Validation should run during conversion, at component publication, at workcell assembly, and in the target runtime. The chosen profile and version must be pinned in the build manifest and validation record; silently validating against “latest” would make a previously published claim non-reproducible.

### Applying SimReady to the Workcell case study

| Publication boundary | Existing or candidate profile direction | Immediate evidence required |
|----------------------|-----------------------------------------|-----------------------------|
| Table, bin, battery pack, static fixtures | Existing neutral/PhysX prop profiles where applicable | Placeability, units, geometry, materials, collision/rigid-body behavior, validation JSON |
| UR10 robot body | Existing neutral/runnable/Isaac-oriented robot profiles as supported | Articulation, driven joints, physics backend, default variants, runtime execution |
| Robotiq gripper | Applicable robot/end-effector feature set; do not assume the robot-body profile is automatically sufficient | Joint behavior, grasp/contact behavior, attachment interface, selected physics implementation |
| Conveyor | Existing features plus a project-local behavior profile if driven material transport is not covered | Collision, driven surface/actuation, velocity interface, runtime behavior |
| X-ray scanner and sensors | Existing placeable/visual features plus candidate sensor capability if required | Coordinate frame, sensor interface, outputs, runtime/synthetic-data behavior |
| Workcell public interface | Composition validation plus a candidate workcell profile if no accepted profile covers the use case | Dependency closure, public interfaces, configuration, topology, runtime task acceptance |

The workcell must not be stamped with a broad profile merely because each child asset passes some profile. Aggregate composition can introduce new failures: invalid attachment frames, overlapping collisions, broken relationships, incompatible variant defaults, missing material dependencies, or a task that no longer runs. Component validation and assembly/runtime acceptance are separate gates.

If the Foundation does not yet contain an accepted workcell or factory profile covering the desired use case, the correct path is:

1. select existing profiles for the component claims they genuinely cover;
2. define a clearly named **project-local candidate profile** for missing workcell capabilities;
3. document its data mapping, gaps, requirements, validators, and runtime tests;
4. avoid calling that candidate an official SimReady standard until it passes the relevant acceptance and standardization process.

### Required publication evidence

A SimReady-aware package publication should add evidence such as:

```text
data/
  package_contract.json
  source_manifest.json
  mapping_report.json
  capability_claims.json          # profile IDs + exact versions + applicability
  validation/
    <profile>-<version>.json       # machine-readable validator output
    runtime_acceptance.json
    validation_environment.json   # validator/tool/runtime versions
```

Validation metadata stamped into a USD layer can improve discoverability, but it must not replace the external report and reproducibility record. The claim needs an asset hash/version, profile version, feature/requirement resolution, validator version, execution environment, result, and date.

### Deferred integration with Asset Structure 3.0 and USD GoodStart

The final integration should be designed in a follow-up synthesis rather than assumed from folder names. The main open questions are:

| Integration question | Why it matters |
|----------------------|----------------|
| Which public entry point is validated? | Profile claims must attach to the stable interface consumers actually reference, not an arbitrary internal payload. |
| Does each variant require its own profile claim? | A neutral, PhysX, MuJoCo, controller, or end-effector configuration may satisfy different features and requirements. |
| Are unloaded payloads validated structurally and loaded payloads behaviorally? | Selective loading must not hide invalid dependencies or unsupported feature branches. |
| How are child-profile claims aggregated at workcell/factory level? | Passing components do not prove correct assembly, topology, or runtime task behavior. |
| Where are validation reports and stamps published? | Evidence must survive package versioning without turning mutable validation results into asset source truth. |
| Which checks belong to asset packages versus scene/project layers? | Asset-local capabilities and project-level scenario/runtime acceptance have different owners and release cycles. |
| How are official and project-local profiles distinguished? | Experimental capability work must not be misrepresented as an accepted NVIDIA or industry standard. |

The provisional responsibility split is therefore:

```text
Asset Structure 3.0  -> package and composition architecture
SimReady Foundation  -> capability semantics, specification maturity, and executable evidence
USD GoodStart        -> project/scene ownership and peer opinion strength
Dataprep pipeline    -> deterministic transformation that satisfies all selected contracts
```

This section intentionally stops at that boundary. A later combined design should map profiles and validation gates onto each 3.0 package/variant and then map assembly/runtime acceptance onto the relevant USD GoodStart project layers without duplicating ownership.

---

## 18. NVIDIA DSX Blueprint — Evidence-Based Conclusions and GoodStart Corrections

The [NVIDIA Omniverse DSX Blueprint](https://docs.omniverse.nvidia.com/dsx/latest/index.html), its [SimReady asset journey](https://docs.omniverse.nvidia.com/dsx/latest/simready-assets.html), the public [AI Factory pipeline samples](https://nvidia-omniverse.github.io/aif-pipeline-samples/index.html), and the [Generic CDU reference asset](https://github.com/NVIDIA-Omniverse/aif-pipeline-samples/blob/main/assets/Generic_CDU/Generic_CDU.usda) add concrete digital-twin evidence to the comparisons in this paper. They strengthen the proposed separation between scene ownership, reusable asset publication, configurable simulation content, and runtime systems. They also require several corrections to earlier GoodStart wording.

### Evidence boundary

DSX is an NVIDIA blueprint and reference workflow for AI Factory digital twins. NVIDIA describes it as a starting point that developers are expected to customize, not a turn-key production application or a universal OpenUSD standard. The evidence below is therefore classified deliberately:

- **OpenUSD mechanics:** normative composition behavior such as sublayer and LIVERPS strength ordering.
- **Published DSX pattern:** the documented asset delivery tree and the observable Generic CDU reference implementation.
- **Proposed GoodStart policy:** the scene-level ownership order and the extensions derived for broader industrial digital twins.

DSX validates the asset-package side of the proposed architecture. It does **not** prescribe the full GoodStart order `OPIN → CAM → ENV → RUNTIME → SIM → DATA → ACTGR → ANIM → VAR → MTL → PHY → ASS`, nor does it establish that every project needs all of those lanes.

### Observed DSX asset composition

The DSX delivery guidance publishes one model as an atomic package:

```text
<model_name>/
  <model_name>.usd                       # public asset interface
  layers/
    <model_name>_Properties.usda         # intrinsic AIF metadata
    <model_name>_ConnectionPoints.usd    # reusable physical ports
  payloads/
    internal.usd                         # internal geometry
    external.usd                         # external geometry
  data/
    <model_name>.json                    # Scene Optimizer preset
```

The public Generic CDU sample makes the asset-internal strength order inspectable:

```usda
subLayers = [
    @./layers/Generic_CDU_Properties.usda@,
    @./layers/Generic_CDU_ConnectionPoints.usd@
]
```

For that sample, the interface layer's direct local opinions are strongest, the properties layer is the first and strongest sublayer, and the connection-points layer is the next sublayer. The interface authors external and internal payload arcs; external geometry is available by default, while the internal prim is authored inactive in the published sample. Because local layer-stack opinions are stronger than payload opinions under LIVERPS, the asset-local semantic layers can non-destructively enrich the payloaded geometry at matching composed paths.

This is useful evidence, not a universal mandate that every asset must order properties above connection points. Those contributions should normally own disjoint fields. If they can collide, the package contract must state the intended order and validators must test it.

#### DSX composition diagram

```mermaid
flowchart TB
    SceneRoot["Project / digital-twin scene root"]
    ASS["ASS_LYR.usda<br/>scene-level asset assembly"]

    subgraph DSXPackage["DSX-style SimReady equipment package"]
        direction TB
        Interface["model_name.usd<br/>public asset interface"]

        subgraph SemanticLayers["Asset-local semantic layers"]
            direction LR
            Properties["model_name_Properties.usda<br/>sublayer 1 · strongest sublayer<br/>intrinsic product properties"]
            Connections["model_name_ConnectionPoints.usd<br/>sublayer 2<br/>reusable facility ports"]
        end

        subgraph GeometryPayloads["Selective geometry payloads"]
            direction LR
            External["external.usd<br/>external shell<br/>available by default"]
            Internal["internal.usd<br/>internal detail<br/>inactive in reference sample"]
        end

        Preset["data/model_name.json<br/>Scene Optimizer preset<br/>pipeline input · not a USD arc"]
        GeometryBuild["CAD conversion +<br/>geometry optimization"]
        Validation["Geometry + asset validation<br/>published package evidence"]

        Interface -->|subLayers #1| Properties
        Interface -->|subLayers #2| Connections
        Interface -->|payload| External
        Interface -->|payload / opt-in| Internal
        Preset -->|drives geometry optimization| GeometryBuild
        GeometryBuild -->|produces payload| External
        GeometryBuild -->|produces payload| Internal
        Properties --> Validation
        Connections --> Validation
        External --> Validation
        Internal --> Validation
    end

    SceneRoot -->|subLayers| ASS
    ASS -->|GoodStart policy: references public interface| Interface

    classDef scene fill:#dceeff,stroke:#2167ae,color:#10243a,stroke-width:2px
    classDef interface fill:#ffcc80,stroke:#e65100,color:#3b2305,stroke-width:3px
    classDef semantic fill:#e9ddf7,stroke:#7048b6,color:#25133f,stroke-width:2px
    classDef payload fill:#e8f5e9,stroke:#2e7d32,color:#17351d,stroke-width:2px
    classDef pipeline fill:#fff3e0,stroke:#ef6c00,color:#3b2305,stroke-width:2px
    class SceneRoot,ASS scene
    class Interface interface
    class Properties,Connections semantic
    class External,Internal payload
    class Preset,GeometryBuild,Validation pipeline
    style DSXPackage fill:#f8fafc,stroke:#52697d,stroke-width:2px
    style SemanticLayers fill:#f5f0fb,stroke:#7048b6,stroke-width:1px
    style GeometryPayloads fill:#f1f8f3,stroke:#2e7d32,stroke-width:1px
```

**Figure 18.1 — DSX-style equipment asset composition.** Under the corrected GoodStart policy, the model interface is the intended scene reference target; DSX documents it as the main asset interface file. Product properties and physical connection points remain asset-local sublayers; external and internal geometry remain selectively loadable payloads. The optimizer preset participates in the production pipeline but is not itself composed into the USD stage. Compare this with the configurable robot graph in [Figure 16.1](#composition-overview).

### Breakout — DSX equipment assets versus Isaac Sim Asset Structure 3.0

The DSX and [Isaac Sim Asset Structure 3.0](https://docs.isaacsim.omniverse.nvidia.com/6.0.1/robot_setup/asset_structure.html) patterns use the same OpenUSD building blocks but optimize different reusable-asset problems. DSX starts from facility equipment that must become placeable, queryable, selectively visible, and connectable to electrical, cooling, and airflow systems. Isaac Sim starts from articulated robots that must preserve shared structure while switching physics backends and adding optional control, ROS, sensor, or end-effector features.

| Comparison dimension | NVIDIA DSX / AI Factory equipment pattern | NVIDIA Isaac Sim Asset Structure 3.0 | Why the difference matters |
|----------------------|-------------------------------------------|--------------------------------------|----------------------------|
| Primary asset class | Racks, coolant distribution units, chillers, building shells, and other facility equipment | Robot bodies, manipulators, mobile robots, hands, grippers, and articulated systems | The package boundary should follow the product and its consumers, not one universal folder taxonomy. |
| Central design question | How does CAD-derived equipment become a validated SimReady asset with product semantics and facility interfaces? | How does one robot identity support shared geometry plus selectable physics and behavior stacks? | DSX emphasizes enrichment and facility integration; Isaac emphasizes controlled simulation configuration. |
| Stable downstream entry point | `<model_name>.usd` | `asset.usd` final composed interface; published filenames may be product-specific | Both protect consumers from private file reorganization. |
| Shared structural content | Main assembly with external/internal geometry payloads | `base.usda`, `instances.usda`, `geometries.usd`, `materials.usda`, and `robot.usda` | Isaac exposes more robot-internal workstream boundaries because articulation and reusable mesh/physics structure demand them. |
| Semantic contribution | `<model>_Properties.usda` with `aif:core:*` and `aif:spec:*` properties | Dedicated `robot.usda` Robot Schema layer plus robot-level metadata and relationships | Both isolate semantics from geometry, but their schemas answer different domain questions. |
| Physical interfaces | Explicit connection-point geometry for power, cooling, and airflow, authored with `guide` purpose | Robot links, joints, named poses, attachment frames, and end-effector composition | Facility ports and articulation interfaces need different schemas and validation even when they meet in one workcell. |
| Heavy-content strategy | Split external and internal equipment geometry into payloads | Reuse geometry through references; add feature and backend content through payloads | DSX primarily controls equipment detail; Isaac controls both data weight and optional simulation capability. |
| Configuration strategy | The published example focuses on load choice and separately authored enrichment; it does not require a broad variant matrix | Variants select physics backends or feature configurations without duplicating the robot identity | Do not introduce variants merely for symmetry. Use them when consumers need a finite supported choice. |
| Physics strategy | Simulation metadata and connection contracts support external thermal, electrical, airflow, and related services | Neutral physics foundation plus backend-specific PhysX, MuJoCo, or other layers | Backend isolation prevents incompatible solver opinions from contaminating shared robot data. |
| Optional features | Internal detail and domain-specific metadata or connections as required by the equipment class | Controllers, ROS graphs, sensors, end effectors, and other add-on feature stacks | Isaac's feature graph is intentionally more configurable because robot capabilities change by task and runtime. |
| Source-update rule | Normalize and optimize CAD, preserving enough hierarchy and breadcrumb data for deterministic regeneration | Keep source assets unchanged; transform structure and add simulation features downstream | Both protect re-import, but Isaac states the source/transform/feature separation especially explicitly. |
| Validation center | Geometry quality, units, hierarchy, materials, intrinsic properties, connection points, atomic delivery | Structure, robot schema, articulation, joints, backend physics, feature selections, and runtime behavior | Passing one pattern's checks does not prove conformance to the other pattern's use case. |
| Best-fit benefit | Consistent equipment publication, selective internal detail, facility connectivity, metadata-driven engineering workflows | Reusable multiphysics robots, isolated tuning, controlled feature selection, maintainable controller and end-effector integration | Each pattern minimizes the complexity that is dominant for its asset class. |

Neither pattern replaces the other. A robot installed in an AI Factory can remain an Isaac-style configurable robot product while the enclosing cell, facility equipment, and utility interfaces follow DSX-style publication. The workcell or facility assembly references each public interface and owns the connections between them. It should not flatten the robot's backend variants into facility layers or copy DSX equipment properties into the robot's private physics files.

The combined recursive model is:

```text
GoodStart scene ownership (B)
  -> facility / workcell assembly
       -> DSX-style equipment packages (C)
       -> Isaac-style configurable robot packages (C + D)
       -> scene-owned topology between public ports and attachment interfaces
       -> SimReady profile validation per package and per assembled use case
```

The benefit of maintaining both approaches is controlled specialization. Their public-interface rule remains shared, so the scene can compose them uniformly. Their private layers remain domain-specific, so equipment metadata does not dictate robot physics architecture and robot feature variants do not inflate every passive facility asset.

### Corrections to the proposed USD GoodStart interpretation

| Earlier or ambiguous wording | Corrected conclusion |
|------------------------------|----------------------|
| Assets at the bottom are “universal.” | A weak scene-level asset assembly with intentional refinements above it is common in the compared pipelines, but it remains a domain policy. OpenUSD defines strength mechanics, not one universal semantic order. |
| `DATA_LYRs` and an asset `Properties.usda` can both own stable product metadata. | Intrinsic reusable product facts belong in the asset package. `DATA_LYRs` owns project- or instance-scoped mappings, identifiers, relationships, and context. Duplicate independent authorship is prohibited by default. |
| Connection points may be asset layers, payloads, or scene-level data without a sharper distinction. | The published DSX pattern uses an asset-local connection-point sublayer. A scene topology layer may connect placed instances through their public ports, but should not duplicate port geometry or intrinsic port metadata. Payloading connection points would be a separate, justified GoodStart design. |
| The wrapper can sit beside a separate dependency directory. | Keep the public interface, layers, payloads, and data together in one atomic asset folder with anchored relative dependencies. |
| DSX validates the exact `DATA_LYRs` and `RUNTIME_LYR` positions. | DSX separates validated assets from simulations, operational data, scene state, and runtime services at the system level. The exact GoodStart scene-layer positions remain a proposed ownership policy that must be tested per use case. |

### Breakout — Why this architecture matters for digital twins, robotics, and Omniverse

Classic visual-effects production and operational digital twins both benefit from OpenUSD, but their dominant composition problems differ.

| Dimension | Classic VFX shot pipeline | Digital twin / robotics / Omniverse application |
|-----------|---------------------------|-------------------------------------------------|
| Primary lifecycle | Bounded shot or sequence refined toward rendered deliverables | Long-lived system evolving from design through commissioning and operation |
| Dominant ordering question | Which downstream department refines or overrides the shot? | Which system owns asset truth, simulation setup, configuration, project context, and live state? |
| Asset boundary | Published characters, props, sets, and materials consumed by shots | Recursive facilities, lines, cells, machines, robots, sensors, and connection interfaces |
| Configuration | Often shot- or asset-specific artistic variants | Supported physics backends, controllers, end effectors, sensors, operating modes, and fidelity levels |
| Loading | Shot working set and render needs | Selective loading of facilities, internal equipment, collision, sensor, or solver-specific content |
| External systems | Production tracking, caches, render farm, editorial | CAD/BIM/PLM, ERP/AAS, control systems, telemetry, solvers, data lakes, agents, and runtime APIs |
| Acceptance evidence | Image, cache, shot, and render validation | Package validation plus configuration-, assembly-, simulation-, and runtime-acceptance evidence |

A departmental shot stack—Paradigm **A**—is optimized for ordered refinement of a bounded production unit. Digital twins usually need Paradigm **B** at the scene boundary, Paradigm **C** at every reusable asset boundary, and Paradigm **D** wherever a stable asset identity exposes controlled simulation configurations. Robotics makes this especially visible: one robot identity may need neutral structure, selectable PhysX or MuJoCo data, optional controllers and ROS graphs, swappable end effectors, sensors, collision representations, and deferred high-detail geometry without changing the downstream reference target.

OpenUSD can integrate these concerns because it supplies several orthogonal mechanisms in one composed stage:

1. **Ordered sublayers** express explicit peer ownership and non-destructive refinement.
2. **References** preserve reusable asset identity while remapping assets into assembly namespaces.
3. **Payloads** defer heavy or optional content without changing the public asset entry point.
4. **Variant sets** expose supported configurations without turning each configuration into a different asset identity.
5. **Schemas, relationships, and collections** make simulation semantics, interfaces, and alternate views queryable.
6. **Session and project layers** allow contextual or live opinions without rewriting the published asset source.

Common interchange files such as OBJ, FBX, STEP, or a flattened scene export can carry valuable geometry, hierarchy, materials, and sometimes metadata. A single classic file does not, by itself, provide OpenUSD's distributed opinion composition, explicit strength ordering, stable cross-file asset interface, selective payload loading, or composed variant model. A pipeline can reproduce parts of those behaviors with databases, sidecars, naming rules, custom merge code, and generated exports, but then the external pipeline is effectively rebuilding a composition system around the files. The precise conclusion is therefore not that other formats can never participate in a digital twin; it is that a flattened interchange file alone cannot preserve the live, modular composition contract required by this architecture.

For Omniverse, this distinction is operational rather than academic. DSX combines validated SimReady OpenUSD assets with Kit applications, USD storage, simulation services, a simulation data delegate, a data lake, streaming, and AI-agent interaction. The asset packages provide stable authored interfaces; the runtime systems provide changing simulation and operational context. If those responsibilities are flattened into one mutable file or one undifferentiated strongest layer, asset updates can overwrite operational edits, runtime values can contaminate reusable product truth, and configuration or loading choices become difficult to reproduce.

### Resulting GoodStart policy

The proposed USD GoodStart layer order remains useful as a **scene-level ownership policy**, subject to these corrected rules:

1. Keep the project root thin and treat its ordered sublayers as contracted ownership lanes, not as a universal taxonomy or version history.
2. Let `ASS_LYR.usda` reference the public interface of an atomic asset package; do not reach into private layers or payloads.
3. Keep intrinsic product properties and reusable connection points inside the asset package.
4. Use `DATA_LYRs.usda` for project- and instance-scoped identifiers, mappings, context, and cross-asset relationships—not as a second owner of intrinsic product truth.
5. Use `PHY_LYR` or a declared topology layer for scene-owned connections between placed public ports when that concern is not owned by a simulation package.
6. Keep transient operational values and explicit runtime snapshots in `RUNTIME_LYR.usda` or an equivalent session/runtime mechanism, separate from stable asset and project facts.
7. Keep solver outputs in `SIM_LYR.usda` only when an authored USD result is required; high-volume or transient results may remain in external stores and be connected through runtime services.
8. Declare write targets, collision policy, payload defaults, variant semantics, source mapping, and validation evidence in machine-readable package and scene contracts.
9. Keep the modular authoring package as source of truth. If a target runtime needs fewer files or less resolver fan-out, generate a fingerprinted deployment package and benchmark it separately rather than flattening or hand-editing the maintained authoring graph.

The corrected default asset-package profile is:

```text
010_ASS_USD/
  USD_Startpoint/
    <source_or_normalized_startpoint>.usd
  USD_Wrappers/
    <asset_id>/
      <asset_id>.usd
      layers/
        <asset_id>_Properties.usda
        <asset_id>_ConnectionPoints.usd
      payloads/
        external.usd
        internal.usd
      data/
        <asset_id>.json
        source_manifest.json
        mapping_profile.json
        package_contract.json
```

Small or purely visual assets may use a reduced profile when selective loading, connection points, or separate metadata workstreams provide no benefit. The contract should explain omitted capabilities rather than generating empty layers merely to match a folder diagram.

### Final conclusion

The strongest evidence-based conclusion is a hybrid: **B + C + D** for digital twins and robotics, rather than one ever-growing scene sublayer stack. GoodStart can govern project-level ownership and opinion strength; DSX-style asset packages can provide stable reusable equipment interfaces; Isaac-style configurable products can expose physics and behavior choices; SimReady can define and verify the required capabilities; and Omniverse runtime services can manage simulation and operational data without turning live state into asset source truth.

This differs from the dominant classic VFX pattern **A + C**, where departmental shot refinement is usually the central ordering problem. Both use the same OpenUSD composition mechanics. The architectural difference comes from lifecycle, ownership, configuration, selective loading, external-system integration, and acceptance requirements—not from a different version of USD.

---

## 19. NVIDIA VFI — Factory-Scale Authoring, Composition, and Deployment Structure

### Abstract and evidence boundary

**Reader problem.** A factory program can adopt stable asset interfaces, payloads, instancing, and explicit workstream layers and still perform poorly when thousands of authored layers must be resolved across remote storage. The reverse failure also occurs: a team can collapse the dataset into a compact file set that loads quickly but is difficult to update, validate, or regenerate because authoring ownership and asset boundaries have disappeared.

**Intended outcome.** This section separates four related structures: engineering source structure, modular OpenUSD authoring structure, the composed operational stage, and generated deployment packaging. It shows how NVIDIA's Virtual Facility Integration guidance changes the proposed GoodStart policy without turning VFI into another fixed sublayer order.

**Sources used.** The primary product-scoped sources are the [VFI Guide overview](https://docs.omniverse.nvidia.com/vfi/latest/index.html), [Content Iteration Cycle](https://docs.omniverse.nvidia.com/vfi/latest/guide/content-iteration-cycle.html), [Factory-Level USD Structuring](https://docs.omniverse.nvidia.com/vfi/latest/guide/factory-level-structuring.html), [VFI Asset Structure Examples](https://docs.omniverse.nvidia.com/vfi/latest/guide/usd-structure-example.html), and [Asset Structure Performance Optimizations and Tradeoffs](https://docs.omniverse.nvidia.com/vfi/latest/guide/asset-structure-optimizations-and-tradeoffs.html). Supporting implementation evidence comes from the pinned [VFI script-samples revision](https://github.com/NVIDIA-Omniverse/vfi-samples/tree/2b11331c63694be791320cfee8b4b76aaace9473), the pinned [AI Factory pipeline-samples revision](https://github.com/NVIDIA-Omniverse/aif-pipeline-samples/tree/41038967ef0a2459b128a225161f8d59beb3b424), and the [Data Aggregation and Navigation project-assembly guide](https://docs.omniverse.nvidia.com/dang/latest/guide/assembly.html). These sources were reviewed on 8 August 2026; the inspected VFI pages report an update date of 6 August 2026.

**Treatment.** The NVIDIA documentation and repositories are external, public, official ecosystem sources. They are referenced and paraphrased rather than imported. VFI behavior remains NVIDIA/Omniverse product guidance, not normative OpenUSD Core behavior. The VFI sample repository is covered by the NVIDIA Omniverse license at the inspected revision, so this paper does not reproduce its implementation. The AIF pipeline-samples repository remains pinned and licensed separately. In the derived OpenUSD-GoodStart publication, Chapter 5 owns the architectural decision; Chapters 6, 9, and 20 should receive focused cross-links for interfaces, publication, packaging, and automation.

**What is preserved and generalized.** This section preserves VFI's lifecycle, structuring stages, asset-boundary criteria, instancing constraints, authoring/deployment distinction, and directional performance evidence. Product UI steps, Kit-version defects, converter switches, screenshots, NVIDIA sample content, and commands are excluded because they do not define a general layer-order rule.

### VFI does not add a fifth composition paradigm

VFI reinforces Paradigms **B** and **C** and can participate in **D** when a facility asset exposes controlled alternatives or optional content. Its principal new contribution is not a new strength order. It is the explicit separation between the structure that teams maintain and the structure that a target deployment consumes.

| Structure | Primary question | Typical contents | Authority and lifecycle |
|-----------|------------------|------------------|-------------------------|
| Engineering source structure | What did CAD, BIM, PLM, DCC, scanning, or simulation author? | Native assemblies, product structure, supplier hierarchy, source identifiers | Owned upstream; preserve provenance and mapping evidence |
| Modular OpenUSD authoring structure | What must be independently updated, reused, loaded, validated, or owned? | Public interfaces, payloads, component and subcomponent assets, material libraries, animation clips, domain layers | Maintained publication source of truth |
| Composed operational stage | What facility, line, cell, machine, robot, and context must the consumer see? | Referenced assets, placement, topology, project selections, scenario layers, runtime or session opinions | Composed result for a task; not necessarily a single stored file |
| Generated deployment package | What file fan-out and representation meet the target runtime envelope? | Consolidated component libraries, subcomponent libraries, binary heavy data, optional sharding, deployment manifests | Reproducible build artifact; never an independent authoring truth |

This distinction corrects a common interpretation of the proposed GoodStart folder tree. A directory or layer lane can be the correct ownership boundary without being the ideal network or runtime package. Conversely, a fast eight-layer deployment artifact does not prove that eight authored files are sufficient for lifecycle management.

### VFI content cycle and the authoring-to-deployment diamond

The VFI guide presents conversion, validation, optimization, and structure/assembly as an iteration cycle. Its factory-level guidance then expands a monolithic export into reusable assets, interfaces, payloads, subcomponents, libraries, animation, and domain layers. Finally, its performance guidance permits a deployment build to consolidate selected modules into fewer library files. The resulting topology is a diamond: narrow source intake, wider modular authoring, and narrower measured deployment packaging.

```mermaid
flowchart LR
    Source["CAD, BIM, DCC, scan, and simulation sources"] --> Convert["Extract and convert"]
    Convert --> Validate["Validate units, geometry, hierarchy, identity, and quality"]
    Validate --> Structure["Structure modular authoring graph"]

    subgraph Authoring["Maintained authoring source of truth"]
        direction TB
        Interface["Stable public interfaces"]
        Components["Components and subcomponents"]
        Payloads["Payload and load boundaries"]
        Instancing["Instancing at valid opinion boundaries"]
        Libraries["Shared material and resource libraries"]
        Domains["Physics, sensors, semantics, and other domain layers"]
        Motion["Animation clips and material-flow representations"]
    end

    Structure --> Interface
    Structure --> Components
    Structure --> Payloads
    Structure --> Instancing
    Structure --> Libraries
    Structure --> Domains
    Structure --> Motion

    Interface --> Package["Generate deployment package"]
    Components --> Package
    Payloads --> Package
    Instancing --> Package
    Libraries --> Package
    Domains --> Package
    Motion --> Package

    Package --> Measure["Measure cold load, warm load, memory, interaction, and resolver fan-out"]
    Measure -->|"targets fail"| Package
    Measure -->|"targets pass"| Runtime["Publish fingerprinted runtime artifact"]
```

**Figure 19.1 - VFI authoring-to-deployment diamond.** The arrows do not imply that every project needs every authoring contribution or one mandatory packaging strategy. They show responsibility flow: source evidence enters a validated modular graph; a reproducible packaging step derives a runtime artifact; measurements decide whether that artifact is fit for its target environment. The deployment result does not replace the maintained graph.

### Seven VFI structuring steps and their GoodStart implications

| VFI step | Source-grounded intent | GoodStart interpretation |
|----------|------------------------|--------------------------|
| 1. Separate animation | Keep time-varying animation outside geometry and bind it through layers or value clips | Keep asset geometry replaceable; place scenario animation at the narrowest stable boundary that owns it |
| 2. Identify asset boundaries | Align assets with lifecycle, ownership, reuse, validation, optimization, instancing, and selective-loading needs | Do not mirror a source hierarchy blindly; record why each component or assembly is a publication unit |
| 3. Add interface/payload separation when useful | Keep public fields available while heavy implementation is unloaded | Reference the public interface from `ASS_LYR`; do not require every small asset to manufacture an empty payload split |
| 4. Enable instancing | Align instance boundaries with where opinions and animation must be authored | Do not instance an entire articulated robot when independent joint state is required; instance reusable rigid links or subcomponents instead |
| 5. Organize materials as libraries | Reference and reuse canonical material definitions instead of duplicating them per mesh | Treat material libraries as governed reusable assets with explicit renderer and portability boundaries |
| 6. Layer domain-specific data | Add physics, sensors, semantics, or material specialization against stable paths without modifying source assets | Keep reusable asset-domain facts asset-local; keep project relationships and instance context in the consuming scene |
| 7. Model object handling deliberately | Use Point Instancers and time-sampled data for large repeated populations instead of dynamic reparenting or duplicated prims | Separate high-volume material-flow representation from equipment identity; use richer referenced prims only when individual identity or overrides justify their cost |

The steps form a decision sequence, not a mandatory folder checklist. Optionality is explicit: interface/payload separation is most useful when stable unloaded state and selective loading matter, and deployment consolidation is justified only by the measured target environment.

### Instancing follows opinion granularity

VFI makes a constraint especially visible for robotics and factory scenes: instanceability and authoring freedom are coupled. Descendants of an OpenUSD instance proxy cannot receive arbitrary per-instance opinions. A whole articulated robot therefore cannot be treated as one immutable shared instance when its links, joints, annotations, visibility, or task state must differ independently. Reusable rigid geometry can be instanced at link or subcomponent boundaries, while each robot retains the unique articulation structure required for control and simulation.

This reinforces the Isaac Sim comparison rather than contradicting it. Isaac Asset Structure 3.0 governs configurable robot packages; VFI governs how many such products and facility assets can be aggregated and optimized at factory scale. The shared rule is to design stable composition boundaries before enabling instancing. Retrofitting instanceability after downstream paths and overrides have proliferated is a restructuring project, not a metadata toggle.

### Breakout — Authoring structure is not deployment structure

| Dimension | Proposed GoodStart scene lanes | VFI modular authoring | VFI runtime package | Isaac Asset Structure 3.0 |
|-----------|--------------------------------|-----------------------|---------------------|---------------------------|
| Central question | Who owns each scene-level opinion? | What is independently reusable, updated, validated, optimized, or loaded? | What representation meets deployment latency and memory targets? | Which robot structure, backend, and optional features are selected? |
| Primary scale | Project or digital-twin scene | Components, equipment, workcells, lines, and factory assemblies | Facility runtime or distribution target | Configurable robot product |
| Main mechanisms | Ordered sublayers and public asset references | Interfaces, references, payloads, material libraries, domain layers, clips, and instancing | Consolidated component/subcomponent libraries, binary heavy layers, optional sharding | References, payloads, variants, and feature stacks |
| Unit of change | Contracted ownership lane | Asset, aggregate, library, or domain contribution | Generated deployment artifact | Robot feature or supported configuration |
| Instancing concern | Scene placement and repeated products | Match instance boundaries to opinion and animation granularity | Preserve prototype sharing while reducing file fan-out | Reuse rigid structure without freezing required articulation differences |
| Validation center | Write targets, collision policy, layer strength, and scene behavior | Structure, identity, stable paths, source mapping, asset quality, and unloaded behavior | Cold/warm load, memory, resolver calls, layer count, and interaction targets | Articulation, backend, controller, feature selection, and runtime behavior |
| Source of truth | Authored project profile | Yes - maintained modular package | No - reproducibly generated | Published robot interface and package |

The benefit of keeping these structures separate is reversible optimization. Teams can change a deployment package when infrastructure or working-set needs change without rewriting the semantic ownership model. They can also improve authoring boundaries without forcing every consumer to adopt private source paths, because the public interface and build contract remain stable.

### Directional VFI performance evidence

The VFI performance page reports an anonymized factory case with approximately 500,000 prims and compares several packaging strategies. The reported results are directional, environment-sensitive observations rather than a portable benchmark:

| Inspected strategy | Cold load | Warm load | Process memory | Layer count |
|--------------------|-----------|-----------|----------------|-------------|
| Monolithic baseline | About 2.1 minutes | About 56 seconds | About 15 GB | 3,664 |
| Highly disaggregated structure | About 4 minutes | About 1.6 minutes | About 11.6 GB | 11,488 |
| Component and subcomponent library packaging | About 53 seconds | About 15 seconds | About 6.6 GB | 8 |

The correct conclusion is not that eight layers are universally optimal. The case demonstrates that fine-grained lifecycle structure and runtime layer fan-out can pull in opposite directions, especially across remote or cloud storage. The applicable requirement is to benchmark cold and warm paths separately and record the resolver, cache, network, storage, hardware, payload-load policy, prim count, and working set used for the test.

Layer count is therefore an operational metric, not an architectural score. A monolith can be slow, a disaggregated graph can be slower, and a generated package can be faster while preserving the logical scene. The deployment decision must be evidence-led.

### Omniverse Blueprints and Workflows source map

The [NVIDIA Omniverse documentation overview](https://docs.nvidia.com/omniverse/index.html#nvidiatab-blueprints-workflows) is useful as a maintained discovery hub. It is not, by itself, evidence for one layer order. Each linked blueprint or workflow owns a different system boundary and must be evaluated through its specific documentation or repository.

| Discovered source | Relevance to this paper | Treatment |
|-------------------|-------------------------|-----------|
| [Virtual Facility Integration Guide](https://docs.omniverse.nvidia.com/vfi/latest/index.html) | Factory-scale asset boundaries, recursive aggregation, instancing, domain layering, and packaging | Core Section 19 evidence within NVIDIA's product boundary |
| [AI Factory Digital Twin Pipeline Samples](https://nvidia-omniverse.github.io/aif-pipeline-samples/) | Executable CAD conversion, optimization, validation, properties, connection points, and delivery evidence | Supporting implementation evidence; already used by Section 18; pin revision |
| [DSX Blueprint](https://docs.omniverse.nvidia.com/dsx/latest/index.html) | AI Factory equipment packages and system responsibility boundaries | Core Section 18 evidence; do not duplicate here |
| [Data Aggregation and Navigation Guide](https://docs.omniverse.nvidia.com/dang/latest/guide/assembly.html) | Source-preserving wrappers, references/payloads, project assembly, and collaborative edit layers | Supporting scene-assembly evidence for Paradigms B and C |
| [Omniverse Reference Architectures](https://docs.omniverse.nvidia.com/arch-diagrams/latest/index.html) | High-level system integration context | Discovery and system-context source; insufficient alone for layer-strength claims |
| [Digital Twin for Interactive Fluid Simulation](https://github.com/NVIDIA-Omniverse-blueprints/digital-twins-for-fluid-simulation) | Separation of authored visualization state, simulation/inference services, caches, and deployment profiles | Supporting runtime-boundary evidence for future research; not a layer-order authority |
| Synthetic-data, motion-generation, streaming, CAE, and web-viewer workflows | Downstream consumers and deployment examples | Follow only when a claim affects an identified composition, asset-interface, or runtime boundary |

This source map prevents catalog inflation. A link appearing under NVIDIA Blueprints or Workflows proves discoverability and product ownership, not that its architecture should be copied into the GoodStart root stack.

### Corrections to the proposed GoodStart profile

VFI produces the following concrete corrections and additions:

1. The proposed GoodStart layer order remains a **scene-level authoring and ownership profile**, not a runtime packaging prescription.
2. `ASS_LYR.usda` should reference stable public asset or aggregate interfaces. Deployment packaging may redirect or resolve those interfaces through a governed build, but consumers must not depend on private authoring files.
3. Asset boundaries should be justified by lifecycle, ownership, update cadence, source identity, validation scope, reuse, instancing, and selective-loading needs.
4. The authoring graph may intentionally expand into many component and subcomponent layers. The deployment graph may intentionally consolidate them, provided composed behavior, public interfaces, identity, and instancing are preserved and verified.
5. A derived representation created by merging, decimating, clustering, or deactivating source content is regenerable output. Its manifest must point back to the source package and transformation profile.
6. Animation, scenario clips, point-instanced material flow, and solver/runtime streams require explicit ownership. They should not be baked into reusable equipment geometry merely to reduce file count.
7. Instancing policy must be decided before publication and tested against expected per-instance opinions. `instanceable = true` is not a late-stage universal optimization.
8. Binary formats are appropriate for heavy geometry or array data; readable sparse interfaces and contracts may remain ASCII. File format choice does not replace the composition contract.
9. Every deployment profile must record the environment and evidence that justified its packaging choices. A package that is fast on a local warm cache is not automatically fit for a remote cold start.
10. The modular authoring package remains authoritative. Deployment artifacts are never hand-edited and never become a second independent source of product truth.

The machine-readable package or scene contract should add these fields:

| Contract field | Required meaning |
|----------------|------------------|
| `authoring_profile` | Versioned modular structure and ownership policy used as source of truth |
| `deployment_profile` | Named packaging strategy, target environment, payload defaults, and sharding or consolidation rules |
| `source_fingerprint` | Hash or immutable identifier of the accepted authoring package |
| `transform_profile` | Versioned conversion, restructuring, optimization, and packaging recipe |
| `interface_map` | Public entry points and any permitted mapping into packaged libraries |
| `identity_map` | Source, publication, and domain identifiers preserved through packaging |
| `benchmark_context` | Resolver, cache state, storage, network, hardware, working set, and load policy |
| `acceptance_evidence` | Cold/warm load, memory, layer fan-out, composition, instancing, and behavioral validation results |
| `regeneration_rule` | Trigger and procedure for rebuilding after source, schema, profile, or dependency change |

These are proposed GoodStart contract fields, not NVIDIA or OpenUSD schema requirements. A project may use different names, but it must carry equivalent evidence if it claims reproducible authoring-to-deployment transformation.

### Resulting integrated architecture

The paper's earlier **B + C + D** conclusion remains valid and becomes more precise:

```text
GoodStart scene ownership (B)
  -> recursively composed public assets and aggregates (C)
       -> DSX-style equipment packages where appropriate (C)
       -> Isaac-style configurable robot products where appropriate (C + D)
       -> VFI-style modular factory authoring graph (B + C, with optional D)
  -> SimReady capability and validation evidence across declared profiles
  -> governed deployment build
       -> measured packaged representation for the target runtime
  -> Omniverse applications and services consume authored and runtime contracts
```

VFI therefore changes how the architecture is delivered, not the universal rules of OpenUSD strength. GoodStart governs scene ownership; public asset interfaces protect recursive composition; DSX and Isaac provide domain-specific package patterns; SimReady governs declared capability assurance; VFI governs factory-scale structuring and the authoring-to-deployment transformation; and target-runtime measurements decide how much modularity should remain physically distributed in a published package.

### Research conclusion

The most important VFI contribution is the rejection of a false choice between maintainable modularity and runtime performance. OpenUSD allows a program to maintain explicit asset, workstream, payload, animation, material, semantic, and simulation boundaries while producing a different physical package for a specific runtime. That is possible because logical composition, authored layer files, and delivered storage units are related but not identical concepts.

Classic file pipelines can also generate optimized delivery files, but they usually require external databases, sidecars, naming rules, and custom merge logic to preserve the authoring graph and its provenance. OpenUSD keeps the public interfaces, composition arcs, prim identities, load boundaries, and opinions in a queryable model that the packaging pipeline can transform and validate. The advantage is not the number of files. It is the ability to change that number without losing the architectural contract.

---

## Revision History

| Version | Date | Notes |
|---------|------|-------|
| 1.9.0 | 2026-08-08 | Added Section 19 integrating NVIDIA Virtual Facility Integration guidance and the NVIDIA Omniverse Blueprints/Workflows source map; separated engineering source, modular authoring, composed operational, and generated deployment structures; added the VFI authoring-to-deployment diamond, seven-step transfer table, GoodStart/VFI/Isaac comparison, directional packaging-performance evidence, instancing and object-handling implications, discovery-source dispositions, new GoodStart contract fields, and the correction that modular authoring truth may be reproducibly packaged for a measured runtime without becoming a fifth composition paradigm or a flattened replacement source. Updated the Executive Summary, decision guide, ecosystem resources, canonical links, GoodStart policy, ARYS routing, tags, and synchronized version metadata. |
| 1.8.0 | 2026-07-31 | Added Section 18 with source-grounded NVIDIA DSX conclusions, the observable Generic CDU asset-internal sublayer and payload pattern, a DSX composition Mermaid diagram, a DSX-equipment-versus-Isaac-Asset-Structure-3.0 comparison breakout and table, a digital-twin/robotics/Omniverse versus classic-VFX breakout, and the resulting B+C+D hybrid conclusion; corrected the overbroad “universal” asset-base claim, separated intrinsic asset properties from scene/instance `DATA_LYRs`, separated reusable connection points from scene topology, aligned the proposed wrapper layout with an atomic DSX-style package, and clarified that DSX does not prescribe the exact GoodStart scene order or runtime/data positions. |
| 1.7.0 | 2026-07-17 | Added Section 16.1.1, “Engineering-to-twin hierarchy reconciliation,” which turns the CAD/PLM-to-digital-twin problem into a reproducible identity, mapping, package-publication, and validation contract. It distinguishes references and authored transforms for canonical placement, relationships/collections for alternate semantic views, and relocates for controlled composed-namespace edits; adds a verified correction that USD relationships are uniform rather than time-sampled; extends the Workcell pipeline, acceptance gates, references, ARYS routing, and tags accordingly. |
| 1.6.3 | 2026-07-17 | Removed the direct nAurava Technologies Workcell-DigitalTwin repository link while the asset remains under development; retained the named project context and independent technical case study, and recorded that the public repository reference may be added once the asset is finished and ready for publication |
| 1.6.2 | 2026-07-16 | Prepared the paper for external review: removed personal attribution and private-channel links from the M&E material while preserving its complete technical content as an author-created synthesis informed by internal VFX practitioner discussions; limited Unreal Engine claims to Epic's public documentation; added explicit independent-research, non-AOUSD-endorsement, and Workcell licensing/status notices |
| 1.6.1 | 2026-07-16 | Added an Executive Summary architecture map that positions the four composition paradigms by scene/project versus asset/product boundary, shows their distinct design questions, and presents NVIDIA SimReady as a cross-cutting capability-assurance axis over shared OpenUSD building blocks rather than as a fifth composition paradigm |
| 1.6.0 | 2026-07-16 | Added Section 17 treating NVIDIA SimReady Foundation as a distinct capability-contract, validation, and standardization axis; documented the requirement/capability/feature/profile hierarchy, three-phase workflow, dataprep insertion points, Workcell application, publication evidence, and deferred integration questions for Asset Structure 3.0 and the proposed USD GoodStart layer order |
| 1.5.0 | 2026-07-16 | Added Section 16.2, a Workcell-DigitalTwin conversion case study documenting the inspected mixed initial stage, a requirements-led dataprep/publication pipeline, concern-routing rules, acceptance gates, and three related delivery states: pure Asset Structure 3.0-ready product, thin ENV/MTL/ASS envelope, and the proposed USD GoodStart envelope around the same canonical package |
| 1.4.5 | 2026-07-15 | Corrected the over-simplified 1.4.4 comparison: restored the complete classic layer stack and all Isaac Sim files, arc types, variant branches, and payload semantics; reorganized only their visual grouping to produce readable, similarly sized vertical panels side by side |
| 1.4.4 | 2026-07-15 | Replaced the GitHub-unstable and visually unbalanced paradigm comparison with a balanced, flat two-panel Mermaid diagram; removed nested subgraphs and HTML label markup while retaining one minimal container-level alignment link |
| 1.4.3 | 2026-07-15 | Earlier internal-research treatment of possible future Unreal direction; superseded by the public-source-only wording in 1.6.2 |
| 1.4.2 | 2026-07-15 | Strengthened the Introduction's “Why this matters” section with precise architectural claims, an official NVIDIA Omniverse foundation reference, evidence-based Unreal Engine OpenUSD status, and an explicit caveat against presenting future major-version speculation as a confirmed roadmap |
| 1.4.1 | 2026-07-15 | Upgraded the frontmatter to ARYS 1.3 with synchronized canonical tags, Domain020 ownership, provenance, agent-native routing, maturation metadata, and a complete visible dual-header block |
| 1.4.0 | 2026-07-15 | Reorganized the opening into a brief results-focused Executive Summary, a separate research Introduction, and a Composition Foundations section for mechanics, LIV(E)RPS, and the two comparison axes |
| 1.3.9 | 2026-07-15 | Added a pre-case-study decision matrix with a scored questionnaire, validity gates, hybrid interpretation rules, and recommended starting architectures for the four composition paradigms |
| 1.3.8 | 2026-07-15 | Connected the evolution sequence at the Mermaid subgraph/container level so the versions remain vertically stacked while every individual version box preserves its horizontal left-to-right layout |
| 1.3.7 | 2026-07-15 | Restacked the five asset-structure evolution diagrams vertically, with each generation using a readable left-to-right internal layout across the available page width |
| 1.3.6 | 2026-07-15 | Added an opening research thesis framing the asset-structure history as evidence of OpenUSD's adaptable composition model, its transfer from film/VFX to robotics and digital twins, and the need for explicit interfaces, contracts, dataprep, provenance, and validation |
| 1.3.5 | 2026-07-15 | Added a compact side-by-side Mermaid comparison of all five reconstructed Isaac asset-structure generations, with simplified vertical mini-structures and a visible left-to-right evolution path |
| 1.3.4 | 2026-07-15 | Replaced context-free GoodStart shorthand in the Executive Summary and key comparisons with the linked term "proposed USD GoodStart layer order"; added a concise definition and a direct link to the repository TL;DR |
| 1.3.3 | 2026-07-15 | Added an Executive Summary reference to the recursive digital-twin implications and dataprep transformation responsibilities, with direct links to Section 16, Section 16.1, and the dataprep subsection |
| 1.3.2 | 2026-07-15 | Added the direct official Isaac Sim 6.0.1 Asset Structure page link to the prominent Asset Structure 3.0 mention in the Executive Summary |
| 1.3.1 | 2026-07-15 | Expanded the introduction to Section 16.1 with the dataprep transformation boundary: preservation of CAD/BIM source evidence, simulation-oriented restructuring, composition generation, validation, incremental regeneration, and versioned adaptable simulation-requirement profiles |
| 1.3.0 | 2026-07-15 | Added a historical breakout reconstructing importer/asset generations 1.x, 1.17, 2.0.1, and 3.0 with evidence caveats; added Section 16.1 Digital Twin Implications with a recursive factory composition model, adaptation rules, Mermaid diagram, and proposed factory package profile |
| 1.2.5 | 2026-07-15 | Forced the two vertical comparison subgraphs into a side-by-side layout with an invisible container-level Mermaid link that does not alter their internal top-to-bottom directions |
| 1.2.4 | 2026-07-15 | Restored the paradigm comparison to two vertical diagrams placed side by side; removed the cross-subgraph edge that caused Mermaid to flatten both structures horizontally |
| 1.2.3 | 2026-07-15 | Added a stylized Mermaid comparison between the classic linear scene/shot sublayer-strength stack and NVIDIA Isaac Sim Asset Structure 3.0 as a configurable asset composition graph |
| 1.2.2 | 2026-07-15 | Promoted NVIDIA Isaac Sim into the Executive Summary and added an early composition-paradigm comparison distinguishing peer sublayer strength, scene ownership lanes, published asset interfaces, and configurable simulation assets |
| 1.2.1 | 2026-07-15 | Added a Mermaid composition overview for the Isaac Sim Asset Structure 3.0 case study, including the GoodStart scene boundary, public asset interface, shared asset stack, physics variants, and optional feature stacks |
| 1.2.0 | 2026-07-14 | Added NVIDIA Isaac Sim 6.0 Asset Structure 3.0 case study with source screenshots, base and expanded feature-stack analysis, composition-arc roles, and an optional GoodStart robot/multi-physics asset-package profile |
| 1.1.9 | 2026-07-03 | Added explicit impact decision for GoodStart Minimal Layer Setup: keep default root stack stable, generate asset-package folders/contracts/reports/workflow notes, and keep per-asset metadata/connection points below public wrapper/interface assets |
| 1.1.8 | 2026-07-03 | Added NVIDIA SimReady / Physical AI addendum: asset interface rule, bounded workstream layers, reference-payload pattern, separate simulation metadata, connection points, validation artifacts, and scene-level vs asset-package ownership split |
| 1.0.0 | 2026-06-10 | Initial research document informed by internal discussions with experienced visual-effects practitioners |
| 1.0.1 | 2026-06-10 | Added OpenUSD Learning & Ecosystem Resources link collection |
| 1.1.0 | 2026-06-10 | Added Learn OpenUSD, da Vinci, Remedy, Survival Guide, ASWF reference-first, session layers; LIV(E)RPS two-axis synthesis |
| 1.1.1 | 2026-06-10 | Section 1 practitioner-synthesis Mermaid: three parallel pillars (LGT→SIM→ANIM→CAM) on shared MAT+ASS base; USD realization notes |
| 1.1.2 | 2026-06-10 | Section 1 Sketch 2 (global SIM/LGT + shots on top); padding via spacer nodes + subGraphTitleMargin |
| 1.1.3 | 2026-06-10 | Restore in-diagram subgraph titles (M&E sequence / Parallel pillars) with extra header spacing |
| 1.1.4 | 2026-06-10 | Section 1 diagrams: visible header nodes (SeqHdr/PillarHdr); PadLeft/PadRight centering; remove left-only spacers |
| 1.1.5 | 2026-06-10 | Revert Section 1 Mermaid to simple nested subgraph titles (Screenshot-2 layout); drop spacer/header-node experiments |
| 1.1.6 | 2026-06-10 | Unify full LIV(E)RPS sidebar (L→S) in all comparison Mermaid diagrams §2–§11 |
| 1.1.7 | 2026-06-26 | Update USD GoodStart to explicit `RUNTIME_LYR` split: live/session-backed telemetry and snapshots are separate from static `DATA_LYRs` metadata/identifier layers |
