#!/usr/bin/env python3
"""
Update GoodStart_ROOT.usda subLayers and customLayerData to match the new folder layout.

New layout:
- 030_USD_LYR/       # general visual/layout/material layers
- 040_SIM_LYR/       # simulation layers
- 050_VARIANTS_LYR/  # variant/config layers
- 060_METADATA_LYR/  # metadata/standards layers

This script:
- Remaps subLayers paths to the correct folders based on layer type:
  * General layers (Opinion, Mtl_work, AssetImport) → 030_USD_LYR/
  * Variant layers → 050_VARIANTS_LYR/
  * Simulation layers → 040_SIM_LYR/
  * Metadata layers (AAS, OPCUA, etc.) → 060_METADATA_LYR/
- Optionally adds sample layers (sample_Sim_LYR.usda, sample_Metadata_LYR.usda) if missing
- Updates omni_layer.authoring_layer and omni_layer.locked entries to use correct paths

Usage:
    python scripts/update_root_layers.py GoodStart_ROOT.usda [--no-log] [--no-samples]
    
    --no-log      : Skip writing log file
    --no-samples  : Don't add sample layers automatically

You can also pass a different root file if desired.
"""

import sys
import os
from pathlib import Path
from datetime import datetime

try:
    from pxr import Sdf
except ImportError:
    print("Error: usd-core not installed. Install with: pip install usd-core")
    sys.exit(1)


# Layer basenames mapped to their correct folder paths
LAYER_MAPPING = {
    # General USD layers (030_USD_LYR)
    "your very Personal opinion_LYR.usda": "./030_USD_LYR/your very Personal opinion_LYR.usda",
    "Opinion_xyz_LYR.usda": "./030_USD_LYR/Opinion_xyz_LYR.usda",
    "Opinion_abc_LYR.usda": "./030_USD_LYR/Opinion_abc_LYR.usda",
    "Opinion_LYR.usda": "./030_USD_LYR/Opinion_LYR.usda",
    "Mtl_work_LYR.usda": "./030_USD_LYR/Mtl_work_LYR.usda",
    "Mtl_Work_LYR.usda": "./030_USD_LYR/Mtl_Work_LYR.usda",
    "AssetImport_LYR.usda": "./030_USD_LYR/AssetImport_LYR.usda",
    "Layout_LYR.usda": "./030_USD_LYR/Layout_LYR.usda",
    "Animation_LYR.usda": "./030_USD_LYR/Animation_LYR.usda",
    "Lighting_LYR.usda": "./030_USD_LYR/Lighting_LYR.usda",
    "sample_USD_LYR.usda": "./030_USD_LYR/sample_USD_LYR.usda",
    
    # Variant layers (050_VARIANTS_LYR)
    "Variant_LYR.usda": "./050_VARIANTS_LYR/Variant_LYR.usda",
    "sample_Variants_LYR.usda": "./050_VARIANTS_LYR/sample_Variants_LYR.usda",
    
    # Simulation layers (040_SIM_LYR)
    "sample_Sim_LYR.usda": "./040_SIM_LYR/sample_Sim_LYR.usda",
    
    # Metadata layers (060_METADATA_LYR)
    "sample_Metadata_LYR.usda": "./060_METADATA_LYR/sample_Metadata_LYR.usda",
    "AAS_LYR.usda": "./060_METADATA_LYR/AAS_LYR.usda",
    "OPCUA_LYR.usda": "./060_METADATA_LYR/OPCUA_LYR.usda",
    "CatenaX_LYR.usda": "./060_METADATA_LYR/CatenaX_LYR.usda",
}

# Sample layers to add if missing (optional - user can add manually if desired)
SAMPLE_LAYERS_TO_ADD = [
    "./030_USD_LYR/sample_USD_LYR.usda",
    "./040_SIM_LYR/sample_Sim_LYR.usda",
    "./050_VARIANTS_LYR/sample_Variants_LYR.usda",
    "./060_METADATA_LYR/sample_Metadata_LYR.usda",
]


def _get_layer_path(basename: str) -> str:
    """Return the canonical relative path for a layer based on its basename.
    
    If the layer is in the mapping, use that. Otherwise, try to infer from folder patterns
    or default to 030_USD_LYR for general layers.
    """
    if basename in LAYER_MAPPING:
        return LAYER_MAPPING[basename]
    
    # Fallback: check for folder patterns in old paths
    # This handles legacy paths that might still be in the file
    return f"./030_USD_LYR/{basename}"


