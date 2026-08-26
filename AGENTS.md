# USD GoodStart Agent Orientation

## Gate 0

- Repository role: legacy public USD project template and research repository.
- Repository operating mode: `MAINTENANCE_ONLY`.
- Repo Harness lifecycle: `SHADOW`.
- Repository governance: `GOVERNANCE.md`.
- Orientation map: `HORIZON_USD_GoodStart.md`.
- Maintenance plan: `ROADMAP_USD_GoodStart.md`.
- Shared governance owner: the sibling `Personal_Governance_Harness` repository.
- Preserve all unrelated user changes. Stop on overlapping edits or unclear public-link impact.

This is a repository-local orientation contract. It does not activate this
harness in Personal Governance, promote this repository to a Domain Knowledge
Harness, or redefine shared ARYS, lifecycle, review-routing, or tag law.

## Required context

Load only the context needed for the task:

1. Read `GOVERNANCE.md` for authority, maintenance scope, and stop conditions.
2. Read the relevant `## Execution Plan` row in `ROADMAP_USD_GoodStart.md`.
3. Use `HORIZON_USD_GoodStart.md` to locate the smallest relevant source set.
4. For public README, tutorial, or path changes, read the public-compatibility
   rules in `010_Harness/EVALUATION.md`.
5. For generator or validation changes, read `010_Harness/TOOLS.md`.
6. For research work, read only the target paper and its cited evidence.

Repository presence is not permission to recursively load `WIP_Docs/`,
`History/`, image trees, generated outputs, or all USD assets.

## Allowed maintenance

The following work is in scope:

- Continue the asset-structure research paper at
  `WIP_Docs/ASWF_Asset_Group_Minimal_Production_Workflow_DISCOVERY.md`.
- Maintain `README.md`, especially public links, tutorial routes, compatibility
  notes, and honest current-state guidance.
- Prepare the minimal-project generator for Linux while preserving the current
  Windows entry points and generated structure unless an accepted change says otherwise.
- Repair broken links, validation, packaging, security, and cross-platform behavior.
- Inventory and prepare item-level migration proposals for `OpenUSD-GoodStart`.

New broad feature development, a second OpenUSD knowledge corpus, bulk migration,
public redirects, path removal, and repository retirement are out of scope unless
the operator changes this contract.

## Public compatibility boundary

This repository remains public and externally referenced. Treat these as public
interfaces:

- the repository URL and default branch;
- `README.md` headings and anchors used by external posts;
- tutorial and research paths under `WIP_Docs/`;
- YouTube, LinkedIn, and haluszka.com links;
- sample USD paths referenced by tutorials or the README;
- generator download names and documented commands.

Do not rename, move, delete, redirect, or substantially rewrite a public interface
without an impact inventory, replacement route, link check, and explicit operator
approval. Git history alone is not an adequate public compatibility mechanism.

## Authority boundary

`USD_GoodStart` owns its project-specific layer-stack proposal, sample assets,
generator behavior, historical tutorials, research record, and maintenance
decisions. It does not own OpenUSD normative meaning.

For OpenUSD semantics, verify claims against the applicable AOUSD, Pixar OpenUSD,
or product-owner source. The separate `OpenUSD-GoodStart` repository is the planned
long-term destination and current Domain020 route, but it is not yet accepted as a
replacement for this repository's public material. Migration is item-by-item and
never implied by copying.

## Verification entry points

Use only checks that are truthful for the current environment:

```powershell
python scripts/setup_usd_project.py --version
python scripts/validate_asset.py <path-to-asset>
python scripts/validate_scene.py <path-to-root-layer>
```

On Linux or macOS:

```bash
sh scripts/setup_usd_project.sh --version
sh scripts/setup_usd_project.sh /path/to/new/project
```

The validation commands require `usd-core`. The current GitHub workflow is not a
release gate: it references stale sample paths and suppresses validator failures
with `|| true`. `setup_usd_project.py --help` is not currently a supported help
command. See `010_Harness/TOOLS.md` before claiming validation success.

## Stop conditions

Stop and report `HOLD` when:

- a change may break an externally referenced path, anchor, download, or video route;
- the intended OpenUSD authority is unclear or a project proposal is being presented as normative;
- migration would create two active mutable owners or delete the only public copy;
- Linux support changes generated output without an accepted compatibility decision;
- required dependencies or validation evidence are unavailable;
- the task overlaps pre-existing user changes; or
- activation, publication, migration, deletion, commit, push, or retirement was not explicitly authorized.
