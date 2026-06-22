# Skills Surface

Low-level public-safe view of installed Hermes skill packs and categories. Private/client-specific skills are counted but not fully listed.

## Category counts

| Category | Count |
|---|---:|
| .archive | 11 |
| apple | 6 |
| autonomous-ai-agents | 7 |
| creative | 34 |
| data-science | 2 |
| devops | 9 |
| ecc-imports | 4 |
| email | 2 |
| gaming | 2 |
| github | 11 |
| mcp | 1 |
| media | 7 |
| mlops | 19 |
| note-taking | 4 |
| personal | 5 |
| productivity | 20 |
| red-teaming | 1 |
| research | 13 |
| smart-home | 4 |
| social-media | 2 |
| software-development | 33 |
| uncategorized | 18 |

## Public-safe examples

| Skill | Category | Description |
|---|---|---|
| `strategic-reading` | uncategorized | Read a book, article, transcript, or case study through the lens of a specific strategic problem you |
| `article-enrichment` | uncategorized | Transform raw article text dumps in the brain into structured pages with executive summary, verbatim quotes, key insights, why-it-matters, a |
| `skillpack-check` | uncategorized | / |
| `chrome-extensions` | uncategorized | > |
| `modern-web-guidance` | uncategorized | / |
| `concept-synthesis` | uncategorized | Deduplicate and synthesize raw concept stubs into a tiered intellectual map (T1 Canon to T4 Riff), tracing idea evolution across sources ove |
| `ingest` | uncategorized | Route content to specialized ingestion skills. Detects input type and delegates. |
| `yuanbao` | uncategorized | Yuanbao (元宝) groups: @mention users, query info/members. |
| `maintain` | uncategorized | / |
| `academic-verify` | uncategorized | Verify a research claim or academic citation by tracing it through publication → methodology → raw data → independent replication. Routes th |
| `dogfood` | uncategorized | Exploratory QA of web apps: find bugs, evidence, reports. |
| `perplexity-research` | uncategorized | Brain-augmented web research. Sends brain context about a topic to Perplexity, which searches the web with citations and returns what is NEW |
| `retrieval-reflex` | uncategorized | When/what to retrieve — open the brain page for a salient entity before answering from memory. |
| `brain-pdf` | uncategorized | Generate a publication-quality PDF from a GBrain page or markdown file using Hermes-native Chrome rendering. The brain page remains the sour |
| `openhue` | smart-home | Control Philips Hue lights, scenes, rooms via OpenHue CLI. |
| `home-hvac-diagnostics` | smart-home | Diagnose residential HVAC comfort/airflow problems using sensor data, photos, duct/register checks, and safe homeowner tests. |
| `native-mcp` | mcp | MCP client: connect servers, register tools (stdio/HTTP). |
| `xurl` | social-media | X/Twitter via xurl CLI: post, search, DM, media, v2 API. |
| `kanban-codex-lane` | autonomous-ai-agents | Use when a Hermes Kanban worker wants to run Codex CLI as an isolated implementation lane while Hermes keeps ownership of task lifecycle, re |
| `hermes-agent` | autonomous-ai-agents | Configure, extend, or contribute to Hermes Agent. |
| `coding-agent-clis` | autonomous-ai-agents | Use when delegating software work to an external coding-agent CLI such as Claude Code, Codex, or OpenCode, especially for isolated implement |
| `jupyter-live-kernel` | data-science | Iterative Python via live Jupyter kernel (hamelnb). |
| `[REDACTED]` | .archive | Diagnose and advise on residential HVAC comfort imbalance: hot/cold rooms, upstairs/downstairs temperature splits, duct/register airflow, th |
| `[REDACTED]` | .archive | Operate, publish, protect, troubleshoot, and theme the Hermes Web Dashboard. |
| `[REDACTED]` | .archive | Install, update, run, and verify Node/npm-based CLI tools safely; covers npx vs npm install, Node version pitfalls, and global CLI verificat |
| `hermes-gateway-routing` | .archive | Inspect, configure, and patch Hermes gateway message routing across origin chats, home channels, threads, and approval flows. |
| `[REDACTED]` | .archive | [REDACTED] |
| `n8n-workflow-operations` | .archive | Operate, debug, back up, patch, and verify n8n workflows across Dev/QA/UAT/PreProd/Prod with environment-specific safety gates. |
| `[REDACTED]` | .archive | Publish a locally running web app from a Linux host with systemd, reverse proxying, HTTPS, Cloudflare-aware DNS checks, narrow sudo wrappers |
| `[REDACTED]` | .archive | AudioCraft: MusicGen text-to-music, AudioGen text-to-sound. |
| `simplify-code` | software-development | Parallel 3-agent cleanup of recent code changes. |
| `codebase-recon-debrief` | software-development | Use when working in an unfamiliar or messy codebase and the task requires understanding flows before editing. Enforces briefing, targeted re |
| `ponytail-help` | software-development | > |
| `[REDACTED]` | software-development | Debug Hermes TUI slash commands: Python, gateway, Ink UI. |
| `plan` | software-development | Plan mode: write an actionable markdown plan to .hermes/plans/, no execution. Bite-sized tasks, exact paths, complete code. |
| `[REDACTED]` | software-development | Modify, debug, or extend the s6-overlay supervision tree inside the Hermes Agent Docker image — adding new services, debugging profile gatew |
| `runtime-debuggers` | software-development | Use when debugging running Python or Node processes with breakpoints, stepping, attach flows, or post-mortem inspection rather than ad-hoc l |
| `ponytail-audit` | software-development | > |
| `[REDACTED]` | software-development | Execute plans via delegate_task subagents (2-stage review). |
| `spike` | software-development | Throwaway experiments to validate an idea before build. |

## Operational meaning

- Skills are markdown procedure packs loaded into the agent context when relevant.
- They cover domains such as software development, DevOps, research, media, productivity, ML/MLOps, smart home, and creative generation.
- The public repository documents the skill surface, not private procedural contents or secrets.
