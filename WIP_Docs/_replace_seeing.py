"""Replace 'What you're seeing' with varied narrative hooks."""

VARIANTS = [
    "**Now she digs into:**",
    "**At this moment:**",
    "**The key moment:**",
    "**Here:**",
    "**Interesting approach:**",
    "**The slide lands:**",
    "**Hailey shifts to:**",
    "**This is where:**",
    "**The question:**",
    "**The answer:**",
    "**Now:**",
    "**The demo:**",
    "**The idea:**",
    "**The pattern:**",
]

def main():
    with open("WhatYouShouldKnowAboutContentAggregation__VIDEO_DEEP_DIVE_TUTORIAL.md", "r", encoding="utf-8") as f:
        content = f.read()

    # Both apostrophe variants
    old1 = "**What you're seeing:**"
    old2 = "**What you're seeing:**"  # curly apostrophe U+2019
    old2_actual = "**What you" + "\u2019" + "re seeing:**"

    count = 0
    i = 0
    while old1 in content or old2_actual in content:
        variant = VARIANTS[i % len(VARIANTS)]
        if old1 in content:
            content = content.replace(old1, variant, 1)
        else:
            content = content.replace(old2_actual, variant, 1)
        count += 1
        i += 1

    with open("WhatYouShouldKnowAboutContentAggregation__VIDEO_DEEP_DIVE_TUTORIAL.md", "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Replaced {count} occurrences")

if __name__ == "__main__":
    main()
