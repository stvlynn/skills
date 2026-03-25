#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
APP_DIR="$SKILL_DIR/app"

ensure_command() {
  local cmd="$1"
  local hint="$2"

  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "$hint" >&2
    exit 1
  fi
}

ensure_node_runtime() {
  ensure_command "node" "Node.js 20+ is required to run PV Tool."
  ensure_command "npm" "npm is required to run PV Tool."

  local node_major
  node_major="$(node -p "process.versions.node.split('.')[0]")"
  if [ "$node_major" -lt 20 ]; then
    echo "PV Tool requires Node.js 20+ because the bundled app uses Vite 7." >&2
    exit 1
  fi
}

ensure_dependencies() {
  ensure_node_runtime

  if [ ! -d "$APP_DIR/node_modules" ]; then
    install_dependencies
  fi
}

install_dependencies() {
  ensure_node_runtime
  cd "$APP_DIR"
  npm ci
}

normalize_base_path() {
  local base="${VITE_BASE:-/pv-tool/}"

  if [[ "$base" != /* ]]; then
    base="/$base"
  fi

  if [[ "$base" != */ ]]; then
    base="$base/"
  fi

  printf '%s\n' "$base"
}

local_url() {
  local host="$1"
  local port="$2"
  local base
  base="$(normalize_base_path)"

  printf 'http://%s:%s%s\n' "$host" "$port" "$base"
}
