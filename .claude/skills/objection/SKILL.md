---
name: objection
description: "Handle sales objections using your context. Pulls from your expertise to craft authentic responses."
---

# /objection — Handle an Objection

A prospect pushes back. You type the objection. Claude crafts a response grounded in your experience, framework, and voice — not a generic sales script.

## Before Generating

Read these files in order:
1. `reference/core/soul.md` — Your beliefs and framework
2. `reference/core/audience.md` — What buyers struggle with, what they've tried before
3. `reference/core/offer.md` — Your transformation, guarantee, delivery
4. `reference/core/voice.md` — How you sound

Also scan `outputs/` for any case studies — real results are the strongest objection handler.

## Ask One Question

"What did they say? Give me the objection in their words."

Common objections for high-ticket services:
- "That's expensive" / "I can't justify the cost"
- "How is this different from [competitor/alternative]?"
- "I've tried coaching before and it didn't work"
- "I don't have time for this right now"
- "Can't I just do this myself?"
- "My team won't buy in"
- "I need to think about it"

## Craft the Response

Structure:
1. **Acknowledge** — Don't dismiss it. Show you've heard it before and it's reasonable.
2. **Reframe** — Use your contrarian belief or framework from `soul.md` to shift the frame. Not a trick — a genuine perspective they haven't considered.
3. **Prove** — One specific example, result, or data point. Pull from case studies in `outputs/` or `soul.md#External Perception` if available.
4. **Redirect** — Bring it back to their specific situation. Reference what you know about their buyer profile from `audience.md`.

Rules:
- Match `voice.md` exactly. If you're direct, be direct. Don't soften.
- Never be defensive. Confidence, not persuasion.
- Keep it to 3-5 sentences. This is a conversation, not a pitch.
- Never pressure. If they're not ready, say so honestly.

## Save Output

Write to `outputs/[YYYY-MM-DD]-objection-[topic-slug].md` with frontmatter:

```yaml
---
type: output
format: objection
date: [today]
last-updated: [today's date and time]
source_files:
  - reference/core/soul.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/core/voice.md
---
```

After saving, ask: "Want me to save this to a running objection library? Useful for training your team or preparing for sales calls."
