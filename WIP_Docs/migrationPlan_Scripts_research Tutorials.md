---
arys_schema_version: '1.2'
id: d3fa217c-bc98-485c-b379-a984d6ec103e
title: migrationPlan Scripts research Tutorials
type: PRACTICAL
status: active
trust_level: 2
created: '2026-02-17T09:24:41Z'
last_modified: '2026-02-17T09:24:41Z'
---

**Version**: 1.0.0 | **Date**: 16.02.2026 | **Time**: 12:00 | **GlobalID**: 20260216_1200_USD_GoodStart_batch

**Tag block:**
#gaming #livrps #layers #variants #debugging #validation #reference #vscode #import #variant #material #opinions #openusd #workflow_automation #best_practices #usd_core #references #analysis #composition #conversion


### Summary  Migrating Tutorials
I went through the **highest‑leverage** tutorials in `OV_USD_Tutorials` (project structure/naming, LIVRPS+layers+variants, IDE debugging, data prep/validation, plus the “Unified Naming” reference). There’s a lot of good *workflow guidance* we can reuse in `USD_GoodStart` — but also a few **technically wrong / misleading** claims + code snippets that we should **not** import.

---

### What’s worth pulling into `USD_GoodStart` (high-signal)
#### 1) **Variant/material-debugging playbook (Yellow “V” / Blue “I”)**
The LIVRPS02 + LIVRPS03 tutorials have strong *debug framing*:
- **Pattern recognition**: Yellow V often = *a stronger opinion is blocking the variant* (Local/Inherited binding, same prim level, etc.)
- **Fix strategy**: move bindings by hierarchy level + use `bindingStrength` deliberately (`strongerThanDescendants` for variant-driven bindings; `weakerThanDescendants` for defaults).

This maps *directly* onto your current `USD_GoodStart` pain point: **your `VAR_LYR.usda` is currently pulling the MatLib in and doing bindings inside the variant layer** (so the “variant layer loads MatLib” complaint is structurally expected).

#### 2) **Validation emphasis: use `usdchecker` as the “truth meter”**
Multiple tutorials consistently recommend adding `usdchecker` to the pipeline (`usdchecker --composition`, `--timeSamples`, etc.). This is a good “missing piece” for GoodStart: your repo currently leans on custom Python validators — which is good — but adding a `usdchecker` step (where available) raises confidence and catches different classes of issues.

#### 3) **Data prep principles (separation of concerns)**
The “Data Preparation Best Practices” tutorial reinforces a clean mental model:
- **Logic/config** in USDA (human readable)
- **Heavy geometry** in payloads (USDC/USD)
- **Materials** centralized and referenced
- **Avoid renaming referenced files**
This aligns with your GoodStart guide, and the tutorial’s checklists are worth reusing (not necessarily the code).

#### 4) **Model kinds + module hierarchy (optional additions)**
- `Understanding_Model_Kinds__TUTORIAL.md`: good conceptual primer (kinds as semantics / validation tool).
- `USD_Module_Hierarchy_and_API_Structure__TUTORIAL.md`: good for developers (imports, schema thinking). Optional for GoodStart depending on audience.

---

### What’s missing in `USD_GoodStart` (based on these tutorials)
- **A dedicated “Debugging variants/materials” page** (or chapter) that explains:
  - Yellow V / Blue I meaning
  - A repeatable triage checklist
  - Where to author defaults vs variants (hierarchy + layer responsibilities)
- **A “Validation ladder”** section:
  - Quick check: open in Composer/usdview
  - CLI check: `usdchecker` (if installed)
  - Repo check: your `scripts/validate_*.py`
- **A crisp “conventions vs USD rules” callout**:
  - File numbering/prefixing helps humans/automation, but **USD composition strength is not determined by filename numbers** — only by arcs + layer stack order.

---

### “Be careful” — what NOT to pull (or must rewrite)
#### 1) **Some Python API snippets are wrong**
The LIVRPS03 tutorial contains code like `prim.GetCompositionArcs()` and `prop.GetResolveInfo()` / `.source`. That is **not correct as written**.

- **Correct concept**: You can query composition arcs via `UsdPrimCompositionQuery`, not `UsdPrim.GetCompositionArcs()`.  
  Source: OpenUSD API docs (`UsdPrimCompositionQuery::GetCompositionArcs`) via Context7 `/websites/openusd_release_api`.

