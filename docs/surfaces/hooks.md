# Hooks, Webhooks, and Hook Manifests

Public-safe low-level inventory of hook surfaces. Hook command bodies and private runtime payloads are not published.

| Surface | Value |
|---|---|
| Shell hooks allowlist present | False |
| Shell hooks allowlist entries | 0 |
| Plugin hook manifests detected | 30 |
| Webhook summary | webhook platform not enabled |

## Hook manifest paths

| Relative path |
|---|
| `.hermes/oss-evals/2026-06-26/orca-sandbox/home/.gemini/config/hooks.json` |
| `.hermes/oss-evals/2026-06-26/orca-sandbox/home/.cursor/hooks.json` |
| `.hermes/oss-evals/2026-06-26/orca-sandbox/config/orca/codex-runtime-home/home/hooks.json` |
| `.hermes/oss-evals/agent-orchestrators/2026-07-13/wit/hooks/hooks.json` |
| `.hermes/hermes-agent.pre-v2026.7.7-20260707_215257_EDT/.codex/hooks.json` |
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
| `.claude/plugins/cache/thedotmack/claude-mem/13.2.0/hooks/hooks.json` |
| `.claude/plugins/cache/thedotmack/claude-mem/13.11.0/hooks/hooks.json` |
| `.claude/plugins/cache/thedotmack/claude-mem/13.4.0/hooks/hooks.json` |
| `.claude/plugins/cache/thedotmack/claude-mem/13.3.0/hooks/hooks.json` |
| `.claude/plugins/cache/thedotmack/claude-mem/13.4.1/hooks/hooks.json` |
| `.claude/plugins/cache/claude-plugins-official/superpowers/d884ae04edeb/hooks/hooks.json` |
| `.claude/plugins/cache/claude-code-warp/warp/2.0.0/hooks/hooks.json` |
| `.claude/plugins/cache/headroom-marketplace/headroom/0.22.3/hooks/hooks.json` |
| `.claude/plugins/cache/ponytail/ponytail/4.6.0/hooks/hooks.json` |

## Boundaries

- Hook manifest paths are published to document extension points.
- Hook bodies, command lines, environment variables, tokens, and private payloads are intentionally excluded.
