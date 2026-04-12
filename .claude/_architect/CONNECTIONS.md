# Architect Connection Guide

How the distribution skills (`/publish`, `/campaign`, `/repurpose`) connect to live channels. All connections run through the **architect's** Claude Code environment — the client never configures any of this.

---

## Architecture

```
                         THE CODIFY COMPOUND LOOP

     EXTRACT                COMPOUND                 GENERATE
    ─────────              ──────────               ──────────
    Client talks    ──>    Context files    ──>     Ads, emails,
    /extract               grow + link              proposals, content
    /import                /enrich adds              that sound like
    /research              cross-references          the client wrote them


    ┌───────────┐       ┌──────────────┐       ┌──────────────┐
    │  OBSIDIAN │       │  SOVEREIGN   │       │  DISTRIBUTE  │
    │  (Client) │──────>│  VAULT       │──────>│  (Architect)  │
    │           │       │  (GitHub /   │       │              │
    │  View     │       │   Forgejo)   │       │  Gmail       │
    │  files    │       │              │       │  GoHighLevel │
    │  Answer   │       │  Context/    │       │  Social      │
    │  questions│       │  Decisions/  │       │  Blog        │
    │           │<──────│  Research/   │       │  SMS         │
    │  See      │  sync │  Outputs/    │       │              │
    │  results  │       │              │       └──────────────┘
    └───────────┘       └──────┬───────┘
                               │ ▲
                               │ │  new research + cross-references
                               │ │  written back to vault
                               │ │
                               ▼ │
                        ┌──────────────┐       ┌──────────────┐
                        │  OPENCLAW    │──────>│  TELEGRAM    │
                        │  (Private    │       │  (Mobile)    │
                        │   Server)    │       │              │
                        │              │       │  5:30 AM     │
                        │  2 AM deep   │       │  Morning     │
                        │  research    │       │  brief on    │
                        │              │       │  your phone  │
                        │  Competitor  │       │              │
                        │  monitoring  │       │  Approve /   │
                        │              │       │  reject      │
                        │  Cross-ref   │       │  content     │
                        │  new research│       │              │
                        │  against     │       │  Voice note  │
                        │  Context/    │───────│──> captured  │
                        │              │  ◄────│  as research │
                        │  Update      │       │              │
                        │  [[links]]   │       └──────────────┘
                        └──────────────┘

    ──────────────────────────────────────────────────────

    THE CLOSED LOOP:

    You talk  ──>  Context files grow  ──>  Better outputs
       ▲                                        │
       │           Overnight engine             │
       └───────  enriches + links  ◄────────────┘

    Every output, every research file, every decision
    feeds back into the vault. The vault gets smarter.
    Tomorrow's outputs are better than today's.

    Week 1    4 context files. Basic outputs.
    Month 3   40+ files. Outputs use your exact language.
    Year 1    Digital twin. The vault knows your business
              better than any consultant ever could.
```

The client creates context. The architect distributes it. OpenClaw compounds it overnight. The client never touches a third-party tool.

---

## MCP Servers Required

These must be configured in the **architect's** `~/.claude.json` — NOT in the client's vault.

### 1. Gmail

Sends emails directly from the architect's Gmail (or client's, if configured).

```json
"gmail": {
  "type": "stdio",
  "command": "node",
  "args": ["/opt/homebrew/lib/node_modules/@gongrzhe/server-gmail-autoauth-mcp/dist/index.js"],
  "env": {
    "GMAIL_OAUTH_PATH": "/path/to/.gmail-mcp/gcp-oauth.keys.json",
    "GMAIL_CREDENTIALS_PATH": "/path/to/.gmail-mcp/credentials.json"
  }
}
```

**Setup:** `npm install -g @gongrzhe/server-gmail-autoauth-mcp` then follow OAuth flow.

**Skills that use it:** `/publish email`, `/campaign`

### 2. GoHighLevel

Manages social posts, email campaigns, SMS, blog posts, contacts, and workflows.

```json
"gohighlevel": {
  "type": "stdio",
  "command": "node",
  "args": ["/path/to/GoHighLevel-MCP/dist/server.js"],
  "env": {
    "GHL_API_KEY": "your-api-key",
    "GHL_LOCATION_ID": "your-location-id"
  }
}
```

**Setup:** Clone GoHighLevel-MCP repo, build, add API key from GHL settings.

**Skills that use it:**
| Skill | GHL Tools Used |
|-------|---------------|
| `/publish social` | `create_social_post` |
| `/publish blog` | `create_blog_post` |
| `/publish sms` | `send_sms` |
| `/campaign` | `create_social_post`, `send_email`, `create_blog_post` |
| `/repurpose` | All of the above |

### 3. YouTube Transcript (Research)

Pulls transcripts from YouTube for `/research` and research.

```json
"youtube-transcript": {
  "type": "stdio",
  "command": "npx",
  "args": ["-y", "@kimtaeyoon83/mcp-server-youtube-transcript"]
}
```

### 4. Gemini (Research + Images)

Deep research, image generation, document analysis.

