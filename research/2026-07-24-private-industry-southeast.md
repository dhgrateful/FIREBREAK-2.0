---
type: research
format: market
date: 2026-07-24
last-updated: 2026-07-24 09:30
confidence: high
related:
  - "[[audience]]"
  - "[[offer]]"
---

# Private Industry — Southeast (Exhaustive Rebuild)

Second FIREBREAK segment expanded to an **exhaustive Southeast** pass, after
Prescribed Burns. Round 1's private-industry list (129 contacts) survived only in
GoHighLevel, so this is a fresh 66-org SE list built around the firebreak-device
ICP: **facilities with ignition/wildfire exposure and real safety budgets.**

## Result (2026-07-24)

66-org SE list (`research/private-industry/prospects_se.json`) enriched via the
**Apollo industrial profile** (`enrich_apollo_deep.py` with `DEEP_PROFILE=industrial`).
**149 verified contacts loaded**, tagged `SE Prospect` + `Private Industry`.

Buyer titles landed are exactly right: **Process Safety Managers, EHS Managers,
plant Fire Chiefs, Emergency Response Coordinators/Managers, Plant Managers,** and —
for utilities — **Vegetation Management / Wildfire Mitigation** leads (the strongest
wildfire-liability buyer motivation).

Hunter was run first but under-performed for this segment (mixed roles + wrong
domains: Vulcan→a Canadian miner, BWX→Broadcom/CA, Kiawah→a pastry chef). Apollo's
title-targeted search + `people/match` is the right tool for private-industry EHS
rosters. Kept the Apollo output; Hunter pass discarded.

## Segment mix (66 orgs)

| Vertical | Orgs | Why they buy |
|---|---|---|
| Electric utilities | 11 | Wildfire liability, transmission-ROW ignition, vegetation mgmt |
| Refineries / pipeline / terminals | 13 | Process-safety budgets, fire brigades, WUI tank farms |
| Chemical plants | 9 | Process safety, on-site emergency response |
| Pulp / paper / sawmills / steel | 9 | Mill fire exposure, large wooded sites |
| Mining / aggregates / cement | 4 | Reclaimed land, dry-site ignition |
| Railroads | 2 | ROW fire ignition, hazmat corridors |
| Resorts / golf (WUI) | 7 | Wildland-urban interface, grounds/land |
| Ports | 3 | Fuel/hazmat handling, emergency mgmt |
| Agribusiness / ranch land | 4 | Large land holdings, Deseret Ranches burns |
| Defense / shipyards | 2 | On-site fire depts, EHS engineering |
| Timber (as industrial mills) | 2 | Mill safety + land management |

## How it was built (repeatable)

1. `prospects_private_se.json` — org names + Likely Buyer Titles + Priority Band.
2. Correct domains mapped in `targets_private_se.json` (fixed Hunter mis-resolves).
3. `DEEP_PROFILE=industrial python3 enrich_apollo_deep.py <targets> 3` — top-3
   EHS/safety/fire contacts per site, title-filtered, `people/match` for emails.
4. Curate: drop contractor-domain (`indsg.com`) + rail "Fireman/Oiler" false hits,
   sanitize names, canonicalize legit parent domains (`southernco.com`, `dom.com`,
   `tecoenergy.com`, `vmcmail.com`, `vit.org`, `perdue.com`).
5. `load_to_ghl.py <csv> "Private Industry"` — per-row `<REGION> Prospect` tag.

## Coverage notes

- Empty in Apollo (0 clean): Oglethorpe Power, TVA (`.gov`), Buckeye, Georgia-
  Pacific (`gapac.com`), Argos, Sanderson Farms, Alico, Deseret Ranches, Weyerhaeuser
  & PotlatchDeltic corporate, Pinehurst, Palmetto Bluff, Streamsong. Reach via
  Hunter or manual.
- **TX Gulf Coast refineries** (the biggest) were held out — TX maps to SW, not SE.
  Pick them up in the national/SW phase.

## National expansion — DONE (2026-07-24)

Extended private industry to all 5 regions with per-region tags (`W/SW/NE/MW
Prospect` + `Private Industry`), via the Apollo industrial deep enricher + a
`person_locations` filter (`DEEP_LOCATIONS`) so national companies (Chevron,
Marathon, Dow, etc.) return region-specific staff, correctly tagged.

| Region | Loaded | Standout buyers |
|---|---|---|
| West | 103 | Utility Wildfire Mitigation leads (PG&E, SCE, SDG&E, PacifiCorp, PGE, PSE, Idaho Power, NV Energy, Xcel, Tri-State); CA/PNW refinery process-safety + fire chiefs; Sierra Pacific, Green Diamond; Pebble Beach, Vail |
| Southwest | 104 | TX Gulf refinery/petrochem Process Safety Directors + plant Fire Chiefs (Motiva, ExxonMobil, Shell Deer Park, Flint Hills, LyondellBasell, Dow, BASF, CPChem); APS wildfire mitigation + fire chief; King Ranch |
| Northeast | 75 | Con Ed/PSEG/Eversource/Exelon; PBF/Monroe refineries; DuPont/Air Products/Arkema; Amtrak Chief Fire Safety Officer; U.S. Steel |
| Midwest | 90 | Ameren/DTE/Consumers/ComEd/AEP; BP Whiting + Marathon/Flint Hills refineries; Dow Midland, 3M, CF Industries, Cargill/ADM; U.S. Steel Fire Chief + Deputy; Caterpillar/Deere |

Per-region lists in `targets_private_<region>.json`; loaded CSVs
`<region>_private_load.csv` (also feed the pipeline's dedup). GHL total ~767.

## Next
National **prescribed burns** (western/Great-Plains state forestry + federal +
timber), then the **Wildfire suppression** segment (fire departments, Cal Fire /
state wildfire divisions, federal IHCs, air tanker & helitack operators, wildland
fire contractors).
