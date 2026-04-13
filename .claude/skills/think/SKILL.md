---
name: think
description: "Combined research, decision, and codification workflow. Use when exploring a question, making a decision, or updating Context files based on new information. The strategic reasoning skill — fills the gap between extraction and generation."
---

# /think — Research, Decide, Codify

This skill is for: **"I need to work through something before I act."**

Something came your way — a competitor move, a pricing question, a market shift, a vague feeling that something needs to change. You don't need a plan. Just start. The skill finds the overlap between your thinking and your context.

---

## Two Modes of Work

| Mode | You're doing | Examples |
|------|--------------|----------|
| **Enriching the core** | Pulling insights → Context files | Mining conversations, making decisions, updating offer.md |
| **Creating for the world** | Context files → output | Ads, emails, proposals, content |

`/think` is for **enriching the core**. When you're ready to create, use `/ad`, `/email`, `/content`, or just ask.

Both are work. Enriching the core levels up everything downstream.

---

## Route by Intent

Detect mode from natural language:

| User Says | Mode |
|-----------|------|
| "figure out", "explore", "I'm trying to..." | Full Flow |
| "research", "investigate", "what do we know about" | Research Only |
| "decide", "we chose", "document decision" | Decide Only |
| "codify", "apply", "update context files" | Codify Only |
| "add context", "enrich", "I have new info" | Codify Only |

If unclear, ask: "Are you exploring a question, documenting a decision, or updating Context files?"

---

## Procedure

### 1. Read the Context Stack

Before anything, read:
1. `reference/core/soul.md`
2. `reference/core/audience.md`
3. `reference/core/offer.md`
4. `reference/core/voice.md`

Scan recent files:
- `decisions/` — last 5 by date
- `research/` — last 3 by date

### 2. Full Flow (Default)

```
Research → Checkpoint → Decide → Checkpoint → Codify
```

**Research phase:**
- Define the question: "What specifically are you trying to figure out?"
- Gather from vault context, web search, user input
- Synthesize: one-sentence summary, key findings (5-10 bullets), implications for Context files, open questions
- Save to `research/YYYY-MM-DD-topic.md`

**Checkpoint:**
> "Ready to make a decision, or need more research?"

**Decide phase:**
- Present options with pros/cons
- Document choice and rationale
- Describe what Context files are affected:
  ```markdown
  ## What Changes
  offer.md gets a guarantee section. audience.md gets a new pain point.
  ```
- Save to `decisions/YYYY-MM-DD-topic.md`

**Checkpoint:**
> "Ready to update Context files now, or save for later?"

**Codify phase:**
- Apply changes described in the decision to Context files
- Update `last-updated` on every file touched
- Cross-reference with `[[links]]` where relevant

### 3. Research Only

```
/think research "topic"
```

Investigate, synthesize, save to `research/`. Don't decide yet.

### 4. Decide Only

```
/think decide "topic"
```

Document a decision with rationale. Save to `decisions/`.

### 5. Codify Only

```
/think codify
```

Apply recent decisions to Context files. Check for accepted decisions not yet codified.

---

## Active Guidance

On every `/think` invocation, detect state and guide:

| If you find... | Then... |
|----------------|---------|
| Recent research, no decision | "You have research on [topic]. Ready to make a decision?" |
| Decision documented but not codified | "Decision [topic] is accepted. Ready to update Context files?" |
| Nothing in progress | "What are you trying to figure out?" |

**The goal is Context files.** Research and decisions are waypoints. Keep asking: "What needs to happen to get this into your Context?"

---

## File Formats

**Research output:**
```yaml
---
type: research
status: active
date: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
---
```

**Decision output:**
```yaml
---
type: decision
status: proposed | accepted | codified
date: YYYY-MM-DD
last-updated: YYYY-MM-DD HH:MM
---
```

---

## When NOT to Use

- Quick factual questions (just ask)
- Simple file edits (just edit)
- Generating content (use `/ad`, `/email`, `/content`, `/vsl`)

Use `/think` when the answer requires investigation and the choice needs documentation.

---

## Why This Matters

Research and decisions go stale. Context files compound. Every update makes all downstream content better. The think cycle filters — not everything goes in. Only the sharpest insights survive into Context. Curation over collection.
