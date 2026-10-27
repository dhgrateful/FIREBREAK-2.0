---
type: research
format: market
date: 2026-07-13
last-updated: 2026-07-23 18:10
confidence: high
related:
  - "[[audience]]"
  - "[[offer]]"
---

# Prescribed-Burn Operators — Southeast (Batch 1)

First prospecting batch for FIREBREAK targeting the **prescribed-burn** market,
built to run through the **same pipeline** used for the Private Industry round
(the Python GHL tool on the `connect-gohighlevel-location` branch). This is the
research half — the real, Hunter-resolvable organization list. Enrichment
(real names + emails via Hunter) and the GHL import run on the machine that has
the pipeline + API keys.

## Result (2026-07-13)

112-org SE list built and enriched via Hunter over two passes. **32 verified,
correct-role contacts loaded into GHL**, tagged `SE Prospect` + `Prescribed Burns`.
Wins concentrated in private forestry firms, TIMOs, conservation NGOs, and land
trusts (Hunter's strong zone). State forestry agencies / councils / military
(.gov/.mil) stayed empty — Hunter doesn't index them; Apollo would, but the Apollo
key is on the free plan (search/enrichment 403-blocked). See [[audience]].

## Update — Apollo pass (2026-07-23)

Operator upgraded Apollo to a paid plan. Built an **Apollo enrichment step**
(`enrich_apollo.py` + `curate_apollo.py`) that recovers the `.gov`/`.edu`/`.mil`
contacts Hunter couldn't reach. Apollo's two-step flow: `mixed_people/api_search`
(candidates — email + last name obfuscated) → `people/match` by id (reveals the
verified email; ~1 credit each).

**+18 verified, correct-role contacts loaded** (tagged `SE Prospect` +
`Prescribed Burns`), plus the **9 borderline** (right org, soft/stewardship role)
approved and loaded on operator's go — bringing Round 2 to **59 contacts** total. Wins: Georgia
Forestry Commission (Prescribed Fire Center Coordinator), NC Forest Service
(Wildfire Mitigation Forester), SC Forestry Commission (Fire Staff Forester),
Texas A&M Forest Service (District Fire Coordinator), Eglin AFB Jackson Guard (AF
Wildland Fire Ops Section Chief), Camp Lejeune (Fire Chief), Fort Moore/Stewart
(Army Wildland Fire forester), Kentucky Div of Forestry (Chief Forester), Arkansas
Forestry, SC DNR, NC Wildlife, plus Enviva, Manulife Timberland, NWTF, Forest
Stewards Guild, AFM, Forest Resource Consultants, Auburn Forestry.

**Apollo gotcha — shared-domain contamination.** Searching a broad state domain
(e.g. `forestry.alabama.gov`, `dof.virginia.gov`) can return people Apollo files
under a *different* agency on the same `.gov` tenant (Rehab, Human Services, DOT).
An unfiltered fallback search makes this worse. Fix: **title-filtered search only**
+ require a strong fire/forestry title token. **Alabama, Mississippi, Virginia, and
Louisiana state forestry agencies are NOT cleanly in Apollo** — dropped rather than
load a wrong-agency contact. The 9 "borderline" (right org, soft/stewardship/admin
role) were approved by the operator and loaded too.

Still open (national expansion + the ~15 orgs with no resolvable domain / no
Apollo presence: small Rx-burn contractors, volunteer fire councils).

## Update — exhaustive SE deep pass (2026-07-23)

Operator directive: max out the Southeast before going national. Built
`enrich_apollo_deep.py` (pulls the top-N fire/forestry contacts per org, not one)
+ `regions.py` (per-row region tag; still `SE Prospect` for all SE data).

**+85 contacts → Prescribed Burns SE now 144 total.**
- **State forestry agencies, deep:** +36. GA/NC/SC/FL/TX/AR/KY/TN forestry — 4-5
  foresters/fire staff each (district foresters, unit foresters, fire coordinators,
  wildland firefighters). Confirmed legit alt email domains: `gfc.state.ga.us` (GA),
  `ncagr.gov` (NC), `freshfromflorida.com` (FL/FDACS), `tfs.tamu.edu` (TX).
- **Timber/TIMOs, deep:** +48. Rayonier, PotlatchDeltic, Weyerhaeuser, Westervelt,
  RMS, Molpus, Campbell Global, F&W, Interfor, West Fraser, Larson & McGowin,
  International Paper (incl. 2 plant Fire Chiefs) — silviculture foresters. Apollo
  swaps Rayonier↔PotlatchDeltic labels; canonicalize org from the email domain.
- **State wildlife agencies: thin in Apollo** — only NC Wildlife returned a clean
  fire/forestry hit. VA DWR / LA leaked to VITA/VDOT/Louisiana Tech (guard caught
  it). AL/MS/VA state forestry confirmed NOT cleanly in Apollo. These need Hunter
  (their `.com`/`.org` domains) or manual.

Still open for a fully-exhaustive SE: wildlife agencies via Hunter, TNC/NGO deep,
more Rx-burn contractors + Red Hills plantations + land trusts + water-management
districts (list-widening via research), DoD installations.

## National prescribed-burns expansion (2026-07-24)

Extended prescribed burns to all regions, per-region tags (`W/SW/NE/MW Prospect` +
`Prescribed Burns`), fire-profile deep enricher + `person_locations` filter. **+88
contacts.**

| Region | Loaded | Standout |
|---|---|---|
| West | 38 | WA DNR Fire Program Mgr, CO State Forest Service wildland-fire program + deputy state forester, MT DNRC FMOs, Green Diamond & Sierra Pacific foresters; TNC Prescribed Fire Coordinators/Managers |
| Midwest | 26 | MO Conservation Asst Fire Chief, Indiana DNR Fire Chiefs, WI/MI DNR foresters, Pheasants Forever Rx-fire specialist; **TNC Director of Fire Mgmt + Rx Fire Managers** |
| Southwest | 8 | AZ District Forester, OSU fire/emergency prof; TNC Rx Fire Specialist + TX Fire Manager |
| Northeast | 16 | PA Fire Mgmt Forester, MA DCR + Maine Forest Service foresters; TNC Burn Boss, Rx Fire Module Leader, PA/DE Fire Program Mgr |

**Key finding:** The Nature Conservancy (`nature.org`/`tnc.org`) is the richest Rx-
fire source in Apollo — dedicated Prescribed Fire Managers/Coordinators/Burn Bosses
in every region. State agencies vary: WA/OR/CO/MT/WI/MI/ME/PA/MA/AZ surfaced well;
NJ Forest Fire Service, NY DEC, MN/IA/OH/ID/NV/UT/WY forestry, CAL FIRE, TX P&W did
NOT surface cleanly (shared/broad `.gov` or not indexed) — reach via Hunter/manual.
Prescribed Burns total now 232 (144 SE + 88 national). ~950 Apollo credits used.

## What's in this batch

- **File:** `research/prescribed-burns/prospects.json` — 77 organizations,
  drops straight into the pipeline's `.context/prospects.json` (exact schema
  `enrich.py` expects: `Region, Organization, Site / Property, Segment,
  Geography, Likely Buyer Titles, Priority Band, Priority Score`).
