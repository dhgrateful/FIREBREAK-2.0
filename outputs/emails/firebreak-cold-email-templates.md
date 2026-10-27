---
type: output
status: active
date: 2026-07-28
last-updated: 2026-07-28 09:55
related:
  - "[[offer]]"
  - "[[audience]]"
---

# FIREBREAK Cold-Email Templates (GHL format)

12 HTML email templates built in the exact look of the GHL master
**"FIREBREAK EMAIL TEMPLATE - Danny"** (same header logos, Ubuntu font,
`#EAF0F6` card, "Let's make a difference, / Danny / Director of Business
Development" sign-off, unsubscribe footer). Named by subcategory. Copy is the
verified, operator-approved copy from the FIREBREAK cold-email Google Docs
([FIREBREAK Drive folder](https://drive.google.com/drive/folders/1KuJGXUTXn71pX180U-fUKb5xFX7aC2oF),
updated 2026-09-01). Merge fields use GHL native tokens (`{{contact.first_name}}`,
`{{contact.company_name}}`).

## ⭐ CURRENT initial emails (2026-09-03) — "8-minute Fit Check" CTA

Operator deleted the original first-touch emails and changed the CTA from a 15-min
discovery call to a low-commitment **8-minute Fit Check**
(booking link `https://link.powerinlocal.com/widget/booking/hQNQc6UdEgjUszNcEoj0`).
Rewritten Hormozi-style: catchy cold-open subject, lead with the prospect's most
*active* problem (see `research/2026-09-03-firebreak-problem-stacks-icp-valueprop.md`),
then FIREBREAK as the new category (air, no water/chemicals). One initial email per of
**four** categories (Airport added). Generator: `.context/pipeline/build_initial_emails.py`.

| Category | HTML file | Subject (lead) |
|---|---|---|
| Private Industry | `private-industry-initial.html` | When water makes the fire worse |
| Prescribed Burns | `prescribed-burns-initial.html` | Finish the unit before the window closes |
| Airport | `airport-initial.html` | The foam is going away. The fire isn't. |
| Wildfire | `wildfire-initial.html` | Hold a line where there's no water for miles |

**Subject A/B options** — Private Industry: *When water makes the fire worse · The foam
problem at {{contact.company_name}} · Your first five minutes*. Prescribed Burns:
*Finish the unit before the window closes · Machine control over your flame front · 6×
faster burn, 55% output*. Airport: *The foam is going away. The fire isn't. · Past AFFF
at {{contact.company_name}} · The grass fire foam won't fix*. Wildfire: *Hold a line
with no hydrant · The embers jumping your line · No water for miles*.

The 12 templates below are the ORIGINAL first-touch/variant set (CTA = firebreakinfo.com/demo,
now superseded for first touch). Kept for reference / the role-variant angles + bumps.

Files live in `outputs/emails/`. Regenerate with
`.context/pipeline/build_email_templates.py`.

| # | Template name | File |
|---|---|---|
| 1 | FIREBREAK — Private Industry — Hold the Line | `private-industry-hold-the-line.html` |
| 2 | FIREBREAK — Private Industry — Where Water Is a Liability | `private-industry-water-liability.html` |
| 3 | FIREBREAK — Private Industry — Protect the Asset | `private-industry-protect-the-asset.html` |
| 4 | FIREBREAK — Private Industry — Follow-up (+3d) | `private-industry-followup.html` |
| 5 | FIREBREAK — Prescribed Burns — Steer the Burn | `prescribed-burns-steer-the-burn.html` |
| 6 | FIREBREAK — Prescribed Burns — Beat the Weather Window | `prescribed-burns-weather-window.html` |
| 7 | FIREBREAK — Prescribed Burns — For the Preserve | `prescribed-burns-for-the-preserve.html` |
| 8 | FIREBREAK — Prescribed Burns — Follow-up (+3d) | `prescribed-burns-followup.html` |
| 9 | FIREBREAK — Wildfire — No Water Required | `wildfire-no-water-required.html` |
| 10 | FIREBREAK — Wildfire — Protect the Structures | `wildfire-protect-the-structures.html` |
| 11 | FIREBREAK — Wildfire — Reduce Firefighter Exposure | `wildfire-reduce-exposure.html` |
| 12 | FIREBREAK — Wildfire — Follow-up (+3d) | `wildfire-followup.html` |

## Subject-line options (rotate / A-B test)

**Private Industry:** Buying your brigade time at {{contact.company_name}} · The
first 5 minutes of a fire at your facility · Another layer between an ignition and
a shutdown · A fire tool that doesn't add water to the problem · Protecting your
site in the first 10 minutes

**Prescribed Burns:** Directing your flame front on demand · Machine control over
your flame front · 6× faster burn front, at 55% output · Getting the burn done
inside the window · Make the fire stop exactly where you say

**Wildfire:** Holding a line where there's no water to pull from · A line you can
hold with no hydrant for miles · Suppression that runs on air, not water · Stop the
embers that jump ahead of the fire · A defensive line that keeps crews further back

## Getting them into GoHighLevel

**The GHL email API cannot import custom HTML** — the `POST /emails/builder`
endpoint only ever creates a blank default template (verified against 6 field-name
variants; no update endpoint exists). Custom-HTML import is UI-only. To load these:

1. Marketing → Emails → Templates → **+ New Template → Import HTML** (a.k.a.
   "Code Your Own").
2. Paste the contents of the matching `.html` file; name it per the table above.
3. Set the subject from the options above when you attach it to a
   campaign/workflow.

Each file is self-contained and renders identically to the master template.
