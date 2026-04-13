---
name: brief
description: "Welcome back + morning brief. Shows vault state, recent changes, what to do next, and recommended focus. Use this when starting a session, checking in, or asking for a summary."
---

# /brief — Welcome Back + Morning Brief

The single entry point for "where am I and what should I do next?" Combines vault state, recent activity, and recommended focus into one view.

## Usage

```
/brief              → Today's brief (welcome + status + focus)
/brief weekly       → Week-in-review summary
```

---

## Procedure

### 1. Read the Vault State

Before showing anything, silently read:
- All files in `reference/core/` — check `status` and `last-updated` in frontmatter
- Recent files in `outputs/` — last 3 by date
- Recent files in `decisions/` — last 3 by date
- Recent files in `research/` — last 3 by date
- Count of files in each folder

### 2. Determine First Visit or Return

**First visit** — all Context files have `status: draft` or are template-only (contain `<!-- -->` placeholders with no real content).

**Returning** — at least one Context file has `status: active` or `status: compounding`.

### 3. If First Visit

**Welcome to Codify**

This is your Context Architecture — a secure vault where your expertise compounds over time. Everything you share here stays here. The AI reads it all before generating anything, so your outputs reflect your judgment, not generic advice.

**Start here:**
- Type `/extract soul` to capture your core identity
- Or `/import` if you have existing material (proposals, website copy, emails) — it's faster

### 4. If Returning — Generate Brief

Format:

```markdown
# Brief — [date]

## Your Context Files
- [For each file: name, depth (Draft / Working / Strong), last-updated]
- [Flag any file not updated in 14+ days]

## Since Last Session
- [New files in outputs/, decisions/, research/]
- [Modified Context files]
- [Recent git commits via `git log --since="24 hours ago"`]

## Vault Health
- [File counts per folder]
- [Stale files count]
- [Biggest enrichment opportunity]

## Open Tasks
- [ ] [Any unchecked tasks across vault markdown files]

## Recommended Focus
[1-2 sentence recommendation based on vault state and recent activity]
```

**Recommended next step logic:**
- If any Context file has `status: draft`: "Your [file] could go deeper. Run `/enrich [file]` to strengthen it."
- If any Context file has no `[[links]]`: "Your [file] has no connections. Run `/enrich [file]` to link it up."
- If all Context files are strong: "Your context is solid. Ready to create? Try `/ad`, `/email`, `/content`, or `/proposal`."

### 5. Show Available Skills

| Command | What It Does |
|---------|-------------|
| `/extract` | Build Context files through conversation |
| `/import` | Mine existing documents into Context files |
| `/enrich` | Go deeper on any Context file |
| `/think` | Research, decide, and codify — strategic reasoning |
| `/ad` | Create ad copy, hooks, video scripts |
| `/email` | Create email sequences |
| `/content` | Create content for any platform |
| `/proposal` | Create a client proposal |
| `/landing` | Create landing page copy |
| `/vsl` | Write video sales letter scripts |
| `/case-study` | Turn a client win into a case study |
| `/follow-up` | Write a follow-up after a call or meeting |
| `/objection` | Handle a sales objection |
| `/pitch` | Elevator pitch, event intro, speaker bio |
| `/research` | Research a prospect, competitor, or market trend |
| `/audit` | See your vault health |

### 6. Save + Deliver

Save to `content/[date]-brief.md` and display in chat.

---

## Tone Rules

- Do NOT mention git, GitHub, terminal, CLI, API, MCP, skills, or any technical infrastructure
- This client is a senior leader with deep expertise. Speak to their intelligence, not their technical ability.
- Keep it concise. No filler. Lead with what matters.
- The status report IS the value. They type `/brief` and immediately know where they stand.
