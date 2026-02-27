"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 4 (metadata API coverage)
- Chapter 8 (validation and governance audit readiness)

Why this script exists:
- It provides an end-to-end "set and inspect" matrix for metadata APIs.
- Useful for defining consistent governance checklists in pipelines.

How to run:
- From the __usd_cert folder:
  python additional-examples/metadata_set_and_list_example.py

What to observe:
1) Layer metadata fields and customLayerData.
2) Prim metadata plus authored/all metadata listing.
3) Attribute metadata and customData listing patterns.
"""

from pxr import Sdf, Usd, UsdGeom

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
root_layer.comment = "This is a bicycle simulation layer"
root_layer.documentation = "Complete documentation for the bicycle asset"
root_layer.defaultPrim = "bicycle"
root_layer.startTimeCode = 0
root_layer.endTimeCode = 100
root_layer.framesPerSecond = 24
root_layer.timeCodesPerSecond = 24
root_layer.owner = "NV"
root_layer.sessionOwner = "NV"

# Set custom layer data
root_layer.customLayerData = {
    "project": "Bicycle Simulation",
    "version": "1.0.0"
}

print("Layer metadata set successfully")
print(f"  Comment: {root_layer.comment}")
print(f"  Documentation: {root_layer.documentation}")
print(f"  Default Prim: {root_layer.defaultPrim}")
print(f"  Time Range: {root_layer.startTimeCode} - {root_layer.endTimeCode}")
print(f"  FPS: {root_layer.framesPerSecond}")
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
    "documentation": root_layer.documentation,
    "defaultPrim": root_layer.defaultPrim,
    "startTimeCode": root_layer.startTimeCode,
    "endTimeCode": root_layer.endTimeCode,
    "framesPerSecond": root_layer.framesPerSecond,
    "timeCodesPerSecond": root_layer.timeCodesPerSecond,
    "customLayerData": root_layer.customLayerData,
    "owner": root_layer.owner,
    "sessionOwner": root_layer.sessionOwner,
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
attr.SetMetadata("customData", {
    "manufacturer": "Acme Tires",
    "partNumber": "TRE-001"
})

print("Attribute metadata set successfully")
print(f"  Comment: {attr.GetMetadata('comment')}")
print(f"  Documentation: {attr.GetMetadata('documentation')}")
print(f"  Display Name: {attr.GetMetadata('displayName')}")
print(f"  Interpolation: {attr.GetMetadata('interpolation')}")

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

# ============================================================
# SUMMARY OF SET METHODS
# ============================================================
print("\n" + "=" * 70)
print("SUMMARY - SET METHODS")
print("=" * 70)
print("""
LAYER:
  root_layer.comment = "..."
  root_layer.documentation = "..."
  root_layer.defaultPrim = "primName"
  root_layer.startTimeCode = 0
  root_layer.endTimeCode = 100
  root_layer.framesPerSecond = 24
  root_layer.customLayerData = {...}

PRIM:
  prim.SetMetadata("key", value)
  prim.SetCustomData({...})
  prim.SetActive(True)
  prim.SetHidden(False)

ATTRIBUTE:
  attr.SetMetadata("key", value)
  attr.SetMetadata("customData", {...})
""")

# ============================================================
# SUMMARY OF LIST METHODS
# ============================================================
print("=" * 70)
print("SUMMARY - LIST METHODS")
print("=" * 70)
print("""
LAYER:
  # Access through properties (no GetAllMetadata() method)
  root_layer.comment
  root_layer.documentation
  root_layer.defaultPrim
  root_layer.customLayerData
  # etc.

PRIM:
  prim.GetAllMetadata()          # Returns dict of all metadata
  prim.GetAllAuthoredMetadata()  # Returns dict of authored metadata only
  prim.GetMetadata("key")        # Get specific metadata value

ATTRIBUTE:
  attr.GetAllMetadata()          # Returns dict of all metadata
  attr.GetAllAuthoredMetadata()  # Returns dict of authored metadata only
  attr.GetMetadata("key")        # Get specific metadata value
""")
