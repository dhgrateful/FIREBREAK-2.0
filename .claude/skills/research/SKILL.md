---
name: research
description: "Research a prospect, competitor, market trend, or topic. Saves to research/ and cross-references with Context files. Compounds over time."
---

# /research — Research That Compounds

Gathers intelligence and saves it to your vault where it informs every future output. Research files are the fuel for `/ad`, `/email`, `/proposal`, and `/objection`.

## Usage

```
/research                    → Ask what to research
/research prospect [name]    → Pre-call brief on a prospect
/research competitor [name]  → Competitive analysis
/research market [topic]     → Market trend or industry signal
/research topic [topic]      → Deep dive on any subject relevant to your business
/research opportunities      → Scan all context + research files for revenue opportunities
```

## Before Researching

Read these files first:
1. `reference/core/audience.md` — So you can flag fit signals for prospects
2. `reference/core/soul.md` — So you can compare competitors against your positioning
3. `reference/core/offer.md` — So you can identify differentiation gaps
4. Recent files in `research/` — So you don't duplicate existing research

---

## Mode: Prospect Research

**Triggered by:** `/research prospect David Park` or `/research prospect Meridian HVAC`

### What to Find

Use web search to gather:
- Company overview (what they do, size, industry, revenue if public)
- The person's role, tenure, background
- Recent news, press mentions, podcast appearances
- Company reviews (Glassdoor, G2, industry forums)
- LinkedIn profile summary (via Google cache — do NOT scrape LinkedIn directly)
- Any public content they've written or been quoted in

### Cross-Reference with Context

After gathering, compare findings against `audience.md`:
- **Fit signals** — Does this person match the buyer profile? Flag specific matches.
- **Pain signals** — Any indicators of the problems described in `audience.md#Voice of Customer`?
- **Buying trigger signals** — Any recent events that match `audience.md#Buying Trigger`? (leadership change, acquisition activity, rapid growth, public complaints)
- **Disqualifier signals** — Anything that matches `audience.md#Disqualifiers`? Flag honestly.

### Output Format

```markdown
## Pre-Call Brief: [Name] — [Company]

### Fit Assessment
[Strong fit / Possible fit / Likely not a fit] — [one-line reason]

### Background
[2-3 sentences on the person and company]

### What They're Likely Dealing With
[Based on company signals cross-referenced with audience.md]

### Talking Points
- [Specific thing to reference in conversation]
- [Question to ask based on what you found]
- [Connection point to your framework from soul.md]

### Watch For
[Any disqualifier signals or red flags]

### Sources
[Links to where you found this information]
```

---

## Mode: Competitor Research

**Triggered by:** `/research competitor [name]`

### What to Find

- Their positioning (website, about page, sales page)
- Their offer structure and pricing (if public)
- Their content strategy (what they post, where, how often)
- Their client testimonials and case studies
- Their weaknesses (complaints, negative reviews, gaps in positioning)

### Cross-Reference with Context

Compare against your `soul.md` and `offer.md`:
- **Where you overlap** — Same claims, same audience, same language
- **Where you differ** — Your contrarian beliefs vs. their conventional positioning
- **Where they're weak** — Gaps in their offer that your framework addresses
- **Where they're strong** — Be honest. What are they doing well?

### Output Format

```markdown
## Competitor Analysis: [Name]

### Their Positioning
[What they claim to do]

### Your Differentiation
[Where your approach from soul.md diverges — be specific]

### Their Gaps
[What they don't cover that you do]

### Their Strengths
[What they do well — be honest]

### Opportunity
[One actionable insight for your positioning, content, or outreach]
```

---

## Mode: Market Research

**Triggered by:** `/research market [topic]`

Search for trends, data, reports, and signals on the topic. Cross-reference against `soul.md` and `audience.md` to find angles unique to your positioning.

### Output Format

```markdown
## Market Signal: [Topic]

### What's Happening
[Summary of the trend or data]

### Why It Matters to Your Business
[How this connects to your audience, offer, or positioning]

### Opportunity
[What you could do with this — content angle, offer adjustment, outreach timing]

### Sources
[Links]
```

---

## Mode: Topic Research

**Triggered by:** `/research topic [topic]`

Deep dive on any subject. Could be an industry concept, a methodology, a new regulation, a technology shift — anything the client wants to understand better.

Cross-reference against all Context files and existing research to find connections.

---

## Mode: Opportunities

**Triggered by:** `/research opportunities`

This is the strategic scan. Reads your full vault — all Context files, all research, all decisions — and surfaces revenue opportunities unique to your positioning.

### Load Full Context

Read in order:
1. All `reference/core/` files
2. Last 10 `decisions/` files
3. All `research/` files
4. Last 5 `outputs/` files (to avoid repeating)

### Cross-Reference

- What does your `soul.md` say you believe that your market doesn't? Where's the content gap?
- What does `audience.md` say they struggle with that no competitor is addressing?
- What does `offer.md` deliver that competitors don't mention? Where's the positioning gap?
- What patterns emerge across your prospect research? Who keeps showing up?
- What recent decisions suggest a new angle?

### Output Format

For each opportunity:
- **The signal** — What data point triggered this
- **The gap** — Why nobody else is doing this
- **The play** — What you'd actually do (content, outreach, offer adjustment)
- **The source** — Which files informed this insight

---

## Save to Vault

Write ALL research to `research/[YYYY-MM-DD]-[mode]-[slug].md` with frontmatter:

```yaml
---
type: research
format: [prospect|competitor|market|topic]
date: [today]
last-updated: [today's date and time]
related:
  - "[[audience]]"
  - "[[soul]]"
---
```

**Always add `[[cross-references]]`** to the Context files that informed or are informed by this research.

## The Compound Loop

Research files are not throwaway. They accumulate:
- `/research opportunities` scans all research files to find patterns across prospects and competitors
- `/ad` and `/email` reference recent research for timely angles
- `/objection` pulls competitor research for differentiation arguments
- `/proposal` uses prospect research for personalized framing
- The architect reviews research during Brain Sync calls to spot strategic patterns the client can't see from inside their business

**More research = smarter outputs. That's the compound loop.**

## Architect Integration

The architect uses research during Brain Sync sessions:
- Reviews accumulated prospect research to identify ideal client patterns
- Reviews competitor research to refine positioning in `soul.md`
- Reviews market research to inform strategic decisions in `decisions/`
- Spots patterns across multiple research files that the client misses day-to-day
- Updates Context files based on research insights — this is where compounding happens

Research is the raw material. The architect turns it into strategic direction. The Context files capture the direction. The outputs reflect it. That's the loop.
