# -*- coding: utf-8 -*-
"""Inline frame notes for Chapters 3, 4, 5."""
path = 'WhatYouShouldKnowAboutContentAggregation__VIDEO_DEEP_DIVE_TUTORIAL.md'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

def replace_chapter(content, ch_num, first_img, new_content):
    """Replace chapter block from first image to ### Intro bridge."""
    marker = '## Chapter ' + str(ch_num)
    start = content.find('\n\n<a href="Pics/WhatYouShouldKnowAboutContentAggregation/' + first_img + '">', content.find(marker))
    end = content.find('\n\n### Intro bridge\n\n', start)
    if start < 0 or end < 0:
        return content, False
    return content[:start] + '\n\n' + new_content + content[end:], True

# Chapter 3
ch3_new = '''<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h34_55.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h34_55.png" alt="Key moment - 28:07" width="900" /></a>

**What you're seeing:** Example question (answered): parallel collaboration works best when geometry/materials/rigging live in separate layers and are composed as sublayers (often inside an asset payload). **Why it matters:** references give you modular asset boundaries; sublayers inside the asset give you internal work lanes. **Learn more:** [10 - References](#link-10), [9 - Layers and sublayers](#link-9)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h35_06.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h35_06.png" alt="Key moment - 28:56" width="900" /></a>

**What you're seeing:** "What is lofting?" slide: expose information *from payload up to the reference layer* so people can see what exists without loading heavy content. **Why it matters:** lofting is a key tactic for "fast stage open + still debuggable", especially when your referenced assets are huge. **Learn more:** [10 - References](#link-10), [11 - Payloads](#link-11), [67 - Reference deck](#link-67)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h36_01.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h36_01.png" alt="Key moment - 29:39" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h36_37.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h36_37.png" alt="Key moment - 30:30" width="900" /></a>

**What you're seeing:** Houdini demo of lofting: the UI shows how authored data is split across layers so consumers can browse/parameterize assets without forcing heavy geometry load. **Why it matters:** this is the "collaboration reality" view - where layer boundaries are visible and therefore governable. **Learn more:** [42 - Solaris/USD docs](#link-42), [29 - Writing USD from Houdini](#link-29)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h37_19.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h37_19.png" alt="Key moment - 31:18" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h37_53.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h37_53.png" alt="Key moment - 32:08" width="900" /></a>

**What you're seeing:** Transition into model hierarchy: "be kind to the pipeline by using Model Kinds". **Why it matters:** references keep assets modular, but model kinds make large composed scenes *navigable* and *machine-queryable*. **Learn more:** [72 - Model kinds](#link-72), [16 - Best practices index](#link-16)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h32_48.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h32_48.png" alt="Key moment - 32:48" width="900" /></a>

**What you're seeing:** Houdini variant browsing (chair) - this is what "interface-first" looks like in practice: you can navigate options without rewriting the scene. **Learn more:** [70 - Variant sets](#link-70), [11 - Payloads](#link-11)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h37_56.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h37_56.png" alt="Key moment - 33:01" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h38_04.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h38_04.png" alt="Key moment - 33:52" width="900" /></a>

**What you're seeing:** "Model Kinds: 3 main kinds" slide (component / assembly / group) with the key rules. **Why it matters:** kinds let tools traverse your scene like a table-of-contents; they're a quiet but high-leverage "aggregation quality" signal. **Learn more:** [72 - Model kinds](#link-72), [73 - Kind system (OpenUSD)](#link-73)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h38_54.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h38_54.png" alt="Key moment - 34:39" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h39_58.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h39_58.png" alt="Key moment - 35:28" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h42_43.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h42_43.png" alt="Key moment - 36:19" width="900" /></a>

**What you're seeing:** Houdini demo showing the scene graph annotated with kind metadata across the Kitchen Set hierarchy. **Why it matters:** this is how "a mess of prims" becomes "a structured model hierarchy" that can be validated and queried across tools. **Learn more:** [72 - Model kinds](#link-72), [15 - Stage API](#link-15)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h44_49.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h44_49.png" alt="Key moment - 37:03" width="900" /></a>

**What you're seeing:** Model kinds slide with chat question context: where to place assembly/group and how to structure hierarchy for teams. **Why it matters:** hierarchy is a collaboration contract - it determines who can safely edit what without stepping on other teams' toes. **Learn more:** [72 - Model kinds](#link-72), [67 - Reference deck](#link-67)'''

