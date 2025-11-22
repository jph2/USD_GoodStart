
# **OpenUSD Best Practices Guide**
A comprehensive, multi‑disciplinary guide merging VFX, Digital Twin, Simulation, and CAD-to-USD production workflows.

---

# **Chapter 1 — Core Principles of OpenUSD Asset Structure**

OpenUSD is designed for scalable, non-destructive collaboration. Four pillars define effective USD asset creation:

## **1.1 Legibility**
- Use clear, intent-first names: `LargeCardboardBox`, not `Box01`.
- Separate public vs. private prims:
  - `Geometry` vs. `_internal_geo`
- Avoid timestamps, random hashes, and unstable naming schemes.
- Use ASCII/UTF‑8 identifiers for maximum compatibility.

## **1.2 Modularity**
- Assets must be self-contained.
- Use **anchored relative paths** (`@./payloads/mesh.usd@`).
- Define **stable root prims** as the asset interface.
- Internals may change as long as the public API stays stable.

## **1.3 Performance**
- Prefer `.usdc` for production.
- Use **payloads** for heavy geometry.
- Use **instancing** to reduce prim count.
- Keep hierarchies shallow.

## **1.4 Navigability**
- Use `Collections` to group lights, colliders, materials, controls.
- Strive for short, predictable hierarchies.
- Keep organizational scopes clean:  
  `/MyAsset/Geometry/MeshA`

---

# **Chapter 2 — The Reference/Payload Pattern**

## **2.1 Purpose**
This separates:
- **Interface Layer** → lightweight structure + controls
- **Payload Layer** → heavy geometry, shading, internals

### **Example**
```
Asset.usd
└── MyAsset (Xform)
      ├── variantSets
      ├── primvars
      └── payload @./payload.usd@
```

## **2.2 Why It Matters**
- Opens instantly in bounding-box mode  
- Heavy geometry loads only when needed  
- Allows lofted controls above payloads

## **2.3 Lofting**
Move important controls **above** the payload arc:
- Variant selections  
- Model quality toggles  
- Material overrides  
- Extents  
- Draw modes  

---

# **Chapter 3 — Composition Strength (LIVERPS)**

USD resolves opinions in this order:

1. **Local**  
2. **Inherits**  
3. **Variants**  
4. **References**  
5. **Payloads**  
6. **Sublayers**

## **3.1 The Root Layer Trap**
If you define strong opinions (like transforms) in the root, you cannot override them.

### ***Wrong***
```
def Xform "Machine"
{
    double xformOp:translate = (10, 0, 0)
}
```

### ***Correct***
- Keep the root thin  
- Author transforms, references, materials in sublayers  

---

# **Chapter 4 — Layer Stacking & Workstreams**

A clean, multi-layer approach enables parallel work.

## **4.1 Example Layer Stack**
```
Root.usda
  ├── Variant_LYR.usda
  ├── Materials_LYR.usda
  ├── AssetImport_LYR.usda
  └── Physics_LYR.usda
```

## **4.2 Department Ownership**
- **Modeling** → AssetImport  
- **Shading** → Materials  
- **TA / Config** → Variants  
- **Lighting / Layout** → Opinions  

---

# **Chapter 5 — Parameterization**

## **5.1 Variant Sets**
Use for **discrete** changes:
- LOD  
- Damage states  
- Model versions  

## **5.2 Primvars**
Use for **continuous** values:
- Colors  
- Roughness  
- Procedural parameters  

## **5.3 Combine Them**
Variants define structure.  
Primvars define values.

---

# **Chapter 6 — Recommended Project Structure**

```
USD_Project/
├── 000_SOURCE/
├── 010_ASS_USD/
├── 020_LYR_USD/
├── 030_TEX/
└── Root.usda
```

## **6.1 Folder Purpose**
- **000_SOURCE** → CAD, FBX, vendor files  
- **010_ASS_USD** → converted USD geometry  
- **020_LYR_USD** → composition layers  
- **030_TEX** → global textures  
- **Root.usda** → entry point  

---

# **Chapter 7 — Path Rules**

## **7.1 Always Use Relative Paths**
```
@./010_ASS_USD/Engine.usdc@
```

## **7.2 Never Use Absolute Paths**
Breaks portability.

## **7.3 Anchoring**
Relative paths are anchored to the current file location.

---

# **Chapter 8 — Tools & Software**

## **8.1 Preferred**
- Houdini Solaris  
- Omniverse Kit/Composer  
- usdview  
- ShapeFX Loki  

## **8.2 Limited Tools**
- Blender  
- Cinema4D  
(Export-only, no composition arcs)

## **8.3 Version Control**
- Use Git LFS  
- Avoid storing binary crate files directly in Git without LFS  

---

# **Chapter 9 — CAD → USD Workflow**

## **9.1 Pipeline**
1. Collect source CAD in `000_SOURCE`.
2. Convert using:
   - Omniverse CAD importer  
   - CAD-to-OpenUSD tools  
3. Validate topology, hierarchy, metadata.
4. Store geometry in `010_ASS_USD`.

## **9.2 CAD Cleanup**
- Remove empty assemblies  
- Simplify hierarchical clutter  
- Standardize naming  

## **9.3 Simulation Prep**
Add physics metadata in `Physics_LYR.usda`.

---

# **Chapter 10 — Metadata Strategy**

Two approved methods:

## **10.1 Custom Attributes**
For dynamic or query-heavy fields:

```
string digitalTwin:plmId = "PLM-12345"
```

## **10.2 customData Dictionaries**
For descriptive/nested metadata:

```
customData = {
    dictionary digitalTwin = {
        string source = "CAD-System"
    }
}
```

---

# **Chapter 11 — Digital Twin, Simulation & Physical AI**

## **11.1 Physics**
Add colliders, rigid-body data:
```
float physics:mass = 10.0
```

## **11.2 Semantics**
```
string ml:class = "conveyor"
int ml:instanceId = 5
```

## **11.3 Domain Randomization**
Useful for synthetic data & AI training:
- Material variation  
- Lighting variation  
- Pose variation  

---

# **Chapter 12 — CI/CD, Validation & Automation**

## **12.1 Tools**
- `usdchecker`  
- Custom Python validators  
- Build scripts in CI (GitHub Actions, Jenkins, GitLab)  

## **12.2 What to Validate**
- File structure  
- Broken references  
- Naming conventions  
- Payload usage  
- Variant correctness  

---

# **Chapter 13 — Implementation Strategy**

Follow the Agile scaling model:

## **13.1 Stage 1 — POC**
- Validate CAD → USD pipeline  
- Test payloading  

## **13.2 Stage 2 — MVP**
- Assemble small working digital twin  

## **13.3 Stage 3 — Scaling**
- Build shared library  
- Introduce CI/CD  
- Establish departmental conventions  

---

# **Chapter 14 — Asset Lifecycle**

1. Source CAD  
2. Convert to USD  
3. Author geometry layer  
4. Add materials  
5. Add variants  
6. Add physics  
7. Assemble  
8. Validate  
9. Publish to repository  

---

# **Chapter 15 — Additional Resources**

- NVIDIA Digital Twin Learning Path  
- LearnOpenUSD.org  
- USDWG resources  
- AOUSD standardisation  
- GitHub: CAD-to-OpenUSD  
- Pixar USD Repository  

---

# **End of Document**
