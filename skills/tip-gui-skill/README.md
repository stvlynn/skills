# Tip GUI Skill Prototype

This skill wraps a local Youtu-Tip install behind a small Python CLI so OpenClaw/Codex-style agents can query runtime state, capture desktop screenshots, and prepare for guarded GUI automation.

## What it does today

- discovers Tip sidecar on localhost
- reads Tip user config from `~/Library/Application Support/Tip/settings.json`
- reports the active provider/model configuration without exposing secrets
- captures real screenshots through Tip's local GUI environment
- probes vision readiness and image-intent endpoints
- exposes guarded single-step GUI action contracts

## What it does not do yet

- promise real element targeting
- guarantee robust semantic screen understanding on every provider
- offer unrestricted autonomous desktop control
- bypass macOS permission requirements

## Current status

The prototype verifies that:
- local screenshot capture works
- sidecar health and vision-related probe paths are reachable
- GUI action contracts are available with dry-run safety by default
- end-to-end image understanding still depends on the active upstream model provider and its protocol support

So the current bottleneck is not local capture; it is provider compatibility for vision requests.

## Safety levels

### observe
Read-only inspection of config, health, and provider state.

### assist
Low-risk GUI actions such as click/type/press, but still dry-run by default.

### dangerous
Reserved for future explicit approval flows. Not implemented in this prototype.

## Files

- `scripts/tip_gui_bridge.py` — main adapter CLI
- `scripts/tip_gui_client.py` — tiny wrapper for other scripts/agents
- `examples/quickstart.md` — example usage

## Example

```bash
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py health
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py config
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py describe
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py click --x 100 --y 200
```

## Future direction

The long-term direction is:
1. keep Tip as provider layer
2. extract a reusable local GUI bridge/service contract
3. optionally expose that bridge as MCP or another cross-agent transport