- **Resolve info**: `GetResolveInfo()` is associated with attributes (and returns a `UsdResolveInfo` where you call methods like `GetSource()`), not `.source` field access as shown.  
  Source: OpenUSD API docs (`UsdResolveInfo`) via Context7 `/websites/openusd_release_api`.

So: we should reuse the **debug workflow** but **rewrite** any suspect code using verified APIs.

#### 2) **Misleading statement: numbering == strength**
In `USD_Project_Structure_and_File_Organization__TUTORIAL.md`, there are lines implying “lower numbers are stronger” in a way that could be read as a USD rule. That’s only a *convention*. In USD:
- sublayer strength is determined by **order in `subLayers`**
- overall strength is governed by composition arcs (LIVRPS/LIVRPS+E) and authored opinions

We should not import that phrasing without a fix.

#### 3) **Unified naming system is a “style”, not universally better**
`02.4_Naming _Conventions_Unified.md` proposes `GMESH_`, `MLIBS_`, `YREFS_`, etc. That can be great for automation — but it’s **not automatically compatible** with GoodStart’s current convention (your `_GEO/_MAT/_LYR` suffix scheme). If we adopt it, we should do it as:
- an **optional naming profile**, or
- a mapping table (GoodStart suffixes ↔ unified prefixes), not a forced migration.

---

### Concrete pull list (what I recommend we integrate first)
1) **Add a “Variants & Material Binding Debugging” section** to your `OpenUSD_Best_Practices_Guide (17).md`:
   - Yellow V / Blue I explanation
   - “hierarchy-level binding” recipe (`strongerThanDescendants` vs `weakerThanDescendants`)
   - “don’t let variant layers load MatLib” guideline (MatLib should be loaded in material layer; variants only select/bind)

2) **Add a “Validation ladder”**:
   - Recommend `usdchecker` usage (when available)
   - Keep your repo scripts as the project-specific checks
   - Emphasize portability checks (absolute paths)

3) **Update naming chapter wording**:
   - Keep your suffix system as default
   - Add a short subsection: “Unified Prefix System (optional)” referencing the unified naming doc as an alternative
   - Add an explicit warning: **filename numbering doesn’t affect USD composition**

4) **(Implementation follow-up)** refactor `USD_GoodStart` layer responsibilities to match the teaching:
   - Move MatLib reference out of `050_VAR_LYR/VAR_LYR.usda` into `030_USD_LYR/Mtl_import_LYR.usda`
   - Keep variant layer focused on variant selection/bindings only (and avoid “importing” MatLib there)

---

### Research deltas (from `OV_USD_Research`) — what to **add/clarify** in the migration gate
These research notes overlap with the tutorial migration themes and add a few **important clarifications**. Recommended: treat these as **migration “safety notes”** to avoid re‑introducing misleading claims.

#### 1) Omniverse Variant Editor icons: Yellow **L** vs Grey **V** (tool behavior, not “core USD law”)
Source: `OV_Dev/OV_USD_Research/research/workflows/variants_livrps_ide_workflows.md`
- **What it adds**: Explains that Omniverse can represent “local but should inherit” vs “true inheritance” using UI icons, and that the *configuration* can be persisted in the USDA file (example uses a `variantSet` block that includes a `variantPrimPaths` array).
- **Migration delta / guardrail**:
  - Document this as **Omniverse/Presenter behavior** (UI semantics), not a generic USD rule.
  - If we ever mention `variantPrimPaths`, label it **app/tool-authored configuration** and avoid implying it’s a canonical OpenUSD variant authoring pattern.

#### 2) Relationships vs attributes: value/target resolution differs (critical for `material:binding` debugging)
Sources:
- `OV_Dev/OV_USD_Research/research/usd_core/attributes_usage_research.md`
- `OV_Dev/OV_USD_Research/research/usd_core/usd_properties_research.md`
- **What it adds**:
  - Reinforces that **properties = attributes + relationships**, and that relationships are link/target based.
  - Highlights a key debugging nuance: **relationship opinions are combined**, while attribute value resolution is typically “strongest wins” for the resolved value.
