# CLAUDE.md — Context Architecture Conventions

This file tells any AI assistant how to work inside this vault. Read it before doing anything.

---

## Who This Vault Belongs To

A senior leader with deep domain expertise. Their institutional knowledge — frameworks, beliefs, judgment calls — is the most valuable asset in this vault. Respect it. Preserve their voice. Never genericize their expertise.

## Vault Structure

- `reference/core/` — Core identity files: soul, audience, offer, voice.
- `decisions/` — Strategic decisions with dates and reasoning.
- `research/` — Market intelligence, competitor analysis, industry signals.
- `outputs/` — Generated content: ads, emails, proposals, campaigns.
- `content/` — Published and draft content (LinkedIn, newsletter, blog).
- `whatsapp/` — Pocket Architect conversation logs.
- `snapshots/` — Context snapshots and extraction archives.

## Skills

All work runs through skills in `.claude/skills/`:
- `/start` — Welcome screen. Shows vault state and what to do next
- `/setup` — Personalize a new vault
- `/extract` — Context Extraction interviews (soul, audience, offer, voice)
- `/import` — Mine existing documents (proposals, emails, website copy) into Context files
- `/enrich` — Deepen thin Context files with follow-up questions
- `/generate` — Generate high-fidelity outputs (ads, emails, proposals) from Context files
- `/ad` — Generate ad copy (Meta/Facebook/Instagram)
- `/email` — Generate email sequences (cold, warm, nurture)
- `/content` — Generate content for any platform (LinkedIn, blog, newsletter, X/Twitter, Instagram)
- `/proposal` — Generate client proposal
- `/landing` — Generate landing page copy
- `/site` — Generate website pages — copy + code — from Context files
- `/case-study` — Turn a client win into a formatted case study
- `/follow-up` — Write a follow-up message after a call or meeting
- `/objection` — Handle a sales objection using your context
- `/pitch` — Elevator pitch, event intro, podcast bio, speaker page
- `/snapshot` — Rapid extraction from a voice note, call transcript, or business summary
- `/research` — Research a prospect, competitor, market trend
- `/scout` — Cross-reference context against market signals, surface opportunities
- `/brief` — Morning brief: vault health, open tasks, recommended focus
- `/audit` — Check vault health
- `/security` — Vault security audit, red team simulation, hardening report
- `/gate` — Check/set tier gating for skill access
- `/publish` — Push outputs to live channels (Focus tier)
- `/campaign` — Full pipeline: ad + email + content + landing, then distribute (Focus tier)
- `/repurpose` — Take one output, create versions for every channel (Focus tier)
- `/update` — Pull latest Codify skills and system updates (never touches client data)
- `/openclaw` — Set up OpenClaw autonomous operations (Focus tier, architect-only)

## File Conventions

- **Frontmatter is required.** Every file starts with YAML frontmatter:
  ```yaml
  ---
  type: context | decision | research | output | daily
  status: active | draft | archived
  date: YYYY-MM-DD
  last-updated: YYYY-MM-DD HH:MM
  ---
  ```
- **Always update `last-updated`** when modifying any file. Use the current date and time (24h format). This tells the client when each file was last touched.
- **Use Obsidian links.** Write `[[soul]]` not `[soul](soul.md)`. Double brackets create the knowledge graph.
- **Cross-reference everything.** When a decision relates to the audience, link it: `[[audience]]`. This builds the compound loop.
- **Date your files.** Decisions and research use format: `YYYY-MM-DD-topic-slug.md`

## Writing Rules

- Lead with the point. No throat-clearing.
- Use bullet points over paragraphs where possible.
- Include "Why" sections in every decision file.
- Keep daily notes short — 3-5 bullets max.
- **Preserve the client's exact language during extraction.** Clean up grammar only if unclear. Do NOT rewrite their voice — capture it. Their 30 years of judgment shows up in how they phrase things.

## Folder Routing

When creating new files:
- Strategic choices → `decisions/`
- Market data, competitor intel, trends → `research/`
- Generated content (ads, emails, proposals) → `outputs/`
- Published content (LinkedIn, newsletters) → `content/`
- Never modify `reference/core/` files casually — these are the foundation. Enrich deliberately via `/enrich`.

## The Compound Loop

This vault gets smarter because:
1. Decisions and research are captured continuously
2. Those files link back to Context files
3. AI reads the full graph before generating anything
4. Outputs improve because context compounds
5. Monthly review hardens the best insights into permanent Context files

**Context > Prompts. Always.**

---

*This file is read by Claude Code, ChatGPT, Gemini, or any AI that opens this folder. It makes them work like they know the business.*
