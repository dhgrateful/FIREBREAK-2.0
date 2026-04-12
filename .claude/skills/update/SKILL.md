---
name: update
description: "Architect-only skill. Pull the latest Codify skills and system files. Run during Brain Sync sessions, not by the client."
---

# /update — System Update (Architect Only)

This skill is for the **architect** to run during Brain Sync sessions. The client should never run this directly — they'll see technical output that doesn't make sense to them.

## When to Run

- During monthly Brain Sync calls
- After releasing new skills or dashboard updates
- Before onboarding a client on a new tier

## Procedure

### 1. Check for Upstream Remote

```bash
git remote get-url upstream 2>/dev/null || git remote add upstream https://github.com/mike-scott-darwin/codify-vault-template.git
```

### 2. Fetch and Apply Updates

```bash
git fetch upstream main --quiet
```

Pull only system files — never touch client data:

```bash
# Update skills
git checkout upstream/main -- .claude/skills/

# Update dashboards
git checkout upstream/main -- _dashboards/

# Update templates
git checkout upstream/main -- _templates/ 2>/dev/null || true

# Update system config
git checkout upstream/main -- CLAUDE.md

# Update plugin configs
git checkout upstream/main -- .obsidian/community-plugins.json 2>/dev/null || true
```

### 3. Commit and Sync

```bash
git add -A
git diff --cached --quiet || git commit -m "[update] Codify system update — $(date +%Y-%m-%d)"
git push origin main --quiet 2>/dev/null || true
```

### 4. Report

Say: "System updated. New skills and dashboards are live."

If nothing changed: "Already on the latest version."

## What Gets Updated vs. What's Protected

| Updated (Codify system) | Protected (client data) |
|------------------------|------------------------|
| `.claude/skills/` | `reference/core/` |
| `_dashboards/` | `decisions/` |
| `_templates/` | `research/` |
| `CLAUDE.md` | `outputs/` |
| `.obsidian/plugins/` | `content/` |

## Error Handling

| Situation | Action |
|-----------|--------|
| No internet | Say "Can't reach the update server. We'll try next session." |
| Upstream not accessible | Say "Update channel isn't configured yet. I'll set it up." Then add the remote. |
| Merge conflict | Keep the client's version. Investigate manually. |
