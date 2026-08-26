# Scheduled Tasks and Cron Jobs

Public-safe low-level inventory of Hermes scheduled automation. Private/client-sensitive names are grouped, but schedules, execution modes, scripts, and workdirs are retained when safe.

| Task | Category | Schedule | Mode | Script | Delivery | Workdir | Last run |
|---|---|---|---|---|---|---|---|
| Daily Hermes Backup | Backup & sync | 0 3 * * * | no-agent (script stdout delivered directly) | daily_hermes_backup.sh | configured private channel | ~ | 2026-08-26T03:01:25.951577-04:00  ok |
| Daily DB SQLite Google Drive Backup | Backup & sync | 30 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-26T04:32:00.274393-04:00  ok |
| github-health-digest | GitHub & publishing | 0 9 * * 1-5 | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-25T09:46:34.400183-04:00  ok |
| Check Windows nightly cleanup logs | Other scheduled automation | 15 2 * * * |  |  | configured private channel |  | 2026-08-26T02:18:04.729459-04:00  ok |
| world-update-brief | Media/news monitoring | 0 7,19 * * * |  |  | configured private channel | ~/.hermes/scripts | 2026-08-25T23:05:22.301561-04:00  ok |
| [Backup & sync task] | Backup & sync | every 180m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-08-26T05:57:50.286842-04:00  ok |
| [GitHub & publishing task] | GitHub & publishing | every 1440m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-08-25T10:23:31.751107-04:00  ok |
| Weekly deep memory cleanup | Knowledge & memory | 0 5 * * 0 |  |  | configured private channel |  | 2026-08-23T05:11:36.740185-04:00  error: RuntimeError: HTTP 429: Hold up for a bit, you've exceeded the rate limit on your API key. |
| Daily GBrain Google Drive Backup | Backup & sync | 45 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-26T04:45:37.546540-04:00  ok |
| Daily RSS Bot Stats Report | GitHub & publishing | 0 8 * * * | no-agent (script stdout delivered directly) | rss_bot_daily_report.py | configured private channel |  | 2026-08-25T08:01:16.429808-04:00  ok |
| SwitchBot Meter Pro hourly Google Sheet logger | Home automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-26T06:03:52.860725-04:00  ok |
| Home Assistant filtered 3-hour Google Sheet logger | Home automation | every 180m | no-agent (script stdout delivered directly) | ha_entities_to_sheets.py | configured private channel |  | 2026-08-26T05:58:52.408285-04:00  ok |
| [REDACTED] | Knowledge & memory | once at 2026-09-01 08:43 |  |  | configured private channel |  |  |
| [REDACTED] | Other scheduled automation | 20 8,20 * * * |  |  | configured private channel | ~ | 2026-08-25T20:38:17.596155-04:00  error: TimeoutError: Timed out waiting for the TERMINAL_CWD write lock after 660s — another cron job (a workdir writer, or long-running readers) has held it for longer than the cron inactivity limit. If a workdir job is the holder, stagger its schedule or remove its |
| [Private finance automation task] | Private finance automation | every 720m | no-agent (script stdout delivered directly) | [private script] | origin |  | 2026-08-25T22:49:57.872714-04:00  ok |
| [Private finance automation task] | Private finance automation | 0 8,14,20 * * * | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-08-25T20:09:19.260206-04:00  ok |
| Hermes cron auto-healer | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | hermes_auto_healer.py | origin | ~ | 2026-08-26T06:06:59.013754-04:00  ok |
| [Reliability watchdogs task] | Reliability watchdogs | every 720m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-08-26T01:24:21.196115-04:00  ok |
| Nightly GBrain update watchdog | Knowledge & memory | 20 3 * * * | no-agent (script stdout delivered directly) | gbrain_update_watchdog.py | origin | ~ | 2026-08-26T03:21:00.535775-04:00  ok |
| [Private finance automation task] | Private finance automation | 15 8,14,20 * * * |  | [private script] | origin |  | 2026-08-25T20:57:06.065014-04:00  ok |
| [Private finance automation task] | Private finance automation | 20 8,14,20 * * * |  | [private script] | origin |  | 2026-08-25T20:49:31.501810-04:00  error: TimeoutError: Timed out waiting for the TERMINAL_CWD write lock after 660s — another cron job (a workdir writer, or long-running readers) has held it for longer than the cron inactivity limit. If a workdir job is the holder, stagger its schedule or remove its |
| Hermes Python env guard | Reliability watchdogs | every 120m | no-agent (script stdout delivered directly) | hermes_python_env_guard.py | origin |  | 2026-08-26T05:59:50.407491-04:00  ok |
| ForgetMe YouTube new video monitor | Media/news monitoring | every 30m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-26T06:12:04.342398-04:00  ok |
| Hourly GBrain auto-healer | Knowledge & memory | every 60m | no-agent (script stdout delivered directly) | gbrain_hourly_healer.py | origin | ~ | 2026-08-26T05:36:45.755951-04:00  ok |
| Update public Hermes architecture repo | GitHub & publishing | 15 6 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-25T06:18:32.120331-04:00  ok |
| OpenSourceProjects.dev hourly review | GitHub & publishing | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-26T05:47:06.857804-04:00  ok |
| Telegram @github hourly review | GitHub & publishing | every 60m |  | telegram_github_watch.py | configured private channel |  | 2026-08-26T05:17:54.925126-04:00  ok |
| Glances system watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | glances_system_monitor.py | configured private channel | ~ | 2026-08-26T06:02:53.144062-04:00  ok |
| Daily React Doctor web watchdog | Reliability watchdogs | 30 9 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-25T10:40:22.905538-04:00  ok |
| Hermes architecture public site watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-26T06:02:53.988965-04:00  ok |
| Hermes private ops wiki public route watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-26T06:02:54.444757-04:00  ok |
| Telegram @notboring_tech hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-08-26T05:47:07.899650-04:00  ok |
| Telegram @git_developer hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-08-26T05:54:48.478976-04:00  ok |
| NousResearch X hourly review | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-07-22T05:30:54.042853-04:00  ok |
| Nightly cross-chat memory triage | Knowledge & memory | 45 1 * * * |  |  | configured private channel | ~ | 2026-08-17T01:55:20.635906-04:00  ok |
| [Private finance automation task] | Private finance automation | every 240m | no-agent (script stdout delivered directly) | [private script] | configured private channel | ~ | 2026-08-26T02:53:57.476991-04:00  ok |
| Nightly Hermes memory hygiene | Knowledge & memory | 0 3 * * * |  |  | configured private channel |  | 2026-08-26T03:07:18.495025-04:00  ok |
| Watch awesome-ai-workflows for Hermes-relevant additions | Other scheduled automation | 0 10 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-08-25T10:00:22.494715-04:00  ok |
| GVault public route watchdog | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-26T06:13:04.680870-04:00  ok |
| Weekly high-signal backlog review | Other scheduled automation | 0 10 * * 5 |  |  | origin |  | 2026-07-10T10:04:11.175781-04:00  ok |
| Hermes latency watchdog | Reliability watchdogs | every 60m | no-agent (script stdout delivered directly) | hermes_latency_watchdog.py | configured private channel | ~ | 2026-08-26T05:47:09.001169-04:00  ok |
| Hermes session housekeeping | Other scheduled automation | 10 5 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-26T05:10:31.981291-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 9 * * 1 |  |  | origin |  | 2026-08-24T09:59:42.599145-04:00  ok |
| Weekly PixelRAG maintenance | Other scheduled automation | 0 11 * * 0 | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-23T11:00:28.072625-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  | 2026-08-24T10:19:27.168554-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  | 2026-08-24T10:30:07.647236-04:00  ok |
| Weekly Telegram Bot API dependency check | Other scheduled automation | 0 9 * * 1 |  |  | origin |  | 2026-08-24T09:21:06.719547-04:00  ok |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  | 2026-08-04T08:22:15.134118-04:00  ok |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| alpha | Other scheduled automation | every 60m |  |  | configured private channel |  |  |
| Mattermost public route auto-healer | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-26T06:13:05.234387-04:00  ok |
| Habr Russian articles hourly monitor | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-26T05:48:58.620940-04:00  ok |
| Watch chrome-devtools-mcp pilot triggers | Other scheduled automation | 0 10 * * 1 | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-08-24T10:01:00.783989-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 9,21 * * * |  |  | configured private channel | ~ | 2026-08-25T21:11:44.608607-04:00  error: TimeoutError: Timed out waiting for the TERMINAL_CWD write lock after 660s — another cron job (a workdir writer, or long-running readers) has held it for longer than the cron inactivity limit. If a workdir job is the holder, stagger its schedule or remove its |
| [REDACTED] | Other scheduled automation | 35 9,21 * * * |  |  | configured private channel | ~ | 2026-08-25T21:46:58.548129-04:00  error: TimeoutError: Timed out waiting for the TERMINAL_CWD write lock after 660s — another cron job (a workdir writer, or long-running readers) has held it for longer than the cron inactivity limit. If a workdir job is the holder, stagger its schedule or remove its |
| [REDACTED] | Backup & sync | 5 10,22 * * * |  |  | origin | ~ | 2026-08-25T22:16:06.594019-04:00  error: TimeoutError: Timed out waiting for the TERMINAL_CWD write lock after 660s — another cron job (a workdir writer, or long-running readers) has held it for longer than the cron inactivity limit. If a workdir job is the holder, stagger its schedule or remove its |
| Telegram @quotaradar hourly forward | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-26T05:48:59.708915-04:00  ok |
| Daily discussion journal Google Sheet updater | Other scheduled automation | 35 11 * * * |  |  | configured private channel | ~ | 2026-08-25T11:53:15.307134-04:00  error: Gateway shutdown (post-interrupt) killed the job's tool subprocess before the run finished. |
| Nightly Hermes & Orchestrator deep optimizer | Other scheduled automation | 15 0 * * * |  | [REDACTED] | origin | ~ | 2026-08-26T00:34:36.008928-04:00  ok |
| Reassess QM for Hermes | Other scheduled automation | once at 2026-11-01 13:13 |  |  | origin |  |  |
| DoorDash CLI Linux/Windows release watchdog | Reliability watchdogs | 0 9 * * * | no-agent (script stdout delivered directly) | doordash_cli_watch.py | origin |  | 2026-08-25T09:00:05.267213-04:00  ok |
| Weekly TencentDB Agent Memory adoption recheck | Knowledge & memory | 0 10 * * 1 |  |  | configured private channel |  | 2026-08-24T10:21:49.076425-04:00  ok |
| Daily Hermes stable release watch | Other scheduled automation | 5 11 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-25T11:06:00.131916-04:00  ok |
| Reassess Qwen3.8-Max Hermes relevance | Other scheduled automation | once in 30d |  |  | origin |  |  |
| Daily Google Keep useful-resource review | Other scheduled automation | 0 9 * * * |  |  | origin |  | 2026-08-25T09:12:22.367030-04:00  ok |
| GPT-5.6 Terra pilot daily metrics | Other scheduled automation | 50 23 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-19T23:51:44.035309-04:00  ok |
| Reassess Kitesurf for Hermes | Other scheduled automation | once at 2026-09-07 15:38 |  |  | origin |  |  |
| GPT-5.6 Terra pilot final reviewer checkpoint | Other scheduled automation | once at 2026-08-19 18:15 |  |  | origin | ~ | 2026-08-19T18:22:06.175556-04:00  error: RuntimeError: Non-streaming API call timed out after 90s with no response (threshold: 90s) |
| Glances root disk cleanup every 3 hours | Other scheduled automation | every 180m | no-agent (script stdout delivered directly) | glances_disk_cleanup.py | configured private channel | ~ | 2026-08-26T04:43:29.083255-04:00  ok |
| [REDACTED] | Other scheduled automation | once at 2026-08-20 13:29 |  |  | origin | ~ | 2026-08-20T13:42:18.476245-04:00  ok |
| codex-chatgpt-web #154 watch → swap + decommission old provider | Other scheduled automation | every 720m |  |  | origin |  | 2026-08-26T05:49:42.679364-04:00  ok |
| [REDACTED] | Reliability watchdogs | */15 * * * * | no-agent (script stdout delivered directly) | wud_evening_watchdog.py | origin |  | 2026-08-26T06:15:05.277819-04:00  ok |

## Execution model

- **no-agent script jobs**: scheduler executes a script and delivers stdout verbatim; empty stdout means silent success.
- **agent-backed jobs**: scheduler injects context/script output into Hermes and lets the agent reason before delivering a response.
- **private delivery targets** are intentionally collapsed to `configured private channel`.
