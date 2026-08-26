---
arys_schema_version: "1.3"
id: "d3f6f59b-16f3-48cc-b07a-8781e2c17646"
kanban_id: null
title: "USD GoodStart Maintenance and Transition Roadmap"
document_version: "0.2.0"
framework: "USD_GoodStart_Shadow_Harness"
type: ROADMAP
status: draft
trust_level: 3
visibility: external
created: "2026-08-24T10:26:00+02:00"
last_modified: "2026-08-24T10:43:00+02:00"
origin_domain: "Domain020"
author: "Jan Haluszka / Codex"
provenance:
  git_repo: "USD_GoodStart"
  git_branch: "main"
  git_commit_short: null
  git_commit_full: null
  git_path: "ROADMAP_USD_GoodStart.md"
agent_index:
  context: "Canonical shadow roadmap for maintaining USD GoodStart's public surface and preparing a reversible future transition."
  maturation: 1
  routing:
    goal: "#goal"
    execution_plan: "#execution-plan"
    paper: "#wp-mnt-002-asset-structure-research"
    linux: "#wp-mnt-003-linux-generator-support"
    migration: "#wp-mig-001-item-level-migration-preparation"
tags: [usd_goodstart, roadmap, maintenance, linux, public_compatibility, migration]
---

# USD GoodStart Maintenance and Transition Roadmap

**Version**: 0.2.0 | **Date**: 24.08.2026 | **Time**: 10:43 | **GlobalID**: 20260824_1043_USDGoodStartMaintenanceTransitionRoadmap_v0.2.0

**Last Updated:** 24.08.2026 10:43

**Framework:** USD_GoodStart_Shadow_Harness

**Status:** draft

**Origin Domain:** Domain020

**Git:** Repo: USD_GoodStart | Branch: main | Path: ROADMAP_USD_GoodStart.md | Commit: pending

**Tag block:**
#usd_goodstart #roadmap #maintenance #linux #public_compatibility #migration

## Goal

Keep the legacy public repository accurate and usable while limiting development
to essential maintenance, the asset-structure research paper, and cross-platform
support for the minimal-project generator. Prepare future migration without
promoting an unready destination or breaking existing public references.

This file's `## Execution Plan` is the repository-local status authority for the
shadow harness. It does not activate the harness, authorize publication, or
override Personal Governance.

## Status vocabulary

- `DONE`: evidence exists for the bounded result.
- `NEXT`: accepted next maintenance package, not automatically authorized for writes.
- `OPEN`: allowed maintenance that may proceed when requested.
- `HOLD`: blocked pending an explicit gate or decision.

## Execution Plan

| Work package | Status | Scope | Closure gate |
|---|---|---|---|
| `WP-SH-001` | `DONE` | Create the shadow maintenance harness without editing existing repository content. | New files validate structurally; pre-existing changes remain untouched. |
| `WP-MNT-001` | `OPEN` | Inventory public paths, README anchors, downloads, tutorials, videos, and known external references. | Machine-readable or reviewable inventory plus link/file checks and no public mutation. |
| `WP-MNT-002` | `OPEN` | Continue the asset-structure research paper. | Source-backed revision, proposal/authority boundaries, working internal links, and recorded review. |
| `WP-MNT-003` | `DONE` | Prepare the minimal-project generator for Linux. | POSIX launcher, Windows compatibility, three-scale cross-platform fixture parity, spaced-path check, and documented dependencies. |
| `WP-MNT-004` | `OPEN` | Harden stale or non-gating validation and CI behavior. | Real fixture paths, failures propagate, dependencies are pinned/documented, and local/CI results agree. |
| `WP-MIG-001` | `HOLD` | Prepare item-level migration proposals to `OpenUSD-GoodStart`. | Destination readiness, per-item owner/evidence decision, public compatibility plan, rollback, and operator acceptance. |
| `WP-RET-001` | `HOLD` | Redirect, archive, or retire this repository. | Public dependency audit, accepted destination, preserved history, explicit operator decision, and reversible transition plan. |

## WP-MNT-001 — Public compatibility inventory

Record repository URLs, README headings/anchors, tutorial paths, research paths,
download names, YouTube links, LinkedIn/haluszka.com references, and sample asset
paths. This package is observational until a separate maintenance change is
accepted. Missing or unreachable links are findings, not permission to delete.

## WP-MNT-002 — Asset-structure research

Canonical current paper:
`WIP_Docs/ASWF_Asset_Group_Minimal_Production_Workflow_DISCOVERY.md`.

Allowed work includes continued comparison of GoodStart, ASWF, Learn OpenUSD,
CAD-to-OpenUSD, and industrial/digital-twin asset structures. Revisions must
distinguish upstream facts, cited practice, GoodStart proposals, hypotheses, and
unverified recommendations. The paper may evolve in this repository while the
repository remains public-maintenance-only.

## WP-MNT-003 — Linux generator support

The current generator is `scripts/setup_usd_project.py`, with Windows batch and
PowerShell launchers. Linux support must provide an honest Linux-native route;
the `.bat` file itself is not portable.

Minimum acceptance direction:

1. Define the supported Python version and `usd-core` requirement boundary.
2. Provide a Linux shell invocation or launcher with safe quoting and exit codes.
3. Remove or isolate Windows-only path, shell, encoding, and interaction assumptions.
4. Generate each supported scale into temporary clean directories on Windows and Linux.
5. Compare required file manifests and semantically relevant generated content.
6. Preserve documented Windows behavior or record an accepted compatibility change.
7. Update the README and script documentation without breaking existing download routes.

Implemented route: `scripts/setup_usd_project.sh`. It delegates to the same
`setup_usd_project.py` used by the Windows wrappers; no second generator exists.

Verification on 24.08.2026 used Windows batch and Ubuntu/WSL shell launchers with
identical answers for centimeters, meters, and millimeters. Each pair produced
22 files, zero relative-path differences, and zero content differences after
normalizing platform-native CRLF/LF line endings. A Linux target path containing
spaces produced the same 22-file result. Both launchers returned exit code `0`.

## WP-MNT-004 — Validation hardening

The present GitHub workflow suppresses validator failures and references paths
that are absent from the current root. Hardening must select real fixtures,
allow failures to fail CI, verify all supported root scales, and state what
cannot be validated without `usd-core` or an application runtime.

## WP-MIG-001 — Item-level migration preparation

No bulk migration is planned. Each candidate records source path, public
dependencies, owner, authority, license/visibility, destination comparison,
adaptation needs, verification, rollback, and source disposition. The target
repository's current incompleteness is a binding hold on authority switching.

## Stop gates

- No breaking public route without explicit operator approval.
- No repository retirement while external references still depend on it.
- No `OpenUSD-GoodStart` promotion through implication or file copying.
- No release claim from the current non-gating CI workflow.
- No overwrite of pre-existing user changes.
- No commit, push, deployment, redirect, archive, or deletion without separate authorization.
