"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 0 (stage lifecycle: create -> open -> edit -> save)

Why this script exists:
- It demonstrates a full edit cycle on a real file stage.
- This mirrors "pipeline reality": stages are reopened and modified many times.

How to run:
- From the __usd_cert folder:
  python basic/open_stage.py

What to expect:
1) Opens _assets/first_stage.usda.
2) Adds /World Xform.
3) Saves and prints updated USDA output.
"""

from pxr import Usd

# Open an existing USD stage from disk:
stage: Usd.Stage = Usd.Stage.Open("_assets/first_stage.usda")

# Add a simple prim so we can see a change in the saved file:
stage.DefinePrim("/World", "Xform")

# Save the stage back to disk:
stage.Save()

# Print the stage as text so we can inspect the result:
print(stage.ExportToString(addSourceFileComment=True))