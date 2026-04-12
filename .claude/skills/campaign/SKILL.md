---
name: campaign
description: "Full pipeline — generate ad + email + post + landing page from Context files, then distribute everything. One command, full campaign."
---

# /campaign — Full Campaign Pipeline

One skill. Full campaign. Reads your Context files, generates every asset, and distributes them to live channels.

This is the highest-value skill in the system. It's the reason context compounds into revenue.

## Usage

```
/campaign                    → Full campaign (ad + email + post + landing)
/campaign launch [topic]     → Campaign around a specific topic/offer
/campaign retarget           → Retargeting campaign from existing outputs
```

## Procedure

### 1. Load Full Context

Read in order:
1. All `reference/core/` files
2. Last 5 `decisions/`
3. Last 5 `research/`
4. Last 5 `outputs/` (to avoid repeating)

### 2. Identify the Campaign Angle

If topic specified, use it. Otherwise, ask:
"What's this campaign about? (new offer, event, content push, seasonal, retarget)"

Cross-reference the topic against Context files to find:
- The audience pain point it addresses (from `audience.md`)
- The transformation it promises (from `offer.md`)
- The voice it should use (from `voice.md`)
- The belief it's built on (from `soul.md`)

### 3. Generate All Assets

Create these in sequence, each building on the last:

**Asset 1: Ad Copy (3 variations)**
- Hook A: Pattern interrupt
- Hook B: Problem-aware
- Hook C: Proof-forward
- Body: Problem → agitation → solution → proof → CTA
- Save to `outputs/[date]-campaign-ad-[slug].md`

**Asset 2: Email Sequence (3 emails)**
- Email 1: Problem awareness (day 0)
- Email 2: Solution + proof (day 2)
- Email 3: CTA + urgency (day 4)
- Save to `outputs/[date]-campaign-email-[slug].md`

**Asset 3: LinkedIn Post**
- Contrarian take or data point from Context files
- Short paragraphs, white space
- Ends with observation, not hard CTA
- Save to `outputs/[date]-campaign-post-[slug].md`

**Asset 4: Landing Page Copy**
- Headline (from ad hook that works best)
- Subheadline (the transformation)
- 3 bullet proof points
- Objection handling (from `offer.md`)
- CTA
- Save to `outputs/[date]-campaign-landing-[slug].md`

### 4. Review Package

Present all 4 assets together:

"Here's your full campaign:

**Ads** — 3 variations ready to test
**Emails** — 3-email sequence, spaced 2 days apart
**LinkedIn** — 1 post, ready to publish
**Landing page** — Copy ready for your page builder

Want to review each one, or distribute everything now?"

### 5. Distribute

If approved, run `/publish` on each asset:
- Ads → GoHighLevel social posts
- Emails → GoHighLevel email campaign or Gmail drafts
- LinkedIn post → GoHighLevel social
- Landing page → Provide copy (manual placement)

### 6. Log Campaign

Create a campaign log in `outputs/[date]-campaign-log-[slug].md`:

```yaml
---
type: output
format: campaign-log
date: [today]
campaign: [topic]
assets:
  - ad-copy: 3 variations
  - email-sequence: 3 emails
  - linkedin-post: 1
  - landing-page: 1
distributed:
  - channel: [list]
    date: [today]
source_files:
  - reference/core/soul.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/core/voice.md
---
```

This tracks what campaigns ran, what context they used, and where they went. Over time, this data compounds — showing which Context file elements drive the best campaigns.
