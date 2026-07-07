# Hermes Agent Architecture

> Public-safe architecture snapshot generated at `2026-07-07T06:15:47-04:00`.
>
> Source of truth: local Hermes configuration and runtime status on the operator Linux host.
>
> Sensitive values, private chat IDs, OAuth headers, personal finance/client workflow names, and tokens are intentionally omitted or grouped.

## Executive Summary

Hermes Agent runs as a **Linux-primary, multi-platform AI operations hub**. The gateway is a systemd service that connects Telegram, Mattermost, WhatsApp, API Server, Home Assistant, MCP servers, cron jobs, skills, memory/context stores, and remote Windows operations.

The current architecture adds a **durable Kanban orchestration layer**: `default` remains the interactive/orchestrator profile, while `researcher`, `worker`, and `reviewer` are launched as ephemeral Kanban worker-runs for durable research, implementation, and verification tasks. Safe post-session automation generates local review artifacts (session summaries, skill-mining candidates, trace-derived code graphs) without silently installing skills or uploading traces.

The default model remains **`openai-codex / gpt-5.5`**. Local/experimental providers such as **LM Studio** and **Free Kimi** are configured as optional providers only; they are not the default route for Telegram or production workflows.

## High-Level Architecture

![Hermes Architecture](docs/hermes-architecture.svg)

## Runtime Topology

| Layer | Components | Notes |
|---|---|---|
| User channels | Telegram, Mattermost, WhatsApp, API Server | Gateway adapters route inbound messages into the same Hermes agent core. |
| Agent core | Hermes Agent gateway + CLI + tool loop | Runs on Linux under `hermes-gateway.service`. |
| Models | OpenAI Codex primary, Copilot fallback, optional LM Studio, optional Free Kimi proxy | Provider selection is explicit; experimental endpoints are not default. |
| Tools | Terminal, files, browser, web, vision, TTS, cron, delegation, Home Assistant, GBrain, NotebookLM, CodeGraph | Enabled toolsets differ by platform/session but the gateway exposes the main operational surface. |
| Knowledge | GBrain, NotebookLM, session search, imported Claude context, skills | Long-term memory and research context are split across structured stores and markdown skills. |
| Automation | Hermes cron scheduler, no-agent scripts, hooks, plugins, post-session automation | Backups, monitoring, GitHub publication, finance snapshots, smart-home logging, news/media digests, watchdogs, session summaries, skill-mining reviews, and trace graphs. |
| Durable orchestration | Kanban dispatcher + `default`/`researcher`/`worker`/`reviewer` profiles | The gateway dispatcher claims ready tasks and launches profile-specific worker-runs; `stopped` profiles are normal idle state. |
| Operational surfaces | Tasks, skills, rules, hooks, plugins, MCP servers, toolsets | Documented as public-safe counts/categories plus selected non-sensitive examples. |
| Remote systems | Windows workstation over SSH, Home Assistant, Google Drive/GitHub, local LM Studio | Linux remains the control plane; Windows is operated remotely when needed. |

## Operational Surface Inventory

| Surface | Detected public-safe state | Notes |
|---|---|---|
| Scheduled tasks / cron | 49 jobs; 28 no-agent script jobs; 0 agent-backed jobs | Exact private task names are grouped by category. |
| Skills | 266 detected skill files across 24 categories | Private/client-sensitive skill names are omitted from examples. |
| Hooks / webhooks | shell allowlist present: False; allowlist entries: 0; plugin hook manifests: 27 | Hook command bodies are not published. |
| Plugins | 77 visible plugin rows captured; enabled estimate 5 | Descriptions omitted to avoid leaking credential/env surfaces. |
| MCP servers | 11 configured MCP servers | GBrain, NotebookLM, CodeGraph are the active core MCP surfaces. |


### Scheduled tasks / cron categories

