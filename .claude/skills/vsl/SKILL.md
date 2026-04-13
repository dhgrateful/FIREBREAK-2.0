---
name: vsl
description: "Write high-converting Video Sales Letter scripts. Use when creating VSL scripts, sales videos, about page videos, or any structured 5-20 minute sales video. Produces camera-ready scripts optimised for spoken delivery. Never invents facts."
---

# /vsl — Video Sales Letter Script

Write structured, high-converting video scripts from your Context files. Camera-ready, optimised for spoken delivery.

---

## Critical Rule: Never Invent Facts

- Do NOT invent statistics, numbers, or credentials
- Do NOT assume pricing, years in business, or client counts
- Do NOT fabricate testimonials or results
- If information is missing, ASK for it before proceeding

---

## Before Writing

Read these files in order:
1. `reference/core/soul.md` — Who you are
2. `reference/core/audience.md` — Who you serve
3. `reference/core/offer.md` — What you sell
4. `reference/core/voice.md` — How you sound

Also check:
- `decisions/` — Recent decisions (last 5 by date)
- `research/` — Recent research (last 3 by date)

If any Context file has `status: draft` or is mostly empty, warn:
"Your [file] is thin. Output quality will improve if you run `/enrich [file]` first. Generate anyway?"

---

## Triage: Which Framework?

| Signal | Framework |
|--------|-----------|
| Community, membership, $47-$497/month | **18-Section Community** |
| B2B, high-ticket ($3K+), services | **7-Step B2B** |

If unclear, ask: "Is this for a community/membership or a B2B high-ticket service?"

---

## Framework: 18-Section Community VSL

For community and membership offers.

**Flow:**
1. Hook — pain recognition ("that's exactly how I feel")
2. Epiphany Bridge — your journey from struggle to solution
3. Peek Plan — what you'll cover
4. Features + Soft CTA
5. The Plan — step-by-step transformation
6. Answer Questions — preempt objections
7. Stack Proof — diverse social proof
8. Change Tone — shift to serious/direct
9. Zoom Out — bigger picture
10. Price Anchor — compare value
11. Low Effort / High Reward — easy to start
12. Recap Obstacles — what stops them
13. Address Objections — one by one
14. Roadmap — what happens after joining
15. Worst Case / Best Case — frame the decision
16. Hard CTA — clear instruction
17. Risk Reversal — make joining safer than not joining
18. Final CTA — close

**Key principles:**
- CTAs progress: soft → soft → hard
- Social proof covers diverse backgrounds
- Risk reversal makes joining feel safer than not joining

---

## Framework: 7-Step B2B VSL

For high-ticket B2B services.

**Flow:**
1. 60-90 Second Summary — tweet version of entire pitch
2. Hook — attention + credibility
3. Why (Legitimacy) — why you, why now
4. Market Drivers — external forces creating urgency
5. Offer & Price — state price upfront
6. Objection Handling — address concerns directly
7. Qualification + CTA — who it IS and ISN'T for

**Key principles:**
- State price upfront (trains pixel on qualified buyers)
- For affluent buyers: direct, conservative claims, no hype
- Clear qualification: who it IS and ISN'T for

---

## Process

1. **Triage** — Determine framework from offer type
2. **Gather context** — Verify you have required Context files
3. **Get campaign name** — Ask: "What should we call this VSL?"
4. **Write script** — Follow framework structure
5. **Verify facts** — Check every claim against source material
6. **Optimise for spoken delivery** — Contractions, short sentences, natural flow
7. **Save** — Write to output path

---

## Spoken Delivery Optimisation

- Contractions: you're, don't, can't, won't
- Fragments: "Not theory. Patterns."
- Simple words: "use" not "utilise"
- ~5th grade reading level
- Short sentences that breathe

---

## Save Output

Write to `outputs/YYYY-MM-DD-vsl-[campaign-name]/vsl-script.md`

Include frontmatter:
```yaml
---
type: output
format: vsl
date: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
status: draft
source_files:
  - reference/core/soul.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/core/voice.md
---
```

Script should include:
- Header: target audience, transformation, estimated runtime
- Sections with timestamps
- Delivery/production notes where helpful

---

## When NOT to Use

- Short-form video under 60 seconds (use `/ad`)
- Static image ads (use `/ad`)
- General copywriting or landing pages (use `/landing`)
- Content without sales intent (use `/content`)

Use `/vsl` for structured 5-20 minute sales video scripts.
