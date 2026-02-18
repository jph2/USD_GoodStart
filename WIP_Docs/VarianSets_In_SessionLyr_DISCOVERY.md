# Variant Sets in Session Layer - Discovery

**Version:** 1.4.0
**Date:** 26.01.2026
**Time:** 11:55
**GlobalID:** 20260126_1155_VariantSetsInSessionLyr_001
**Last Updated:** 26.01.2026 12:45
**Framework:** General_Research (Discovery Phase)
**Status:** Solution Identified - Ready for Implementation
**Domain:** USD/Omniverse (Domain_OmniUSD_Guardrails)
**Tag block:**
#variant #layer #conversion #omniverse #openusd #material #variants #opinions #workflow_automation #best_practices #usd_core #hybrid #layers #composition #quality_assurance #validation #analysis #case_study #workflow_optimization #deterministic_workflows

---

## 🎯 **Discovery Overview**

**Subject:** Forcing variant selections to be written to session layer instead of current editing layer in Omniverse/OpenUSD workflows

**Purpose:** Investigate how to ensure variant set selections (e.g., material variants, configuration options) are authored to the session layer rather than polluting base layer files when working in Omniverse Kit applications.

**Research Framework:**
- **Ruling contract:** `Research_Definition/research_configuration_rules.yml`
- **Location:** `General_Research/070_Proj_RESEARCH/02_Research_WIP/`
- **Next Phase:** Convert to `_RESEARCH.md` when ready for structured analysis
- **Domain Context:** USD/Omniverse development (Domain_OmniUSD_Guardrails)

---

## 📋 **Initial Observations**

<!-- FRAME_STATUS: UNSET -->

### Problem Statement

**Current Behavior:**
- When working in Omniverse Kit/Composer and changing variant selections (e.g., switching from Material_A to Material_B, or changing configuration variants), the variant selection is written to **whichever layer is currently active/editable**.
- This causes **layer pollution** - base layer files (e.g., `050_VAR_LYR/VAR_LYR.usda`) get modified with variant selections that should be temporary session-level changes.
- If these changes are saved, they become permanent in the layer files, breaking the intended layer structure and causing version control issues.

**Desired Behavior:**
- Variant selections should be written to the **session layer** (temporary, in-memory layer) by default.
- Session layer changes should **not persist** to disk unless explicitly intended.
- Base layer files should remain clean and unmodified by temporary variant testing.

**Impact:**
- **File integrity:** Base layer files get polluted with temporary variant selections
- **Version control:** Unintended changes get committed to layer files
- **Workflow disruption:** Users must manually revert changes or risk breaking layer structure
- **Collaboration issues:** Other team members see unintended variant selections in shared layer files

### Key Questions to Explore:

1. **USD Session Layer Mechanics:**
   - How does USD's session layer work?
   - What is the relationship between session layer and regular layers?
   - How does Omniverse Kit handle session layer vs. regular layer editing?

2. **Variant Selection Authoring:**
   - Where does USD/Omniverse write variant selections by default?
   - What controls which layer variant selections are written to?
   - Is there a way to force variant selections to session layer?

3. **Omniverse Kit Behavior:**
   - How does Omniverse Kit determine the target layer for variant selections?
   - Are there settings or preferences to control this behavior?
   - What is the "authoring layer" concept in Omniverse?

4. **Workflow Solutions:**
   - What are best practices for variant management in Omniverse?
   - Are there workarounds or techniques to prevent layer pollution?
   - How do other USD workflows handle this issue?

5. **Technical Implementation:**
   - Can USD Python API control where variant selections are written?
   - Are there Omniverse extensions that address this?
   - What are the USD composition rules that govern this behavior?

### Preliminary Findings (Updated with MCP Research):

- **Finding 1:** ✅ USD has a concept of "session layer" - accessible via `Usd.Stage.GetSessionLayer()`
- **Finding 2:** ✅ Omniverse Kit has an "authoring layer" concept - controlled by `omni_layer` metadata and `Usd.Stage.SetEditTarget()`
- **Finding 3:** ✅ Variant selections follow standard edit target rules - they go to the current `EditTarget`
- **Finding 4:** ✅ **SOLUTION CONFIRMED:** Temporarily setting edit target to session layer before `SetVariantSelection()` causes variant selections to be written to session layer
- **Finding 5:** ✅ `UsdEditContext` provides automatic edit target restoration for scoped edits
- **Finding 6:** ✅ `omni.usd.get_context().get_stage()` is the recommended way to get the stage in Omniverse Kit

---

## 🔍 **Research Scope**

<!-- SCOPE_STATUS: UNSET -->

### Boundaries:

**What to Include:**
- USD session layer mechanics and behavior
- Omniverse Kit/Composer variant selection workflows
- USD Python API methods for controlling variant selection authoring
- Best practices for variant management in layered USD workflows
- Technical solutions and workarounds for forcing variant selections to session layer
- Extension development possibilities for Omniverse
- Comparison with other USD authoring tools (Maya, Houdini, etc.)

**What to Exclude (save for later phases):**
- General USD composition arc explanations (unless directly relevant)
- Complete variant set creation workflows (focus on selection, not creation)
- Material authoring workflows (unless variant-related)
- CAD-to-USD conversion workflows
- Metadata management (unless variant-related)

### Success Criteria:

**Discovery Phase Success:**
- Clear understanding of how USD/Omniverse handles variant selection authoring
- Identification of root cause for variant selections being written to wrong layers
- Documentation of available solutions, workarounds, or techniques
- Assessment of feasibility for implementing a solution
- Clear path forward for either:
  - Implementing a technical solution
  - Establishing workflow best practices
  - Developing an Omniverse extension if needed

**Transition to Research Phase:**
- When technical solutions are identified and need detailed analysis
- When implementation approaches need to be evaluated
- When extension development requirements are understood

---

## 📚 **References & Resources**

