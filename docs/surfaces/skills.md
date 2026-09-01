# Skills Surface

Low-level public-safe view of installed Hermes skill packs and categories. Private/client-specific skills are counted but not fully listed.

## Category counts

| Category | Count |
|---|---:|
| .archive | 11 |
| android | 2 |
| apple | 5 |
| autonomous-ai-agents | 20 |
| creative | 40 |
| data-science | 1 |
| devops | 28 |
| ecc-imports | 4 |
| email | 5 |
| external | 7 |
| gaming | 2 |
| github | 16 |
| mcp | 2 |
| media | 7 |
| mlops | 23 |
| note-taking | 4 |
| operations | 3 |
| personal | 9 |
| productivity | 49 |
| red-teaming | 1 |
| research | 35 |
| security | 4 |
| smart-home | 5 |
| social-media | 2 |
| software-development | 94 |
| uncategorized | 19 |
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
| `evaluating-llms-harness` | mlops | lm-eval-harness: benchmark LLMs (MMLU, GSM8K, etc.). |
| `weights-and-biases` | mlops | W&B: log ML experiments, sweeps, model registry, dashboards. |
| `llama-cpp` | mlops | llama.cpp local GGUF inference + HF Hub model discovery. |
| `obliteratus` | mlops | OBLITERATUS: abliterate LLM refusals (diff-in-means). |
| `outlines` | mlops | Outlines: structured JSON/regex/Pydantic LLM generation. |
| `serving-llms-vllm` | mlops | vLLM: high-throughput LLM serving, OpenAI API, quantization. |
| `qdrant-vector-search` | mlops | High-performance vector similarity search engine for RAG and semantic search. Use when building production RAG systems requiring fast neares |
| `strategic-reading` | uncategorized | Read a book, article, transcript, or case study through the lens of a specific strategic problem you |
| `better-colors` | external | OKLCH color space and color usage for web projects. Convert hex/rgb/hsl to oklch, generate palettes, check contrast, handle gamut boundaries |
| `better-layout` | external | Layout structure for web interfaces, from grouping and alignment to reading order, progressive disclosure, and adaptive breakpoints. Use whe |
| `better-ui` | external | Design engineering principles for making interfaces feel polished. Use when building UI components, reviewing frontend code, implementing an |
| `better-interface` | external | >- |
| `better-typography` | external | Web typography from choosing fonts to spacing, wrapping and accessibility. Use when picking or pairing typefaces, configuring variable fonts |
| `better-accessibility` | external | Accessibility engineering for product interfaces, from focus states and keyboard support to ARIA, forms, and screen readers. Use when buildi |
| `better-writing` | external | >- |
| `gif-search` | media | Search/download GIFs from Tenor via curl + jq. |
| `video-analysis` | media | Use when analyzing an explicitly supplied local video file. |
| `spotify` | media | Spotify: play, search, queue, manage playlists and devices. |
| `youtube-content` | media | YouTube transcripts to summaries, threads, blogs. |
| `article-enrichment` | uncategorized | Transform raw article text dumps in the brain into structured pages with executive summary, verbatim quotes, key insights, why-it-matters, a |
| `grounded-citations` | research | Ground answers and documents in cited, verifiable sources. |
| `osint-investigation` | research | Public-records OSINT investigation framework — SEC EDGAR filings, USAspending contracts, Senate lobbying, OFAC sanctions, ICIJ offshore leak |
| `domain-intel` | research | Passive domain reconnaissance using Python stdlib. Subdomain discovery, SSL certificate inspection, WHOIS lookups, DNS records, domain avail |
| `[REDACTED]` | research | Evaluate agent memory systems locally before adopting cloud memory vendors like Synap, Mem0, Zep, or Supermemory. |
| `llm-wiki` | research | Karpathy |
| `pixelrag-mcp-operations` | research | Operate and harden a local PixelRAG MCP wrapper for Hermes without exposing dangerous long-lived serve helpers through the gateway. |
| `blogwatcher` | research | Monitor blogs and RSS/Atom feeds via blogwatcher-cli tool. |
| `[REDACTED]` | research | Evidence-first evaluation of third-party model releases, quantizations, conversions, altered-safety variants, and gated model repositories b |
| `[REDACTED]` | research | Evaluate whether a third-party service or product is trustworthy, integrable, and compliant enough for automation, purchasing, or review for |

## Operational meaning

- Skills are markdown procedure packs loaded into the agent context when relevant.
- They cover domains such as software development, DevOps, research, media, productivity, ML/MLOps, smart home, and creative generation.
- The public repository documents the skill surface, not private procedural contents or secrets.
