---
type: research
status: active
date: 2026-08-19
last-updated: 2026-08-19 10:00
confidence: high
related:
  - "[[audience]]"
  - "[[offer]]"
---

# Airport Fire Departments (ARFF) — New Target Segment

Do airports have firefighters worth targeting for FIREBREAK? **Yes — at commercial
airports, by federal law.**

## The regulatory reality (FAA Part 139)

- **~520 U.S. airports** are certificated under **14 CFR Part 139** — the ones that
  serve scheduled passenger airlines (international, regional, and municipal
  commercial-service airports).
- Every Part 139 airport must staff **ARFF (Aircraft Rescue & Fire Fighting)**
  crews on-field whenever air carriers operate (§139.315–139.319). That's a
  dedicated, trained, on-staff airport fire department at each one.
- **ARFF Index (A–E)** scales required equipment/staffing to the length of aircraft
  served and daily departures — bigger airports = bigger fire departments.

## Who has firefighters, who doesn't

- **Commercial / Part 139 airports (public — city / county / airport or port
  authority owned):** have ARFF firefighters. **These are the buyers.**
- **General-aviation / private airports (non-Part 139):** **no ARFF requirement** —
  they rely on the local municipal fire department (8–15 min runway response).
  So the "private airport" bucket is largely empty of on-staff fire personnel.
- **Military airfields:** have fire departments (DoD — separate federal track).

