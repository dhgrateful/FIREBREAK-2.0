---
name: ad
description: "Generate ad copy (Facebook/Instagram/Meta) from your Context files."
---

# /ad — Generate Ad Copy

Creates ad copy that sounds like you, speaks to your buyer, and sells your offer.

## Before Generating

Read these files in order:
1. `reference/core/soul.md` — Who you are
2. `reference/core/audience.md` — Who you serve
3. `reference/core/offer.md` — What you sell
4. `reference/core/voice.md` — How you sound

Also scan `decisions/` and `research/` for recent entries.

If any Context file has `status: draft` or is mostly empty, warn:
"Your [file] is thin. Output quality will improve if you run `/enrich [file]` first. Generate anyway?"

## What to Generate

- 3 hook variations (pattern-interrupt opening lines)
- Primary copy body (150-200 words)
- Call to action
- Suggested headline and description for Meta ad format

The copy must:
- Use the client's voice and signature phrases from `voice.md`
- Reference the specific transformation from `offer.md`
- Address the audience's pain points using their language from `audience.md`
- Reflect core beliefs from `soul.md`

## Save Output

Write to `outputs/[YYYY-MM-DD]-ad-[slug].md` with frontmatter:

```yaml
---
type: output
format: ad
date: [today]
last-updated: [today's date and time]
source_files:
  - reference/core/soul.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/core/voice.md
---
```
