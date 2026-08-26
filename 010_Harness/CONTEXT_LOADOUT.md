---
arys_schema_version: "1.3"
id: "7d7d0ad0-9453-49e4-9d2d-994f71bd40f4"
kanban_id: null
title: "USD GoodStart Shadow Context Loadout"
document_version: "0.1.0"
framework: "USD_GoodStart_Shadow_Harness"
type: CONTEXT
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
  git_path: "010_Harness/CONTEXT_LOADOUT.md"
agent_index:
  context: "Task-classed minimal context routes for the USD GoodStart shadow maintenance harness."
  maturation: 1
  routing:
    default: "#default-loadout"
    task_routes: "#task-routes"
    expansion: "#expansion-and-stop-rules"
tags: [usd_goodstart, context, routing, shadow_harness, maintenance]
---

# USD GoodStart Shadow Context Loadout

**Version**: 0.1.0 | **Date**: 24.08.2026 | **Time**: 10:26 | **GlobalID**: 20260824_1026_USDGoodStartShadowContextLoadout_v0.1.0

**Last Updated:** 24.08.2026 10:26

**Framework:** USD_GoodStart_Shadow_Harness

**Status:** draft

**Origin Domain:** Domain020

**Git:** Repo: USD_GoodStart | Branch: main | Path: 010_Harness/CONTEXT_LOADOUT.md | Commit: pending

**Tag block:**
#usd_goodstart #context #routing #shadow_harness #maintenance

## Default loadout

Load `AGENTS.md`, `GOVERNANCE.md`, the relevant Roadmap work package, and only
the target files. Do not recursively load the repository.

## Task routes

| Task | Required context | Excluded by default |
|---|---|---|
| Maintain public README | `README.md`, public compatibility gate, directly linked target files | all research, History, image trees |
| Edit asset-structure paper | target paper, cited evidence needed for changed claims, `SOURCE_MAP.md` | unrelated tutorials and assets |
| Add Linux generator support | `scripts/setup_usd_project.py`, current launchers, script docs, relevant root fixtures, `TOOLS.md` | research corpus and History |
| Harden validation/CI | validator scripts, workflow, actual fixture paths, `TOOLS.md`, `EVALUATION.md` | tutorial prose and images |
| Repair tutorial/video route | exact tutorial, referenced media/link, relevant README anchor | all other tutorials |
| Prepare migration item | exact source item, public dependencies, candidate destination counterpart, authority evidence | bulk source/destination corpora |

## Expansion and stop rules

Expand to upstream OpenUSD evidence only for claims changed by the task. Expand
to `OpenUSD-GoodStart` only for a bounded comparison or destination proposal.
Use `History/` only when a current public reference depends on historical assets.

Stop when a bounded task would require broad migration, public path removal,
authority transfer, or recursive corpus loading.
