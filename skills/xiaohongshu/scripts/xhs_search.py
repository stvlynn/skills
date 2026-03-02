#!/usr/bin/env python3
"""
小红书搜索工具
依赖本地 xiaohongshu-mcp 服务 (http://localhost:18060)

Usage:
    python3 xhs_search.py <关键词> [数量]
"""
import os
import sys
import json
import urllib.request
import urllib.error

MCP_URL = os.environ.get("XHS_MCP_URL", "http://localhost:18060")


def search(keyword, limit=10):
    """搜索小红书内容"""
    try:
        data = json.dumps({"keyword": keyword}).encode()
        req = urllib.request.Request(
            f"{MCP_URL}/api/v1/feeds/search",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode())

        items = result.get("items", [])[:limit]

        results = []
        for item in items:
            note_card = item.get("note_card", {})
            user = note_card.get("user", {})
            interact = note_card.get("interact_info", {})

            results.append({
                "id": item.get("id"),
                "title": note_card.get("display_title", ""),
                "author": user.get("nickname", ""),
                "likes": interact.get("liked_count", "0"),
                "xsec_token": item.get("xsec_token", "")
            })

        return results

    except urllib.error.URLError:
        print("Service not running. Start xiaohongshu-mcp first.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Search failed: {e}", file=sys.stderr)
        sys.exit(1)


def get_detail(note_id, xsec_token):
    """获取帖子详情"""
    try:
        data = json.dumps({
            "note_id": note_id,
            "xsec_token": xsec_token
        }).encode()
        req = urllib.request.Request(
            f"{MCP_URL}/api/v1/feeds/detail",
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"Failed to get detail: {e}", file=sys.stderr)
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 xhs_search.py <keyword> [limit]")
        print("Example: python3 xhs_search.py 弥勒旅游 5")
        sys.exit(1)

    keyword = sys.argv[1]
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    print(f"Search: {keyword}")
    print("=" * 60)

    results = search(keyword, limit)

    for i, item in enumerate(results, 1):
        print(f"\n[{i}] {item['title']}")
        print(f"    Author: {item['author']}")
        print(f"    Likes:  {item['likes']}")
        print(f"    ID:     {item['id']}")

    print(f"\n\nFound {len(results)} results")

    print("\n" + "=" * 60)
    print("JSON:")
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
