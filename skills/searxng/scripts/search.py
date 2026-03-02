#!/usr/bin/env python3
"""
SearXNG Search CLI
Powered by local SearXNG instance

Usage:
    python search.py --query "search terms" [options]

Options:
    --query, -q        Search query (required)
    --category, -c     Search category (default: general)
    --limit, -l        Number of results (default: 10)
    --language, -lang  Language code (default: en)
    --safe-search      Safe search level 0-2 (default: 0)
    --timeout          Request timeout in seconds (default: 10)
    --json             Output as JSON
    --quiet            Quiet mode (just URLs)
    --help, -h         Show this help message

Categories:
    general, images, videos, news, files, map, music, social_media,
    it, science, shopping, economic, entertainment, repositories
"""

import argparse
import json
import os
import sys
import time
import urllib.parse
import urllib.request
import urllib.error
from typing import Optional

# Configuration — override with environment variables
DEFAULT_URL = os.environ.get("SEARXNG_URL", "http://localhost:8888")
DEFAULT_TIMEOUT = int(os.environ.get("SEARXNG_TIMEOUT", "10"))
DEFAULT_LIMIT = int(os.environ.get("SEARXNG_MAX_RESULTS", "10"))

# Category to SearXNG format mapping
CATEGORY_MAP = {
    "general": "general",
    "images": "images",
    "videos": "videos",
    "news": "news",
    "files": "files",
    "map": "map",
    "music": "music",
    "social_media": "social_media",
    "it": "it",
    "science": "science",
    "shopping": "shopping",
    "economic": "economic",
    "entertainment": "entertainment",
    "repositories": "repositories",
}


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="SearXNG Search CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic search
  python search.py -q "LLM observability"

  # Image search
  python search.py -q "cute cats" -c images

  # News search with limit
  python search.py -q "AI news" -c news -l 5

  # JSON output for programmatic use
  python search.py -q "Python" --json

  # Quiet mode (URLs only)
  python search.py -q "tutorial" --quiet
        """
    )

    parser.add_argument(
        "-q", "--query",
        required=True,
        help="Search query (required)"
    )

    parser.add_argument(
        "-c", "--category",
        default="general",
        choices=list(CATEGORY_MAP.keys()),
        help="Search category (default: general)"
    )

    parser.add_argument(
        "-l", "--limit",
        type=int,
        default=DEFAULT_LIMIT,
        help=f"Number of results (default: {DEFAULT_LIMIT})"
    )

    parser.add_argument(
        "--language",
        default="en",
        help="Language code (default: en)"
    )

    parser.add_argument(
        "--safe-search",
        type=int,
        default=0,
        choices=[0, 1, 2],
        help="Safe search level 0-2 (default: 0)"
    )

    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help=f"Request timeout in seconds (default: {DEFAULT_TIMEOUT})"
    )

    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
        help=f"SearXNG instance URL (default: {DEFAULT_URL})"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON"
    )

    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Quiet mode (just URLs)"
    )

    parser.add_argument(
        "--no-header",
        action="store_true",
        help="Don't print header/footer"
    )

    return parser.parse_args()


def check_service(url: str, timeout: int) -> tuple[bool, str]:
    """Check if SearXNG service is available."""
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "SearXNG-Search/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return True, "Service available"
    except urllib.error.URLError as e:
        return False, f"Connection error: {e.reason}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def parse_engine_result(result: dict, quiet: bool = False) -> Optional[dict]:
    """Parse a single search result."""
    if not result:
        return None

    # Extract fields safely
    title = result.get("title", "No title")
    url = result.get("url", "")
    desc = result.get("content", result.get("description", ""))
    engine = result.get("engine", "unknown")

    if not url:
        return None

    # Parse URL for additional info
    parsed = urllib.parse.urlparse(url)

    return {
        "title": title.strip() if title else "No title",
        "url": url,
        "description": desc.strip()[:200] if desc else "",
        "engine": engine,
        "parsed_url": {
            "scheme": parsed.scheme,
            "netloc": parsed.netloc,
            "path": parsed.path,
            "params": parsed.params,
            "query": parsed.query,
            "fragment": parsed.fragment
        }
    }


def search(
    query: str,
    category: str = "general",
    limit: int = 10,
    language: str = "en",
    safe_search: int = 0,
    timeout: int = 10,
    url: str = DEFAULT_URL
) -> dict:
    """Perform a search query."""
    # Build search URL
    search_url = f"{url}/search"

    # Prepare parameters
    params = {
        "q": query,
        "categories": CATEGORY_MAP.get(category, "general"),
        "language": language,
        "safesearch": str(safe_search),
        "format": "json",
        "pageno": "1",
    }

    # URL encode parameters
    encoded_params = urllib.parse.urlencode(params)

    # Make request as POST (required by SearXNG)
    start_time = time.time()

    try:
        req = urllib.request.Request(
            search_url,
            data=encoded_params.encode("utf-8"),
            headers={
                "User-Agent": "SearXNG-Search/1.0",
                "Accept": "application/json",
                "Accept-Language": f"{language},en;q=0.9",
                "Content-Type": "application/x-www-form-urlencoded",
                "Referer": url,
                "Origin": url.rstrip("/")
            }
        )

        with urllib.request.urlopen(req, timeout=timeout) as response:
            data = json.loads(response.read().decode("utf-8"))

    except urllib.error.HTTPError as e:
        raise Exception(f"HTTP Error {e.code}: {e.reason}")
    except urllib.error.URLError as e:
        raise Exception(f"Connection error: {e.reason}")
    except json.JSONDecodeError:
        raise Exception("Invalid response from search engine")

    elapsed_time = time.time() - start_time

    # Parse results
    results = []
    raw_results = data.get("results", [])

    for r in raw_results[:limit]:
        parsed = parse_engine_result(r)
        if parsed:
            results.append(parsed)

    # Extract suggestions if available
    suggestions = []
    infobox = data.get("infobox", "")
    if infobox:
        suggestions = [infobox]

    return {
        "query": query,
        "category": category,
        "results": results,
        "count": len(results),
        "time": round(elapsed_time, 3),
        "suggestions": suggestions,
        "total_results": data.get("number_of_results", 0)
    }


def format_text_output(data: dict, quiet: bool = False) -> str:
    """Format results as text."""
    output_parts = []

    if not quiet:
        # Header
        query = data["query"]
        category = data["category"]
        output_parts.append(f'🔍 Search: "{query}"')
        output_parts.append(f"📂 Category: {category}")
        output_parts.append("━" * 60)

    # Results
    for i, result in enumerate(data["results"], 1):
        if quiet:
            output_parts.append(result["url"])
        else:
            title = result["title"][:70] + "..." if len(result["title"]) > 70 else result["title"]
            output_parts.append(f"{i}. {title}")
            output_parts.append(f"   🌐 {result['url'][:80]}...")
            if result["description"]:
                desc = result["description"][:100] + "..." if len(result["description"]) > 100 else result["description"]
                output_parts.append(f"   📝 {desc}")
            output_parts.append(f"   ⚙️  Source: {result['engine']}")
            output_parts.append("")

    if not quiet and data["results"]:
        # Footer
        output_parts.append("━" * 60)
        output_parts.append(f"✅ Found {data['count']} results in {data['time']}s")

    if not data["results"]:
        output_parts.append("❌ No results found")

    return "\n".join(output_parts)


def format_json_output(data: dict) -> str:
    """Format results as JSON."""
    clean_output = {
        "query": data["query"],
        "category": data["category"],
        "results": [
            {
                "title": r["title"],
                "url": r["url"],
                "description": r["description"],
                "engine": r["engine"]
            }
            for r in data["results"]
        ],
        "count": data["count"],
        "time_seconds": data["time"]
    }

    return json.dumps(clean_output, ensure_ascii=False, indent=2)


def main():
    """Main entry point."""
    args = parse_args()

    # Check service availability
    available, message = check_service(args.url, args.timeout)
    if not available:
        print(f"❌ {message}", file=sys.stderr)
        print(f"\n💡 Make sure SearXNG is running:")
        print(f"   docker compose up -d")
        print(f"   See SKILL.md \"First-time Deployment\" for setup instructions.")
        sys.exit(1)

    try:
        # Perform search
        data = search(
            query=args.query,
            category=args.category,
            limit=args.limit,
            language=args.language,
            safe_search=args.safe_search,
            timeout=args.timeout,
            url=args.url
        )

        # Output results
        if args.json:
            print(format_json_output(data))
        else:
            print(format_text_output(data, args.quiet))

        sys.exit(0)

    except Exception as e:
        print(f"❌ Search failed: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
