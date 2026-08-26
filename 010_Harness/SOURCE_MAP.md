---
arys_schema_version: "1.3"
id: "72bccba2-c1ca-4ff2-9ebd-e8cc7a777d55"
kanban_id: null
title: "USD GoodStart Shadow Source Map"
document_version: "0.1.0"
framework: "USD_GoodStart_Shadow_Harness"
type: MAP
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
  git_path: "010_Harness/SOURCE_MAP.md"
agent_index:
  context: "Ownership and migration classification for USD GoodStart source families."
  maturation: 1
  routing:
    classes: "#source-classes"
    migration: "#migration-dispositions"
    conflicts: "#conflict-handling"
tags: [usd_goodstart, source_map, ownership, migration, provenance]
---

# USD GoodStart Shadow Source Map

**Version**: 0.1.0 | **Date**: 24.08.2026 | **Time**: 10:26 | **GlobalID**: 20260824_1026_USDGoodStartShadowSourceMap_v0.1.0

**Last Updated:** 24.08.2026 10:26

**Framework:** USD_GoodStart_Shadow_Harness

**Status:** draft

**Origin Domain:** Domain020

**Git:** Repo: USD_GoodStart | Branch: main | Path: 010_Harness/SOURCE_MAP.md | Commit: pending

**Tag block:**
#usd_goodstart #source_map #ownership #migration #provenance

## Source classes

| Class | Examples | Authority treatment |
|---|---|---|
| Project authoring truth | README recommendations, layer proposal, generator behavior | Owned here for this project; label proposals clearly. |
| Maintained research | Asset-structure paper | Owned here as analysis; factual claims remain source-bound. |
| Tutorial companion | Video deep-dives and local examples | Owned here as instructional synthesis; original videos/sources retain their authority. |
| Upstream authority | AOUSD, Pixar OpenUSD, product-owner material | Cite and verify; do not silently rewrite as local truth. |
| Historical evidence | `History/`, superseded examples | Preserve when public compatibility or provenance requires it. |
| Generated output | Generated project folders, reports, CI output | Disposable evidence or deliverable; never semantic authority by itself. |
| Candidate destination | `OpenUSD-GoodStart` counterpart | Compare and review; destination presence is not promotion. |

## Migration dispositions

Each migration candidate receives one disposition:

- `KEEP_PUBLIC_CURRENT`
- `KEEP_PUBLIC_HISTORICAL`
- `ADAPT_TO_DESTINATION`
- `REFERENCE_FROM_DESTINATION`
- `HOLD_CONFLICT`
- `RETIRE_AFTER_PUBLIC_GATE`

No default bulk disposition exists. Each record must name the exact source,
destination, public dependencies, owner, evidence, verification, and rollback.

## Conflict handling

When source and destination disagree, do not choose the newer file automatically.
Compare intended audience, evidence, upstream authority, public dependencies,
project-specific decisions, and destination readiness. Unresolved conflicts are
`HOLD_CONFLICT`; they do not justify overwriting either repository.
