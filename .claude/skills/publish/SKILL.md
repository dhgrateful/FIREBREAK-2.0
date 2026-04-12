---
name: publish
description: "Push generated outputs to live channels — email, social, blog, newsletter. The last mile from context to revenue."
---

# /publish — Distribute Your Outputs

Takes content from `outputs/` and pushes it to live channels. This is the skill that turns reference files into revenue.

## Usage

```
/publish                    → Show recent outputs, ask where to send
/publish [filename]         → Publish a specific output
/publish [filename] email   → Send as email
/publish [filename] social  → Post to social channels
/publish [filename] blog    → Publish as blog post
/publish [filename] all     → Distribute to all channels
```

## Procedure

### 1. Select Output

If no filename specified, list the 5 most recent files in `outputs/`:
```
Recent outputs ready to publish:
1. 2026-03-25-ad-copy-spring-campaign.md
2. 2026-03-24-linkedin-post-context-engineering.md
3. 2026-03-23-email-sequence-onboarding.md

Which one? (or type a filename)
```

### 2. Read the Output

Read the selected file. Check its `format` frontmatter to determine the best channels:

| Format | Default channels |
|--------|-----------------|
| ad | GoHighLevel social post |
| email | Gmail or GoHighLevel email |
| post | GoHighLevel social (LinkedIn, Facebook) |
| newsletter | GoHighLevel email campaign |
| blog | GoHighLevel blog post |
| proposal | Gmail direct send |
| landing | Suggest manual — provide copy for their landing page builder |
| vsl | Suggest manual — provide script for video recording |

### 3. Confirm Before Sending

ALWAYS confirm before publishing. Show:
- The content that will be sent
- The channel(s) it will go to
- The recipient(s) or audience

"Ready to publish this to [channel]. Here's what will go out:

[preview]

Send it? (yes/no)"

### 4. Distribute

Use the appropriate MCP tool:

**Email (Gmail):**
- Use `mcp__gmail__send_email` for direct sends
- Use `mcp__gmail__draft_email` if they want to review first

**Email (GoHighLevel):**
- Use `mcp__gohighlevel__send_email` for campaign emails

**Social (GoHighLevel):**
- Use `mcp__gohighlevel__create_social_post` for LinkedIn, Facebook, Instagram

**Blog (GoHighLevel):**
- Use `mcp__gohighlevel__create_blog_post`

**SMS (GoHighLevel):**
- Use `mcp__gohighlevel__send_sms` for text-based outreach

### 5. Log the Distribution

After publishing, update the output file's frontmatter:

```yaml
published:
  - channel: linkedin
    date: 2026-03-25
  - channel: email
    date: 2026-03-25
```

This prevents duplicate sends and tracks what went where.

### 6. Report

"Published to [channels]. Your [output type] is live."
