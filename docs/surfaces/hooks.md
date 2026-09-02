# Hooks, Webhooks, and Hook Manifests

Public-safe low-level inventory of hook surfaces. Hook command bodies and private runtime payloads are not published.

| Surface | Value |
|---|---|
| Shell hooks allowlist present | False |
| Shell hooks allowlist entries | 0 |
| Plugin hook manifests detected | 22 |
| Webhook summary | webhook platform not enabled |

## Hook manifest paths

| Relative path |
|---|
| `.claude/plugins/marketplaces/thedotmack/plugin/hooks/hooks.json` |
| `.claude/plugins/marketplaces/thedotmack/cursor-hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-plugins-official/plugins/learning-output-style/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-plugins-official/plugins/security-guidance/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-plugins-official/plugins/hookify/hooks/hooks.json` |
| `.claude/plugins/marketplaces/claude-plugins-official/plugins/claude-security/hooks/hooks.json` |
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
| `.claude/plugins/cache/thedotmack/claude-mem/13.13.0/hooks/hooks.json` |
| `.claude/plugins/cache/claude-plugins-official/superpowers/6.1.1/hooks/hooks.json` |
| `.claude/plugins/cache/claude-plugins-official/superpowers/6.2.0/hooks/hooks.json` |
| `.claude/plugins/cache/claude-code-warp/warp/2.0.0/hooks/hooks.json` |
| `.claude/plugins/cache/headroom-marketplace/headroom/0.22.3/hooks/hooks.json` |
| `.claude/plugins/cache/ponytail/ponytail/4.6.0/hooks/hooks.json` |

## Boundaries

- Hook manifest paths are published to document extension points.
- Hook bodies, command lines, environment variables, tokens, and private payloads are intentionally excluded.
