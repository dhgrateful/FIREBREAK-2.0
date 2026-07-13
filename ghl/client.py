"""A small GoHighLevel (HighLevel API v2 / LeadConnector) client.

Uses only the Python standard library, so it runs with no `pip install`.
Credentials are read from the environment (see `load_env`).
"""

import json
import os
import urllib.error
import urllib.parse
import urllib.request

API_BASE = "https://services.leadconnectorhq.com"
# HighLevel pins behaviour to an API version via this header.
API_VERSION = "2021-07-28"


class GHLError(Exception):
    """Raised when the HighLevel API returns a non-2xx response."""

    def __init__(self, status, body):
        self.status = status
        self.body = body
        super().__init__(f"GoHighLevel API error {status}: {body}")


def load_env(path=".env"):
    """Load KEY=VALUE pairs from a .env file into os.environ.

    Existing environment variables are not overwritten. Lines that are blank,
    comments (`#`), or missing an `=` are ignored. A tiny replacement for
    python-dotenv so we don't need a third-party dependency.
    """
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            value = value.strip().strip('"').strip("'")
            os.environ.setdefault(key.strip(), value)


class GHLClient:
    """Thin wrapper over the HighLevel v2 REST API.

    Pass a token / location_id explicitly, or leave them out to read
    GHL_PRIVATE_TOKEN and GHL_LOCATION_ID from the environment.
    """

    def __init__(self, token=None, location_id=None):
        self.token = token or os.environ.get("GHL_PRIVATE_TOKEN")
        self.location_id = location_id or os.environ.get("GHL_LOCATION_ID")
        if not self.token:
            raise ValueError(
                "Missing GHL token. Set GHL_PRIVATE_TOKEN in .env or pass token=."
            )
        if not self.location_id:
            raise ValueError(
                "Missing location id. Set GHL_LOCATION_ID in .env or pass location_id=."
            )

    def _request(self, method, path, params=None, body=None):
        url = API_BASE + path
        if params:
            url += "?" + urllib.parse.urlencode(params)

        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Authorization", f"Bearer {self.token}")
        req.add_header("Version", API_VERSION)
        req.add_header("Accept", "application/json")
        # HighLevel sits behind Cloudflare, which blocks the default
        # "Python-urllib/x.y" agent. Send a conventional UA instead.
        req.add_header("User-Agent", "firebreak-ghl/1.0")
        if data is not None:
            req.add_header("Content-Type", "application/json")

        try:
            with urllib.request.urlopen(req) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw) if raw else {}
        except urllib.error.HTTPError as exc:
            raise GHLError(exc.code, exc.read().decode("utf-8")) from exc

    # --- Convenience methods -------------------------------------------------

    def verify(self):
        """Lightweight auth/connectivity check. Returns the raw response."""
        return self._request(
            "GET",
            "/contacts/",
            params={"locationId": self.location_id, "limit": 1},
        )

    def list_contacts(self, limit=20, **filters):
        """List contacts in the configured location."""
        params = {"locationId": self.location_id, "limit": limit}
        params.update(filters)
        return self._request("GET", "/contacts/", params=params)

    def get_contact(self, contact_id):
        """Fetch a single contact by id."""
        return self._request("GET", f"/contacts/{contact_id}")

    def create_contact(self, **fields):
        """Create a contact. e.g. create_contact(firstName='Ada', email='a@b.com')."""
        body = {"locationId": self.location_id}
        body.update(fields)
        return self._request("POST", "/contacts/", body=body)

    def upsert_contact(self, **fields):
        """Create-or-update a contact (deduped by email within the location).

        Idempotent: safe to re-run without creating duplicates.
        """
        body = {"locationId": self.location_id}
        body.update(fields)
        return self._request("POST", "/contacts/upsert", body=body)

    def list_tags(self):
        return self._request("GET", f"/locations/{self.location_id}/tags").get("tags", [])

    def list_custom_fields(self):
        return self._request(
            "GET", f"/locations/{self.location_id}/customFields"
        ).get("customFields", [])

    def create_custom_field(self, name, data_type="TEXT"):
        return self._request(
            "POST",
            f"/locations/{self.location_id}/customFields",
            body={"name": name, "dataType": data_type},
        ).get("customField", {})
