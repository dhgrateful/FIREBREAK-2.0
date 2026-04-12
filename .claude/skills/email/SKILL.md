---
name: email
description: "Generate email sequences (cold outreach, warm nurture, follow-up) from your Context files."
---

# /email — Generate Email Sequence

Creates emails that sound like you wrote them, not a marketer.

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

Ask the client: "What kind of email? Cold outreach, warm follow-up, or nurture sequence?"

**Cold outreach (default):** 3-email sequence
- Email 1: Pattern-interrupt opener. Lead with insight, not pitch.
- Email 2: Proof/story. One specific client result.
- Email 3: Direct ask. Short, no pressure, clear next step.

**Warm follow-up:** Single email responding to a specific trigger (met at event, they downloaded something, referral intro).

**Nurture sequence:** 5-email sequence that builds authority over 2 weeks.

The copy must:
- Use the client's voice — short sentences if that's their style, direct if that's their tone
- Never open with "I hope this finds you well" or any filler
- Reference specific transformations, not vague promises
- Include their signature phrases naturally

## Save Output

Write to `outputs/[YYYY-MM-DD]-email-[slug].md` with frontmatter:

```yaml
---
type: output
format: email
date: [today]
last-updated: [today's date and time]
source_files:
  - reference/core/soul.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/core/voice.md
---
```
