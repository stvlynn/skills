#!/usr/bin/env python3
import argparse
import base64
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path
from typing import Any, Dict, List, Optional

TIP_SETTINGS = Path.home() / "Library/Application Support/Tip/settings.json"
DEFAULT_PORTS = [8787, 8788]
TIP_REPO = Path.home() / "service/youtu-tip/youtu-tip"
TIP_LOCAL_ENV = TIP_REPO / "python/app/gui_agent/local_env.py"
TIP_PYTHON = TIP_REPO / "python/.venv/bin/python"
ARTIFACT_ROOT = Path.home() / ".openclaw/workspace/tmp/tip-gui-skill"


def jprint(payload: Dict[str, Any]) -> None:
    print(json.dumps(payload, ensure_ascii=False, indent=2))


def base_response(action: str) -> Dict[str, Any]:
    return {
        "ok": True,
        "action": action,
        "summary": "",
        "error": None,
        "artifacts": {},
        "data": {},
    }


def load_settings() -> Dict[str, Any]:
    if not TIP_SETTINGS.exists():
        raise FileNotFoundError(f"Tip settings file not found: {TIP_SETTINGS}")
    return json.loads(TIP_SETTINGS.read_text())


def probe_port(port: int) -> Optional[Dict[str, Any]]:
    url = f"http://127.0.0.1:{port}/health"
    try:
        with urllib.request.urlopen(url, timeout=1.5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return {"port": port, "url": url, "health": data}
    except Exception as exc:  # noqa: BLE001
        return {"port": port, "url": url, "error": str(exc)}


def active_profile(settings: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    active_id = settings.get("llmActiveId")
    for profile in settings.get("llmProfiles", []):
        if profile.get("id") == active_id:
            return profile
    return None


def ensure_tip_python() -> Path:
    if not TIP_PYTHON.exists():
        raise FileNotFoundError(f"Tip Python venv not found: {TIP_PYTHON}")
    return TIP_PYTHON


def ensure_artifact_root() -> Path:
    ARTIFACT_ROOT.mkdir(parents=True, exist_ok=True)
    return ARTIFACT_ROOT


def write_artifact(name: str, data: bytes) -> str:
    root = ensure_artifact_root()
    stamp = time.strftime("%Y%m%d-%H%M%S")
    path = root / f"{stamp}-{name}"
    path.write_bytes(data)
    return str(path)


def _run_tip_python(snippet: str) -> Dict[str, Any]:
    python_bin = ensure_tip_python()
    proc = subprocess.run(
        [str(python_bin), "-c", snippet],
        capture_output=True,
        text=True,
        cwd=str(TIP_REPO),
    )
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout).strip() or f"Tip helper failed with code {proc.returncode}")
    try:
        return json.loads(proc.stdout)
    except Exception as exc:  # noqa: BLE001
        raise RuntimeError(f"Failed to parse Tip helper JSON: {exc}; raw={proc.stdout[:500]}") from exc


