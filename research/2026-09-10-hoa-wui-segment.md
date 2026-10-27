---
type: research
status: active
date: 2026-09-10
last-updated: 2026-09-10 12:00
related:
  - "[[audience]]"
  - "[[offer]]"
purpose: HOA / WUI-community segment — buyer, geography, and outreach build
---

# HOA / WUI Communities — New Target Segment

Are homeowners associations a FIREBREAK prospect? **Yes — the WUI ones out West,
driven by the insurance crisis.**

## Why HOAs are a real (and timely) buyer

- **HOAs own the common-area fuel breaks** — greenbelts, open space, roadside
  rights-of-way — that carry fire straight into a neighborhood, and are legally
  responsible for defensible space on them (CA **Zone 0** rules, 2026).
- **Insurance is the burning platform:** HOA master policies now carry liability if
  common areas don't meet defensible-space standards; insurers **deny claims and
  non-renew** communities that don't mitigate. That's forcing spend right now.
- **FIREBREAK fit:** create/hold a community-scale fuel break on common open space,
  reduce ember exposure to the neighborhood, do it with no water/chemicals on
  equipment the community's landscape/maintenance crews already run.

## Geography — start where the fires are (per operator)

**West first** (CA leads: WUI master-planned + foothill/mountain communities), then
CO, AZ, NV. Florida de-prioritized (hurricane/flood, not wildfire). Region tag by the
management firm's region; segment tag **`HOA`**.

## Buyer & channel

The person "in charge of that" = the community's **General Manager** (large
master-planned communities) or **Community Association Manager**, plus
**operations/maintenance directors**. They concentrate at **HOA management companies**
(each runs many WUI associations) — clean domains, ideal for Hunter.

## Build (2026-09-10) — Hunter, West + SW

Hunter domain-search on 22 Western/SW HOA management firms; filtered to buyer titles
(GM / community & association manager / regional director / ops-maintenance-facilities
director / president-VP), dropped back-office (IT/HR/accounting/escrow/lifestyle/
customer-service/marketing/sales); capped 14/firm. **196 loaded** (West 142, SW 54) —
75 General Managers, 70 Community/Association Managers, 30 execs/VPs, 9 regional
directors. Tagged `<region> Prospect` + `HOA`.

- **Strong Hunter coverage:** Action Property Mgmt, Seabreeze, Powerstone, Keystone
  Pacific, PMP, The Management Trust, MSI (CO), Advance HOA (CO), AAM (AZ), City
  Property (AZ), Goodwin (TX).
- **No/thin coverage (0):** Euclid, Homestead, Hammersmith, Taylor Assoc (NV), Kinney
  — bad domain guess or no Hunter data. Retry with corrected domains later.
- Loader: `.context/pipeline/build_hoa_hunter.py` → `.context/hoa_load.csv`.

## Batch 2 (2026-09-10) — more firms + master-planned communities: +43

Hunter hit its **billing-period cap** mid-run (1000/1000 searches used, 0 left) — got
19 through (Kinney, RowCal, Curtis) then pivoted the rest to **Apollo** (added `hoa`
profile to `enrich_apollo_deep.py`; `.com`/`.org` community domains are clean for
Apollo). Apollo: **+24** (of 21 orgs). **Batch-2 total +43 → HOA segment = 239.**

- **Master-planned communities are the standout direct targets** (own GM + maintenance
  + forestry staff): **Tahoe Donner** (GM + **Defensible Space Program Manager** + Asst
  Ops Directors), **Rancho Santa Fe Association** (CAO/GM), **The Sea Ranch** (Community
  Manager/CEO + Facilities Director), **Pine Mountain Club** (GM), **Anthem** (Maint Mgr,
  `anthemcouncil.com`), **Sun City Grand** (GM, `livegrandaz.com`). Plus CAMs at Warren,
  LCM, Homestead, CCMC.
- **No Apollo/Hunter coverage (0):** Nordic, Desert Mgmt, Euclid, Hammersmith, Taylor
  (NV), Brown, Trestle, Lake Wildwood, Bear Valley Springs, Hidden Valley Lake.
- Files: `build_hoa_hunter2.py`, `targets_hoa_apollo.json` → `hoa_apollo_load.csv`.

## Not yet done / open

- **Large named WUI master-planned communities** with their own GM/staff domains
  (Coto de Caza, Blackhawk, Lake Arrowhead, Tahoe/Incline, Anthem, Serrano, Castle
  Pines, communities near Boulder/Colo. Springs/Prescott/Flagstaff) — direct targets.
- **Community Services Districts / Metro Districts** (quasi-govt WUI communities).
- **National firms** (FirstService, Associa, RealManage, CCMC) skipped for clean
  region tags — their staff span all regions; revisit if a national channel play is wanted.
- **HOA-specific email set** (Hormozi, 8-min Fit Check) — lead with the insurance/
  liability + common-area fuel-break angle.
