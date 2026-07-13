"""Load the enriched FIREBREAK prospect list into GoHighLevel as contacts.

- Deduplicates by email (one contact per person; multi-site companies collapse
  into a single contact with all their sites listed).
- Skips rows whose best-contact email failed verification ("invalid").
- Tags every contact: "SE Prospect" + "Private Industry".
- Maps Job Title / Site(s) / Segment / Priority Band into custom fields.
- Uses upsert, so re-running updates rather than duplicating.

Run:  python3 load_to_ghl.py
"""

import csv
import time
from collections import defaultdict

from ghl import GHLClient, load_env

CSV_PATH = ".context/firebreak_prospects_enriched.csv"
TAGS = ["SE Prospect", "Private Industry"]
SKIP_VERIFICATION = {"invalid"}
CUSTOM_FIELDS = ["Job Title", "Site(s)", "Segment", "Priority Band"]


def ensure_custom_fields(client):
    """Return {name: id}, creating any missing fields."""
    existing = {f["name"]: f["id"] for f in client.list_custom_fields()}
    out = {}
    for name in CUSTOM_FIELDS:
        if name in existing:
            out[name] = existing[name]
        else:
            f = client.create_custom_field(name)
            out[name] = f["id"]
            print(f"  created custom field: {name}")
    return out


def main():
    load_env()
    client = GHLClient()
    fields = ensure_custom_fields(client)

    rows = list(csv.DictReader(open(CSV_PATH)))

    # Group by email -> aggregate sites; keep first row's details.
    by_email = {}
    sites_by_email = defaultdict(set)
    skipped_no_email = skipped_invalid = 0
    for r in rows:
        email = (r["Best Contact Email"] or "").strip().lower()
        if not email:
            skipped_no_email += 1
            continue
        if r["Verification"] in SKIP_VERIFICATION:
            skipped_invalid += 1
            continue
        by_email.setdefault(email, r)
        if r["Site / Property"]:
            sites_by_email[email].add(r["Site / Property"])

    print(f"{len(rows)} rows -> {len(by_email)} unique contacts to upsert "
          f"(skipped {skipped_no_email} no-email, {skipped_invalid} invalid)\n")

    created = updated = errors = 0
    for i, (email, r) in enumerate(sorted(by_email.items()), 1):
        name = r["Best Contact Name"].strip()
        first, _, last = name.partition(" ")
        website = r["Domain"]
        if website and not website.startswith("http"):
            website = "https://" + website
        cf = [
            {"id": fields["Job Title"], "field_value": r["Best Contact Title"]},
            {"id": fields["Site(s)"], "field_value": "; ".join(sorted(sites_by_email[email]))},
            {"id": fields["Segment"], "field_value": r["Segment"]},
            {"id": fields["Priority Band"], "field_value": r["Priority Band"]},
        ]
        try:
            res = client.upsert_contact(
                email=email,
                firstName=first,
                lastName=last,
                name=name,
                companyName=r["Organization"],
                website=website,
                tags=TAGS,
                source="FIREBREAK enrichment",
                customFields=cf,
            )
            if res.get("new"):
                created += 1
            else:
                updated += 1
            if i % 20 == 0:
                print(f"  [{i}/{len(by_email)}] ...")
        except Exception as e:  # noqa: BLE001
            errors += 1
            print(f"  ERROR {r['Organization']} <{email}>: {e}")
        time.sleep(0.12)

    print(f"\nDone. created={created} updated={updated} errors={errors}")
    print(f"Tags applied: {TAGS} (GHL stores them lowercased)")


if __name__ == "__main__":
    main()
