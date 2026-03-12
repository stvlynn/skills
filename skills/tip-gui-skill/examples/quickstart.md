# Quickstart

## Read-only checks

```bash
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py health
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py config
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py ports
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py describe
```

## Dry-run actions

```bash
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py click --x 10 --y 10
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py type --text "hello"
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py press --key Enter
```

## Explicit action mode

```bash
python3 skills/tip-gui-skill/scripts/tip_gui_bridge.py click --x 10 --y 10 --confirm
```

The current prototype still reports limitations honestly and should not be treated as a fully autonomous GUI agent.