```json
"gemini": {
  "type": "stdio",
  "command": "env",
  "args": ["GEMINI_API_KEY=your-key", "npx", "-y", "@rlabs-inc/gemini-mcp"]
}
```

---

## OpenClaw — The Always-On Engine

OpenClaw runs on a **private server** (VPS — Hetzner, DigitalOcean, or equivalent), executing scheduled jobs against all client vaults from one machine. The client never installs or configures OpenClaw — it's part of the architect's infrastructure, shared across all clients. It connects to Telegram for delivery and approvals.

### Telegram Bot: `@Codify_build_bot`

Supergroup with 4 topic channels:

| Topic | What gets sent | Skills that feed it |
|-------|---------------|-------------------|
| **Ops** | Morning briefs, repo health, staleness alerts | `/brief` |
| **Research** | Overnight findings, positioning audits | `/research` |
| **Content** | Draft review, approval loop, posting confirmation | `/campaign`, `/repurpose` |
| **General** | Quick questions, idea capture, routing | Ad hoc |

### Scheduled Jobs

| Job | Schedule | What it does |
|-----|----------|-------------|
| Morning Brief | 5:30 AM daily | Overnight research summary, vault health, open tasks, competitor signals → Telegram Ops |
| Deep Research | 2:00 AM daily | Runs `/research` against market signals, saves to `research/` |
| Content Queue | Every 5 min | Polls codify.build platform for pending content, sends to Telegram Content for approval |
| Competitor Monitor | Weekly | Tracks competitor moves, sends alerts to Telegram Research |
| Staleness Check | Daily | Flags Context files not updated in 14+ days → Telegram Ops |
| Vault Backup | Hourly | Git pull/push across all client vaults |

### How Approval Works (from Phone)

1. OpenClaw generates a draft and sends it to Telegram Content topic
2. Architect sees it on their phone
3. Reply `approve <id>` → OpenClaw publishes via GHL/Gmail
4. Reply `reject <id>` → OpenClaw archives the draft
5. Reply with feedback → OpenClaw revises and re-sends

### OpenClaw Setup Per Client

```bash
# Add a client workspace to OpenClaw
openclaw workspace create [client-name] \
  --vault-path ~/vaults/[client]-sovereign-vault \
  --telegram-topic [topic-id]

# Add morning brief cron
openclaw workspace [client-name] cron add "morning-brief" \
  --schedule "30 5 * * *"

# Add overnight research cron
openclaw workspace [client-name] cron add "deep-research" \
  --schedule "0 2 * * *"
```

### Environment Variables

```bash
# Telegram
TELEGRAM_BOT_TOKEN=your-bot-token
TELEGRAM_SUPERGROUP_ID=your-group-id
TELEGRAM_OPS_TOPIC_ID=topic-id
TELEGRAM_RESEARCH_TOPIC_ID=topic-id
TELEGRAM_CONTENT_TOPIC_ID=topic-id

# OpenRouter (model routing)
OPENROUTER_API_KEY=your-key

# Codify Platform Bridge
CODIFY_API_URL=https://codify.build
CODIFY_API_KEY=shared-secret
CODIFY_USER_ID=supabase-user-uuid
```

---

## Per-Client vs. Shared

| Connection | Shared (architect) | Per-client |
|-----------|-------------------|------------|
| GoHighLevel | One GHL account, multiple sub-accounts (locations) per client | Each client gets their own GHL Location ID |
| Gmail | Architect's Gmail for DFY sends | Client's Gmail if they want sends from their address |
| Telegram | One bot, one supergroup | Per-client topic threads within the supergroup |
| OpenClaw | One private server (VPS), all clients | Per-client workspace + cron jobs on architect's machine |
| YouTube | Shared | Shared |
| Gemini | Shared | Shared |

### Setting Up a New Client's GHL Sub-Account

1. In GoHighLevel, create a new Sub-Account (Location) for the client
2. Note the Location ID
3. When running distribution for that client, update the `GHL_LOCATION_ID` env var
4. Or maintain a lookup file mapping client → location ID

---

## How the Architect Runs Distribution

The architect does NOT run distribution from the client's Obsidian. They:

1. Pull the client's vault to their own machine (git pull)
2. Open it in their own Claude Code (with MCP servers configured)
3. Run `/publish`, `/campaign`, `/repurpose`
4. Outputs go live through the architect's MCP connections
5. Push the updated vault back (distribution logs in frontmatter)

The client sees the results in their `outputs/` folder — with `published:` metadata showing where it went.

---

## Future Connections

| Platform | Status | How |
|----------|--------|-----|
| Substack | Planned | MCP server or API |
| Beehiiv | Planned | MCP server or API |
| LinkedIn direct | Planned | LinkedIn API (currently via GHL) |
| Stripe | Planned | Payment tracking in vault |
| Calendly | Planned | Booking links in campaigns |
| Slack | Available | Claude Code Slack integration |
| WhatsApp | Planned | GHL or Twilio integration |
| Podcast feed | Planned | RSS generation from vault content |
