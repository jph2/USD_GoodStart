#!/usr/bin/env python3
"""
USD Validation Script (Combined)

Convenience script that validates USD assets or scenes with auto-detection.
Can also use the specific scripts: validate_asset.py or validate_scene.py

Validates USD files for:
- File syntax errors
- Missing references
- Invalid layer composition
- Layer ordering (for scenes)

Usage:
    python scripts/validate_usd.py path/to/file.usd
    python scripts/validate_usd.py path/to/asset.usda
    python scripts/validate_usd.py GoodStart_ROOT.usda

Note: This script validates USD files but does not modify them. USD files should use
relative paths (e.g., @../010_ASS_USD/asset.usd@, @./020_LYR_USD/file.usda@) for portability.
The script uses absolute paths internally for validation but USD files themselves should
contain relative paths. See README.md "Path Best Practices" section for guidance.
"""

# Standard library imports
import sys      # For command-line arguments and exit codes
import os       # For operating system operations
from pathlib import Path  # Modern Python path handling

# USD library imports
try:
    from pxr import Usd, Sdf, UsdUtils
    # Usd: Main USD API for stages, prims, and high-level operations
    # Sdf: Scene Description Foundation - low-level layer and data access
    # UsdUtils: Utility functions for USD operations
except ImportError:
    print("Error: usd-core not installed. Install with: pip install usd-core")
    sys.exit(1)


