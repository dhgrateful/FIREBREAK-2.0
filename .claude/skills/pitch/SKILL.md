---
name: pitch
description: "Generate your pitch — elevator, event intro, podcast bio, speaker page. Multiple lengths from the same context."
---

# /pitch — Craft Your Pitch

Creates versions of "what you do" for different situations. All grounded in your Context files so every version sounds like you.

## Before Generating

Read these files in order:
1. `reference/core/soul.md` — Who you are, your framework, your origin
2. `reference/core/audience.md` — Who you serve
3. `reference/core/offer.md` — Your transformation
4. `reference/core/voice.md` — How you sound

## Ask One Question

"What's this for? Pick one or tell me the situation."

| Format | Length | Use case |
|--------|--------|----------|
| **One-liner** | 1 sentence | LinkedIn headline, Twitter bio, name tag |
| **Elevator** | 30 seconds (~75 words) | Networking events, "so what do you do?" |
| **Introduction** | 2 minutes (~300 words) | Panel intro, podcast guest bio, speaking engagement |
| **Speaker page** | Full page (~500 words) | Website about page, conference submission |
| **All of the above** | All four | Generate the full set at once |

If they don't specify, generate all four.

## Writing Rules

- Lead with the transformation, not the credentials
- Use their contrarian belief from `soul.md` as the hook — it's what makes them different
- Include the origin moment from `soul.md` in the Introduction and Speaker page versions
- Reference specific results from `offer.md#Transformation` or `soul.md#External Perception`
- Match `voice.md` tone — if they're anti-corporate, the pitch should be anti-corporate
- No buzzwords from `voice.md#Anti-Language`
- The one-liner should be memorizable. Test: could they say it without reading it?

## Save Output

Write to `outputs/[YYYY-MM-DD]-pitch-[format-slug].md` with frontmatter:

```yaml
---
type: output
format: pitch
date: [today]
last-updated: [today's date and time]
source_files:
  - reference/core/soul.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/core/voice.md
---
```
