#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path
from typing import List

BRIDGE = Path(__file__).with_name("tip_gui_bridge.py")


def main(argv: List[str]) -> int:
    proc = subprocess.run([sys.executable, str(BRIDGE), *argv], capture_output=True, text=True)
    if proc.stdout:
        try:
            payload = json.loads(proc.stdout)
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        except Exception:  # noqa: BLE001
            print(proc.stdout)
    if proc.stderr:
        print(proc.stderr, file=sys.stderr)
    return proc.returncode


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