def validate_asset(asset_path):
    """
    Validate a USD asset file.
    
    What is a USD Asset?
    - A USD asset is typically a single USD file containing geometry, materials, or other 3D content
    - Assets are reusable building blocks that can be referenced by scenes
    - Examples: A character model, a prop, a material definition
    
    This function checks:
    1. File exists and can be opened
    2. All prims (3D objects) are valid
    3. References to other files are valid
    4. Layer composition is correct
    5. Best practices are followed
    """
    # Convert to absolute path and resolve any ".." or "." in the path
    asset_path = Path(asset_path).resolve()
    
    # Check if file exists
    if not asset_path.exists():
        print(f"ERROR: Asset file not found: {asset_path}")
        return False
    
    print(f"Validating asset: {asset_path}")
    
    # Open the USD file as a Stage
    # A Stage is USD's main container - think of it as the "scene" or "world"
    stage = Usd.Stage.Open(str(asset_path))
    if not stage:
        print(f"ERROR: Failed to open USD file: {asset_path}")
        return False
    
    # Initialize lists to collect problems
    errors = []      # Critical issues that prevent the asset from working
    warnings = []    # Issues that might cause problems but don't break the asset
    
    # Check for root layer (the main file itself)
    root_layer = stage.GetRootLayer()
    if not root_layer:
        errors.append("No root layer found")
        return False
    
    # Validate all prims in the asset
    # A "prim" is USD's term for any object (geometry, lights, cameras, materials, etc.)
    prim_count = 0
    for prim in stage.Traverse():  # Traverse walks through ALL prims in the hierarchy
        prim_count += 1
        
        # Check if this prim is valid
        if not prim.IsValid():
            errors.append(f"Invalid prim: {prim.GetPath()}")
            continue  # Skip to next prim
        
        # Check for broken references
        # References are USD's way of linking to other USD files
        if prim.HasAuthoredReferences():
            # Get all references this prim points to
            refs = prim.GetReferences().GetAddedOrExplicitItems()
            for ref in refs:
                ref_path = ref.assetPath  # The path to the referenced file
                if ref_path:
                    # Use USD's built-in asset resolver to find the file
                    resolved_layer = Sdf.Layer.FindOrOpen(ref_path)
                    if not resolved_layer:
                        # If USD's resolver can't find it, check if it's a relative path
                        if not ref_path.startswith("@"):  # "@" indicates USD asset path
                            # Try resolving relative to current layer's location
                            layer_path = root_layer.ResolvePath(ref_path)
                            if not layer_path or not Path(layer_path).exists():
                                # Warning (not error) because file might be elsewhere or created dynamically
                                warnings.append(f"Potential missing reference: {ref_path} at {prim.GetPath()}")
    
    print(f"Found {prim_count} prims")
    
    # Check layer composition (sublayers)
    # Sublayers are additional USD files stacked on top of the root layer
    if root_layer:
        sublayers = root_layer.subLayerPaths
        if sublayers:
            for sublayer_path in sublayers:
                # Resolve the sublayer path
                resolved_path = root_layer.ResolvePath(sublayer_path)
                if not resolved_path:
                    warnings.append(f"Cannot resolve sublayer: {sublayer_path}")
                elif not Path(resolved_path).exists():
                    warnings.append(f"Missing sublayer file: {resolved_path}")
    
    # Check for default prim (USD best practice)
    # Default prim tells tools which prim to focus on when opening the file
    if not stage.GetDefaultPrim():
        warnings.append("No default prim set (recommended for asset files)")
    
    # Report results
    if errors:
        print("\nERRORS:")
        for error in errors:
            print(f"  - {error}")
    
    if warnings:
        print("\nWARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    if not errors and not warnings:
        print("\n✓ Asset validation passed")
        return True
    
    if errors:
        print(f"\n✗ Asset validation failed with {len(errors)} error(s)")
    else:
        print(f"\n⚠ Asset validation passed with {len(warnings)} warning(s)")
    
    return len(errors) == 0


def validate_scene(root_file):
    """
    Validate entire USD scene.
    
    What is a USD Scene?
    - A scene is typically the "root" or "master" USD file that combines multiple layers
    - Scenes use "sublayers" to stack multiple USD files together
    - The root file references layer files (like AssetImport_LYR.usda) which then reference assets
    - Example: GoodStart_ROOT.usda combines multiple layer files to build the final scene
    
    This function checks:
    1. Root file exists and can be opened
    2. All sublayers exist and can be opened
    3. Layer ordering follows best practices (asset imports at bottom)
    4. All prims in the composed scene are valid
    5. Best practices are followed (default prim, etc.)
    """
    # Convert to absolute path
    root_file = Path(root_file).resolve()
    
    # Check if root file exists
    if not root_file.exists():
        print(f"ERROR: Root file not found: {root_file}")
        return False
    
    print(f"Validating scene: {root_file}")
    
    # Open the root USD file as a Stage
    # The stage represents the final composed scene (root + all sublayers combined)
    stage = Usd.Stage.Open(str(root_file))
    if not stage:
        print(f"ERROR: Failed to open root file: {root_file}")
        return False
    
    # Initialize lists to collect problems
    errors = []      # Critical issues
    warnings = []    # Potential issues
    
    # Check for root layer (the main file itself)
    root_layer = stage.GetRootLayer()
    if not root_layer:
        errors.append("No root layer found")
        return False
    
    # Validate all sublayers
    # Sublayers are additional USD files that are "stacked" on top of the root layer
    sublayers = root_layer.subLayerPaths
    print(f"\nFound {len(sublayers)} sublayers:")
    
    # Check each sublayer
    for i, sublayer_path in enumerate(sublayers):
        print(f"  {i+1}. {sublayer_path}")
        # Resolve the sublayer path (handle relative paths)
        resolved_path = root_layer.ResolvePath(sublayer_path)
        
        if not resolved_path:
            errors.append(f"Cannot resolve sublayer: {sublayer_path}")
        elif not Path(resolved_path).exists():
            errors.append(f"Missing sublayer file: {resolved_path}")
        else:
            # Validate sublayer can be opened as a USD layer
            sublayer_layer = Sdf.Layer.FindOrOpen(str(resolved_path))
            if not sublayer_layer:
                warnings.append(f"Cannot open sublayer: {resolved_path}")
            else:
                # Also try opening as a full Stage to validate composition
                sublayer_stage = Usd.Stage.Open(str(resolved_path))
                if not sublayer_stage:
                    warnings.append(f"Sublayer opens but stage validation failed: {resolved_path}")
    
    # Check layer ordering (USD best practice)
    # Asset import layers should be at the BOTTOM (last in list)
    # This allows other layers to override/modify imported assets
    if sublayers:
        last_layer = sublayers[-1]  # Last layer has highest "strength"
        if "AssetImport" in last_layer or "asset" in last_layer.lower():
            print("✓ Asset import layer correctly positioned at bottom")
        else:
            warnings.append("Consider placing asset import layer at bottom of subLayers array")
    
    # Check for default prim (USD best practice)
    if not stage.GetDefaultPrim():
        warnings.append("No default prim set (recommended for scene files)")
    
    # Validate all prims in the composed scene
    prim_count = 0
    invalid_prim_count = 0
    for prim in stage.Traverse():
        prim_count += 1
        if not prim.IsValid():
            invalid_prim_count += 1
            errors.append(f"Invalid prim: {prim.GetPath()}")
    
    print(f"\nScene contains {prim_count} prims")
    if invalid_prim_count > 0:
        print(f"  ⚠ {invalid_prim_count} invalid prim(s) found")
    
    # Report results
    if errors:
        print("\nERRORS:")
        for error in errors:
            print(f"  - {error}")
    
    if warnings:
        print("\nWARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    if not errors and not warnings:
        print("\n✓ Scene validation passed")
        return True
    
    if errors:
        print(f"\n✗ Scene validation failed with {len(errors)} error(s)")
    else:
        print(f"\n⚠ Scene validation passed with {len(warnings)} warning(s)")
    
    return len(errors) == 0


def main():
    """
    Main function - entry point when script is run from command line.
    
    This function implements AUTO-DETECTION logic:
    - It tries to figure out if the file is an asset or a scene
    - Uses heuristics: number of sublayers, filename patterns
    - Falls back to asset validation if uncertain
    
    Command-line arguments:
    - sys.argv[0] = script name (validate_usd.py)
    - sys.argv[1] = first argument (the USD file path to validate)
    """
    # Check if user provided a file path
    if len(sys.argv) < 2:
        print("Usage: python validate_usd.py <path_to_usd_file>")
        print("\nThis script auto-detects whether to validate as asset or scene.")
        print("For explicit control, use:")
        print("  python scripts/validate_asset.py <asset_file>")
        print("  python scripts/validate_scene.py <scene_file>")
        sys.exit(1)
    
    # Get the file path from command-line arguments
    usd_file = Path(sys.argv[1])
    
    # AUTO-DETECTION LOGIC:
    # Try to determine if this is an asset or a scene based on file structure
    
    # First, try to open the file to examine its structure
    stage = Usd.Stage.Open(str(usd_file))
    if stage:
        root_layer = stage.GetRootLayer()
        if root_layer:
            sublayers = root_layer.subLayerPaths
            
            # Heuristic 1: Number of sublayers
            # Scenes typically have multiple sublayers (e.g., 3-4+ layer files)
            # Assets typically have 0-1 sublayers (or none at all)
            
            # Heuristic 2: Filename pattern
            # Files with "ROOT" or "root" in the name are usually scenes
            # Examples: GoodStart_ROOT.usda, scene_root.usd
            
            # Decision logic:
            if len(sublayers) > 2 or "root" in usd_file.name.lower():
                # Likely a scene - validate as scene
                # Scenes have more complex validation (layer ordering, etc.)
                success = validate_scene(usd_file)
            else:
                # Likely an asset - validate as asset
                # Assets have simpler structure
                success = validate_asset(usd_file)
        else:
            # No root layer - can't determine, default to asset validation
            success = validate_asset(usd_file)
    else:
        # Can't open file - exit with error
        print(f"ERROR: Cannot open USD file: {usd_file}")
        sys.exit(1)
    
    # Exit with appropriate code:
    # - 0 = success (no errors)
    # - 1 = failure (has errors)
    sys.exit(0 if success else 1)


# This block runs only when the script is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()

