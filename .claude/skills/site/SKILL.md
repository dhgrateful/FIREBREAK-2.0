---
name: site
description: "Generate website pages — copy + code — from your Context files. No design tools needed."
---

# /site — Build Website Pages From Your Context

Generates complete website pages — copy AND working HTML — from your vault. Your Context files are the design system. No Figma, no Canva, no third-party tools.

## Before Generating

Read these files in order:
1. `reference/core/soul.md` — Who you are, what you believe
2. `reference/core/audience.md` — Who you serve
3. `reference/core/offer.md` — What you sell
4. `reference/core/voice.md` — How you sound
5. `reference/core/design.md` — Brand colours, fonts, style (if it exists)

Also scan `decisions/` and `research/` for recent entries.

If any Context file has `status: draft` or is mostly empty, warn:
"Your [file] is thin. Output quality will improve if you run `/enrich [file]` first. Generate anyway?"

If `reference/core/design.md` doesn't exist, ask:
"No design file found. I'll ask a few quick questions to create one — or I can use clean defaults. Your call."

## Design File Setup

If creating `reference/core/design.md`, ask these questions:

1. "What are your brand colours? (If unsure, share your logo or website and I'll extract them)"
2. "Any font preference? (If not, I'll use a clean modern pairing)"
3. "What's the feel — corporate, friendly, bold, minimal?"

Create `reference/core/design.md` with:

```yaml
---
type: context
status: active
date: [today]
last-updated: [today's date and time]
---
```

Include:
- **Colours** — primary, secondary, accent, background, text
- **Fonts** — headings, body (use Google Fonts for portability)
- **Style** — border radius, spacing scale, shadow style
- **Components** — button style, card style, section patterns

## What to Generate

Ask: "What page do you need — homepage, about, services, contact, or something else?"

### Homepage
1. **Hero** — Headline from `offer.md` transformation + subheadline + primary CTA
2. **Problem** — 3 pain points from `audience.md#Voice of Customer`
3. **Solution** — Your approach from `soul.md`
4. **How it works** — 3 steps from `offer.md` delivery mechanics
5. **Proof** — Testimonials or results from `soul.md#External Perception`
6. **CTA** — Repeat the primary action

### About
1. **Origin story** — From `soul.md#Origin Story` and `soul.md#Defining Moments`
2. **Mission** — From `soul.md#Mission`
3. **Credentials** — From `soul.md#External Perception`
4. **Values** — From `soul.md#Core Beliefs`

### Services
1. **Offer breakdown** — From `offer.md` tiers/packages
2. **Who it's for** — From `audience.md`
3. **What's included** — From `offer.md` deliverables
4. **Pricing** — From `offer.md` if public

### Contact
1. **Simple form** — Name, email, message
2. **Direct line** — From `offer.md` or `soul.md` contact info
3. **Social links** — If available in context

## Build Rules

Generate a single self-contained HTML file per page:
- All CSS inline in a `<style>` block (no external dependencies except Google Fonts)
- Mobile-responsive (flexbox/grid, media queries)
- Semantic HTML (`<header>`, `<main>`, `<section>`, `<footer>`)
- Fast — no JavaScript unless the page needs it (form validation, mobile nav toggle)
- Accessible — proper heading hierarchy, alt text, contrast ratios
- All colours, fonts, and spacing from `reference/core/design.md`

Do NOT:
- Add cookie banners, analytics, or tracking
- Use CSS frameworks (Bootstrap, Tailwind)
- Add placeholder images — use CSS shapes/gradients or leave image spots clearly marked with `<!-- IMAGE: description of what goes here -->`
- Over-design. Clean and functional beats fancy.

## Multi-Page Sites

If generating multiple pages:
1. Create consistent navigation across all pages
2. Use relative links between pages
3. Share the same `<style>` block (copy it, don't reference external files)
4. Keep footer consistent

## Save Output

Save TWO files per page:

**Copy file** (for review and editing):
`outputs/[YYYY-MM-DD]-site-[page-slug].md`

```yaml
---
type: output
format: site-copy
page: [homepage|about|services|contact]
date: [today]
last-updated: [today's date and time]
source_files:
  - reference/core/soul.md
  - reference/core/audience.md
  - reference/core/offer.md
  - reference/core/voice.md
  - reference/core/design.md
---
```

**Built page** (ready to deploy):
`outputs/site/[page-slug].html`

After generating, tell the client:
"Your page is ready. Open `outputs/site/[page-slug].html` in a browser to preview. Edit the copy in the `.md` file and re-run `/site` to rebuild."

## Tone

Match `voice.md`. No hype, no filler. Every word earns its place.
