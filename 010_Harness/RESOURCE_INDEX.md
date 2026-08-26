---
arys_schema_version: "1.3"
id: "e02d08a6-1b56-47ad-a63f-f915601a66c5"
kanban_id: null
title: "USD GoodStart Shadow Resource Index"
document_version: "0.1.0"
framework: "USD_GoodStart_Shadow_Harness"
type: INDEX
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
  git_path: "010_Harness/RESOURCE_INDEX.md"
agent_index:
  context: "Bounded resource routes for maintaining USD GoodStart without treating the repository as OpenUSD authority."
  maturation: 1
  routing:
    local: "#local-authoring-resources"
    public: "#public-dependency-resources"
    external: "#external-authority-and-destination-routes"
tags: [usd_goodstart, resources, source_routing, public_compatibility, maintenance]
---

# USD GoodStart Shadow Resource Index

**Version**: 0.1.0 | **Date**: 24.08.2026 | **Time**: 10:26 | **GlobalID**: 20260824_1026_USDGoodStartShadowResourceIndex_v0.1.0

**Last Updated:** 24.08.2026 10:26

**Framework:** USD_GoodStart_Shadow_Harness

**Status:** draft

**Origin Domain:** Domain020

**Git:** Repo: USD_GoodStart | Branch: main | Path: 010_Harness/RESOURCE_INDEX.md | Commit: pending

**Tag block:**
#usd_goodstart #resources #source_routing #public_compatibility #maintenance

## Local authoring resources

| Resource | Role |
|---|---|
| `README.md` | Public product overview and compatibility surface |
| `WIP_Docs/ASWF_Asset_Group_Minimal_Production_Workflow_DISCOVERY.md` | Maintained asset-structure research paper |
| `WIP_Docs/*VIDEO_DEEP_DIVE_TUTORIAL*.md` | Publicly useful tutorial companions; select individually |
| `scripts/setup_usd_project.py` | Cross-platform generator implementation candidate |
| `scripts/setup_usd_project.bat` | Existing Windows command-shell launcher |
| `scripts/setup_usd_project.ps1` | Existing PowerShell launcher |
| `scripts/README.md` | Script usage documentation |
| `scripts/AUTOMATION_PROMPT.md` | Generator behavior/design reference; not executable authority |
| `.github/workflows/validate.yml` | Current informative CI configuration; not a release gate |
| `History/` | Historical compatibility evidence; load only when required |

## Public dependency resources

- GitHub repository: `https://github.com/jph2/USD_GoodStart`
- Public links embedded in `README.md` and selected tutorials
- YouTube videos and playlists linked from tutorial companions
- LinkedIn and haluszka.com references that direct readers into this material

An external URL is a dependency locator, not automatically an authority or a
license grant.

## External authority and destination routes

- AOUSD specifications: normative OpenUSD semantics for their versioned scope.
- Pixar OpenUSD documentation/source: implementation and API evidence.
- Product-owner documentation: product-specific behavior.
- Sibling `Personal_Governance_Harness`: shared governance law.
- Sibling `OpenUSD-GoodStart`: Domain020 route and future migration candidate,
  not an accepted replacement for this repository's current public surface.

Use exact, task-relevant sources. Do not mirror entire external corpora here.