# Chapter 4
ch4_new = '''<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h46_25.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h46_25.png" alt="Key moment - 37:52" width="900" /></a>

**What you're seeing:** Houdini/Solaris view with an inspection panel and code/editor view: this is the practical "where is the payload boundary?" authoring environment. **Why it matters:** payload design is only safe when you can audit it (what loads, what stays available, what is referenced vs payloaded). **Learn more:** [11 - Payloads](#link-11), [15 - Stage API](#link-15)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h46_48.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h46_48.png" alt="Key moment - 38:39" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h46_51.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h46_51.png" alt="Key moment - 39:25" width="900" /></a>

**What you're seeing:** Same Houdini setup, with chat prompts about hierarchy design (e.g., "why not group of groups?"). **Why it matters:** payload boundaries and hierarchy design interact - you want a hierarchy that remains meaningful even when parts are unloaded. **Learn more:** [72 - Model kinds](#link-72), [73 - Kind system (OpenUSD)](#link-73)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h48_16.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h48_16.png" alt="Key moment - 40:16" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h48_34.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h48_34.png" alt="Key moment - 40:58" width="900" /></a>

**What you're seeing:** Model kinds slide with an audience question overlay about "advantages of not defining kinds". **Why it matters:** "no kinds" is easy short-term, but it removes structure that tools and teams rely on for navigation/validation - especially when payloads hide geometry and you only have metadata to reason with. **Learn more:** [72 - Model kinds](#link-72), [16 - Best practices index](#link-16)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h49_22.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h49_22.png" alt="Key moment - 41:50" width="900" /></a>

**What you're seeing:** Agenda highlight: "Be kind to the pipeline by using Model Kinds!" **Why it matters:** this is the "payload-safe navigation contract" idea: even unloaded content should still be discoverable through a stable hierarchy. **Learn more:** [72 - Model kinds](#link-72)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h50_29.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h50_29.png" alt="Key moment - 42:46" width="900" /></a>

**What you're seeing:** Houdini demo title: "Scene Graph Tree - Model Kind". **Why it matters:** this is the concrete way kinds show up in a DCC: as columns/filters/navigation aids that help you manage large composed graphs. **Learn more:** [72 - Model kinds](#link-72), [42 - Solaris/USD docs](#link-42)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h52_15.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h52_15.png" alt="Key moment - 43:30" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h52_44.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h52_44.png" alt="Key moment - 44:23" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h52_54.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h52_54.png" alt="Key moment - 45:15" width="900" /></a>

**What you're seeing:** Example question (and answer) on **model hierarchy contract** violations (e.g., components cannot contain other components). **Why it matters:** hierarchy correctness is part of aggregation correctness - it determines how scenes are traversed, validated, and reused. **Learn more:** [72 - Model kinds](#link-72), [73 - Kind system (OpenUSD)](#link-73)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h44_49.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h44_49.png" alt="Key moment - 44:49" width="900" /></a>

**What you're seeing:** Model kinds recap slide with question context ("should the assembly/group be placed in a separate file?"). **Why it matters:** this is the bridge back to composition decisions: file boundaries (references/sublayers/payloads) and semantic boundaries (kinds) need to align. **Learn more:** [10 - References](#link-10), [72 - Model kinds](#link-72)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h52_58.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h52_58.png" alt="Key moment - 46:00" width="900" /></a>

**What you're seeing:** Closing "Thank you" slide with links to community/support channels. **Learn more:** [17 - Week 2 slides](#link-17), [18 - NVIDIA Discord](#link-18)'''

# Chapter 5
ch5_new = '''<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h53_36.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h53_36.png" alt="Key moment - 46:51" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h54_13.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h54_13.png" alt="Key moment - 47:39" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h48_16.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h48_16.png" alt="Key moment - 48:16" width="900" /></a>

**What you're seeing:** Closing "Thank you" slide during Q&A (contact links + study group + Discord). **Why it matters:** the *actual* pipeline questions people ask during Q&A (paths, portability, tool behavior) are almost always "opinion/source resolution" problems in disguise. **Learn more:** [12 - LIVRPS](#link-12), [13 - Value resolution](#link-13), [18 - NVIDIA Discord](#link-18)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h48_16.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h48_16.png" alt="Key moment - 48:16" width="900" /></a>

**What you're seeing:** Model kinds slide with a question overlay. **Why it matters:** "what kind is this prim?" becomes a practical debugging question when the composed hierarchy doesn't behave like people expect. **Learn more:** [72 - Model kinds](#link-72), [73 - Kind system (OpenUSD)](#link-73)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h54_52.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h54_52.png" alt="Key moment - 48:26" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h55_23.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h55_23.png" alt="Key moment - 49:17" width="900" /></a> <a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h55_28.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h55_28.png" alt="Key moment - 50:06" width="900" /></a>

**What you're seeing:** Houdini/Solaris scene graph view showing the Kitchen Set hierarchy and kind metadata. **Why it matters:** this is the hands-on "trace surface": you identify the prim, then locate the authored source/layer/arc that is currently winning. **Learn more:** [15 - Stage API](#link-15), [12 - LIVRPS](#link-12)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h56_10.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h56_10.png" alt="Key moment - 50:51" width="900" /></a>

**What you're seeing:** A practical recap frame that anchors the "turn this into a checklist" mindset. **Why it matters:** opinion resolution only helps if it tells you *where to fix the source-of-truth* (not where to apply yet another band-aid layer). **Learn more:** [13 - Value resolution](#link-13), [67 - Reference deck](#link-67)

<a href="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_9h03_27.png"><img src="Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_9h03_27.png" alt="Key moment - 51:42" width="900" /></a>

**What you're seeing:** Solaris node graph view (the procedural "how this stage is built" perspective). **Why it matters:** in node-based authoring, "the source" may be a node graph that emits layers - tracing winning opinions means mapping stage results back to the authoring graph. **Learn more:** [42 - Solaris/USD docs](#link-42), [15 - Stage API](#link-15)'''

# Apply
for ch_num, first_img, new_content in [(3, 'ContentAggregation_8h34_55.png', ch3_new), (4, 'ContentAggregation_8h46_25.png', ch4_new), (5, 'ContentAggregation_8h53_36.png', ch5_new)]:
    content, ok = replace_chapter(content, ch_num, first_img, new_content)
    if not ok:
        print("Chapter", ch_num, "not found")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Chapters 3, 4, 5 done")