**Implication for tagging:** the meaningful split isn't "private vs municipal" — it's
**Commercial/Part 139 (has ARFF) vs GA/private (doesn't).** We tag the buyers
`Airport` + `Commercial ARFF`; if any private/corporate field surfaces real fire
staff we tag it `Private Airport`.

## Buyer titles

ARFF Chief / Airport Fire Chief, Fire Chief, Deputy/Assistant Fire Chief,
Battalion/Division Chief, ARFF Captain, Fire Marshal, Director of Public Safety,
Airport Operations Director, Emergency Manager. (Apollo `arff` profile.)

## Pipeline

- Target orgs = Part 139 airports keyed by their operating authority's domain
  (`atl.com`, `flynashville.com`, `rdu.com`, …). ARFF may sit under the airport
  domain (authority-run departments) or under the city FD (municipally-run) — Apollo
  surfaces whichever is indexed.
- Profile `DEEP_PROFILE=arff`; region via `DEEP_LOCATIONS`; lists
  `targets_airport_<region>.json`; tags `Airport|Commercial ARFF` via load_to_ghl.py.

## FIREBREAK fit / angles (to develop)

Airfields carry real vegetation/grass-fire risk on and around runways, fuel-farm
fire exposure, and WUI risk at the perimeter — all water-independent, directed-
airflow use cases. ARFF itself is foam-based for fuel fires; FIREBREAK's angle is
holding/redirecting flame & embers off runways, fuel storage, and terminals without
tapping the airport's water system.

## Southeast result (2026-08-19) — proof of concept

Enriched 31 SE Part 139 airports (`arff` profile). 86 contacts surfaced, curated to
**29 loaded** (18 true fire/ARFF + 11 public-safety / operations directors), tagged
`SE Prospect` + `Airport` + `Commercial ARFF`.

- **Real airport ARFF departments** (fire under the airport authority's own domain):
  Southwest Florida (Fire Chief Tracy Young + ARFF Captain + Battalion Chief),
  Greenville-Spartanburg (Deputy Fire Chief + ARFF Lieutenant + Battalion Chief),
  Norfolk (Aircraft Rescue Firefighters + Fire Lieutenant), Columbia (Battalion
  Chief + Asst Chief of Fire), plus Fire Chiefs at Richmond & Cincinnati/N. Kentucky.
- **Big hubs run ARFF via the city fire dept** (ATL, MIA, TPA, CLT, RDU) → Apollo
  surfaced their **Airport Operations / Public Safety directors** instead — the right
  entry point there; the actual firefighters sit under the municipal FD domain.
- **Curation rule:** keep fire / ARFF / rescue / battalion+division chief / public
  safety + operations *directors*; drop junior ops (specialist/agent/officer/manager)
  and contamination (a "Division Chief **Attorney**", an "**IS** Technical" director,
  a "Fire **Alarm** System" tech). Watch alt airport domains (Savannah=`flysav.com`,
  Piedmont=`gsoair.org`, Birmingham=`flybhm.com`).

## National result (2026-08-19) — all five regions

| Region | Loaded | Standout airport fire departments |
|---|--:|---|
| Southeast | 29 | SW Florida (Fire Chief + ARFF Capt + BC), Greenville-Spartanburg, Norfolk, Richmond, CVG |
| West | 28 | Sea-Tac (Asst Fire Chief + 2 BCs), Spokane, Portland, Anchorage (ARFF), Honolulu, Bozeman, Jackson Hole |
| Southwest | 15 | **DFW full ARFF dept** (Fire Chief + Asst + 3 Capts), Austin, Tucson |
| Northeast | 19 | **Boston Logan** (2 Fire Chiefs + Capt + Lt), Pittsburgh, Manchester, Buffalo, T.F. Green |
| Midwest | 13 | **Indianapolis** (Div Chief + Marshal + BC + Public Safety), Detroit, Omaha, Cleveland, Milwaukee |

**104 airport contacts total**, all `Airport` + `Commercial ARFF` + region-tagged.

### Wave 2 (2026-08-19) — regional/mid-size airports: +62

Second pass over ~73 mid-size Part 139 airports → **62 loaded** (GHL total ~1,081;
airport segment now **166**). Two flavors: airports with a dedicated ARFF dept under
their own domain (Grand Rapids, Flint, Pensacola, Wilmington, Asheville, Long Island
MacArthur, Bangor), and small airports where the **city fire department provides
ARFF** (Fayetteville, Santa Barbara, Eugene, Provo, Idaho Falls, Waco, Lawton) — kept
their fire leadership since that city FD is the airport's fire authority. Extra
contamination the shared city/state domains pulled (all dropped): Alaska **state**
fire/DPS on `alaska.gov`, a Medford **real-estate** domain, a **home-inspection**
firefighter, a Santa Fe **convention center** director, an AZ **charter-schools**
board.

**Pattern confirmed:** mid-size airports run ARFF under the airport authority's own
domain (fire staff surface cleanly); the biggest hubs (ATL/LAX/ORD/JFK/MSP/SFO/DEN)
run ARFF via the city fire dept or Port Authority PD, so only their ops/public-safety
directors surface under the airport domain — the actual firefighters sit under the
municipal FD / PA domain (reachable later via Hunter or city-FD targeting).

### Wave 3 (2026-08-19) — long tail: +39

Third pass over ~59 smaller regional airports → **39 loaded** (airport segment now
**205**; GHL total ~1,129). Clear diminishing returns — many fields returned zero
(NE3 got 0 clean), confirming we've reached the practical floor for airports with
their own reachable ARFF. Good late hits: Bellingham, Aspen, Sun Valley, Helena,
Glacier Park, Las Cruces, Prescott, Appleton, Sioux Gateway, Nantucket, Abilene.

## Airport segment — DONE (205 total)

| Wave | Airports | Loaded |
|---|--:|--:|
| 1 (major/primary) | ~100 | 104 |
| 2 (mid-size regional) | ~73 | 62 |
| 3 (long tail) | ~59 | 39 |
| **Total** | **~230** | **205** |

**Practically exhausted.** What remains is NOT cleanly reachable in Apollo:
- **Mega-hub ARFF** (ATL→Atlanta FD, LAX→LAFD, ORD→Chicago FD, JFK/EWR/LGA→PANYNJ,
  DEN→Denver FD, SFO→SFFD, MSP→MAC): embedded in big city fire departments — same
  shared-domain contamination as CAL FIRE. Searching those domains returns mostly
  non-airport city firefighters, so it would dilute the segment, not extend it.
  Best pursued later via Hunter or by name-targeting each airport's ARFF battalion.
- **Tiny GA / non-Part-139 fields:** essentially no dedicated fire staff.
- **Private/corporate fields + FBOs:** rare fire staff → tag `Private Airport` if found.

Sources: FAA Part 139 / ARFF (faa.gov/airports), 14 CFR §139.315–319 (ecfr.gov).
