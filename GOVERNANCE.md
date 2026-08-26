---
arys_schema_version: "1.3"
id: "4a57fc5e-3cd0-4ac4-9e69-91f1e74d22c8"
kanban_id: null
title: "USD GoodStart Shadow Repository Governance"
document_version: "0.1.0"
framework: "USD_GoodStart_Shadow_Harness"
type: GOVERNANCE
status: draft
trust_level: 3
visibility: external
created: "2026-08-24T10:26:00+02:00"
last_modified: "2026-08-24T10:26:00+02:00"
origin_domain: "Domain020"
author: "Jan Haluszka / Codex"
provenance:
  git_repo: "USD_GoodStart"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "GOVERNANCE.md"
agent_index:
  context: "Shadow governance for maintaining the public legacy USD GoodStart repository while preparing a controlled future migration."
  maturation: 1
  routing:
    authority_and_scope: "#authority-and-scope"
    repository_state: "#repository-state"
    ownership: "#repository-truth-and-ownership"
    maintenance: "#maintenance-only-contract"
    compatibility: "#public-compatibility-contract"
    migration: "#migration-boundary"
    change_control: "#change-control"
tags: [usd_goodstart, governance, shadow_harness, maintenance, public_compatibility, migration]
---

# USD GoodStart Shadow Repository Governance

**Version**: 0.1.0 | **Date**: 24.08.2026 | **Time**: 10:26 | **GlobalID**: 20260824_1026_USDGoodStartShadowRepositoryGovernance_v0.1.0

**Last Updated:** 24.08.2026 10:26

**Framework:** USD_GoodStart_Shadow_Harness

**Status:** draft

**Origin Domain:** Domain020

**Git:** Repo: USD_GoodStart | Branch: main | Path: GOVERNANCE.md | Commit: pending

**Tag block:**
#usd_goodstart #governance #shadow_harness #maintenance #public_compatibility #migration

## Authority and scope

This document applies Personal Governance law to the repository-local operation
of `USD_GoodStart`. It is a shadow contract and does not activate a registry
record or transfer authority.

Authority resolves in this order:

1. Applicable law, licenses, and binding external obligations.
2. Versioned AOUSD, Pixar OpenUSD, and owning-product sources for their subjects.
3. The active `Personal_Governance_Harness` and its shared law.
4. This repository governance for local maintenance and public compatibility.
5. `ROADMAP_USD_GoodStart.md` for repository execution and status.
6. `README.md`, research, tutorials, scripts, and implementation notes according
   to their declared scope and evidence.

Generated output, GitHub Actions output, copied material, and a future destination
repository do not become authority through convenience or location.

## Repository state

| Concern | State | Meaning |
|---|---|---|
| Public repository | `LEGACY_PUBLIC_MAINTENANCE` | Existing links and useful material remain available. |
| Repo Harness | `SHADOW` | Local instructions may be tested but are not registered or promoted. |
| Development policy | `MAINTENANCE_ONLY` | Only the bounded classes below are accepted. |
| Future destination | `CANDIDATE_NOT_READY` | `OpenUSD-GoodStart` may receive reviewed items later; no bulk switch. |
| Retirement | `HOLD` | No date, redirect, archive, or deletion is authorized. |

The public repository state and harness lifecycle are separate. A shadow harness
does not make the public repository inactive, and a public repository does not
make the harness active.

## Repository truth and ownership

`USD_GoodStart` remains the current owner of:

- its public README and stable public routes;
- its proposed minimal USD project and layer structure;
- its setup generator, launchers, sample assets, and validation mechanisms;
- its asset-structure research paper and historical research record;
- its tutorial companions and their links to public videos; and
- its maintenance, compatibility, migration, and eventual retirement decisions.

It does not own:

- normative OpenUSD semantics or API truth;
- the Domain020 corpus owned by the separate `OpenUSD-GoodStart` repository;
- shared Personal Governance law; or
- product-specific behavior owned by NVIDIA, DCC vendors, or other product owners.

Repository recommendations must be labeled as GoodStart proposals, practices, or
research conclusions. Normative claims require the applicable upstream authority.

## Maintenance-only contract

Accepted maintenance classes are:

1. Continued authoring of
   `WIP_Docs/ASWF_Asset_Group_Minimal_Production_Workflow_DISCOVERY.md`.
2. README upkeep needed for accuracy, public routing, and compatibility.
3. Linux enablement for the minimal-project generator, including a Linux-native
   entry point and cross-platform verification.
4. Repairs to links, validation, packaging, security, and supported compatibility.
5. Item-level migration inventory, comparison, and proposal preparation.

Broad new feature development or a new local OpenUSD knowledge architecture is
out of scope. If a proposed change does not fit one of the five classes, it is
`HOLD` pending an explicit scope decision.

## Public compatibility contract

Public links are part of the maintained product surface. Before changing a public
path, heading anchor, tutorial filename, download, video route, or documented
command, the change must identify:

- the current public locator;
- known inbound references where discoverable;
- the replacement or compatibility route;
- link and file-existence verification;
- rollback; and
- operator approval for any breaking or externally visible transition.

Historical content may carry corrections or visible supersession notes. It must
not disappear merely because newer content exists elsewhere.

## Migration boundary

`OpenUSD-GoodStart` is the intended long-term destination, but it is not yet an
accepted replacement for this repository. Migration is an item-level transaction:

1. Identify the exact source artifact and public dependencies.
2. Classify its current owner, evidence, license, visibility, and authority.
3. Compare it with the candidate destination and resolve conflicts.
4. Adapt or reconstruct it under the destination's accepted governance.
5. Verify destination quality and public route behavior.
6. Record whether the source remains canonical, becomes historical, redirects,
   or can eventually be retired.
7. Obtain explicit operator acceptance before switching any public route.

Copying is not promotion. Destination presence does not retire the source. Bulk
moves, deletes, redirects, and authority transfer remain `HOLD`.

## Validation truth

The current GitHub workflow is informative only because validator failures are
suppressed and some referenced fixture paths are stale. Local validators require
`usd-core`. Until the roadmap hardens these checks, neither CI success nor an
unverified local invocation proves release readiness.

The shadow harness may document failures and define future acceptance criteria.
It may not relabel incomplete checks as passing.

## Change control

- `AGENTS.md` is the compact agent front door and carries no ARYS header.
- This file owns local authority and maintenance boundaries.
- `HORIZON_USD_GoodStart.md` is orientation only.
- `ROADMAP_USD_GoodStart.md` owns repository maintenance status and its canonical
  `## Execution Plan`.
- `010_Harness/` contains supporting context, source, tool, and evaluation routes.
- Shared governance changes are made in Personal Governance, not copied here.

Activation, registry mutation, public migration, redirect, archive, deletion,
release, commit, or push requires separate authorization. Until then, this
repository harness remains `SHADOW`.
