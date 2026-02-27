"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 6 and Chapter 8 (layer edits + production edge cases)

Why this script exists:
- It demonstrates composition change management by removing a sublayer.
- This is useful for debugging "why did this opinion disappear?" issues.

How to run:
- From the __usd_cert folder:
  python basic/root_layer_example3.py

What to expect:
1) Opens root_layer_example2.usda if present.
2) Removes ./extra_layer2.usda from root sublayers.
3) Saves and prints resulting stage text.
"""

from pxr import Usd, Sdf
import os

# Remove a sub layer:
stage_path = "_assets/root_layer_example2.usda"
if os.path.exists(stage_path):
    stage: Usd.Stage = Usd.Stage.Open(stage_path)

    if "./extra_layer2.usda" in stage.GetRootLayer().subLayerPaths:
        stage.GetRootLayer().subLayerPaths.remove("./extra_layer2.usda")

    # Save stage:
    stage.Save()

# Print the contents of the stage:
print("\nStage contents:")
print(stage.ExportToString())

