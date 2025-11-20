# Changelog

All notable changes to the USD GoodStart project template will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Prerequisites section with software requirements
- Example Asset Lifecycle documentation with scripts
- Usage Examples and Troubleshooting section
- Validation scripts (`validate_asset.py`, `validate_scene.py`, `validate_usd.py`)
- CI/CD integration (GitHub Actions workflow)
- Expanded Metadata and Interoperability section with mapping strategies
- Synthetic Data & Physical AI Readiness section
- Security, Access Control, and Collaboration guidance
- Learning Path Alignment cross-references
- Git LFS configuration guidance
- CHANGELOG.md for tracking changes
- DCC Tool Limitations section (Blender/C4D limitations)
- Path Best Practices section (relative paths guidance)

### Changed
- Enhanced documentation with more detailed workflows
- Expanded metadata mapping examples
- Improved project planning section
- Updated all USD file examples to use relative paths
- Added detailed beginner-friendly comments to validation scripts

## [1.0.1] - 2025-01-20

### Added
- DCC Tool Limitations section explaining Blender/C4D can only read/write USD but don't support layering/referencing
- Path Best Practices section emphasizing use of relative paths in USD files
- Relative paths guidance in all folder READMEs

### Changed
- Updated DCC Tools section to clarify limitations of Blender/C4D
- Updated all USD file examples to demonstrate relative paths
- Enhanced validation scripts with detailed comments for beginners

## [1.0.0] - Initial Release

### Added
- Basic project structure (000_SOURCE, 010_ASS_USD, 020_LYR_USD, 030_TEX)
- Root README with digital twin focus
- Folder-specific READMEs
- CAD conversion pipeline documentation
- Version control best practices
- DCC file integration guidance
- VFX industry best practices references
- NVIDIA Digital Twin resources
- Learning resources (AOUSD, Awesome OpenUSD, etc.)

