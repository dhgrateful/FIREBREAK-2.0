# Architect Onboarding Guide

How to onboard a new client with zero friction.

---

## Before the Call (10 min)

1. **Personalize the installer:**
   Open `_architect/install-codify.command` and set:
   - `VAULT_NAME` → client's business name (lowercase, hyphens)
   - `GITHUB_TEMPLATE` → the template repo URL

2. **Send the installer to the client:**
   Email or DM with this message:

   > "Before our call, download this file and double-click it. It takes about 2 minutes and sets everything up. You don't need to do anything else."

   Attach: `install-codify.command`

3. **Set up their GoHighLevel sub-account:**
   - Create a new Location in GHL for this client
   - Note the Location ID (needed for distribution later)
   - See `_architect/CONNECTIONS.md` for details

---

## On the Call (45 min)

### First 5 min — Verify Setup

1. Ask them to open Obsidian — they should see the vault
2. If plugins aren't trusted: "Click 'Enable' on that popup"
3. Have them open the chat pane: `Cmd+P` → "Agent Client: Open Chat"
4. Claude Code connects automatically — wait for the "Connected" indicator
5. Verify you can see the vault files in Obsidian's sidebar
6. If "no upstream branch" popup appears — click the X. You'll fix remotes after the call.

### Minutes 5-10 — Setup and Import

Run `/setup` to personalize their vault. Then offer both paths:

```
/setup              → Personalizes vault, asks name + business name
```

Then either:
```
/import             → "Paste your website About page, a proposal, or any emails"
```
or:
```
/extract soul       → Guided questions if they have nothing to paste
```

**Pro tip:** `/import` is faster and more impressive. If they paste their website copy, Claude fills 3-4 Context files in seconds. The "wow" moment is bigger.

### Minutes 10-40 — Fill Context Files

Goal: get all 4 Context files to "Working" depth.

| Command | What it fills | Time |
|---------|--------------|------|
| `/extract soul` | Core identity — beliefs, origin, framework | ~10 min |
| `/extract audience` | Buyer profile — pain points, triggers, language | ~7 min |
| `/extract offer` | Value prop — transformation, deliverables, guarantee | ~7 min |
| `/extract voice` | Tone — phrases, anti-language, emotional target | ~7 min |

After each extraction, point out the file populating in the sidebar. The visual feedback is the "wow" moment.

### Last 5 min — Tour + Next Steps

1. Open `_dashboards/context-power.md` — show them their vault health
2. Open the Graph View (`Cmd+P` → "Graph View") — show the knowledge connections
3. Explain the compound loop: "Every decision you log, every piece of research — it all feeds into better outputs"
4. Schedule the first Brain Sync (monthly review)

---

## After the Call (15 min)

### 1. Create the client's sovereign vault on GitHub

From your own terminal (not the client's):

```bash
cd [client-vault-path]

# Remove the template origin
git remote remove origin

# Create their private repo and push
gh repo create [client]-sovereign-vault --private --source=. --push --remote=origin
```

**Critical:** This must happen before the client reopens Obsidian, or the Git plugin will show a "no upstream branch" error.

### 2. Set the tier

```bash
echo "pro" > [client-vault-path]/reference/core/.tier
# or "trial" for free trial, "vip" for VIP engagement
```

### 3. Run first generation

From your Claude Code (with MCP servers configured):

```
/ad                → Show them what their context produces
/content linkedin  → LinkedIn post from their Context files
```

Send them the outputs. This proves the system works.

### 4. Run first audit

```
/audit
```

Share the report. Identify enrichment opportunities for the next session.

### 5. Set up distribution (VIP tier only)

See `_architect/CONNECTIONS.md` for full details. Key steps:
- Ensure GHL sub-account is created with client's branding
- Test `/publish` with a draft email to verify connections
- Configure social accounts in GHL for the client's channels

---

## Skill Reference (All Tiers)

### Client-Facing Skills

| Skill | Tier | What it does |
|-------|------|-------------|
| `/start` | All | Welcome screen, shows available skills |
| `/extract` | All | Context Extraction — guided questions → Context files |
| `/import` | All | Mine existing docs (proposals, emails, website) → Context files |
| `/ad` | Pro+ | Generate ad copy (Meta/Facebook/Instagram) |
| `/email` | Pro+ | Generate email sequences (cold, warm, nurture) |
| `/content` | Pro+ | Generate content for any platform (LinkedIn, blog, newsletter, X/Twitter, Instagram) |
| `/proposal` | Pro+ | Generate client proposal |
| `/landing` | Pro+ | Generate landing page copy |
| `/enrich` | Pro+ | Deepen thin Context files with follow-ups |
| `/audit` | All | Vault health check |
| `/research` | Pro+ | Research prospects, competitors, market trends, and scan for opportunities |
| `/brief` | VIP | Morning brief — overnight activity, vault health |

### Architect-Only Skills (Internal)

| Skill | What it does |
|-------|-------------|
| `/update` | Pull latest Codify skills from template repo |
| `/gate` | Check/set tier gating |
| `/publish` | Push outputs to live channels (email, social, blog) |
| `/campaign` | Full pipeline — generate all assets + distribute |
| `/repurpose` | Take one output, create versions for every channel |

### Distribution Skills → MCP Connections

| Skill action | MCP tool | Platform |
|-------------|----------|----------|
| Send email | `mcp__gmail__send_email` | Gmail |
| Draft email | `mcp__gmail__draft_email` | Gmail |
| Social post | `mcp__gohighlevel__create_social_post` | LinkedIn, FB, IG via GHL |
| Blog post | `mcp__gohighlevel__create_blog_post` | GHL Blog |
| SMS | `mcp__gohighlevel__send_sms` | GHL |
| Email campaign | `mcp__gohighlevel__send_email` | GHL |

---

## The Client's Ongoing Experience

| Action | How | When |
|--------|-----|------|
| Browse files | Open Obsidian | Anytime |
| Chat with AI | Agent Client chat pane | Anytime |
| Check dashboards | Open `_dashboards/context-power.md` | Weekly |
| Add a daily note | Create file in `content/` | Daily (optional) |
| Log a decision | Create file in `decisions/` | As needed |
| Import new docs | `/import` in chat pane | As needed |
| Get AI outputs | `/ad`, `/email`, `/content`, `/proposal`, `/landing` in chat or book architect session | As needed |
| Deepen Context files | `/enrich` in chat or architect runs it | Monthly |
| Vault health review | Brain Sync session — architect runs `/audit` | Monthly |

---

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Installer won't run | Right-click → Open → "Open anyway" (macOS Gatekeeper) |
| Homebrew install hangs | Client may need to enter their Mac password |
| Claude Code not found | Run `npm install -g @anthropic-ai/claude-code @zed-industries/claude-agent-acp` in terminal |
| Agent Client stuck on "Connecting..." | Check Settings → Agent Client → Command is `/opt/homebrew/bin/claude-agent-acp` |
| "No upstream branch" popup on boot | Client's vault has no `origin` remote — architect must create GitHub repo first |
| Obsidian Git not syncing | Verify `origin` remote is set: `git remote -v` in vault directory |
| `/publish` fails | MCP servers not configured — check architect's `~/.claude.json`. See `CONNECTIONS.md` |
| GHL post fails | Verify Location ID and API key in MCP config |
| Client sees git commands | Skill is architect-only. Client skills should never run shell commands |
| Client added files in wrong folder | Move them during Brain Sync — no harm done |
| Client is overwhelmed | "Just open Obsidian and browse. I handle the rest." |
