# Scheduled Tasks and Cron Jobs

Public-safe low-level inventory of Hermes scheduled automation. Private/client-sensitive names are grouped, but schedules, execution modes, scripts, and workdirs are retained when safe.

| Task | Category | Schedule | Mode | Script | Delivery | Workdir | Last run |
|---|---|---|---|---|---|---|---|
| Daily Hermes Backup | Backup & sync | 0 3 * * * | no-agent (script stdout delivered directly) | daily_hermes_backup.sh | configured private channel | ~ | 2026-06-23T03:00:21.477369-04:00  ok |
| Sync & Merge All | Backup & sync | 0 */8 * * * |  |  | configured private channel |  | 2026-06-23T08:02:21.676541-04:00  ok |
| Daily DB SQLite Google Drive Backup | Backup & sync | 30 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-06-23T04:31:38.155078-04:00  ok |
| github-health-digest | GitHub & publishing | 0 9 * * 1-5 |  | github_health_digest.py | configured private channel | ~ | 2026-06-23T09:01:39.942994-04:00  ok |
| Check Windows nightly cleanup logs | Other scheduled automation | 15 2 * * * |  |  | configured private channel |  | 2026-06-23T02:21:37.713315-04:00  ok |
| world-update-brief | Media/news monitoring | 0 7,19 * * * |  |  | configured private channel | ~/.hermes/scripts | 2026-06-23T07:39:10.808510-04:00  error: RuntimeError: Промежуточный статус по production-запуску: |
| [Backup & sync task] | Backup & sync | every 180m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-06-23T11:38:38.347927-04:00  ok |
| Auto-update public portfolio site Projects | GitHub & publishing | every 1440m | no-agent (script stdout delivered directly) | [private script] | configured private channel |  | 2026-06-22T14:37:09.074472-04:00  ok |
| Weekly memory-to-gbrain compaction | Knowledge & memory | 0 5 * * 0 |  |  | configured private channel |  | 2026-06-21T05:04:43.642652-04:00  ok |
| Daily GBrain Google Drive Backup | Backup & sync | 45 4 * * * | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-06-23T04:45:27.392052-04:00  ok |
| Daily RSS Bot Stats Report | GitHub & publishing | 0 8 * * * | no-agent (script stdout delivered directly) | rss_bot_daily_report.py | configured private channel |  | 2026-06-23T08:00:45.290270-04:00  ok |
| SwitchBot Meter Pro hourly Google Sheet logger | Home automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel |  | 2026-06-23T13:38:44.411187-04:00  ok |
| Home Assistant filtered 3-hour Google Sheet logger | Home automation | every 180m | no-agent (script stdout delivered directly) | ha_entities_to_sheets.py | configured private channel |  | 2026-06-23T14:05:46.401717-04:00  ok |
| [REDACTED] | Knowledge & memory | once at 2026-09-01 08:43 |  |  | configured private channel |  |  |
| [Media/news monitoring task] | Media/news monitoring | 20 8,20 * * * |  |  | configured private channel | ~ | 2026-06-23T08:20:36.931864-04:00  ok |
| [Private finance automation task] | Private finance automation | every 720m | no-agent (script stdout delivered directly) | [private script] | origin |  | 2026-06-23T09:22:27.026117-04:00  error: Script timed out after 120s: ~/.hermes/scripts/refresh_monarch_auth.py |
| [Private finance automation task] | Private finance automation | 0 8,14,20 * * * |  |  | origin | ~ | 2026-06-23T14:03:17.813094-04:00  ok |
| Hermes cron auto-healer | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | hermes_auto_healer.py | origin | ~ | 2026-06-23T14:12:43.152633-04:00  ok |
| [Reliability watchdogs task] | Reliability watchdogs | every 720m | no-agent (script stdout delivered directly) | [private script] | origin | ~ | 2026-06-23T12:34:42.386333-04:00  ok |
| Nightly GBrain update watchdog | Knowledge & memory | 20 3 * * * | no-agent (script stdout delivered directly) | gbrain_update_watchdog.py | origin | ~ | 2026-06-23T03:20:17.675776-04:00  ok |
| [Private finance automation task] | Private finance automation | 15 8,14,20 * * * |  | [private script] | origin | ~ | 2026-06-23T14:16:32.729895-04:00  ok |
| [Private finance automation task] | Private finance automation | 20 8,14,20 * * * |  | [private script] | origin | ~ | 2026-06-23T08:22:39.533055-04:00  ok |
| Hermes Python env guard | Reliability watchdogs | every 120m | no-agent (script stdout delivered directly) | hermes_python_env_guard.py | origin |  | 2026-06-23T12:55:41.158906-04:00  ok |
| ForgetMe YouTube new video monitor | Media/news monitoring | every 30m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-06-23T14:14:43.634165-04:00  ok |
| Hourly GBrain auto-healer | Knowledge & memory | every 60m | no-agent (script stdout delivered directly) | gbrain_hourly_healer.py | origin | ~ | 2026-06-23T13:42:43.836024-04:00  ok |
| Update public Hermes architecture repo | GitHub & publishing | 15 6 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-06-23T06:15:39.662472-04:00  ok |
| OpenSourceProjects.dev hourly review | GitHub & publishing | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-06-23T13:44:43.082652-04:00  ok |
| Telegram @github hourly review | GitHub & publishing | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-06-23T13:47:37.442894-04:00  ok |
| Glances system watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | glances_watchdog.py | origin | ~ | 2026-06-23T14:03:20.300129-04:00  ok |
| Daily React Doctor web watchdog | Reliability watchdogs | 30 9 * * * | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-06-23T09:30:27.295333-04:00  ok |
| Private Hermes ops wiki updater | Other scheduled automation | every 360m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-06-23T12:52:45.352152-04:00  ok |
| Hermes architecture public site watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-06-23T14:03:20.425270-04:00  ok |
| Hermes private ops wiki public route watchdog | Reliability watchdogs | every 15m | no-agent (script stdout delivered directly) | [REDACTED] | origin | ~ | 2026-06-23T14:03:20.551066-04:00  ok |
| Telegram @notboring_tech hourly review | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-06-23T13:47:38.465150-04:00  ok |
| Telegram @git_developer hourly review | Other scheduled automation | every 60m | no-agent (script stdout delivered directly) | [REDACTED] | configured private channel | ~ | 2026-06-23T13:47:39.349312-04:00  ok |

## Execution model

- **no-agent script jobs**: scheduler executes a script and delivers stdout verbatim; empty stdout means silent success.
- **agent-backed jobs**: scheduler injects context/script output into Hermes and lets the agent reason before delivering a response.
- **private delivery targets** are intentionally collapsed to `configured private channel`.
