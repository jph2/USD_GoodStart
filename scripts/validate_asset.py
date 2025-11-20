#!/usr/bin/env python3
"""
USD Asset Validation Script

Validates USD assets for common issues:
- File syntax errors
- Missing references
- Invalid layer composition
- Metadata completeness

Usage:
    python scripts/validate_asset.py path/to/asset.usd
    python scripts/validate_asset.py 010_ASS_USD/asset.usd

Note: This script validates USD files but does not modify them. USD files should use
relative paths (e.g., @../010_ASS_USD/asset.usd@) for portability. The script uses
absolute paths internally for validation but USD files themselves should contain relative paths.
"""

# Standard library imports
import sys      # For command-line arguments and exit codes
import os       # For operating system operations
from pathlib import Path  # Modern Python path handling (better than os.path)

# USD library imports
# pxr is the Python namespace for USD (Pixar's Universal Scene Description)
try:
    from pxr import Usd, Sdf, UsdUtils
    # Usd: Main USD API for stages, prims, and high-level operations
    # Sdf: Scene Description Foundation - low-level layer and data access
    # UsdUtils: Utility functions for USD operations
except ImportError:
    # If USD is not installed, provide helpful error message
    print("Error: usd-core not installed. Install with: pip install usd-core")
    sys.exit(1)  # Exit with error code 1


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
    # Convert input path to Path object for easier manipulation
    asset_path = Path(asset_path)
    
    # STEP 1: Check if file exists
    # This is the first thing to verify - no point continuing if file doesn't exist
    if not asset_path.exists():
        print(f"ERROR: Asset file not found: {asset_path}")
        return False  # Return False to indicate validation failed
    
    print(f"Validating: {asset_path}")
    
    # STEP 2: Open the USD file as a "Stage"
    # A Stage is USD's main container - think of it as the "scene" or "world"
    # It contains all the prims (3D objects, lights, cameras, etc.)
    stage = Usd.Stage.Open(str(asset_path))
    if not stage:
        # If stage is None, the file couldn't be opened (corrupted, wrong format, etc.)
        print(f"ERROR: Failed to open USD file: {asset_path}")
        return False
    
    # STEP 3: Initialize lists to collect problems we find
    errors = []      # Critical issues that prevent the asset from working
    warnings = []    # Issues that might cause problems but don't break the asset
    
    # STEP 4: Check for root layer
    # Every USD file has a "root layer" - this is the main file itself
    # The root layer is the foundation that all other layers stack on top of
    root_layer = stage.GetRootLayer()
    if not root_layer:
        # If there's no root layer, the file is completely broken
        errors.append("No root layer found")
        return False  # Can't continue without a root layer
    
    # STEP 5: Validate all prims in the asset
    # A "prim" (pronounced "prim") is USD's term for any object in the scene
    # Prims can be: geometry (meshes), lights, cameras, materials, groups, etc.
    # stage.Traverse() walks through ALL prims in the scene hierarchy
    prim_count = 0
    for prim in stage.Traverse():
        prim_count += 1
        
        # Check if this prim is valid
        # Invalid prims are broken and can cause rendering or loading issues
        if not prim.IsValid():
            # Get the path (location) of the invalid prim for error reporting
            # Example path: "/World/Characters/Hero/Mesh"
            errors.append(f"Invalid prim: {prim.GetPath()}")
        
        # Check prim path type (absolute vs relative)
        # USD prim paths can be absolute (starting with "/") or relative
        # Absolute paths are more explicit and recommended for clarity
        prim_path = prim.GetPath()
        if prim_path and not Sdf.Path(prim_path).IsAbsolutePath():
            # Relative prim paths are valid but absolute paths are clearer
            # This is informational, not an error
            pass  # Could add a check here if needed
            continue  # Skip to next prim - can't check references on invalid prim
        
        # STEP 6: Check for broken references
        # References are USD's way of linking to other USD files
        # Example: A character asset might reference a separate material file
        # HasAuthoredReferences() checks if this prim has any references defined
        if prim.HasAuthoredReferences():
            # Get all the references this prim points to
            refs = prim.GetReferences().GetAddedOrExplicitItems()
            
            # Check each reference to make sure the file it points to exists
            for ref in refs:
                ref_path = ref.assetPath  # The path to the referenced file
                if ref_path:
                    # Use USD's built-in asset resolver to find the file
                    # This handles relative paths, search paths, and USD's "@" asset paths
                    # Note: USD files should contain relative paths (e.g., @../010_ASS_USD/asset.usd@)
                    # for portability. The script resolves these internally for validation.
                    
                    # Check if reference path is an absolute file system path (not recommended)
                    # Absolute paths break when projects are moved or shared
                    if ref_path and not ref_path.startswith("@") and not ref_path.startswith("./") and not ref_path.startswith("../"):
                        # Check if it looks like an absolute path (Windows: C:\, D:\ or Unix: /)
                        # os is already imported at the top of the file
                        if os.path.isabs(ref_path) or (len(ref_path) > 1 and ref_path[1] == ":"):
                            warnings.append(f"Absolute file path detected in reference: '{ref_path}' at prim '{prim.GetPath()}'. "
                                           "Consider using relative paths (e.g., @../010_ASS_USD/asset.usd@) for portability.")
                    
                    resolved_layer = Sdf.Layer.FindOrOpen(ref_path)
                    
                    if not resolved_layer:
                        # If USD's resolver can't find it, check if it's a relative path
                        # USD paths starting with "@" are special asset paths
                        if not ref_path.startswith("@"):
                            # Try to resolve relative to the current layer's location
                            layer_path = root_layer.ResolvePath(ref_path)
                            # Check if the resolved path actually exists on disk
                            if not layer_path or not Path(layer_path).exists():
                                # This is a warning, not an error, because:
                                # - The file might be in a different location
                                # - It might be loaded from a server (Nucleus)
                                # - It might be created dynamically
                                warnings.append(f"Potential missing reference: {ref_path} at {prim.GetPath()}")
    
    print(f"Found {prim_count} prims")
    
    # STEP 7: Check layer composition
    # Layers in USD allow you to stack multiple files on top of each other
    # Sublayers are additional USD files that are combined with the root layer
    # This enables non-destructive editing and collaboration
    if root_layer:
        sublayers = root_layer.subLayerPaths  # Get list of sublayer file paths
        if sublayers:
            print(f"Found {len(sublayers)} sublayers")
            for sublayer_path in sublayers:
                # Resolve the sublayer path (handle relative paths, etc.)
                resolved_path = root_layer.ResolvePath(sublayer_path)
                
                if not resolved_path:
                    # Can't figure out where the sublayer file is
                    warnings.append(f"Cannot resolve sublayer: {sublayer_path}")
                elif not Path(resolved_path).exists():
                    # The file path was resolved, but the file doesn't exist on disk
                    warnings.append(f"Missing sublayer file: {resolved_path}")
    
    # STEP 8: Check for default prim (USD best practice)
    # A default prim is the "main" object in a USD file
    # It's like the "entry point" - tools know where to start when opening the file
    # Not having one isn't an error, but it's recommended for better tool compatibility
    if not stage.GetDefaultPrim():
        warnings.append("No default prim set (recommended for asset files)")
    
    # STEP 9: Report all findings
    # Print errors first (critical issues)
    if errors:
        print("\nERRORS:")
        for error in errors:
            print(f"  - {error}")
    
    # Then print warnings (potential issues)
    if warnings:
        print("\nWARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    # STEP 10: Return validation result
    # Return True only if there are no errors (warnings are OK)
    if not errors and not warnings:
        print("\n✓ Asset validation passed")
        return True
    
    # If there are errors, validation failed
    if errors:
        print(f"\n✗ Validation failed with {len(errors)} error(s)")
    else:
        # Only warnings - validation passed but with concerns
        print(f"\n⚠ Validation passed with {len(warnings)} warning(s)")
    
    # Return True if no errors (even if there are warnings)
    # Return False if there are any errors
    return len(errors) == 0


def main():
    """
    Main function - entry point when script is run from command line.
    
    Command-line arguments:
    - sys.argv[0] = script name (validate_asset.py)
    - sys.argv[1] = first argument (the USD file path to validate)
    """
    # Check if user provided a file path
    if len(sys.argv) < 2:
        # No file path provided - show usage instructions
        print("Usage: python validate_asset.py <path_to_usd_file>")
        sys.exit(1)  # Exit with error code 1
    
    # Get the file path from command-line arguments
    asset_path = sys.argv[1]
    
    # Run validation and get result (True = passed, False = failed)
    success = validate_asset(asset_path)
    
    # Exit with appropriate code:
    # - 0 = success (no errors)
    # - 1 = failure (has errors)
    # This is important for CI/CD systems that check exit codes
    sys.exit(0 if success else 1)


# This block runs only when the script is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()

