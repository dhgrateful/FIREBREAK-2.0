---
name: ad
description: "Create and review Meta/Facebook/Instagram ads. Flexible entry points: full pipeline (copy + images), copy only, creative variations (hook library), video scripts, or compliance review. Use when asked to create ads, ad copy, video scripts, creative variations, or review ads."
---

# /ad — Create Ads from Context

Create ads that sound like you, speak to your buyer, and sell your offer. Multiple entry points — from a single hook to a full campaign batch.

---

## Before Generating

Read these files in order:
1. `reference/core/soul.md` — Who you are
2. `reference/core/audience.md` — Who you serve
3. `reference/core/offer.md` — What you sell
4. `reference/core/voice.md` — How you sound

Also scan `decisions/` and `research/` for recent entries.

If any Context file has `status: draft` or is mostly empty, warn:
"Your [file] is thin. Output quality will improve if you run `/enrich [file]` first. Generate anyway?"

---

## Entry Points

Detect what the user wants from natural language:

| User Says | Mode | What Happens |
|-----------|------|-------------|
| "ads", "ad copy", "full ads" | Full Pipeline | Copy + image prompts |
| "just copy", "ad text" | Copy Only | Primary text + headlines |
| "hooks", "one-liners", "creative variations" | Hook Library | Bulk diversified hooks |
| "video scripts", "ad scripts", "spoken word" | Video Scripts | Camera-ready spoken scripts |
| "review", "audit", "compliance check" | Review | Quality + compliance check |

If unclear, ask: "What do you need? Full ads with images, just copy, hooks/variations, video scripts, or a review?"

---

## Mode: Full Pipeline (Static Ads)

Each batch = 5-6 angles. Each angle = copy + image prompt.

### Hook Rules

**Hook = 123-135 characters** (visible before "See more" on Facebook).

- No questions (binary "no" response kills engagement)
- No "you/your" in first 3 lines
- No emojis
- Pack customer language into the hook

**Hook Formulas:**
1. **Transformation:** "How [audience] go from [pain] to [benefit] using [approach]"
2. **Even Without:** "Here's how even [audience] (without [advantage]) are [achieving benefit]"
3. **Eliminates:** "This [approach] eliminates [pain 1], [pain 2], without [trade-off]"

### Ad Styles (vary across batch)

| Style | Length |
|-------|--------|
| Deep Ad | 500-800 words |
| UGC/Native | 100-300 words |
| Direct Response | 100-400 words |
| Pattern Interrupt | Under 100 words |
| Testimonial | 200-400 words |

### Image Prompts

For each angle, include 3 image prompt types:

| Type | Use Case |
|------|----------|
| Graphic | Typography-focused, frameworks, authority |
| Lo-fi | UGC style, authenticity, social proof |
| Interrupt | Pattern interrupt, scroll-stopping, contrarian |

**Format: 1:1 + 9:16** — design 9:16 first with critical content in centre 1:1 safe zone.

### Workflow

1. Read Context files
2. Ask for campaign name
3. Select 5-6 angles from Context
4. Write all image prompts first
5. Write all ad copy second
6. Cold traffic language check — no insider jargon
7. Save to `outputs/YYYY-MM-DD-ads-[campaign]/ads-batch-001.md`

---

## Mode: Hook Library (Creative Variations)

Generate punchy, diversified hooks for Meta's algorithm. Any quantity — "give me 5" or "give me 50".

### Process

1. **Core Outcome:** Single transformation every buyer achieves
2. **Extract Specifics:** Roles, timelines, niche pains, value props, failed alternatives, proof points
3. **Reasons to Buy:** 15-20 fundamentally different reasons
4. **Hook Categories:** Ensure variety across problem agitation, emotional state, transformation, contrarian, identity callout
5. **Generate:** Requested quantity of creative variations
6. **Save:** `outputs/YYYY-MM-DD-hooks-[campaign]/hooks-batch-001.md`

### The Anchor Rule

Every variation MUST include at least one specific element:
- A specific role, outcome, or company
- A specific niche pain
- A specific value prop
- A specific timeline or proof point

**The Specificity Test:** If this hook could sell a gym membership, a coaching program, or a generic course — it fails. Rewrite it.

---

## Mode: Video Scripts

Create spoken-word ad scripts (30-90 seconds) for camera delivery.

### Script Structure

**Hook** (1-2 sentences): Lead with pain, desire, or belief. Create curiosity.
**Body** (4-8 sentences): Why problem exists. Position offer. Include proof.
**CTA** (2-3 sentences): Clear instruction. What happens after click.

### Spoken Delivery

- Contractions: you're, don't, can't, won't
- Fragments: "Not theory. Patterns."
- Simple words: "use" not "utilise"
- Each ad = fundamentally different reason to buy

Generate 15-30 scripts across multiple angles. Save to `outputs/YYYY-MM-DD-video-ads-[campaign]/video-ads-batch-001.md`

---

## Mode: Review

Review ads through compliance and quality lenses before shipping.

### Checks

| Lens | What It Checks |
|------|----------------|
| Compliance | Earnings claims, health claims, testimonial attribution |
| Platform Policy | Meta triggers, Personal Attributes violations |
| Copy Quality | Hook strength, specificity, cold traffic clarity |
| Voice Match | Does it sound like the client's `voice.md`? |

### Severity

| Level | Meaning |
|-------|---------|
| **P1** | Blocks launch (legal/platform risk) |
| **P2** | Fix before launch (reduces performance) |
| **P3** | Nice to have (optimisation) |

---

## Compliance (All Modes)

**Never say:**
- Cures/treats/heals [condition]
- Guaranteed results
- Will eliminate [problem]

**Safe to say:**
- Many have found this helpful
- Supports/complements existing approach
- Framework for understanding

---

## Quality Checklist (All Modes)

| Check | Requirement |
|-------|-------------|
| Anchor specificity | Every hook has at least one offer-specific detail |
| Cold traffic language | No jargon — stranger understands in 3 seconds |
| Hook length | 123-135 characters for static hooks |
| No questions | Hooks don't start with yes/no questions |
| Angle diversity | Each concept uses a genuinely different entry point |
| Voice match | Copy matches `voice.md` tone |
| Compliance | No banned claims, proper attribution |

---

## Save Output

All outputs use frontmatter:

```yaml
---
type: output
format: ad | video-ad-script | creative-variations
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
