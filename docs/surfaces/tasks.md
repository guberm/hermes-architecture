# Scheduled Tasks and Cron Jobs

Public-safe low-level inventory of Hermes scheduled automation. Private/client-sensitive names are grouped, but schedules, execution modes, scripts, and workdirs are retained when safe.

| Task | Category | Schedule | Mode | Script | Delivery | Workdir | Last run |
|---|---|---|---|---|---|---|---|
| Daily Hermes Backup | Backup & sync | 0 3 * * * | no-agent (script stdout delivered directly) | daily_hermes_backup.sh | configured private channel | ~ | 2026-09-01T03:00:36.723228-04:00  ok |
| Daily DB SQLite Google Drive Backup | Backup & sync | 30 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-09-01T04:31:36.061221-04:00  ok |
| github-health-digest | GitHub & publishing | 0 9 * * 1-5 | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-31T09:01:58.790052-04:00  ok |
| Check Windows nightly cleanup logs | Other scheduled automation | 15 2 * * * |  |  | configured private channel |  | 2026-09-01T02:19:02.998980-04:00  ok |
| world-update-brief | Media/news monitoring | 0 7,19 * * * |  |  | configured private channel |  | 2026-08-31T21:46:08.550272-04:00  ok |
| [Backup & sync task] | Backup & sync | every 180m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-09-01T03:25:25.473123-04:00  ok |
| [GitHub & publishing task] | GitHub & publishing | every 1440m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-08-31T10:27:59.032019-04:00  ok |
| Weekly deep memory cleanup | Knowledge & memory | 0 5 * * 0 |  |  | configured private channel |  | 2026-08-30T05:25:24.234322-04:00  ok |
| Daily GBrain Google Drive Backup | Backup & sync | 45 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-09-01T04:46:00.418520-04:00  ok |
| Daily RSS Bot Stats Report | GitHub & publishing | 0 8 * * * | no-agent (script stdout delivered directly) | rss_bot_daily_report.py | configured private channel |  | 2026-08-31T08:01:08.065652-04:00  ok |
| SwitchBot Meter Pro hourly Google Sheet logger | Home automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-09-01T06:02:12.942203-04:00  ok |
| Home Assistant filtered 3-hour Google Sheet logger | Home automation | every 180m | no-agent (script stdout delivered directly) | ha_entities_to_sheets.py | configured private channel |  | 2026-09-01T03:28:28.518350-04:00  ok |
| [REDACTED] | Knowledge & memory | once at 2026-09-01 08:43 |  |  | configured private channel |  |  |
| [REDACTED] | Other scheduled automation | 20 8,20 * * * |  |  | configured private channel | ~ | 2026-08-31T20:31:53.333745-04:00  error: TimeoutError: Timed out waiting for the TERMINAL_CWD write lock after 660s — another cron job (a workdir writer, or long-running readers) has held it for longer than the cron inactivity limit. If a workdir job is the holder, stagger its schedule or remove its |
| [Private finance automation task] | Private finance automation | every 720m | no-agent (script stdout delivered directly) | [private script] | origin |  | 2026-08-31T23:07:48.584714-04:00  ok |
| [Private finance automation task] | Private finance automation | 0 8,14,20 * * * | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-08-31T20:09:16.286549-04:00  ok |
| Hermes cron auto-healer | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | hermes_auto_healer.py | origin | ~ | 2026-09-01T06:11:16.961175-04:00  ok |
| [Reliability watchdogs task] | Reliability watchdogs | every 720m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-09-01T01:31:50.210986-04:00  ok |
| Nightly GBrain update watchdog | Knowledge & memory | 20 3 * * * | no-agent (script stdout delivered directly) | gbrain_update_watchdog.py | origin | ~ | 2026-09-01T03:20:26.821820-04:00  ok |
| [Private finance automation task] | Private finance automation | 15 8,14,20 * * * |  | [private script] | origin |  | 2026-08-31T20:16:26.835520-04:00  ok |
| [Private finance automation task] | Private finance automation | 20 8,14,20 * * * |  | [private script] | origin |  | 2026-08-31T20:35:59.916091-04:00  ok |
| Hermes Python env guard | Reliability watchdogs | every 120m | no-agent (script stdout delivered directly) | hermes_python_env_guard.py | origin |  | 2026-09-01T04:48:48.981310-04:00  ok |
| ForgetMe YouTube new video monitor | Media/news monitoring | every 30m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-01T05:59:08.686297-04:00  ok |
| Hourly GBrain auto-healer | Knowledge & memory | every 60m | no-agent (script stdout delivered directly) | gbrain_hourly_healer.py | origin | ~ | 2026-08-26T13:04:36.758315-04:00  error: Script exited with code 1 |
| Update public Hermes architecture repo | GitHub & publishing | 15 6 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-31T06:18:31.395420-04:00  ok |
| OpenSourceProjects.dev hourly review | GitHub & publishing | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-09-01T05:37:01.997055-04:00  ok |
| Telegram @github hourly review | GitHub & publishing | every 60m |  | telegram_github_watch.py | configured private channel |  | 2026-09-01T05:56:08.222988-04:00  ok |
| Glances system watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | glances_system_monitor.py | configured private channel | ~ | 2026-09-01T06:00:12.179984-04:00  ok |
| Daily React Doctor web watchdog | Reliability watchdogs | 30 9 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-31T09:30:26.475827-04:00  ok |
| Hermes architecture public site watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-01T06:01:10.121941-04:00  ok |
| Hermes private ops wiki public route watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-01T06:01:10.526189-04:00  ok |
| Telegram @notboring_tech hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-09-01T05:38:02.490364-04:00  ok |
| Telegram @git_developer hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-09-01T05:38:03.486425-04:00  ok |
| NousResearch X hourly review | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-07-22T05:30:54.042853-04:00  ok |
| Nightly cross-chat memory triage | Knowledge & memory | 45 1 * * * |  |  | configured private channel | ~ | 2026-08-17T01:55:20.635906-04:00  ok |
| [Private finance automation task] | Private finance automation | every 240m | no-agent (script stdout delivered directly) | [private script] | configured private channel | ~ | 2026-09-01T03:25:35.632157-04:00  ok |
| Nightly Hermes memory hygiene | Knowledge & memory | 0 3 * * * |  |  | configured private channel |  | 2026-09-01T03:02:23.541812-04:00  ok |
| Watch awesome-ai-workflows for Hermes-relevant additions | Other scheduled automation | 0 10 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-08-31T10:00:40.993472-04:00  ok |
| GVault public route watchdog | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-01T06:14:17.972838-04:00  ok |
| Weekly high-signal backlog review | Other scheduled automation | 0 10 * * 5 |  |  | origin |  | 2026-07-10T10:04:11.175781-04:00  ok |
| Hermes latency watchdog | Reliability watchdogs | every 60m | no-agent (script stdout delivered directly) | hermes_latency_watchdog.py | configured private channel | ~ | 2026-09-01T05:38:04.782096-04:00  ok |
| Hermes session housekeeping | Other scheduled automation | 10 5 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-09-01T05:10:53.960239-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 9 * * 1 |  |  | origin |  | 2026-08-31T09:37:02.600876-04:00  ok |
| Weekly PixelRAG maintenance | Other scheduled automation | 0 11 * * 0 | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-30T11:00:11.676877-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  | 2026-08-31T10:19:05.634688-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  | 2026-08-31T10:03:12.933223-04:00  ok |
| Weekly Telegram Bot API dependency check | Other scheduled automation | 0 9 * * 1 |  |  | origin |  | 2026-08-31T09:08:27.213212-04:00  ok |
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
| Mattermost public route auto-healer | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-01T06:14:18.480856-04:00  ok |
| Habr Russian articles hourly monitor | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-09-01T06:09:44.916267-04:00  ok |
| Watch chrome-devtools-mcp pilot triggers | Other scheduled automation | 0 10 * * 1 | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-08-31T10:00:44.322568-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 9,21 * * * |  |  | configured private channel | ~ | 2026-08-31T21:11:18.970632-04:00  error: TimeoutError: Timed out waiting for the TERMINAL_CWD write lock after 660s — another cron job (a workdir writer, or long-running readers) has held it for longer than the cron inactivity limit. If a workdir job is the holder, stagger its schedule or remove its |
| [REDACTED] | Other scheduled automation | 35 9,21 * * * |  |  | configured private channel | ~ | 2026-08-31T21:50:45.455087-04:00  ok |
| [REDACTED] | Backup & sync | 5 10,22 * * * |  |  | origin | ~ | 2026-08-31T22:08:09.683158-04:00  ok |
| Telegram @quotaradar hourly forward | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-09-01T06:09:46.046491-04:00  ok |
| Daily discussion journal Google Sheet updater | Other scheduled automation | 35 11 * * * |  |  | configured private channel | ~ | 2026-08-31T11:45:21.926811-04:00  ok |
| Nightly Hermes & Orchestrator deep optimizer | Other scheduled automation | 15 0 * * * |  | [REDACTED] | origin | ~ | 2026-09-01T00:17:10.438811-04:00  ok |
| Reassess QM for Hermes | Other scheduled automation | once at 2026-11-01 13:13 |  |  | origin |  |  |
| DoorDash CLI Linux/Windows release watchdog | Reliability watchdogs | 0 9 * * * | no-agent (script stdout delivered directly) | doordash_cli_watch.py | origin |  | 2026-08-31T09:00:56.434447-04:00  ok |
| Weekly TencentDB Agent Memory adoption recheck | Knowledge & memory | 0 10 * * 1 |  |  | configured private channel |  | 2026-08-31T10:02:59.392372-04:00  ok |
| Daily Hermes stable release watch | Other scheduled automation | 5 11 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-31T11:05:05.679106-04:00  ok |
| Reassess Qwen3.8-Max Hermes relevance | Other scheduled automation | once in 30d |  |  | origin |  |  |
| Daily Google Keep useful-resource review | Other scheduled automation | 45 9 * * * |  |  | origin |  | 2026-08-31T09:50:51.842205-04:00  ok |
| GPT-5.6 Terra pilot daily metrics | Other scheduled automation | 50 23 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-19T23:51:44.035309-04:00  ok |
| Reassess Kitesurf for Hermes | Other scheduled automation | once at 2026-09-07 15:38 |  |  | origin |  |  |
| Glances root disk cleanup every 3 hours | Other scheduled automation | every 180m | no-agent (script stdout delivered directly) | glances_disk_cleanup.py | configured private channel | ~ | 2026-09-01T04:22:45.762753-04:00  ok |
| codex-chatgpt-web #154 watch → swap + decommission old provider | Other scheduled automation | every 720m |  |  | origin |  | 2026-09-01T06:00:36.138064-04:00  ok |
| [REDACTED] | Reliability watchdogs | */15 * * * * | no-agent (script stdout delivered directly) | wud_evening_watchdog.py | origin |  | 2026-09-01T06:15:18.272382-04:00  ok |

## Execution model

- **no-agent script jobs**: scheduler executes a script and delivers stdout verbatim; empty stdout means silent success.
- **agent-backed jobs**: scheduler injects context/script output into Hermes and lets the agent reason before delivering a response.
- **private delivery targets** are intentionally collapsed to `configured private channel`.
