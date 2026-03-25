#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "$SCRIPT_DIR/common.sh"

ensure_dependencies

if [ ! -d "$APP_DIR/dist" ]; then
  "$SCRIPT_DIR/build.sh"
fi

host="${PV_TOOL_PREVIEW_HOST:-127.0.0.1}"
port="${PV_TOOL_PREVIEW_PORT:-4174}"
url="$(local_url "$host" "$port")"

echo "Starting PV Tool preview server at $url"

cd "$APP_DIR"
exec npm run preview -- --host "$host" --port "$port" "$@"
