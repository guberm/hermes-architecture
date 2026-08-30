# Scheduled Tasks and Cron Jobs

Public-safe low-level inventory of Hermes scheduled automation. Private/client-sensitive names are grouped, but schedules, execution modes, scripts, and workdirs are retained when safe.

| Task | Category | Schedule | Mode | Script | Delivery | Workdir | Last run |
|---|---|---|---|---|---|---|---|
| Daily Hermes Backup | Backup & sync | 0 3 * * * | no-agent (script stdout delivered directly) | daily_hermes_backup.sh | configured private channel | ~ | 2026-08-30T03:00:54.571593-04:00  ok |
| Daily DB SQLite Google Drive Backup | Backup & sync | 30 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-30T04:31:06.525811-04:00  ok |
| github-health-digest | GitHub & publishing | 0 9 * * 1-5 | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-28T09:01:20.065095-04:00  ok |
| Check Windows nightly cleanup logs | Other scheduled automation | 15 2 * * * |  |  | configured private channel |  | 2026-08-30T02:16:13.266619-04:00  ok |
| world-update-brief | Media/news monitoring | 0 7,19 * * * |  |  | configured private channel |  | 2026-08-29T19:50:06.844185-04:00  ok |
| [Backup & sync task] | Backup & sync | every 180m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-08-30T06:15:59.402642-04:00  ok |
| [GitHub & publishing task] | GitHub & publishing | every 1440m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-08-29T10:25:59.854703-04:00  ok |
| Weekly deep memory cleanup | Knowledge & memory | 0 5 * * 0 |  |  | configured private channel |  | 2026-08-30T05:25:24.234322-04:00  ok |
| Daily GBrain Google Drive Backup | Backup & sync | 45 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-30T04:45:26.213044-04:00  ok |
| Daily RSS Bot Stats Report | GitHub & publishing | 0 8 * * * | no-agent (script stdout delivered directly) | rss_bot_daily_report.py | configured private channel |  | 2026-08-29T08:00:38.466051-04:00  ok |
| SwitchBot Meter Pro hourly Google Sheet logger | Home automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-30T05:41:41.202310-04:00  ok |
| Home Assistant filtered 3-hour Google Sheet logger | Home automation | every 180m | no-agent (script stdout delivered directly) | ha_entities_to_sheets.py | configured private channel |  | 2026-08-30T03:17:50.285769-04:00  ok |
| [REDACTED] | Knowledge & memory | once at 2026-09-01 08:43 |  |  | configured private channel |  |  |
| [REDACTED] | Other scheduled automation | 20 8,20 * * * |  |  | configured private channel | ~ | 2026-08-29T20:22:13.187028-04:00  ok |
| [Private finance automation task] | Private finance automation | every 720m | no-agent (script stdout delivered directly) | [private script] | origin |  | 2026-08-29T23:01:28.717636-04:00  ok |
| [Private finance automation task] | Private finance automation | 0 8,14,20 * * * | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-08-29T20:09:21.915714-04:00  ok |
| Hermes cron auto-healer | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | hermes_auto_healer.py | origin | ~ | 2026-08-30T06:15:57.124602-04:00  ok |
| [Reliability watchdogs task] | Reliability watchdogs | every 720m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-08-30T01:29:18.645223-04:00  ok |
| Nightly GBrain update watchdog | Knowledge & memory | 20 3 * * * | no-agent (script stdout delivered directly) | gbrain_update_watchdog.py | origin | ~ | 2026-08-30T03:20:51.347282-04:00  ok |
| [Private finance automation task] | Private finance automation | 15 8,14,20 * * * |  | [private script] | origin |  | 2026-08-29T20:15:34.030505-04:00  ok |
| [Private finance automation task] | Private finance automation | 20 8,14,20 * * * |  | [private script] | origin |  | 2026-08-29T20:27:55.345853-04:00  ok |
| Hermes Python env guard | Reliability watchdogs | every 120m | no-agent (script stdout delivered directly) | hermes_python_env_guard.py | origin |  | 2026-08-30T04:33:10.841320-04:00  ok |
| ForgetMe YouTube new video monitor | Media/news monitoring | every 30m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-30T06:15:57.870723-04:00  ok |
| Hourly GBrain auto-healer | Knowledge & memory | every 60m | no-agent (script stdout delivered directly) | gbrain_hourly_healer.py | origin | ~ | 2026-08-26T13:04:36.758315-04:00  error: Script exited with code 1 |
| Update public Hermes architecture repo | GitHub & publishing | 15 6 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-29T06:18:28.127041-04:00  ok |
| OpenSourceProjects.dev hourly review | GitHub & publishing | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-30T05:51:42.747106-04:00  ok |
| Telegram @github hourly review | GitHub & publishing | every 60m |  | telegram_github_watch.py | configured private channel |  | 2026-08-30T05:23:38.131578-04:00  ok |
| Glances system watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | glances_system_monitor.py | configured private channel | ~ | 2026-08-30T06:03:48.926931-04:00  ok |
| Daily React Doctor web watchdog | Reliability watchdogs | 30 9 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-29T09:30:42.139130-04:00  ok |
| Hermes architecture public site watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-30T06:04:47.112347-04:00  ok |
| Hermes private ops wiki public route watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-30T06:04:47.644151-04:00  ok |
| Telegram @notboring_tech hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-08-30T05:54:43.705617-04:00  ok |
| Telegram @git_developer hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-08-30T05:55:09.959731-04:00  ok |
| NousResearch X hourly review | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-07-22T05:30:54.042853-04:00  ok |
| Nightly cross-chat memory triage | Knowledge & memory | 45 1 * * * |  |  | configured private channel | ~ | 2026-08-17T01:55:20.635906-04:00  ok |
| [Private finance automation task] | Private finance automation | every 240m | no-agent (script stdout delivered directly) | [private script] | configured private channel | ~ | 2026-08-30T03:17:57.247595-04:00  ok |
| Nightly Hermes memory hygiene | Knowledge & memory | 0 3 * * * |  |  | configured private channel |  | 2026-08-30T03:01:05.873172-04:00  ok |
| Watch awesome-ai-workflows for Hermes-relevant additions | Other scheduled automation | 0 10 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-08-29T10:00:48.730169-04:00  ok |
| GVault public route watchdog | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-30T06:10:55.976160-04:00  ok |
| Weekly high-signal backlog review | Other scheduled automation | 0 10 * * 5 |  |  | origin |  | 2026-07-10T10:04:11.175781-04:00  ok |
| Hermes latency watchdog | Reliability watchdogs | every 60m | no-agent (script stdout delivered directly) | hermes_latency_watchdog.py | configured private channel | ~ | 2026-08-30T05:55:10.608537-04:00  ok |
| Hermes session housekeeping | Other scheduled automation | 10 5 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-30T05:10:22.169469-04:00  ok |
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
| Mattermost public route auto-healer | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-30T06:10:56.456434-04:00  ok |
| Habr Russian articles hourly monitor | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-30T06:01:45.943534-04:00  ok |
| Watch chrome-devtools-mcp pilot triggers | Other scheduled automation | 0 10 * * 1 | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-08-24T10:01:00.783989-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 9,21 * * * |  |  | configured private channel | ~ | 2026-08-29T21:03:00.327926-04:00  ok |
| [REDACTED] | Other scheduled automation | 35 9,21 * * * |  |  | configured private channel | ~ | 2026-08-29T21:40:59.297623-04:00  ok |
| [REDACTED] | Backup & sync | 5 10,22 * * * |  |  | origin | ~ | 2026-08-29T22:07:35.720943-04:00  ok |
| Telegram @quotaradar hourly forward | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-30T06:01:46.935695-04:00  ok |
| Daily discussion journal Google Sheet updater | Other scheduled automation | 35 11 * * * |  |  | configured private channel | ~ | 2026-08-29T11:44:12.486024-04:00  ok |
| Nightly Hermes & Orchestrator deep optimizer | Other scheduled automation | 15 0 * * * |  | [REDACTED] | origin | ~ | 2026-08-30T00:16:59.606540-04:00  ok |
| Reassess QM for Hermes | Other scheduled automation | once at 2026-11-01 13:13 |  |  | origin |  |  |
| DoorDash CLI Linux/Windows release watchdog | Reliability watchdogs | 0 9 * * * | no-agent (script stdout delivered directly) | doordash_cli_watch.py | origin |  | 2026-08-29T09:00:27.744626-04:00  ok |
| Weekly TencentDB Agent Memory adoption recheck | Knowledge & memory | 0 10 * * 1 |  |  | configured private channel |  | 2026-08-24T10:21:49.076425-04:00  ok |
| Daily Hermes stable release watch | Other scheduled automation | 5 11 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-29T11:05:09.171618-04:00  ok |
| Reassess Qwen3.8-Max Hermes relevance | Other scheduled automation | once in 30d |  |  | origin |  |  |
| Daily Google Keep useful-resource review | Other scheduled automation | 45 9 * * * |  |  | origin |  | 2026-08-29T09:50:25.533313-04:00  ok |
| GPT-5.6 Terra pilot daily metrics | Other scheduled automation | 50 23 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-19T23:51:44.035309-04:00  ok |
| Reassess Kitesurf for Hermes | Other scheduled automation | once at 2026-09-07 15:38 |  |  | origin |  |  |
| Glances root disk cleanup every 3 hours | Other scheduled automation | every 180m | no-agent (script stdout delivered directly) | glances_disk_cleanup.py | configured private channel | ~ | 2026-08-30T04:04:06.765214-04:00  ok |
| codex-chatgpt-web #154 watch → swap + decommission old provider | Other scheduled automation | every 720m |  |  | origin |  | 2026-08-30T05:57:11.487878-04:00  ok |
| [REDACTED] | Reliability watchdogs | */15 * * * * | no-agent (script stdout delivered directly) | wud_evening_watchdog.py | origin |  | 2026-08-30T06:15:57.506069-04:00  ok |

## Execution model

- **no-agent script jobs**: scheduler executes a script and delivers stdout verbatim; empty stdout means silent success.
- **agent-backed jobs**: scheduler injects context/script output into Hermes and lets the agent reason before delivering a response.
- **private delivery targets** are intentionally collapsed to `configured private channel`.
