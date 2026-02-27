"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 8 (production debugging patterns)

Why this script exists:
- It focuses on "is this authored/defined?" style diagnostics.
- These checks are crucial when composed stages behave unexpectedly.

How to run:
- From the __usd_cert folder:
  python additional-examples/property_example.py

What to observe:
1) IsDefined / IsAuthored checks for properties.
2) Property flattening behavior.
3) Property stack inspection as an opinion-resolution debugging tool.
"""

# Methods & Attributes of interest:
# 'IsDefined', 'IsAuthored'
# 'FlattenTo'
# 'GetPropertyStack'
from pxr import Usd, Sdf
### High Level ###
stage = Usd.Stage.CreateInMemory()
prim_path = Sdf.Path("/World")
prim = stage.DefinePrim(prim_path, "Cube")
# Check if the attribute defined
attr = prim.CreateAttribute("height", Sdf.ValueTypeNames.Double)
print(attr.IsDefined()) # Returns: True
attr = prim.GetAttribute("someRandomName")
print(attr.IsDefined())
if not attr:
    attr = prim.CreateAttribute("someRandomName", Sdf.ValueTypeNames.String)
# Check if the attribute has any written values in any layer
print(attr.IsAuthored()) # Returns: True
attr.Set("debugString")
# Flatten the attribute to another prim (with optionally a different name)
# This is quite usefull when you need to copy a specific attribute only instead
# of a certain prim.
prim_path = Sdf.Path("/box")
prim = stage.DefinePrim(prim_path, "Cube")
attr.FlattenTo(prim, "someNewName")
# Inspect the property value source layer stack.
# Note the method signature takes a time code as an input. If you supply a default time code
# value clips will be stripped from the result.
time_code = Usd.TimeCode(1001)
print(attr.GetPropertyStack(time_code))
### Low Level ###
# The low level API does not offer any "extras" worthy of noting.