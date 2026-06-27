#!/usr/bin/env python3
"""Generate public-safe Hermes architecture documentation.

This script intentionally publishes a redacted architecture view:
- no tokens, API keys, chat IDs, phone numbers, OAuth headers, cookies, or private paths that imply secrets
- private cron jobs are grouped by category rather than listed verbatim
- public documentation is regenerated from local Hermes state and committed only when content changes
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
from textwrap import dedent

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
SURFACES = DOCS / "surfaces"

PUBLIC_REPO = "this public repository"
GENERATED_AT = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")

SECRET_PATTERNS = re.compile(r"(?i)(token|secret|password|api[_-]?key|authorization|cookie|session|xauthority|chat_id|phone)")
LONG_TOKEN = re.compile(r"[A-Za-z0-9_\-]{24,}")


def run(cmd: list[str], timeout: int = 30) -> tuple[int, str]:
    try:
        p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=timeout)
        return p.returncode, p.stdout.strip()
    except Exception as e:
        return 999, f"ERROR: {type(e).__name__}: {e}"


def load_yaml(path: pathlib.Path):
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except Exception:
        return {}


def redact(value, key: str = ""):
    # For a public repo, omit secret-bearing fields entirely rather than publishing
    # placeholder keys such as api_key/token/password.
    if SECRET_PATTERNS.search(key):
        return "[OMITTED]"
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            if SECRET_PATTERNS.search(str(k)):
                continue
            out[k] = redact(v, str(k))
        return out
    if isinstance(value, list):
        return [redact(v, key) for v in value]
    if isinstance(value, str):
        value = sanitize_text(value) if 'sanitize_text' in globals() else value
        if LONG_TOKEN.search(value) and not value.startswith(("http://", "https://", "~/", "C:\\")):
            return "[REDACTED]"
        return value
    return value


def classify_cron_job(name: str) -> str:
    n = name.lower()
    if any(x in n for x in ["backup", "sync", "drive"]):
        return "Backup & sync"
    if any(x in n for x in ["gbrain", "memory", "claude"]):
        return "Knowledge & memory"
    if any(x in n for x in ["github", "repo", "projects"]):
        return "GitHub & publishing"
    if any(x in n for x in ["home assistant", "switchbot", "meter", "hvac"]):
        return "Home automation"
    if any(x in n for x in ["finance", "monarch"]):
        return "Private finance automation"
    if any(x in n for x in ["youtube", "rss", "world", "news", "brief"]):
        return "Media/news monitoring"
    if any(x in n for x in ["healer", "guard", "watchdog"]):
        return "Reliability watchdogs"
    return "Other scheduled automation"


def is_sensitive_public_string(value: str) -> bool:
    return bool(re.search(r"(?i)(mich[a]el|gu[b]er(?:m)?|/home/[a-z][a-z]|monarch|finance|financial|gmail|insurance|mcdonald|rustdesk|chorus|triparc|kateryna|aurora|vts|preprod|prod|personal|bank|tax|telegram:-|mattermost:)", value or ""))


def safe_public_name(name: str) -> str:
    """Return a public-safe label: preserve infrastructure names, group private/client surfaces."""
    if is_sensitive_public_string(name):
        return f"[{classify_cron_job(name)} task]"
    return name


def parse_cron_blocks(cron_list: str) -> list[dict[str, str]]:
    """Parse `hermes cron list --all` into a sanitized, public-safe task list."""
    jobs: list[dict[str, str]] = []
    current: dict[str, str] = {}
    keymap = {
        "Name": "name", "Schedule": "schedule", "Repeat": "repeat", "Next run": "next_run",
        "Deliver": "deliver", "Script": "script", "Mode": "mode", "Workdir": "workdir",
        "Last run": "last_run",
    }
    for raw in cron_list.splitlines():
        line = raw.strip()
        if not line:
            continue
        m = re.match(r"^(Name|Schedule|Repeat|Next run|Deliver|Script|Mode|Workdir|Last run):\s*(.*)$", line)
        if not m:
            continue
        k, v = m.group(1), sanitize_text(m.group(2).strip())
        if k == "Name":
            if current:
                jobs.append(current)
            current = {"name": safe_public_name(v), "category": classify_cron_job(v)}
        elif current:
            current[keymap[k]] = v
    if current:
        jobs.append(current)
    for j in jobs:
        if j.get("deliver") and j["deliver"] != "origin":
            j["deliver"] = "configured private channel"
        if j.get("script") and is_sensitive_public_string(j["script"]):
            j["script"] = "[private script]"
        if j.get("workdir") and is_sensitive_public_string(j["workdir"]):
            j["workdir"] = "[private workdir]"
        if j.get("workdir"):
            j["workdir"] = j["workdir"].replace(str(pathlib.Path.home()), "~")
    return jobs


def parse_tools_surface(tools_output: str) -> dict:
    """Parse a public-safe summary of Hermes toolsets/tools from CLI output."""
    toolsets: dict[str, int] = {}
    enabled_hint = 0
    for raw in tools_output.splitlines():
        line = raw.strip()
        if "enabled" in line.lower():
            enabled_hint += 1
        if line.startswith("│"):
            cols = [c.strip() for c in line.strip("│").split("│")]
            if len(cols) >= 2 and cols[0] and cols[1] and not cols[0].lower().startswith(("name", "tool")):
                ts = re.sub(r"\s+", " ", cols[1])[:60]
                if ts and not set(ts) <= {"─", "━"}:
                    toolsets[ts] = toolsets.get(ts, 0) + 1
    return {"toolset_counts_estimate": dict(sorted(toolsets.items())), "enabled_rows_estimate": enabled_hint, "note": "CLI parsing is best-effort; full tool schemas are runtime-generated and not published."}


def clean_md_cell(value: object) -> str:
    text = str(value if value is not None else "")
    text = text.replace("|", "/").replace("\n", " ").strip()
    return text[:300]


def collect_skill_surface() -> dict:
    """Collect public-safe skill counts and non-sensitive examples."""
    roots = [
        pathlib.Path.home() / ".hermes" / "skills",
        pathlib.Path.home() / ".hermes" / "hermes-agent" / "skills",
    ]
    sensitive_words = re.compile(r"(?i)(michael|finance|monarch|gmail|personal|insurance|mcdonald|rustdesk|chorus|triparc|kateryna)")
    categories: dict[str, int] = {}
    examples: list[dict[str, str]] = []
    total = 0
    for root in roots:
        if not root.exists():
            continue
        for md in root.rglob("SKILL.md"):
            if ".git" in md.parts or "node_modules" in md.parts:
                continue
            rel = md.relative_to(root)
            parts = rel.parts
            category = parts[0] if len(parts) > 2 else "uncategorized"
            text = md.read_text(encoding="utf-8", errors="replace")[:4000]
            name_match = re.search(r"(?m)^name:\s*[\"']?([^\"'\n]+)", text)
            desc_match = re.search(r"(?m)^description:\s*[\"']?([^\"'\n]+)", text)
            name = (name_match.group(1).strip() if name_match else md.parent.name)
            desc = (desc_match.group(1).strip() if desc_match else "")
            total += 1
            categories[category] = categories.get(category, 0) + 1
            if len(examples) < 40 and not sensitive_words.search(name + " " + desc + " " + category):
                examples.append({"name": name, "category": category, "description": desc[:140]})
    return {
        "total_detected": total,
        "categories": dict(sorted(categories.items())),
        "public_examples": examples,
        "note": "Examples omit personal/client-sensitive skill names; full local skill inventory remains private.",
    }


def collect_hook_surface() -> dict:
    """Collect public-safe hook/webhook/allowlist surfaces."""
    home = pathlib.Path.home()
    hook_files: list[str] = []
    hook_roots = [home / ".hermes", home / ".claude" / "plugins"]
    for root in hook_roots:
        if not root.exists():
            continue
        for p in root.rglob("hooks.json"):
            if any(part in {"node_modules", ".git", "venv", "__pycache__"} for part in p.parts):
                continue
            rel = str(p.relative_to(home))
            if len(hook_files) < 30:
                hook_files.append(rel)
    shell_allowlist = home / ".hermes" / "shell-hooks-allowlist.json"
    shell_hook_count = 0
    if shell_allowlist.exists():
        try:
            data = json.loads(shell_allowlist.read_text(encoding="utf-8"))
            shell_hook_count = len(data) if isinstance(data, list) else len(data.keys()) if isinstance(data, dict) else 0
        except Exception:
            shell_hook_count = -1
    webhook_list = run(["hermes", "webhook", "list"], 60)[1]
    webhook_summary = "webhook platform appears enabled/configured" if "not enabled" not in webhook_list.lower() else "webhook platform not enabled"
    return {
        "shell_hooks_allowlist_present": shell_allowlist.exists(),
        "shell_hooks_allowlist_entries": shell_hook_count,
        "claude_plugin_hook_files_detected": len(hook_files),
        "public_hook_file_examples": hook_files,
        "webhook_summary": webhook_summary,
        "note": "Hook contents and command bodies are not published; only hook surfaces/counts are documented.",
    }


def collect_plugin_surface() -> dict:
    output = run(["hermes", "plugins", "list"], 120)[1]
    enabled = len(re.findall(r"\benabled\b", output))
    not_enabled = len(re.findall(r"not enabled", output))
    # Public-safe category summary from visible plugin names; descriptions can mention env vars/secrets, so omit raw output.
    names = []
    for line in output.splitlines():
        m = re.match(r"^│\s*([a-zA-Z0-9_.-]+)\s+│\s+(enabled|not enabled)", line)
        if m:
            names.append({"name": m.group(1), "status": m.group(2)})
    return {
        "detected_plugins": names[:80],
        "enabled_count_estimate": max(0, enabled - not_enabled),
        "not_enabled_count_estimate": not_enabled,
        "note": "Plugin descriptions are omitted from the public inventory because they may mention credential/environment surfaces.",
    }


def collect_task_surface(cron_list: str) -> dict:
    jobs = parse_cron_blocks(cron_list)
    modes = {"no_agent": 0, "agent": 0, "unknown": 0}
    public_categories: dict[str, int] = {}
    for j in jobs:
        mode = (j.get("mode") or "").lower()
        if "no-agent" in mode or "no_agent" in mode:
            modes["no_agent"] += 1
        elif mode:
            modes["agent"] += 1
        else:
            modes["unknown"] += 1
        cat = j.get("category", "Other scheduled automation")
        public_categories[cat] = public_categories.get(cat, 0) + 1
    if modes["agent"] == 0 and modes["unknown"] == 0:
        modes["agent"] = max(0, len(jobs) - modes["no_agent"])
    return {
        "cron_total": len(jobs),
        "execution_modes": modes,
        "public_categories": dict(sorted(public_categories.items())),
        "jobs_public": jobs,
        "note": "Task names that expose personal/client workflows are replaced with category labels; schedules/scripts/modes are retained when safe.",
    }


def collect_inventory() -> dict:
    config_path = pathlib.Path.home() / ".hermes" / "config.yaml"
    cfg = load_yaml(config_path)

    hermes_version = run(["hermes", "--version"], 60)[1]
    gateway_status = run(["hermes", "gateway", "status"], 60)[1]
    cron_list = run(["hermes", "cron", "list", "--all"], 120)[1]
    mcp_list = run(["hermes", "mcp", "list"], 60)[1]
    tools_list = run(["hermes", "tools", "list"], 60)[1]
    profiles = run(["hermes", "profile", "list"], 60)[1]
    fallback = run(["hermes", "fallback", "list"], 60)[1]
    rules_list = run(["hermes", "rules", "list", "--all"], 60)[1]
    kanban_assignees = run(["hermes", "kanban", "assignees"], 60)[1]

    # LM Studio local status: no secrets involved.
    lmstudio = {"base_url": "http://127.0.0.1:1234/v1", "models": [], "chat_smoke": "not_run"}
    try:
        import urllib.request
        with urllib.request.urlopen("http://127.0.0.1:1234/v1/models", timeout=3) as r:
            data = json.loads(r.read().decode())
            lmstudio["models"] = [m.get("id") for m in data.get("data", []) if m.get("id")]
        # Try configured model only enough to classify current state.
        payload = json.dumps({
            "model": "gemma4unc",
            "messages": [{"role": "user", "content": "Reply with exactly: LOCAL_OK"}],
            "max_tokens": 20,
            "temperature": 0,
        }).encode()
        req = urllib.request.Request(
            "http://127.0.0.1:1234/v1/chat/completions",
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=20) as r:
            resp = json.loads(r.read().decode())
            lmstudio["chat_smoke"] = resp.get("choices", [{}])[0].get("message", {}).get("content", "")[:120]
    except Exception as e:
        msg = str(e)
        if hasattr(e, "read"):
            try:
                msg = e.read().decode("utf-8", "replace")[:500]
            except Exception:
                pass
        lmstudio["chat_smoke"] = f"blocked_or_unavailable: {msg[:240]}"

    providers = redact(cfg.get("providers", {}))
    custom_providers = redact(cfg.get("custom_providers", []))
    mcp_servers = redact(cfg.get("mcp_servers", {}))
    skills_surface = collect_skill_surface()
    hooks_surface = collect_hook_surface()
    plugins_surface = collect_plugin_surface()
    tasks_surface = collect_task_surface(cron_list)
    tools_surface = parse_tools_surface(tools_list)
    gateway_platforms = sorted({
        "telegram", "mattermost", "whatsapp", "api_server", "homeassistant"
    })

    # Cron category counts, not names, for public safety.
    cron_categories: dict[str, int] = {}
    for line in cron_list.splitlines():
        m = re.search(r"Name:\s+(.+)$", line)
        if m:
            cat = classify_cron_job(m.group(1))
            cron_categories[cat] = cron_categories.get(cat, 0) + 1

    inventory = {
        "generated_at": GENERATED_AT,
        "public_repo": PUBLIC_REPO,
        "host": {
            "primary": "Linux host running Hermes gateway as a systemd service",
            "windows_remote": "Windows workstation over SSH for desktop tasks",
            "timezone": "operator local timezone",
        },
        "hermes": {
            "version_output": hermes_version,
            "primary_model": redact(cfg.get("model", {})),
            "fallback_model": redact(cfg.get("fallback_model", {})),
            "providers": providers,
            "custom_providers": custom_providers,
            "auxiliary": redact(cfg.get("auxiliary", {})),
            "delegation": redact(cfg.get("delegation", {})),
            "memory": redact(cfg.get("memory", {})),
            "stt": redact(cfg.get("stt", {})),
            "tts": redact(cfg.get("tts", {})),
        },
        "gateway": {
            "status_summary": summarize_status(gateway_status),
            "platforms": gateway_platforms,
            "home_channels": "Configured privately; IDs are intentionally not published.",
        },
        "mcp": {
            "servers": mcp_servers,
            "list_output_sanitized": sanitize_text(mcp_list),
        },
        "tools": {
            "list_output_sanitized": sanitize_text(tools_list),
        },
        "profiles": {
            "output_sanitized": sanitize_text(profiles),
        },
        "orchestration": {
            "kanban": redact(cfg.get("kanban", {})),
            "safe_self_improvement": redact(cfg.get("session_automation", {})),
            "rules_summary": [
                "External agent resources are evidence sources; convert useful patterns into Hermes-native artifacts instead of direct-installing untrusted registries.",
                "Durable multi-step work should prefer Kanban with default/researcher/worker/reviewer profiles; delegate_task remains for bounded fork-join reasoning.",
                "Config/profile/rule/skill/private-architecture changes require verification and private backup before final reporting.",
            ],
            "kanban_assignees_sanitized": sanitize_text(kanban_assignees),
            "profile_team": ["default", "researcher", "worker", "reviewer"],
            "policy": "default is the interactive orchestrator; Kanban dispatcher launches researcher/worker/reviewer as ephemeral worker-runs when tasks are assigned.",
        },
        "fallback": {
            "output_sanitized": sanitize_text(fallback),
        },
        "scheduled_automation": {
            "active_job_categories": cron_categories,
            "note": "Exact job names are intentionally grouped for the public repo because some jobs reference private personal or client workflows.",
        },
        "operational_surfaces": {
            "tasks": tasks_surface,
            "skills": skills_surface,
            "hooks": hooks_surface,
            "plugins": plugins_surface,
            "tools": tools_surface,
        },
        "local_models": {
            "lm_studio": lmstudio,
            "note": "Main Hermes remains openai-codex/gpt-5.5. LM Studio is configured as an optional local provider, not the default.",
        },
     }
    return redact(inventory)


def sanitize_text(text: str) -> str:
    text = str(text)
    home = str(pathlib.Path.home())
    text = text.replace(home, "~")
    text = re.sub(r"\b[Mm]ich[a]el Gu[b]er\b", "Hermes operator", text)
    text = re.sub(r"\b[Mm]ich[a]el's\b", "the operator's", text)
    text = re.sub(r"\b[Mm]ich[a]el\b", "operator", text)
    text = re.sub(r"mich[a]el\.gu[b]er", "operator", text, flags=re.I)
    text = re.sub(r"mich[a]el@gu[b]er\.dev|gu[b]erm@gmail\.com", "[operator email omitted]", text, flags=re.I)
    text = re.sub(r"\bgu[b]erm\.github\.io\b", "public portfolio site", text, flags=re.I)
    text = re.sub(r"\bgu[b]erm\b", "repo-owner", text, flags=re.I)
    text = re.sub(r"(Token:|Authorization:|API_SERVER_KEY=|TELEGRAM_BOT_TOKEN=).*", r"\1 [REDACTED]", text)
    text = re.sub(r"telegram:-?\d+(?::\d+)?", "telegram:[REDACTED]", text)
    text = re.sub(r"mattermost:[^\s]+", "mattermost:[REDACTED]", text)
    text = re.sub(r"Bearer\s+[A-Za-z0-9._\-]+", "Bearer [REDACTED]", text)
    return text


def summarize_status(status: str) -> dict:
    active = "active (running)" in status or "Gateway is running" in status or "✓" in status
    m = re.search(r"Main PID:\s+(\d+)", status)
    return {
        "running": active,
        "pid_present": bool(m),
        "service": "hermes-gateway.service",
        "detail": "Systemd gateway service is enabled/running on the Linux host." if active else "Gateway status requires attention.",
    }


def provider_table(inv: dict) -> str:
    rows = []
    primary = inv["hermes"]["primary_model"]
    rows.append(("Primary", primary.get("provider", ""), primary.get("default", ""), "Default for Telegram/API/CLI gateway sessions"))
    fb = inv["hermes"].get("fallback_model", {})
    rows.append(("Fallback", fb.get("provider", ""), fb.get("model", ""), "Used when primary fails"))
    providers = inv["hermes"].get("providers", {}) or {}
    for name, cfg in providers.items():
        rows.append(("Optional provider", name, cfg.get("model", ""), cfg.get("base_url", "")))
    md = "| Role | Provider | Model | Notes |\n|---|---|---|---|\n"
    for r in rows:
        md += "| " + " | ".join(str(x).replace("|", "\\|") for x in r) + " |\n"
    return md


def cron_table(inv: dict) -> str:
    cats = inv["scheduled_automation"].get("active_job_categories", {})
    md = "| Category | Active jobs | Public-safe purpose |\n|---|---:|---|\n"
    descriptions = {
        "Backup & sync": "Protect configuration, repositories, databases, and knowledge stores.",
        "Knowledge & memory": "Keep GBrain/memory/context stores healthy and up to date.",
        "GitHub & publishing": "Maintain GitHub/publication surfaces and repo health digests.",
        "Home automation": "Log smart-home/home-environment telemetry.",
        "Private finance automation": "Private finance workflow snapshots; details omitted from public docs.",
        "Media/news monitoring": "News, RSS, YouTube, and briefing pipelines.",
        "Reliability watchdogs": "Auto-healing, environment guards, timeout/watchdog checks.",
        "Other scheduled automation": "Other local automation jobs.",
    }
    for cat, count in sorted(cats.items()):
        md += f"| {cat} | {count} | {descriptions.get(cat, 'Local automation.')} |\n"
    return md


def skill_category_table(inv: dict) -> str:
    skills = inv.get("operational_surfaces", {}).get("skills", {})
    cats = skills.get("categories", {})
    md = "| Skill category | Count |\n|---|---:|\n"
    for cat, count in sorted(cats.items()):
        md += f"| {cat} | {count} |\n"
    return md


def skill_examples_table(inv: dict) -> str:
    examples = inv.get("operational_surfaces", {}).get("skills", {}).get("public_examples", [])
    md = "| Skill | Category | Public-safe description |\n|---|---|---|\n"
    for ex in examples[:25]:
        md += f"| `{ex.get('name','')}` | {ex.get('category','')} | {str(ex.get('description','')).replace('|','/')} |\n"
    return md


def operational_surface_table(inv: dict) -> str:
    surf = inv.get("operational_surfaces", {})
    tasks = surf.get("tasks", {})
    skills = surf.get("skills", {})
    hooks = surf.get("hooks", {})
    plugins = surf.get("plugins", {})
    return dedent(f"""
    | Surface | Detected public-safe state | Notes |
    |---|---|---|
    | Scheduled tasks / cron | {tasks.get('cron_total', 0)} jobs; {tasks.get('execution_modes', {}).get('no_agent', 0)} no-agent script jobs; {tasks.get('execution_modes', {}).get('agent', 0)} agent-backed jobs | Exact private task names are grouped by category. |
    | Skills | {skills.get('total_detected', 0)} detected skill files across {len(skills.get('categories', {}))} categories | Private/client-sensitive skill names are omitted from examples. |
    | Hooks / webhooks | shell allowlist present: {hooks.get('shell_hooks_allowlist_present')}; allowlist entries: {hooks.get('shell_hooks_allowlist_entries')}; plugin hook manifests: {hooks.get('claude_plugin_hook_files_detected')} | Hook command bodies are not published. |
    | Plugins | {len(plugins.get('detected_plugins', []))} visible plugin rows captured; enabled estimate {plugins.get('enabled_count_estimate', 0)} | Descriptions omitted to avoid leaking credential/env surfaces. |
    | MCP servers | {len(inv.get('mcp', {}).get('servers', {}))} configured MCP servers | GBrain, NotebookLM, CodeGraph are the active core MCP surfaces. |
    """).strip().replace("\n    ", "\n") + "\n"


def hook_examples_table(inv: dict) -> str:
    hooks = inv.get("operational_surfaces", {}).get("hooks", {})
    files = hooks.get("public_hook_file_examples", [])
    md = "| Hook manifest surface |\n|---|\n"
    for f in files[:20]:
        # Keep only relative paths; these are plugin/package surfaces, not hook bodies.
        md += f"| `{f}` |\n"
    if not files:
        md += "| none detected |\n"
    return md


def plugin_table(inv: dict) -> str:
    plugins = inv.get("operational_surfaces", {}).get("plugins", {}).get("detected_plugins", [])
    md = "| Plugin | Status |\n|---|---|\n"
    for p in plugins[:30]:
        md += f"| `{p.get('name','')}` | {p.get('status','')} |\n"
    if not plugins:
        md += "| none parsed | n/a |\n"
    return md


def generate_markdown(inv: dict) -> str:
    lm = inv["local_models"]["lm_studio"]
    lm_status = "available" if lm.get("models") else "not reachable"
    local_try = lm.get("chat_smoke", "")
    return dedent(f"""
    # Hermes Agent Architecture

    > Public-safe architecture snapshot generated at `{inv['generated_at']}`.
    >
    > Source of truth: local Hermes configuration and runtime status on the operator Linux host.
    >
    > Sensitive values, private chat IDs, OAuth headers, personal finance/client workflow names, and tokens are intentionally omitted or grouped.

    ## Executive Summary

    Hermes Agent runs as a **Linux-primary, multi-platform AI operations hub**. The gateway is a systemd service that connects Telegram, Mattermost, WhatsApp, API Server, Home Assistant, MCP servers, cron jobs, skills, memory/context stores, and remote Windows operations.

