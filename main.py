"""Entry point: verify the GoHighLevel connection and show a quick summary.

Run with:  python3 main.py
"""

from ghl import GHLClient, GHLError, load_env


def main():
    load_env()
    client = GHLClient()

    print(f"Verifying GoHighLevel connection to location {client.location_id} ...")
    try:
        result = client.verify()
    except GHLError as exc:
        print(f"❌ Connection failed (HTTP {exc.status}): {exc.body}")
        raise SystemExit(1)

    total = result.get("meta", {}).get("total", "unknown")
    print(f"✅ Connected. Location reports {total} contact(s).")


if __name__ == "__main__":
    main()
