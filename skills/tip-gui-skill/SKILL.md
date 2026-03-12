---
name: tip-gui-skill
description: Reuse local Youtu-Tip GUI capabilities through a safe adapter CLI so OpenClaw/Codex-style agents can inspect desktop GUI state and perform guarded single-step actions on macOS.
---

# Tip GUI Skill

Use this skill when an agent needs a local, macOS-native GUI bridge based on Youtu-Tip instead of browser-only automation.

## When to use

- You want to inspect whether Tip sidecar is running
- You want to confirm the configured online model/provider
- You want a local adapter entrypoint for future GUI actions
- You want guarded single-step desktop actions with JSON output

## Do not use for

- Browser-only tasks where normal browser tooling is enough
- Dangerous desktop automation without explicit confirmation
- Bulk destructive actions
- Claims of fully autonomous GUI control without verification

## Required permissions

Youtu-Tip itself may require:
- Accessibility
- Screen Recording

Without those, health checks may pass while real GUI control still fails.

## Commands

```bash
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py health
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py config
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py ports
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py describe
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py click --x 10 --y 10
```

## Safety model

- `observe`: read-only checks
- `assist`: low-risk actions, still guarded
- `dangerous`: not enabled by default in this prototype

Action commands are dry-run by default unless `--confirm` is explicitly passed.

## Output contract

All commands must return JSON. Agents should parse fields like:
- `ok`
- `action`
- `summary`
- `error`
- `artifacts`
- `data`

## Current prototype limits

This prototype currently provides:
- sidecar discovery
- config inspection
- provider/model visibility
- real screenshot capture via Tip local environment
- safe action contract scaffolding

It does **not** yet promise stable semantic full-screen understanding or robust multi-step autonomous desktop control.