- **Scope:** Southeast US, both public agencies + NGOs **and** private
  contractors/landowners (per operator decision 2026-07-13). National expansion
  is a later batch.
- **Priority bands:** A (22) = high-volume, high-resolvability. B (32) = solid.
  C (23) = harder to reach or lower Hunter coverage — run last.

### Segment mix
| Segment | Count | Notes |
|---|---|---|
| State Forestry Agency | 12 | Highest Rx-fire volume; one per SE state |
| Conservation NGO | 12 | TNC state chapters, Longleaf Alliance, NWTF, etc. |
| Timber / TIMO / REIT | 8 | Weyerhaeuser, Rayonier, PotlatchDeltic, Westervelt… |
| Rx-Burn Contractor | 8 | For-hire burn companies (named from state vendor DBs) |
| Prescribed Fire Council | 7 | State councils + regional coordination |
| University / Extension | 7 | Research forests + fire extension programs |
| Military / DoD | 6 | Biggest single-site burners; **weak Hunter coverage (.mil)** |
| State Wildlife Agency | 5 | WMA / game-land burn programs |
| Forestry Mgmt / Consulting | 5 | AFM, F&W, Milliken — manage private acreage |
| Plantation / Private Land | 3 | Red Hills + coastal quail/wildlife lands |
| Research + Private Conservation | 4 | Tall Timbers, Jones Center, Nokuse, Nemours |

## How to run it (on the pipeline machine)

The pipeline lives on the `connect-gohighlevel-location` branch and needs
`HUNTER_API_KEY` + `GHL_PRIVATE_TOKEN` + `GHL_LOCATION_ID` in `.env` (already
configured there from the Private Industry round).

1. Copy `prospects.json` into the pipeline's `.context/prospects.json`.
2. **Change the tag** in `load_to_ghl.py`:
   ```python
   TAGS = ["SE Prospect", "Prescribed Burns"]   # was ["SE Prospect", "Private Industry"]
   ```
3. **Tune the scorer** in `enrich.py` — the current `ROLE_KEYWORDS` are tuned
   for industrial safety titles and will under-rank Rx-fire buyers. Add:
   ```python
   ("burn boss", 10), ("prescribed fire", 10), ("wildland fire", 10),
   ("fire management", 9), ("fire program", 9), ("forester", 8),
   ("forestry", 7), ("silviculture", 7), ("land manager", 8),
   ("land management", 8), ("stewardship", 8), ("natural resources", 7),
   ("conservation", 6), ("wildlife", 6), ("restoration", 6), ("ecologist", 6),
   ```
4. `python3 enrich.py` → writes `.context/firebreak_prospects_enriched.csv`.
   Review the "Best Contact" columns before loading.
5. `python3 load_to_ghl.py` → upserts contacts into GHL, tagged
   **`SE Prospect` + `Prescribed Burns`**, custom fields Job Title / Site(s) /
   Segment / Priority Band. Upsert = safe to re-run.

## Known coverage gaps (expected — pipeline skips them gracefully)

- **Military / DoD (Band C):** natural-resources staff use `.mil` addresses
  Hunter doesn't index. These likely return "no personal emails" — reach by
  phone or via the DoD partnership contacts, not cold email.
- **Small contractors + volunteer councils (Band C):** some run on
  Weebly/WordPress/personal domains; Hunter coverage is thin. Run them last so
  they don't burn search credits ahead of Band A/B.
- Individual sole-proprietor names from the VA vendor list (e.g. single-person
  entries) were dropped in favor of company-form orgs Hunter can resolve.

## Sources
- Southern Group of State Foresters — state forestry agencies & PBAs: https://southernforests.org/
- Southern Fire Exchange — prescribed fire councils: https://southernfireexchange.org/prescribed-fire-councils/
- Southeast Prescribed Fire Update — contractor databases: https://sites.cnr.ncsu.edu/southeast-fire-update/prescribed-burn-contractors/
- Virginia DWR — prescribed fire contractor list: https://dwr.virginia.gov/quail/additional-links/prescribed-burn-contractors/
