# Scheduled Tasks and Cron Jobs

Public-safe low-level inventory of Hermes scheduled automation. Private/client-sensitive names are grouped, but schedules, execution modes, scripts, and workdirs are retained when safe.

| Task | Category | Schedule | Mode | Script | Delivery | Workdir | Last run |
|---|---|---|---|---|---|---|---|
| Daily Hermes Backup | Backup & sync | 0 3 * * * | no-agent (script stdout delivered directly) | daily_hermes_backup.sh | configured private channel | ~ | 2026-08-07T03:00:31.214554-04:00  ok |
| Daily DB SQLite Google Drive Backup | Backup & sync | 30 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-07T04:32:28.986505-04:00  ok |
| github-health-digest | GitHub & publishing | 0 9 * * 1-5 | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-06T11:46:16.894817-04:00  ok |
| Check Windows nightly cleanup logs | Other scheduled automation | 15 2 * * * |  |  | configured private channel |  | 2026-08-07T02:18:56.279187-04:00  ok |
| world-update-brief | Media/news monitoring | 0 7,19 * * * |  |  | configured private channel | ~/.hermes/scripts | 2026-08-06T20:42:17.535267-04:00  ok |
| [Backup & sync task] | Backup & sync | every 180m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-08-07T05:03:54.748887-04:00  ok |
| [GitHub & publishing task] | GitHub & publishing | every 1440m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-08-06T15:45:24.353214-04:00  ok |
| Weekly deep memory cleanup | Knowledge & memory | 0 5 * * 0 |  |  | configured private channel |  | 2026-08-02T05:38:02.815209-04:00  ok |
| Daily GBrain Google Drive Backup | Backup & sync | 45 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-07T04:45:59.979651-04:00  ok |
| Daily RSS Bot Stats Report | GitHub & publishing | 0 8 * * * | no-agent (script stdout delivered directly) | rss_bot_daily_report.py | configured private channel |  | 2026-08-06T08:01:21.598100-04:00  ok |
| SwitchBot Meter Pro hourly Google Sheet logger | Home automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-07T06:08:13.633828-04:00  ok |
| Home Assistant filtered 3-hour Google Sheet logger | Home automation | every 180m | no-agent (script stdout delivered directly) | ha_entities_to_sheets.py | configured private channel |  | 2026-08-07T04:47:52.499315-04:00  ok |
| [REDACTED] | Knowledge & memory | once at 2026-09-01 08:43 |  |  | configured private channel |  |  |
| [REDACTED] | Other scheduled automation | 20 8,20 * * * |  |  | configured private channel | ~ | 2026-08-06T20:48:53.194809-04:00  ok |
| [Private finance automation task] | Private finance automation | every 720m | no-agent (script stdout delivered directly) | [private script] | origin |  | 2026-08-06T21:19:43.497164-04:00  ok |
| [Private finance automation task] | Private finance automation | 0 8,14,20 * * * | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-08-06T20:38:53.748355-04:00  ok |
| Hermes cron auto-healer | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | hermes_auto_healer.py | origin | ~ | 2026-08-07T06:14:12.305433-04:00  ok |
| [Reliability watchdogs task] | Reliability watchdogs | every 720m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-08-07T01:26:03.133914-04:00  ok |
| Nightly GBrain update watchdog | Knowledge & memory | 20 3 * * * | no-agent (script stdout delivered directly) | gbrain_update_watchdog.py | origin | ~ | 2026-08-07T03:20:30.679768-04:00  ok |
| [Private finance automation task] | Private finance automation | 15 8,14,20 * * * |  | [private script] | origin | ~ | 2026-08-06T20:42:37.764653-04:00  ok |
| [Private finance automation task] | Private finance automation | 20 8,14,20 * * * |  | [private script] | origin | ~ | 2026-08-06T20:50:47.167787-04:00  ok |
| Hermes Python env guard | Reliability watchdogs | every 120m | no-agent (script stdout delivered directly) | hermes_python_env_guard.py | origin |  | 2026-08-07T04:33:46.937839-04:00  ok |
| ForgetMe YouTube new video monitor | Media/news monitoring | every 30m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-07T05:56:05.320271-04:00  ok |
| Hourly GBrain auto-healer | Knowledge & memory | every 60m | no-agent (script stdout delivered directly) | gbrain_hourly_healer.py | origin | ~ | 2026-08-07T05:34:02.794897-04:00  ok |
| Update public Hermes architecture repo | GitHub & publishing | 15 6 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-06T06:15:52.892669-04:00  ok |
| OpenSourceProjects.dev hourly review | GitHub & publishing | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-07T05:34:03.624098-04:00  ok |
| Telegram @github hourly review | GitHub & publishing | every 60m |  | telegram_github_watch.py | configured private channel | ~ | 2026-08-07T05:35:01.321444-04:00  ok |
| Glances system watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | glances_watchdog.py | configured private channel | ~ | 2026-08-06T20:59:53.058765-04:00  ok |
| Daily React Doctor web watchdog | Reliability watchdogs | 30 9 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-06T11:47:16.650158-04:00  ok |
| Private Hermes ops wiki updater | Other scheduled automation | every 360m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-07T00:27:19.288762-04:00  ok |
| Hermes architecture public site watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-07T01:54:09.728076-04:00  ok |
| Hermes private ops wiki public route watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-07T02:10:09.497142-04:00  ok |
| Telegram @notboring_tech hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-08-07T05:55:05.784946-04:00  ok |
| Telegram @git_developer hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-08-07T05:55:06.808473-04:00  ok |
| NousResearch X hourly review | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-07-22T05:30:54.042853-04:00  ok |
| Nightly cross-chat memory triage | Knowledge & memory | 45 1 * * * |  |  | configured private channel | ~ | 2026-08-07T01:53:59.194210-04:00  error: RuntimeError: Context length exceeded: max compression attempts (3) reached. |
| [Private finance automation task] | Private finance automation | every 240m | no-agent (script stdout delivered directly) | [private script] | configured private channel | ~ | 2026-08-07T04:33:59.220549-04:00  ok |
| Nightly Hermes memory hygiene | Knowledge & memory | 0 3 * * * |  |  | configured private channel |  | 2026-08-07T03:02:17.975006-04:00  ok |
| Watch awesome-ai-workflows for Hermes-relevant additions | Other scheduled automation | 0 10 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-08-06T10:00:27.730723-04:00  ok |
| GVault public route watchdog | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-07T06:12:11.978015-04:00  ok |
| Weekly high-signal backlog review | Other scheduled automation | 0 10 * * 5 |  |  | origin |  | 2026-07-10T10:04:11.175781-04:00  ok |
| Hermes latency watchdog | Reliability watchdogs | every 60m | no-agent (script stdout delivered directly) | hermes_latency_watchdog.py | configured private channel | ~ | 2026-08-07T05:55:07.516304-04:00  ok |
| Hermes session housekeeping | Other scheduled automation | 10 5 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-08-07T05:10:55.471717-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 9 * * 1 |  |  | origin |  | 2026-08-03T10:37:51.286999-04:00  ok |
| Weekly PixelRAG maintenance | Other scheduled automation | 0 11 * * 0 | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-02T11:01:06.331768-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  | 2026-08-03T12:04:32.854418-04:00  error: Gateway shutdown (final-cleanup) killed the job's tool subprocess before the run finished. |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  | [REDACTED] |
| Weekly Telegram Bot API dependency check | Other scheduled automation | 0 9 * * 1 |  |  | origin |  | 2026-08-03T09:13:30.835673-04:00  ok |
| Reassess First Customer Finder pilot timing | Other scheduled automation | once in 30d |  |  | origin |  |  |
| Backlog opportunity watcher | Other scheduled automation | every 120m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~/.hermes/scripts | 2026-08-07T04:52:51.668561-04:00  ok |
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
| Mattermost public route auto-healer | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-07T06:12:12.285762-04:00  ok |
| Habr Russian articles hourly monitor | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-07T06:01:33.733588-04:00  ok |
| Watch chrome-devtools-mcp pilot triggers | Other scheduled automation | 0 10 * * 1 | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-08-03T10:00:10.044584-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 9,21 * * * |  |  | configured private channel | ~ | 2026-08-06T21:05:39.932340-04:00  error: RuntimeError: Context length exceeded: max compression attempts (3) reached. |
| [REDACTED] | Other scheduled automation | 35 9,21 * * * |  |  | configured private channel | ~ | 2026-08-06T21:41:54.585298-04:00  ok |
| [REDACTED] | Backup & sync | 5 10,22 * * * |  |  | origin | ~ | 2026-08-06T22:10:31.360602-04:00  ok |
| Telegram @quotaradar hourly forward | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-08-07T06:01:35.020682-04:00  ok |
| Dormant candidate repository watcher | GitHub & publishing | 37 10 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~/.hermes/scripts | 2026-08-06T12:25:04.025042-04:00  ok |
| Daily discussion journal Google Sheet updater | Other scheduled automation | 35 11 * * * |  |  | configured private channel | ~ | 2026-08-06T11:50:21.848801-04:00  error: RuntimeError: Connection error. |
| Nightly Hermes & Orchestrator deep optimizer | Other scheduled automation | 15 0 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-07T00:15:44.329232-04:00  ok |
| Reassess QM for Hermes | Other scheduled automation | once at 2026-11-01 13:13 |  |  | origin |  |  |
| DoorDash CLI Linux/Windows release watchdog | Reliability watchdogs | 0 9 * * * | no-agent (script stdout delivered directly) | doordash_cli_watch.py | origin |  | 2026-08-06T09:00:11.814889-04:00  ok |
| Weekly TencentDB Agent Memory adoption recheck | Knowledge & memory | 0 10 * * 1 |  |  | configured private channel |  | 2026-08-03T11:05:23.405335-04:00  ok |
| Daily Hermes stable release watch | Other scheduled automation | 5 11 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-06T11:49:57.351470-04:00  ok |
| Reassess Qwen3.8-Max Hermes relevance | Other scheduled automation | once in 30d |  |  | origin |  |  |
| Primary backup one-hour finality check | Backup & sync | once at 2026-08-05 11:26 |  |  | origin |  | 2026-08-05T11:29:08.686546-04:00  ok |
| Daily Google Keep useful-resource review | Other scheduled automation | 0 9 * * * |  |  | origin |  | 2026-08-06T11:45:54.119166-04:00  error: RuntimeError: Connection error. |
| GPT-5.6 Terra pilot two-week reviewer checkpoint | Other scheduled automation | once at 2026-08-19 18:15 |  |  | origin | ~ |  |
| GPT-5.6 Terra pilot daily metrics | Other scheduled automation | 50 23 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-08-06T23:50:37.199962-04:00  ok |

## Execution model

- **no-agent script jobs**: scheduler executes a script and delivers stdout verbatim; empty stdout means silent success.
- **agent-backed jobs**: scheduler injects context/script output into Hermes and lets the agent reason before delivering a response.
- **private delivery targets** are intentionally collapsed to `configured private channel`.
