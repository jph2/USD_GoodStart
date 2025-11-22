# Best Practices for OpenUSD Asset Structure

This document outlines best practices for structuring OpenUSD assets to ensure scalability, performance, and collaboration, based on NVIDIA's Learn OpenUSD curriculum and industry standards.

## 1. Core Principles

A scalable asset structure relies on four key principles:

### **Legibility**
*   **Naming:** Use clear, intent-driven names (e.g., `LargeCardboardBox` vs `Box01`).
*   **Conventions:** Differentiate public vs. internal elements (e.g., capitalized `Geometry` for public, underscored `_internal_calculations` for private).
*   **Standards:** Use ASCII/UTF-8 identifiers; avoid dynamic tokens like timestamps in persistent names.

### **Modularity**
*   **Encapsulation:** Assets should be self-contained with anchored paths for local dependencies.
*   **Interfaces:** Define stable entry points (root prims) that don't change even if internals do.
*   **Reuse:** Structure assets to be referenced and instanced easily.

### **Performance**
*   **Payloading:** Use the Reference/Payload pattern to defer loading of heavy data.
*   **Instancing:** Use Point Instancing or Scenegraph Instancing to reduce prim counts.
*   **File Formats:** Prefer `.usdc` (Crate) for efficient I/O in production, and `.usda` only for text-based debugging or simple configs.

### **Navigability**
*   **Discovery:** Use Relationships and Collections to group logical items (e.g., "lights", "physics_colliders") at the top level.
*   **Hierarchy:** Keep model hierarchies shallow and consistent.

---

## 2. The Reference/Payload Pattern

This is the standard for non-trivial assets. It separates the lightweight "interface" from the heavy "implementation".

### **Structure**
```text
Asset_File.usd (Interface)
├── Root Prim (Xform/Scope)
│   ├── Public Interface (Properties, Attributes)
│   ├── Lofted Variant Sets (Control logical variations)
│   ├── Lofted Primvars (Control material/shader inputs)
│   └── Payload Arc ───> Payload_File.usd (Content)
                            ├── Detailed Geometry
                            ├── High-Res Materials
                            └── Internal Hierarchies
```

### **Why use it?**
*   **Performance:** Consumers can load the asset without the payload (bounding box mode) to save memory and time.
*   **Workflow:** Animators can work with lightweight proxies while lighters/renderers load full geometry.

### **"Lofting"**

**What "Lofting" Means:**

"Lofting" in USD refers to moving important controls (variant sets, primvars, metadata) **above** the payload arc so they are accessible **without loading the heavy content**. The term comes from the idea of "lifting" or "elevating" these controls to a higher level in the composition hierarchy.

**Why Loft?**

When you use a payload, the heavy geometry is **lazy-loaded** (only loaded when requested). However, if variant sets, primvars, or other controls are **inside** the payload file, you must load the entire payload just to see what variants are available or to change a color. By "lofting" these controls **above** the payload arc (in the interface file), they become immediately accessible without loading the heavy geometry.

**Visual Example:**

```usda
# Asset_File.usd (Interface - Lightweight)
def Xform "Pump" (
    prepend payload = @./Payloads/Pump_payload.usdc@  # Heavy geometry here
)
{
    # ✅ LOFTED: These are accessible WITHOUT loading the payload
    
    # Lofted Variant Set
    variantSet "resolution" = "high" {
        "low" {
            uniform token model:lod = "low"
        }
        "high" {
            uniform token model:lod = "high"
        }
    }
    
    # Lofted Primvars (for material control)
    color3f primvars:displayColor = (0.3, 0.5, 0.9)
    float primvars:roughnessFactor = 0.5
    
    # Lofted Metadata
    string digitalTwin:plmId = "PLM-00982"
    double3[] extentsHint = [(-1, -1, -1), (1, 1, 1)]
}
```

**What Gets Lofted:**

*   **Variant Sets** - Control logical variations (LOD, color, damage state) without loading geometry
*   **Primvars** - Control material/shader inputs (`primvars:displayColor`, `primvars:roughnessFactor`)
*   **Extents Hints** - Bounding box information for viewport culling
*   **Draw Modes** - Control how the asset is displayed (wireframe, bounding box, full)
*   **Metadata** - PLM IDs, operational parameters, digital twin data
*   **Material Bindings** - Material assignments that can be changed without loading geometry

