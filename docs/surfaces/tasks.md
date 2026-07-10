# Scheduled Tasks and Cron Jobs

Public-safe low-level inventory of Hermes scheduled automation. Private/client-sensitive names are grouped, but schedules, execution modes, scripts, and workdirs are retained when safe.

| Task | Category | Schedule | Mode | Script | Delivery | Workdir | Last run |
|---|---|---|---|---|---|---|---|
| Daily Hermes Backup | Backup & sync | 0 3 * * * | no-agent (script stdout delivered directly) | daily_hermes_backup.sh | configured private channel | ~ | 2026-07-10T03:00:28.149180-04:00  ok |
| Sync & Merge All | Backup & sync | 0 */8 * * * |  |  | configured private channel |  | 2026-07-10T00:02:18.866428-04:00  ok |
| Daily DB SQLite Google Drive Backup | Backup & sync | 30 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-07-10T04:31:22.471010-04:00  ok |
| github-health-digest | GitHub & publishing | 0 9 * * 1-5 |  | github_health_digest.py | configured private channel | ~ | 2026-07-09T09:01:56.949202-04:00  ok |
| Check Windows nightly cleanup logs | Other scheduled automation | 15 2 * * * |  |  | configured private channel |  | 2026-07-10T02:19:58.531330-04:00  ok |
| world-update-brief | Media/news monitoring | 0 7,19 * * * |  |  | configured private channel | ~/.hermes/scripts | 2026-07-09T19:21:50.392463-04:00  ok |
| [Backup & sync task] | Backup & sync | every 180m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-07-10T03:24:25.253657-04:00  ok |
| Auto-update public portfolio site Projects | GitHub & publishing | every 1440m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-07-09T14:47:08.197331-04:00  ok |
| Weekly deep memory cleanup | Knowledge & memory | 0 5 * * 0 |  |  | configured private channel |  | 2026-07-05T05:04:15.463684-04:00  ok |
| Daily GBrain Google Drive Backup | Backup & sync | 45 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-07-10T04:45:38.506910-04:00  ok |
| Daily RSS Bot Stats Report | GitHub & publishing | 0 8 * * * | no-agent (script stdout delivered directly) | rss_bot_daily_report.py | configured private channel |  | 2026-07-09T08:01:07.821028-04:00  ok |
| SwitchBot Meter Pro hourly Google Sheet logger | Home automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-07-10T05:27:35.190665-04:00  ok |
| Home Assistant filtered 3-hour Google Sheet logger | Home automation | every 180m | no-agent (script stdout delivered directly) | ha_entities_to_sheets.py | configured private channel |  | 2026-07-10T05:39:36.350045-04:00  ok |
| [REDACTED] | Knowledge & memory | once at 2026-09-01 08:43 |  |  | configured private channel |  |  |
| [Media/news monitoring task] | Media/news monitoring | 20 8,20 * * * |  |  | configured private channel | ~ | 2026-07-09T20:22:20.475245-04:00  ok |
| [Private finance automation task] | Private finance automation | every 720m | no-agent (script stdout delivered directly) | [private script] | origin |  | 2026-07-09T22:00:05.008738-04:00  ok |
| [Private finance automation task] | Private finance automation | 0 8,14,20 * * * |  |  | origin | ~ | 2026-07-09T20:08:55.120028-04:00  ok |
| Hermes cron auto-healer | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | hermes_auto_healer.py | origin | ~ | 2026-07-10T06:01:34.529676-04:00  ok |
| [Reliability watchdogs task] | Reliability watchdogs | every 720m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-07-09T20:36:30.062079-04:00  ok |
| Nightly GBrain update watchdog | Knowledge & memory | 20 3 * * * | no-agent (script stdout delivered directly) | gbrain_update_watchdog.py | origin | ~ | 2026-07-10T03:20:26.084669-04:00  ok |
| [Private finance automation task] | Private finance automation | 15 8,14,20 * * * |  | [private script] | origin | ~ | 2026-07-09T20:15:54.474138-04:00  ok |
| [Private finance automation task] | Private finance automation | 20 8,14,20 * * * |  | [private script] | origin | ~ | 2026-07-09T20:23:46.885325-04:00  ok |
| Hermes Python env guard | Reliability watchdogs | every 120m | no-agent (script stdout delivered directly) | hermes_python_env_guard.py | origin |  | 2026-07-10T04:32:28.071613-04:00  ok |
| ForgetMe YouTube new video monitor | Media/news monitoring | every 30m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-10T06:02:34.940622-04:00  ok |
| Hourly GBrain auto-healer | Knowledge & memory | every 60m | no-agent (script stdout delivered directly) | gbrain_hourly_healer.py | origin | ~ | 2026-07-10T06:01:36.978118-04:00  ok |
| Update public Hermes architecture repo | GitHub & publishing | 15 6 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-09T06:15:56.029968-04:00  ok |
| OpenSourceProjects.dev hourly review | GitHub & publishing | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-07-10T05:34:33.663333-04:00  ok |
| Telegram @github hourly review | GitHub & publishing | every 60m |  | telegram_github_watch.py | configured private channel | ~ | 2026-07-10T05:28:42.839257-04:00  ok |
| Glances system watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | glances_watchdog.py | origin | ~ | 2026-07-10T06:00:36.667190-04:00  ok |
| Daily React Doctor web watchdog | Reliability watchdogs | 30 9 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-09T09:31:00.546574-04:00  ok |
| Private Hermes ops wiki updater | Other scheduled automation | every 360m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-10T02:41:29.429577-04:00  ok |
| Hermes architecture public site watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-10T06:00:36.802764-04:00  ok |
| Hermes private ops wiki public route watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-10T06:00:36.944478-04:00  ok |
| Telegram @notboring_tech hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-07-10T05:42:34.258583-04:00  ok |
| Telegram @git_developer hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-07-10T05:38:59.150702-04:00  ok |
| NousResearch X hourly review | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-07-10T05:34:34.307134-04:00  ok |
| Nightly cross-chat memory triage | Knowledge & memory | 45 1 * * * |  |  | configured private channel | ~ | 2026-07-10T02:00:12.518456-04:00  ok |
| [Private finance automation task] | Private finance automation | every 240m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-07-10T05:44:45.132406-04:00  ok |
| Nightly Hermes memory hygiene | Knowledge & memory | 0 3 * * * |  |  | configured private channel |  | 2026-07-10T03:03:31.123161-04:00  ok |
| Watch awesome-ai-workflows for Hermes-relevant additions | Other scheduled automation | 0 10 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-07-09T10:00:48.276393-04:00  ok |
| Ensure hermesui Caddy auth | Other scheduled automation | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-07-10T06:13:34.966520-04:00  ok |
| GVault Caddy route watchdog | Reliability watchdogs | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-07-10T06:15:35.120565-04:00  ok |
| Weekly high-signal backlog review | Other scheduled automation | 0 10 * * 5 |  |  | origin |  |  |
| Hermes latency watchdog | Reliability watchdogs | every 60m | no-agent (script stdout delivered directly) | hermes_latency_watchdog.py | configured private channel | ~ | 2026-07-10T06:01:37.552083-04:00  ok |
| Hermes session housekeeping | Other scheduled automation | 10 5 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-07-10T05:20:04.869001-04:00  ok |
| [REDACTED] | Knowledge & memory | once at 2026-07-13 19:04 |  |  | origin |  |  |
| [REDACTED] | Other scheduled automation | 0 9 * * 1 |  |  | origin |  |  |
| Weekly PixelRAG maintenance | Other scheduled automation | 0 11 * * 0 | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-08T17:51:41.010305-04:00  ok |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  |  |
| [REDACTED] | Other scheduled automation | 0 10 * * 1 |  |  | origin |  |  |
| Weekly Telegram Bot API dependency check | Other scheduled automation | 0 9 * * 1 |  |  | origin |  |  |

## Execution model

- **no-agent script jobs**: scheduler executes a script and delivers stdout verbatim; empty stdout means silent success.
- **agent-backed jobs**: scheduler injects context/script output into Hermes and lets the agent reason before delivering a response.
- **private delivery targets** are intentionally collapsed to `configured private channel`.
