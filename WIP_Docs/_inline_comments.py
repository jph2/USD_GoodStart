#!/usr/bin/env python3
"""Move frame-by-frame comments inline after each image in the tutorial."""

import re

path = r"E:\SynologyDrive\9999_LocalRepo\USD_GoodStart\WIP_Docs\WhatYouShouldKnowAboutContentAggregation__VIDEO_DEEP_DIVE_TUTORIAL.md"

with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Chapter 1: Replace images block + Frame-by-frame notes with interleaved version
old_ch1 = r'''<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_26\.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_26\.png" alt="Key moment - 9:32" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_34\.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_34\.png" alt="Key moment - 10:23" width="900" /></a>

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_04\.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_04\.png" alt="Key moment - 11:08" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_23\.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_23\.png" alt="Key moment - 12:04" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_26\.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_26\.png" alt="Key moment - 12:57" width="900" /></a>

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_48\.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_48\.png" alt="Key moment - 13:45" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_52\.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_52\.png" alt="Key moment - 14:34" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_23\.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_23\.png" alt="Key moment - 15:19" width="900" /></a>

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_47\.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_47\.png" alt="Key moment - 16:10" width="900" /></a>

### Frame-by-frame notes \(what you are seeing\)

- \*\*\[ContentAggregation_8h21_26\]\(Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_26\.png\)\*\*:.*?
  - \*\*Learn more\*\*: \[10 - References\]\(#link-10\), \[11 - Payloads\]\(#link-11\)

### Intro bridge'''

new_ch1 = '''<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_26.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_26.png" alt="Key moment - 9:32" width="900" /></a>

**What you're seeing:** "Back to the problem…" + the joke question: *"I just wanted to resize my mug. Where do I put it?"* **Why it matters:** a tiny change forces you to choose the *right* contribution mechanism (sublayer vs reference vs payload) based on intent, not convenience. **Learn more:** [8 - Introduction to composition](#link-8), [12 - LIVRPS](#link-12), [67 - Reference deck](#link-67)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_34.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_34.png" alt="Key moment - 10:23" width="900" /></a>

**What you're seeing:** The "Four Pillars of Asset Structure": **Legibility, Modularity, Performance, Navigability**. **Why it matters:** these pillars are the decision rubric for the rest of the tutorial - they explain *why* some aggregation styles scale and others rot. **Learn more:** [14 - Asset structure](#link-14), [16 - Best practices index](#link-16)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_04.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_04.png" alt="Key moment - 11:08" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_23.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_23.png" alt="Key moment - 12:04" width="900" /></a>

**What you're seeing:** Example question about naming internal prims `geo_final_v3`, `materials_latest`, `rig_backup`. **Why it matters:** those names blur *public interface* vs *internal implementation*. Downstream teams start binding to "whatever was there today," and you lose the ability to restructure safely. **Learn more:** [14 - Asset structure](#link-14), [69 - Prims](#link-69)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_26.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_26.png" alt="Key moment - 12:57" width="900" /></a>

**What you're seeing:** Section header: **Asset Interface & Encapsulation**. **Why it matters:** in production, "aggregation reliability" is mostly "interface stability". Encapsulation is how you keep interfaces stable while internals evolve. **Learn more:** [68 - Default prim](#link-68), [14 - Asset structure](#link-14)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_48.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_48.png" alt="Key moment - 13:45" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_52.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_52.png" alt="Key moment - 14:34" width="900" /></a>

**What you're seeing:** "Spot the problem" encapsulation example: absolute paths and downstream references to deep internal prim paths (like `/Chair/geo/seat_mesh`) break portability. **Why it matters:** if downstream content points inside an asset's guts, you cannot refactor without breaking consumers. That is exactly how "it works on my machine" stages are created. **Learn more:** [14 - Asset structure](#link-14), [68 - Default prim](#link-68), [67 - Reference deck](#link-67)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_23.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_23.png" alt="Key moment - 15:19" width="900" /></a>

**What you're seeing:** "Asset Interface - What Is It?" defining two core interface tools: **Default prim** as the stable entry point for consumers; **Encapsulation** via a clean public surface (`/Chair`, `/Chair/Looks`) hiding `_internal`. **Why it matters:** these are the two interface tools you need to keep consumers stable. **Learn more:** [68 - Default prim](#link-68), [10 - References](#link-10)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_47.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_47.png" alt="Key moment - 16:10" width="900" /></a>

**What you're seeing:** Section header: **Reference/Payload Pattern** (the handoff from "interface" to "load policy"). **Why it matters:** once your interface is clean, you can split "metadata you always want" from "heavy data you load on demand." **Learn more:** [10 - References](#link-10), [11 - Payloads](#link-11)

### Intro bridge'''

# Use DOTALL to match across newlines; the regex needs to match the full block
pattern = r'(<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_26\.png">.*?</a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_34\.png">.*?</a>\s*\n\s*\n<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_04\.png">.*?</a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_23\.png">.*?</a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_26\.png">.*?</a>\s*\n\s*\n<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_48\.png">.*?</a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_52\.png">.*?</a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_23\.png">.*?</a>\s*\n\s*\n<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_47\.png">.*?</a>\s*\n\s*\n)### Frame-by-frame notes \(what you are seeing\)\s*\n\s*\n(?:- \*\*\[ContentAggregation_8h21_26\].*?\n  - \*\*Learn more\*\*:.*?\n\s*\n)(?:- \*\*\[ContentAggregation_8h21_34\].*?\n  - \*\*Learn more\*\*:.*?\n\s*\n)(?:- \*\*\[ContentAggregation_8h22_04\].*?\n  - \*\*Learn more\*\*:.*?\n\s*\n)(?:- \*\*\[ContentAggregation_8h22_26\].*?\n  - \*\*Learn more\*\*:.*?\n\s*\n)(?:- \*\*\[ContentAggregation_8h22_48\].*?\n  - \*\*Learn more\*\*:.*?\n\s*\n)(?:- \*\*\[ContentAggregation_8h23_23\].*?\n  - \*\*Learn more\*\*:.*?\n\s*\n)(?:- \*\*\[ContentAggregation_8h23_47\].*?\n  - \*\*Learn more\*\*:.*?\n\s*\n)(### Intro bridge)'

# Simpler: just find and replace the block between the images and ### Intro bridge
# Read the exact bytes to get the pattern
marker_start = '<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h21_26.png">'
marker_end = '### Intro bridge\n\nThis chapter sets the rules of the game.'

idx_start = content.find(marker_start)
idx_end = content.find(marker_end)
if idx_start == -1 or idx_end == -1:
    print("Could not find markers")
    print("idx_start:", idx_start, "idx_end:", idx_end)
else:
    before = content[:idx_start]
    after = content[idx_end:]
    content = before + new_ch1 + "\n\n" + after
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Chapter 1 done")
