---
name: generate
description: "Generate high-fidelity outputs (ads, emails, proposals, posts) from your Soul files. Context > Prompts."
---

# /generate — Output Generation from Context

Reads your Soul files in `reference/core/` and generates business outputs that sound like you. The more complete your Soul files, the better the output.

## Usage

```
/generate ad          → Facebook/Instagram ad copy
/generate email       → Cold or warm email sequence
/generate post        → LinkedIn post
/generate proposal    → Client proposal
/generate brief       → Morning brief from recent activity
/generate landing     → Landing page copy
```

## Procedure

### 1. Read the Reference Stack

Before generating ANYTHING, read these files in order:
1. `reference/core/soul.md` — Who they are
2. `reference/core/audience.md` — Who they serve
3. `reference/core/offer.md` — What they sell
4. `reference/core/voice.md` — How they sound

Also scan:
- `decisions/` — Recent decisions (last 5 by date)
- `research/` — Recent research (last 3 by date)

### 2. Check Depth

Before generating, assess Soul file completeness:
- If any Soul file is at Skeleton depth (< 200 bytes), warn:
  "Your [file] is thin. Output quality will improve if you run `/extract [file]` first. Generate anyway?"
- If all files are at Working+ depth, proceed.

### 3. Generate Output

Use the full reference stack as context. The output must:
- Use the client's voice (from `voice.md`)
- Reference their specific transformation (from `offer.md`)
- Address their audience's actual pain points (from `audience.md`)
- Reflect their core beliefs (from `soul.md`)
- Incorporate recent decisions if relevant

### 4. Save Output

Write generated content to `outputs/` with format:
```
outputs/[YYYY-MM-DD]-[type]-[slug].md
```

Include frontmatter:
```yaml
---
type: output
format: [ad|email|post|proposal|brief|landing]
date: [today]
source_files:
  - reference/core/soul.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/core/voice.md
---
```

### 5. Before/After (Optional)

If the user asks, show the delta:
- Generate the same output WITHOUT reading Soul files (generic)
- Show both side by side
- The difference is the proof that context > prompts