**Performance Benefit:**

Without lofting:
- User wants to see variant options → Must load entire payload (slow)
- User wants to change color → Must load entire payload (slow)
- Viewport needs bounding box → Must load entire payload (slow)

With lofting:
- User sees variant options → No payload load needed (instant)
- User changes color → No payload load needed (instant)
- Viewport gets bounding box → No payload load needed (instant)

**Best Practice:** Always loft controls that users or tools need to access frequently, especially variant sets and key primvars.

---

## 3. Composition Strength (LIV(E)RPS)

**What is LIV(E)RPS?**

LIV(E)RPS is the rulebook that decides which data "wins" when multiple sources provide conflicting information in a USD scene. It stands for the strength ordering from **strongest to weakest**:

| Letter | Name | What It Is | Strength |
|--------|------|------------|----------|
| **L** | **Local** | Direct edits in the current layer | **Strongest** |
| **I** | **Inherits** | Properties inherited from classes/templates | Very strong |
| **V** | **Variants** | Switchable options (e.g., red/blue, high/low) | Pretty strong |
| **(E)** | **(rElocates)** | Remap prim paths during composition | Between Variants & References |
| **R** | **References** | Pulling in other USD files/assets | Not so strong |
| **P** | **Payloads** | Heavy data loaded on demand | Only if needed |
| **S** | **Specializes** | Weak template/base class | **Weakest** |

**Note on rElocates (E):**

**rElocates** remap prim paths during composition, allowing you to move/rename prims non-destructively:

```usda
# Relocate /OldPath to /NewPath
relocates = {
    /OldPath: /NewPath
}
```

**Why rElocates Matter:**
- **Asset reorganization**: Remap paths without breaking references
- **Multi-site pipelines**: Adapt paths when assets move between systems
- **Non-destructive editing**: Rename prims without losing composition
- **Position in strength**: Variants > rElocates > References

**⚠️ Implementation Status:** **LIV(E)RPS** (with rElocates) is the official OpenUSD specification from Pixar. rElocates are officially part of LIV(E)RPS (position 4, between Variants and References). **Omniverse Kit App 108.1 status: Unconfirmed** — rElocates not mentioned in Omniverse release notes, but are already part of PIXAR OpenUSD Definitions. When working with Omniverse, verify support or use LIVRPS order without rElocates.

**Simple Rule:** When two or more sources set the same property, **the one higher in LIV(E)RPS wins**. This keeps complex 3D scenes predictable and conflict-free.

**Example:** If a referenced asset sets `color=blue` but your local layer sets `color=red`, the local (red) wins because **Local > Reference**.

---

Understanding composition strength is critical for structuring root files. Opinions in the **Root Layer (Local)** are the strongest and cannot be easily overridden by sublayers.

### **The "Root Layer Trap"**
*   **Problem:** If you define attributes, references, or payloads directly in the root file (e.g., `def Xform "MyAsset" { double xformOp:translate = (10,0,0) }`), no sublayer can override that position because **Local > SubLayers**.
*   **Solution:** Keep the Root File "thin". It should primarily define the structure and hold the `subLayer` list.
*   **Best Practice:** Author actual opinions (geometry references, layout transforms, shading) inside the sublayers (e.g., `Layout.usd`), not the root file. This allows other sublayers (like `Overrides.usd` or `Variants.usd`) to override them successfully.

### **Anti-Patterns: Inline Geometry & Direct References**

#### **1. Inline Geometry (Storing Data in Root)**
*   **Definition:** Defining `def Mesh` with heavy vertex data directly in the Root Layer.
*   **Status:** ⛔ **CRITICAL ANTI-PATTERN**
*   **Why it fails:**
    *   **Performance:** The Root Layer is *always* parsed first. Heavy text data bloats open times.
    *   **Memory:** The Root Layer cannot be unloaded. Geometry sits in RAM permanently.
    *   **Collaboration:** Causes massive merge conflicts.
