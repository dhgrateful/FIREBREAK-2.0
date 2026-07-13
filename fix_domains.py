"""Re-run Hunter domain search with CORRECT explicit domains for companies that
the company-name lookup resolved to the wrong entity or a jobs/investor subdomain.
Updates the cache in place; then re-run enrich.py to rebuild the CSV.
"""

import json
import os
import time
import urllib.parse
import urllib.request

from ghl import load_env

load_env()
KEY = os.environ["HUNTER_API_KEY"]
CACHE_PATH = ".context/hunter_cache.json"

# org name in sheet -> correct primary domain
OVERRIDES = {
    # wrong company entirely
    "Buckeye": "buckeye.com",
    "Alico": "alicoinc.com",
    "Sea Island Company": "seaisland.com",
    "Motiva": "motiva.com",
    "Vulcan Materials": "vulcanmaterials.com",
    "Omni Hotels": "omnihotels.com",
    "Viña Santa Rita": "santarita.com",
    # resolved to wrong subdomain -> no personal emails
    "Southern Company / Georgia Power": "georgiapower.com",
    "Pinehurst Resort": "pinehurst.com",
    "Chemours": "chemours.com",
    "Huntington Ingalls Industries": "hii.com",
    "BWX Technologies": "bwxt.com",
    "Arizona Public Service": "aps.com",
    "Freeport-McMoRan": "fcx.com",
    "Barrick": "barrick.com",
    "Climax Molybdenum": "climaxmolybdenum.com",
    "bp": "bp.com",
    "Roseburg Forest Products": "roseburg.com",
    "PG&E": "pge.com",
    "Pebble Beach Company": "pebblebeach.com",
    "Perdue AgriBusiness": "perdueagribusiness.com",
    "Salamander Resort": "salamanderhotels.com",
    "Sun Valley Resort": "sunvalley.com",
    "Rio Tinto Kennecott": "riotinto.com",
    "Green Diamond Resource Company": "greendiamond.com",
    "Roseburg Forest Products ": "roseburg.com",
}


def _get(path, **params):
    params["api_key"] = KEY
    url = f"https://api.hunter.io/v2/{path}?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": "firebreak-ghl/1.0"})
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return {"_error": e.code, "_body": e.read().decode()}


def main():
    cache = json.load(open(CACHE_PATH))
    for org, domain in OVERRIDES.items():
        res = _get("domain-search", domain=domain, limit=40)
        data = res.get("data", {})
        n = len(data.get("emails", []))
        cache[org] = {
            "domain": data.get("domain"),
            "pattern": data.get("pattern"),
            "organization": data.get("organization"),
            "emails": data.get("emails", []),
            "error": res.get("_error"),
        }
        print(f"  {org:<35} {domain:<26} -> {data.get('organization') or '?'} ({n} emails)")
        time.sleep(0.15)
    json.dump(cache, open(CACHE_PATH, "w"), indent=1)
    print("\nCache updated. Now re-run: python3 enrich.py")


if __name__ == "__main__":
    main()
