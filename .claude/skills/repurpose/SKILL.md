---
name: repurpose
description: "Take one output and create versions for every channel — ad, email, post, blog, SMS, newsletter."
---

# /repurpose — One Piece, Every Channel

Takes a single output and adapts it for every distribution channel. One LinkedIn post becomes an ad, an email, a blog intro, and an SMS.

## Usage

```
/repurpose [filename]              → Repurpose into all formats
/repurpose [filename] email,sms    → Repurpose into specific formats
```

## Procedure

### 1. Read Source Output

Read the file from `outputs/`. Identify its core message, proof points, and CTA.

### 2. Read Voice

Read `reference/core/voice.md` to maintain consistency across all versions.

### 3. Generate Versions

From the source content, create:

| Format | Adaptation |
|--------|-----------|
| **Ad copy** | Hook + compressed body + CTA. Under 125 words. |
| **Email** | Subject line + personal opening + value + CTA. Conversational. |
| **LinkedIn post** | Contrarian take format. Short paragraphs. No hard CTA. |
| **X/Twitter thread** | 3-5 tweets. One insight per tweet. Punchy. |
| **Blog post** | Expanded version with subheadings, examples, proof. 800-1200 words. |
| **SMS** | 160 characters. Direct CTA. |
| **Newsletter block** | 2-3 paragraphs that slot into a weekly newsletter. |

### 4. Save All Versions

Save each to `outputs/` with format:
```
outputs/[date]-repurpose-[format]-[slug].md
```

Link all versions to the source file in frontmatter:
```yaml
repurposed_from: outputs/[original-filename].md
```

### 5. Distribute (Optional)

Ask: "Want to publish these now?"
If yes, run `/publish` on each version.
