"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 1 (attributes vs relationships as the core vocabulary)

Why this script exists:
- It prints prim properties and classifies each property type.
- This makes the "two buckets only" model concrete and inspectable.

How to run:
- From the __usd_cert folder:
  python data-types/6a_property_example.py

What to observe:
1) Attributes printed separately from relationships.
2) How schema-authored properties appear on typical UsdGeom prims.
3) Why property inspection is the first debugging tool in data modeling.
"""

from pxr import Usd, UsdGeom, Gf

file_path = "_assets/attributes_ex1.usda"

stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

# Define a sphere under the World xForm:
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Sphere"))

# Define a cube under the World xForm and set it to be 5 units away from the sphere:
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube"))
UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5, 0, 0))
cube.GetPrim().CreateRelationship("material:binding")

# # Get the property names of the cube prim:
# cube_prop_names = cube.GetPrim().GetPropertyNames()

# # Print the property names:
# for prop_name in cube_prop_names:
#     print(prop_name)

# ================================================================
# print the properties of the cube prim:
cube_props = cube.GetPrim().GetProperties()
# cube_props = cube.GetPrim().GetAuthoredProperties()

for prop in cube_props:
    # print Attributes
    if isinstance(prop, Usd.Attribute):
        print(f"ATTRIBUTE: {prop.GetName()}")
    
    # print Relationships
    elif isinstance(prop, Usd.Relationship):
        print(f"RELATIONSHIP: {prop.GetName()}")

# ================================================================

stage.Save()