# Models, Gateway, and Runtime Routing

Low-level public-safe runtime routing document.

## Model/provider routing

| Role | Provider | Model | Notes |
|---|---|---|---|
| Primary |  |  | Default for Telegram/API/CLI gateway sessions |
| Fallback |  |  | Used when primary fails |


## Gateway

| Item | Value |
|---|---|
| Service | `hermes-gateway.service` |
| Running | `True` |
| Platforms | `api_server, homeassistant, mattermost, telegram, whatsapp` |

## Local model status

| Item | Value |
|---|---|
| LM Studio base URL | `http://127.0.0.1:1234/v1` |
| Model IDs | `mythosnanoq6, qwythos9bq5, gemma4coderq3, gemma4coderq4, oymuncq4, [REDACTED], gemma4unc, [REDACTED]` |
| Chat smoke test | `blocked_or_unavailable: {     "error": {         "message": "Failed to load model \"gemma4unc\". Error: Model loading was stopped due to insufficient system resources. Under the current settings, this model requires approximately 14.36 GB of memory, and continuing` |

## Safety routing

- Primary remains OpenAI Codex `gpt-5.5`.
- Copilot remains fallback.
- LM Studio and Free Kimi are optional/experimental providers until they pass reliable smoke tests.