| Category | Active jobs | Public-safe purpose |
|---|---:|---|
| Backup & sync | 5 | Protect configuration, repositories, databases, and knowledge stores. |
| GitHub & publishing | 6 | Maintain GitHub/publication surfaces and repo health digests. |
| Home automation | 2 | Log smart-home/home-environment telemetry. |
| Knowledge & memory | 7 | Keep GBrain/memory/context stores healthy and up to date. |
| Media/news monitoring | 3 | News, RSS, YouTube, and briefing pipelines. |
| Other scheduled automation | 12 | Other local automation jobs. |
| Private finance automation | 5 | Private finance workflow snapshots; details omitted from public docs. |
| Reliability watchdogs | 9 | Auto-healing, environment guards, timeout/watchdog checks. |


### Skills surface

Hermes currently has a broad skill surface. The public inventory lists category counts and non-sensitive examples only.

| Skill category | Count |
|---|---:|
| .archive | 11 |
| apple | 5 |
| autonomous-ai-agents | 12 |
| creative | 37 |
| data-science | 2 |
| devops | 9 |
| ecc-imports | 4 |
| email | 3 |
| gaming | 2 |
| github | 14 |
| mcp | 2 |
| media | 7 |
| mlops | 24 |
| note-taking | 4 |
| personal | 8 |
| productivity | 26 |
| red-teaming | 1 |
| research | 20 |
| security | 2 |
| smart-home | 5 |
| social-media | 2 |
| software-development | 44 |
| uncategorized | 21 |
| web-development | 1 |


Public-safe skill examples:

| Skill | Category | Public-safe description |
|---|---|---|
| `dspy` | mlops | DSPy: declarative LM programs, auto-optimize prompts, RAG. |
| `fine-tuning-with-trl` | mlops | TRL: SFT, DPO, PPO, GRPO, reward modeling for LLM RLHF. |
| `axolotl` | mlops | Axolotl: YAML LLM fine-tuning (LoRA, DPO, GRPO). |
| `unsloth` | mlops | Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM. |
| `instructor` | mlops | Extract structured data from LLM responses with Pydantic validation, retry failed extractions automatically, parse complex JSON with type sa |
| `nemo-curator` | mlops | GPU-accelerated data curation for LLM training. Supports text/image/video/audio. Features fuzzy deduplication (16× faster), quality filterin |
| `huggingface-hub` | mlops | HuggingFace hf CLI: search/download/upload models, datasets. |
| `segment-anything-model` | mlops | SAM: zero-shot image segmentation via points, boxes, masks. |
| `chroma` | mlops | Open-source embedding database for AI applications. Store embeddings and metadata, perform vector and full-text search, filter by metadata.  |
| `faiss` | mlops | Facebook |
| `weights-and-biases` | mlops | W&B: log ML experiments, sweeps, model registry, dashboards. |
| `evaluating-llms-harness` | mlops | lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.). |
| `llama-cpp` | mlops | llama.cpp local GGUF inference + HF Hub model discovery. |
| `obliteratus` | mlops | OBLITERATUS: abliterate LLM refusals (diff-in-means). |
| `serving-llms-vllm` | mlops | vLLM: high-throughput LLM serving, OpenAI API, quantization. |
| `outlines` | mlops | Outlines: structured JSON/regex/Pydantic LLM generation. |
| `qdrant-vector-search` | mlops | High-performance vector similarity search engine for RAG and semantic search. Use when building production RAG systems requiring fast neares |
| `strategic-reading` | uncategorized | Read a book, article, transcript, or case study through the lens of a specific strategic problem you |
| `gif-search` | media | Search/download GIFs from Tenor via curl + jq. |
| `spotify` | media | Spotify: play, search, queue, manage playlists and devices. |
| `youtube-content` | media | YouTube transcripts to summaries, threads, blogs. |
| `article-enrichment` | uncategorized | Transform raw article text dumps in the brain into structured pages with executive summary, verbatim quotes, key insights, why-it-matters, a |
| `osint-investigation` | research | Public-records OSINT investigation framework — SEC EDGAR filings, USAspending contracts, Senate lobbying, OFAC sanctions, ICIJ offshore leak |
| `domain-intel` | research | Passive domain reconnaissance using Python stdlib. Subdomain discovery, SSL certificate inspection, WHOIS lookups, DNS records, domain avail |
| `[REDACTED]` | research | Evaluate agent memory systems locally before adopting cloud memory vendors like Synap, Mem0, Zep, or Supermemory. |


### Hooks, webhooks, and plugin hook manifests

