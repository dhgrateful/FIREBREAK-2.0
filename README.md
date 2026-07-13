# FIREBREAK

GoHighLevel (HighLevel API v2 / LeadConnector) integration.

## Setup

1. Copy the example env file and fill in your credentials:
   ```sh
   cp .env.example .env
   # then edit .env with your Private Integration Token + Location ID
   ```
   Create a Private Integration Token in HighLevel under
   **Settings → Private Integrations**.

2. Verify the connection (no dependencies required — uses the Python stdlib):
   ```sh
   python3 main.py
   ```
   Expected output:
   ```
   ✅ Connected. Location reports N contact(s).
   ```

## Usage

```python
from ghl import GHLClient, load_env

load_env()
client = GHLClient()                       # reads token + location from .env

client.verify()                            # connectivity / auth check
client.list_contacts(limit=20)             # list contacts
client.get_contact("<contact_id>")         # fetch one contact
client.create_contact(firstName="Ada", email="ada@example.com")
```

## Layout

| Path             | Purpose                                              |
| ---------------- | ---------------------------------------------------- |
| `ghl/client.py`  | Stdlib HighLevel v2 client (auth, requests, helpers) |
| `main.py`        | Connection verification entry point                  |
| `.env`           | Secrets (gitignored — never commit)                  |
| `.env.example`   | Template for `.env`                                  |

## Notes

- API base: `https://services.leadconnectorhq.com` with the
  `Version: 2021-07-28` header.
- HighLevel sits behind Cloudflare, which blocks the default
  `Python-urllib` user-agent; the client sends a conventional `User-Agent`.
- **Security:** if a token has been shared in plain text, rotate it in
  HighLevel and put the new value only in `.env`.
