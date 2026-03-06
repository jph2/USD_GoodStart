# One-off script to fix Chapter 6 frame note
path = "WhatYouShouldKnowAboutContentAggregation__VIDEO_DEEP_DIVE_TUTORIAL.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Use curly quotes to match file (U+201C, U+201D)
old = """### Frame note (what you are seeing)

- **[ContentAggregation_8h52_54](Pics/WhatYouShouldKnowAboutContentAggregation/ContentAggregation_8h52_54.png)**: Model hierarchy example question answer: a **component** cannot contain another component; \u201cHero\u201d should be assembly/group when it meaningfully collects other components.
  - **Anti-pattern tie-in**: treating hierarchy as \u201cwhatever looks tidy\u201d instead of a semantic contract leads to brittle navigation, validation failures, and wrong assumptions downstream.
  - **Learn more**: [72 - Model kinds](#link-72), [73 - Kind system (OpenUSD)](#link-73)

### Intro bridge"""

new = """**What you're seeing:** Model hierarchy example question answer: a **component** cannot contain another component; \u201cHero\u201d should be assembly/group when it meaningfully collects other components. **Why it matters:** treating hierarchy as \u201cwhatever looks tidy\u201d instead of a semantic contract leads to brittle navigation, validation failures, and wrong assumptions downstream. **Learn more:** [72 - Model kinds](#link-72), [73 - Kind system (OpenUSD)](#link-73)

### Intro bridge"""

if old in content:
    content = content.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Chapter 6 done")
else:
    print("Block not found")
    idx = content.find("### Frame note (what you are seeing)")
    print("Frame note at:", idx)
    if idx >= 0:
        print("Context:", repr(content[idx:idx+200]))
