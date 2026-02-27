"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 1 (working with authored attributes in practice)

Why this script exists:
- It compares generic attribute access with schema-aware accessors.
- This helps learners understand when to prefer schema API methods.

How to run:
- From the __usd_cert folder:
  python data-types/6b_property_example.py

What to observe:
1) Full attribute list on a cube prim.
2) Values via GetAttribute("name") and schema helpers (GetSizeAttr, etc.).
3) Safe mutation of authored values and immediate read-back.
"""

from pxr import Usd, UsdGeom, Gf

file_path = "_assets/attributes_ex2.usda"
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Sphere"))
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube"))
UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5, 0, 0))

# Get the attributes of the cube prim
cube_attrs = cube.GetPrim().GetAttributes()
for attr in cube_attrs:
    print(attr)

# # Get the authored attributes of the cube prim
# cube_attrs = cube.GetPrim().GetAuthoredAttributes()
# for attr in cube_attrs:
#     print(attr)

# you can also use GetAttribute() to access attributes
print("Size: ", cube.GetPrim().GetAttribute("size").Get())
print("Extent: ", cube.GetPrim().GetAttribute("extent").Get())
print("Display Color: ", cube.GetPrim().GetAttribute("displayColor").Get())


#=============================== schema based property ===================
# Get the size, display color, and extent attributes of the cube
cube_size: Usd.Attribute = cube.GetSizeAttr()
cube_displaycolor: Usd.Attribute = cube.GetDisplayColorAttr()
cube_extent: Usd.Attribute = cube.GetExtentAttr()

# where possible use schema API to access attributes
print(f"Size: {cube_size.Get()}")
print(f"Extent: {cube_extent.Get()}")
print(f"Display Color: {cube_displaycolor.Get()}")

# # Modify the size, extent, and display color attributes:
cube_size.Set(cube_size.Get() * 2)
cube_extent.Set(cube_extent.Get() * 2)
cube_displaycolor.Set([(0.0, 1.0, 0.0)])

# where possible use schema API to access attributes
print(f"Size: {cube_size.Get()}")
print(f"Extent: {cube_extent.Get()}")
print(f"Display Color: {cube_displaycolor.Get()}")
#==========================================================================


stage.Save()