---
type: decision
status: active
date: <% tp.date.now("YYYY-MM-DD") %>
---

# Decision: <% tp.system.prompt("What did you decide?") %>

## Context
<% tp.system.prompt("What triggered this decision?") %>

## Why
<% tp.system.prompt("Why this over the alternatives?") %>

## Impact
<!-- What Soul files does this affect? Link them: [[soul]], [[audience]], [[offer]], [[voice]] -->

