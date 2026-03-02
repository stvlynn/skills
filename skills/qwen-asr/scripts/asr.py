#!/usr/bin/env python3
"""
Qwen ASR Client - Transcribe audio using Qwen3-ASR service

Usage:
    python asr.py audio.wav [--lang zh]
    python asr.py --url "https://example.com/audio.wav"
    python asr.py --check
"""

import os
import sys
import argparse
import subprocess
import time
from pathlib import Path

# Service configuration
SERVICE_URL = os.environ.get("QWEN_ASR_URL", "http://localhost:8100")
SERVICE_DIR = Path(__file__).resolve().parent.parent / "service"


def check_service():
    """Check if ASR service is running."""
    try:
        import urllib.request
        req = urllib.request.Request(f"{SERVICE_URL}/health", method="GET")
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status == 200
    except Exception:
        return False


def start_service():
    """Start the ASR service."""
    start_script = SERVICE_DIR / "start.sh"
    if start_script.exists():
        print("Starting ASR service...")
        subprocess.Popen(
            ["bash", str(start_script)],
            cwd=str(SERVICE_DIR),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        for _ in range(30):
            if check_service():
                print("Service started!")
                return True
            time.sleep(1)
    return False


def transcribe_file(audio_path: str, language: str = None) -> str:
    """Transcribe audio file using ASR service."""
    import urllib.request
    import urllib.parse
    import json

    if not check_service():
        print("ASR service not running, attempting to start...")
        if not start_service():
            raise Exception("Failed to start ASR service. Run: bash service/start.sh")

    # Build multipart form data manually to avoid requests dependency
    import mimetypes
    boundary = "----FormBoundary7MA4YWxkTrZu0gW"
    filename = os.path.basename(audio_path)
    content_type = mimetypes.guess_type(audio_path)[0] or "application/octet-stream"

    with open(audio_path, "rb") as f:
        file_data = f.read()

    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'
        f"Content-Type: {content_type}\r\n\r\n"
    ).encode() + file_data + f"\r\n--{boundary}--\r\n".encode()

    url = f"{SERVICE_URL}/transcribe"
    if language:
        url += f"?language={urllib.parse.quote(language)}"

    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read().decode())
    return result["text"]


def transcribe_url(audio_url: str, language: str = None) -> str:
    """Transcribe audio from URL using ASR service."""
    import urllib.request
    import urllib.parse
    import json

    if not check_service():
        print("ASR service not running, attempting to start...")
        if not start_service():
            raise Exception("Failed to start ASR service. Run: bash service/start.sh")

    params = {"audio_url": audio_url}
    if language:
        params["language"] = language

    url = f"{SERVICE_URL}/transcribe_url?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, method="POST")
    with urllib.request.urlopen(req, timeout=120) as resp:
        result = json.loads(resp.read().decode())
    return result["text"]


def main():
    parser = argparse.ArgumentParser(description="Qwen ASR - Audio Transcription")
    parser.add_argument("--check", action="store_true", help="Check service status")
    parser.add_argument("input", nargs="?", help="Audio file path or URL")
    parser.add_argument("--lang", "-l", help="Language code (zh, en, ja, etc.)")
    parser.add_argument("--url", "-u", action="store_true", help="Input is URL not file")

    args = parser.parse_args()

    if args.check:
        if check_service():
            print("ASR service is running")
            try:
                import urllib.request, json
                with urllib.request.urlopen(f"{SERVICE_URL}/info", timeout=5) as resp:
                    info = json.loads(resp.read().decode())
                print(f"   Model: {info.get('model', 'Unknown')}")
                print(f"   Device: {info.get('device', 'Unknown')}")
            except Exception:
                pass
        else:
            print("ASR service is not running")
            print("   Run: cd qwen-asr && bash service/start.sh")
        return

    if not args.input:
        parser.print_help()
        sys.exit(1)

    try:
        if args.url:
            print(f"Transcribing from URL: {args.input[:50]}...")
            text = transcribe_url(args.input, args.lang)
        else:
            print(f"Transcribing file: {args.input}")
            text = transcribe_file(args.input, args.lang)

        print(f"\nResult:\n{text}")

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
