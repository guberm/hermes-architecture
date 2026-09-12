# MCP Servers and Toolsets

Low-level public-safe view of model-facing integration surfaces.

## MCP servers

| Server | Public-safe config |
|---|---|
| `keep-mcp` | `{"command": "~/.hermes/scripts/keep-mcp-server", "args": [], "enabled": true, "connect_timeout": 30, "timeout": 120, "supports_parallel_tool_calls": false, "sampling": {"enabled": false}, "tools": {"include": ["find", "get_note", "create_note", "create_list", "update_note", "add_list_item", "update_` |
| `codegraph` | `{"command": "~/.nvm/versions/node/v22.19.0/bin/codegraph", "args": ["serve", "--mcp"], "timeout": 120, "connect_timeout": 60, "enabled": true}` |
| `gbrain` | `{"url": "http://127.0.0.1:3131/mcp", "headers": {}, "enabled": true, "timeout": 300, "connect_timeout": 60}` |
| `notebooklm` | `{"command": "npx", "args": ["-y", "notebooklm-mcp@latest"], "env": {"NOTEBOOKLM_PROFILE": "standard", "NOTEBOOKLM_DISABLED_TOOLS": "cleanup_data,re_auth", "HEADLESS": "true", "BROWSER_CHANNEL": "chrome", "DISPLAY": ":0", "XDG_RUNTIME_DIR": "/run/user/1000"}, "connect_timeout": 120, "timeout": 600, "` |
| `windows-cua` | `{"command": "~/.local/bin/windows-cua-mcp", "args": [], "connect_timeout": 120, "timeout": 120, "enabled": false}` |
| `monarch` | `{"url": "https://api.monarch.com/mcp", "enabled": false, "auth": "oauth", "timeout": 300, "connect_timeout": 120, "oauth": {"scope": "mcp:read", "redirect_port": 38475, "client_name": "Hermes Agent"}, "tools": {"include": ["GetTransactions", "GetCategories", "GetTags", "GetBusinesses", "GetCreditSco` |
| `cloudflare-api` | `{"url": "https://mcp.cloudflare.com/mcp", "enabled": true, "auth": "oauth", "timeout": 300, "connect_timeout": 300, "oauth": {"redirect_port": 38476, "client_name": "Hermes Agent"}}` |
| `pixelrag` | `{"command": "~/github/pixelrag-mcp/.venv/bin/python", "args": ["~/github/pixelrag-mcp/server.py"], "enabled": true}` |
| `vibe_trading` | `{"command": "~/.hermes/scripts/vibe-trading-mcp", "args": [], "enabled": true, "connect_timeout": 120, "timeout": 300, "tools": {"include": ["list_skills", "load_skill", "backtest", "factor_analysis", "analyze_options", "pattern_recognition", "get_market_data", "get_stock_news", "get_sec_filings", "` |
| `display` | `{"url": "https://api.display.dev/v1/mcp", "headers": {}, "timeout": 180, "connect_timeout": 60, "sampling": {"enabled": false}, "enabled": true}` |
| `open_notebook` | `{"command": "~/.hermes/oss-evals/open-notebook/open-notebook-mcp-wrapper.sh", "enabled": true}` |
| `context7` | `{"url": "https://mcp.context7.com/mcp", "enabled": true}` |
| `gamma` | `{"url": "https://mcp.gamma.app/mcp", "auth": "oauth", "enabled": false, "tools": {"exclude": ["[REDACTED]", "[REDACTED]", "[REDACTED]"]}}` |
| `hugging_face` | `{"url": "https://huggingface.co/mcp", "auth": "oauth", "enabled": false}` |
| `supabase` | `{"url": "https://mcp.supabase.com/mcp", "auth": "oauth", "enabled": false}` |
| `twilio-docs` | `{"url": "https://mcp.twilio.com/docs", "enabled": true}` |
| `twelve-data` | `{"url": "https://mcp.twelvedata.com/mcp", "auth": "oauth", "enabled": true, "tools": {"exclude": ["oauth_login", "auth_status", "oauth_configure", "get_api_usage"]}}` |
| `vercel` | `{"url": "https://mcp.vercel.com", "auth": "oauth", "enabled": true}` |
| `cloudflare` | `{"url": "https://mcp.cloudflare.com/mcp?codemode=false", "auth": "oauth", "tools": {"exclude": ["docs", "*_radar_*", "*_accounts_magic_*", "*_accounts_mnm_*", "*_accounts_cni_*", "*_accounts_teamnet_*", "[REDACTED]", "*_accounts_dlp_*", "*_accounts_devices*", "*_accounts_dex_*", "*_accounts_datasecu` |

## Toolset counts parsed from CLI

| Toolset | Count estimate |
|---|---:|

## Integration contract

- MCP servers expand Hermes with external tool schemas at runtime.
- Toolsets gate high-risk surfaces such as terminal, file editing, browser automation, cron management, Home Assistant, image generation, and TTS.
- Exact tool schemas are runtime-generated and not fully duplicated in the public repo.
