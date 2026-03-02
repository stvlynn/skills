#!/bin/bash
# SearXNG Search - Shell Aliases
# Source this file in your .zshrc or .bashrc:
#   source ~/.openclaw/skills/skills/searxng/aliases.sh

SEARXNG_SEARCH_SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]:-$0}")" && pwd)/scripts/search.py"

# Quick search (5 results)
sxsearch() {
    python3 "$SEARXNG_SEARCH_SCRIPT" --query "$1" --limit 5 "${@:2}"
}

# Image search (6 results)
sxisearch() {
    python3 "$SEARXNG_SEARCH_SCRIPT" --query "$1" --category images --limit 6 "${@:2}"
}

# News search (5 results)
sxnsearch() {
    python3 "$SEARXNG_SEARCH_SCRIPT" --query "$1" --category news --limit 5 "${@:2}"
}

# JSON output
sxjsearch() {
    python3 "$SEARXNG_SEARCH_SCRIPT" --query "$1" --json "${@:2}"
}

# Service status
sxstatus() {
    curl -s http://localhost:8888/health | head -5
}

# Example usage:
#   sxsearch "AI news"
#   sxisearch "cute cats"
#   sxnsearch "technology"
#   sxjsearch "Python tutorial" | jq '.results[0].url'
#   sxstatus
