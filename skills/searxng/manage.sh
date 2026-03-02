#!/bin/bash
# SearXNG Service Management
# Usage: bash manage.sh [status|start|stop|restart|logs|search|help]

SEARXNG_DIR="${SEARXNG_DIR:-$HOME/service/searxng}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SKILL_SCRIPT="$SCRIPT_DIR/scripts/search.py"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

status() {
    echo -e "${BLUE}=== SearXNG Service Status ===${NC}"
    cd "$SEARXNG_DIR"
    docker compose ps
    echo ""
    echo -e "${BLUE}=== Quick Test ===${NC}"
    curl -s "http://localhost:8888/" | grep -o "searxng" | head -1 && echo -e "${GREEN}✓ Web interface available${NC}" || echo -e "${RED}✗ Web interface not available${NC}"
}

start() {
    echo -e "${GREEN}Starting SearXNG...${NC}"
    cd "$SEARXNG_DIR"
    docker compose up -d
    sleep 3
    status
}

stop() {
    echo -e "${YELLOW}Stopping SearXNG...${NC}"
    cd "$SEARXNG_DIR"
    docker compose down
}

restart() {
    echo -e "${YELLOW}Restarting SearXNG...${NC}"
    cd "$SEARXNG_DIR"
    docker compose restart
    sleep 3
    status
}

logs() {
    echo -e "${BLUE}=== Viewing Logs (Ctrl+C to exit) ===${NC}"
    cd "$SEARXNG_DIR"
    docker compose logs -f
}

search() {
    if [ -z "$1" ]; then
        echo -e "${RED}Usage: manage.sh search \"your query\"${NC}"
        return 1
    fi
    python3 "$SKILL_SCRIPT" -q "$1" "${@:2}"
}

isearch() {
    if [ -z "$1" ]; then
        echo -e "${RED}Usage: manage.sh isearch \"cute cats\"${NC}"
        return 1
    fi
    python3 "$SKILL_SCRIPT" -q "$1" -c images "${@:2}"
}

nsearch() {
    if [ -z "$1" ]; then
        echo -e "${RED}Usage: manage.sh nsearch \"AI news\"${NC}"
        return 1
    fi
    python3 "$SKILL_SCRIPT" -q "$1" -c news "${@:2}"
}

jsearch() {
    if [ -z "$1" ]; then
        echo -e "${RED}Usage: manage.sh jsearch \"Python\"${NC}"
        return 1
    fi
    python3 "$SKILL_SCRIPT" -q "$1" --json "${@:2}"
}

help() {
    echo -e "${BLUE}=== SearXNG Search - Usage Guide ===${NC}"
    echo ""
    echo -e "${GREEN}Service Management:${NC}"
    echo "  bash manage.sh status    - Show service status"
    echo "  bash manage.sh start     - Start SearXNG service"
    echo "  bash manage.sh stop      - Stop SearXNG service"
    echo "  bash manage.sh restart   - Restart SearXNG service"
    echo "  bash manage.sh logs      - View service logs"
    echo ""
    echo -e "${GREEN}Search Commands:${NC}"
    echo "  bash manage.sh search \"query\" [options]    - General search"
    echo "  bash manage.sh isearch \"query\" [options]   - Image search"
    echo "  bash manage.sh nsearch \"query\" [options]   - News search"
    echo "  bash manage.sh jsearch \"query\" [options]   - JSON output"
    echo ""
    echo -e "${GREEN}Environment Variables:${NC}"
    echo "  SEARXNG_DIR    - SearXNG docker-compose directory (default: ~/service/searxng)"
    echo "  SEARXNG_URL    - SearXNG instance URL (default: http://localhost:8888)"
    echo ""
    echo -e "${GREEN}Web Access:${NC}"
    echo "  http://localhost:8888"
}

case "$1" in
    status)   status ;;
    start)    start ;;
    stop)     stop ;;
    restart)  restart ;;
    logs)     logs ;;
    search)   search "${@:2}" ;;
    isearch)  isearch "${@:2}" ;;
    nsearch)  nsearch "${@:2}" ;;
    jsearch)  jsearch "${@:2}" ;;
    help|--help|-h) help ;;
    "")       help ;;
    *)        search "$@" ;;
esac
