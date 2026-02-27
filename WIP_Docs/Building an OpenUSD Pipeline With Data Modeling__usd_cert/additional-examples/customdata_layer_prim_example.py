"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 4 (governance data by scope)

Why this script exists:
- It compares custom data usage at layer, prim, and attribute levels.
- This helps learners choose where operational metadata should live.

How to run:
- From the __usd_cert folder:
  python additional-examples/customdata_layer_prim_example.py

What to observe:
1) Layer customLayerData for global context.
2) Prim customData for object-level business metadata.
3) Attribute customData for field-specific context.
"""

from pxr import Sdf, Usd, UsdGeom

# Create a stage and get its root layer
stage = Usd.Stage.CreateInMemory()
root_layer = stage.GetRootLayer()

# ============================================================
# LAYER CUSTOMDATA
# ============================================================
print("=" * 60)
print("LAYER CUSTOMDATA EXAMPLE")
print("=" * 60)

# Set customData on the layer
root_layer.customLayerData = {
    "project": "Bicycle Simulation",
    "version": "1.0.0",
    "author": "Engineering Team",
    "created": "2024-02-16",
    "pipeline": {
        "software": "USD",
        "renderer": "Hydra",
        "exportSettings": {
            "compression": True,
            "precision": "float32"
        }
    },
    "tags": ["vehicle", "simulation", "prototype"]
}

# Access layer customData
print(f"\nLayer customData:")
print(f"  Project: {root_layer.customLayerData.get('project')}")
print(f"  Version: {root_layer.customLayerData.get('version')}")
print(f"  Author: {root_layer.customLayerData.get('author')}")
print(f"  Tags: {root_layer.customLayerData.get('tags')}")
print(f"  Renderer: {root_layer.customLayerData.get('pipeline', {}).get('renderer')}")
print(f"  Compression: {root_layer.customLayerData.get('pipeline', {}).get('exportSettings', {}).get('compression')}")

# ============================================================
# PRIM CUSTOMDATA
# ============================================================
print("\n" + "=" * 60)
print("PRIM CUSTOMDATA EXAMPLE")
print("=" * 60)

# Create a prim and set customData
prim_path = Sdf.Path("/bicycle")
prim = stage.DefinePrim(prim_path, "Xform")

# Set customData on the prim
# Note: Prim customData only supports basic types (string, number, bool, dict)
# Lists/arrays are NOT supported at the prim level
prim.SetCustomData({
    "assetId": "BIKE-001",
    "category": "Transportation",
    "status": "In Development",
    "owner": "Design Department",
    "specifications": {
        "frameType": "Mountain",
        "gearCount": 21,
        "weight_kg": 12.5,
        "color": "red"
    },
    "lastModified": "2024-02-16",
    "version": 3
})

# Access prim customData
custom_data = prim.GetCustomData()
print(f"\nPrim customData:")
print(f"  Asset ID: {custom_data.get('assetId')}")
print(f"  Category: {custom_data.get('category')}")
print(f"  Status: {custom_data.get('status')}")
print(f"  Owner: {custom_data.get('owner')}")
print(f"  Frame Type: {custom_data.get('specifications', {}).get('frameType')}")
print(f"  Weight: {custom_data.get('specifications', {}).get('weight_kg')} kg")
print(f"  Last Modified: {custom_data.get('lastModified')}")
print(f"  Version: {custom_data.get('version')}")

# You can also access individual keys directly
print(f"\nDirect access to specific key:")
print(f"  Asset ID (direct): {prim.GetCustomDataByKey('assetId')}")

# Check if a key exists
print(f"\nChecking if key exists:")
print(f"  Has 'assetId': {prim.HasCustomDataKey('assetId')}")
print(f"  Has 'nonexistent': {prim.HasCustomDataKey('nonexistent')}")

# ============================================================
# ATTRIBUTE CUSTOMDATA (for comparison)
# ============================================================
print("\n" + "=" * 60)
print("ATTRIBUTE CUSTOMDATA EXAMPLE")
print("=" * 60)

# Create an attribute with customData
attr = prim.CreateAttribute("tire:size", Sdf.ValueTypeNames.Float)
attr.Set(10)
attr.SetMetadata("customData", {
    "manufacturer": "Acme Tires Inc.",
    "model": "RoadMaster 3000",
    "partNumber": "TRE-2024-001",
    "warranty_months": 24
})

# Access attribute customData
attr_custom_data = attr.GetMetadata('customData')
print(f"\nAttribute customData:")
print(f"  Manufacturer: {attr_custom_data.get('manufacturer')}")
print(f"  Model: {attr_custom_data.get('model')}")
print(f"  Part Number: {attr_custom_data.get('partNumber')}")
print(f"  Warranty: {attr_custom_data.get('warranty_months')} months")

# ============================================================
# SUMMARY
# ============================================================
print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("Layer customData:    root_layer.customLayerData = {...}")
print("                     root_layer.customLayerData.get('key')")
print()
print("Prim customData:     prim.SetCustomData({...})")
print("                     prim.GetCustomData()")
print("                     prim.GetCustomDataByKey('key')")
print("                     prim.HasCustomDataKey('key')")
print()
print("Attribute customData: attr.SetMetadata('customData', {...})")
print("                      attr.GetMetadata('customData')")
