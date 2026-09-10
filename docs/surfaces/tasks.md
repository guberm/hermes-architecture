# Scheduled Tasks and Cron Jobs

Public-safe low-level inventory of Hermes scheduled automation. Private/client-sensitive names are grouped, but schedules, execution modes, scripts, and workdirs are retained when safe.

| Task | Category | Schedule | Mode | Script | Delivery | Workdir | Last run |
|---|---|---|---|---|---|---|---|
| Daily Hermes Backup | Backup & sync | 0 3 * * * | no-agent (script stdout delivered directly) | daily_hermes_backup.sh | configured private channel | ~ | 2026-09-10T03:01:54.628563-04:00  ok |
| Daily DB SQLite Google Drive Backup | Backup & sync | 30 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-09-10T04:31:18.749014-04:00  ok |
| github-health-digest | GitHub & publishing | 0 9 * * 1-5 | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-09-09T09:02:28.210118-04:00  error: Interrupted by shutdown before terminal completion.  (2 failures in a row) |
| Check Windows nightly cleanup logs | Other scheduled automation | 15 2 * * * |  |  | configured private channel |  | 2026-09-10T02:21:43.589290-04:00  ok |
| world-update-brief | Media/news monitoring | 0 7,19 * * * |  |  | configured private channel |  | 2026-09-09T20:15:06.129033-04:00  ok |
| [Backup & sync task] | Backup & sync | every 180m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-09-10T03:40:42.269752-04:00  ok |
| [GitHub & publishing task] | GitHub & publishing | every 1440m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-09-09T14:03:25.624986-04:00  ok |
| Weekly deep memory cleanup | Knowledge & memory | 0 5 * * 0 |  |  | configured private channel |  | 2026-09-06T05:06:07.529755-04:00  ok |
| Daily GBrain Google Drive Backup | Backup & sync | 45 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-09-10T04:46:03.521342-04:00  ok |
| Daily RSS Bot Stats Report | GitHub & publishing | 0 8 * * * | no-agent (script stdout delivered directly) | rss_bot_daily_report.py | configured private channel |  | 2026-09-09T08:02:07.075574-04:00  ok |
| SwitchBot Meter Pro hourly Google Sheet logger | Home automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-09-10T05:43:09.228287-04:00  ok |
| Home Assistant filtered 3-hour Google Sheet logger | Home automation | every 180m | no-agent (script stdout delivered directly) | ha_entities_to_sheets.py | configured private channel |  | 2026-09-10T05:59:21.494805-04:00  ok |
| [REDACTED] | Other scheduled automation | 20 8,20 * * * |  |  | configured private channel | ~ | 2026-09-09T20:30:18.422787-04:00  ok |
| [Private finance automation task] | Private finance automation | every 720m | no-agent (script stdout delivered directly) | [private script] | origin |  | 2026-09-10T00:10:12.364832-04:00  ok |
| [Private finance automation task] | Private finance automation | 0 8,14,20 * * * | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-09-09T20:09:02.128132-04:00  ok |
| Hermes cron auto-healer | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | hermes_auto_healer.py | origin | ~ | 2026-09-10T06:08:12.697237-04:00  ok |
| [Reliability watchdogs task] | Reliability watchdogs | every 720m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-09-09T23:34:59.257177-04:00  ok |
| Nightly GBrain update watchdog | Knowledge & memory | 20 3 * * * | no-agent (script stdout delivered directly) | gbrain_update_watchdog.py | origin | ~ | 2026-09-10T03:21:00.147658-04:00  ok |
| [Private finance automation task] | Private finance automation | 15 8,14,20 * * * |  | [private script] | origin |  | 2026-09-09T20:17:06.179094-04:00  ok |
| [Private finance automation task] | Private finance automation | 20 8,14,20 * * * |  | [private script] | origin |  | 2026-09-09T20:27:47.230963-04:00  ok |
| Hermes Python env guard | Reliability watchdogs | every 120m | no-agent (script stdout delivered directly) | hermes_python_env_guard.py | origin |  | 2026-09-10T04:39:54.859311-04:00  ok |
| ForgetMe YouTube new video monitor | Media/news monitoring | every 30m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-10T06:05:12.069819-04:00  ok |
| Hourly GBrain auto-healer | Knowledge & memory | every 60m | no-agent (script stdout delivered directly) | gbrain_hourly_healer.py | origin | ~ | 2026-09-10T05:47:09.136583-04:00  ok |
| Update public Hermes architecture repo | GitHub & publishing | 15 6 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-09T06:16:37.619495-04:00  ok |
| OpenSourceProjects.dev hourly review | GitHub & publishing | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-09-10T05:38:06.588130-04:00  ok |
| Telegram @github hourly review | GitHub & publishing | every 60m |  | telegram_github_watch.py | configured private channel |  | 2026-09-10T05:47:08.751739-04:00  ok |
| Glances system watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | glances_system_monitor.py | configured private channel | ~ | 2026-09-10T06:07:16.899175-04:00  ok |
| Daily React Doctor web watchdog | Reliability watchdogs | 30 9 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-09T09:30:42.994849-04:00  ok |
| Hermes architecture public site watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-10T06:08:12.946208-04:00  ok |
| Hermes private ops wiki public route watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-10T06:08:12.886502-04:00  ok |
| Telegram @notboring_tech hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-09-10T05:53:10.196370-04:00  ok |
| Telegram @git_developer hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-09-10T05:57:10.717308-04:00  ok |
| NousResearch X hourly review | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-09-10T05:36:09.108179-04:00  ok |
| Nightly cross-chat memory triage | Knowledge & memory | 45 1 * * * |  |  | configured private channel | ~ | 2026-09-10T02:02:38.952243-04:00  ok |
| [Private finance automation task] | Private finance automation | every 240m | no-agent (script stdout delivered directly) | [private script] | configured private channel | ~ | 2026-09-10T04:45:23.048908-04:00  ok |
| Nightly Hermes memory hygiene | Knowledge & memory | 0 3 * * * |  |  | configured private channel |  | 2026-09-10T03:03:56.110341-04:00  ok |
| Watch awesome-ai-workflows for Hermes-relevant additions | Other scheduled automation | 0 10 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-09-09T10:00:48.245500-04:00  ok |
| GVault public route watchdog | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-10T06:15:14.006227-04:00  ok |
| Weekly high-signal backlog review | Other scheduled automation | 0 10 * * 5 |  |  | origin |  | 2026-07-10T10:04:11.175781-04:00  ok |
| Hermes latency watchdog | Reliability watchdogs | every 60m | no-agent (script stdout delivered directly) | hermes_latency_watchdog.py | configured private channel | ~ | 2026-09-10T05:43:07.383669-04:00  ok |
| Hermes session housekeeping | Other scheduled automation | 10 5 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-09-10T05:11:30.514146-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 9 * * 1 |  |  | origin |  | 2026-09-07T10:02:32.233408-04:00  ok |
| Weekly PixelRAG maintenance | Other scheduled automation | 0 11 * * 0 | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-06T11:30:29.961592-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  | 2026-09-07T11:02:51.239288-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  | 2026-09-07T10:23:39.112272-04:00  ok |
| Weekly Telegram Bot API dependency check | Other scheduled automation | 0 9 * * 1 |  |  | origin |  | 2026-09-07T09:14:17.457618-04:00  ok |
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
| Mattermost public route auto-healer | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-10T06:14:13.792582-04:00  ok |
| Habr Russian articles hourly monitor | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-09-10T05:21:45.345864-04:00  ok |
| Watch chrome-devtools-mcp pilot triggers | Other scheduled automation | 0 10 * * 1 | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-09-07T10:00:29.274999-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 9,21 * * * |  |  | configured private channel | ~ | 2026-09-09T21:05:01.203925-04:00  ok |
| [REDACTED] | Other scheduled automation | 35 9,21 * * * |  |  | configured private channel | ~ | 2026-09-09T21:42:11.521989-04:00  ok |
| [REDACTED] | Backup & sync | 5 10,22 * * * |  |  | origin | ~ | 2026-09-09T22:08:35.339673-04:00  ok |
| Telegram @quotaradar hourly forward | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-09-10T05:39:07.065814-04:00  ok |
| Daily discussion journal Google Sheet updater | Other scheduled automation | 35 11 * * * |  |  | configured private channel | ~ | 2026-09-09T11:46:36.520820-04:00  ok |
| Nightly Hermes & Orchestrator deep optimizer | Other scheduled automation | 15 0 * * * |  | [REDACTED] | origin | ~ | 2026-09-10T00:17:10.721202-04:00  ok |
| Reassess QM for Hermes | Other scheduled automation | once at 2026-11-01 13:13 |  |  | origin |  |  |
| DoorDash CLI Linux/Windows release watchdog | Reliability watchdogs | 0 9 * * * | no-agent (script stdout delivered directly) | doordash_cli_watch.py | origin |  | 2026-09-09T09:00:36.802588-04:00  ok |
| Weekly TencentDB Agent Memory adoption recheck | Knowledge & memory | 0 10 * * 1 |  |  | configured private channel |  | 2026-09-07T10:09:34.946171-04:00  ok |
| Daily Hermes stable release watch | Other scheduled automation | 5 11 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-09T11:05:02.987612-04:00  ok |
| Daily Google Keep useful-resource review | Other scheduled automation | 45 9 * * * |  |  | origin |  | 2026-09-09T10:05:49.267022-04:00  ok |
| GPT-5.6 Terra pilot daily metrics | Other scheduled automation | 50 23 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-19T23:51:44.035309-04:00  ok |
| Reassess Kitesurf for Hermes | Other scheduled automation | once at 2026-09-07 15:38 |  |  | origin |  | 2026-09-07T16:31:05.705899-04:00  ok |
| Glances root disk cleanup every 3 hours | Other scheduled automation | every 180m | no-agent (script stdout delivered directly) | glances_disk_cleanup.py | configured private channel | ~ | 2026-09-10T05:58:10.216928-04:00  ok |
| codex-chatgpt-web #154 watch → swap + decommission old provider | Other scheduled automation | every 720m |  |  | origin |  | 2026-09-09T23:47:02.595898-04:00  ok |
| [REDACTED] | Reliability watchdogs | */15 * * * * | no-agent (script stdout delivered directly) | wud_evening_watchdog.py | origin |  | 2026-09-10T06:15:13.839279-04:00  ok |
| one-shot external Hermes v4 restart | Other scheduled automation | once in 1m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-09-06T12:20:52.319397-04:00  ok |
| Universal cron failure auto-retry watchdog | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-09-10T06:13:13.519873-04:00  ok |

## Execution model

- **no-agent script jobs**: scheduler executes a script and delivers stdout verbatim; empty stdout means silent success.
- **agent-backed jobs**: scheduler injects context/script output into Hermes and lets the agent reason before delivering a response.
- **private delivery targets** are intentionally collapsed to `configured private channel`.
