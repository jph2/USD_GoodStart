"""
Tutorial support script for:
Building an OpenUSD Pipeline With Data Modeling - VIDEO_DEEP_DIVE_TUTORIAL

Chapter tie-back:
- Chapter 0 (problem framing + first stage lifecycle)

Why this script exists:
- It gives you the simplest possible "first success" with USD authoring.
- If this runs, your Python + USD environment is working.

How to run:
- From the __usd_cert folder:
  python basic/create_stage.py

What to expect:
1) Creates _assets/first_stage.usda.
2) Prints the stage in USDA text form.
3) Lets you confirm that "stage creation" is deterministic before you move
   into attributes, relationships, metadata, and exchange patterns.
"""

# Import the `Usd` module from the `pxr` package:
from pxr import Usd

# Define a file path name:
file_path = "_assets/first_stage.usda"
# Create a stage at the given `file_path`:
stage: Usd.Stage = Usd.Stage.CreateNew(file_path)
print(stage.ExportToString(addSourceFileComment=True))