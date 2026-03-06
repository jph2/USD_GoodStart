# -*- coding: utf-8 -*-
"""Apply Content Aggregation 6-chapter restructure edits."""
path = "WhatYouShouldKnowAboutContentAggregation__VIDEO_DEEP_DIVE_TUTORIAL.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Payloads carry forward: Chapter 5 is correct (Lofting/Overrides)

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
