---
type: dashboard
---

# Context Power

Your business brain at a glance. The more complete your Context files, the better your outputs.

---

## Your Context Files

```dataview
TABLE
  choice(status = "compounding", "Deep", choice(status = "active", "Solid", choice(status = "draft", "Getting there", "Empty"))) as "Depth",
  choice(length(file.outlinks) > 2, "Connected", choice(length(file.outlinks) > 0, "Some links", "No links yet")) as "Connections",
  last-updated as "Last Updated"
FROM "reference/core"
SORT file.name ASC
```

### What to do next
- **Empty** — Run `/extract` to fill it in
- **Getting there** — Run `/enrich` to go deeper
- **Solid** — Enriched but needs cross-references to other files
- **Deep** — Rich, linked, compounding. This is your competitive edge.

---

## Recent Decisions

```dataview
TABLE
  last-updated as "Last Updated",
  status as "Status"
FROM "decisions"
SORT date DESC
LIMIT 5
```

---

## Recent Outputs

```dataview
TABLE
  format as "Type",
  last-updated as "Last Updated"
FROM "outputs"
SORT date DESC
LIMIT 5
```

---

## Needs Attention

Files not updated in 14+ days:

```dataview
LIST
FROM "reference/core" OR "decisions"
WHERE date(now) - file.mtime > dur(14 days)
SORT file.mtime ASC
```

---

## Your Vault at a Glance

| What | Count |
|------|-------|
| Context files | `$= dv.pages('"reference/core"').length` |
| Decisions | `$= dv.pages('"decisions"').length` |
| Research | `$= dv.pages('"research"').length` |
| Outputs | `$= dv.pages('"outputs"').length` |
| Daily notes | `$= dv.pages('"content"').length` |

> More files = more connections. More connections = better outputs. That's how your vault gets smarter over time.
