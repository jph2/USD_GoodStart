"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 3 (attribute authoring and inspection details)
- Chapter 4 (attribute-level metadata for governance)

Why this script exists:
- It shows authored attribute listing on a prim.
- It includes interpolation metadata to reinforce schema-aware context.

How to run:
- From the __usd_cert folder:
  python data-types/7b_attributes_examples.py

What to observe:
1) Authored value and type on tire:size.
2) Metadata assigned at attribute scope.
3) Difference between "all attributes" and "authored attributes".
"""

from pxr import Sdf, Usd, UsdGeom
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/bicycle")
prim = stage.DefinePrim(prim_path, "Xform")
attr = prim.CreateAttribute("tire:size", Sdf.ValueTypeNames.Float)
attr.Set(10)
attr.SetMetadata("interpolation", UsdGeom.Tokens.constant)

# Get all attributes
print("All Attributes:")
for attr in prim.GetAttributes():
    print(f"  Name: {attr.GetName()} | Value: {attr.Get()} | Type: {attr.GetTypeName()}")

# # Get only authored attributes
# print("Authored Attributes:")
# for attr in prim.GetAuthoredAttributes():
#     print(f"  {attr.GetName()}: {attr.Get()}")

# print()

# # Print specific metadata
# print(f"Interpolation Metadata: {attr.GetMetadata('interpolation')}")

# # Print all metadata
# print("\nAll Metadata:")
# for key in attr.GetAllMetadata():
#     print(f"  {key}: {attr.GetMetadata(key)}")