---
arys_schema_version: "1.3"
id: "3a6a5402-4153-43e1-8e29-40f52e16841f"
kanban_id: null
title: "USD GoodStart Shadow Tool Contract"
document_version: "0.2.0"
framework: "USD_GoodStart_Shadow_Harness"
type: STANDARD
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
  git_path: "010_Harness/TOOLS.md"
agent_index:
  context: "Truthful command, dependency, and cross-platform boundaries for USD GoodStart maintenance."
  maturation: 1
  routing:
    commands: "#current-command-surface"
    limitations: "#known-limitations"
    linux: "#linux-support-acceptance-direction"
tags: [usd_goodstart, tools, validation, generator, linux, ci]
---

# USD GoodStart Shadow Tool Contract

**Version**: 0.2.0 | **Date**: 24.08.2026 | **Time**: 10:43 | **GlobalID**: 20260824_1043_USDGoodStartShadowToolContract_v0.2.0

**Last Updated:** 24.08.2026 10:43

**Framework:** USD_GoodStart_Shadow_Harness

**Status:** draft

**Origin Domain:** Domain020

**Git:** Repo: USD_GoodStart | Branch: main | Path: 010_Harness/TOOLS.md | Commit: pending

**Tag block:**
#usd_goodstart #tools #validation #generator #linux #ci

## Current command surface

| Purpose | Command | Current truth |
|---|---|---|
| Show generator version | `python scripts/setup_usd_project.py --version` | Works without `usd-core`. |
| Generate project | `python scripts/setup_usd_project.py [target]` | Interactive; behavior must be verified in a disposable target. |
| Windows launcher | `scripts/setup_usd_project.bat` | Windows-only command-shell entry point. |
| PowerShell launcher | `scripts/setup_usd_project.ps1` | PowerShell entry point; not proof of Linux support. |
| Linux/macOS launcher | `sh scripts/setup_usd_project.sh [target]` | POSIX wrapper around the same Python generator; verified on Ubuntu/WSL. |
| Validate asset | `python scripts/validate_asset.py <asset>` | Requires `usd-core`. |
| Validate scene | `python scripts/validate_scene.py <root-layer>` | Requires `usd-core`. |
| Convenience validation | `python scripts/validate_usd.py <path>` | Requires environment and target verification. |

Run generators only against explicit disposable directories until output scope and
overwrite behavior are verified.

## Known limitations

- `setup_usd_project.py --help` is currently interpreted as a target directory
  and enters interactive setup; it is not a supported help command.
- The current environment does not have `usd-core`, so USD validation cannot be
  claimed from the checks performed while creating this shadow harness.
- `.github/workflows/validate.yml` references absent sample paths, including
  `GoodStart_ROOT.usda`, and suppresses validator failures with `|| true`.
- CI success therefore does not currently prove USD validity.
- Generated text uses platform-native line endings: CRLF on Windows and LF on Linux. Relative paths and normalized content have parity.

These are maintenance findings and roadmap inputs, not authorization to alter
the pre-existing implementation changes in the working tree.

## Linux support acceptance direction

Linux support should be implemented around the Python generator, with a shell
launcher or documented direct invocation. Acceptance requires:

- safe POSIX path and argument handling;
- meaningful non-zero exit codes;
- non-interactive or scriptable inputs for test automation;
- explicit encoding and line-ending behavior;
- temporary-directory generation tests for all supported scales;
- required-file and semantic-content comparison across Windows and Linux; and
- preserved Windows launcher behavior or an explicitly accepted compatibility change.

A `.bat` translation alone is insufficient if the Python implementation retains
Windows-only assumptions.

Verification on 24.08.2026 covered centimeters, meters, and millimeters through
both the Windows batch and Ubuntu/WSL shell launchers. Every run returned `0` and
created the same 22 relative files with identical normalized content. The POSIX
launcher also passed `sh -n`, `--version`, and a target-path-with-spaces run.
