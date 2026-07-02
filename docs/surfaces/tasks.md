# Scheduled Tasks and Cron Jobs

Public-safe low-level inventory of Hermes scheduled automation. Private/client-sensitive names are grouped, but schedules, execution modes, scripts, and workdirs are retained when safe.

| Task | Category | Schedule | Mode | Script | Delivery | Workdir | Last run |
|---|---|---|---|---|---|---|---|
| Daily Hermes Backup | Backup & sync | 0 3 * * * | no-agent (script stdout delivered directly) | daily_hermes_backup.sh | configured private channel | ~ | 2026-07-02T03:00:59.471917-04:00  ok |
| Sync & Merge All | Backup & sync | 0 */8 * * * |  |  | configured private channel |  | 2026-07-02T00:03:19.607428-04:00  ok |
| Daily DB SQLite Google Drive Backup | Backup & sync | 30 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-07-02T04:31:52.123119-04:00  ok |
| github-health-digest | GitHub & publishing | 0 9 * * 1-5 |  | github_health_digest.py | configured private channel | ~ | 2026-07-01T09:02:24.318574-04:00  ok |
| Check Windows nightly cleanup logs | Other scheduled automation | 15 2 * * * |  |  | configured private channel |  | 2026-07-02T02:18:58.284092-04:00  ok |
| world-update-brief | Media/news monitoring | 0 7,19 * * * |  |  | configured private channel | ~/.hermes/scripts | 2026-07-01T19:54:43.522699-04:00  ok |
| [Backup & sync task] | Backup & sync | every 180m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-07-02T06:04:02.607663-04:00  ok |
| Auto-update public portfolio site Projects | GitHub & publishing | every 1440m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-07-01T14:42:53.799721-04:00  ok |
| Weekly deep memory cleanup | Knowledge & memory | 0 5 * * 0 |  |  | configured private channel |  | 2026-06-28T05:04:32.133874-04:00  ok |
| Daily GBrain Google Drive Backup | Backup & sync | 45 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-07-02T04:46:08.632601-04:00  ok |
| Daily RSS Bot Stats Report | GitHub & publishing | 0 8 * * * | no-agent (script stdout delivered directly) | rss_bot_daily_report.py | configured private channel |  | 2026-07-01T08:01:00.207442-04:00  ok |
| SwitchBot Meter Pro hourly Google Sheet logger | Home automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-07-02T05:22:01.704789-04:00  ok |
| Home Assistant filtered 3-hour Google Sheet logger | Home automation | every 180m | no-agent (script stdout delivered directly) | ha_entities_to_sheets.py | configured private channel |  | 2026-07-02T05:21:02.529503-04:00  ok |
| [REDACTED] | Knowledge & memory | once at 2026-09-01 08:43 |  |  | configured private channel |  |  |
| [Media/news monitoring task] | Media/news monitoring | 20 8,20 * * * |  |  | configured private channel | ~ | 2026-07-01T20:22:49.473279-04:00  ok |
| [Private finance automation task] | Private finance automation | every 720m | no-agent (script stdout delivered directly) | [private script] | origin |  | 2026-07-01T21:45:19.014252-04:00  ok |
| [Private finance automation task] | Private finance automation | 0 8,14,20 * * * |  |  | origin | ~ | 2026-07-01T20:05:56.788049-04:00  ok |
| Hermes cron auto-healer | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | hermes_auto_healer.py | origin | ~ | 2026-07-02T06:11:01.443722-04:00  ok |
| [Reliability watchdogs task] | Reliability watchdogs | every 720m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-07-01T20:18:42.950434-04:00  ok |
| Nightly GBrain update watchdog | Knowledge & memory | 20 3 * * * | no-agent (script stdout delivered directly) | gbrain_update_watchdog.py | origin | ~ | 2026-07-02T03:20:56.665623-04:00  ok |
| [Private finance automation task] | Private finance automation | 15 8,14,20 * * * |  | [private script] | origin | ~ | 2026-07-01T20:16:39.395819-04:00  ok |
| [Private finance automation task] | Private finance automation | 20 8,14,20 * * * |  | [private script] | origin | ~ | 2026-07-01T20:24:19.977870-04:00  ok |
| Hermes Python env guard | Reliability watchdogs | every 120m | no-agent (script stdout delivered directly) | hermes_python_env_guard.py | origin |  | 2026-07-02T05:29:00.840649-04:00  ok |
| ForgetMe YouTube new video monitor | Media/news monitoring | every 30m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-02T06:05:01.458582-04:00  ok |
| Hourly GBrain auto-healer | Knowledge & memory | every 60m | no-agent (script stdout delivered directly) | gbrain_hourly_healer.py | origin | ~ | 2026-07-02T05:58:02.891275-04:00  ok |
| Update public Hermes architecture repo | GitHub & publishing | 15 6 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-01T06:15:56.588615-04:00  ok |
| OpenSourceProjects.dev hourly review | GitHub & publishing | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-07-02T06:00:01.980105-04:00  ok |
| Telegram @github hourly review | GitHub & publishing | every 60m |  | telegram_github_watch.py | configured private channel | ~ | 2026-07-02T06:02:01.722134-04:00  ok |
| Glances system watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | glances_watchdog.py | origin | ~ | 2026-07-02T06:06:03.506521-04:00  ok |
| Daily React Doctor web watchdog | Reliability watchdogs | 30 9 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-01T09:30:48.878580-04:00  ok |
| Private Hermes ops wiki updater | Other scheduled automation | every 360m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-02T02:21:04.642844-04:00  ok |
| Hermes architecture public site watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-02T06:06:03.641551-04:00  ok |
| Hermes private ops wiki public route watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-07-02T06:06:03.777468-04:00  ok |
| Telegram @notboring_tech hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-07-02T06:02:02.863782-04:00  ok |
| Telegram @git_developer hourly review | Other scheduled automation | every 60m |  | [REDACTED] | configured private channel | ~ | 2026-07-02T06:02:03.598683-04:00  ok |
| NousResearch X hourly review | Other scheduled automation | every 60m |  | nousresearch_x_watch.py | configured private channel | ~ | 2026-07-02T06:03:01.802983-04:00  ok |
| Nightly cross-chat memory triage | Knowledge & memory | 45 1 * * * |  |  | configured private channel | ~ | 2026-07-02T01:50:39.464625-04:00  ok |
| [Private finance automation task] | Private finance automation | every 240m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-07-02T04:26:06.061404-04:00  ok |
| Nightly Hermes memory hygiene | Knowledge & memory | 0 3 * * * |  |  | configured private channel |  | 2026-07-02T03:03:37.177121-04:00  ok |
| Watch awesome-ai-workflows for Hermes-relevant additions | Other scheduled automation | 0 10 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-07-01T10:00:41.712758-04:00  ok |
| Ensure hermesui Caddy auth | Other scheduled automation | every 5m | no-agent (script stdout delivered directly) | [REDACTED] | origin |  | 2026-07-02T06:13:01.525527-04:00  ok |

## Execution model

- **no-agent script jobs**: scheduler executes a script and delivers stdout verbatim; empty stdout means silent success.
- **agent-backed jobs**: scheduler injects context/script output into Hermes and lets the agent reason before delivering a response.
- **private delivery targets** are intentionally collapsed to `configured private channel`.
