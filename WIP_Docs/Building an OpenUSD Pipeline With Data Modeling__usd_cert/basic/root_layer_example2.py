"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 6 (extract/transform outputs and layered authoring)
- Chapter 8 (composition troubleshooting)

Why this script exists:
- It demonstrates creating a root layer plus a dedicated authored sublayer.
- It also shows direct Sdf prim authoring in a specific layer.

How to run:
- From the __usd_cert folder:
  python basic/root_layer_example2.py

What to expect:
1) Creates root and extra USDA layers.
2) Adds sublayer path to root layer.
3) Authors /Xform2a into the extra layer via Sdf API.
4) Prints both layer contents for comparison.
"""

from pxr import Usd, Sdf
import os

# Create a new stage:
stage_path = "_assets/root_layer_example2.usda"
if os.path.exists(stage_path):
    os.remove(stage_path)
stage: Usd.Stage = Usd.Stage.CreateNew(stage_path)

# Get the root layer object:
root_layer: Sdf.Layer = stage.GetRootLayer()
print("Root layer identifier:", os.path.relpath(root_layer.identifier))

# Add a simple prim to the root layer:
stage.DefinePrim("/World", "Xform")

# Create an additional layer in USDA format:
extra_layer_path = "_assets/extra_layer2.usda"
if os.path.exists(extra_layer_path):
    os.remove(extra_layer_path)
extra_layer: Sdf.Layer = Sdf.Layer.CreateNew(extra_layer_path)

# Add the extra layer as a sublayer to the root layer:
rel_path = "./" + os.path.basename(extra_layer.identifier)
root_layer.subLayerPaths.append(rel_path)

#===============================================================

# # Set the edit target to the extra layer so new prims go there:
# stage.SetEditTarget(Usd.EditTarget(extra_layer))

# # Create a prim within extra_layer.usda:
# stage.DefinePrim("/Xform2", "Xform")
# extra_layer.defaultPrim = "Xform2"
# extra_layer.documentation = "This is the extra layer"

#===============================================================

# Create a second prim within extra_layer.usda using Sdf API:
prim_spec = Sdf.CreatePrimInLayer(extra_layer, "/Xform2a")
prim_spec.specifier = Sdf.SpecifierDef
prim_spec.typeName = "Xform" 


# Save both layers:
stage.Save()
extra_layer.Save()

# Print the contents of the root layer:
print("\nRoot layer contents:")
print(root_layer.ExportToString())

# Print the contents of the extra layer:
print("\nExtra layer contents:")
print(extra_layer.ExportToString())