def remap_subLayers(layer: Sdf.Layer, root_dir: Path, add_samples: bool = True):
    """Rewrite subLayerPaths to use the new folder structure and optionally add sample layers.
    
    Args:
        layer: The Sdf.Layer to update
        root_dir: Path to the root USD file
        add_samples: If True, add sample layers if they're missing
    
    Returns:
        (old_paths, new_paths) tuple for reporting
    """
    old_paths = list(layer.subLayerPaths)
    new_paths = []
    changes = []

    print(f"\nFound {len(old_paths)} subLayer(s):")
    for i, p in enumerate(old_paths, 1):
        print(f"  {i}. {p}")

    # Remap existing layers
    for p in old_paths:
        base = os.path.basename(p)
        new_p = None

        # Use mapping if available
        if base in LAYER_MAPPING:
            new_p = LAYER_MAPPING[base]
        elif "020_LYR_USD" in p or "030_LYR_USD" in p:
            # Legacy path format - use mapping or infer
            new_p = _get_layer_path(base)
        elif p.startswith("./030_USD_LYR/") or p.startswith("./040_SIM_LYR/") or \
             p.startswith("./050_VARIANTS_LYR/") or p.startswith("./060_METADATA_LYR/"):
            # Already in correct format, but might need remapping if basename is in mapping
            if base in LAYER_MAPPING:
                new_p = LAYER_MAPPING[base]
            else:
                new_p = p  # Keep as-is
        else:
            # Leave untouched (e.g., external layers)
            new_p = p

        new_paths.append(new_p)
        if p != new_p:
            changes.append((p, new_p))

    # Add sample layers if requested and missing
    if add_samples:
        existing_basenames = {os.path.basename(p) for p in new_paths}
        added_samples = []
        
        for sample_path in SAMPLE_LAYERS_TO_ADD:
            sample_basename = os.path.basename(sample_path)
            # Check if this sample layer already exists (by basename or exact path)
            if sample_basename not in existing_basenames and sample_path not in new_paths:
                # Verify the file exists before adding
                resolved = root_dir.parent / sample_path[2:]  # Remove "./"
                if resolved.exists():
                    new_paths.append(sample_path)
                    added_samples.append(sample_path)
                    print(f"\n+ Adding sample layer: {sample_path}")
                else:
                    print(f"\n⚠ Sample layer not found (skipping): {sample_path}")

        if added_samples:
            changes.extend([(None, p) for p in added_samples])

    if changes:
        print(f"\nUpdating {len([c for c in changes if c[0] is not None])} subLayer path(s):")
        for old, new in changes:
            if old is not None:
                print(f"  {old!r} -> {new!r}")
        layer.subLayerPaths = new_paths
    else:
        print("\n✓ All subLayer paths are already correct (no changes needed)")

    # Verify layer files exist
    print(f"\nVerifying layer files exist:")
    for new_p in new_paths:
        if new_p.startswith("./"):
            # Resolve relative to root file's directory
            resolved = root_dir.parent / new_p[2:]  # Remove "./"
            if resolved.exists():
                print(f"  ✓ {new_p}")
            else:
                print(f"  ⚠ {new_p} (file not found: {resolved})")

    return old_paths, new_paths


