---
name: audit
description: "Check vault health — stale files, orphaned notes, missing cross-references, and context gaps."
---

# /audit — Vault Health Check

Scans your entire vault and reports on context health. Identifies what needs attention so your AI outputs stay sharp.

## Usage

```
/audit               → Full vault audit
/audit context       → Audit Context files only
/audit stale         → Show files not updated in 14+ days
/audit orphans       → Show files with no cross-references
```

## Procedure

### 1. Scan All Files

Read every file in:
- `reference/core/` — Core identity
- `decisions/` — Strategic decisions
- `research/` — Market intelligence
- `outputs/` — Generated content
- `content/` — Daily logs

### 2. Assess Each Dimension

**Depth Score (per file) — read from `status` in frontmatter:**
- Empty — no status or template only
- Getting there — `status: draft` (extracted, not yet enriched)
- Solid — `status: active` (enriched at least once)
- Deep — `status: compounding` (enriched + cross-referenced)

**Freshness Score:**
- Fresh: updated within 7 days
- Current: updated within 14 days
- Stale: not updated in 14-30 days
- Overdue: not updated in 30+ days

**Connection Score:**
- Count `[[links]]` in and out
- Flag files with zero connections (orphans)
- Flag Context files that reference each other (good)

**Completeness Score:**
- Check each Context file for empty sections (marked with `<!-- -->` comments)
- Calculate percentage of sections filled

### 3. Generate Report

Output a structured report:

```
## Vault Audit — [date]

### Overall Context Power: [score]/100

### Context Files
| File | Depth | Freshness | Connections | Completeness |
|------|-------|-----------|-------------|--------------|
| soul.md | Working | Fresh | 3 in / 2 out | 85% |
| audience.md | Draft | Stale | 0 in / 1 out | 40% |
| ... | ... | ... | ... | ... |

### Action Items (Priority Order)
1. [Most impactful enrichment opportunity]
2. [Second priority]
3. [Third priority]

### Compound Score Trend
- Total vault files: [n]
- Total cross-references: [n]
- Files at Working+ depth: [n/total]
- Decisions logged this month: [n]
```

### 4. Save Report

Write to `outputs/[date]-vault-audit.md` for historical tracking.