Hermes has multiple hook-related surfaces: shell-hook allowlists, webhook subscriptions, and imported Claude/Claude plugin hook manifests. The public repo records only surface/count information, not hook command bodies.

| Hook manifest surface |
|---|
| `.hermes/oss-evals/2026-06-26/orca-sandbox/home/.gemini/config/hooks.json` |
| `.hermes/oss-evals/2026-06-26/orca-sandbox/home/.cursor/hooks.json` |
| `.hermes/oss-evals/2026-06-26/orca-sandbox/config/orca/codex-runtime-home/home/hooks.json` |
| `.hermes/hermes-agent/.codex/hooks.json` |
| `.claude/plugins/marketplaces/thedotmack/plugin/hooks/hooks.json` |
| `.claude/plugins/marketplaces/thedotmack/cursor-hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-plugins-official/plugins/learning-output-style/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-plugins-official/plugins/security-guidance/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-plugins-official/plugins/hookify/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-plugins-official/plugins/ralph-loop/hooks/hooks.json` |
| `[REDACTED]` |
| `.claude/plugins/marketplaces/claude-code-warp/plugins/warp/hooks/hooks.json` |
| `.claude/plugins/marketplaces/headroom-marketplace/plugins/headroom-agent-hooks/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-code-plugins/plugins/learning-output-style/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-code-plugins/plugins/security-guidance/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-code-plugins/plugins/hookify/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-code-plugins/plugins/ralph-wiggum/hooks/hooks.json` |
| `[REDACTED]` |
| `.claude/plugins/marketplaces/ponytail/hooks/hooks.json` |
| `.claude/plugins/cache/thedotmack/claude-mem/13.10.1/hooks/hooks.json` |


### Plugin surface

| Plugin | Status |
|---|---|
| `browser-browser-use` | not enabled |
| `browser-browserbase` | not enabled |
| `browser-firecrawl` | not enabled |
| `chronos` | not enabled |
| `basic` | not enabled |
| `drain` | not enabled |
| `nous` | not enabled |
| `self-hosted` | not enabled |
| `disk-cleanup` | not enabled |
| `google_meet` | not enabled |
| `fal` | not enabled |
| `krea` | not enabled |
| `openai` | not enabled |
| `openai-codex` | not enabled |
| `openrouter` | not enabled |
| `xai` | not enabled |
| `alibaba-provider` | not enabled |
| `anthropic-provider` | not enabled |
| `arcee-provider` | not enabled |
| `bedrock-provider` | not enabled |
| `copilot-provider` | not enabled |
| `copilot-acp-provider` | not enabled |
| `custom-provider` | not enabled |
| `deepseek-provider` | not enabled |
| `gemini-provider` | not enabled |
| `gmi-provider` | not enabled |
| `huggingface-provider` | not enabled |
| `kilocode-provider` | not enabled |
| `kimi-coding-provider` | not enabled |
| `minimax-provider` | not enabled |


## Low-Level Surface Files

The repository includes dedicated, low-level public-safe files for each operational surface:

| File | Contents |
|---|---|
| [`docs/surfaces/tasks.md`](docs/surfaces/tasks.md) | Scheduled tasks/cron jobs, modes, scripts, schedules, delivery class, workdir class. |
| [`docs/surfaces/skills.md`](docs/surfaces/skills.md) | Skill categories, counts, public-safe examples, operational semantics. |
| [`docs/surfaces/hooks.md`](docs/surfaces/hooks.md) | Shell hook allowlist state, webhook state, plugin hook manifests. |
| [`docs/surfaces/plugins.md`](docs/surfaces/plugins.md) | Hermes plugin registry rows and status. |
| [`docs/surfaces/mcp-and-toolsets.md`](docs/surfaces/mcp-and-toolsets.md) | MCP servers and toolset count estimates. |
| [`docs/surfaces/models-and-gateway.md`](docs/surfaces/models-and-gateway.md) | Model routing, gateway status, channel/platform surface. |
| [`docs/surfaces/orchestration.md`](docs/surfaces/orchestration.md) | Kanban profiles, rules layer, self-improvement automation, and operating contract. |

## Model Routing