def remap_customLayerData(layer: Sdf.Layer) -> bool:
    """Update omni_layer authoring_layer and locked entries to new folder structure paths.
    
    Returns:
        True if changes were made, False otherwise
    """
    data = dict(layer.customLayerData)
    omni_layer = data.get("omni_layer")
    if not isinstance(omni_layer, dict):
        print("\nNo omni_layer customLayerData found (skipping)")
        return False

    changed = False

    # Update authoring_layer
    authoring = omni_layer.get("authoring_layer")
    if isinstance(authoring, str):
        base = os.path.basename(authoring)
        new_authoring = _get_layer_path(base)
        if authoring != new_authoring:
            print(f"\nUpdating authoring_layer:")
            print(f"  {authoring!r} -> {new_authoring!r}")
            omni_layer["authoring_layer"] = new_authoring
            changed = True
        else:
            print(f"\n✓ authoring_layer already correct: {authoring}")

    # Update locked dictionary
    locked = omni_layer.get("locked")
    if isinstance(locked, dict):
        new_locked = {}
        locked_changes = []
        for k, v in locked.items():
            base = os.path.basename(k)
            # Check if this layer is in our mapping or needs remapping
            if base in LAYER_MAPPING:
                new_key = LAYER_MAPPING[base]
            elif "020_LYR_USD" in k or "030_LYR_USD" in k:
                new_key = _get_layer_path(base)
            else:
                new_key = k  # Keep as-is
            
            if k != new_key:
                locked_changes.append((k, new_key))
            new_locked[new_key] = v
        
        if locked_changes:
            print(f"\nUpdating {len(locked_changes)} locked layer path(s):")
            for old, new in locked_changes:
                print(f"  {old!r} -> {new!r}")
            omni_layer["locked"] = new_locked
            changed = True
        else:
            print(f"\n✓ All locked layer paths already correct ({len(locked)} entries)")

    if changed:
        data["omni_layer"] = omni_layer
        layer.customLayerData = data

    return changed


def write_log(log_path: Path, root_path: Path, old_sub: list, new_sub: list, changed_omni: bool, changes_made: bool):
    """Write a log file documenting the changes made."""
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(f"USD Root Layer Update Log\n")
        f.write(f"{'=' * 60}\n")
        f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Root File: {root_path}\n")
        f.write(f"Changes Made: {'Yes' if changes_made else 'No'}\n")
        f.write(f"\n")
        
        if old_sub != new_sub:
            f.write(f"subLayers Changes:\n")
            f.write(f"-" * 60 + "\n")
            for old, new in zip(old_sub, new_sub):
                if old != new:
                    f.write(f"  OLD: {old}\n")
                    f.write(f"  NEW: {new}\n")
                    f.write(f"\n")
        
        if changed_omni:
            f.write(f"customLayerData Changes:\n")
            f.write(f"-" * 60 + "\n")
            f.write(f"  omni_layer.authoring_layer and/or omni_layer.locked updated\n")
            f.write(f"\n")
        
        f.write(f"Final subLayers ({len(new_sub)}):\n")
        f.write(f"-" * 60 + "\n")
        for i, p in enumerate(new_sub, 1):
            f.write(f"  {i}. {p}\n")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/update_root_layers.py <root_usd_file> [--no-log] [--no-samples]")
        print("       --no-log      : Skip writing log file")
        print("       --no-samples  : Don't add sample layers (sample_Sim_LYR.usda, sample_Metadata_LYR.usda)")
        sys.exit(1)

    write_log_file = "--no-log" not in sys.argv
    
    root_path = Path(sys.argv[1]).resolve()
    if not root_path.exists():
        print(f"ERROR: Root file not found: {root_path}")
        sys.exit(1)

    print(f"Opening root layer: {root_path}")
    layer = Sdf.Layer.FindOrOpen(str(root_path))
    if not layer:
        print(f"ERROR: Failed to open layer: {root_path}")
        print("       Make sure usd-core is installed: pip install usd-core")
        sys.exit(1)

    print(f"✓ Successfully opened layer: {layer.identifier}")
    print(f"  File size: {root_path.stat().st_size} bytes")

    # Check if --no-samples flag is present
    add_samples = "--no-samples" not in sys.argv
    
    old_sub, new_sub = remap_subLayers(layer, root_path, add_samples=add_samples)
    changed_omni = remap_customLayerData(layer)

    changes_made = old_sub != new_sub or changed_omni

    if changes_made:
        print(f"\nSaving changes to: {root_path}")
        if not layer.Save():
            print(f"ERROR: Failed to save layer!")
            sys.exit(1)
        print("✓ File saved successfully")
        
        # Write log file
        if write_log_file:
            log_path = root_path.parent / f"{root_path.stem}_update_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            write_log(log_path, root_path, old_sub, new_sub, changed_omni, changes_made)
            print(f"✓ Log written to: {log_path.name}")
    else:
        print("\n✓ No changes needed - file is already up to date")

    print(f"\nFinal subLayers ({len(layer.subLayerPaths)}):")
    for i, p in enumerate(layer.subLayerPaths, 1):
        print(f"  {i}. {p}")

    print("\nDone. Open the root file in usdview or Omniverse to verify the layer stack.")


if __name__ == "__main__":
    main()