*   **Exception:** Simple helpers (e.g., a 4-vertex ground plane) are acceptable.

#### **2. Direct References (Bypassing Payloads)**
*   **Definition:** Using `references = @./geo.usd@` instead of `payload = @./geo.usd@`.
*   **Status:** ⚠️ **Use with Caution**
*   **Why it fails:**
    *   **Eager Loading:** Forces immediate loading of heavy assets, killing viewport performance.
    *   **UX:** Users cannot choose to see only bounding boxes.
*   **Best Practice:** Always use **Payloads** for heavy assets to enable "lazy" loading.

### **Summary Recommendation**

| Approach | Status | Impact |
| :--- | :--- | :--- |
| **Inline Geometry in Root** | ⛔ **Avoid** | Bloats file, slows parsing, locks memory. |
| **Direct References** | ⚠️ **Caution** | Forces eager loading, slows viewport. |
| **Payloads** | ✅ **Best Practice** | Enables lazy loading, fast open, memory management. |

---

## 4. Root File and Layer Stacking Strategy

**Critical Concept:** The root file defines the structure and layer composition. Asset loading happens in the **lowest (weakest) layer**, with all modifications stacked on top.

### **Root File Structure**

The root file (`GoodStart_ROOT.usda` or `Asset_Root.usd`) should be **thin** and contain:
*   Base scene structure (e.g., `def Xform "World"`)
*   `subLayers` array defining the layer stack
*   Metadata (defaultPrim, upAxis, metersPerUnit)
*   **NO** geometry, references, payloads, or attribute values

### **Layer Stack Order (Array Ordering: First = Strongest, Last = Weakest)**

The `subLayers` array is ordered from **strongest (first)** to **weakest (last)**. This is separate from LIV(E)RPS composition strength ordering, which applies to composition arcs. The array ordering determines layer application: first in array = strongest (applied last, overrides others), last in array = weakest (applied first, can be overridden).

**Standard Layer Stack:**
1.  **Opinion_xyz_LYR.usda** (first/strongest) - Overrides and opinions
    *   Final overrides
    *   Scene-specific modifications
    *   Layout adjustments

2.  **Variant_LYR.usda** - Variants and configurations
    *   Variant set definitions
    *   Configuration options
    *   Logical variations

3.  **Mtl_work_LYR.usda** - Materials and shading work
    *   Material assignments and overrides
    *   Texture bindings
    *   Shader modifications

4.  **AssetImport_LYR.usda** (last/weakest) - **CRITICAL: Asset Loading Layer**
    *   References and payloads for all assets
    *   Holds geometry imports
    *   This is where assets enter the scene
    *   Must be last in array so other layers can override it

### **Why AssetImport Must Be Last in Array**

**This is crucial:** The AssetImport layer must be the **last (weakest) in the array** because:
*   It loads assets via references/payloads
*   Earlier layers (materials, variants, opinions) need to be able to override asset properties
*   Materials, variants, and opinions must be able to modify what's loaded
*   The `subLayers` array is ordered strongest-first: first = strongest (applied last), last = weakest (applied first)
*   If AssetImport were first in the array, nothing could override the loaded assets

**Example Root File:**
```usda
#usda 1.0
(
    defaultPrim = "World"
    subLayers = [
        @./020_LYR_USD/Opinion_xyz_LYR.usda@,      # First = strongest (applied last, overrides others)
        @./020_LYR_USD/Variant_LYR.usda@,         # Second
        @./020_LYR_USD/Mtl_work_LYR.usda@,        # Third
        @./020_LYR_USD/AssetImport_LYR.usda@       # Last = weakest (applied first, can be overridden) - loads assets
    ]
)

def Xform "World" {}
```

**Note:** The `subLayers` array ordering (strongest-first) is separate from LIV(E)RPS composition strength ordering (Local > Inherits > Variants > rElocates > References > Payloads > Specializes). Both work together to determine which opinions win in USD composition.

