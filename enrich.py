"""Enrich FIREBREAK prospect list with contacts/emails via the Hunter.io API.

- One domain search per UNIQUE company (cached -> never re-spends credits).
- Ranks returned people against the sheet's target buyer titles.
- Verifies the single best contact per company.
- Writes a CSV mapped 1:1 back to the 187 prospect rows.

Run:  python3 enrich.py
"""

import csv
import json
import os
import time
import urllib.parse
import urllib.request

from ghl import load_env

load_env()
KEY = os.environ["HUNTER_API_KEY"]
BASE = "https://api.hunter.io/v2"

CACHE_PATH = ".context/hunter_cache.json"
VERIFY_CACHE_PATH = ".context/hunter_verify_cache.json"
PROSPECTS_PATH = ".context/prospects.json"
OUT_CSV = ".context/firebreak_prospects_enriched.csv"

# Keywords that signal a relevant buyer for FIREBREAK (safety / ops / site leadership).
ROLE_KEYWORDS = [
    ("ehs", 10), ("hse", 10), ("eh&s", 10), ("environmental health", 10),
    ("process safety", 10), ("safety", 8), ("fire", 8), ("emergency", 8),
    ("loss prevention", 8), ("risk", 6), ("security", 5), ("health", 5),
    ("environment", 6), ("refinery manager", 9), ("mill manager", 9),
    ("plant manager", 9), ("site manager", 8), ("terminal manager", 8),
    ("general manager", 7), ("operations", 6), ("reliability", 5),
    ("maintenance", 5), ("facility", 5), ("facilities", 5),
    ("superintendent", 5), ("resort", 4), ("ranch", 4),
]


def _get(path, **params):
    params["api_key"] = KEY
    url = f"{BASE}/{path}?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "firebreak-ghl/1.0"})
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        return {"_error": e.code, "_body": body}


def load_cache(path):
    return json.load(open(path)) if os.path.exists(path) else {}


def save_cache(path, obj):
    json.dump(obj, open(path, "w"), indent=1)


def score_email(e):
    pos = (e.get("position") or "").lower()
    dept = (e.get("department") or "").lower()
    text = pos + " " + dept
    s = 0
    for kw, w in ROLE_KEYWORDS:
        if kw in text:
            s += w
    # tie-breaker: Hunter confidence + seniority
    s = s * 100 + (e.get("confidence") or 0)
    sen = (e.get("seniority") or "")
    if sen == "executive":
        s += 30
    elif sen == "senior":
        s += 15
    return s


def best_contact(emails):
    personal = [e for e in emails if e.get("type") != "generic" and e.get("first_name")]
    if not personal:
        return None
    return max(personal, key=score_email)


def main():
    prospects = json.load(open(PROSPECTS_PATH))
    cache = load_cache(CACHE_PATH)
    vcache = load_cache(VERIFY_CACHE_PATH)

    orgs = []
    for p in prospects:
        o = p["Organization"].strip()
        if o not in orgs:
            orgs.append(o)

    print(f"{len(prospects)} prospect rows / {len(orgs)} unique companies\n")

    # --- Domain search per unique company ---
    for i, org in enumerate(orgs, 1):
        if org in cache:
            continue
        res = _get("domain-search", company=org, limit=30)
        data = res.get("data", {})
        cache[org] = {
            "domain": data.get("domain"),
            "pattern": data.get("pattern"),
            "organization": data.get("organization"),
            "emails": data.get("emails", []),
            "error": res.get("_error"),
        }
        save_cache(CACHE_PATH, cache)
        d = cache[org]
        bc = best_contact(d["emails"])
        tag = f"{d['domain'] or '?'}"
        if bc:
            tag += f" -> {bc['value']} ({bc.get('position')})"
        elif d.get("error"):
            tag += f" [error {d['error']}]"
        else:
            tag += " [no personal emails]"
        print(f"  [{i:>3}/{len(orgs)}] {org}: {tag}")
        time.sleep(0.15)

    # --- Verify best contact per company ---
    print("\nVerifying best contacts...")
    for org in orgs:
        bc = best_contact(cache[org]["emails"])
        if not bc:
            continue
        em = bc["value"]
        if em in vcache:
            continue
        res = _get("email-verifier", email=em)
        vcache[em] = res.get("data", {}).get("status") or res.get("_error") or "unknown"
        save_cache(VERIFY_CACHE_PATH, vcache)
        time.sleep(0.15)

    # --- Build CSV (1 row per prospect) ---
    cols = [
        "Region", "Organization", "Site / Property", "Segment", "Geography",
        "Likely Buyer Titles", "Priority Band", "Priority Score",
        "Domain", "Email Pattern",
        "Best Contact Name", "Best Contact Title", "Best Contact Email",
        "Email Confidence", "Verification", "Other Relevant Emails", "Generic Emails",
    ]
    n_with_email = 0
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for p in prospects:
            c = cache[p["Organization"].strip()]
            emails = c["emails"]
            bc = best_contact(emails)
            generic = [e["value"] for e in emails if e.get("type") == "generic"]
            relevant = []
            for e in emails:
                if e is bc or e.get("type") == "generic":
                    continue
                if score_email(e) >= 500:  # has a role-keyword hit
                    relevant.append(f"{e['value']} ({e.get('position')})")
            row = {
                "Region": p.get("Region", ""),
                "Organization": p["Organization"],
                "Site / Property": p.get("Site / Property", ""),
                "Segment": p.get("Segment", ""),
                "Geography": p.get("Geography", ""),
                "Likely Buyer Titles": p.get("Likely Buyer Titles", ""),
                "Priority Band": p.get("Priority Band", ""),
                "Priority Score": p.get("Priority Score", ""),
                "Domain": c.get("domain") or "",
                "Email Pattern": c.get("pattern") or "",
                "Best Contact Name": f"{bc.get('first_name','')} {bc.get('last_name','')}".strip() if bc else "",
                "Best Contact Title": bc.get("position", "") if bc else "",
                "Best Contact Email": bc.get("value", "") if bc else "",
                "Email Confidence": bc.get("confidence", "") if bc else "",
                "Verification": vcache.get(bc["value"], "") if bc else "",
                "Other Relevant Emails": "; ".join(relevant[:5]),
                "Generic Emails": "; ".join(generic[:3]),
            }
            if row["Best Contact Email"]:
                n_with_email += 1
            w.writerow(row)

    print(f"\nWrote {OUT_CSV}")
    print(f"Prospect rows with a named best-contact email: {n_with_email}/{len(prospects)}")

    acct = _get("account").get("data", {}).get("requests", {})
    if acct:
        print(f"Hunter searches used: {acct['searches']['used']}/{acct['searches']['available']}"
              f" | verifications used: {acct['verifications']['used']}/{acct['verifications']['available']}")


if __name__ == "__main__":
    main()
