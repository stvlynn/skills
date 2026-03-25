#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "$SCRIPT_DIR/common.sh"

ensure_dependencies

host="${PV_TOOL_DEV_HOST:-127.0.0.1}"
port="${PV_TOOL_DEV_PORT:-4173}"
url="$(local_url "$host" "$port")"

echo "Starting PV Tool dev server at $url"

cd "$APP_DIR"
exec npm run dev -- --host "$host" --port "$port" "$@"
