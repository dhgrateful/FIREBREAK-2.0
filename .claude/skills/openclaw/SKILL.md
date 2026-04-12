---
name: openclaw
description: "Architect-only. Set up OpenClaw autonomous operations for a Focus tier client. One command, 3 inputs."
---

# /openclaw — Set Up Autonomous Operations

Architect-only skill. Connects a Focus tier client's vault to OpenClaw for overnight research, morning briefs, content queue, and automated backups.

**Prerequisites:** OpenClaw must already be running on the architect's machine (M1 Mac Mini or VPS).

## Usage

```
/openclaw setup              → Set up a new client
/openclaw status [client]    → Check a client's jobs
/openclaw pause [client]     → Pause all jobs for a client
/openclaw resume [client]    → Resume paused jobs
```

## Setup Procedure

### 1. Gather 3 Inputs

Ask:
1. **"Client name?"** → Used for workspace name (lowercase, hyphens)
2. **"Vault repo URL?"** → The client's GitHub sovereign vault URL
3. **"Client's Telegram username?"** → To add them to the Telegram group (optional — architect can manage solo)

### 2. Create Workspace

```bash
# Clone the client's vault to the OpenClaw machine
git clone [vault-repo-url] ~/vaults/[client-name]-sovereign-vault

# Create OpenClaw workspace
openclaw workspace create [client-name] \
  --vault-path ~/vaults/[client-name]-sovereign-vault
```

### 3. Create Telegram Topic

```bash
# Create a topic thread in the Codify supergroup for this client
# (Telegram Bot API — create_forum_topic)
curl -s -X POST "https://api.telegram.org/bot$TELEGRAM_BOT_TOKEN/createForumTopic" \
  -d "chat_id=$TELEGRAM_SUPERGROUP_ID" \
  -d "name=[Client Name] — Ops" \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['result']['message_thread_id'])"
```

Save the topic ID for cron job configuration.

### 4. Add Standard Cron Jobs

```bash
# Morning brief — 5:30 AM daily
openclaw workspace [client-name] cron add "morning-brief" \
  --schedule "30 5 * * *" \
  --telegram-topic [topic-id]

# Overnight research — 2:00 AM daily
openclaw workspace [client-name] cron add "deep-research" \
  --schedule "0 2 * * *"

# Vault backup — every hour
openclaw workspace [client-name] cron add "vault-sync" \
  --schedule "0 * * * *"

# Staleness check — 6:00 AM daily
openclaw workspace [client-name] cron add "staleness-check" \
  --schedule "0 6 * * *" \
  --telegram-topic [topic-id]

# Competitor monitor — Monday 3:00 AM
openclaw workspace [client-name] cron add "competitor-scan" \
  --schedule "0 3 * * 1"
```

### 5. Test

```bash
# Run a test morning brief
openclaw workspace [client-name] run morning-brief

# Verify Telegram delivery
# Should appear in the client's topic thread
```

### 6. Confirm

Say: "OpenClaw is live for [client name]. They'll get their first morning brief tomorrow at 5:30 AM."

## What Gets Created

| Component | Details |
|-----------|---------|
| Workspace | `~/vaults/[client]-sovereign-vault` on OpenClaw machine |
| Cron jobs | 5 jobs: brief, research, sync, staleness, competitor |
| Telegram | New topic thread in Codify supergroup |
| Git sync | Hourly pull/push against client's sovereign vault |

## Cost Per Client

| Item | Cost |
|------|------|
| VPS overhead | ~$1/mo per client (shared $4/mo VPS) |
| API calls (overnight research) | ~$0.50/day (cheap model tier) |
| Telegram | Free |
| **Total** | **~$15-20/mo per client** |

Covered by the Focus tier fee ($1,497 + $497/mo). Margin is strong.

## Troubleshooting

| Problem | Fix |
|---------|-----|
| Cron not firing | `openclaw workspace [client] cron list` — check schedule |
| Telegram not delivering | Verify bot token and topic ID |
| Git sync fails | Check SSH key / GitHub auth on OpenClaw machine |
| Brief is empty | Vault has no recent activity — normal for new clients |
| Research job times out | Check model routing — use cheap tier (Gemini Flash) |
