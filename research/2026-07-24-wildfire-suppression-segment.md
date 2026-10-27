---
type: research
format: market
date: 2026-07-24
last-updated: 2026-07-24 12:00
confidence: high
related:
  - "[[audience]]"
  - "[[offer]]"
---

# Wildfire Suppression — "Those Responsible for Fighting Them"

Third FIREBREAK segment: the people who fight wildfires (distinct from the
prescribed-burn operators who set them intentionally). Tag = `Wildfire` + region.
Built with a suppression-tuned Apollo profile (`DEEP_PROFILE=wildfire`): fire
chiefs, battalion/division chiefs, fuels & fire operations, hotshot supers,
helitack, engine captains, fire management officers, aerial firefighters.

## Result (2026-07-24) — West + Southwest (where the wildland fire is)

| Region | Loaded | Standout buyers |
|---|---|---|
| West | 31 | LA County Fire (Battalion/Division Chiefs), Orange County Fire Authority (incl. Wildland Fire Defense lead + Fire Marshal), Ventura County Fire, WA DNR Fuels Specialist, Oregon State Fire Marshal + deputies; contractors Grayback Forestry & Wildfire Defense Systems; aerial firefighting Neptune Aviation & Dauntless Air |
| Southwest | 19 | TX A&M Forest Service Director of Aviation, Austin Fire Chief + Battalion Chiefs, Tucson Assistant Chief/Fire Marshal, Phoenix Fire Captains, Oklahoma State Fire Marshal + Assistant |

**50 wildfire contacts loaded**, all region-tagged.

## What works / what doesn't in Apollo

- **Best targets:** county/metro fire departments with their own domains
  (`ocfa.org`, `ventura.org`, `phoenix.gov`, `austintexas.gov`, `tucsonaz.gov`,
  `lacounty.gov`), private wildland-fire contractors, and aerial-firefighting
  operators — all clean corporate/agency domains.
- **CAL FIRE is NOT reachable via `fire.ca.gov`** — Apollo's shared `ca.gov` net
  returns people from the FBI, Corrections, Caltrans, EDD, Education instead. The
  single biggest US wildfire agency needs Hunter or an Apollo org-id approach.
- Drop aircraft **mechanics/maintenance** (not buyers) and watch `.gov`
  contamination (a Health-Dept "fire chief," a legal "Post-Conviction division
  chief," an "antibiotic stewardship" director all slipped through title matches).

## CAL FIRE + Federal added via Hunter (2026-08-19)

**Hunter searches by exact domain, so it dodges the shared-`.gov` contamination that
broke Apollo.** This unlocked the two biggest gaps:

- **CAL FIRE (`fire.ca.gov`): +74.** Hunter has 1,239 emails on the domain, all
  clean CAL FIRE — pulled the fire leadership (Unit/Division/Battalion/Operations/
  Deputy/Assistant/Fire Chiefs), dropped admin/HR. Tagged `W Prospect` + `Wildfire`.
- **Federal (`blm.gov` +11, `nps.gov` +4): +15.** BLM Fire Chief, Chief of Wildland
  Fire Operations, Chief of Aviation; NPS Wildland Fire Director + Fire Chiefs.
  National staff → tagged **`Federal Prospect`** + `Wildfire` + `Federal` (added
  `Federal` to `regions.py`). USFS `fs.usda.gov`, NIFC `nifc.gov`, DOI `doi.gov` had
  no usable Hunter coverage (USFS email is on the contaminated `usda.gov`).

**Wildfire segment now 139:** West 31 + SW 19 + CAL FIRE 74 + Federal 15.
Loaders: `calfire_load.csv`, `fedfire_load.csv` (from `*_hunter.json`).

## Not pursued (low incremental value)

- **NE / MW / SE state wildfire** — in these regions wildfire response *is* the state
  forestry agency, and those are already captured in the **Prescribed Burns** segment
  (232, all regions); Rx vs suppression staff overlap heavily, so a "Wildfire" re-mine
  would mostly re-tag existing contacts. SE Hunter probe (FL `fdacs.gov`, GA
  `gatrees.org`, etc.) confirmed forestry-fire titles are buried in the huge state-Ag
  domains — thin yield.
- More **contractors + aviation** (Coulson, Bridger, 10 Tanker, Columbia helicopters).
- Big-hub airport ARFF via city FDs (separate segment note).
