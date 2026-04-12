---
type: dashboard
---

# Reference Health

How deep is your context? Deeper files = better outputs.

---

## Context File Strength

```dataview
TABLE
  choice(status = "compounding", "Deep", choice(status = "active", "Solid", choice(status = "draft", "Getting there", "Empty"))) as "Depth",
  length(file.outlinks) as "Links out",
  length(file.inlinks) as "Links in",
  last-updated as "Last Updated"
FROM "reference/core"
SORT status ASC
```

### What the levels mean
- **Empty** — Template only. Run `/extract` to fill it in.
- **Getting there** — First extraction done. Run `/enrich` to go deeper.
- **Solid** — Enriched with follow-up material. Add cross-references to reach Deep.
- **Deep** — Rich, linked, actively maintained. This is your competitive edge.

### How files level up
1. `/extract` moves a file from Empty → Getting there (status: draft)
2. `/enrich` moves it from Getting there → Solid (status: active)
3. Cross-references + continued enrichment → Deep (status: compounding)

---

## Most Connected Files

Your best-linked files — these make your outputs strongest:

```dataview
TABLE
  length(file.outlinks) + length(file.inlinks) as "Total Connections",
  last-updated as "Last Updated"
FROM "reference/core" OR "decisions" OR "research"
WHERE length(file.outlinks) + length(file.inlinks) > 0
SORT (length(file.outlinks) + length(file.inlinks)) DESC
LIMIT 10
```

---

## Ready to Generate?

When your Context files reach "Solid" depth, your outputs will be sharp and specific. Until then, keep enriching with `/enrich` or import more material with `/import`.
