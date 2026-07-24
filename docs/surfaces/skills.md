# Skills Surface

Low-level public-safe view of installed Hermes skill packs and categories. Private/client-specific skills are counted but not fully listed.

## Category counts

| Category | Count |
|---|---:|
| .archive | 11 |
| android | 2 |
| apple | 5 |
| autonomous-ai-agents | 15 |
| creative | 38 |
| data-science | 2 |
| devops | 20 |
| ecc-imports | 4 |
| email | 3 |
| gaming | 2 |
| github | 14 |
| mcp | 2 |
| media | 7 |
| mlops | 25 |
| note-taking | 4 |
| personal | 9 |
| productivity | 34 |
| red-teaming | 1 |
| research | 27 |
| security | 3 |
| smart-home | 5 |
| social-media | 2 |
| software-development | 66 |
| uncategorized | 23 |
| web-development | 1 |

## Public-safe examples

| Skill | Category | Description |
|---|---|---|
| `dspy` | mlops | DSPy: declarative LM programs, auto-optimize prompts, RAG. |
| `fine-tuning-with-trl` | mlops | TRL: SFT, DPO, PPO, GRPO, reward modeling for LLM RLHF. |
| `axolotl` | mlops | Axolotl: YAML LLM fine-tuning (LoRA, DPO, GRPO). |
| `unsloth` | mlops | Unsloth: 2-5x faster LoRA/QLoRA fine-tuning, less VRAM. |
| `instructor` | mlops | Extract structured data from LLM responses with Pydantic validation, retry failed extractions automatically, parse complex JSON with type sa |
| `nemo-curator` | mlops | GPU-accelerated data curation for LLM training. Supports text/image/video/audio. Features fuzzy deduplication (16× faster), quality filterin |
| `huggingface-hub` | mlops | HuggingFace hf CLI: search/download/upload models, datasets. |
| `segment-anything-model` | mlops | SAM: zero-shot image segmentation via points, boxes, masks. |
| `chroma` | mlops | Open-source embedding database for AI applications. Store embeddings and metadata, perform vector and full-text search, filter by metadata. |
| `faiss` | mlops | Facebook |
| `[REDACTED]` | mlops | Evidence-first evaluation of local LLM recommendations against the user |
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
| `llm-wiki` | research | Karpathy |
| `pixelrag-mcp-operations` | research | Operate and harden a local PixelRAG MCP wrapper for Hermes without exposing dangerous long-lived serve helpers through the gateway. |
| `blogwatcher` | research | Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool. |
| `[REDACTED]` | research | Evidence-first evaluation of third-party model releases, quantizations, conversions, altered-safety variants, and gated model repositories b |
| `[REDACTED]` | research | Evaluate whether a third-party service or product is trustworthy, integrable, and compliant enough for automation, purchasing, or review for |
| `[REDACTED]` | research | Operate the academic research workflow from paper discovery through experiment-backed writing and submission. |
| `[REDACTED]` | research | Evidence-first review of technical articles, architecture case studies, and bare blog links—especially when no public implementation artifac |
| `darwinian-evolver` | research | Evolve prompts/regex/SQL/code with Imbue |
| `[REDACTED]` | research | Calibrate and safely relax LLM editorial-admissibility gates in automated news pipelines when valid event reports are rejected as opinion, r |
| `[REDACTED]` | research | Evaluate desktop AI-agent applications that edit files, run commands, use local/remote/cloud models, or overlap with Hermes. Use for product |
| `[REDACTED]` | research | Diagnose inaccessible public websites, login portals, and SPAs by separating DNS, network, TLS, HTTP routing, static-app loading, browser ex |
| `polymarket` | research | Query Polymarket: markets, prices, orderbooks, history. |
| `[REDACTED]` | research | Evidence-first privacy and adoption review for desktop apps claiming fully local processing of sensitive data. |
| `[REDACTED]` | research | Evaluate and tune news-selection gates for both precision and recall. Use when a digest feels too short, a classifier rejects too much, edit |

## Operational meaning

- Skills are markdown procedure packs loaded into the agent context when relevant.
- They cover domains such as software development, DevOps, research, media, productivity, ML/MLOps, smart home, and creative generation.
- The public repository documents the skill surface, not private procedural contents or secrets.
