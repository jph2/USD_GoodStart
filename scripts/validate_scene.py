#!/usr/bin/env python3
"""
USD Scene Validation Script

Validates the entire scene (root file and all layers) for:
- Layer composition correctness
- Asset references
- Missing files
- Layer ordering

Usage:
    python scripts/validate_scene.py GoodStart_ROOT.usda
"""

# Standard library imports
import sys      # For command-line arguments and exit codes
import os       # For operating system operations
from pathlib import Path  # Modern Python path handling

# USD library imports
try:
    from pxr import Usd, Sdf
    # Usd: Main USD API for stages, prims, and high-level operations
    # Sdf: Scene Description Foundation - low-level layer and data access
except ImportError:
    print("Error: usd-core not installed. Install with: pip install usd-core")
    sys.exit(1)


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
    # Convert input path to Path object
    root_file = Path(root_file)
    
    # STEP 1: Check if root file exists
    if not root_file.exists():
        print(f"ERROR: Root file not found: {root_file}")
        return False
    
    print(f"Validating scene: {root_file}")
    
    # STEP 2: Open the root USD file as a Stage
    # The stage represents the final composed scene (root + all sublayers combined)
    stage = Usd.Stage.Open(str(root_file))
    if not stage:
        print(f"ERROR: Failed to open root file: {root_file}")
        return False
    
    # STEP 3: Initialize lists to collect problems
    errors = []      # Critical issues
    warnings = []    # Potential issues
    
    # STEP 4: Check for root layer
    # The root layer is the main file itself
    root_layer = stage.GetRootLayer()
    if not root_layer:
        errors.append("No root layer found")
        return False
    
    # STEP 5: Validate all sublayers
    # Sublayers are additional USD files that are "stacked" on top of the root layer
    # They are listed in the root file's subLayers metadata
    # Example: subLayers = [@./020_LYR_USD/AssetImport_LYR.usda@, ...]
    sublayers = root_layer.subLayerPaths  # Get list of sublayer file paths
    print(f"\nFound {len(sublayers)} sublayers:")
    
    # Check each sublayer to make sure it exists and can be opened
    for i, sublayer_path in enumerate(sublayers):
        print(f"  {i+1}. {sublayer_path}")  # Show which layer we're checking
        
        # Resolve the sublayer path
        # This handles relative paths (like ./020_LYR_USD/file.usda)
        # and converts them to absolute paths
        resolved_path = root_layer.ResolvePath(sublayer_path)
        
        if not resolved_path:
            # USD couldn't figure out where this file is
            # This is an error because the scene won't work without all layers
            errors.append(f"Cannot resolve sublayer: {sublayer_path}")
        elif not Path(resolved_path).exists():
            # The path was resolved, but the file doesn't exist on disk
            errors.append(f"Missing sublayer file: {resolved_path}")
        else:
            # File exists - now verify it can actually be opened as a USD file
            # First check at the Sdf (low-level) layer level
            sublayer_layer = Sdf.Layer.FindOrOpen(str(resolved_path))
            if not sublayer_layer:
                # File exists but can't be opened as a USD layer (corrupted?)
                warnings.append(f"Cannot open sublayer: {resolved_path}")
            else:
                # Layer opens OK, but also try opening as a full Stage
                # This validates the layer's composition (references, sublayers, etc.)
                sublayer_stage = Usd.Stage.Open(str(resolved_path))
                if not sublayer_stage:
                    # Layer opens but stage validation fails (composition issues?)
                    warnings.append(f"Sublayer opens but stage validation failed: {resolved_path}")
    
    # STEP 6: Check layer ordering (USD best practice)
    # In USD, layers are applied from bottom to top
    # The last layer in the list has the highest "strength" (overrides earlier layers)
    # Best practice: Asset import layers should be at the BOTTOM (last in list)
    # This way, other layers can override/modify the imported assets
    if sublayers:
        last_layer = sublayers[-1]  # Get the last layer in the list
        # Check if it's an asset import layer (by name pattern)
        if "AssetImport" in last_layer or "asset" in last_layer.lower():
            print("✓ Asset import layer correctly positioned at bottom")
        else:
            # Not an error, but a recommendation for better organization
            warnings.append("Consider placing asset import layer at bottom of subLayers array")
    
    # STEP 7: Check for default prim (USD best practice)
    # A default prim tells tools which prim to focus on when opening the file
    # Not required, but recommended for better tool compatibility
    if not stage.GetDefaultPrim():
        warnings.append("No default prim set (recommended for scene files)")
    
    # STEP 8: Validate all prims in the composed scene
    # After all layers are combined, check that all resulting prims are valid
    prim_count = 0
    invalid_prim_count = 0
    for prim in stage.Traverse():
        prim_count += 1
        if not prim.IsValid():
            invalid_prim_count += 1
            # Invalid prims are broken and will cause problems
            errors.append(f"Invalid prim: {prim.GetPath()}")
    
    print(f"\nScene contains {prim_count} prims")
    if invalid_prim_count > 0:
        print(f"  ⚠ {invalid_prim_count} invalid prim(s) found")
    
    # STEP 9: Check for composition errors (placeholder for future checks)
    # Composition is how USD combines layers, references, variants, etc.
    # This is a placeholder that can be extended with specific composition validation
    composition_query = Usd.CompositionQuery(stage.GetPseudoRoot())
    if composition_query:
        # Future: Could check for circular references, invalid composition arcs, etc.
        pass  # Can be extended with specific composition checks
    
    # STEP 10: Report all findings
    if errors:
        print("\nERRORS:")
        for error in errors:
            print(f"  - {error}")
    
    if warnings:
        print("\nWARNINGS:")
        for warning in warnings:
            print(f"  - {warning}")
    
    # STEP 11: Return validation result
    if not errors and not warnings:
        print("\n✓ Scene validation passed")
        return True
    
    if errors:
        print(f"\n✗ Scene validation failed with {len(errors)} error(s)")
    else:
        print(f"\n⚠ Scene validation passed with {len(warnings)} warning(s)")
    
    # Return True if no errors (warnings are OK), False if errors exist
    return len(errors) == 0


def main():
    """
    Main function - entry point when script is run from command line.
    
    Command-line arguments:
    - sys.argv[0] = script name (validate_scene.py)
    - sys.argv[1] = first argument (the root USD file path to validate)
    """
    # Check if user provided a file path
    if len(sys.argv) < 2:
        print("Usage: python validate_scene.py <path_to_root_usd_file>")
        sys.exit(1)
    
    # Get the root file path from command-line arguments
    root_file = sys.argv[1]
    
    # Run validation and get result (True = passed, False = failed)
    success = validate_scene(root_file)
    
    # Exit with appropriate code:
    # - 0 = success (no errors)
    # - 1 = failure (has errors)
    # Important for CI/CD systems that check exit codes
    sys.exit(0 if success else 1)


# This block runs only when the script is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()