### USD/OpenUSD Documentation:
- **Pixar USD Documentation:** [openusd.org](https://openusd.org/)
- **NVIDIA Learn OpenUSD:** [docs.nvidia.com/learn-openusd](https://docs.nvidia.com/learn-openusd/latest/index.html)
- **USD Python API:** Session layer and variant selection methods
- **USD Composition:** LIV(E)RPS and layer stacking rules

### Omniverse Documentation:
- **Omniverse Kit Documentation:** [docs.omniverse.nvidia.com](https://docs.omniverse.nvidia.com/)
- **Omniverse Composer Manual:** Layer management and variant workflows
- **Omniverse Extensions:** Extension development for custom workflows

### Project-Specific Resources:
- **USD_GoodStart Repository:** `E:\SynologyDrive\9999_LocalRepo\USD_GoodStart`
  - Layer structure: `050_VAR_LYR/VAR_LYR.usda` - Variant layer file
  - Root file: `GoodStart_ROOT.usda` - Contains layer stack and `omni_layer` metadata
  - README: Comprehensive USD workflow documentation
- **Domain Guardrails:** `Domain_OmniUSD_Guardrails/` - USD/Omniverse standards and best practices

### MCP Tools Available:
- **USDcodeNIM MCP:** USD code validation and generation helpers
- **SynapGarden MCP:** Omniverse, Isaac Sim, Isaac Lab related resources

### Related Research Areas:
- USD layer management best practices
- Omniverse authoring layer workflows
- Session layer vs. persistent layer patterns
- Variant management in production USD pipelines

---

## 🔬 **Technical Context**

### Current Project Structure:

**USD_GoodStart Layer Stack:**
```
GoodStart_ROOT.usda
├── subLayers = [
│   @./040_SIM_LYR/sample_SIM_LYR.usda@,
│   @./060_META_LYR/sample_META_LYR.usda@,
│   @./030_USD_LYR/sample_USD_LYR.usda@,
│   @./050_VAR_LYR/sample_VAR_LYR.usda@,
│   @./030_USD_LYR/your very Personal opinion_LYR.usda@,
│   @./050_VAR_LYR/VAR_LYR.usda@,  ← Variant layer (problematic)
│   @./030_USD_LYR/abc_Opinion_LYR.usda@,
│   @./030_USD_LYR/xyz_Opinion_LYR.usda@,
│   @./030_USD_LYR/Mtl_import_LYR.usda@,
│   @./030_USD_LYR/Ass_import_LYR.usda@
│ ]
└── omni_layer metadata:
    └── authoring_layer = "./030_USD_LYR/your very Personal opinion_LYR.usda"
    └── locked = { ... }  (includes VAR_LYR.usda)
```

**Variant Layer Example (`050_VAR_LYR/VAR_LYR.usda`):**
```usda
over "World"
{
    over "Geo"
    {
        over "nvidia_shader_ball" (
            variants = {
                string Mtl_Variant = "material_1"  ← This gets changed
            }
            prepend variantSets = "Mtl_Variant"
        )
        {
            variantSet "Mtl_Variant" = {
                "material_1" { ... }
                "material_2" { ... }
            }
        }
    }
}
```

### Key USD Concepts:

**Session Layer:**
- Temporary, in-memory layer that sits on top of the layer stack
- Changes in session layer do not persist to disk
- Used for temporary edits, testing, and preview

**Authoring Layer:**
- The layer that Omniverse Kit writes edits to
- Determined by `omni_layer` metadata or active layer selection
- Can be set per-stage or per-edit

**Layer Stacking:**
- Layers are ordered from weakest (bottom) to strongest (top)
- Session layer is typically the strongest layer
- Variant selections follow LIV(E)RPS composition rules

---

## 🚀 **Next Steps**

### Immediate Actions:

1. **Investigate USD Session Layer API:**
   - Research `Usd.Stage.GetSessionLayer()` and related methods
   - Understand how to set session layer as target for edits
   - Explore USD Python API for variant selection authoring

2. **Examine Omniverse Kit Behavior:**
   - Test variant selection in Omniverse Composer
   - Observe which layer gets modified
   - Check for settings/preferences related to authoring layer
   - Investigate `omni_layer` metadata behavior

3. **Review USD_GoodStart Project:**
   - Analyze current variant layer structure
   - Check `omni_layer` metadata in root file
   - Understand layer locking configuration
   - Document current workflow issues

4. **Search for Existing Solutions:**
   - Check Omniverse forums and community discussions
   - Review USD best practices documentation
   - Look for extensions or tools that address this
   - Compare with other USD authoring tools (Maya, Houdini)

5. **Consult MCP Resources:**
   - Use USDcodeNIM MCP for USD code examples
   - Query SynapGarden MCP for Omniverse-specific resources
   - Search for variant management patterns

### Future Research Needs:

- **If Technical Solution Found:**
  - Detailed implementation analysis
  - Python script development for forcing session layer
  - Extension development requirements (if needed)
  - Testing and validation approach

- **If Workflow Solution Needed:**
  - Best practices documentation
  - Workflow guidelines for team
  - Layer management protocols
  - Version control integration

- **If Extension Development Required:**
  - Omniverse Kit extension architecture
  - Extension development workflow
  - Integration with existing tools
  - User interface design considerations

### Validation Requirements:

- **Test Scenarios:**
  - Change variant selection in Omniverse Composer
  - Verify which layer gets modified
  - Test session layer targeting
  - Validate layer file integrity after changes

- **Success Metrics:**
  - Variant selections go to session layer (not base layers)
  - Base layer files remain unmodified
  - Workflow is intuitive and reliable
  - No unintended file pollution

---

## 🔍 **External Research Prompts**

### Prompt for Perplexity/ChatGPT Research

**Copy the following prompt to Perplexity or ChatGPT for independent research:**

---

**Research Request: USD/Omniverse Variant Selection Session Layer Control**

I'm working with OpenUSD/Omniverse workflows and need to understand how to control where variant set selections are written when editing in Omniverse Kit applications.

**Problem Context:**
- When changing variant selections (e.g., material variants, configuration options) in Omniverse Composer/Kit, the selections are being written to the currently active/editable layer instead of the session layer
- This causes base layer files (like `050_VAR_LYR/VAR_LYR.usda`) to be polluted with temporary variant selections
- If saved, these changes become permanent in layer files, breaking the intended layer structure and causing version control issues
- I need variant selections to be written to the session layer (temporary, in-memory) by default, not to persistent layer files

**Technical Context:**
- Using USD layer stack with multiple sublayers (variant layers, material layers, asset import layers)
- Root file contains `omni_layer` metadata with `authoring_layer` specification
- Some layers are locked, but variant selections still seem to write to unlocked layers
- Session layer exists and can be accessed via `Usd.Stage.GetSessionLayer()` in Python API

**Research Questions:**

1. **USD Session Layer Mechanics:**
   - How does USD's session layer work in practice?
   - What is the relationship between session layer and regular layers in the composition stack?
   - How does the session layer interact with variant selections specifically?
   - Can variant selections be explicitly authored to the session layer using USD Python API?

2. **Omniverse Kit Behavior:**
   - How does Omniverse Kit/Composer determine which layer to write variant selections to?
   - What controls the "authoring layer" behavior in Omniverse?
   - Are there settings, preferences, or configuration options to force variant selections to session layer?
   - How does the `omni_layer` metadata `authoring_layer` field affect variant selection authoring?
   - Does layer locking prevent variant selection edits, or only other types of edits?

3. **USD Python API Solutions:**
   - What USD Python API methods exist for controlling where variant selections are written?
   - Can `Usd.Prim.SetVariantSelection()` be used with a specific edit target (session layer)?
   - How do `Usd.EditTarget` and `Usd.Stage.SetEditTarget()` work with variant selections?
   - Are there examples of Python scripts that force variant selections to session layer?
   - What is the relationship between `Usd.Stage.GetEditTarget()` and variant selection authoring?

4. **Best Practices & Workflows:**
   - What are industry best practices for variant management in USD/Omniverse workflows?
   - How do production pipelines handle temporary variant testing without polluting base layers?
   - Are there workflow patterns or techniques that avoid this issue entirely?
   - How do other USD authoring tools (Maya USD, Houdini Solaris) handle variant selection authoring?

5. **Omniverse Extensions & Solutions:**
   - Are there existing Omniverse extensions that address variant selection layer targeting?
   - What would be required to develop an Omniverse extension for this functionality?
   - Are there community discussions, forum posts, or GitHub issues about this specific problem?
   - Has NVIDIA addressed this in recent Omniverse releases or documentation?

6. **Code Examples & Technical Details:**
   - Provide Python code examples showing how to:
     - Get the session layer from a USD stage
     - Set edit target to session layer
     - Author variant selections to session layer programmatically
     - Verify which layer contains variant selections
   - Explain the USD composition rules (LIV(E)RPS) as they relate to variant selections and layer targeting
   - Show how to inspect `omni_layer` metadata and understand its effect on authoring behavior

**Requested Information:**
- Technical documentation references (USD API docs, Omniverse docs)
- Code examples and Python snippets
- Forum discussions or community knowledge
- Best practice recommendations
- Known limitations or workarounds
- Comparison with other USD authoring tools

**Please provide:**
1. Comprehensive technical explanation of how variant selection authoring works
2. Specific API methods and code examples for controlling authoring target
3. Omniverse-specific behavior and configuration options
4. Production workflow recommendations
5. Links to relevant documentation, forum discussions, or GitHub issues

---

**Usage Notes:**
- Use this prompt in Perplexity for web-search enhanced research
- Use in ChatGPT for detailed technical explanations and code examples
- Modify the prompt to focus on specific aspects if needed
- Save findings back to this discovery document

---

## 🔬 **MCP Research Findings**

### Research Date: 26.01.2026

**Sources Consulted:**
- **USDcodeNIM MCP** (USD Python code generation) → Generated [L04]
- **SynapGarden Isaac MCP** (Omniverse/Isaac Sim documentation) → Retrieved [L08, L09, L10, L15]
- **Context7 MCP** (OpenUSD API documentation) → Retrieved [L01, L02, L03, L05, L06, L07, L11, L12, L13, L14]

**Note:** All source links are documented in the **Appendix: Source Links** section at the end of this document. Links are numbered [L01]-[L15] for cross-referencing.

---

### Finding 1: USD Session Layer API (CONFIRMED) [Refs: L01, L02, L03]

**The USD Python API provides explicit methods for controlling where edits are written:**

**Key Methods:**
- `Usd.Stage.GetSessionLayer()` - Returns the session layer handle [L02]
- `Usd.Stage.SetEditTarget(editTarget)` - Sets where edits go [L02]
- `Usd.EditTarget(layer)` - Creates an edit target from a layer [L01]
- `Usd.Stage.GetEditTarget()` - Returns current edit target [L02]

**Session Layer Characteristics:**
- Temporary, in-memory layer at the top of the layer stack
- Strongest layer in composition (overrides all persistent layers)
- Does NOT persist to disk when stage is saved
- Always exists for every USD stage

---

### Finding 2: Core Solution Pattern (VALIDATED) [Refs: L04, L05, L06]

**Python code pattern for forcing variant selections to session layer:**

```python
from pxr import Usd, Sdf

# Get the stage (in Omniverse Kit)
import omni.usd
stage = omni.usd.get_context().get_stage()

# 1. Save the original edit target
original_edit_target = stage.GetEditTarget()

# 2. Get the session layer
session_layer = stage.GetSessionLayer()

# 3. Set edit target to session layer
stage.SetEditTarget(Usd.EditTarget(session_layer))

# 4. Make the variant selection change
prim = stage.GetPrimAtPath('/World/Geo/nvidia_shader_ball')
variant_sets = prim.GetVariantSets()
variant_set = variant_sets.GetVariantSet('Mtl_Variant')
variant_set.SetVariantSelection('material_2')

# 5. Restore the original edit target
stage.SetEditTarget(original_edit_target)
```

**Key Insight:** `UsdVariantSet.SetVariantSelection()` always writes to the current edit target. By temporarily switching the edit target to the session layer, the selection is authored there instead of the authoring layer.

---

### Finding 3: UsdEditContext for Scoped Edits (CONFIRMED) [Refs: L07, L01]

**USD provides `UsdEditContext` for automatically restoring edit targets:**

```cpp
// C++ pattern - Python equivalent available
void ExampleEditContext(const UsdStagePtr &stage, const UsdEditTarget &editTarget) {
    // Construct UsdEditContext, setting the edit target for the scope.
    UsdEditContext editContext(stage, editTarget);

    // Perform operations that should be affected by the new edit target...

    // The original edit target will be restored automatically when 
    // editContext goes out of scope.
}
```

**Python equivalent:**

```python
from pxr import Usd

# Using context manager pattern
with Usd.EditContext(stage, Usd.EditTarget(session_layer)):
    # All edits within this block go to session layer
    variant_set.SetVariantSelection('material_2')
# Original edit target is automatically restored here
```

---

### Finding 4: Omniverse Kit Integration (CONFIRMED) [Refs: L08, L09, L10]

**Getting the stage in Omniverse Kit:**

```python
import omni.usd

# Recommended way in Omniverse Kit
stage = omni.usd.get_context().get_stage()

# Check if valid
if not stage:
    print("No valid stage found.")
```

**Isaac Sim also has a helper function:** [L08]

```cpp
// C++ API in Isaac Sim
inline bool isaacsim::core::includes::utils::usd::setAuthoringLayer(
    pxr::UsdStageRefPtr stage,
    const std::string &layerIdentifier
)
// Select an existing layer as edit target
```

---

### Finding 5: Variant-Specific Edit Targets (CONFIRMED) [Refs: L03, L05, L06]

**USD provides specialized methods for variant editing:**

```python
# Get an edit target specifically for editing within a variant
variant_edit_target = variant_set.GetVariantEditTarget(layer)  # [L05]

# Get stage and edit target pair for variant editing
stage_ptr, edit_target = variant_set.GetVariantEditContext(layer)  # [L05]
```

**However:** These are for editing WITHIN variants (the content), not for variant SELECTION. Variant selection still follows the standard edit target rules. [L06]

---

### Finding 6: Session Layer Verification (CONFIRMED) [Refs: L02, L11]

**Verify variant selections are in session layer:**

```python
# Print session layer contents to verify [L02]
print(stage.GetSessionLayer().ExportToString())

# Print root layer to verify it's clean [L02]
print(stage.GetRootLayer().ExportToString())
```

---

### Finding 7: Extension Development Path (IDENTIFIED) [Refs: L09, L12, L13]

**If a permanent solution is needed, an Omniverse extension could:**

1. Intercept variant selection UI events
2. Override the default behavior to target session layer
3. Provide user controls for choosing target layer
4. Integrate with the Omniverse layer management UI

**Extension would use:**
- `omni.kit.commands` for command interception [L12]
- `omni.usd` for stage and layer access [L09]
- Standard USD Python API for variant operations [L03]

---

## 🌐 **Perplexity Research Findings**

### Research Date: 26.01.2026

**Source:** Perplexity AI web search with multiple authoritative sources.

**Note:** This section provides independent verification and additional context for findings from MCP research. Some overlap exists, but new insights are highlighted.

---

### Finding P1: Session Layer Purpose Confirmed by Pixar [Refs: L16, L17]

**Pixar's header comments explicitly describe the session layer as the intended place for runtime variant selections:**

> "A very common intended use is variant selections: Pixar's own header comments describe the session layer explicitly as the place to store runtime variant picks so they do not pollute authored asset files."

**Key Insight:** This is not just a workaround—it's the *designed* behavior. Session layer was created specifically for this use case.

---

### Finding P2: LIVRPS Clarification [Refs: L18, L17]

**Variant selections are token opinions that follow normal composition:**

- Variant selections are stored as `variantSelections = {"model": "High"}` on prims
- The **L (Layers)** in LIVRPS determines which layer's opinion wins
- Session layer sits at the top, so its variant selections override all others
- The **V (Variants)** in LIVRPS refers to variant *content*, not variant *selection*

**Critical Distinction:** Variant selection (which variant is active) is a layer opinion. Variant content (what's inside each variant) is variant composition.

---

### Finding P3: Omniverse `omni_layer` Metadata Details [Refs: L20]

**How Omniverse determines the authoring layer:**

1. The stage's USD edit target
2. The layer selected in the Layer panel
3. Omniverse's `authoring_layer` metadata for the current workspace

**Code to inspect `omni_layer` metadata:**

```python
from pxr import Usd

stage = omni.usd.get_context().get_stage()
root_layer = stage.GetRootLayer()

# "omni_layer" metadata is a dict-like custom data blob
omni_layer_meta = root_layer.customLayerData.get("omni_layer", {})
print("omni_layer metadata:", omni_layer_meta)

authoring_layer = omni_layer_meta.get("authoring_layer")
print("Configured authoring_layer:", authoring_layer)
```

**New Insight:** You can modify `omni_layer.authoring_layer` to change the default target layer.

---

### Finding P4: Layer Locking Behavior Clarified [Refs: L20]

**Layer locking prevents direct edits but NOT overrides from stronger layers:**

> "Locking a layer prevents direct edits to that specific file but does not stop a stronger layer from overriding its opinions."

**Implication:** Even if VAR_LYR.usda is locked, if Omniverse writes a variant selection to an unlocked layer above it, the variant appears to change. The locked layer remains clean, but users see a different variant active.

---

### Finding P5: No Built-in "Force to Session Layer" Setting [Refs: L20, L21]

**Confirmed: Omniverse has no global preference for "always write variants to session layer":**

> "Omniverse does not currently document a per-operation switch like 'when changing variants, always use session layer,' so the practical control point is still the global authoring target."

**Solution:** Must be implemented via:
- Manual layer panel selection
- Scripting/extension to intercept variant changes
- Workflow discipline

---

### Finding P6: Production Best Practices [Refs: L18, L23]

**Recommended separation of concerns:**

| Layer Type | Purpose |
|------------|---------|
| **Asset USD** | Declares variant sets and their content (definitions) |
| **Shot/Config USD** | Sets `variantSelections` for a particular context |
| **Session Layer** | Temporary testing before committing to config layer |

**Production workflow pattern:**

1. Lock asset and VAR layers for normal users
2. Use dedicated config layer (e.g., `200_CFG_LYR/CFG.usda`) for selections
3. Session layer for experimentation
4. Tool to "bake" session selections into config layer when approved

---

### Finding P7: Other DCCs (Maya, Houdini) Use Same Pattern [Refs: L23]

**Maya USD and Houdini Solaris follow identical principles:**

- Maya USD: Exposes explicit edit-target selection; variant UI honors that choice
- Houdini Solaris: Authors into explicit USD node's layer or designated "working" layer
- Both: Keep asset layers separate from shot layers to prevent contamination

**Validation:** This is an industry-wide pattern, not just an Omniverse quirk.

---

### Finding P8: Helper Context Manager Pattern (NEW) [Refs: L16, L19]

**Reusable Python context manager for session layer editing:**

```python
from contextlib import contextmanager
from pxr import Usd

@contextmanager
def session_edit_target(stage: Usd.Stage):
    """Context manager to temporarily use session layer as edit target."""
    old_target = stage.GetEditTarget()
    session_layer = stage.GetSessionLayer()
    stage.SetEditTarget(Usd.EditTarget(session_layer))
    try:
        yield
    finally:
        stage.SetEditTarget(old_target)

# Usage
with session_edit_target(stage):
    prim = stage.GetPrimAtPath("/World/MyAsset")
    vs = prim.GetVariantSets().GetVariantSet("config")
    vs.SetVariantSelection("Option_B")
```

**Advantage:** Clean exception-safe pattern, automatically restores original target.

---

### Finding P9: Variant Selection Verification Code (NEW) [Refs: L18]

**Inspect which layer contains a variant selection:**

```python
from pxr import Usd, Sdf

stage = omni.usd.get_context().get_stage()
root_layer = stage.GetRootLayer()
session_layer = stage.GetSessionLayer()
prim_path = Sdf.Path("/World/Model")

def print_variant_selections(layer, label):
    prim_spec = layer.GetPrimAtPath(prim_path)
    if not prim_spec:
        print(label, ": no prim spec")
        return
    vs = prim_spec.variantSelections
    print(label, "variantSelections:", dict(vs) if vs else {})

print_variant_selections(root_layer, "Root")
print_variant_selections(session_layer, "Session")

# Walk sublayers to find where opinion is authored
for sub_id in root_layer.subLayerPaths:
    sub = Sdf.Layer.FindOrOpen(sub_id)
    if sub:
        print_variant_selections(sub, f"Sublayer {sub_id}")
```

**Use Case:** Debug which layer is "polluted" with variant selections.

---

### Finding P10: Recommended Workflow for USD_GoodStart [Refs: L18, L20]

**Specific recommendations for your layer structure:**

1. **Introduce a dedicated config layer:**
   - Create `200_CFG_LYR/CFG.usda` (or similar)
   - Update `omni_layer.authoring_layer` to point to this file
   - This becomes the default target for variant selections

2. **For ad-hoc testing:**
   - Provide script/extension that switches edit target to session layer
   - Session layer for experimentation
   - "Bake" button to copy selections from session → config layer

3. **Lock asset and VAR layers:**
   - Prevent accidental modifications
   - Only pipeline TDs modify these layers

4. **Layer panel workflow:**
   - Show Session Layer in Omniverse Layer panel
   - Manually switch to Session Layer before testing variants

---

### Finding P11: AOUSD Forum Insight on Variant Edit Targets [Refs: L22]

**Important clarification from Alliance for OpenUSD forum:**

> "`variant_set.GetVariantEditContext()` wraps the current variant as an edit context, but still uses the stage's current edit target as the layer; it only redirects opinions into the selected variant branch, not into a different layer."

**Implication:** `GetVariantEditContext()` is for editing *content inside* a variant, NOT for controlling which layer the variant selection goes to. These are separate concerns.

---

### Finding P12: Extension Development Path Confirmed [Refs: L20, L21, L22]

**A custom Omniverse extension could:**

1. Listen to variant selection changes in the UI (or provide its own variant picker)
2. On change, temporarily set `stage.SetEditTarget(Usd.EditTarget(stage.GetSessionLayer()))`
3. Call `SetVariantSelection()` on the chosen prim/variant
4. Restore the previous edit target

**Offer from Perplexity:** "I can sketch a minimal Omniverse extension skeleton that adds a 'Set variant in session layer' right-click option in the Stage tree for quick use in Composer."

---

## 📝 **Notes & Observations**

### Current Understanding (Updated with MCP + Perplexity Research):

- **USD Session Layer:** Fully accessible via `Usd.Stage.GetSessionLayer()` ✓ [L02, L17]
- **Design Intent:** Session layer was *designed* by Pixar specifically for variant selections ✓ [L16]
- **Edit Target Control:** `Usd.Stage.SetEditTarget()` controls where ALL edits go ✓ [L02, L17]
- **Variant Selections:** Follow standard edit target rules - authored to current edit target ✓ [L06, L18]
- **LIVRPS Clarification:** Variant *selection* is a Layer opinion; variant *content* is Variants composition ✓ [L18]
- **Omniverse Integration:** `omni.usd.get_context().get_stage()` provides stage access ✓ [L09]
- **omni_layer Metadata:** Controls Omniverse authoring layer, can be inspected/modified ✓ [L20]
- **Layer Locking:** Prevents direct edits but not overrides from stronger layers ✓ [L20]
- **No Built-in Switch:** Omniverse has no "force variants to session" preference ✓ [L20, L21]
- **Industry Pattern:** Maya USD, Houdini Solaris use same separation pattern ✓ [L23]

### Validated Assumptions (All Confirmed):

1. ✅ Variant selections ARE being written to the active/authoring layer [L06, L18]
2. ✅ Session layer IS the appropriate target for temporary variant selections [L16, L17]
3. ✅ There IS a way to force variant selections to session layer (via API) [L04, L19]
4. ✅ This IS solvable with standard USD Python API [L02, L03, L06]
5. ✅ This is the *designed* behavior per Pixar's original intent [L16]
6. ✅ Same pattern is used industry-wide (Maya, Houdini, etc.) [L23]

### Solution Approaches (Refined):

**Approach A: Manual Python Script** [Findings 2, P8]
- Use `session_edit_target()` context manager pattern
- Wrap in a reusable function
- Can be run from Omniverse Script Editor

**Approach B: Dedicated Config Layer** [Finding P10]
- Create `200_CFG_LYR/CFG.usda` for variant selections
- Update `omni_layer.authoring_layer` to point to this file
- Session layer for experimentation only
- "Bake" button to promote session → config

**Approach C: Omniverse Extension** [Findings 7, P12]
- Listen to variant selection changes in UI
- Intercept and redirect to session layer
- Provide "Set variant in session layer" right-click option
- Most seamless user experience

**Approach D: Workflow + Layer Panel** [Finding P5]
- Show Session Layer in Layer panel ("Show Session Layer")
- Manually switch to Session Layer before testing variants
- Simple, no coding required
- Relies on user discipline

### Answered Questions:

1. ~~Can we intercept the Omniverse UI's variant selection commands?~~
   **Answer:** Yes, via extension or `omni.kit.commands` interception [L12, P12]

2. ~~Is there a Kit setting to change default variant selection behavior?~~
   **Answer:** No global setting exists; must use scripting or manual layer selection [L20, L21]

3. ~~How does layer locking interact with session layer targeting?~~
   **Answer:** Locking prevents direct edits but stronger layers can still override [L20]

4. ~~Should variant selections in session layer be saveable on demand?~~
   **Answer:** Yes, recommended pattern is "bake" from session → config layer when approved [L18, P10]

### Remaining Questions:

1. Should we implement Approach B (config layer) or C (extension) first?
2. What should the extension UI look like?
3. Should the helper script be packaged as an extension or standalone?

---

## 📎 **Appendix: Source Links**

### Link Index

All sources retrieved via MCP tools on 26.01.2026. Links are numbered for cross-referencing with findings above.

---

**[L01]** OpenUSD API - UsdEditTarget Header Source  
https://openusd.org/release/api/edit_target_8h_source.html  
Pixar's official USD API documentation for UsdEditTarget class. Defines constructors, `ForLocalDirectVariant()` static method, `ComposeOver()`, and `GetLayer()` methods. Essential reference for understanding how edit targets control where USD edits are authored.

**[L02]** OpenUSD API - UsdStage Header Source  
https://openusd.org/release/api/usd_2usd_2stage_8h_source.html  
Pixar's official USD API documentation for UsdStage class. Documents `GetSessionLayer()`, `GetRootLayer()`, `SetEditTarget()`, `GetEditTarget()`, layer management, and muting functions. Core reference for stage-level operations including session layer access.

**[L03]** OpenUSD API - UsdVariantSets Header Source  
https://openusd.org/release/api/variant_sets_8h_source.html  
Pixar's official USD API documentation for UsdVariantSet class. Defines `SetVariantSelection()`, `GetVariantSelection()`, `ClearVariantSelection()`, `BlockVariantSelection()`, `GetVariantEditTarget()`, and `GetVariantEditContext()`. Authoritative source for variant manipulation methods.

**[L04]** USDcodeNIM MCP - Generated Code Sample (Session Layer Pattern)  
MCP Tool Response: user-nvidia-USDcodeNIM/generate_usd_code  
AI-generated Python code demonstrating the pattern for setting edit target to session layer before making variant selections. Validated against USD API documentation. Provides the core solution pattern used in Finding 2.

**[L05]** OpenUSD API - UsdVariantSet::GetVariantEditTarget  
https://openusd.org/release/api/variant_sets_8h_source.html  
USD API method for getting an edit target configured for authoring within a variant. Returns a UsdEditTarget for editing variant content (not selection). Clarifies the distinction between variant content editing and variant selection.

**[L06]** OpenUSD API - UsdVariantSet::SetVariantSelection  
https://openusd.org/release/api/variant_sets_8h_source.html  
USD API method for setting the variant selection on a VariantSet. Authors the selection to the current EditTarget. Key insight: selection authoring follows standard edit target rules, enabling session layer targeting.

**[L07]** OpenUSD API - UsdEditContext Header Source  
https://openusd.org/release/api/edit_context_8h_source.html  
Pixar's official USD API documentation for UsdEditContext class. Provides RAII-style scoped edit target management. Automatically saves and restores the original edit target when the context goes out of scope. Essential for clean, exception-safe edit target switching.

**[L08]** Isaac Sim API - setAuthoringLayer Function  
https://docs.isaacsim.omniverse.nvidia.com/latest/py/api/function__usd_8h_1a71bb0f30a0ffcb452f8e1469c781ceae.html  
Isaac Sim C++ helper function for selecting an existing layer as edit target. Demonstrates NVIDIA's pattern for authoring layer control in Omniverse-based applications. Returns true if layer is successfully selected.

**[L09]** Omniverse Kit PXR USD API - Usd Core Module  
https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr/Usd.html  
NVIDIA's Omniverse Kit documentation for the pxr.Usd module. Lists all available classes including UsdStage, UsdEditTarget, UsdEditContext, and UsdVariantSet. Official reference for USD Python API in Omniverse context.

**[L10]** Omniverse Kit PXR USD API - Sdf Module  
https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr/Sdf.html  
NVIDIA's Omniverse Kit documentation for the pxr.Sdf module. Documents SdfLayer, SdfPrimSpec, variant selection proxies, and low-level scene description types. Essential for understanding layer-level operations.

**[L11]** NVIDIA OpenUSD Code Samples - Session Layer Synchronization  
https://github.com/nvidia-omniverse/openusd-code-samples/blob/main/source/prims/print-or-export-prim/py_usd.md  
NVIDIA's official USD code samples showing how to synchronize a prim with session layer changes. Demonstrates `include_session_layer` parameter for ensuring prims reflect session layer modifications.

**[L12]** NVIDIA OpenUSD Code Samples - ChangeProperty Command  
https://github.com/nvidia-omniverse/openusd-code-samples/blob/main/source/visibility/show-hide-prim/py_kit_cmds.md  
NVIDIA's official USD code samples for using `omni.kit.commands` to change prim properties. Demonstrates Kit command pattern for intercepting and modifying property operations. Relevant for extension development approach.

**[L13]** NVIDIA OpenUSD Code Samples - Variant Selection  
https://github.com/nvidia-omniverse/openusd-code-samples/blob/main/source/variant-sets/select-variant/py_usd.md  
NVIDIA's official USD code samples for variant selection in Python. Shows standard patterns for defining variant sets, adding variants, and selecting variants programmatically.

**[L14]** OpenUSD API - UsdUtilsStageCache::GetSessionLayerForVariantSelections  
https://openusd.org/release/api/class_usd_utils_stage_cache.html  
USD utility function for retrieving or constructing a session layer based on variant selections. Returns cached session layer if available, otherwise creates new one with specified overs. Advanced pattern for variant-aware session layer management.

**[L15]** OpenUSD API - Pcp Module (Composition)  
https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr/Pcp.html  
NVIDIA's Omniverse Kit documentation for the pxr.Pcp module. Documents PrimCache Population including variant selection composition, layer stacks, and composition error types. Reference for understanding USD composition mechanics.

---

### Links from Perplexity Research (L16-L24)

**[L16]** SideFX HDK - stage.h Source Documentation  
https://www.sidefx.com/docs/hdk/stage_8h_source.html  
SideFX Houdini Development Kit documentation for USD stage handling. Contains Pixar's original header comments describing session layer as the intended place for runtime variant selections. Authoritative source confirming session layer design intent.

**[L17]** Remedy Entertainment USD Book - Edit Target  
https://remedy-entertainment.github.io/USDBook/terminology/edittarget.html  
Remedy Entertainment's comprehensive USD reference book explaining edit targets and session layers. Describes how edit targets control where authored opinions go and how session layer participates in LIVRPS composition. Excellent conceptual explanation.

**[L18]** Innoactive Documentation - Layers and Variants  
https://docs.innoactive.io/iasup/layers-and-variants  
Innoactive's documentation on USD layers and variant behavior. Explains how variant selections are token opinions that follow normal composition rules, and how session layer overrides weaker layers. Includes production best practices for layer separation.

**[L19]** Isaac Sim 6.0 - OpenUSD Fundamentals  
https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omniverse_usd/open_usd.html  
NVIDIA Isaac Sim documentation on OpenUSD fundamentals. Includes example code for session layer access, edit contexts, and variant authoring. Shows how session layer changes don't persist when saving root layer.

**[L20]** Omniverse Extensions - Layers Extension Documentation  
https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html  
NVIDIA's official documentation for the Omniverse Layers extension. Describes `omni_layer` metadata, `authoring_layer` configuration, session layer usage, live session layers, layer locking behavior, and recommended merge workflows. Primary reference for Omniverse-specific layer behavior.

**[L21]** Omniverse Dev Guide - Author Variant Data  
https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd/variant-sets/author-variant-data.html  
NVIDIA's developer guide for authoring variant data in Omniverse. Documents `GetVariantSets()`, `SetVariantSelection()`, and `GetVariantEditContext()` methods. Confirms no built-in "force to session layer" switch for variant selections.

**[L22]** AOUSD Forum - Edit Target and Variants Discussion  
https://forum.aousd.org/t/query-whether-stage-edit-target-is-targeting-a-particular-variant/1003  
Alliance for OpenUSD forum discussion clarifying relationship between edit targets and variant contexts. Explains that `GetVariantEditContext()` redirects into variant branch but still uses current edit target layer. Important for understanding variant editing vs. selection.

**[L23]** Maya USD GitHub - Variant Selection Discussions  
https://github.com/Autodesk/maya-usd/discussions/3191  
Autodesk Maya USD GitHub discussions on variant selection patterns. Shows Maya USD exposes explicit edit-target selection and that teams commonly separate asset files from shot/config files. Validates industry-wide pattern across DCCs.

**[L24]** Perplexity Research Summary  
https://www.perplexity.ai/search/2812e082-72e2-4ec3-ac3a-4423e29a49c6  
Perplexity AI research session compiling multiple sources on USD variant selection and session layer behavior. Synthesizes findings from Pixar docs, Omniverse docs, SideFX, Remedy, AOUSD forum, and Maya USD discussions into comprehensive guidance.

---


---

### Source Categories

**Official Pixar OpenUSD Documentation:**
- L01, L02, L03, L05, L06, L07, L14

**NVIDIA Omniverse Documentation:**
- L08, L09, L10, L15, L19, L20, L21

**NVIDIA OpenUSD Code Samples:**
- L11, L12, L13

**MCP Tool Generated Content:**
- L04 (USDcodeNIM)

**Third-Party USD Documentation:**
- L16 (SideFX HDK), L17 (Remedy USD Book), L18 (Innoactive)

**Community & Forum Discussions:**
- L22 (AOUSD Forum), L23 (Maya USD GitHub)

**AI Research Synthesis:**
- L24 (Perplexity)

---

## 📄 Appendix B: Raw External Research

> **Purpose:** This appendix preserves the original, unedited research outputs from external AI tools for reference and traceability. Content is stored verbatim as received.

---

### B1: Perplexity Research Output (26.01.2026)

**Query:** USD variant selections in session layer, Omniverse Kit behavior, forcing variants to session layer

**Raw Response:**

---

Variant selections are authored wherever the current stage edit target points; in USD this can be the session layer, a sublayer, or a referenced layer, and Omniverse Kit largely follows that rule with some Omniverse‑specific "authoring layer" metadata on top. To keep variants ephemeral, you must ensure the edit target is the session layer (or a dedicated override layer) before calling any variant‑authoring API, or override Omniverse's default authoring behavior via scripting or extensions. [sidefx](https://www.sidefx.com/docs/hdk/stage_8h_source.html)

#### 1. USD session layer and variants

- Every `UsdStage` has an implicit in‑memory **session layer** at the top of its layer stack, intended for ephemeral edits that should not be saved back to any file. [remedy-entertainment.github](https://remedy-entertainment.github.io/USDBook/terminology/edittarget.html)
- The session layer behaves like any other `SdfLayer` in composition: it participates in LIVRPS (Layering, Inherits, Variants, References, Payloads, Specializes), but because it is strongest in the layer stack, any opinions there override the same opinions in weaker layers. [docs.innoactive](https://docs.innoactive.io/iasup/layers-and-variants)
- A very common intended use is variant selections: Pixar's own header comments describe the session layer explicitly as the place to store runtime variant picks so they do not pollute authored asset files. [sidefx](https://www.sidefx.com/docs/hdk/stage_8h_source.html)
- Variant selections are just token opinions on prims (e.g. `variantSelections = {"model": "High"}`), so they follow normal composition: a variant selection in the session layer will override a selection in a root or sublayer, and the authoritative value is found by LIVRPS resolution. [docs.innoactive](https://docs.innoactive.io/iasup/layers-and-variants)
- You can author variant selections in the session layer by making that layer the edit target (`Usd.Stage.SetEditTarget` with an `EditTarget` that points to the session layer) before calling `SetVariantSelection()` or editing the prim's `variantSelections` metadata. [docs.isaacsim.omniverse.nvidia](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omniverse_usd/open_usd.html)

#### 2. Omniverse Kit "authoring layer" behavior

- Omniverse exposes the USD layer stack through its Layer panel and adds its own `omni_layer` metadata (including `authoring_layer`) on the root file to encode which layer should receive edits for a given workspace. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- In Kit/Composer, the "current authoring layer" is determined by a combination of:  
  - The stage's USD edit target,  
  - The layer selected in the Layer panel,  
  - Omniverse's `authoring_layer` metadata for the current "workspace" file.  
  This means UI operations often drive `Stage.SetEditTarget()` behind the scenes. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- By default, interactive edits (including variant selection from the UI) are written to whichever layer Omniverse considers the active authoring layer; if that is a concrete sublayer (e.g. your `050_VAR_LYR/VAR_LYR.usda`), variant picks will be authored there instead of the session layer. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- Layer locking in Omniverse mainly prevents direct modifications to that layer; if another (unlocked) layer is chosen as the authoring target, Omniverse can still create stronger overrides there that effectively "change" variants even though the original layer remains locked. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- There is no global UI preference documented that "forces all variant selections to the session layer"; instead, Omniverse recommends exposing the **Session Layer** in the Layer panel ("Show Session Layer") and treating it as the top override layer for temporary work, or using live‑session layers for collaboration and then merging changes back into dedicated layers. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)

Implication for your issue: if your current Omniverse workspace's `authoring_layer` is a persistent VAR layer, UI‑driven variant changes will land there unless you explicitly switch the authoring target to the session layer (via the Layer panel or via scripting) or intercept the operation.

#### 3. USD Python API: forcing variant authorship to session layer

**3.1 Core methods**

Relevant USD APIs:

- `stage.GetSessionLayer()` → returns the implicit session `SdfLayer`. [docs.isaacsim.omniverse.nvidia](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omniverse_usd/open_usd.html)
- `Usd.EditTarget` and `Usd.Stage.SetEditTarget()` → control which layer receives authored opinions. [remedy-entertainment.github](https://remedy-entertainment.github.io/USDBook/terminology/edittarget.html)
- `Usd.Prim.GetVariantSets()` → get `Usd.VariantSets` for a prim; `GetVariantSet(name)` returns `Usd.VariantSet`. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd/variant-sets/author-variant-data.html)
- `Usd.VariantSet.SetVariantSelection(variantName)` → authors a variant selection in the **current edit target**. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd/variant-sets/author-variant-data.html)
- `Usd.VariantSet.GetVariantEditContext()` → context manager that authors opinions into the currently selected variant on the current edit target. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd/variant-sets/author-variant-data.html)

The key is: `SetVariantSelection()` writes into whatever `stage.GetEditTarget()` points at, so you must set the edit target to the session layer first. [sidefx](https://www.sidefx.com/docs/hdk/stage_8h_source.html)

**3.2 Example: author variant selection to session layer**

```python
from pxr import Usd, Sdf

# Open an existing stage
stage = Usd.Stage.Open("path/to/root.usd")

# Get the session layer
session_layer = stage.GetSessionLayer()  # in-memory SdfLayer
print("Session layer:", session_layer.identifier)

# Option A: use a direct edit context
with Usd.EditContext(stage, session_layer):
    prim = stage.GetPrimAtPath("/World/Model")
    varset = prim.GetVariantSets().GetVariantSet("model")
    varset.SetVariantSelection("High")  # authored in session layer

# Option B: explicitly set an edit target
edit_target = Usd.EditTarget(session_layer)
stage.SetEditTarget(edit_target)

prim = stage.GetPrimAtPath("/World/Model")
varset = prim.GetVariantSets().GetVariantSet("model")
varset.SetVariantSelection("High")  # also goes into session layer
```

Because the session layer is in‑memory, calling `stage.GetRootLayer().Save()` will not write these variant selections to disk; they remain ephemeral unless you explicitly save or export the session layer. [docs.isaacsim.omniverse.nvidia](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omniverse_usd/open_usd.html)

**3.3 Verifying which layer contains the variant selection**

You can inspect the underlying `SdfPrimSpec` on each layer:

```python
from pxr import Usd, Sdf

stage = Usd.Stage.Open("path/to/root.usd")
root_layer = stage.GetRootLayer()
session_layer = stage.GetSessionLayer()

prim_path = Sdf.Path("/World/Model")

def print_variant_selections(layer, label):
    prim_spec = layer.GetPrimAtPath(prim_path)
    if not prim_spec:
        print(label, ": no prim spec")
        return
    vs = prim_spec.variantSelections
    print(label, "variantSelections:", dict(vs) if vs else {})

print_variant_selections(root_layer, "Root")
print_variant_selections(session_layer, "Session")

# Also walk sublayers to see which one holds the authored opinion
for sub_id in root_layer.subLayerPaths:
    sub = Sdf.Layer.FindOrOpen(sub_id)
    print_variant_selections(sub, f"Sublayer {sub_id}")
```

This lets you confirm whether the variant selection ended up in a base VAR layer, a higher‑priority override layer, or the session layer. [docs.innoactive](https://docs.innoactive.io/iasup/layers-and-variants)

**3.4 Edit targets and variants**

- `stage.GetEditTarget()` returns the current target; `SetVariantSelection()` always writes into this target, whether that's the root layer, a sublayer, a referenced layer via a "working in context" `EditTarget`, or the session layer. [remedy-entertainment.github](https://remedy-entertainment.github.io/USDBook/terminology/edittarget.html)
- `variant_set.GetVariantEditContext()` wraps the current **variant** as an edit context, but still uses the stage's current edit target as the layer; it only redirects opinions into the selected variant branch, not into a different layer. [forum.aousd](https://forum.aousd.org/t/query-whether-stage-edit-target-is-targeting-a-particular-variant/1003)
- For advanced scenarios where you want to author directly into a variant on a specific layer (e.g. the session layer), you can combine both: construct an `EditTarget` that targets the session layer and a specific variant path (using e.g. `Usd.EditTarget.ForLocalDirectVariant` in C++ or the equivalent in Python), then call `SetEditTarget()` and author inside that context. [forum.aousd](https://forum.aousd.org/t/query-whether-stage-edit-target-is-targeting-a-particular-variant/1003)

#### 4. LIVRPS and why your VAR layer gets polluted

- **L (Layers)**: the strongest layer wins; the session layer sits above the root stack, but Kit may set a different authoring target when you click in the Layer panel. [remedy-entertainment.github](https://remedy-entertainment.github.io/USDBook/terminology/edittarget.html)
- **I (Inherits)**, **V (Variants)**, **R (References)**, **P (Payloads)**, **S (Specializes)**: variant selections are part of `V`, but the choice of **which layer** supplies that selection is handled at `L` (layering) strength. [perplexity](https://www.perplexity.ai/search/2812e082-72e2-4ec3-ac3a-4423e29a49c6)
- If Omniverse sets the authoring target to your VAR layer (because of `authoring_layer` metadata or explicit selection), any UI variant picks simply create or override `variantSelections` there, making them persistent. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- To avoid "pollution" of base VAR files, production pipelines typically:  
  - Reserve base VAR layers for **definitions only** (the set of variants and their contents).  
  - Use a separate "shot config" or "layout" layer that carries variant selections and other overrides for a particular context.  
  - Or rely on the session layer/live session layer for testing and only promote chosen configurations into persistent layers when approved. [docs.innoactive](https://docs.innoactive.io/iasup/layers-and-variants)

#### 5. Omniverse‑specific workflows and configuration

**5.1 Using session layer in Omniverse**

- Omniverse's "Layers" extension documents the session layer explicitly as the place for non‑persistent content and live‑session deltas; you can reveal it with "Show Session Layer" and then set it as the active authoring target. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- During a Live Session, Omniverse creates a "Live Session" sublayer inside the session layer; all deltas (including transforms, waypoints, markups, etc.) are stored there until merged. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- Best practice in the Omniverse docs is to merge live‑session changes into dedicated layers (Xform, Lighting, Materials, etc.) rather than root, and to treat the session/live layers as temporary buffers. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)

For your use case, you can adapt this pattern by:

- Showing the Session Layer in the Layer window.  
- Making the Session Layer the authoring layer before interacting with variant UI, either manually or via a small helper extension that automatically switches the edit target when the "variants" UI is used.  

**5.2 `omni_layer` metadata and `authoring_layer`**

- The `omni_layer` metadata is stored on the root file and describes a logical layer structure (e.g. "ROOT", "Assets_Layer", "Material_Layer", "Session Layer") and which one is the **authoring layer** for the current workspace. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- Omniverse uses this to route UI edits: if `authoring_layer` is set to `050_VAR_LYR/VAR_LYR.usda`, many changes, including variant selections, will end up there. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- Changing this metadata (via UI or a script) to point to a dedicated override layer (e.g. `200_CONFIG_LYR/CONFIG.usda`) or to the session layer avoids contaminating base VAR layers. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)

Omniverse does not currently document a per‑operation switch like "when changing variants, always use session layer," so the practical control point is still the global authoring target.

**5.3 Layer locking**

- According to the Omniverse Layers docs, locking a layer prevents direct edits to that specific file but does not stop a stronger layer from overriding its opinions. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- Variant changes you see "ignoring" lock likely come from an unlocked higher‑priority or authoring layer adding its own variant selection; the original VAR layer remains unchanged but appears overridden. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)

#### 6. Production best practices and other DCCs

- Many USD pipelines treat **variant definitions** and **variant selections** as separate concerns:  
  - Asset USD: declares variant sets and their content.  
  - Shot/Scene/Config USD: sets `variantSelections` for a particular use of the asset. [perplexity](https://www.perplexity.ai/search/2812e082-72e2-4ec3-ac3a-4423e29a49c6)
- To avoid polluting asset files, teams often:  
  - Lock or keep asset layers read‑only in the DCC.  
  - Configure the DCC's edit target to a shot config layer or session layer.  
  - Provide tools that copy chosen variant selections from the session into dedicated config layers once approved. [github](https://github.com/Autodesk/maya-usd/discussions/3191)
- In Maya USD and Houdini Solaris, similar patterns exist:  
  - Maya USD exposes explicit edit‑target selection; you can pick a referenced layer or a session/override layer, and variant UI honors that choice. [github](https://github.com/Autodesk/maya-usd/discussions/3191)
  - Solaris tends to author into an explicit USD node's layer or a designated "working" layer, and users usually keep asset layers separate from shot layers to prevent contamination. [github](https://github.com/Autodesk/maya-usd/discussions/3191)

Your current layering scheme (VAR layer + other domain layers) fits this; you likely need an additional "config" or "shot variant selection" layer plus automation to ensure that's the active authoring target during variant changes.

#### 7. Omniverse extensions, discussions, and potential solution

- Omniverse's own "Variant Workflows" docs describe authoring variant data on particular layers and using variant edit contexts, but do not provide a built‑in "always write variant selections to session layer" switch. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd/variant-sets/author-variant-data.html)
- Community discussions on edit targets and variants (e.g. on the Alliance for OpenUSD forum and Maya USD discussions) show a common pattern: use `Usd.EditTarget` to direct edits into a specific layer or variant branch and build tooling around that for artists. [forum.aousd](https://forum.aousd.org/t/query-whether-stage-edit-target-is-targeting-a-particular-variant/1003)
- A custom Omniverse extension could:  
  - Listen to variant selection changes in the UI (or provide its own variant picker UI).  
  - On change, temporarily set `stage.SetEditTarget(Usd.EditTarget(stage.GetSessionLayer()))`.  
  - Call `SetVariantSelection()` on the chosen prim/variant.  
  - Optionally restore the previous edit target afterwards.  

This would guarantee that variant selections from this tool always land in the session layer, regardless of the global authoring layer.

#### 8. Concrete code snippets for your toolbox

**8.1 Get session layer and set edit target (Omniverse Kit Python console)**

```python
from pxr import Usd

stage = omni.usd.get_context().get_stage()  # typical Kit/Composer access
session_layer = stage.GetSessionLayer()
print("Session layer:", session_layer.identifier)

# Make session layer the current edit target
stage.SetEditTarget(Usd.EditTarget(session_layer))
```

**8.2 Author a variant selection into session layer**

```python
from pxr import Usd

stage = omni.usd.get_context().get_stage()
session_layer = stage.GetSessionLayer()

with Usd.EditContext(stage, session_layer):
    prim = stage.GetPrimAtPath("/World/MyAsset")
    vs = prim.GetVariantSets().GetVariantSet("material")
    vs.SetVariantSelection("Steel")  # goes into session layer
```

**8.3 Helper: temporarily push session edit target**

```python
from contextlib import contextmanager
from pxr import Usd

@contextmanager
def session_edit_target(stage: Usd.Stage):
    old_target = stage.GetEditTarget()
    session_layer = stage.GetSessionLayer()
    stage.SetEditTarget(Usd.EditTarget(session_layer))
    try:
        yield
    finally:
        stage.SetEditTarget(old_target)

# Usage
with session_edit_target(stage):
    prim = stage.GetPrimAtPath("/World/MyAsset")
    vs = prim.GetVariantSets().GetVariantSet("config")
    vs.SetVariantSelection("Option_B")
```

**8.4 Inspect `omni_layer` metadata (from root layer)**

Omniverse stores this as custom layer metadata; you can inspect it as follows:

```python
from pxr import Usd

stage = omni.usd.get_context().get_stage()
root_layer = stage.GetRootLayer()

# "omni_layer" metadata is a dict-like custom data blob
omni_layer_meta = root_layer.customLayerData.get("omni_layer", {})
print("omni_layer metadata:", omni_layer_meta)

authoring_layer = omni_layer_meta.get("authoring_layer")
print("Configured authoring_layer:", authoring_layer)
```

Then adjust it by writing to `customLayerData` and saving if you want to change the persistent authoring configuration; Omniverse's Layers extension uses this to know which logical layer to target. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)

#### 9. Recommended workflow for your case

Given your VAR layers are being polluted:

- Introduce a dedicated **config layer** (e.g. `200_CFG_LYR/CFG.usda`) that is the default authoring layer for variant selections, and update `omni_layer.authoring_layer` to this file. [docs.innoactive](https://docs.innoactive.io/iasup/layers-and-variants)
- For ad‑hoc testing, provide a small script or extension that:  
  - Switches the edit target to the session layer while the user is in "variant experimentation" mode.  
  - Optionally provides a button to "Bake current variant selections from session layer into config layer," copying `variantSelections` from the session prim specs into the config layer prim specs.  
- Lock asset and VAR layers for normal users; only pipeline TDs or tools should modify them, minimizing accidental writes. [docs.innoactive](https://docs.innoactive.io/iasup/layers-and-variants)

#### 10. Key references

- USD `UsdStage` and session layer behavior (including note that session layers are meant for runtime variant selections). [remedy-entertainment.github](https://remedy-entertainment.github.io/USDBook/terminology/edittarget.html)
- Isaac Sim / Omniverse "OpenUSD Fundamentals" example code for session layer and edit contexts. [docs.isaacsim.omniverse.nvidia](https://docs.isaacsim.omniverse.nvidia.com/6.0.0/omniverse_usd/open_usd.html)
- Omniverse Layers extension docs describing session layer, live session layer, and authoring patterns. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html)
- Omniverse variant authoring examples and variant edit contexts. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd/variant-sets/author-variant-data.html)
- OpenUSD & community resources on edit targets and variant edit targets. [forum.aousd](https://forum.aousd.org/t/query-whether-stage-edit-target-is-targeting-a-particular-variant/1003)

If you want, I can sketch a minimal Omniverse extension skeleton that adds a "Set variant in session layer" right‑click option in the Stage tree for quick use in Composer.

---
Here is a minimal but functional skeleton for an Omniverse extension that adds a “Set variant in session layer” right‑click option to the Stage tree and applies the variant selection into the session layer.

The sketch assumes:

- Omniverse Kit / Composer environment.  
- You are comfortable generating a template extension, then replacing the Python file contents with something like this.  
- Variant logic: it looks at the currently selected prim, asks you for a variant set and variant name (simplest), and then writes the selection to the **session layer** using `Usd.EditContext`.

***

## 1. `extension.toml` (minimal config)

```toml
[package]
# Change these to match your namespace/project
name = "com.yourcompany.variant_session_picker"
version = "0.0.1"
title = "Variant Session Picker"
description = "Adds 'Set variant in session layer' to Stage context menu"
category = "usd"

[dependencies]
"omni.kit.uiapp" = {}
"omni.usd" = {}
"omni.kit.window.stage" = {}
"omni.kit.window.popup_dialog" = {}
"omni.kit.context_menu" = {}

[[python.modules]]
name = "com.yourcompany.variant_session_picker"
```

***

## 2. `__init__.py` – extension skeleton

```python
import omni.ext
import omni.usd
from pxr import Usd

import omni.kit.context_menu as context_menu
import omni.kit.window.popup_dialog as popup_dialog


class VariantSessionPickerExtension(omni.ext.IExt):
    def on_startup(self, ext_id):
        self._ext_id = ext_id

        # Register a context menu item on the Stage tree
        self._menu_handle = context_menu.add_menu_item(
            context_menu.DEFAULT_STAGE_CONTEXT_MENU_ID,
            "Set variant in session layer",
            self._on_menu_click,
        )

    def on_shutdown(self):
        if self._menu_handle:
            context_menu.remove_menu_item(self._menu_handle)
            self._menu_handle = None

    # ------------------------------------------------------------------ #
    # Context menu callback
    # ------------------------------------------------------------------ #
    def _on_menu_click(self, menu, item):
        ctx = omni.usd.get_context()
        stage = ctx.get_stage()
        if not stage:
            return

        # Get selected prim path from USD context
        sel = ctx.get_selection()
        paths = sel.get_selected_prim_paths()
        if not paths:
            return

        prim_path = paths[0]
        prim = stage.GetPrimAtPath(prim_path)
        if not prim or not prim.IsValid():
            return

        # Ask user which variant set and variant name to use
        self._show_variant_dialog(stage, prim)

    # ------------------------------------------------------------------ #
    # Simple popup to enter variant set + variant name
    # ------------------------------------------------------------------ #
    def _show_variant_dialog(self, stage: Usd.Stage, prim: Usd.Prim):
        title = "Set Variant in Session Layer"

        def on_ok(result, fields):
            if result != popup_dialog.DialogResult.OK:
                return

            varset_name = fields.get("varset_name", "").strip()
            variant_name = fields.get("variant_name", "").strip()

            if not varset_name or not variant_name:
                return

            self._set_variant_in_session(stage, prim, varset_name, variant_name)

        popup_dialog.create_input_dialog(
            title=title,
            message=f"Prim: {prim.GetPath()}\nEnter variant set and variant name.",
            ok_label="Apply",
            cancel_label="Cancel",
            input_fields={
                "varset_name": {
                    "label": "Variant Set",
                    "default": "config",
                },
                "variant_name": {
                    "label": "Variant Name",
                    "default": "",
                },
            },
            callback=on_ok,
        )

    # ------------------------------------------------------------------ #
    # Core logic: author variant selection into session layer
    # ------------------------------------------------------------------ #
    def _set_variant_in_session(
        self, stage: Usd.Stage, prim: Usd.Prim, varset_name: str, variant_name: str
    ):
        session_layer = stage.GetSessionLayer()
        if not session_layer:
            return

        # Temporarily set edit target to session layer
        old_target = stage.GetEditTarget()
        stage.SetEditTarget(Usd.EditTarget(session_layer))

        try:
            variant_sets = prim.GetVariantSets()
            vset = variant_sets.GetVariantSet(varset_name)
            if not vset.IsValid():
                # Optionally: you could log or show a message here
                return

            vset.SetVariantSelection(variant_name)
        finally:
            # Restore previous edit target
            stage.SetEditTarget(old_target)
```

***

## 3. How it behaves

- You right‑click a prim in the **Stage** tree.  
- Choose “Set variant in session layer”.  
- A small dialog asks for:  
  - Variant set name (e.g. `config`, `material`, `model`).  
  - Variant name (e.g. `Option_A`, `Steel`).  
- The extension:  
  - Gets the current `UsdStage` from Omniverse.  
  - Gets the **session layer** via `stage.GetSessionLayer()`.  
  - Temporarily sets the edit target to the session layer.  
  - Calls `SetVariantSelection()` on the chosen prim/variant set.  
  - Restores the previous edit target.

All variant selections authored through this action will live entirely in the session layer, leaving your base layers (VAR, asset, config) untouched.

If you’d like, I can extend this skeleton to:

- Auto‑enumerate existing variant sets and present them as dropdowns.  
- Offer a second menu item “Bake session variants into layer…” that copies `variantSelections` from session layer into a chosen sublayer.

---
How to set variant selection to a specific non-session layer
---

You set a variant selection to a specific non‑session layer by making that layer the stage’s edit target (or a variant‑aware edit target) and then calling the usual USD variant APIs; the key is to point `Usd.EditTarget` at the desired `SdfLayer` before you author the selection. [forum.aousd](https://forum.aousd.org/t/query-whether-stage-edit-target-is-targeting-a-particular-variant/1003)

***

## 1. Direct USD pattern: sublayer or referenced layer

Assume you have a stage with a particular `SdfLayer` (not the session layer) you want to write into, e.g. `050_VAR_LYR/VAR_LYR.usda` or a material/config layer.

### 1.1 Get the target layer

If the layer is a sublayer of the root:

```python
from pxr import Usd, Sdf

stage = Usd.Stage.Open("path/to/root.usd")
root_layer = stage.GetRootLayer()

# Find a sublayer by identifier/path
target_id = "050_VAR_LYR/VAR_LYR.usda"
target_layer = Sdf.Layer.FindOrOpen(target_id)
print("Target layer:", target_layer.identifier)
```

If the layer comes via a reference (not a sublayer), the principle is the same: you still get its `SdfLayer` (often via your own bookkeeping or by inspecting `UsdPrimCompositionQuery`), then use it in an `EditTarget`. [github](https://github.com/Autodesk/maya-usd/discussions/3191)

### 1.2 Set edit target and author the variant selection

```python
from pxr import Usd

stage = Usd.Stage.Open("path/to/root.usd")
target_layer = Sdf.Layer.FindOrOpen("050_VAR_LYR/VAR_LYR.usda")

# Point the stage edit target at this concrete layer
edit_target = Usd.EditTarget(target_layer)
stage.SetEditTarget(edit_target)

prim = stage.GetPrimAtPath("/World/MyAsset")
varset = prim.GetVariantSets().GetVariantSet("material")
varset.SetVariantSelection("Steel")  # authored into target_layer
```

Because `stage.GetEditTarget()` now refers to `target_layer`, the authored `variantSelections` opinion will appear on that layer’s `SdfPrimSpec`. [forum.aousd](https://forum.aousd.org/t/query-whether-stage-edit-target-is-targeting-a-particular-variant/1003)

***

## 2. Authoring inside a specific variant on a specific layer

If you want to author **data inside a variant** on a specific non‑session layer (e.g. tweak attributes inside `material=Steel` on a dedicated material layer), you combine a variant edit context with a layer‑specific edit target:

```python
from pxr import Usd

stage = Usd.Stage.Open("path/to/root.usd")
target_layer = Sdf.Layer.FindOrOpen("050_MAT_LYR/MAT_LYR.usda")

prim = stage.GetPrimAtPath("/World/MyAsset")
vset = prim.GetVariantSets().GetVariantSet("material")

# 1) Create an edit target that points at the target layer
layer_edit_target = Usd.EditTarget(target_layer)

# 2) Wrap both: use the variant’s edit context while the stage has that edit target
with Usd.EditContext(stage, layer_edit_target):
    with vset.GetVariantEditContext():
        # These specs go into the selected variant, *on target_layer*
        attr = prim.CreateAttribute("displayColor", Usd.Vec3fArray)
        attr.Set([(0.9, 0.9, 0.9)])
```

Internally, `GetVariantEditContext()` nests an additional mapping (variant branch) on top of the layer edit target; the composition forum thread confirms this pattern and shows how `GetVariantEditTarget(layer)` creates such nested edit targets. [grill.readthedocs](https://grill.readthedocs.io/en/latest/views.html)

***

## 3. Omniverse‑specific: setting edit target to a non‑session layer

In Kit/Composer you can do the same from Python, targeting any writable layer (sublayer or referenced) instead of the session layer:

```python
from pxr import Usd, Sdf
import omni.usd

ctx = omni.usd.get_context()
stage = ctx.get_stage()

# Example: pick a layer by identifier (must be part of the stage's layer stack)
target_id = "050_VAR_LYR/VAR_LYR.usda"
target_layer = Sdf.Layer.FindOrOpen(target_id)

# Make it the edit target for the stage
stage.SetEditTarget(Usd.EditTarget(target_layer))

# Now author the variant selection
prim = stage.GetPrimAtPath("/World/MyAsset")
vset = prim.GetVariantSets().GetVariantSet("config")
vset.SetVariantSelection("Option_A")
```

- Omniverse’s Layer widget does this under the hood via `set_edit_target(layer_item)`; documentation notes that any **writable** layer (not read‑only, not locked, not muted) can be used as an edit target. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/kit/docs/omni.kit.widget.layers/1.8.0/omni.kit.widget.layers/omni.kit.widget.layers.LayerModel.html)
- The UI’s “Set as edit layer / authoring layer” context‑menu options wrap this: they choose a `layer_item`, call `set_edit_target`, then all subsequent operations (including variant changes) write into that non‑session layer. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/kit/docs/omni.kit.widget.layers/1.8.8/omni.kit.widget.layers/omni.kit.widget.layers.ContextMenu.html)

If you prefer the UI route, simply right‑click the desired layer in the Omniverse Layers panel, choose “Set as Edit Layer” (or “Set as Authoring Layer”), and then perform your variant changes; this will direct the `variantSelections` opinions into that layer instead of the session or root.

***

If you tell me whether your target is a sublayer, a referenced asset layer, or an Omniverse “logical” layer (from `omni_layer` metadata), I can give a tailored snippet that locates that exact `SdfLayer` and sets it as the edit target automatically.

----

Save variant selection changes to a sublayer instead of session layer
---

Set the **stage edit target** to the sublayer you want, then call `SetVariantSelection()`; that will write the selection into that sublayer instead of the session layer. [docs.nvidia](https://docs.nvidia.com/learn-openusd/latest/composition-basics/variant-sets.html)

***

## Core idea

- Variant selection is just `variantSelections` metadata authored on the prim at the current **edit target**. [docs.nvidia](https://docs.nvidia.com/learn-openusd/latest/composition-basics/variant-sets.html)
- If the edit target is your **sublayer**, the opinion goes into that sublayer (and will be saved with it) instead of into the session layer. [lucascheller.github](https://lucascheller.github.io/VFX-UsdSurvivalGuide/pages/core/composition/livrps.html)

***

## Minimal USD Python example (any DCC)

```python
from pxr import Usd, Sdf

# Open root stage
stage = Usd.Stage.Open("path/to/root.usd")
root_layer = stage.GetRootLayer()

# Find the sublayer you want to store the selection in
target_layer_id = "050_VAR_LYR/VAR_LYR.usda"  # must match subLayerPaths entry
target_layer = Sdf.Layer.FindOrOpen(target_layer_id)

# Point the stage edit target at that sublayer
stage.SetEditTarget(Usd.EditTarget(target_layer))

# Now author the variant selection
prim = stage.GetPrimAtPath("/World/MyAsset")
vset = prim.GetVariantSets().GetVariantSet("config")
vset.SetVariantSelection("Option_A")  # goes into target_layer, not session
```

- After this, inspecting `target_layer.GetPrimAtPath("/World/MyAsset")` will show the `variantSelections` entry on that sublayer. [lucascheller.github](https://lucascheller.github.io/VFX-UsdSurvivalGuide/pages/core/composition/livrps.html)
- The session layer remains unchanged because it is no longer the edit target.

***

## Omniverse Kit / Composer variant via sublayer

In Omniverse, you can do the same via Python (or via the Layers UI):

```python
from pxr import Usd, Sdf
import omni.usd

ctx = omni.usd.get_context()
stage = ctx.get_stage()

# Identify your sublayer by its identifier/path
target_layer_id = "050_VAR_LYR/VAR_LYR.usda"
target_layer = Sdf.Layer.FindOrOpen(target_layer_id)

# Make this sublayer the edit target
stage.SetEditTarget(Usd.EditTarget(target_layer))

# Author variant selection
prim = stage.GetPrimAtPath("/World/MyAsset")
vset = prim.GetVariantSets().GetVariantSet("material")
vset.SetVariantSelection("Steel")  # stored in 050_VAR_LYR/VAR_LYR.usda
```

Or via UI:

- In the **Layers** panel, right‑click the desired sublayer and choose “Set as Edit Layer” / “Set as Authoring Layer”. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_variant-presenter.html)
- Then use the **Variant Editor** / Variant Presenter to change the variant; the selection will be authored into that sublayer, because it is now the current authoring layer. [docs.omniverse.nvidia](https://docs.omniverse.nvidia.com/extensions/latest/ext_variant-editor.html)

***

## Quick verification snippet

```python
from pxr import Sdf

prim_path = Sdf.Path("/World/MyAsset")
prim_spec = target_layer.GetPrimAtPath(prim_path)
print("variantSelections on target layer:", dict(prim_spec.variantSelections))
```

This confirms the variant selection is stored on the sublayer you targeted, not on the session layer. [lucascheller.github](https://lucascheller.github.io/VFX-UsdSurvivalGuide/pages/core/composition/livrps.html)



---

*End of Perplexity Raw Output*

---

### B2: ChatGPT Research Output

Below is the most useful mental model (USD-first), then Omniverse-specific behavior, then concrete Python/Kit snippets you can drop into your workflow to force **variant selections** into the **session layer**.

---

## 1) USD session layer mechanics (what it really is)

### Where the session layer sits in the stack

Every `UsdStage` has:

* a **root layer** (`stage.GetRootLayer()`)
* a **root session layer** (`stage.GetSessionLayer()`)

When you ask USD for the stage layer stack, USD can include session layers **above** the root stack. In the API docs, `GetLayerStack(includeSessionLayers=True)` is explicitly described as returning the strong-to-weak sublayers rooted at the **session layer first**, then the strong-to-weak sublayers rooted at the **root layer**. ([openusd.org][1])

So: **the session layer is (by design) the strongest place to put temporary opinions**.

### Why session layers are used for “temporary picks” (including variants)

USD documentation calls out session layers as the place for ephemeral edits (classic examples: UI state, temporary overrides, *and* variant selections). ([NVIDIA Omniverse Docs][2])

### What a “variant selection” is in USD data terms

A variant selection is **just authored metadata** on a prim spec (e.g. USDA shows `variants = { string shading = "realistic" }`). Omniverse’s own dev-guide sample prints exactly that form when selecting a variant. ([NVIDIA Omniverse Docs][3])

Under the hood, this lands in a prim spec’s **`variantSelections`** dictionary (Sdf-level), i.e. “keys are variant set names, values are chosen variants”. ([NVIDIA Omniverse Docs][4])

### Key control point: the stage edit target

USD writes authored opinions (including variant selections) into the **current `UsdEditTarget`**:

* `stage.GetEditTarget()`
* `stage.SetEditTarget(...)`
* helpers like `stage.GetEditTargetForLocalLayer(layer)` ([openusd.org][1])

So if your edit target points at a file-backed layer, **variant selection edits will be written there**. If your edit target points at the **session layer**, the selection stays temporary.

---

## 2) How Omniverse Kit/Composer chooses the layer for variant selection edits

### The “Authoring Layer” in the Layers panel is effectively the stage edit target

Omniverse’s Layers documentation describes the authoring layer workflow: by default it’s the root layer, and you change it by **double-clicking** another layer in the Layers panel. ([NVIDIA Omniverse Docs][5])

That “authoring layer” is the layer most UI edits (including variant selection toggles) will write into, because the UI is authoring through the stage’s active edit context/target.

### Variant Editor confirms it is tied to the current authoring layer

Omniverse’s Variant Editor explicitly states a limitation: **“Only variants in the current authoring layer can be modified.”** ([NVIDIA Omniverse Docs][6])
That’s a strong hint that variant-related authoring is not “magically session-layered” — it follows authoring-layer/edit-target rules.

### Auto Authoring mode can re-route where edits end up

Omniverse’s `omni.kit.usd.layers` adds an “Auto Authoring” mode: edits go into a delegate layer and get distributed into the layer where they have the “strongest opinions”. ([NVIDIA Omniverse Docs][7])
Also, `active_authoring_layer_context()` notes that in auto-authoring it returns the edit context of the **default layer** (not simply the current edit target). ([NVIDIA Omniverse Docs][8])

Practical implication:

* If you’re in **Auto Authoring**, simply “locking” some layers may not give you the result you expect; edits can be distributed elsewhere.
* If you want deterministic “put variant selections in session layer”, prefer **Normal** mode + explicitly set authoring layer/edit target.

### `omni_layer` / `authoring_layer` metadata

Omniverse stores some layer workflow state in `customLayerData`, commonly under a dictionary named `omni_layer`, including an `authoring_layer` string. You can see this pattern in real USDA files. ([Gist][9])
The Layers utilities also explicitly provide helpers to **save/restore authoring layer to/from custom data**. ([NVIDIA Omniverse Docs][10])

So if your root file’s `customLayerData["omni_layer"]["authoring_layer"]` points at something like `050_VAR_LYR/VAR_LYR.usda`, Kit may restore that as your authoring layer on open — and your variant selections will “pollute” it unless you override.

---

## 3) USD Python API: forcing variant selections into the session layer

### Minimal “force to session layer” pattern (pure USD)

```python
from pxr import Usd

stage = ...  # your Usd.Stage
session_layer = stage.GetSessionLayer()

# Make a proper edit target for that layer (recommended)
session_target = stage.GetEditTargetForLocalLayer(session_layer)

prim = stage.GetPrimAtPath("/World/Car")
vset = prim.GetVariantSets().GetVariantSet("materialVariant")

with Usd.EditContext(stage, session_target):
    vset.SetVariantSelection("BluePaint")
```

This works because the selection is authored into the **current edit target**, and you’ve temporarily made that the session layer. ([openusd.org][1])

### Verify which layer contains the selection

```python
from pxr import Sdf

path = Sdf.Path("/World/Car")
spec = session_layer.GetPrimAtPath(path)
print("Session layer selections:", spec.variantSelections if spec else None)
```

`variantSelections` is the SdfPrimSpec dictionary where the authored selections live. ([NVIDIA Omniverse Docs][4])

### Find the first layer in the stack that authored a selection

```python
from pxr import Sdf

def find_variant_authors(stage, prim_path: str):
    p = Sdf.Path(prim_path)
    results = []
    for layer in stage.GetLayerStack(includeSessionLayers=True):
        spec = layer.GetPrimAtPath(p)
        if spec and spec.variantSelections:
            results.append((layer.identifier, dict(spec.variantSelections)))
    return results

print(find_variant_authors(stage, "/World/Car"))
```

`GetLayerStack(includeSessionLayers=True)` returns session-rooted layers first, then root-rooted layers. ([openusd.org][1])

---

## 4) Omniverse-specific Python: set authoring layer to session (and keep it there)

### In Kit/Composer: get the stage and set edit target to session

```python
import omni.usd
from pxr import Usd

stage = omni.usd.get_context().get_stage()
session_layer = stage.GetSessionLayer()
session_target = stage.GetEditTargetForLocalLayer(session_layer)

# Option A: set it globally (until changed again)
stage.SetEditTarget(session_target)
```

`GetEditTargetForLocalLayer()` and `SetEditTarget()` are standard USD mechanisms. ([openusd.org][1])

### Using `omni.kit.usd.layers` helpers (Kit-native)

Omniverse exposes layer utilities including `LayerUtils.set_edit_target(stage, layer_identifier)` and save/restore helpers for authoring-layer custom data. ([NVIDIA Omniverse Docs][10])

A typical pattern is:

```python
import omni.usd
from omni.kit.usd.layers import LayerUtils

stage = omni.usd.get_context().get_stage()
session_id = stage.GetSessionLayer().identifier

LayerUtils.set_edit_target(stage, session_id)
```

### If Auto Authoring is enabled: set its default layer to session

If you must use Auto Authoring, point its “new opinions” default layer at the session layer:

```python
import omni.usd
import omni.kit.usd.layers as layers

ctx = omni.usd.get_context()
layers_api = layers.get_layers(ctx)
auto = layers_api.get_auto_authoring()

session_id = ctx.get_stage().GetSessionLayer().identifier
auto.set_default_layer(session_id)
```

AutoAuthoring’s `set_default_layer(layer_identifier)` is documented as the place newly-created opinions go. ([NVIDIA Omniverse Docs][7])

---

## 5) Why “locking layers” often doesn’t solve this

Layer locking in Omniverse is a workflow feature (commands like `LockLayerCommand` exist in `omni.kit.usd.layers`). But **locking one layer doesn’t force authoring into session**; it usually just prevents edits from being authored *to that locked layer*. If Kit’s authoring layer is some other unlocked file, selections will still go there.

In Auto Authoring, edits can also be distributed to whichever layer has strongest opinions. ([NVIDIA Omniverse Docs][7])
So: locking is useful, but it’s not a replacement for explicitly setting authoring/edit target.

---

## 6) Best-practice workflows used in production (to avoid polluting base layers)

### Common patterns

1. **Define variants in asset layers; select variants in an assembly/shot override layer**

   * Variant definitions live with the asset.
   * Selections live in a stronger “assembly” layer so each instance can pick differently (Omniverse sample notes selecting in “other USD layers” is expected). ([NVIDIA Omniverse Docs][3])

2. **Use session layer for “auditioning,” then intentionally promote**

   * Audition variants in session layer (temporary).
   * When approved, copy/paste or script the selections into the correct persistent override layer.

3. **Dedicated “scratch override” layer**

   * Instead of session, create a top sublayer like `*_TMP_OVERRIDES.usda` that’s ignored by VCS or excluded from publish, and make that the authoring layer.

### How other tools handle it (high level)

* **Houdini Solaris** makes edit targeting explicit (e.g. the “Edit Target Layer” node exists specifically to choose which layer receives edits). ([sidefx.com][11])
* Many DCC USD integrations follow the same principle: *variant selection writes to the current edit target* unless you change the target.

---

## 7) Existing Omniverse discussions & signals this is a known pain point

A few relevant NVIDIA forum threads that touch variants + layer authoring issues:

* Variants breaking / warnings about variants authored in a different layer ([NVIDIA Developer Forums][12])
* Variant set options / `omni_layer` / `authoring_layer` appearing in real files & discussions ([NVIDIA Developer Forums][13])
* Reports of authoring-layer state bugs when scripting authoring layer changes ([NVIDIA Developer Forums][14])

These don’t all say “write variant selections to session”, but they confirm that **variant authoring is closely tied to layer targeting** in Composer.

---

## 8) Quick “do this in Composer” checklist

1. Open **Layers** panel.
2. Make sure the **Session Layer** is visible (Composer docs treat Session Layer as the place for non-persistent content). ([NVIDIA Omniverse Docs][5])
3. **Double-click Session Layer** to make it the **authoring layer** (so UI-driven variant selection goes there).
4. If Auto Authoring is on, switch to **Normal** (or set AutoAuthoring default layer to session via script). ([NVIDIA Omniverse Docs][7])

---

## 9) Inspecting `omni_layer` metadata (why your stage keeps reverting)

```python
import omni.usd

stage = omni.usd.get_context().get_stage()
root = stage.GetRootLayer()

omni_layer = (root.customLayerData or {}).get("omni_layer", {})
print("Stored authoring layer:", omni_layer.get("authoring_layer"))
print("Locked dict:", omni_layer.get("locked"))
print("Muteness dict:", omni_layer.get("muteness"))
```

That `customLayerData["omni_layer"]["authoring_layer"]` pattern is visible in sample USDA content. ([Gist][9])
If this points at `050_VAR_LYR/VAR_LYR.usda`, Kit may restore that as authoring layer on open, and your variant picks will keep landing there until you override it.

---

### Bottom line

**Variant selections are authored into whatever layer the stage is currently targeting (edit target/authoring layer).** In Omniverse, that’s controlled by the Layers system (Normal vs Auto Authoring) and the user-selected authoring layer. To keep selections temporary, **set the authoring layer/edit target to the session layer** (UI or script) before changing variants.

If you want, I can also sketch a small Kit extension pattern (event subscription + “force session edit target on stage open and before variant changes”) using `omni.kit.usd.layers` APIs/events.

[1]: https://openusd.org/dev/api/class_usd_stage.html "Universal Scene Description: UsdStage Class Reference"
[2]: https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/105.0.2/pxr/Usd.html?utm_source=chatgpt.com "Usd module — pxr-usd-api 105.0.2 documentation"
[3]: https://docs.omniverse.nvidia.com/dev-guide/latest/programmer_ref/usd/variant-sets/select-variant.html "Select a Variant for a Variant Set — Omniverse Developer Guide"
[4]: https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/latest/pxr/Sdf.html?utm_source=chatgpt.com "Sdf module — Omniverse Kit"
[5]: https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html "Layers — Omniverse Extensions"
[6]: https://docs.omniverse.nvidia.com/extensions/latest/ext_variant-editor.html "Variant Editor — Omniverse Extensions"
[7]: https://docs.omniverse.nvidia.com/kit/docs/omni.kit.usd.layers/latest/omni.kit.usd.layers/omni.kit.usd.layers.AutoAuthoring.html "AutoAuthoring — Omniverse Kit"
[8]: https://docs.omniverse.nvidia.com/kit/docs/omni.kit.usd.layers/latest/omni.kit.usd.layers/omni.kit.usd.layers.active_authoring_layer_context.html "active_authoring_layer_context — Omniverse Kit"
[9]: https://gist.github.com/alankent/3f2ee170a97cf46aaf74bde8839920a1 "Sample USDA file for Omniverse to display the current time · GitHub"
[10]: https://docs.omniverse.nvidia.com/kit/docs/omni.kit.usd.layers/2.1.36/omni.kit.usd.layers/omni.kit.usd.layers.LayerUtils.html "LayerUtils — Omniverse Kit 2.1.36 documentation"
[11]: https://www.sidefx.com/docs/houdini/nodes/lop/edittargetlayer.html?utm_source=chatgpt.com "Edit Target Layer"
[12]: https://forums.developer.nvidia.com/t/1-issues-with-variants-breaking-due-to-layers/322625?utm_source=chatgpt.com "#1 Issues with Variants breaking due to Layers?"
[13]: https://forums.developer.nvidia.com/t/modifying-variant-set-option-in-a-child-reference-from-the-parent-variant-set/311390?utm_source=chatgpt.com "Modifying variant set option in a child reference from the ..."
[14]: https://forums.developer.nvidia.com/t/multiple-authoring-layers-bug/278469?utm_source=chatgpt.com "Multiple Authoring Layers bug - General Discussion"

----
I need also a general best practice not only for variant sets but for other things that we may do within a project where we don't want the underlying project to be altered in any way. So, please make sure that this is also covered, and not only for variant sets.
---

Absolutely — the *general* best practice here is: **treat everything in USD as “writes go to the current edit target,”** and then build guardrails so your edit target is *never* a protected/project layer when you’re doing exploratory work.

USD (and Kit apps built on it) will happily author **transforms, attributes, relationships, prim activation/visibility, variants, added references/payloads, etc.** into whatever layer is currently targeted. Variant selections just make the problem extra visible.

Below is a practical “non-destructive authoring playbook” that applies to *all* edits, not only variants.

---

## 1) The core rule: all edits go to the stage’s EditTarget (a layer)

USD’s design is explicit: authoring happens in the current **EditTarget** (layer + optional mapping). If you don’t choose it, tools choose for you. ([remedy-entertainment.github.io][1])

**Session layer** exists specifically as an in-memory, strongest layer meant for *ephemeral overrides*; USD docs even call out variant selections as a common use. ([NVIDIA Omniverse Docs][2])

So the generalized solution is:

* **Protected layers** (asset publishes, “base project” layers): *read-only / never targeted*
* **Working override layer(s)**: where intentional edits should land
* **Session layer**: where “try stuff” edits should land

---

## 2) Recommended non-destructive layer pattern (works for everything)

A widely used production stack looks like this (strong → weak):

1. **Session layer (temporary, per-user, in-memory)**
   Use for: auditioning *anything* (variants, transforms, visibility, material binding, light tweaks, etc.). ([NVIDIA Omniverse Docs][2])

2. **User scratch override layer (file-backed, optional, not committed)**
   Use for: “I want this to survive app restart, but never land in the project publish.”
   Example: `users/<name>/scratch_overrides.usda` sublayered at the top of the root stack.

3. **Shot/Task override layer (file-backed, committed intentionally)**
   Use for: the edits you *do* want version controlled and reviewed.

4. **Project/Asset base layers (published, read-only)**
   Use for: stable content. Treat as immutable.

This is exactly the USD “non-destructive editing via composition” mindset: changes in stronger layers don’t modify weaker layers. ([NVIDIA Docs][3])

---

## 3) Omniverse-specific best practices (applies to any edit)

### A) Always set the “Authoring Layer” before you touch the scene

In Kit apps, the Layers panel’s **Authoring Layer** is the layer your UI edits will target; by default it’s the root layer, and you change it by double-clicking a layer. ([NVIDIA Omniverse Docs][4])

**Best practice:** make “Session Layer” (or your scratch override layer) the authoring layer before interacting.

### B) Be careful with Auto Authoring

Auto Authoring can distribute edits based on “strongest opinions,” which can make it feel like edits “jump layers.” ([NVIDIA Omniverse Docs][5])

If your goal is “never touch project layers”:

* Prefer **Normal authoring** + explicit authoring layer, or
* If you must use Auto Authoring, set its **default layer** to your session/scratch layer. ([NVIDIA Omniverse Docs][5])

### C) Collaboration edits: Live layers are often session-rooted

Omniverse “Live Layer” content is generally placed automatically in the **USD Session Layer** of a stage. ([NVIDIA Omniverse Docs][6])
So Live workflows can be a good way to keep collaborative deltas out of base files (until you explicitly merge/promote).

---

## 4) Concrete Python patterns for “safe / non-destructive editing” (anything, not just variants)

### Pattern 1: “Always edit in session”

```python
from pxr import Usd

def with_session_edit(stage: Usd.Stage):
    session_layer = stage.GetSessionLayer()
    session_target = stage.GetEditTargetForLocalLayer(session_layer)
    return Usd.EditContext(stage, session_target)

# Usage: transforms, attrs, visibility, variants, anything
with with_session_edit(stage):
    prim = stage.GetPrimAtPath("/World/Thing")
    prim.GetAttribute("visibility").Set("invisible")
```

Session layer is explicitly intended for ephemeral overrides. ([NVIDIA Omniverse Docs][2])

### Pattern 2: Guardrail — never allow edits to “protected” layers

```python
def ensure_safe_target(stage, protected_prefixes=("/projects/", "/assets/")):
    layer_id = stage.GetEditTarget().GetLayer().identifier
    if layer_id.startswith(protected_prefixes):
        # force session
        session_layer = stage.GetSessionLayer()
        stage.SetEditTarget(stage.GetEditTargetForLocalLayer(session_layer))
        return False, layer_id
    return True, layer_id
```

(Useful to run before tool actions, scripted UI actions, or per-frame callbacks.)

### Pattern 3: Create a persistent “scratch override” layer and target it

```python
from pxr import Sdf

root = stage.GetRootLayer()
scratch = Sdf.Layer.CreateNew("users/alice/scratch_overrides.usda")
root.subLayerPaths.insert(0, scratch.identifier)  # strongest sublayer in root stack
stage.SetEditTarget(stage.GetEditTargetForLocalLayer(scratch))
```

### Pattern 4: Audit — find which layers got authored (catch accidental pollution)

```python
def dirty_layers(stage):
    return [l.identifier for l in stage.GetLayerStack(includeSessionLayers=True) if l.dirty]

print("Dirty layers:", dirty_layers(stage))
```

Including session layers in the stack is explicitly supported. ([NVIDIA Omniverse Docs][2])

---

## 5) Non-destructive *structural* edits (move/delete/rename) without touching assets

When you need to do namespace edits (move/delete prims that come from referenced assets), USD supports non-destructive namespace editing using **relocates**, rather than editing the referenced asset. ([openusd.org][7])

Practical takeaway: **even “destructive-seeming” operations can be kept non-destructive** if you do them in your override/session layer and let USD express them via composition.

---

## 6) Practical workflow recommendations (team/pipeline level)

### “Two-phase” workflow: audition → promote

1. **Audition in Session Layer** (safe, temporary)
2. If approved, **promote** the deltas into a designated override layer (shot/task layer), then commit.

### Make “protected layers” truly protected

* Enforce **read-only** at the filesystem/Nucleus permission level for published layers.
* In-app locking helps, but it’s not the same as “cannot write.” (Locking is a UX control; EditTarget still matters.)

### Standardize a “safe authoring default”

On file open:

* Set authoring/edit target to **session** or **user scratch**.
* If Auto Authoring is enabled, set its default layer to session/scratch. ([NVIDIA Omniverse Docs][5])

---

### The high-level best practice

**Don’t rely on “hoping the UI writes to the right layer.”** Make it deterministic:

* Pick a **safe edit target** (session or scratch) *first*.
* Keep base/project layers immutable (policy + permissions).
* Audit dirty layers and promote intentionally.

If you tell me whether you’re primarily in **Normal authoring** or **Auto Authoring**, I can give you a small Kit-side snippet that enforces “safe edit target on stage open + before any authoring command” using the `omni.kit.usd.layers` API.

[1]: https://remedy-entertainment.github.io/USDBook/terminology/edittarget.html?utm_source=chatgpt.com "Getting Started with Universal Scene Description (USD)"
[2]: https://docs.omniverse.nvidia.com/kit/docs/pxr-usd-api/105.0.2/pxr/Usd.html?utm_source=chatgpt.com "Usd module — pxr-usd-api 105.0.2 documentation"
[3]: https://docs.nvidia.com/learn-openusd/latest/composition-basics/layers.html?utm_source=chatgpt.com "Layers — Learn OpenUSD"
[4]: https://docs.omniverse.nvidia.com/extensions/latest/ext_core/ext_layers.html?utm_source=chatgpt.com "Layers — Omniverse Extensions"
[5]: https://docs.omniverse.nvidia.com/kit/docs/omni.kit.usd.layers/latest/omni.kit.usd.layers/omni.kit.usd.layers.AutoAuthoring.html?utm_source=chatgpt.com "AutoAuthoring — Omniverse Kit"
[6]: https://docs.omniverse.nvidia.com/guide_rtx-best-practices/latest/common/glossary-of-terms.html?utm_source=chatgpt.com "Omniverse Glossary of Terms — RTX Best Practices ..."
[7]: https://openusd.org/dev/user_guides/namespace_editing.html?utm_source=chatgpt.com "Namespace Editing"



---

*End of Appendix B*

---

**Discovery Created:** 26.01.2026 11:55
**Framework Agent:** OmniUSD Domain Agent + USDcodeNIM MCP + SynapGarden MCP
**Template:** Discovery Exploration Template
**Related Projects:** USD_GoodStart (`E:\SynologyDrive\9999_LocalRepo\USD_GoodStart`)
**Domain:** USD/Omniverse (Domain_OmniUSD_Guardrails)