# Kanban, Profiles, Rules, and Self-Improvement

Public-safe view of the durable orchestration layer added around the Hermes gateway.

## Profile team

| Item | Value | Meaning |
|---|---|---|
| Interactive orchestrator | `default` | Main Telegram/API/CLI profile; decides whether to answer directly, delegate, create Kanban work, or schedule cron. |
| Research lane | `researcher` | Evidence-backed OSS/docs/web due diligence and adoption recommendations. |
| Execution lane | `worker` | File/terminal/code/config implementation and verification for durable work items. |
| Review lane | `reviewer` | Independent review, regression checks, security/config sanity, and final validation. |
| Default assignee | `worker` | Fallback when a task/decomposer does not choose a specialist. |
| Failure limit | `5` | Raised above the previous aggressive default to avoid noisy retry failures. |
| Per-profile concurrency | `1` | Keeps one profile from saturating model/API/browser capacity. |
| Post-session automation | `enabled` | Generates review artifacts only; does not auto-install remote skills or mutate active prompts. |


## Live Kanban assignees

```text
NAME                  ON DISK   COUNTS
claude                yes       (idle)
coding                yes       (idle)
default               yes       done=2, todo=1
researcher            yes       blocked=19, done=10
reviewer              yes       blocked=2, done=3, todo=1
security-restricted   yes       (idle)
worker                yes       blocked=3, done=5, todo=2
```

## Active orchestration config

```json
{
  "kanban": {
    "dispatch_in_gateway": true,
    "dispatch_interval_seconds": 60,
    "failure_limit": 5,
    "worker_log_rotate_bytes": 2097152,
    "worker_log_backup_count": 1,
    "orchestrator_profile": "default",
    "default_assignee": "worker",
    "max_in_progress_per_profile": 1,
    "auto_decompose": true,
    "auto_decompose_per_tick": 3,
    "dispatch_stale_timeout_seconds": 21600,
    "auto_promote_children": true
  },
  "safe_self_improvement": {
    "enabled": true,
    "min_messages": 4,
    "min_tool_calls": 2,
    "artifacts_dir": "session-automation",
    "skill_mining": {
      "enabled": true,
      "min_tool_calls": 2
    },
    "trace_code_graph": {
      "enabled": true,
      "redact_paths": false
    }
  }
}
```

## Rules layer

| Rule theme | Public-safe behavior |
|---|---|
| Operating rule | External agent resources are evidence sources; convert useful patterns into Hermes-native artifacts instead of direct-installing untrusted registries. |
| Operating rule | Durable multi-step work should prefer Kanban with default/researcher/worker/reviewer profiles; delegate_task remains for bounded fork-join reasoning. |
| Operating rule | Config/profile/rule/skill/private-architecture changes require verification and private backup before final reporting. |

## Operating contract

- `default` is the interactive/orchestrator profile and remains running in the gateway.
- `researcher`, `worker`, and `reviewer` normally show as stopped/idle; the Kanban dispatcher launches them as worker-runs when a task is assigned.
- Durable multi-step work should go through Kanban; short fork-join reasoning can still use subagent delegation.
- External repos/tool lists are treated as evidence sources, not trusted installers; useful ideas become Hermes-native skills, rules, docs, config, Kanban tasks, or sandbox pilots.
- Post-session automation writes local review artifacts only: summaries, skill-mining candidates, and trace-derived graph reports.
