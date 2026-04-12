---
name: setup
description: "Personalize a new client's vault and start their first extraction. Conversational — the client just answers questions."
---

# /setup — Personalize Your Context Architecture

The client already has the vault open in Obsidian. The folder structure, plugins, and skills are all in place. This skill personalizes the vault for their business and kicks off their first Context Extraction session.

## Procedure

### 1. Welcome and Gather Info

Say:
"Welcome to Codify. I'm going to set up your Context Architecture — a secure vault for your expertise that compounds over time. The more you put in, the sharper everything that comes out. I just need a couple of things to get started."

Ask these one at a time:

1. **"What's your business name?"**
   → Store for personalizing files

2. **"What's your name?"**
   → Store for personalizing files

### 2. Personalize the Vault

Do this silently — no need to narrate each step.

1. Update `CLAUDE.md` — replace any placeholder references with the client's business name
2. Update `README.md` — personalize with client name and business name
3. Update the vault link in `README.md` — detect the `origin` remote URL and replace `GITHUB_USERNAME/VAULT_REPO_NAME` with the actual repo path. If no `origin` remote exists yet, leave the placeholder (architect sets it post-call).
4. Write the tier file:
   ```bash
   echo "explore" > reference/core/.tier
   echo "0" > reference/core/.extractions
   ```
5. Update frontmatter dates in Context files to today's date
6. Set up the update channel (silently — client never sees this):
   ```bash
   git remote get-url upstream 2>/dev/null || git remote add upstream https://github.com/mike-scott-darwin/codify-vault-template.git
   ```

Say: "Your vault is ready. Everything you see in the sidebar is yours — it's where your expertise will live and compound."

### 3. Quick Tour (30 seconds)

Say:
"Here's what you're looking at:

- **Context** — Your core identity. What you believe, who you serve, how you sound. We're about to fill these in.
- **Decisions** — Every strategic choice you make and the reasoning behind it.
- **Research** — Market intelligence, competitor data, industry signals.
- **Outputs** — Everything the system generates for you — ads, emails, proposals, campaigns.
- **Dashboards** — Open 'Context Power' anytime to see your vault health.

Everything backs up automatically to your secure vault. You don't need to think about it."

### 4. Start First Extraction

Say: "Let's start capturing your expertise. I'm going to ask you some questions about your business — your beliefs, your audience, what you sell, and how you communicate. Just talk naturally. There are no wrong answers — I'm capturing your judgment, not testing it."

Then immediately run `/extract soul`.

## Tone

- **Respectful of their expertise.** This person has 30 years of domain knowledge. Don't talk down to them.
- **Confident.** "Your vault is ready" not "I'm going to try to set up..."
- **Efficient.** They're busy. Don't over-explain the architecture. They need to see their files, not understand the plumbing.
- **Legacy-minded.** Frame everything as protecting and scaling their expertise: "This captures your judgment so it compounds over time."
- **Zero jargon.** No "repo," "git," "commit," "push," "CLI," "API," "terminal," "MCP."

## Error Handling

| Situation | What to say |
|-----------|------------|
| Context files missing | Recreate them silently from the template structure, then continue. |
| Client gets confused | "No worries. I'm handling the setup. You just answer the questions — that's where the value comes from." |
| Client asks about backups | "Everything backs up automatically to a secure vault that only you can access." |
| Client asks how it works | "Think of it as a reference library of your expertise. The AI reads it before creating anything, so everything it produces sounds like you, not a chatbot." |

## What the Client Walks Away With

After 15 minutes:
- Vault personalized with their business name
- First Context file populated from the extraction conversation
- Backup running silently in the background
- All skills available via the chat pane
- Dashboards showing their vault health