The current architecture adds a **durable Kanban orchestration layer**: `default` remains the interactive/orchestrator profile, while `researcher`, `worker`, and `reviewer` are launched as ephemeral Kanban worker-runs for durable research, implementation, and verification tasks. Safe post-session automation generates local review artifacts (session summaries, skill-mining candidates, trace-derived code graphs) without silently installing skills or uploading traces.

    The default model remains **`openai-codex / gpt-5.5`**. Local/experimental providers such as **LM Studio** and **Free Kimi** are configured as optional providers only; they are not the default route for Telegram or production workflows.

    ## High-Level Architecture

    ![Hermes Architecture](docs/hermes-architecture.svg)

    ## Runtime Topology

    | Layer | Components | Notes |
    |---|---|---|
    | User channels | Telegram, Mattermost, WhatsApp, API Server | Gateway adapters route inbound messages into the same Hermes agent core. |
    | Agent core | Hermes Agent gateway + CLI + tool loop | Runs on Linux under `hermes-gateway.service`. |
    | Models | OpenAI Codex primary, Copilot fallback, optional LM Studio, optional Free Kimi proxy | Provider selection is explicit; experimental endpoints are not default. |
    | Tools | Terminal, files, browser, web, vision, TTS, cron, delegation, Home Assistant, GBrain, NotebookLM, CodeGraph | Enabled toolsets differ by platform/session but the gateway exposes the main operational surface. |
    | Knowledge | GBrain, NotebookLM, session search, imported Claude context, skills | Long-term memory and research context are split across structured stores and markdown skills. |
    | Automation | Hermes cron scheduler, no-agent scripts, hooks, plugins, post-session automation | Backups, monitoring, GitHub publication, finance snapshots, smart-home logging, news/media digests, watchdogs, session summaries, skill-mining reviews, and trace graphs. |
    | Durable orchestration | Kanban dispatcher + `default`/`researcher`/`worker`/`reviewer` profiles | The gateway dispatcher claims ready tasks and launches profile-specific worker-runs; `stopped` profiles are normal idle state. |
    | Operational surfaces | Tasks, skills, rules, hooks, plugins, MCP servers, toolsets | Documented as public-safe counts/categories plus selected non-sensitive examples. |
    | Remote systems | Windows workstation over SSH, Home Assistant, Google Drive/GitHub, local LM Studio | Linux remains the control plane; Windows is operated remotely when needed. |

    ## Operational Surface Inventory

    {operational_surface_table(inv)}

    ### Scheduled tasks / cron categories

    {cron_table(inv)}

    ### Skills surface

    Hermes currently has a broad skill surface. The public inventory lists category counts and non-sensitive examples only.

    {skill_category_table(inv)}

    Public-safe skill examples:

    {skill_examples_table(inv)}

    ### Hooks, webhooks, and plugin hook manifests

    Hermes has multiple hook-related surfaces: shell-hook allowlists, webhook subscriptions, and imported Claude/Claude plugin hook manifests. The public repo records only surface/count information, not hook command bodies.

    {hook_examples_table(inv)}

    ### Plugin surface

    {plugin_table(inv)}

    ## Low-Level Surface Files

    The repository includes dedicated, low-level public-safe files for each operational surface:

    | File | Contents |
    |---|---|
    | [`docs/surfaces/tasks.md`](docs/surfaces/tasks.md) | Scheduled tasks/cron jobs, modes, scripts, schedules, delivery class, workdir class. |
    | [`docs/surfaces/skills.md`](docs/surfaces/skills.md) | Skill categories, counts, public-safe examples, operational semantics. |
    | [`docs/surfaces/hooks.md`](docs/surfaces/hooks.md) | Shell hook allowlist state, webhook state, plugin hook manifests. |
    | [`docs/surfaces/plugins.md`](docs/surfaces/plugins.md) | Hermes plugin registry rows and status. |
    | [`docs/surfaces/mcp-and-toolsets.md`](docs/surfaces/mcp-and-toolsets.md) | MCP servers and toolset count estimates. |
    | [`docs/surfaces/models-and-gateway.md`](docs/surfaces/models-and-gateway.md) | Model routing, gateway status, channel/platform surface. |
    | [`docs/surfaces/orchestration.md`](docs/surfaces/orchestration.md) | Kanban profiles, rules layer, self-improvement automation, and operating contract. |

    ## Model Routing

    {provider_table(inv)}

    ### Local model trial status

    | Item | Status |
    |---|---|
    | LM Studio endpoint | `{lm_status}` at `{lm.get('base_url')}` |
    | Reported model IDs | `{', '.join(lm.get('models') or []) or 'none'}` |
    | Chat smoke test | `{str(local_try).replace('`', '')[:300]}` |
    | Safety decision | Main Hermes remains `openai-codex/gpt-5.5`; local provider is optional until a model can load reliably. |

    ## MCP and External Tooling

    | MCP server | Transport | Public-safe purpose |
    |---|---|---|
    | `gbrain` | Local HTTP MCP on `127.0.0.1:3131/mcp` | Personal knowledge graph, memory, code graph, facts, schema tools. |
    | `notebooklm` | `npx notebooklm-mcp@latest` | Grounded research over registered Google NotebookLM notebooks. |
    | `codegraph` | Local Node command | Code intelligence over selected repositories. |

    ## Scheduled Automation

    {cron_table(inv)}

    ## Agentic Operating Model

    {orchestration_table(inv)}

    The important runtime distinction is that `researcher`, `worker`, and `reviewer` do **not** need to be continuously running gateway profiles. They are idle until a Kanban task is assigned to them; then the gateway dispatcher starts a worker-run for that profile and the worker completes, blocks, or retries the task.

    ## Current Profiles

    The live system currently exposes the public-safe profile roster as:

    ```text
    {inv['profiles']['output_sanitized'][:1800]}
    ```

    Current profile contract:

    | Profile | Role | Runtime behavior |
    |---|---|---|
    | `default` | Interactive orchestrator | Stays running in Telegram/API/CLI gateway; routes work. |
    | `researcher` | Research/due-diligence worker | Normally stopped; launched by Kanban for evidence gathering. |
    | `worker` | Implementation/execution worker | Normally stopped; fallback assignee for durable tasks. |
    | `reviewer` | Independent verification worker | Normally stopped; launched for review/regression/security checks. |

    ## Reliability and Safety Boundaries

    - Public repo does **not** publish secrets, chat IDs, API keys, OAuth tokens, cookies, private finance details, or client-specific payloads.
    - The gateway is supervised by systemd and multiple watchdog cron jobs.
    - GBrain runs through a shared local HTTP MCP server to avoid PGLite lock contention.
    - Backups and sync jobs run through cron with Google Drive/GitHub targets.
    - Windows is treated as a remote worker controlled via SSH, not as the primary Hermes control plane.
    - Experimental providers are explicitly optional and must pass direct API + Hermes smoke tests before being used for real agent work.

    ## Operational Notes

    - Hermes version/status summary:

    ```text
    {inv['hermes']['version_output'][:1200]}
    ```

    - Fallback chain:

    ```text
    {inv['fallback']['output_sanitized'][:1200]}
    ```

    - MCP list:

    ```text
    {inv['mcp']['list_output_sanitized'][:1200]}
    ```

    ## Maintenance

    This repository is regenerated by `scripts/update_architecture.py`. The updater is designed to be safe for a public repository:

    1. collect local Hermes runtime state,
    2. redact secrets and private identifiers,
    3. group sensitive scheduled jobs by category,
    4. regenerate Markdown, SVG, HTML, JSON inventory, and PDF,
    5. commit and push only if files changed.

    ## Source Files

    - `ARCHITECTURE.md` - canonical public architecture document.
    - `docs/hermes-architecture.svg` - standalone diagram.
    - `docs/hermes-architecture.html` - browser-friendly diagram page.
    - `docs/Hermes-Architecture.pdf` - rendered PDF copy.
    - `docs/surfaces/*.md` - low-level public-safe inventories for tasks, skills, hooks, plugins, MCP/toolsets, and gateway/model routing.
    - `data/inventory.public.json` - redacted machine-readable snapshot.
    - `scripts/update_architecture.py` - public-safe regeneration script.
    """).strip().replace("\n    ", "\n") + "\n"


def svg_diagram(inv: dict) -> str:
    generated = html.escape(inv["generated_at"])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="860" viewBox="0 0 1280 860" role="img" aria-label="Hermes Agent Architecture">
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M 40 0 L 0 0 0 40" fill="none" stroke="#1e293b" stroke-width="0.5"/></pattern>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L0,6 L9,3 z" fill="#64748b"/></marker>
    <style>
      .bg{{fill:#020617}} .title{{font:700 24px 'JetBrains Mono',monospace;fill:#e2e8f0}} .sub{{font:12px 'JetBrains Mono',monospace;fill:#94a3b8}}
      .box-title{{font:700 14px 'JetBrains Mono',monospace;fill:#f8fafc}} .box-sub{{font:10px 'JetBrains Mono',monospace;fill:#cbd5e1}}
      .small{{font:9px 'JetBrains Mono',monospace;fill:#cbd5e1}} .line{{stroke:#64748b;stroke-width:1.8;marker-end:url(#arrow);fill:none}}
      .dash{{stroke-dasharray:6 4}} .front{{fill:#082f49;stroke:#22d3ee}} .back{{fill:#064e3b;stroke:#34d399}}
      .db{{fill:#3b0764;stroke:#c4b5fd}} .cloud{{fill:#451a03;stroke:#fbbf24}} .sec{{fill:#4c0519;stroke:#fb7185}}
      .ext{{fill:#1e293b;stroke:#cbd5e1}} .bus{{fill:#431407;stroke:#fb923c}}
    </style>
  </defs>
  <rect class="bg" width="1280" height="860"/><rect width="1280" height="860" fill="url(#grid)" opacity="0.55"/>
  <text x="40" y="52" class="title">Hermes Agent Architecture</text>
  <text x="40" y="76" class="sub">Public-safe generated snapshot · {generated}</text>

  <!-- Flows -->
  <path class="line" d="M215 190 C300 190 300 330 385 330"/>
  <path class="line" d="M215 295 C300 295 300 330 385 330"/>
  <path class="line" d="M215 400 C300 400 300 330 385 330"/>
  <path class="line" d="M545 330 C625 330 625 160 705 160"/>
  <path class="line" d="M545 330 C625 330 625 265 705 265"/>
  <path class="line" d="M545 330 C625 330 625 370 705 370"/>
  <path class="line" d="M545 330 C625 330 625 480 705 480"/>
  <path class="line" d="M865 160 C935 160 935 205 1005 205"/>
  <path class="line" d="M865 265 C935 265 935 315 1005 315"/>
  <path class="line" d="M865 370 C935 370 935 430 1005 430"/>
  <path class="line" d="M545 330 C625 330 625 600 705 600"/>
  <path class="line dash" d="M545 330 C620 520 745 705 1005 695"/>

  <!-- User channels -->
  <g><rect x="40" y="135" width="175" height="70" rx="8" fill="#0f172a"/><rect x="40" y="135" width="175" height="70" rx="8" class="front" stroke-width="1.6"/><text x="60" y="165" class="box-title">Telegram</text><text x="60" y="185" class="box-sub">primary mobile UX</text></g>
  <g><rect x="40" y="240" width="175" height="70" rx="8" fill="#0f172a"/><rect x="40" y="240" width="175" height="70" rx="8" class="front" stroke-width="1.6"/><text x="60" y="270" class="box-title">Mattermost</text><text x="60" y="290" class="box-sub">workbench/home lane</text></g>
  <g><rect x="40" y="345" width="175" height="70" rx="8" fill="#0f172a"/><rect x="40" y="345" width="175" height="70" rx="8" class="front" stroke-width="1.6"/><text x="60" y="375" class="box-title">WhatsApp/API</text><text x="60" y="395" class="box-sub">secondary channels</text></g>

  <!-- Core -->
  <g><rect x="365" y="270" width="200" height="120" rx="10" fill="#0f172a"/><rect x="365" y="270" width="200" height="120" rx="10" class="back" stroke-width="2"/><text x="390" y="305" class="box-title">Hermes Gateway</text><text x="390" y="328" class="box-sub">systemd service on Linux</text><text x="390" y="350" class="box-sub">tool loop · skills · rules</text><text x="390" y="372" class="box-sub">Kanban · memory · plugins</text></g>

  <!-- Models -->
  <g><rect x="705" y="115" width="190" height="80" rx="8" fill="#0f172a"/><rect x="705" y="115" width="190" height="80" rx="8" class="cloud" stroke-width="1.6"/><text x="728" y="148" class="box-title">OpenAI Codex</text><text x="728" y="170" class="box-sub">primary gpt-5.5</text></g>
  <g><rect x="705" y="220" width="190" height="80" rx="8" fill="#0f172a"/><rect x="705" y="220" width="190" height="80" rx="8" class="cloud" stroke-width="1.6"/><text x="728" y="253" class="box-title">Copilot</text><text x="728" y="275" class="box-sub">fallback + aux gpt-5.4</text></g>
  <g><rect x="705" y="325" width="190" height="80" rx="8" fill="#0f172a"/><rect x="705" y="325" width="190" height="80" rx="8" class="bus" stroke-width="1.6"/><text x="728" y="358" class="box-title">LM Studio</text><text x="728" y="380" class="box-sub">optional local provider</text></g>
  <g><rect x="705" y="430" width="190" height="80" rx="8" fill="#0f172a"/><rect x="705" y="430" width="190" height="80" rx="8" class="bus" stroke-width="1.6"/><text x="728" y="463" class="box-title">Free Kimi Proxy</text><text x="728" y="485" class="box-sub">experimental reserve only</text></g>

  <!-- Knowledge/tools -->
  <g><rect x="1005" y="165" width="220" height="80" rx="8" fill="#0f172a"/><rect x="1005" y="165" width="220" height="80" rx="8" class="db" stroke-width="1.6"/><text x="1030" y="198" class="box-title">GBrain MCP</text><text x="1030" y="220" class="box-sub">knowledge graph · facts · code</text></g>
  <g><rect x="1005" y="275" width="220" height="80" rx="8" fill="#0f172a"/><rect x="1005" y="275" width="220" height="80" rx="8" class="db" stroke-width="1.6"/><text x="1030" y="308" class="box-title">NotebookLM MCP</text><text x="1030" y="330" class="box-sub">grounded research notebooks</text></g>
  <g><rect x="1005" y="390" width="220" height="80" rx="8" fill="#0f172a"/><rect x="1005" y="390" width="220" height="80" rx="8" class="db" stroke-width="1.6"/><text x="1030" y="423" class="box-title">CodeGraph MCP</text><text x="1030" y="445" class="box-sub">repository code intelligence</text></g>

  <!-- Automation / external -->
  <g><rect x="705" y="555" width="220" height="90" rx="8" fill="#0f172a"/><rect x="705" y="555" width="220" height="90" rx="8" class="sec" stroke-width="1.6"/><text x="730" y="590" class="box-title">Kanban / Automation</text><text x="730" y="612" class="box-sub">cron · post-session reviews</text><text x="730" y="632" class="box-sub">researcher · worker · reviewer</text></g>
  <g><rect x="1005" y="650" width="220" height="90" rx="8" fill="#0f172a"/><rect x="1005" y="650" width="220" height="90" rx="8" class="ext" stroke-width="1.6"/><text x="1030" y="685" class="box-title">External Systems</text><text x="1030" y="707" class="box-sub">Windows SSH · Home Assistant</text><text x="1030" y="727" class="box-sub">GitHub · Google Drive</text></g>

  <!-- Legend -->
  <g transform="translate(40 760)"><text class="box-title" x="0" y="0">Legend</text><rect x="0" y="18" width="18" height="12" class="front"/><text x="26" y="29" class="small">User channels</text><rect x="150" y="18" width="18" height="12" class="back"/><text x="176" y="29" class="small">Hermes core</text><rect x="300" y="18" width="18" height="12" class="cloud"/><text x="326" y="29" class="small">Cloud model</text><rect x="450" y="18" width="18" height="12" class="db"/><text x="476" y="29" class="small">Knowledge/MCP</text><rect x="620" y="18" width="18" height="12" class="sec"/><text x="646" y="29" class="small">Automation</text><rect x="790" y="18" width="18" height="12" class="ext"/><text x="816" y="29" class="small">External systems</text></g>
</svg>'''


def html_diagram(svg: str) -> str:
    return f"""<!doctype html>
