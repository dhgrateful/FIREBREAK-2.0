---
name: enrich
description: "Deepen a Context file by asking follow-up questions based on what's already there. Moves files from Draft to Compounding."
---

# /enrich — Deepen Your Reference Files

Reads an existing Context file and asks targeted follow-up questions to move it from Draft → Working → Compounding depth.

## Usage

```
/enrich              → Check all files, suggest which to enrich
/enrich soul         → Deepen soul.md
/enrich audience     → Deepen audience.md
/enrich offer        → Deepen offer.md
/enrich voice        → Deepen voice.md
```

## Procedure

### 1. Read the Target File

Read the file in `reference/core/`. Assess current depth:
- Count sections with content vs. empty sections
- Check for cross-references (`[[links]]`)
- Measure specificity (vague vs. concrete)

### 2. Identify Gaps

Compare what's there against what's possible:

**Soul gaps:**
- Missing specific examples or stories?
- Anti-positions stated but not explained?
- Framework named but not broken down into steps?

**Audience gaps:**
- Buyer described generically? Need a specific person.
- Voice of customer missing exact quotes?
- Buying trigger vague? Need the specific moment.

**Offer gaps:**
- Transformation described in outcomes but not timeline?
- Delivery mechanics unclear? What happens week by week?
- Guarantee missing or weak?

**Voice gaps:**
- Signature phrases listed but no context for when they use them?
- Anti-language listed but no examples of what they'd say instead?
- No voice sample provided?

### 3. Ask Follow-Up Questions

Ask 2-3 targeted questions based on the gaps. Not the original extraction questions — deeper ones:

Examples:
- "You mentioned [framework]. Walk me through the last time you used it with a client. What happened step by step?"
- "You said you'd never [anti-position]. Has someone ever tried to get you to? What happened?"
- "You described your buyer as [profile]. What's the thing they're most afraid of that they'd never admit in public?"

### 4. Update the File

Weave new answers into the existing file. Don't overwrite — add depth to existing sections or create new subsections.

### 4b. REQUIRED — Add Cross-References

**Every Context file MUST link to at least 2 other Context files.** This is not optional — it drives the knowledge graph.

After weaving in the new content, scan the file for natural connection points and add `[[links]]`:

- Soul mentions how buyers struggle → add `[[audience]]` or `[[audience#Voice of Customer]]`
- Soul mentions the transformation → add `[[offer]]` or `[[offer#Transformation]]`
- Soul mentions tone or communication style → add `[[voice]]`
- Audience mentions the offer or guarantee → add `[[offer]]`
- Offer mentions who it's for → add `[[audience]]`
- Voice mentions beliefs → add `[[soul#Contrarian Belief]]`

If a file currently has **zero outgoing links**, this is your top priority. Add at least 2 before moving on.

### 5. REQUIRED — Update Frontmatter

**You MUST update the frontmatter every time you enrich a file. This drives the dashboards.**

1. Change `last-updated` to the current date and time (e.g. `last-updated: 2026-03-26 14:30`)
2. Change `status` based on what you added:
   - After enrichment with new depth → set `status: active`
   - After adding `[[cross-references]]` to other files → set `status: compounding`

Example — before:
```yaml
status: draft
last-updated: 2026-03-26 14:00
```

After enrichment:
```yaml
status: active
last-updated: 2026-03-26 16:45
```

**If you skip this step, the dashboards won't reflect the enrichment.**

### 6. Report Progress

"Your [file] moved from [old depth] to [new depth]. Next enrichment opportunity: [specific suggestion]."
