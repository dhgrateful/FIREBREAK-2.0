---
name: scout
description: "Cross-reference your context against market signals. Surface opportunities your competitors can't see because they don't have your context."
---

# /scout — Opportunity Scouting

Reads your Soul files and cross-references them against market data to surface revenue opportunities unique to your expertise. Generic AI finds generic opportunities. Your AI — loaded with your context — finds opportunities only you can see.

## Usage

```
/scout               → Full opportunity scan
/scout competitors   → Analyze competitor positioning gaps
/scout content       → Find content angles from your reference stack
/scout offers        → Identify offer variations from audience pain points
```

## Procedure

### 1. Load Full Context

Read in order:
1. All `reference/core/` files
2. Last 10 `decisions/` files
3. Last 10 `research/` files
4. Last 5 `outputs/` files (to avoid repeating)

### 2. Cross-Reference

Based on mode:

**Full scan:**
- What does your soul.md say you believe that your market doesn't?
- What does your audience.md say they struggle with that nobody's addressing?
- What does your offer.md deliver that competitors don't mention?
- What recent decisions suggest a new positioning angle?

**Competitors:**
- Search web for competitors mentioned in research files
- Compare their positioning to your Soul files
- Identify gaps they're not covering that you can

**Content:**
- Cross-reference audience pain points with your frameworks
- Identify untold stories from your origin moments
- Find proof points from recent decisions that could become content

**Offers:**
- Map audience buying triggers to offer mechanics
- Identify underserved segments from disqualifier patterns
- Find upsell opportunities from existing transformation promises

### 3. Output Opportunities

For each opportunity, provide:
- **The signal** — What data point triggered this
- **The gap** — Why nobody else is doing this
- **The play** — What you'd actually do
- **The source** — Which Soul files informed this insight

### 4. Save to Research

Write findings to `research/[date]-scout-[mode].md` with proper frontmatter and cross-references to the Soul files that informed the analysis.
