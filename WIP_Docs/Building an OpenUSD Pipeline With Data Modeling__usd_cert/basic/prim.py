"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 0 and Chapter 1 (prim identity before properties)

Why this script exists:
- It demonstrates simple prim definition with and without explicit type.
- It is the minimal base required before discussing attributes/relationships.

How to run:
- From the __usd_cert folder:
  python basic/prim.py

What to expect:
1) Creates _assets/prims.usda.
2) Authors /hello and /world (Sphere).
3) Saves stage for inspection in usdview.
"""

# Import the `Usd` module from the `pxr` package:
from pxr import Usd

# Create a new USD stage with root layer named "prims.usda":
stage: Usd.Stage = Usd.Stage.CreateNew("_assets/prims.usda")

# Define a new primitive at the path "/hello" on the current stage:
stage.DefinePrim("/hello")

# Define a new primitive at the path "/world" on the current stage with the prim type, Sphere.
stage.DefinePrim("/world", "Sphere")

stage.Save()