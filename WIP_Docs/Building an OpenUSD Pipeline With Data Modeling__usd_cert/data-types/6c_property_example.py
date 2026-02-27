"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 2 (relationships are pointers, not executable behavior)

Why this script exists:
- It demonstrates relationship target management end to end.
- This is the direct data-graph pattern behind Station 7 link contracts.

How to run:
- From the __usd_cert folder:
  python data-types/6c_property_example.py

What to observe:
1) Create relationship and initial target set.
2) Add/remove individual targets.
3) Inspect final target list to verify authored graph state.
"""

from pxr import Usd, UsdGeom, Gf, Sdf

file_path = "_assets/relationships_ex1.usda"
stage = Usd.Stage.CreateNew(file_path)

world_xform: UsdGeom.Xform = UsdGeom.Xform.Define(stage, "/World")

# Define a sphere under the World Xform:
sphere: UsdGeom.Sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath("Sphere"))

# Define a cube under the World Xform and set it to be 5 units away from the sphere:
cube: UsdGeom.Cube = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Cube"))
UsdGeom.XformCommonAPI(cube).SetTranslate(Gf.Vec3d(5, 0, 0))

# Define a cone under the World Xform and set it to be 5 units away from the sphere:
cone: UsdGeom.Cone = UsdGeom.Cone.Define(stage, world_xform.GetPath().AppendPath("Cone"))
UsdGeom.XformCommonAPI(cone).SetTranslate(Gf.Vec3d(10, 0, 0))

# Create typeless container for the group
group = stage.DefinePrim("/World/Group") 

# Define the relationship
group.CreateRelationship("members", custom=True).SetTargets(
    [sphere.GetPath(), cube.GetPath()]
)

# # Add a target to the relationship
group.GetRelationship("members").AddTarget(cone.GetPath())

# # Remove a target from the relationship
group.GetRelationship("members").RemoveTarget(cube.GetPath())

# List relationship targets
members_rel = group.GetRelationship("members")
print("Group members:", [str(p) for p in members_rel.GetTargets()])

stage.Save()