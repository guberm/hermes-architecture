# MCP Servers and Toolsets

Low-level public-safe view of model-facing integration surfaces.

## MCP servers

| Server | Public-safe config |
|---|---|
| `codegraph` | `{"command": "~/.nvm/versions/node/v22.19.0/bin/codegraph", "args": ["serve", "--mcp"], "timeout": 120, "connect_timeout": 60, "enabled": true}` |
| `gbrain` | `{"url": "http://127.0.0.1:3131/mcp", "headers": {}, "enabled": true, "timeout": 300, "connect_timeout": 60}` |
| `notebooklm` | `{"command": "npx", "args": ["-y", "notebooklm-mcp@latest"], "env": {"NOTEBOOKLM_PROFILE": "standard", "NOTEBOOKLM_DISABLED_TOOLS": "cleanup_data,re_auth", "HEADLESS": "true", "BROWSER_CHANNEL": "chrome", "DISPLAY": ":0", "XDG_RUNTIME_DIR": "/run/user/1000"}, "connect_timeout": 120, "timeout": 600, "` |
| `windows-cua` | `{"command": "~/.local/bin/windows-cua-mcp", "args": [], "connect_timeout": 120, "timeout": 120, "enabled": true}` |
| `monarch` | `{"url": "https://api.monarch.com/mcp", "enabled": true, "auth": "oauth", "timeout": 300, "connect_timeout": 120, "oauth": {"scope": "mcp:read", "redirect_port": 38475, "client_name": "Hermes Agent"}, "tools": {"include": ["GetTransactions", "GetCategories", "GetTags", "GetBusinesses", "GetCreditScor` |
| `cloudflare-api` | `{"url": "https://mcp.cloudflare.com/mcp", "enabled": true, "auth": "oauth", "timeout": 300, "connect_timeout": 300, "oauth": {"redirect_port": 38476, "client_name": "Hermes Agent"}}` |
| `pixelrag` | `{"command": "~/github/pixelrag-mcp/.venv/bin/python", "args": ["~/github/pixelrag-mcp/server.py"], "enabled": true}` |
| `vibe_trading` | `{"command": "~/.hermes/scripts/vibe-trading-mcp", "args": [], "enabled": true, "connect_timeout": 120, "timeout": 300, "tools": {"include": ["list_skills", "load_skill", "backtest", "factor_analysis", "analyze_options", "pattern_recognition", "get_market_data", "get_stock_news", "get_sec_filings", "` |
| `display` | `{"url": "https://api.display.dev/v1/mcp", "headers": {}, "timeout": 180, "connect_timeout": 60, "sampling": {"enabled": false}, "enabled": true}` |
| `open_notebook` | `{"command": "~/.hermes/oss-evals/open-notebook/open-notebook-mcp-wrapper.sh", "enabled": true}` |

## Toolset counts parsed from CLI

| Toolset | Count estimate |
|---|---:|

## Integration contract

- MCP servers expand Hermes with external tool schemas at runtime.
- Toolsets gate high-risk surfaces such as terminal, file editing, browser automation, cron management, Home Assistant, image generation, and TTS.
- Exact tool schemas are runtime-generated and not fully duplicated in the public repo.
