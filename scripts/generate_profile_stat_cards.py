#!/usr/bin/env python3
"""Generate matching, accessible SVG cards for profile views and followers."""
from __future__ import annotations

import html
import json
import os
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_BADGE = ROOT / "svg" / "profile" / "badge.svg"
OUTPUT_DIR = ROOT / "svg" / "profile"
API_URL = "https://api.github.com/users/Sarcasticzain"


def read_profile_views() -> int:
    if not SOURCE_BADGE.exists():
        raise FileNotFoundError(
            f"Counter action did not create its expected file: {SOURCE_BADGE}"
        )
    root = ET.parse(SOURCE_BADGE).getroot()
    values = [
        (node.text or "").strip()
        for node in root.iter()
        if node.tag.rsplit("}", 1)[-1] == "text" and (node.text or "").strip()
    ]
    if len(values) < 2:
        raise ValueError("Could not read the count from svg/profile/badge.svg")
    # Upstream action emits the label first and the numeric count second.
    digits = "".join(char for char in values[-1] if char.isdigit())
    if not digits:
        raise ValueError(f"Unexpected profile-view count in SVG: {values[-1]!r}")
    return int(digits)


def read_followers() -> int:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "Sarcasticzain-profile-readme-counter",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(API_URL, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        data = json.load(response)
    return int(data["followers"])


def card_svg(label: str, value: int, accent: str, icon: str, title_id: str) -> str:
    value_text = f"{value:,}"
    safe_label = html.escape(label)
    safe_value = html.escape(value_text)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="260" height="76" viewBox="0 0 260 76" role="img" aria-labelledby="{title_id}-title {title_id}-desc">
  <title id="{title_id}-title">{safe_label}: {safe_value}</title>
  <desc id="{title_id}-desc">A beveled dark profile statistics card.</desc>
  <defs>
    <linearGradient id="panel-{title_id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#17243d"/>
      <stop offset="0.52" stop-color="#0c1425"/>
      <stop offset="1" stop-color="#080d19"/>
    </linearGradient>
    <linearGradient id="edge-{title_id}" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{accent}" stop-opacity="0.95"/>
      <stop offset="0.48" stop-color="#9aa9c6" stop-opacity="0.25"/>
      <stop offset="1" stop-color="{accent}" stop-opacity="0.52"/>
    </linearGradient>
    <linearGradient id="value-{title_id}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#ffffff"/>
      <stop offset="1" stop-color="{accent}"/>
    </linearGradient>
    <filter id="shadow-{title_id}" x="-20%" y="-35%" width="145%" height="190%">
      <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#000000" flood-opacity="0.65"/>
    </filter>
    <filter id="glow-{title_id}" x="-80%" y="-80%" width="260%" height="260%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <!-- Lower offset edge gives the card a subtle 3D/extruded profile. -->
  <rect x="9" y="10" width="242" height="59" rx="14" fill="#03060d" stroke="{accent}" stroke-opacity="0.48" stroke-width="1.4"/>
  <rect x="8" y="5" width="242" height="59" rx="14" fill="url(#panel-{title_id})" stroke="url(#edge-{title_id})" stroke-width="1.5" filter="url(#shadow-{title_id})"/>
  <path d="M23 6.5h212" stroke="#ffffff" stroke-opacity="0.16" stroke-width="1" stroke-linecap="round"/>
  <path d="M10 20v28" stroke="{accent}" stroke-width="2.5" stroke-linecap="round" filter="url(#glow-{title_id})"/>
  <text x="23" y="29" fill="#9cadc6" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="10" font-weight="700" letter-spacing="1.8">{safe_label.upper()}</text>
  <text x="23" y="52" fill="url(#value-{title_id})" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="21" font-weight="800" letter-spacing="0.3">{safe_value}</text>
  <rect x="197" y="15" width="39" height="38" rx="10" fill="#0b1324" stroke="{accent}" stroke-opacity="0.38"/>
  <path d="{icon}" fill="none" stroke="{accent}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M207 54h19" stroke="{accent}" stroke-opacity="0.7" stroke-width="1" stroke-linecap="round"/>
</svg>
'''


def main() -> None:
    views = read_profile_views()
    followers = read_followers()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    cards = {
        "views-card.svg": card_svg(
            "Profile repo views",
            views,
            "#35d9ff",
            "M205 34c5-8 13-12 20-12s15 4 20 12c-5 8-13 12-20 12s-15-4-20-12zm20-4a4 4 0 1 0 0 8 4 4 0 0 0 0-8z",
            "views",
        ),
        "followers-card.svg": card_svg(
            "Followers",
            followers,
            "#a78bfa",
            "M216 31a5 5 0 1 0 0-10 5 5 0 0 0 0 10zm11 1a4 4 0 1 0 0-8 4 4 0 0 0 0 8zm-11 2c-5 0-9 3-9 7v3h18v-3c0-4-4-7-9-7zm11 1h-1c2 2 3 4 3 6v3h7v-3c0-3-4-6-9-6z",
            "followers",
        ),
    }
    for filename, content in cards.items():
        (OUTPUT_DIR / filename).write_text(content, encoding="utf-8")
        print(f"Wrote {OUTPUT_DIR / filename}")


if __name__ == "__main__":
    main()
