---
name: gate
description: "Skill tier gating — checks client tier before running locked skills. Reads tier from vault config."
---

# Skill Gating System

Every skill checks the client's tier before executing. The tier is stored in the vault's config file.

## Tier Config

The file `reference/core/.tier` (or `.tier` in the vault root) stores the client's tier:

```
trial
```

Valid values: `trial`, `build`, `pro`, `vip`

The architect sets this during `/setup`. It's a plain text file — no YAML, no complexity.

## How Gating Works

Every skill SKILL.md includes a tier requirement in its frontmatter. Before executing, check:

1. Read `reference/core/.tier` (fall back to `.tier` in vault root if not found)
2. Compare against the skill's required tier
3. If the client's tier is sufficient, run the skill
4. If not, show the upgrade message

## Tier Hierarchy

```
trial < build < pro < vip
```

- `trial` can run trial-tier skills only (with extraction limits)
- `build` can run trial + build skills
- `pro` can run trial + build + pro skills
- `vip` can run all skills

## Skill Map

### Free Trial

5 extractions + 3 content outputs, no credit card required.

| Skill | Description |
|-------|-------------|
| `/start` | Guided onboarding — first run experience |
| `/extract` | Up to 5 extractions (soul, audience, offer, voice, positioning), then shows upgrade prompt |
| `/import` | Mine existing documents into Context files (counts as an extraction) |
| `/content` | Up to 3 content outputs, then shows upgrade prompt |
| `/audit` | Vault health check (read-only) |

### Build ($99/mo or $699/yr)

Everything in Free Trial (with unlimited extractions and content), plus:

| Skill | Description |
|-------|-------------|
| `/start` | Guided onboarding — first run experience |
| `/extract` | Unlimited — all extractions, re-enterable |
| `/import` | Unlimited — no extraction cap |
| `/enrich` | Deepen existing Context files with follow-up questions |
| `/content` | Unlimited content for any platform (LinkedIn, blog, newsletter, X/Twitter) |
| `/research` | Research a prospect, competitor, market trend, or scan for opportunities |
| `/brief` | Morning brief — decisions, priorities, open threads |
| `/spy` | Competitive intelligence and positioning analysis |
| `/audit` | Vault health check (read-only) |
| `/optimise` | Improve and tighten existing outputs using your context |

### Pro ($199/mo or $1,497/yr) — Most Popular

Everything in Build, plus:

| Skill | Description |
|-------|-------------|
| `/ad` | Generate ad copy (Meta/Facebook/Instagram) |
| `/email` | Generate email sequences (cold, warm, nurture) |
| `/landing` | Generate landing page copy |
| `/proposal` | Generate client proposal |
| `/pitch` | Elevator pitch, event intro, podcast bio, speaker page |
| `/funnel` | Map and generate a full sales funnel |
| `/case-study` | Turn a client win into a formatted case study |
| `/follow-up` | Write a follow-up message after a call or meeting |
| `/objection` | Handle a sales objection using your context |
| `/site` | Generate website copy trained on your context |
| `/leads` | Lead generation and outreach sequences |
| `/ghl` | GoHighLevel integration — push contacts, triggers, automations |

### VIP ($497/mo or $2,997/yr)

Everything in Pro, plus:

| Skill | Description |
|-------|-------------|
| `/publish` | Distribute outputs to live channels |
| `/campaign` | Full pipeline — generate + distribute across channels |
| `/repurpose` | One piece of content into every channel |
| Done-for-you | Architect-managed content calendar and execution |
| Sovereign vault | Dedicated hosting, private repos, custom integrations |

### Architect-Only (Internal — Not Client-Facing)

These skills are used by Codify architects to manage client vaults. They do not appear in client-facing menus.

| Skill | Description |
|-------|-------------|
| `/update` | Pull latest Codify skills and system updates (never touches client data) |
| `/openclaw` | Engine orchestration and automation internals |
| `/gate` | This skill — tier enforcement logic |
| `/setup` | Initial vault provisioning and personalization |

## Upgrade Prompts

When a client tries a locked skill:

**Trial → Build:**
"This skill is available on the Build plan ($99/mo). You get unlimited extractions, content generation, research, and a daily brief — all trained on your context. Ready to upgrade? Talk to your Codify architect."

**Trial/Build → Pro:**
"This skill is available on the Pro plan ($199/mo) — our most popular tier. You get ad copy, email sequences, landing pages, proposals, funnels, and lead generation — all sounding like you. Ready to upgrade? Talk to your Codify architect."

**Any → VIP:**
"This skill is available on the VIP plan ($497/mo). You get done-for-you campaigns, multi-channel distribution, content repurposing, and a sovereign vault with dedicated infrastructure. Ready to upgrade? Talk to your Codify architect."

## Extraction Limit (Free Trial Only)

For trial tier, track extraction count in `reference/core/.extractions`:

```
2
```

Increment after each `/extract` or `/import` run. At 5, show:
"You've used your 5 free extractions. Your Context files are already improving your outputs — imagine what unlimited extractions and full content generation can do. Upgrade to Build ($99/mo) to unlock everything."

Track content output count in `reference/core/.content-outputs`:

```
1
```

Increment after each `/content` run. At 3, show:
"You've used your 3 free content outputs. You've seen what your context can produce — unlock unlimited content, research, and daily briefs on the Build plan ($99/mo). Talk to your Codify architect."

## Notes

- The `.tier`, `.extractions`, and `.content-outputs` files are dotfiles — hidden in Obsidian by default
- The architect sets the tier during `/setup` or manually
- Upgrading is just changing one word in `.tier` — no API calls, no license servers
- This is an honor system backed by the relationship, not DRM
- `/import` counts against the trial extraction limit because it writes to Context files