def post_json(url: str, payload: Dict[str, Any], *, timeout: int = 90) -> Dict[str, Any]:
    req = urllib.request.Request(
        url=url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {body}") from exc


def probe_vision_support() -> Dict[str, Any]:
    for port in DEFAULT_PORTS:
        try:
            payload = post_json(f"http://127.0.0.1:{port}/llm/vision-probe", {}, timeout=30)
            payload["port"] = port
            return payload
        except Exception:
            continue
    raise RuntimeError("No Tip sidecar vision-probe endpoint responded")


def generate_intent_candidates(image_bytes: bytes) -> Dict[str, Any]:
    image_b64 = base64.b64encode(image_bytes).decode("ascii")
    payload = {
        "image": f"data:image/png;base64,{image_b64}",
        "language": "en-US",
    }
    for port in DEFAULT_PORTS:
        try:
            data = post_json(f"http://127.0.0.1:{port}/intents", payload, timeout=90)
            data["port"] = port
            return data
        except Exception:
            continue
    raise RuntimeError("No Tip sidecar intents endpoint responded")


def describe_image_with_profile(image_bytes: bytes, profile: Dict[str, Any]) -> Dict[str, Any]:
    base_url = (profile.get("openaiBaseUrl") or profile.get("baseUrl") or "").rstrip("/")
    if not base_url:
        raise RuntimeError("Active Tip profile has no OpenAI-compatible base URL")
    api_key = (profile.get("apiKey") or "").strip()
    auth = ((profile.get("headers") or {}).get("Authorization") or "").strip()
    if not api_key and auth.lower().startswith("bearer "):
        api_key = auth.split(" ", 1)[1].strip()
    if not api_key:
        raise RuntimeError("Active Tip profile has no API key")
    model = profile.get("openaiModel") or profile.get("apiModel") or profile.get("model")
    if not model:
        raise RuntimeError("Active Tip profile has no model configured")

    image_b64 = base64.b64encode(image_bytes).decode("ascii")
    prompt = "Describe the current macOS screen for an automation agent. Summarize visible apps/windows, likely focus, major actionable UI elements, and any obvious next actions. Keep it concise and structured."
    payload = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": prompt},
                    {"type": "input_image", "image_url": f"data:image/png;base64,{image_b64}"},
                ],
            }
        ],
        "max_output_tokens": 400,
    }
    req = urllib.request.Request(
        url=base_url + "/responses",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {exc.code}: {body}") from exc

    description = raw.get("output_text") or ""
    if not description:
        outputs = raw.get("output") or []
        text_parts = []
        for item in outputs:
            for part in item.get("content") or []:
                if isinstance(part, dict) and isinstance(part.get("text"), str):
                    text_parts.append(part["text"])
        description = "\n".join(text_parts).strip()
    return {
        "provider": profile.get("provider"),
        "model": model,
        "baseUrl": base_url,
        "description": description or "",
        "raw": raw,
    }


def capture_with_tip() -> Dict[str, Any]:
    snippet = f'''
import importlib.util, json
from pathlib import Path
spec = importlib.util.spec_from_file_location("tip_local_env", {str(TIP_LOCAL_ENV)!r})
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
env = module.LocalMacOSEnv()
obs = env.reset({{"source": "tip-gui-skill"}})
shot = obs.get("screenshot") or b""
print(json.dumps({{
  "screenshot_hex": shot.hex(),
  "bytes": len(shot),
  "screenWidth": getattr(env, "screen_width", None),
  "screenHeight": getattr(env, "screen_height", None)
}}))
'''
    payload = _run_tip_python(snippet)
    screenshot = bytes.fromhex(payload.pop("screenshot_hex"))
    artifact = write_artifact("capture.png", screenshot)
    payload["artifact"] = artifact
    return payload


def execute_with_tip(action_code: str) -> Dict[str, Any]:
    snippet = f'''
import importlib.util, json
spec = importlib.util.spec_from_file_location("tip_local_env", {str(TIP_LOCAL_ENV)!r})
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
env = module.LocalMacOSEnv()
before = env.reset({{"source": "tip-gui-skill"}})
obs, reward, done, info = env.step({action_code!r})
before_shot = before.get("screenshot") or b""
after_shot = obs.get("screenshot") or b""
print(json.dumps({{
  "before_hex": before_shot.hex(),
  "after_hex": after_shot.hex(),
  "reward": reward,
  "done": done,
  "info": info,
  "beforeBytes": len(before_shot),
  "afterBytes": len(after_shot),
  "screenWidth": getattr(env, "screen_width", None),
  "screenHeight": getattr(env, "screen_height", None)
}}))
'''
    payload = _run_tip_python(snippet)
    before_artifact = write_artifact("before.png", bytes.fromhex(payload.pop("before_hex")))
    after_artifact = write_artifact("after.png", bytes.fromhex(payload.pop("after_hex")))
    payload["beforeArtifact"] = before_artifact
    payload["afterArtifact"] = after_artifact
    return payload


def cmd_health(_: argparse.Namespace) -> int:
    result = base_response("health")
    probes = [probe_port(p) for p in DEFAULT_PORTS]
    healthy = [p for p in probes if p and p.get("health", {}).get("status") == "ok"]
    result["ok"] = bool(healthy)
    result["summary"] = "Tip sidecar reachable" if healthy else "Tip sidecar not reachable"
    result["data"] = {"probes": probes, "healthyPorts": [p["port"] for p in healthy]}
    if not healthy:
        result["error"] = "No healthy Tip sidecar port responded"
    jprint(result)
    return 0 if healthy else 1


def cmd_ports(_: argparse.Namespace) -> int:
    result = base_response("ports")
    probes = [probe_port(p) for p in DEFAULT_PORTS]
    result["summary"] = "Probed Tip localhost health endpoints"
    result["data"] = {"probes": probes}
    jprint(result)
    return 0


def cmd_config(_: argparse.Namespace) -> int:
    result = base_response("config")
    try:
        settings = load_settings()
        profile = active_profile(settings) or {}
        safe_profile = {
            "id": profile.get("id"),
            "name": profile.get("name"),
            "provider": profile.get("provider"),
            "model": profile.get("model"),
            "apiModel": profile.get("apiModel"),
            "baseUrl": profile.get("baseUrl"),
            "openaiBaseUrl": profile.get("openaiBaseUrl"),
            "stream": profile.get("stream"),
            "timeoutMs": profile.get("timeoutMs"),
            "hasApiKey": bool(profile.get("apiKey")),
            "hasAuthorizationHeader": bool((profile.get("headers") or {}).get("Authorization")),
        }
        result["summary"] = "Loaded active Tip profile"
        result["data"] = {
            "settingsPath": str(TIP_SETTINGS),
            "llmActiveId": settings.get("llmActiveId"),
            "vlmActiveId": settings.get("vlmActiveId"),
            "activeProfile": safe_profile,
        }
    except Exception as exc:  # noqa: BLE001
        result["ok"] = False
        result["summary"] = "Failed to load Tip config"
        result["error"] = str(exc)
    jprint(result)
    return 0 if result["ok"] else 1


def cmd_describe(_: argparse.Namespace) -> int:
    result = base_response("describe")
    try:
        settings = load_settings()
        profile = active_profile(settings) or {}
        probes = [probe_port(p) for p in DEFAULT_PORTS]
        healthy = [p for p in probes if p and p.get("health", {}).get("status") == "ok"]
        capture = capture_with_tip()
        image_bytes = Path(capture["artifact"]).read_bytes()

        vision_probe = None
        intent_result = None
        description = None
        describe_error = None

        try:
            vision_probe = probe_vision_support()
        except Exception as exc:  # noqa: BLE001
            vision_probe = {"error": str(exc)}

        try:
            intent_result = generate_intent_candidates(image_bytes)
        except Exception as exc:  # noqa: BLE001
            intent_result = {"error": str(exc)}

        try:
            description = describe_image_with_profile(image_bytes, profile)
        except Exception as exc:  # noqa: BLE001
            describe_error = str(exc)

        result["summary"] = "Captured current screen and inspected available Tip vision paths"
        result["artifacts"] = {"currentScreenshot": capture["artifact"]}
        result["data"] = {
            "provider": profile.get("provider"),
            "model": profile.get("model"),
            "baseUrl": profile.get("baseUrl") or profile.get("openaiBaseUrl"),
            "healthyPorts": [p["port"] for p in healthy],
            "capture": capture,
            "visionProbe": vision_probe,
            "intentCandidates": intent_result,
            "screenDescription": (description or {}).get("description") if description else None,
            "descriptionError": describe_error,
        }
        result["ok"] = True
    except Exception as exc:  # noqa: BLE001
        result["ok"] = False
        result["summary"] = "Failed to inspect describe readiness"
        result["error"] = str(exc)
    jprint(result)
    return 0 if result["ok"] else 1


def cmd_capture(_: argparse.Namespace) -> int:
    result = base_response("capture")
    try:
        capture = capture_with_tip()
        result["summary"] = "Captured screenshot using Tip local environment"
        result["artifacts"] = {"currentScreenshot": capture["artifact"]}
        result["data"] = capture
    except Exception as exc:  # noqa: BLE001
        result["ok"] = False
        result["summary"] = "Failed to capture screenshot"
        result["error"] = str(exc)
    jprint(result)
    return 0 if result["ok"] else 1


def cmd_click(args: argparse.Namespace) -> int:
    result = base_response("click")
    if not args.confirm:
        result["summary"] = f"Dry-run: would click at ({args.x}, {args.y})"
        result["data"] = {"dryRun": True, "x": args.x, "y": args.y, "safetyLevel": "assist"}
        jprint(result)
        return 0
    try:
        action_code = f"pyautogui.click({args.x}, {args.y})"
        execution = execute_with_tip(action_code)
        result["summary"] = f"Executed click at ({args.x}, {args.y}) through Tip local environment"
        result["artifacts"] = {
            "beforeScreenshot": execution["beforeArtifact"],
            "afterScreenshot": execution["afterArtifact"],
        }
        result["data"] = {"dryRun": False, "x": args.x, "y": args.y, "execution": execution}
    except Exception as exc:  # noqa: BLE001
        result["ok"] = False
        result["summary"] = "Click execution failed"
        result["error"] = str(exc)
    jprint(result)
    return 0 if result["ok"] else 1


def cmd_type(args: argparse.Namespace) -> int:
    result = base_response("type")
    if not args.confirm:
        result["summary"] = "Dry-run: would type provided text"
        result["data"] = {"dryRun": True, "text": args.text, "length": len(args.text), "safetyLevel": "assist"}
        jprint(result)
        return 0
    try:
        action_code = f"pyautogui.write({args.text!r})"
        execution = execute_with_tip(action_code)
        result["summary"] = "Executed typing through Tip local environment"
        result["artifacts"] = {
            "beforeScreenshot": execution["beforeArtifact"],
            "afterScreenshot": execution["afterArtifact"],
        }
        result["data"] = {"dryRun": False, "text": args.text, "length": len(args.text), "execution": execution}
    except Exception as exc:  # noqa: BLE001
        result["ok"] = False
        result["summary"] = "Type execution failed"
        result["error"] = str(exc)
    jprint(result)
    return 0 if result["ok"] else 1


def cmd_press(args: argparse.Namespace) -> int:
    result = base_response("press")
    if not args.confirm:
        result["summary"] = f"Dry-run: would press key '{args.key}'"
        result["data"] = {"dryRun": True, "key": args.key, "safetyLevel": "assist"}
        jprint(result)
        return 0
    try:
        action_code = f"pyautogui.press({args.key!r})"
        execution = execute_with_tip(action_code)
        result["summary"] = f"Executed keypress '{args.key}' through Tip local environment"
        result["artifacts"] = {
            "beforeScreenshot": execution["beforeArtifact"],
            "afterScreenshot": execution["afterArtifact"],
        }
        result["data"] = {"dryRun": False, "key": args.key, "execution": execution}
    except Exception as exc:  # noqa: BLE001
        result["ok"] = False
        result["summary"] = "Keypress execution failed"
        result["error"] = str(exc)
    jprint(result)
    return 0 if result["ok"] else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Tip GUI adapter prototype")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("health")
    p.set_defaults(func=cmd_health)

    p = sub.add_parser("ports")
    p.set_defaults(func=cmd_ports)

    p = sub.add_parser("config")
    p.set_defaults(func=cmd_config)

    p = sub.add_parser("describe")
    p.set_defaults(func=cmd_describe)

    p = sub.add_parser("capture")
    p.set_defaults(func=cmd_capture)

    p = sub.add_parser("click")
    p.add_argument("--x", type=int, required=True)
    p.add_argument("--y", type=int, required=True)
    p.add_argument("--confirm", action="store_true")
    p.set_defaults(func=cmd_click)

    p = sub.add_parser("type")
    p.add_argument("--text", required=True)
    p.add_argument("--confirm", action="store_true")
    p.set_defaults(func=cmd_type)

    p = sub.add_parser("press")
    p.add_argument("--key", required=True)
    p.add_argument("--confirm", action="store_true")
    p.set_defaults(func=cmd_press)

    return parser


def main(argv: List[str]) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
