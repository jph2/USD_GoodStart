# -*- coding: utf-8 -*-
"""Remove duplicate Chapter 1 Inline frame notes block."""
import re

path = "WhatYouShouldKnowAboutContentAggregation__VIDEO_DEEP_DIVE_TUTORIAL.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Pattern: from "### Inline frame notes" through the last bullet, up to (but not including) "### Intro bridge"
start = content.find("### Inline frame notes\n\n")
if start < 0:
    print("Block not found")
    exit(1)

# Find "### Intro bridge" - we want to remove everything from start to just before that
bridge = content.find("\n### Intro bridge\n", start)
if bridge < 0:
    print("Intro bridge not found")
    exit(1)

# What to insert: inline comment for 8h23_47 + newline before ### Intro bridge
replacement = """**What you're seeing:** Section header: **Reference/Payload Pattern** (the handoff from "interface" to "load policy"). **Why it matters:** once your interface is clean, you can split "metadata you always want" from "heavy data you load on demand." **Learn more:** [10 - References](#link-10), [11 - Payloads](#link-11)

"""

new_content = content[:start] + replacement + content[bridge + 1:]  # +1 to keep the \n before ###

with open(path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Done: removed duplicate block, added 8h23_47 inline comment")