| Role | Provider | Model | Notes |
|---|---|---|---|
| Primary | github-copilot | gpt-5.5 | Default for Telegram/API/CLI gateway sessions |
| Fallback | copilot | gpt-5.5 | Used when primary fails |
| Optional provider | lmstudio | gemma4unc | http://127.0.0.1:1234/v1 |
| Optional provider | nvidia | meta/llama-3.3-70b-instruct | https://integrate.api.nvidia.com/v1 |
| Optional provider | freekimi | cfbt-kimi | http://127.0.0.1:3271/v1 |
| Optional provider | forge_freekimi | cfbt-kimi | http://127.0.0.1:8081/v1 |
| Optional provider | forge_lmstudio | gemma4unc | http://127.0.0.1:8082/v1 |
| Optional provider | chatgpt_web | chatgpt-5.5-high-web | https://codex.guber.dev/v1 |


### Local model trial status

| Item | Status |
|---|---|
| LM Studio endpoint | `available` at `http://127.0.0.1:1234/v1` |
| Reported model IDs | `qwenvl3bunc, mythosnanoq6, qwythos9bq5, gemma4coderq3, gemma4coderq4, oymuncq4, [REDACTED], gemma4unc, [REDACTED]` |
| Chat smoke test | `blocked_or_unavailable: {
"error": {
    "message": "Failed to load model \"gemma4unc\". Error: Model loading was stopped due to insufficient system resources. Under the current settings, this model requires approximately 14.36 GB of memory, and continuing` |
| Safety decision | Main Hermes remains `openai-codex/gpt-5.5`; local provider is optional until a model can load reliably. |

## MCP and External Tooling

| MCP server | Transport | Public-safe purpose |
|---|---|---|
| `gbrain` | Local HTTP MCP on `127.0.0.1:3131/mcp` | Personal knowledge graph, memory, code graph, facts, schema tools. |
| `notebooklm` | `npx notebooklm-mcp@latest` | Grounded research over registered Google NotebookLM notebooks. |
| `codegraph` | Local Node command | Code intelligence over selected repositories. |

## Scheduled Automation

| Category | Active jobs | Public-safe purpose |
|---|---:|---|
| Backup & sync | 5 | Protect configuration, repositories, databases, and knowledge stores. |
| GitHub & publishing | 6 | Maintain GitHub/publication surfaces and repo health digests. |
| Home automation | 2 | Log smart-home/home-environment telemetry. |
| Knowledge & memory | 7 | Keep GBrain/memory/context stores healthy and up to date. |
| Media/news monitoring | 3 | News, RSS, YouTube, and briefing pipelines. |
| Other scheduled automation | 12 | Other local automation jobs. |
| Private finance automation | 5 | Private finance workflow snapshots; details omitted from public docs. |
| Reliability watchdogs | 9 | Auto-healing, environment guards, timeout/watchdog checks. |


## Agentic Operating Model

| Item | Value | Meaning |
|---|---|---|
| Interactive orchestrator | `default` | Main Telegram/API/CLI profile; decides whether to answer directly, delegate, create Kanban work, or schedule cron. |
| Research lane | `researcher` | Evidence-backed OSS/docs/web due diligence and adoption recommendations. |
| Execution lane | `worker` | File/terminal/code/config implementation and verification for durable work items. |
| Review lane | `reviewer` | Independent review, regression checks, security/config sanity, and final validation. |
| Default assignee | `worker` | Fallback when a task/decomposer does not choose a specialist. |
| Failure limit | `5` | Raised above the previous aggressive default to avoid noisy retry failures. |
| Per-profile concurrency | `1` | Keeps one profile from saturating model/API/browser capacity. |
| Post-session automation | `enabled` | Generates review artifacts only; does not auto-install remote skills or mutate active prompts. |


The important runtime distinction is that `researcher`, `worker`, and `reviewer` do **not** need to be continuously running gateway profiles. They are idle until a Kanban task is assigned to them; then the gateway dispatcher starts a worker-run for that profile and the worker completes, blocks, or retries the task.

## Current Profiles

The live system currently exposes the public-safe profile roster as:

