#!/bin/bash
# Qwen3-ASR Service Launcher
# Downloads model from ModelScope mirror on first run

set -e
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

# Use HuggingFace mirror for faster model downloads (ModelScope CDN)
export HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
export HF_HOME="${HF_HOME:-$HOME/.cache/huggingface}"

# Activate virtual environment if exists
if [ -f "$SKILL_DIR/venv/bin/activate" ]; then
    source "$SKILL_DIR/venv/bin/activate"
fi

echo "Starting Qwen3-ASR Service..."
echo "   Model mirror: $HF_ENDPOINT"
echo "   Cache: $HF_HOME"

cd "$SCRIPT_DIR"
python3 main.py --host 0.0.0.0 --port 8100
