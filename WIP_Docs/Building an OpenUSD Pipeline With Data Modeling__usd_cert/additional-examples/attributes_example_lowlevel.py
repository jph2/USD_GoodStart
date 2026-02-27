"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 3 (typing discipline)
- Chapter 4 (attribute metadata at low-level API)

Why this script exists:
- It demonstrates direct Sdf-level authoring without schema wrappers.
- Useful when debugging generated layers or building tooling below UsdGeom.

How to run:
- From the __usd_cert folder:
  python additional-examples/attributes_example_lowlevel.py

What to observe:
1) Create prim and attribute specs directly in a layer.
2) Assign default value and interpolation metadata.
3) Understand what high-level APIs are writing under the hood.
"""

### Low Level ###
from pxr import Sdf, UsdGeom
layer = Sdf.Layer.CreateAnonymous()
prim_path = Sdf.Path("/bicycle")
prim_spec = Sdf.CreatePrimInLayer(layer, prim_path)
prim_spec.specifier = Sdf.SpecifierDef
prim_spec.typeName = "Xform"
attr_spec = Sdf.AttributeSpec(prim_spec, "tire:size", Sdf.ValueTypeNames.Double)
attr_spec.default = 10
attr_spec.interpolation = UsdGeom.Tokens.constant
# Or
attr_spec.SetInfo("interpolation", UsdGeom.Tokens.constant)