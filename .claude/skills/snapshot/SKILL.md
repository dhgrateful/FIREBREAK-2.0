---
name: snapshot
description: "Snapshot — rapid extraction from a voice note, call transcript, or business summary. Produces a polished, standalone deliverable."
---

# /snapshot — Snapshot Extraction

One-shot extraction that turns a voice note, call recording, or business summary into three polished context files: Soul, Voice, and Audience. This is the $97 low-ticket product — the client gets a tangible artifact in 48 hours.

## Usage

```
/snapshot <path-to-input>     → Extract from a file (voice transcript, business summary, etc.)
/snapshot                     → Paste or type input directly
```

## Input Sources (any one of these)

- Voice note transcript (from WhatsApp or call)
- Written business summary (email, DM, document)
- Call recording transcript
- Existing website/LinkedIn content (imported via /import first)

Minimum viable input: 500 words or a 3-minute voice note. More is better.

## Procedure

### 1. Read the Input

Read the provided file or pasted content. Identify:
- Who this person is and what they do
- Their beliefs, contrarian positions, origin story
- How they talk — tone, phrases, energy
- Who they serve and what those people struggle with

If the input is thin (under 300 words), flag it:
"This is light — I can build a skeleton, but the snapshot will be stronger with more material. Can you add anything about [specific gap]?"

### 2. Extract Three Files

Write to `reference/core/` — but only these three:

#### soul.md
From the input, extract:
- **Core Description** — what they do, plain language
- **Contrarian Belief** — what they believe that others get wrong
- **Origin Moment** — the story behind their approach (if present)
- **Anti-Positions** — what they refuse to do
- **Institutional Knowledge** — what would be lost if they retired

Mark any section without enough signal as `<!-- Needs enrichment — schedule a Brain Sync -->`.

#### voice.md
From the input, extract:
- **Tone Calibration** — classify as A (analytical), B (guide), or C (practitioner) with reasoning
- **Signature Phrases** — exact words and phrases they repeat
- **Anti-Language** — words/styles that don't match (infer from what they DO say)
- **Voice Sample** — pull the most "them" paragraph from the input verbatim
- **Emotional Target** — how they want people to feel

#### audience.md
From the input, extract:
- **Buyer Profile** — who buys, what they struggle with
- **Failed Alternatives** — what buyers tried before
- **Voice of Customer** — buyer's own words for the problem
- **Buying Trigger** — what makes them act
- **Disqualifiers** — who's a bad fit

### 3. Frontmatter

All three files get:
```yaml
---
type: context
status: draft
date: [today]
last-updated: [today + time]
extracted_via: snapshot
source: [filename or "direct input"]
---
```

### 4. Build the Snapshot Document

After writing the three context files, generate a standalone deliverable at:
`outputs/[date]-snapshot.md`

Format:

```markdown
---
type: output
format: snapshot
date: [today]
status: final
---

# Your Snapshot

## Who You Are
[2-3 paragraphs synthesizing soul.md — their identity, beliefs, what makes them different]

## How You Sound
[1-2 paragraphs on their voice — tone, energy, signature phrases, what they'd never say]

## Who You Serve
[2-3 paragraphs on their audience — the buyer, the struggle, the trigger, the bad fit]

---

## What This Means

These three dimensions — identity, voice, and audience — are the foundation of every piece of content, every ad, every proposal your business produces. When they're aligned and explicit, AI can generate outputs that sound like you wrote them. When they're missing, you get generic.

## What's Next

This snapshot is yours to keep. Three ways to use it:

1. **Hand it to any AI tool** — paste these files into ChatGPT, Claude, or any writing tool. Your outputs will immediately improve.
2. **Use it as a briefing document** — give it to a copywriter, marketer, or VA. They'll understand your business in minutes instead of months.
3. **Let it compound** — upgrade to Codify and these files become the seed of a living context engine that gets smarter every week.

---

*Built by Codify — Context Architecture for Senior Executives*
```

### 5. Quality Check

Before marking complete, verify:
- Every section has real content (not just placeholders)
- Client's exact language is preserved — not rewritten into marketing-speak
- Cross-references are added between files (`[[soul]]`, `[[audience]]`, `[[voice]]`)
- The snapshot document reads as a standalone, professional deliverable
- Total snapshot document is 800-1200 words (enough to be valuable, short enough to read in 5 minutes)

### 6. Report

"Your Snapshot is ready. Three files built:
- Soul: [depth level] — [one-line summary]
- Voice: [depth level] — [one-line summary]
- Audience: [depth level] — [one-line summary]

The standalone document is at `outputs/[date]-snapshot.md`.

Sections marked for enrichment: [list or 'none']. These would deepen during a full Codify engagement."