**Benefits:**
*   **Parallelism:** Different departments can edit separate files simultaneously without merge conflicts
*   **Sparse Overrides:** Each layer only contains changes relevant to that workstream
*   **Non-Destructive:** Assets can be modified without changing source files
*   **Composition Strength:** Higher layers can override lower layers following LIV(E)RPS rules

---

## 5. Asset Parameterization

Make assets reusable by exposing controls.

### **Variant Sets** (Discrete Choices)
Use for switching between completely different geometric or material states.
*   *Example:* `DamageState` (Intact, Damaged, Destroyed), `LOD` (High, Med, Low).
*   *Behavior:* Changes the scene graph structure; generates new instance prototypes.

### **Primvars** (Continuous/Material Values)
Use for passing data to shaders or procedural behaviors.
*   *Example:* `primvars:baseColor`, `primvars:roughnessFactor`.
*   *Behavior:* Values interpolate down the hierarchy; efficiently handled by renderers without breaking instancing.

---

## 6. Recommended Directory Structure

A typical production project structure follows this organization:

```text
USD_GoodStart/
├── GoodStart_ROOT.usda     # Root file (entry point) - defines structure and subLayers
├── 000_SOURCE/             # Original CAD/DCC source files
├── 010_ASS_USD/            # USD assets (converted from CAD or created in DCC)
├── 020_LYR_USD/            # Layer files for non-destructive modifications
│   ├── AssetImport_LYR.usda    # Bottom layer - loads assets (references/payloads)
│   ├── Mtl_work_LYR.usda       # Materials and shading work
│   ├── Variant_LYR.usda        # Variants and configurations
│   └── Opinion_xyz_LYR.usda    # Top layer - overrides and opinions
└── 030_TEX/                # Global texture files
```

**Note on Source Files (`000_SOURCE/`):**

In enterprise environments, source files (CAD, DCC originals) are often managed by **higher-level systems** such as:
*   **PLM (Product Lifecycle Management)** systems
*   **PDM (Product Data Management)** systems
*   **ERP (Enterprise Resource Planning)** systems
*   Other organizing/paradigm programs

The entire source file management may be handled **entirely differently** in these systems, with their own versioning, access control, and storage strategies. However, **for starting out and learning**, it's good practice to maintain a local `000_SOURCE/` folder structure. This provides:
*   **Learning clarity**: Clear visibility of source-to-USD conversion workflow
*   **Development flexibility**: Easy access during initial project setup
*   **Migration path**: As projects mature, source management can migrate to PLM/PDM/ERP systems while maintaining the USD asset structure

The USD asset structure (`010_ASS_USD/`, `020_LYR_USD/`) remains independent of source file management, allowing flexibility in how source files are organized and versioned.

### **Key Structure Principles:**

**Root File (`GoodStart_ROOT.usda`):**
*   Entry point for the entire project
*   Contains `subLayers` array referencing all layer files
*   Defines base scene structure (e.g., `def Xform "World"`)
*   **Thin** - no geometry, references, or payloads directly in root

**Layer Files (`020_LYR_USD/`):**
*   **Opinion_xyz_LYR.usda** (first/strongest) - Final overrides and scene-specific modifications
*   **Variant_LYR.usda** - Variant set definitions
*   **Mtl_work_LYR.usda** - Material assignments and shading
*   **AssetImport_LYR.usda** (last/weakest) - **CRITICAL**: This is where assets are loaded
  *   Contains all `references` and `payload` arcs
  *   Imports assets from `010_ASS_USD/`
  *   Must be last in array so other layers can override

**Asset Directory (`010_ASS_USD/`):**
*   Self-contained USD assets
*   Each asset folder contains:
  *   `Asset.usd` - Entry point (interface)
  *   `payload.usd` - Heavy content (geometry)
  *   `textures/` - Asset-specific textures (optional)
  *   Global textures go in `030_TEX/`

**Why This Structure Works:**
*   **Clear separation**: Assets vs. modifications vs. textures
*   **Non-destructive**: Assets never modified directly
*   **Composition strength**: Layers stack correctly (strongest-first in array: first = strongest, last = weakest)
*   **Team collaboration**: Different teams work on different layers
*   **PLM/PDM integration**: Assets can be versioned independently

