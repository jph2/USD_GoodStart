"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 0 (composition foundation)
- Chapter 6 (exchange pipeline layering mindset)

Why this script exists:
- It introduces root-layer inspection and sublayer authoring.
- Layer composition is critical for non-destructive pipeline workflows.

How to run:
- From the __usd_cert folder:
  python basic/root_layer_example.py

What to expect:
1) Creates _assets/root_layer_example.usda.
2) Creates/opens _assets/extra_layer.usdc.
3) Adds extra layer as a sublayer to the root layer.
4) Saves both and prints root layer text.
"""

from pxr import Usd, Sdf
import os

# Create a new stage:
stage: Usd.Stage = Usd.Stage.CreateNew("_assets/root_layer_example.usda")

# Get the root layer object:
root_layer: Sdf.Layer = stage.GetRootLayer()
# Use relpath to avoid printing build machine filesystem info.
print("Root layer identifier:", os.path.relpath(root_layer.identifier), "Full path:", root_layer.identifier)

# Add a simple prim so the stage is not empty:
stage.DefinePrim("/World", "Xform")

extra_layer = Sdf.Layer.FindOrOpen("_assets/extra_layer.usdc")

# Create an additional layer (in a different format) if it doesn't exist:
if extra_layer is None:
    extra_layer: Sdf.Layer = Sdf.Layer.CreateNew("_assets/extra_layer.usdc")
else:
    print("Extra layer already exists.")

# Anchor the path relative to the root layer for better portability
rel_path = "./" + os.path.basename(extra_layer.identifier)

# Add the extra layer as a sublayer to the root layer:
root_layer.subLayerPaths.append(rel_path)
# print(root_layer.subLayerPaths)
# print(extra_layer.identifier)
# print(extra_layer.realPath)
# print(root_layer.GetPrimAtPath("/World"))    

# Save both layers:
stage.Save()
extra_layer.Save()

# Print the contents of the root layer:
print("Root layer contents:")
print(root_layer.ExportToString())