```text
Profile          Model                        Gateway      Alias        Distribution
 ───────────────    ───────────────────────────    ───────────    ───────────    ────────────────────
 ◆default         gpt-5.5                      running      —            —
  claude          gpt-5.5                      stopped      hermes-claude —
  coding          github-copilot/gpt-5.5       stopped      coding       —
  researcher      gpt-5.5                      stopped      hermes-researcher —
  reviewer        gpt-5.5                      stopped      hermes-reviewer —
  security-restricted gpt-5.5                      stopped      hermes-security —
  worker          gpt-5.5                      stopped      hermes-worker —
```

Current profile contract:

| Profile | Role | Runtime behavior |
|---|---|---|
| `default` | Interactive orchestrator | Stays running in Telegram/API/CLI gateway; routes work. |
| `researcher` | Research/due-diligence worker | Normally stopped; launched by Kanban for evidence gathering. |
| `worker` | Implementation/execution worker | Normally stopped; fallback assignee for durable tasks. |
| `reviewer` | Independent verification worker | Normally stopped; launched for review/regression/security checks. |

## Reliability and Safety Boundaries

- Public repo does **not** publish secrets, chat IDs, API keys, OAuth tokens, cookies, private finance details, or client-specific payloads.
- The gateway is supervised by systemd and multiple watchdog cron jobs.
- GBrain runs through a shared local HTTP MCP server to avoid PGLite lock contention.
- Backups and sync jobs run through cron with Google Drive/GitHub targets.
- Windows is treated as a remote worker controlled via SSH, not as the primary Hermes control plane.
- Experimental providers are explicitly optional and must pass direct API + Hermes smoke tests before being used for real agent work.

## Operational Notes

- Hermes version/status summary:

```text
Hermes Agent v0.18.0 (2026.7.1) · upstream 83016547 · local a8dca0b8 (+1 carried commit)
Project: ~/.hermes/hermes-agent
Python: 3.11.15
OpenAI SDK: 2.24.0
Update available: 57 commits behind — run 'hermes update'
```

- Fallback chain:

```text
Primary:   gpt-5.5  (via github-copilot)

  Fallback chain (1 entry):
1. gpt-5.5  (via copilot)

  Tried in order when the primary fails (rate-limit, 5xx, connection errors).
  Docs: https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers
```

- MCP list:

```text
MCP Servers:

  Name             Transport                      Tools        Status    
  ──────────────── ────────────────────────────── ──────────── ──────────
  codegraph        ~/.nvm/versions/no...   all          ✓ enabled
  gbrain           http://127.0.0.1:3131/mcp      all          ✓ enabled
  notebooklm       npx -y notebooklm-mcp@latest   all          ✓ enabled
  homeway          https://homeway.io/api/mcp     all          ✓ enabled
  windows-cua      ~/.local/bin/windo...   all          ✓ enabled
  monarch          https://api.monarch.com/mcp    17 selected  ✓ enabled
  cloudflare-api   https://mcp.cloudflare.co...   all          ✓ enabled
  pixelrag         ~/github/pixelrag-...   all          ✓ enabled
  vibe_trading     ~/.hermes/scripts/...   29 selected  ✓ enabled
  display          https://api.display.dev/v...   all          ✓ enabled
  open_notebook    ~/.hermes/oss-eval...   all          ✓ enabled
```

## Maintenance

This repository is regenerated by `scripts/update_architecture.py`. The updater is designed to be safe for a public repository:

1. collect local Hermes runtime state,
2. redact secrets and private identifiers,
3. group sensitive scheduled jobs by category,
4. regenerate Markdown, SVG, HTML, JSON inventory, and PDF,
5. commit and push only if files changed.

## Source Files

- `ARCHITECTURE.md` - canonical public architecture document.
- `docs/hermes-architecture.svg` - standalone diagram.
- `docs/hermes-architecture.html` - browser-friendly diagram page.
- `docs/Hermes-Architecture.pdf` - rendered PDF copy.
- `docs/surfaces/*.md` - low-level public-safe inventories for tasks, skills, hooks, plugins, MCP/toolsets, and gateway/model routing.
- `data/inventory.public.json` - redacted machine-readable snapshot.
- `scripts/update_architecture.py` - public-safe regeneration script.
