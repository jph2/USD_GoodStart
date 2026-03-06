# -*- coding: utf-8 -*-
path = "WhatYouShouldKnowAboutContentAggregation__VIDEO_DEEP_DIVE_TUTORIAL.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Use regex to handle potential quote variations
import re

# Ch6: match Frame note block (flexible whitespace)
pat6 = r"### Frame note \(what you are seeing\)\s*\n\s*\n- \*\*\[ContentAggregation_8h52_54\].*?\n  - \*\*Learn more\*\*: \[72 - Model kinds\].*?\n\s*\n### Intro bridge"
repl6 = "**What you're seeing:** Model hierarchy example question answer: a **component** cannot contain another component; \"Hero\" should be assembly/group when it meaningfully collects other components. **Anti-pattern tie-in:** treating hierarchy as \"whatever looks tidy\" instead of a semantic contract leads to brittle navigation, validation failures, and wrong assumptions downstream. **Learn more:** [72 - Model kinds](#link-72), [73 - Kind system (OpenUSD)](#link-73)\n\n### Intro bridge"

m = re.search(pat6, content, re.DOTALL)
if m:
    content = content[:m.start()] + repl6 + content[m.end():]
    print("Ch6 done")
else:
    print("Ch6 not found")

# Ch7
pat7 = r"### Frame note \(what you are seeing\)\s*\n\s*\n- \*\*\[ContentAggregation_8h56_10\].*?\n  - \*\*Learn more\*\*: \[13 - Value resolution\].*?\n\s*\n### Intro bridge"
repl7 = "**What you're seeing:** A recap moment that points toward \"operationalizing\" what you learned (turn the concepts into a checklist/release gate). **Why it matters:** without a checklist, \"aggregation correctness\" is subjective and tool-dependent; with a checklist, it becomes reproducible across people and apps. **Learn more:** [13 - Value resolution](#link-13), [11 - Payloads](#link-11), [67 - Reference deck](#link-67)\n\n### Intro bridge"

m = re.search(pat7, content, re.DOTALL)
if m:
    content = content[:m.start()] + repl7 + content[m.end():]
    print("Ch7 done")
else:
    print("Ch7 not found")

with open(path, "w", encoding="utf-8") as f:
    f.write(content)
