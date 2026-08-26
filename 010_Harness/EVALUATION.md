---
arys_schema_version: "1.3"
id: "6bb65454-5014-4c4c-99e0-96e67255d4c7"
kanban_id: null
title: "USD GoodStart Shadow Maintenance Evaluation"
document_version: "0.1.0"
framework: "USD_GoodStart_Shadow_Harness"
type: EVALUATION
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
  git_path: "010_Harness/EVALUATION.md"
agent_index:
  context: "Release and maintenance gates for the public legacy USD GoodStart repository."
  maturation: 1
  routing:
    gates: "#maintenance-gates"
    shadow: "#shadow-harness-acceptance"
    failure: "#failure-behavior"
tags: [usd_goodstart, evaluation, public_compatibility, validation, shadow_harness]
---

# USD GoodStart Shadow Maintenance Evaluation

**Version**: 0.1.0 | **Date**: 24.08.2026 | **Time**: 10:26 | **GlobalID**: 20260824_1026_USDGoodStartShadowMaintenanceEvaluation_v0.1.0

**Last Updated:** 24.08.2026 10:26

**Framework:** USD_GoodStart_Shadow_Harness

**Status:** draft

**Origin Domain:** Domain020

**Git:** Repo: USD_GoodStart | Branch: main | Path: 010_Harness/EVALUATION.md | Commit: pending

**Tag block:**
#usd_goodstart #evaluation #public_compatibility #validation #shadow_harness

## Maintenance gates

| Gate | Applies to | Pass evidence | Hold condition |
|---|---|---|---|
| `E-PUBLIC` | README, tutorial, path, link, or download changes | affected-route inventory, local link/file checks, external-link review, rollback | unknown inbound impact or broken public route |
| `E-PAPER` | Asset-structure paper | cited evidence for changed claims, proposal/authority labels, internal-link check, review record | unsupported normative claim or missing attribution |
| `E-GENERATOR` | Generator and launchers | disposable generation, required-file manifest, supported-scale checks, meaningful exit status | writes escape target, output incomplete, or compatibility unknown |
| `E-LINUX` | Linux support | Linux run plus Windows comparison, safe quoting, documented dependencies, equivalent required outputs | Linux untested or Windows behavior silently breaks |
| `E-USD` | USD assets and layer roots | successful validator results with recorded `usd-core` environment and exact targets | dependency missing, target stale, or failures suppressed |
| `E-AUTHORITY` | OpenUSD technical claims | exact upstream source and explicit project/proposal boundary | local recommendation presented as normative OpenUSD |
| `E-MIGRATION` | Any destination transfer or public switch | item-level disposition, destination verification, public compatibility, rollback, operator acceptance | bulk inference, destination unready, or two active owners |

## Shadow Harness acceptance

The shadow harness is structurally acceptable when:

- `AGENTS.md` is compact enough to orient an agent without loading the repository;
- governance distinguishes shadow lifecycle from the active public repository;
- maintenance scope is limited to the operator-approved classes;
- public compatibility, Domain authority, migration, and retirement boundaries are explicit;
- the Roadmap contains one `## Execution Plan`;
- context routes avoid recursive loading;
- tool documentation records current failures honestly; and
- all new governed Markdown passes the canonical ARYS 1.3 structural validator.

Structural acceptance does not activate the harness or prove project release readiness.

## Failure behavior

Public mutation, migration, release, deletion, redirect, and authority decisions
fail closed. Internal read-only inspection may continue with visible limitations.
Missing `usd-core`, stale fixtures, suppressed validator failures, or unavailable
Linux evidence must be reported; they must not be converted into a pass.
