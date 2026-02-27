"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 4 (metadata at layer, prim, and attribute scope)

Why this script exists:
- It is a broad "metadata lab" showing set/get/list APIs by scope.
- It helps learners choose correct governance placement for Station 7 data.

How to run:
- From the __usd_cert folder:
  python data-types/7c_metadata_examples.py

What to observe:
1) Layer-level metadata and customLayerData.
2) Prim-level metadata and customData.
3) Attribute-level metadata and authored metadata introspection.
4) Practical API summary for set/list patterns.
"""

from pxr import Sdf, Usd, UsdGeom

# ============================================================
# METADATA - METHODS

### General
# Has:   'HasAuthoredMetadata'/'HasAuthoredMetadataDictKey'/'HasMetadata'/'HasMetadataDictKey'
# Get:   'GetAllAuthoredMetadata'/'GetAllMetadata'/'GetMetadata'/'GetMetadataByDictKey'
# Set:   'SetMetadata'/'SetMetadataByDictKey', 
# Clear: 'ClearMetadata'/'ClearMetadataByDictKey'
### Asset Info (Prims only)
# Has: 'HasAssetInfo'/'HasAssetInfoKey'/'HasAuthoredAssetInfo'/'HasAuthoredAssetInfoKey'
# Get: 'GetAssetInfo'/'GetAssetInfoByKey'
# Set: 'SetAssetInfo'/'SetAssetInfoByKey', 
# Clear: 'ClearAssetInfo'/'ClearAssetInfoByKey'
### Custom Data (Prims, Properties(Attributes/Relationships), Layers)
# Has: 'HasCustomData'/'HasCustomDataKey'/'HasAuthoredCustomData'/'HasAuthoredCustomDataKey'
# Get: 'GetCustomData'/'GetCustomDataByKey'
# Set: 'SetCustomData'/'SetCustomDataByKey', 
# Clear: 'ClearCustomData'/'ClearCustomDataByKey'
# ============================================================

# Create a stage and get its root layer
stage = Usd.Stage.CreateInMemory()
root_layer = stage.GetRootLayer()

# ============================================================
# LAYER METADATA - SET METHODS
# ============================================================
print("=" * 70)
print("LAYER METADATA - SET METHODS")
print("=" * 70)

# Set various layer metadata
root_layer.defaultPrim = "bicycle"
root_layer.comment = "This is a bicycle simulation layer"

# Set custom layer data
root_layer.customLayerData = {
    "project": "Bicycle Simulation",
    "version": "1.0.0"
}

print("Layer metadata set successfully")
print(f"  Comment: {root_layer.comment}")
print(f"  Default Prim: {root_layer.defaultPrim}")
print(f"  customLayerData: {root_layer.customLayerData['project']}")


# ============================================================
# LIST ALL LAYER METADATA
# ============================================================
print("\n" + "=" * 70)
print("ALL LAYER METADATA")
print("=" * 70)

# Layer metadata is accessed through properties, not GetAllMetadata()
# Here are the main layer metadata fields:
layer_metadata = {
    "comment": root_layer.comment,
    "defaultPrim": root_layer.defaultPrim,
    "customLayerData": root_layer.customLayerData
}

for key, value in layer_metadata.items():
    if value:  # Only print if value is set
        print(f"  {key:25s}: {value}")

# ============================================================
# PRIM METADATA - SET METHODS
# ============================================================
print("\n" + "=" * 70)
print("PRIM METADATA - SET METHODS")
print("=" * 70)

# Create a prim
prim_path = Sdf.Path("/bicycle")
prim = stage.DefinePrim(prim_path, "Xform")

# Set various prim metadata using SetMetadata()
prim.SetMetadata("comment", "Main bicycle transform")
prim.SetMetadata("documentation", "Root transform for the bicycle asset")
prim.SetMetadata("hidden", False)
prim.SetMetadata("kind", "component")
prim.SetMetadata("active", True)

# Set custom data
prim.SetCustomData({
    "assetId": "BIKE-001",
    "version": 1
})

# Set specific metadata using dedicated methods
prim.SetActive(True)
prim.SetHidden(False)

print("Prim metadata set successfully")
print(f"  Comment: {prim.GetMetadata('comment')}")
print(f"  Documentation: {prim.GetMetadata('documentation')}")
print(f"  Kind: {prim.GetMetadata('kind')}")
print(f"  Active: {prim.IsActive()}")
print(f"  Hidden: {prim.IsHidden()}")

# ============================================================
# LIST ALL PRIM METADATA
# ============================================================
print("\n" + "=" * 70)
print("ALL PRIM METADATA")
print("=" * 70)

# Get all metadata as a dictionary
all_prim_metadata = prim.GetAllMetadata()
for key in sorted(all_prim_metadata.keys()):
    value = prim.GetMetadata(key)
    print(f"  {key:25s}: {value}")

print("\n" + "-" * 70)
print("AUTHORED PRIM METADATA ONLY")
print("-" * 70)

# Get only authored metadata
authored_metadata = prim.GetAllAuthoredMetadata()
for key in sorted(authored_metadata.keys()):
    value = prim.GetMetadata(key)
    print(f"  {key:25s}: {value}")

# ============================================================
# ATTRIBUTE METADATA - SET METHODS
# ============================================================
print("\n" + "=" * 70)
print("ATTRIBUTE METADATA - SET METHODS")
print("=" * 70)

# Create an attribute
attr = prim.CreateAttribute("tire:size", Sdf.ValueTypeNames.Float)
attr.Set(10)

# Set various attribute metadata using SetMetadata()
attr.SetMetadata("comment", "Tire size in inches")
attr.SetMetadata("documentation", "Standard tire size measurement")
attr.SetMetadata("displayName", "Tire Size")
attr.SetMetadata("hidden", False)
attr.SetMetadata("interpolation", UsdGeom.Tokens.constant)

# Set custom data
# attr.SetMetadata("customData", {
#     "manufacturer": "Acme Tires",
#     "partNumber": "TRE-001"
# })

attr.SetCustomData({
    "manufacturer": "Acme Tires",
    "partNumber": "TRE-001"
})

print("Attribute metadata set successfully")
print(f"  Comment: {attr.GetMetadata('comment')}")
print(f"  Documentation: {attr.GetMetadata('documentation')}")
print(f"  Display Name: {attr.GetMetadata('displayName')}")
print(f"  Interpolation: {attr.GetMetadata('interpolation')}")
print(f"  Custom Data: {attr.GetMetadata('customData')}")

# ============================================================
# LIST ALL ATTRIBUTE METADATA
# ============================================================
print("\n" + "=" * 70)
print("ALL ATTRIBUTE METADATA")
print("=" * 70)

# Get all metadata as a dictionary
all_attr_metadata = attr.GetAllMetadata()
for key in sorted(all_attr_metadata.keys()):
    value = attr.GetMetadata(key)
    print(f"  {key:25s}: {value}")

print("\n" + "-" * 70)
print("AUTHORED ATTRIBUTE METADATA ONLY")
print("-" * 70)

# Get only authored metadata
authored_attr_metadata = attr.GetAllAuthoredMetadata()
for key in sorted(authored_attr_metadata.keys()):
    value = attr.GetMetadata(key)
    print(f"  {key:25s}: {value}")

# # ============================================================
# # SUMMARY OF SET METHODS
# # ============================================================
# print("\n" + "=" * 70)
# print("SUMMARY - SET METHODS")
# print("=" * 70)
# print("""
# LAYER:
#   root_layer.comment = "..."
#   root_layer.documentation = "..."
#   root_layer.defaultPrim = "primName"
#   root_layer.startTimeCode = 0
#   root_layer.endTimeCode = 100
#   root_layer.framesPerSecond = 24
#   root_layer.customLayerData = {...}

# PRIM:
#   prim.SetMetadata("key", value)
#   prim.SetCustomData({...})
#   prim.SetActive(True)
#   prim.SetHidden(False)

# ATTRIBUTE:
#   attr.SetMetadata("key", value)
#   attr.SetMetadata("customData", {...})
# """)

# # ============================================================
# # SUMMARY OF LIST METHODS
# # ============================================================
# print("=" * 70)
# print("SUMMARY - LIST METHODS")
# print("=" * 70)
# print("""
# LAYER:
#   # Access through properties (no GetAllMetadata() method)
#   root_layer.comment
#   root_layer.documentation
#   root_layer.defaultPrim
#   root_layer.customLayerData
#   # etc.

# PRIM:
#   prim.GetAllMetadata()          # Returns dict of all metadata
#   prim.GetAllAuthoredMetadata()  # Returns dict of authored metadata only
#   prim.GetMetadata("key")        # Get specific metadata value

# ATTRIBUTE:
#   attr.GetAllMetadata()          # Returns dict of all metadata
#   attr.GetAllAuthoredMetadata()  # Returns dict of authored metadata only
#   attr.GetMetadata("key")        # Get specific metadata value
# """)
