"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 0 (safe experimentation in-memory)

Why this script exists:
- It shows a no-risk authoring workflow: build in memory first, export later.
- Useful when teaching or debugging without touching existing stage files.

How to run:
- From the __usd_cert folder:
  python basic/in_mem_stage.py

What to expect:
1) Creates an in-memory stage.
2) Authors /World.
3) Prints stage text.
4) Exports to _assets/in_memory_stage.usda.
"""

from pxr import Usd

# Create a new stage stored only in memory:
stage: Usd.Stage = Usd.Stage.CreateInMemory()

# Add a prim so the stage contains some data:
stage.DefinePrim("/World", "Xform")

# Print the stage's contents:
print("In-memory stage:")
print(stage.ExportToString(addSourceFileComment=False))

# Export the stage to disk if needed:
stage.Export("_assets/in_memory_stage.usda", addSourceFileComment=False)