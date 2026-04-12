---
name: landing
description: "Generate landing page copy from your Context files."
---

# /landing — Generate Landing Page Copy

Creates landing page copy that converts because it's built on real context, not templates.

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

Ask: "What's the goal — book a call, download something, or buy directly?"

Sections:
1. **Hero** — Headline + subheadline. Lead with the transformation from `offer.md`.
2. **Problem** — 3 pain points in the audience's own words from `audience.md#Voice of Customer`.
3. **Failed alternatives** — What they've tried from `audience.md#Failed Alternatives`.
4. **Solution** — Your approach from `soul.md`, framed as the answer.
5. **How it works** — Delivery mechanics from `offer.md`, simplified to 3 steps.
6. **Proof** — Testimonials from `soul.md#External Perception`.
7. **Guarantee** — From `offer.md#Guarantee`.
8. **CTA** — One clear action matching the goal.

Tone: match `voice.md`. No hype, no filler.

## Save Output

Write to `outputs/[YYYY-MM-DD]-landing-[slug].md` with frontmatter:

```yaml
---
type: output
format: landing
date: [today]
last-updated: [today's date and time]
source_files:
  - reference/core/soul.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/core/voice.md
---
```
