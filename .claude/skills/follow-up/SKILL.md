---
name: follow-up
description: "Generate a follow-up message after a call or meeting. Sounds like you, references what was discussed."
---

# /follow-up — Write a Follow-Up

Creates a follow-up email or message after a call, meeting, or event. Sounds like you wrote it, not a template.

## Before Generating

Read these files in order:
1. `reference/core/voice.md` — How you sound
2. `reference/core/offer.md` — What you sell (in case they need next steps)
3. `reference/core/soul.md` — Your beliefs (for any insight you'd naturally drop)

## Ask Two Questions

1. "Who did you just meet with? Name and context — prospect, existing client, referral, event connection?"
2. "What stood out from the conversation? Anything specific they said, a problem they mentioned, or something you promised to send?"

## Write the Follow-Up

Rules:
- Open with the point, not "Great meeting you" filler
- Reference something specific from the conversation (this is what makes it feel personal, not templated)
- Keep it under 150 words
- Match their voice from `voice.md` exactly — if they're direct, be direct. No softening.
- Include one insight or observation they didn't ask for — something that shows you were listening and thinking. Pull from `soul.md#Institutional Knowledge` if relevant.
- End with a clear next step — not "let me know if you'd like to chat." Something specific: "I'll send the Decision Audit overview Thursday" or "Want me to sit in on your Monday standup?"

Do NOT:
- Use "I hope this finds you well"
- Use "It was great connecting"
- Use "Just circling back"
- Use "Let's find some time"
- Add a PS unless it's genuinely useful

## Save Output

Write to `outputs/[YYYY-MM-DD]-follow-up-[name-slug].md` with frontmatter:

```yaml
---
type: output
format: follow-up
date: [today]
last-updated: [today's date and time]
source_files:
  - reference/core/voice.md
  - reference/core/offer.md
  - reference/core/soul.md
---
```
