#!/usr/bin/env python3
"""Regenerate _data/projects.yml from the lab's public GitHub repositories.

Repositories of the configured GitHub organization are listed, each one's
topics (tags) are read, and every repository is placed in the first section of
_data/FUTURE_projects_sections.yml whose topic list intersects the repository's
topics. The author shown on each card is the repository's top contributor
(GitHub login), falling back to the organization login when no contributor is
reported.

Repositories without any matching topic are skipped (and logged), so tagging a
repository is what decides where it shows up on the Projects page. The data file
is only overwritten when repositories were successfully listed, so an API
outage never breaks the site build.

Usage:
    python scripts/update_projects.py [--token GH_TOKEN]
"""

import argparse
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("This script requires PyYAML (pip install pyyaml).", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]
CONFIG_YAML = ROOT / "_data" / "FUTURE_projects_sections.yml"
PROJECTS_YAML = ROOT / "_data" / "projects.yml"

API = "https://api.github.com"
SLEEP = 0.15


def get_json(url, token, accept=None):
    headers = {
        "User-Agent": "automationlab-site-updater/1.0",
        "Accept": accept or "application/vnd.github+json",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def load_config():
    with open(CONFIG_YAML, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def list_repos(owner, token):
    repos = []
    page = 1
    while True:
        url = f"{API}/orgs/{owner}/repos?per_page=100&page={page}&sort=full_name"
        batch = get_json(url, token)
        repos.extend(batch)
        if len(batch) < 100:
            return repos
        page += 1
        time.sleep(SLEEP)


def repo_topics(owner, repo, token):
    try:
        data = get_json(f"{API}/repos/{owner}/{repo}/topics", token)
        return set(data.get("names") or [])
    except Exception as exc:  # noqa: BLE001
        print(f"    {repo}: topics unavailable ({exc})", file=sys.stderr)
        return set()


def top_contributor(owner, repo, token):
    try:
        data = get_json(f"{API}/repos/{owner}/{repo}/contributors?per_page=1&anon=false", token)
        if data:
            return data[0].get("login") or ""
    except Exception as exc:  # noqa: BLE001
        print(f"    {repo}: contributors unavailable ({exc})", file=sys.stderr)
    return ""


def section_of(topics, sections):
    for section in sections:
        section_topics = set(section.get("topics") or [])
        if topics & section_topics:
            return section["title"]
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--token", default=None)
    args = parser.parse_args()
    token = args.token or os.environ.get("GITHUB_TOKEN")

    try:
        config = load_config()
    except Exception as exc:  # noqa: BLE001
        print(f"Could not read {CONFIG_YAML}: {exc}", file=sys.stderr)
        sys.exit(1)

    owner = config.get("github_owner")
    if not owner:
        print("github_owner missing from project sections config.", file=sys.stderr)
        sys.exit(1)

    ignore = set(config.get("ignore") or [])
    ignore.add(f"{str(owner).lower()}.github.io")
    sections = config.get("sections") or []
    fallback_author = owner

    try:
        repos = list_repos(owner, token)
    except Exception as exc:  # noqa: BLE001
        print(f"Could not list repositories of {owner}: {exc}", file=sys.stderr)
        print("Leaving existing projects.yml untouched.", file=sys.stderr)
        return

    if not repos:
        print(f"No repositories found for {owner}; leaving projects.yml untouched.", file=sys.stderr)
        return

    print(f"Processing {len(repos)} repository/repositories of {owner}", file=sys.stderr)
    grouped = {section["title"]: [] for section in sections}
    unplaced = []
    for repo in sorted(repos, key=lambda r: r["name"].lower()):
        name = repo["name"]
        if name in ignore:
            print(f"  {name}: ignored", file=sys.stderr)
            continue
        topics = repo_topics(owner, name, token)
        section = section_of(topics, sections)
        if not section:
            print(f"  {name}: skipped, no matching topic (topics: {sorted(topics)})", file=sys.stderr)
            unplaced.append(name)
            continue
        author = top_contributor(owner, name, token) or fallback_author
        grouped[section].append({"title": name, "link": repo["html_url"], "author": author})
        print(f"  {name}: -> {section} (author: {author})", file=sys.stderr)
        time.sleep(SLEEP)

    groups = [
        {"title": title, "items": sorted(items, key=lambda it: it["title"].lower())}
        for title, items in grouped.items()
    ]

    output = (
"# Auto-generated by scripts/FUTURE_update_projects.py - do not edit by hand.\n"
            "# Regenerated on each deploy and periodically from the lab's public GitHub\n"
            "# repositories. Tag a repository with one of the topics listed in\n"
            "# _data/FUTURE_projects_sections.yml to place it in a section on /projects/.\n\n"
        + yaml.safe_dump({"groups": groups}, sort_keys=False, allow_unicode=True)
    )
    PROJECTS_YAML.write_text(output, encoding="utf-8")
    print(f"Wrote {len(groups)} group(s) to {PROJECTS_YAML}", file=sys.stderr)


if __name__ == "__main__":
    main()