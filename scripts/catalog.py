"""Regenerate the catalog in profile/README.md from the public Apify Store API.

Only public listing data is used: name, title, description and pricing.
Also renders "## Recent updates": the newest 10 buyer lines of docs/health/RELEASES.md on architek-earth/apify-actors
main (one line per release: date · actor · version · what changed). That repo is private, so the file is read through
the GitHub API with RELEASES_TOKEN (Contents: read) when set, else raw.githubusercontent.com; if neither works the
section is kept as it is (each actor's promote job also writes it on every release).
Usage: python scripts/catalog.py   (optional env RELEASES_TOKEN)
"""

import base64
import json
import os
import pathlib
import re
import urllib.error
import urllib.request

STORE = "https://api.apify.com/v2/store?username=architekture&limit=200"
README = pathlib.Path(__file__).resolve().parent.parent / "profile" / "README.md"
START, END = "<!-- catalog:start -->", "<!-- catalog:end -->"
R_START, R_END = "<!-- releases:start -->", "<!-- releases:end -->"
RELEASES_API = "https://api.github.com/repos/architek-earth/apify-actors/contents/docs/health/RELEASES.md?ref=main"
RELEASES_RAW = "https://raw.githubusercontent.com/architek-earth/apify-actors/main/docs/health/RELEASES.md"
RECENT = 10
# Same shape as PUBLIC_LINE_RE in ops/setup/promote.py (architek-earth/apify-actors).
RELEASE_LINE = re.compile(r"^\d{4}-\d{2}-\d{2} · \[[^\]]+\]\(https://apify\.com/architekture/[a-z0-9-]+\) · \d+\.\d+\.\d+ · \S.*$")

# Display order of clusters; actors not listed here land in "More".
CLUSTERS: dict[str, list[str]] = {
    "Grocery and retail prices": [
        "woolworths-au-product-scraper", "coles-au-product-scraper", "aldi-au-product-scraper",
        "woolworths-nz-scraper", "new-world-nz-scraper", "paknsave-nz-scraper",
        "tesco-uk-scraper", "sainsburys-uk-scraper", "aldi-ie-scraper", "dunnes-ie-scraper", "mercadona-es-scraper",
    ],
    "E-commerce and marketplaces": ["shopify-products-scraper", "tiktok-shop-products-scraper", "aliexpress-search-scraper"],
    "Jobs, companies and people": ["indeed-scraper", "linkedin-jobs-monitor", "linkedin-people-search-scraper", "yc-companies-scraper"],
    "Video, social and newsletters": [
        "youtube-transcript-scraper", "unified-transcript-api", "threads-replies-scraper",
        "substack-scraper", "ad-intelligence-watchlist",
    ],
    "Search, travel and trends": ["google-trends-scraper", "google-hotels-scraper", "google-shopping-scraper"],
    "Sports": ["tennis-data-scraper"],
    "Documents": ["docparser-invoice-json"],
}


def deprecated(slug: str) -> bool:
    """Deprecated actors stay on Apify for existing users but leave the catalog (public actor API flag)."""
    req = urllib.request.Request(f"https://api.apify.com/v2/acts/architekture~{slug}", headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return bool(json.load(r)["data"].get("isDeprecated"))


def fetch() -> list[dict]:
    req = urllib.request.Request(STORE, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        items = json.load(r)["data"]["items"]
    return [a for a in items if not a.get("isDeprecated") and not deprecated(a["name"])]


def name(a: dict) -> str:
    return re.split(r"\s+[—–-]\s+", a["title"], maxsplit=1)[0].strip()


def line(a: dict) -> str:
    text = " ".join((a.get("description") or "").split())
    first = re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]
    return first if len(first) <= 140 else first[:137].rsplit(" ", 1)[0] + "…"


def price(a: dict) -> str:
    events = ((a.get("currentPricingInfo") or {}).get("pricingPerEvent") or {}).get("actorChargeEvents") or {}
    if not events:
        return "see listing"
    primary = next((e for e in events.values() if e.get("isPrimaryEvent")), next(iter(events.values())))
    per_k = primary["eventPriceUsd"] * 1000
    out = f"${per_k:,.2f} / 1,000 · {primary.get('eventTitle') or 'result'}"
    # Per-run fees (priced like a run, not a row) are shown so the total is not a surprise.
    for e in events.values():
        if e is not primary and e["eventPriceUsd"] >= 0.05:
            out += f" + ${e['eventPriceUsd']:.2f} per {(e.get('eventTitle') or 'run').lower()}"
    return out


def cell(s: str) -> str:
    return s.replace("|", "\\|")


def render(items: list[dict]) -> str:
    by_slug = {a["name"]: a for a in items}
    groups = {k: [s for s in v if s in by_slug] for k, v in CLUSTERS.items()}
    known = {s for v in CLUSTERS.values() for s in v}
    groups["More"] = sorted(s for s in by_slug if s not in known)
    out = [f"**{len(by_slug)} live actors.** Prices are per delivered result; status rows are free.", ""]
    for cluster, slugs in groups.items():
        if not slugs:
            continue
        out += [f"### {cluster}", "", "| Actor | What you get | Price |", "|---|---|---|"]
        for s in slugs:
            a = by_slug[s]
            out.append(f"| [{cell(name(a))}](https://apify.com/architekture/{s}) | {cell(line(a))} | {cell(price(a))} |")
        out.append("")
    return "\n".join(out).rstrip()


def releases_text() -> str | None:
    """RELEASES.md from apify-actors main, or None when it cannot be read (private repo and no token)."""
    token = os.environ.get("RELEASES_TOKEN", "")
    try:
        if token:
            headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
            with urllib.request.urlopen(urllib.request.Request(RELEASES_API, headers=headers), timeout=60) as r:
                return base64.b64decode(json.load(r)["content"]).decode("utf-8")
        with urllib.request.urlopen(RELEASES_RAW, timeout=60) as r:
            return r.read().decode("utf-8")
    except (urllib.error.URLError, KeyError, ValueError) as exc:
        print(f"release notes not readable ({type(exc).__name__}); Recent updates kept as is")
        return None


def recent_lines(text: str) -> list[str]:
    return [ln.strip() for ln in text.splitlines() if RELEASE_LINE.match(ln.strip())][:RECENT]


def with_recent(readme: str, lines: list[str] | None) -> str:
    """Swap in the Recent updates block (the same block the promote job writes); None keeps the existing one."""
    m = re.search(r"## Recent updates\s*\n+" + re.escape(R_START) + r".*?" + re.escape(R_END), readme, flags=re.DOTALL)
    if lines is None and m:
        return readme
    body = "\n\n".join(lines) if lines else "No releases logged yet."
    block = f"## Recent updates\n\n{R_START}\n{body}\n{R_END}"
    if m:
        return readme[: m.start()] + block + readme[m.end() :]
    at = readme.find("\n## Contact")
    if at < 0:
        return readme.rstrip("\n") + "\n\n" + block + "\n"
    return readme[: at + 1] + block + "\n\n" + readme[at + 1 :]


def main() -> None:
    text = README.read_text(encoding="utf-8")
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    new = f"{head}{START}\n{render(fetch())}\n{END}{tail}"
    source = releases_text()
    new = with_recent(new, recent_lines(source) if source is not None else None)
    if new != text:
        README.write_text(new, encoding="utf-8", newline="\n")
        print("catalog updated")
    else:
        print("catalog unchanged")


if __name__ == "__main__":
    main()
