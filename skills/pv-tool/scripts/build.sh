#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=common.sh
source "$SCRIPT_DIR/common.sh"

ensure_dependencies

cd "$APP_DIR"
npm run build -- "$@"

echo "PV Tool production build written to $APP_DIR/dist"
