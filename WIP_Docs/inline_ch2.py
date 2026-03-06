# -*- coding: utf-8 -*-
"""Inline Chapter 2 frame notes."""
path = 'WhatYouShouldKnowAboutContentAggregation__VIDEO_DEEP_DIVE_TUTORIAL.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find Chapter 2 block: from first image to before ### Intro bridge
ch2_section = content.find('## Chapter 2')
replace_start = content.find('\n\n<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_51.png">', ch2_section)
replace_end = content.find('\n\n### Intro bridge\n\n', replace_start)
if replace_start < 0 or replace_end < 0:
    print("Markers not found:", replace_start, replace_end)
    exit(1)
# New Chapter 2 content with inline comments (starts with newline to preserve spacing)
new_ch2 = '''

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_51.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h23_51.png" alt="Key moment - 16:59" width="900" /></a>

**What you're seeing:** Agenda revisited with the **Reference/Payload Pattern** highlighted as "most important from today". **Why it matters:** even when you choose sublayers for collaboration lanes, load-policy decisions (payloads) will change what teammates *see* and debug. **Learn more:** [9 - Layers and sublayers](#link-9), [11 - Payloads](#link-11)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_05.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_05.png" alt="Key moment - 17:44" width="900" /></a>

**What you're seeing:** Houdini/Solaris viewport showing the Kitchen Set scene in context (this is the "real object" we're composing). **Why it matters:** sublayer decisions are only meaningful when you can connect them to a concrete scene graph (what prims exist, what changed, and who owns the change). **Learn more:** [42 - Solaris/USD docs](#link-42), [29 - Writing USD from Houdini](#link-29)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_19.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_19.png" alt="Key moment - 18:35" width="900" /></a>

**What you're seeing:** Houdini UI showing a **layer stack / scene graph list** and a small USDA snippet. **Why it matters:** this is the "audit surface" you need when sublayers get messy: list contributors, then trace which layer is authoring what. **Learn more:** [15 - Stage API](#link-15), [12 - LIVRPS](#link-12)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_32.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_32.png" alt="Key moment - 19:23" width="900" /></a>

**What you're seeing:** "Houdini Demo - payload structure for geometry (Kitchen Set)". **Why it matters:** payload boundaries often become the "fault lines" of collaboration - teams can author opinions that you cannot even see until something is loaded. **Learn more:** [11 - Payloads](#link-11), [67 - Reference deck](#link-67)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_39.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_39.png" alt="Key moment - 20:04" width="900" /></a>

**What you're seeing:** "Reference/Payload pattern" slide: **reference = metadata layer**, **payload = heavy content layer**. **Why it matters:** this is the clean separation you want in a team environment: everybody can read the interface/metadata without loading the world. **Learn more:** [10 - References](#link-10), [11 - Payloads](#link-11)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_58.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h24_58.png" alt="Key moment - 20:57" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h25_08.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h25_08.png" alt="Key moment - 21:45" width="900" /></a>

**What you're seeing:** Example question (and answer): what should live **above the payload boundary** in the reference layer. **Answer logic:** author **variant definitions** and **asset metadata (kind, assetInfo)** in the reference layer; keep heavy geometry in payload. **Why it matters:** this separation keeps interface visible without loading heavy content. **Learn more:** [70 - Variant sets](#link-70), [72 - Model kinds](#link-72), [11 - Payloads](#link-11)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_04.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h22_04.png" alt="Key moment - 22:04" width="900" /></a>

**What you're seeing:** The earlier "bad naming" example question reappears as a reminder: **don't leak implementation details into the public surface**. **Why it matters:** sublayers become dangerous when teams bind to internal names and then "fix layers" accumulate forever. **Learn more:** [14 - Asset structure](#link-14), [68 - Default prim](#link-68)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h25_58.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h25_58.png" alt="Key moment - 22:29" width="900" /></a>

**What you're seeing:** Section header: **Asset Parameterization**. **Why it matters:** parameterization is how teams avoid "duplicate the asset 15 times" - it's also where sublayer strategies can accidentally fight with variants if ownership is unclear. **Learn more:** [70 - Variant sets](#link-70)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h26_19.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h26_19.png" alt="Key moment - 23:14" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h27_25.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h27_25.png" alt="Key moment - 24:03" width="900" /></a>

**What you're seeing:** Houdini scene graph + context menu showing how variants/parameters are operated in a DCC. **Why it matters:** this is where "collaboration lanes" become real: one team owns a variant set, another owns lookdev, another owns layout - and you need a structure that keeps those from colliding. **Learn more:** [70 - Variant sets](#link-70), [9 - Layers and sublayers](#link-9)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h32_48.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h32_48.png" alt="Key moment - 24:50" width="900" /></a>

**What you're seeing:** Houdini showing variant thumbnails / switching UI on an asset (chair). **Why it matters:** if your variant switching requires loading massive geometry every time, your review workflow will die. This is where payload boundaries and lofting become practical, not academic. **Learn more:** [11 - Payloads](#link-11), [67 - Reference deck](#link-67)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h33_40.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h33_40.png" alt="Key moment - 25:40" width="900" /></a>

**What you're seeing:** **Primvars** slide: use primvars for small per-property tweaks (cheaper memory-wise) vs variants for swapping whole configurations. **Why it matters:** "small change vs big configuration swap" is an aggregation decision. It determines whether you need variants, primvars, or just a sublayer override lane. **Learn more:** [71 - Primvars](#link-71), [70 - Variant sets](#link-70)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h34_23.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h34_23.png" alt="Key moment - 26:32" width="900" /></a>

**What you're seeing:** Section header: **Lofting & Workstreams**. **Why it matters:** this is where the talk becomes explicitly "team structure": how modelers, texture artists, and riggers can work without chaos. **Learn more:** [9 - Layers and sublayers](#link-9), [67 - Reference deck](#link-67)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h34_29.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h34_29.png" alt="Key moment - 27:17" width="900" /></a>

**What you're seeing:** Example question: best layer structure for parallel collaboration across geometry/materials/rigging. **Answer intent:** separate department layers (e.g., `geo.usd`, `materials.usd`, `rigging.usd`) then compose them as **sublayers** inside the asset's payload. **Why it matters:** this structure keeps department ownership clear and avoids collisions. **Learn more:** [9 - Layers and sublayers](#link-9), [11 - Payloads](#link-11)
'''

content = content[:replace_start] + new_ch2 + content[replace_end:]
with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Chapter 2 done")