<html lang=\"en\">
<head>
<meta charset=\"utf-8\">
<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">
<title>Hermes Architecture</title>
<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">
<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>
<link href=\"https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap\" rel=\"stylesheet\">
<style>
body {{ margin:0; background:#020617; color:#e2e8f0; font-family:'JetBrains Mono', monospace; }}
.wrap {{ max-width:1320px; margin:0 auto; padding:28px; }}
.card {{ border:1px solid #1e293b; border-radius:18px; background:#0f172a; box-shadow:0 20px 60px rgba(0,0,0,.35); overflow:auto; }}
.summary {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:16px; margin-top:18px; }}
.info {{ border:1px solid #1e293b; background:#0b1120; border-radius:14px; padding:16px; }}
h1 {{ font-size:24px; }} p,li {{ color:#cbd5e1; font-size:13px; line-height:1.6; }}
a {{ color:#22d3ee; }}
</style>
</head>
<body><div class=\"wrap\">
<h1>Hermes Agent Architecture</h1>
<p>Public-safe, generated architecture view. Sensitive values and private workflow details are intentionally omitted.</p>
<div class=\"card\">{svg}</div>
<div class=\"summary\">
<div class=\"info\"><h3>Primary Control Plane</h3><p>Linux-hosted Hermes Gateway under systemd, with Telegram as the main mobile interface.</p></div>
<div class=\"info\"><h3>Model Strategy</h3><p>OpenAI Codex gpt-5.5 primary, Copilot fallback, LM Studio and Free Kimi as optional providers only.</p></div>
<div class=\"info\"><h3>Knowledge & Operations</h3><p>GBrain, NotebookLM, CodeGraph, tasks, skills, hooks, plugins, cron jobs, backups, watchdogs, and remote Windows operations.</p></div>
</div>
<p>Canonical document: <a href=\"../ARCHITECTURE.md\">ARCHITECTURE.md</a></p>
</div></body></html>
"""


def task_details_doc(inv: dict) -> str:
    tasks = inv.get("operational_surfaces", {}).get("tasks", {})
    rows = tasks.get("jobs_public", [])
    md = ["# Scheduled Tasks and Cron Jobs", "", "Public-safe low-level inventory of Hermes scheduled automation. Private/client-sensitive names are grouped, but schedules, execution modes, scripts, and workdirs are retained when safe.", ""]
    md.append("| Task | Category | Schedule | Mode | Script | Delivery | Workdir | Last run |")
    md.append("|---|---|---|---|---|---|---|---|")
    for j in rows:
        md.append("| " + " | ".join(clean_md_cell(j.get(k, "")) for k in ["name", "category", "schedule", "mode", "script", "deliver", "workdir", "last_run"]) + " |")
    md += ["", "## Execution model", "", "- **no-agent script jobs**: scheduler executes a script and delivers stdout verbatim; empty stdout means silent success.", "- **agent-backed jobs**: scheduler injects context/script output into Hermes and lets the agent reason before delivering a response.", "- **private delivery targets** are intentionally collapsed to `configured private channel`.", ""]
    return "\n".join(md)


def skills_details_doc(inv: dict) -> str:
    skills = inv.get("operational_surfaces", {}).get("skills", {})
    md = ["# Skills Surface", "", "Low-level public-safe view of installed Hermes skill packs and categories. Private/client-specific skills are counted but not fully listed.", "", "## Category counts", "", "| Category | Count |", "|---|---:|"]
    for cat, count in sorted((skills.get("categories") or {}).items()):
        md.append(f"| {clean_md_cell(cat)} | {count} |")
    md += ["", "## Public-safe examples", "", "| Skill | Category | Description |", "|---|---|---|"]
    for ex in skills.get("public_examples", []):
        md.append(f"| `{clean_md_cell(ex.get('name'))}` | {clean_md_cell(ex.get('category'))} | {clean_md_cell(ex.get('description'))} |")
    md += ["", "## Operational meaning", "", "- Skills are markdown procedure packs loaded into the agent context when relevant.", "- They cover domains such as software development, DevOps, research, media, productivity, ML/MLOps, smart home, and creative generation.", "- The public repository documents the skill surface, not private procedural contents or secrets.", ""]
    return "\n".join(md)


def hooks_details_doc(inv: dict) -> str:
    hooks = inv.get("operational_surfaces", {}).get("hooks", {})
    md = ["# Hooks, Webhooks, and Hook Manifests", "", "Public-safe low-level inventory of hook surfaces. Hook command bodies and private runtime payloads are not published.", "", "| Surface | Value |", "|---|---|", f"| Shell hooks allowlist present | {hooks.get('shell_hooks_allowlist_present')} |", f"| Shell hooks allowlist entries | {hooks.get('shell_hooks_allowlist_entries')} |", f"| Plugin hook manifests detected | {hooks.get('claude_plugin_hook_files_detected')} |", f"| Webhook summary | {clean_md_cell(hooks.get('webhook_summary'))} |", "", "## Hook manifest paths", "", "| Relative path |", "|---|"]
    for f in hooks.get("public_hook_file_examples", []):
        md.append(f"| `{clean_md_cell(f)}` |")
    md += ["", "## Boundaries", "", "- Hook manifest paths are published to document extension points.", "- Hook bodies, command lines, environment variables, tokens, and private payloads are intentionally excluded.", ""]
    return "\n".join(md)


def plugins_details_doc(inv: dict) -> str:
    plugins = inv.get("operational_surfaces", {}).get("plugins", {})
    md = ["# Plugin Surface", "", "Public-safe Hermes plugin inventory. Descriptions are omitted because plugin metadata can mention credential and environment-variable surfaces.", "", "| Plugin | Status |", "|---|---|"]
    for p in plugins.get("detected_plugins", []):
        md.append(f"| `{clean_md_cell(p.get('name'))}` | {clean_md_cell(p.get('status'))} |")
    md += ["", "## Notes", "", "- Providers, browser backends, dashboard auth, cron providers, and media providers can appear as plugins.", "- Enabled/disabled state is parsed from the Hermes plugin registry output and is best-effort for public docs.", ""]
    return "\n".join(md)


def mcp_tools_details_doc(inv: dict) -> str:
    tools = inv.get("operational_surfaces", {}).get("tools", {})
    md = ["# MCP Servers and Toolsets", "", "Low-level public-safe view of model-facing integration surfaces.", "", "## MCP servers", "", "| Server | Public-safe config |", "|---|---|"]
    for name, cfg in (inv.get("mcp", {}).get("servers") or {}).items():
        md.append(f"| `{clean_md_cell(name)}` | `{clean_md_cell(json.dumps(cfg, ensure_ascii=False))}` |")
    md += ["", "## Toolset counts parsed from CLI", "", "| Toolset | Count estimate |", "|---|---:|"]
    for ts, count in (tools.get("toolset_counts_estimate") or {}).items():
        md.append(f"| {clean_md_cell(ts)} | {count} |")
    md += ["", "## Integration contract", "", "- MCP servers expand Hermes with external tool schemas at runtime.", "- Toolsets gate high-risk surfaces such as terminal, file editing, browser automation, cron management, Home Assistant, image generation, and TTS.", "- Exact tool schemas are runtime-generated and not fully duplicated in the public repo.", ""]
    return "\n".join(md)



def orchestration_table(inv: dict) -> str:
    orch = inv.get("orchestration", {})
    kanban = orch.get("kanban", {}) or {}
    session_auto = (orch.get("safe_self_improvement") or orch.get("session_automation") or {})
    rows = [
        ("Interactive orchestrator", "default", "Main Telegram/API/CLI profile; decides whether to answer directly, delegate, create Kanban work, or schedule cron."),
        ("Research lane", "researcher", "Evidence-backed OSS/docs/web due diligence and adoption recommendations."),
        ("Execution lane", "worker", "File/terminal/code/config implementation and verification for durable work items."),
        ("Review lane", "reviewer", "Independent review, regression checks, security/config sanity, and final validation."),
        ("Default assignee", kanban.get("default_assignee", "worker"), "Fallback when a task/decomposer does not choose a specialist."),
        ("Failure limit", kanban.get("failure_limit", ""), "Raised above the previous aggressive default to avoid noisy retry failures."),
        ("Per-profile concurrency", kanban.get("max_in_progress_per_profile", ""), "Keeps one profile from saturating model/API/browser capacity."),
        ("Post-session automation", "enabled" if session_auto.get("enabled") else "disabled", "Generates review artifacts only; does not auto-install remote skills or mutate active prompts."),
    ]
    md = "| Item | Value | Meaning |\n|---|---|---|\n"
    for item, value, meaning in rows:
        md += f"| {clean_md_cell(item)} | `{clean_md_cell(value)}` | {clean_md_cell(meaning)} |\n"
    return md


def orchestration_details_doc(inv: dict) -> str:
    orch = inv.get("orchestration", {})
    kanban = orch.get("kanban", {}) or {}
    session_auto = (orch.get("safe_self_improvement") or orch.get("session_automation") or {})
    md = [
        "# Kanban, Profiles, Rules, and Self-Improvement",
        "",
        "Public-safe view of the durable orchestration layer added around the Hermes gateway.",
        "",
        "## Profile team",
        "",
        orchestration_table(inv),
        "",
        "## Live Kanban assignees",
        "",
        "```text",
        str(orch.get("kanban_assignees_sanitized", ""))[:3000],
        "```",
        "",
        "## Active orchestration config",
        "",
        "```json",
        json.dumps({"kanban": kanban, "safe_self_improvement": session_auto}, indent=2, ensure_ascii=False),
        "```",
        "",
        "## Rules layer",
        "",
        "| Rule theme | Public-safe behavior |",
        "|---|---|",
        *[f"| Operating rule | {clean_md_cell(rule)} |" for rule in orch.get("rules_summary", [])],
        "",
        "## Operating contract",
        "",
        "- `default` is the interactive/orchestrator profile and remains running in the gateway.",
        "- `researcher`, `worker`, and `reviewer` normally show as stopped/idle; the Kanban dispatcher launches them as worker-runs when a task is assigned.",
        "- Durable multi-step work should go through Kanban; short fork-join reasoning can still use subagent delegation.",
        "- External repos/tool lists are treated as evidence sources, not trusted installers; useful ideas become Hermes-native skills, rules, docs, config, Kanban tasks, or sandbox pilots.",
        "- Post-session automation writes local review artifacts only: summaries, skill-mining candidates, and trace-derived graph reports.",
        "",
    ]
    return "\n".join(md)


def models_gateway_details_doc(inv: dict) -> str:
    md = ["# Models, Gateway, and Runtime Routing", "", "Low-level public-safe runtime routing document.", "", "## Model/provider routing", "", provider_table(inv), "", "## Gateway", "", "| Item | Value |", "|---|---|", f"| Service | `{clean_md_cell(inv.get('gateway',{}).get('status_summary',{}).get('service'))}` |", f"| Running | `{clean_md_cell(inv.get('gateway',{}).get('status_summary',{}).get('running'))}` |", f"| Platforms | `{clean_md_cell(', '.join(inv.get('gateway',{}).get('platforms', [])))}` |", "", "## Local model status", "", "| Item | Value |", "|---|---|"]
    lm = inv.get("local_models", {}).get("lm_studio", {})
    md.append(f"| LM Studio base URL | `{clean_md_cell(lm.get('base_url'))}` |")
    md.append(f"| Model IDs | `{clean_md_cell(', '.join(lm.get('models') or []))}` |")
    md.append(f"| Chat smoke test | `{clean_md_cell(lm.get('chat_smoke'))}` |")
    md += ["", "## Safety routing", "", "- Primary remains OpenAI Codex `gpt-5.5`.", "- Copilot remains fallback.", "- LM Studio and Free Kimi are optional/experimental providers until they pass reliable smoke tests.", ""]
    return "\n".join(md)


def write_surface_docs(inv: dict) -> None:
    SURFACES.mkdir(parents=True, exist_ok=True)
    docs = {
        "index.md": "\n".join([
            "# Low-Level Hermes Operational Surfaces",
            "",
            "Public-safe detailed inventory files generated from the live Hermes runtime.",
            "",
            "| File | Surface |",
            "|---|---|",
            "| [`tasks.md`](tasks.md) | Scheduled tasks / cron jobs, schedules, scripts, execution modes, delivery classes. |",
            "| [`skills.md`](skills.md) | Installed skill categories, counts, public-safe examples, operational semantics. |",
            "| [`hooks.md`](hooks.md) | Shell hook allowlist state, webhooks, plugin hook manifests. |",
            "| [`plugins.md`](plugins.md) | Hermes plugin registry status rows. |",
            "| [`mcp-and-toolsets.md`](mcp-and-toolsets.md) | MCP server configs and toolset count estimates. |",
            "| [`models-and-gateway.md`](models-and-gateway.md) | Model routing, gateway status, platform surface. |",
            "| [`orchestration.md`](orchestration.md) | Kanban profiles, rules layer, self-improvement automation, and operating contract. |",
            "",
            "Private/client-sensitive names, command bodies, IDs, tokens, cookies, and secrets are intentionally omitted or grouped.",
            "",
        ]),
        "tasks.md": task_details_doc(inv),
        "skills.md": skills_details_doc(inv),
        "hooks.md": hooks_details_doc(inv),
        "plugins.md": plugins_details_doc(inv),
        "mcp-and-toolsets.md": mcp_tools_details_doc(inv),
        "models-and-gateway.md": models_gateway_details_doc(inv),
        "orchestration.md": orchestration_details_doc(inv),
    }
    for name, body in docs.items():
        (SURFACES / name).write_text(body, encoding="utf-8")


def md_title(text: str, fallback: str) -> str:
    for line in text.splitlines()[:80]:
        if line.startswith('# '):
            return line[2:].strip()
    return fallback


def md_summary(text: str, max_chars: int = 220) -> str:
    out: list[str] = []
    in_code = False
    for line in text.splitlines():
        if line.startswith('```'):
            in_code = not in_code
            continue
        if in_code:
            continue
        s = line.strip()
        if not s or s.startswith('#') or s.startswith('|') or s.startswith('!['):
            continue
        if s.startswith('- '):
            s = s[2:].strip()
        out.append(s)
        if sum(len(x) for x in out) >= max_chars:
            break
    joined = ' '.join(out).strip()
    return joined[:max_chars] + ('…' if len(joined) > max_chars else '')


def interactive_tags(name: str, text: str) -> list[str]:
    blob = f"{name}\n{text}".lower()
    rules = [
        ('models', ['model', 'provider', 'gateway', 'openai', 'copilot', 'lm studio']),
        ('automation', ['cron', 'task', 'schedule', 'watchdog', 'automation', 'kanban', 'dispatcher']),
        ('tools', ['mcp', 'toolset', 'tool ', 'tools']),
        ('skills', ['skill', 'agent rules', 'rules layer']),
        ('plugins', ['plugin', 'hook', 'webhook']),
        ('surfaces', ['surface', 'route', 'domain', 'public', 'cloudflare', 'caddy']),
        ('data', ['inventory', 'json', 'snapshot']),
        ('security', ['secret', 'token', 'redacted', 'omitted', 'private']),
    ]
    tags = [tag for tag, needles in rules if any(n in blob for n in needles)]
    return tags or ['overview']


def build_interactive_records(inv: dict, arch_md: str) -> list[dict]:
    records: list[dict] = []
    def add(kind: str, name: str, title: str, content: str, path: str, tags: list[str] | None = None) -> None:
        records.append({
            'kind': kind,
            'name': name,
            'title': title,
            'summary': md_summary(content),
            'path': path,
            'tags': tags or interactive_tags(name, content),
            'content': content,
        })
    add('document', 'ARCHITECTURE.md', md_title(arch_md, 'Hermes Architecture'), arch_md, 'ARCHITECTURE.md', ['overview', 'surfaces', 'automation', 'models'])
    for p in sorted(SURFACES.glob('*.md')):
        text = p.read_text(encoding='utf-8', errors='replace')
        add('surface', p.name, md_title(text, p.stem), text, f'docs/surfaces/{p.name}')
    for key, value in sorted(inv.items()):
        if key == 'generated_at':
            continue
        body = f"# Inventory: {key}\n\n```json\n{json.dumps(value, indent=2, ensure_ascii=False)}\n```\n"
        add('inventory', key, f'Inventory: {key}', body, f'data/inventory.public.json#{key}', ['data'] + interactive_tags(key, body))
    add('asset', 'diagram', 'Architecture diagram', '# Architecture diagram\n\nOpen the SVG/HTML diagram or PDF from the quick links.\n', 'docs/hermes-architecture.svg', ['overview', 'surfaces'])
    return records


def public_markdown_to_html(text: str) -> str:
    out: list[str] = []
    lines = text.splitlines()
    i = 0
    in_list = False
    def close_list() -> None:
        nonlocal in_list
        if in_list:
            out.append('</ul>')
            in_list = False
    while i < len(lines):
        line = lines[i]
        if line.startswith('```'):
            close_list()
            lang = html.escape(line[3:].strip())
            code: list[str] = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code.append(lines[i])
                i += 1
            out.append(f'<pre data-lang="{lang}"><code>{html.escape(chr(10).join(code))}</code></pre>')
        elif line.startswith('#'):
            close_list()
            level = min(len(line) - len(line.lstrip('#')), 4)
            label = html.escape(line[level:].strip())
            out.append(f'<h{level}>{label}</h{level}>')
        elif line.startswith('|') and i + 1 < len(lines) and lines[i+1].startswith('|'):
            close_list()
            table_lines: list[str] = []
            while i < len(lines) and lines[i].startswith('|'):
                table_lines.append(lines[i])
                i += 1
            headers = [c.strip() for c in table_lines[0].strip('|').split('|')]
            out.append('<div class="table-wrap"><table><thead><tr>' + ''.join(f'<th>{html.escape(c)}</th>' for c in headers) + '</tr></thead><tbody>')
            for row in table_lines[2:]:
                cells = [c.strip().replace('<br>', ' ') for c in row.strip('|').split('|')]
                out.append('<tr>' + ''.join(f'<td>{html.escape(c)}</td>' for c in cells) + '</tr>')
            out.append('</tbody></table></div>')
            continue
        elif line.strip().startswith('- '):
            if not in_list:
                out.append('<ul>')
                in_list = True
            out.append(f'<li>{html.escape(line.strip()[2:])}</li>')
        elif not line.strip():
            close_list()
        else:
            close_list()
            s = html.escape(line.strip())
            s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
            out.append(f'<p>{s}</p>')
        i += 1
    close_list()
    return '\n'.join(out)


def write_interactive_site(inv: dict, arch_md: str) -> None:
    records = build_interactive_records(inv, arch_md)
    rendered = []
    for r in records:
        rr = dict(r)
        rr['html'] = public_markdown_to_html(r['content'])
        rendered.append(rr)
    stats = {
        'generated_at': inv.get('generated_at', GENERATED_AT),
        'public_repo': PUBLIC_REPO,
        'record_count': len(rendered),
        'security': 'Public-safe generated site. Secrets, tokens, cookies, private chat IDs, and private workflow payloads are omitted or redacted upstream.',
    }
    site_data = {'stats': stats, 'records': [{k: v for k, v in r.items() if k != 'html'} for r in rendered]}
    (DOCS / 'site-data.json').write_text(json.dumps(site_data, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    data_json = json.dumps({'stats': stats, 'records': rendered}, ensure_ascii=False, separators=(',', ':')).replace('&', '\\u0026').replace('<', '\\u003c').replace('>', '\\u003e')
    index = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Hermes Architecture Explorer</title>
<meta name="description" content="Public-safe interactive architecture map for a Hermes Agent setup." />
<style>
:root {{ color-scheme: dark; --bg:#070a12; --panel:#0e1524; --panel2:#121d31; --ink:#edf4ff; --muted:#92a3bd; --line:#263653; --accent:#67e8f9; --accent2:#c084fc; --green:#34d399; --warn:#fbbf24; --radius:20px; --shadow:0 28px 90px rgba(0,0,0,.38); }}
* {{ box-sizing:border-box }}
body {{ margin:0; color:var(--ink); font:14px/1.55 Inter, ui-sans-serif, system-ui, -apple-system, Segoe UI, sans-serif; background:radial-gradient(circle at 16% -10%, rgba(103,232,249,.2), transparent 35%), radial-gradient(circle at 90% 0%, rgba(192,132,252,.18), transparent 32%), var(--bg); }}
a {{ color:var(--accent); text-decoration:none }} a:hover {{ text-decoration:underline }}
.shell {{ display:grid; grid-template-columns:380px minmax(0,1fr); min-height:100vh }}
aside {{ position:sticky; top:0; height:100vh; overflow:auto; padding:22px; border-right:1px solid var(--line); background:rgba(7,10,18,.84); backdrop-filter:blur(18px) }}
main {{ min-width:0; padding:28px }}
.brand {{ display:flex; gap:13px; align-items:center; margin-bottom:18px }} .mark {{ width:44px; height:44px; border-radius:16px; background:linear-gradient(135deg,var(--accent),var(--accent2)); box-shadow:0 16px 48px rgba(103,232,249,.2) }}
h1,h2,h3 {{ line-height:1.08; letter-spacing:-.035em }} .brand h1 {{ margin:0; font-size:20px }} .brand p {{ margin:3px 0 0; color:var(--muted); font-size:12px }}
.search {{ width:100%; border:1px solid var(--line); background:#090f1c; color:var(--ink); border-radius:15px; padding:13px 14px; outline:none }} .search:focus {{ border-color:var(--accent); box-shadow:0 0 0 3px rgba(103,232,249,.12) }}
.stats {{ display:grid; grid-template-columns:repeat(3,1fr); gap:9px; margin:14px 0 }} .stat {{ border:1px solid var(--line); background:var(--panel); border-radius:14px; padding:12px }} .stat b {{ display:block; font-size:18px }} .stat span {{ color:var(--muted); font-size:11px }}
.filters {{ display:flex; flex-wrap:wrap; gap:8px; margin:13px 0 16px }} .chip {{ border:1px solid var(--line); color:var(--muted); background:rgba(18,29,49,.82); border-radius:999px; padding:7px 10px; cursor:pointer; font-size:12px }} .chip.active {{ color:#06111c; background:var(--accent); border-color:var(--accent); font-weight:700 }}
.list {{ display:flex; flex-direction:column; gap:9px }} .card {{ text-align:left; color:inherit; width:100%; border:1px solid var(--line); background:var(--panel); border-radius:15px; padding:13px; cursor:pointer; transition:.16s ease }} .card:hover,.card.active {{ transform:translateY(-1px); border-color:rgba(103,232,249,.7); background:var(--panel2) }} .card h3 {{ margin:0 0 5px; font-size:14px }} .card p {{ margin:0; color:var(--muted); font-size:12px; max-height:40px; overflow:hidden }}
.tags {{ display:flex; gap:6px; flex-wrap:wrap; margin-top:8px }} .tag {{ color:var(--accent); background:rgba(103,232,249,.09); border-radius:999px; padding:2px 7px; font-size:11px }}
.hero {{ border:1px solid var(--line); border-radius:var(--radius); background:linear-gradient(180deg,rgba(18,29,49,.92),rgba(14,21,36,.95)); box-shadow:var(--shadow); padding:25px; margin-bottom:18px }} .hero-top {{ display:flex; justify-content:space-between; gap:20px; align-items:flex-start }} .hero h2 {{ margin:0 0 8px; font-size:36px }} .hero p {{ margin:0; color:var(--muted); max-width:880px }}
.actions {{ display:flex; flex-wrap:wrap; gap:9px; margin-top:14px }} .btn {{ border:1px solid var(--line); background:#0b1220; color:var(--ink); border-radius:12px; padding:9px 12px; text-decoration:none; cursor:pointer }} .btn.primary {{ border:0; color:#06111c; background:linear-gradient(135deg,var(--accent),var(--accent2)); font-weight:800 }}
.doc {{ border:1px solid var(--line); border-radius:var(--radius); background:rgba(14,21,36,.96); box-shadow:var(--shadow); padding:26px; overflow:hidden }} .doc h1 {{ font-size:32px; margin-top:0 }} .doc h2 {{ margin-top:34px; padding-top:18px; border-top:1px solid var(--line) }} .doc p,.doc li {{ color:#cfdaec }} code {{ color:#bfdbfe; background:rgba(148,163,184,.09); border-radius:6px; padding:1px 4px }} pre {{ background:#050812; border:1px solid var(--line); border-radius:14px; color:#dbeafe; padding:14px; overflow:auto }}
.table-wrap {{ overflow:auto; border:1px solid var(--line); border-radius:14px; margin:14px 0 }} table {{ width:100%; min-width:720px; border-collapse:collapse }} th,td {{ padding:9px 10px; border-bottom:1px solid var(--line); text-align:left; vertical-align:top }} th {{ background:#0b1220; color:#e2e8f0; position:sticky; top:0 }} td {{ color:#cbd5e1 }}
.graph {{ display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:10px; margin-top:16px }} .node {{ border:1px solid var(--line); border-radius:16px; padding:12px; background:rgba(103,232,249,.06) }} .node b {{ display:block }} .node span {{ color:var(--muted); font-size:12px }} mark {{ background:rgba(251,191,36,.28); color:inherit; border-radius:4px; padding:0 2px }} .empty {{ border:1px dashed var(--line); border-radius:14px; padding:18px; text-align:center; color:var(--muted) }}
@media (max-width:1000px) {{ .shell {{ grid-template-columns:1fr }} aside {{ position:relative; height:auto }} main {{ padding:16px }} .hero-top {{ flex-direction:column }} .graph {{ grid-template-columns:1fr 1fr }} }}
</style>
</head>
<body>
<div class="shell">
<aside>
  <div class="brand"><div class="mark"></div><div><h1>Hermes Architecture</h1><p>Public interactive map · {html.escape(str(inv.get('generated_at', GENERATED_AT)))}</p></div></div>
  <input id="q" class="search" placeholder="Search models, cron, MCP, tools, surfaces…" />
  <div class="stats"><div class="stat"><b id="total">0</b><span>records</span></div><div class="stat"><b id="matches">0</b><span>matches</span></div><div class="stat"><b>public</b><span>redacted</span></div></div>
  <div id="filters" class="filters"></div>
  <div id="list" class="list"></div>
</aside>
<main>
  <section class="hero">
    <div class="hero-top"><div><h2 id="title">Hermes Architecture Explorer</h2><p id="summary">Public-safe architecture documentation for Hermes Agent: runtime, gateway, models, MCP/toolsets, tasks, skills, hooks, and plugins.</p></div><div class="actions"><a class="btn primary" href="hermes-architecture.html">Diagram</a><a class="btn" href="Hermes-Architecture.pdf">PDF</a><a class="btn" href="../ARCHITECTURE.md">Markdown</a><a class="btn" href="../data/inventory.public.json">JSON</a></div></div>
    <div class="graph"><div class="node"><b>Gateway</b><span>models + channels</span></div><div class="node"><b>Kanban</b><span>researcher / worker / reviewer</span></div><div class="node"><b>Tools</b><span>MCP + local capabilities</span></div><div class="node"><b>Automation</b><span>cron + post-session reviews</span></div><div class="node"><b>Knowledge</b><span>GBrain + skills + rules</span></div></div>
  </section>
  <article id="doc" class="doc"></article>
</main>
</div>
<script id="site-data" type="application/json">{data_json}</script>
<script>
const DATA=JSON.parse(document.getElementById('site-data').textContent); const records=DATA.records;
let selected=Number(localStorage.getItem('archExplorerSelected')||0); let tag=localStorage.getItem('archExplorerTag')||'all';
const q=document.getElementById('q'), list=document.getElementById('list'), doc=document.getElementById('doc');
document.getElementById('total').textContent=records.length;
const norm=s=>(s||'').toLowerCase();
const tags=()=>['all',...Array.from(new Set(records.flatMap(r=>r.tags))).sort()];
function escRe(s){{return s.replace(/[\\^$.*+?()[\]{{}}|]/g,'\\$&')}}
function ok(r){{const query=q.value.trim(); const hay=norm([r.title,r.summary,r.path,r.kind,r.tags.join(' '),r.content].join('\\n')); return (!query||hay.includes(norm(query)))&&(tag==='all'||r.tags.includes(tag));}}
function hi(s){{const query=q.value.trim(); if(!query||query.length<2)return s; return s.replace(new RegExp(escRe(query),'ig'),m=>`<mark>${{m}}</mark>`);}}
function filters(){{const el=document.getElementById('filters'); el.innerHTML=''; for(const t of tags()){{const b=document.createElement('button'); b.className='chip'+(t===tag?' active':''); b.textContent=t; b.onclick=()=>{{tag=t; localStorage.setItem('archExplorerTag',t); render();}}; el.appendChild(b);}}}}
function renderList(items){{list.innerHTML=''; document.getElementById('matches').textContent=items.length; if(!items.length){{list.innerHTML='<div class="empty">No matches</div>'; return;}} for(const r of items){{const idx=records.indexOf(r); const b=document.createElement('button'); b.className='card'+(idx===selected?' active':''); b.innerHTML=`<h3>${{r.title}}</h3><p>${{r.summary||r.path}}</p><div class="tags">${{r.tags.map(t=>`<span class="tag">${{t}}</span>`).join('')}}</div>`; b.onclick=()=>{{selected=idx; localStorage.setItem('archExplorerSelected',selected); render();}}; list.appendChild(b);}}}}
function renderDoc(r){{if(!r)r=records[0]; document.getElementById('title').textContent=r.title; document.getElementById('summary').textContent=r.summary||r.path; doc.innerHTML=hi(r.html);}}
function render(){{const items=records.filter(ok); if(!items.includes(records[selected])&&items[0]) selected=records.indexOf(items[0]); renderList(items); renderDoc(records[selected]||items[0]||records[0]); filters();}}
q.addEventListener('input',render); document.addEventListener('keydown',e=>{{if(e.key==='/'&&document.activeElement!==q){{e.preventDefault();q.focus();}} if(e.key==='Escape'){{q.value='';render();}}}}); render();
</script>
</body>
</html>'''
    (DOCS / 'index.html').write_text(index, encoding='utf-8')


def ensure_public_aliases() -> None:
    """Expose canonical repo files from the docs web root.

    The public Caddy route serves docs/ as the web root, but users reasonably
    expect /ARCHITECTURE.md and /data/inventory.public.json to work. Keep these
    as symlink aliases so the live site and GitHub Pages-style paths both work.
    """
    aliases = {
        DOCS / "ARCHITECTURE.md": pathlib.Path("../ARCHITECTURE.md"),
        DOCS / "data": pathlib.Path("../data"),
    }
    for alias, target in aliases.items():
        if alias.is_symlink() and os.readlink(alias) == str(target):
            continue
        if alias.is_symlink() or alias.is_file():
            alias.unlink()
        elif alias.is_dir():
            shutil.rmtree(alias)
        alias.symlink_to(target)


def write_outputs(inv: dict) -> None:
    DOCS.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    svg = svg_diagram(inv)
    arch_md = generate_markdown(inv)
    (ROOT / "ARCHITECTURE.md").write_text(arch_md, encoding="utf-8")
    write_surface_docs(inv)
    write_interactive_site(inv, arch_md)
    ensure_public_aliases()
    (ROOT / "README.md").write_text(dedent("""
    # Hermes Architecture

    Public-safe architecture documentation for a Hermes Agent setup, including models, MCP servers, tasks, skills, hooks, plugins, cron automation, and remote-system surfaces.

    - Interactive public site: [`docs/index.html`](docs/index.html)
    - Canonical document: [`ARCHITECTURE.md`](ARCHITECTURE.md)
    - Diagram: [`docs/hermes-architecture.svg`](docs/hermes-architecture.svg)
    - Browser view: [`docs/hermes-architecture.html`](docs/hermes-architecture.html)
    - PDF: [`docs/Hermes-Architecture.pdf`](docs/Hermes-Architecture.pdf)
    - Redacted inventory: [`data/inventory.public.json`](data/inventory.public.json)
    - Interactive data: [`docs/site-data.json`](docs/site-data.json)
    - Low-level surfaces: [`docs/surfaces/index.md`](docs/surfaces/index.md)

    This repo intentionally excludes secrets, private chat IDs, tokens, OAuth headers, cookies, and private personal/client workflow payloads.
    """).strip() + "\n", encoding="utf-8")
    (DOCS / "hermes-architecture.svg").write_text(svg, encoding="utf-8")
    (DOCS / "hermes-architecture.html").write_text(html_diagram(svg), encoding="utf-8")
    (DATA / "inventory.public.json").write_text(json.dumps(inv, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (ROOT / ".gitignore").write_text(dedent("""
    .env
    *.key
    *.pem
    *.token
    __pycache__/
    .venv/
    node_modules/
    *.log
    private/
    tmp/
    """).lstrip(), encoding="utf-8")


def render_pdf() -> bool:
    script = pathlib.Path.home() / ".hermes" / "skills" / "brain-pdf" / "scripts" / "render_brain_pdf.py"
    out = DOCS / "Hermes-Architecture.pdf"
    if not script.exists():
        return False
    code, output = run(["python3", str(script), str(ROOT / "ARCHITECTURE.md"), str(out), "--author", "Hermes Architecture"], 120)
    print(output)
    return code == 0 and out.exists() and out.stat().st_size > 1000


def git_commit_push() -> None:
    if not (ROOT / ".git").exists():
        run(["git", "init", "-b", "main"], 30)
    run(["git", "config", "user.name", "Hermes Architecture Bot"], 10)
    run(["git", "config", "user.email", "hermes-architecture@example.invalid"], 10)
    run(["git", "add", "README.md", "ARCHITECTURE.md", "docs", "data", "scripts", ".gitignore"], 30)
    code, status = run(["git", "status", "--porcelain"], 30)
    if status.strip():
        run(["git", "commit", "-m", "docs: update Hermes architecture snapshot"], 60)
        # Push if origin exists.
        code, remotes = run(["git", "remote"], 10)
        if "origin" in remotes.split():
            run(["git", "push", "-u", "origin", "main"], 120)
        print("updated")
    else:
        print("no changes")


def strip_volatile(inv: dict) -> dict:
    """Return inventory without fields that should not force a public commit."""
    clone = json.loads(json.dumps(inv, ensure_ascii=False))
    clone.pop("generated_at", None)
    return clone


def keep_previous_timestamp_if_unchanged(inv: dict) -> dict:
    old_path = DATA / "inventory.public.json"
    if old_path.exists():
        try:
            old = json.loads(old_path.read_text(encoding="utf-8"))
            if strip_volatile(old) == strip_volatile(inv):
                inv["generated_at"] = old.get("generated_at", inv["generated_at"])
        except Exception:
            pass
    return inv


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--commit", action="store_true", help="Commit and push if changed")
    args = ap.parse_args()
    inv = keep_previous_timestamp_if_unchanged(collect_inventory())
    write_outputs(inv)
    pdf_path = DOCS / "Hermes-Architecture.pdf"
    # Chrome embeds PDF metadata that can differ between identical renders. To keep
    # no-agent cron quiet, rerender only when source artifacts changed or PDF is missing.
    code, diff_check = run([
        "git", "diff", "--quiet", "--",
        "ARCHITECTURE.md",
        "docs/hermes-architecture.svg",
        "docs/hermes-architecture.html",
        "data/inventory.public.json",
        "docs/surfaces",
    ], 30)
    needs_pdf = (not pdf_path.exists()) or code != 0 or not (ROOT / ".git").exists()
    pdf_ok = True
    if needs_pdf:
        pdf_ok = render_pdf()
    if not pdf_ok:
        print("WARN: PDF render failed or unavailable", file=sys.stderr)
    if args.commit:
        git_commit_push()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
