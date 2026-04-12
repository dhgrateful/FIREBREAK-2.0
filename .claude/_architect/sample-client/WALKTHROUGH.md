# Full Walkthrough: Marcus Webb — Webb Strategic Advisory

A complete test run using a realistic sample client. Use this to verify every skill works end-to-end.

---

## The Client

**Marcus Webb** — 30 years in operations consulting. Helps mid-market manufacturing CEOs ($15-40M) fix operational inefficiency. Known for his "Operational Gravity Map" framework. Charges premium rates. Allergic to bullshit.

This is exactly the Codify ideal client: deep expertise, strong opinions, institutional knowledge that exists nowhere but in his head.

---

## Step-by-Step Test

### 1. Open Obsidian → Agent Client Chat

Open `Cmd+P` → "Agent Client: Open Chat"

### 2. Run /setup

Type: `/setup`

When asked:
- **Business name:** `Webb Strategic Advisory`
- **Your name:** `Marcus Webb`

Verify:
- [ ] README.md updated with business name
- [ ] CLAUDE.md updated
- [ ] `.tier` file created in `reference/core/`
- [ ] Immediately starts `/extract soul`

### 3. Run /extract soul

Answer each question by pasting from `soul-input.md`. 7 questions:

1. Paste the "dinner party" answer
2. Paste the "contrarian belief" answer
3. Paste the "origin moment" answer
4. Paste the "anti-positions" answer
5. Paste the "institutional knowledge" answer
6. Paste the "proprietary framework" answer
7. Paste the "external perception" answer

Verify:
- [ ] `reference/core/soul.md` populated with all 7 sections
- [ ] Client's exact language preserved (not rewritten)
- [ ] Cross-references added where relevant
- [ ] Depth score reported

### 4. Run /extract audience

Type: `/extract audience`

Paste answers from `audience-input.md`. 5 questions.

Verify:
- [ ] `reference/core/audience.md` populated
- [ ] "Dave Chen" story preserved in client's voice
- [ ] Cross-references to `[[soul]]` and `[[offer]]` added

### 5. Run /extract offer

Type: `/extract offer`

Paste answers from `offer-input.md`. 5 questions.

Verify:
- [ ] `reference/core/offer.md` populated
- [ ] "$500K guarantee" captured exactly
- [ ] "Operational Gravity Map" linked to soul.md

### 6. Run /extract voice

Type: `/extract voice`

Paste answers from `voice-input.md`. 5 questions.

Verify:
- [ ] `reference/core/voice.md` populated
- [ ] Anti-language list captured ("synergy", "leverage", etc.)
- [ ] Email sample preserved verbatim

### 7. Check Dashboards

Open `_dashboards/context-power.md`:
- [ ] All 4 Context files show "Strong" depth
- [ ] No staleness alerts
- [ ] Vault count shows files

### 8. Run /audit

Type: `/audit`

Verify:
- [ ] Reports vault health
- [ ] Shows depth per file
- [ ] Suggests enrichment opportunities

### 9. Generate Outputs

Type: `/ad`

Verify:
- [ ] Ad copy sounds like Marcus (direct, specific, no fluff)
- [ ] References his Operational Gravity Map
- [ ] Uses his language ("decision bottleneck", "the spreadsheet is lying")
- [ ] Saved to `outputs/`

Type: `/content linkedin`

Verify:
- [ ] LinkedIn post sounds like Marcus, not a chatbot
- [ ] Short paragraphs, white space
- [ ] Contrarian angle (probably about "digital transformation is a leadership problem")
- [ ] Saved to `outputs/`

### 10. Test /import (alternative path)

Instead of answering questions one by one, paste Marcus's email from the voice input directly:

Type: `/import`

Paste:
> "Tom — I looked at your P&L and your org chart. You've got 4 people between a customer order and the person who schedules production. That's not a staffing problem, that's an architecture problem. Happy to spend a day at your plant and show you where the drag is. If I can't find $500K in 3 weeks, I'll refund the diagnostic. Let me know."

Verify:
- [ ] Claude identifies voice signals, offer signals, audience signals
- [ ] Updates relevant Context files
- [ ] Reports what was found and what's still missing

---

## Expected Output Quality

After all 4 extractions, any generated output should:

1. **Sound like Marcus** — direct, specific, uses "floor" not "dashboard", short sentences
2. **Reference his framework** — "Operational Gravity Map" should appear naturally
3. **Target his audience** — mid-market manufacturing CEOs stuck at a revenue plateau
4. **Include his proof points** — "$1.2M saved", "$500K guarantee", "14 years, never refunded"
5. **Avoid his anti-language** — no "synergy", "leverage", "unlock potential", "thought leader"

If the output sounds generic, the Context files aren't deep enough. Run `/enrich`.

---

## Time to Complete

| Step | Time |
|------|------|
| /setup | 2 min |
| /extract soul | 10 min |
| /extract audience | 7 min |
| /extract offer | 7 min |
| /extract voice | 7 min |
| /audit + outputs | 5 min |
| **Total** | **~40 min** |
