# Models, Gateway, and Runtime Routing

Low-level public-safe runtime routing document.

## Model/provider routing

| Role | Provider | Model | Notes |
|---|---|---|---|
| Primary | openai-codex | gpt-5.5 | Default for Telegram/API/CLI gateway sessions |
| Fallback | copilot | gpt-5.4 | Used when primary fails |
| Optional provider | lmstudio | gemma4unc | http://127.0.0.1:1234/v1 |
| Optional provider | nvidia | meta/llama-3.3-70b-instruct | https://integrate.api.nvidia.com/v1 |
| Optional provider | freekimi | cfbt-kimi | http://127.0.0.1:3271/v1 |
| Optional provider | forge_freekimi | cfbt-kimi | http://127.0.0.1:8081/v1 |
| Optional provider | forge_lmstudio | gemma4unc | http://127.0.0.1:8082/v1 |


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
| Model IDs | `` |
| Chat smoke test | `blocked_or_unavailable: <urlopen error [Errno 111] Connection refused>` |

## Safety routing

- Primary remains OpenAI Codex `gpt-5.5`.
- Copilot remains fallback.
- LM Studio and Free Kimi are optional/experimental providers until they pass reliable smoke tests.