- **Migration delta / guardrail**:
  - When migrating debugging guidance into `USD_GoodStart`, explicitly separate:
    - **Attribute debugging**: `UsdAttribute.GetResolveInfo(...).GetSource()` / `Get()` for resolved value
    - **Relationship debugging** (e.g. `material:binding`): `GetTargets()` + `GetPropertyStack(...)` to understand authored sites/targets

#### 3) Validation/governance emphasis: “pin versions + composition hygiene” belongs in the migration gate
Source: `OV_Dev/OV_USD_Research/research/digital_twin/validation_simulation_omniverse_research.md`
- **What it adds**: A governance framing that’s useful for `USD_GoodStart` adoption:
  - **Pin USD/Kit versions** and record dates to avoid “version drift” debugging spirals.
  - Treat **composition hygiene** (variants/instancing/payload discipline) as a first-class validation risk (e.g., silent de-instancing, variant conflicts).
  - Encourages using `usdchecker` as part of a validation ladder (aligns with the tutorial pull list).
- **Migration delta / guardrail**:
  - In the `USD_GoodStart` docs-first phase, add a short callout: **version pinning + validation ladder** (UI → `usdchecker` → repo scripts) as the default escalation path.

---

### One decision point (before we change anything)
Do you want the “Unified Naming” (`GMESH_/MLIBS_/YREFS_…`) to become:
- **A)** a *secondary* “advanced/automation profile” inside GoodStart docs (recommended), or  
- **B)** the *primary* GoodStart naming system (bigger migration; higher risk)?

If you pick **A or B**, tell me where you want the integration notes written (chat-only vs a new doc inside `USD_GoodStart/WIP_Docs/…`).

---

### Execution Plan (Docs-first, safe)
**Goal:** integrate the best parts of `OV_USD_Tutorials` into `USD_GoodStart` **without** importing outdated API usage or misleading composition claims.

#### Phase 1 — Documentation integration (no USD file changes)
- **Add new doc**: `USD_GoodStart/WIP_Docs/Debugging_Variants_and_Materials.md`
  - **Include**:
    - Yellow **V** / Blue **I**: what it means, typical root causes
    - A repeatable triage checklist (UI → Layer Stack → IDE → validation)
    - Material binding guidance: hierarchy-level binding + `bindingStrength` (`strongerThanDescendants` vs `weakerThanDescendants`)
    - Rule: **Variant layers should NOT load MatLib**; MatLib belongs in material layer; variant layer selects/binds only
  - **Hard requirement**: no unverified USD Python API calls; link to authoritative OpenUSD docs for composition queries / resolve info.

- **Add new doc**: `USD_GoodStart/WIP_Docs/Validation_Ladder.md`
  - **Include**:
    - Quick checks (Composer/usdview)
    - CLI checks (`usdchecker` when installed; example invocations)
    - Project checks (`scripts/validate_asset.py`, `scripts/validate_scene.py`)
    - Portability checks (absolute paths, missing assets, layer stack sanity)

- **Update guide**: `USD_GoodStart/WIP_Docs/OpenUSD_Best_Practices_Guide (17).md`
  - Add links in **Chapter 18 (Quick Start)** to:
    - `Debugging_Variants_and_Materials.md`
    - `Validation_Ladder.md`
  - Add a callout: **filename numbering/prefixing is a convention; USD strength is arcs + layer stack order.**

- **Update `USD_GoodStart/README.md`**
  - Add a short “Debug & Validate” section linking the two new docs.

#### Phase 2 — (Optional) Template refactor to match the teaching (USD changes)
- Move MatLib reference out of `050_VAR_LYR/VAR_LYR.usda` into `030_USD_LYR/Mtl_import_LYR.usda`.
- Keep `050_VAR_LYR/VAR_LYR.usda` focused on variant selection/bindings only.
- Re-run project validation scripts; ensure no broken references.

---

### “Do NOT import” list (guardrails)
- **Do NOT copy** tutorial Python snippets that use:
  - `prim.GetCompositionArcs()` (rewrite using `UsdPrimCompositionQuery`)
  - `prop.GetResolveInfo()` / `.source` (rewrite using verified `UsdResolveInfo` API on attributes)
- **Do NOT claim** “lower filename numbers are stronger in USD” — clarify it is only a pipeline convention.