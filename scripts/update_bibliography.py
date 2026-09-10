#!/usr/bin/env python3
"""Regenerate _bibliography/papers.bib from OpenAlex for the lab members.

Members are read from _data/people.yml (any group). For each member the best
matching OpenAlex author profile is resolved by name + University of Messina
affiliation, then all their works are fetched and merged into a single BibTeX
file. The file is only overwritten when at least one work is found, so a
temporary API outage never breaks the site build.

Usage:
    python scripts/update_bibliography.py [--mailto someone@unime.it]

The polite-pool contact can also be given via the OPENALEX_MAILTO env var.
"""

import argparse
import json
import os
import re
import sys
import time
import unicodedata
import urllib.parse
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    print("This script requires PyYAML (pip install pyyaml).", file=sys.stderr)
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]
PEOPLE_YAML = ROOT / "_data" / "people.yml"
BIB_FILE = ROOT / "_bibliography" / "papers.bib"

API = "https://api.openalex.org"
SLEEP = 0.15  # seconds between API calls (polite pool)


def norm(value):
    """Lowercase and strip accents, for forgiving comparisons."""
    value = unicodedata.normalize("NFD", str(value))
    value = "".join(c for c in value if not unicodedata.combining(c))
    return value.lower().strip()


def get_json(url, mailto):
    if mailto and "mailto=" not in url:
        sep = "&" if "?" in url else "?"
        url = f"{url}{sep}mailto={urllib.parse.quote(mailto)}"
    req = urllib.request.Request(url, headers={"User-Agent": f"automationlab-site-updater/1.0 (mailto:{mailto})" if mailto else "automationlab-site-updater/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def load_members():
    with open(PEOPLE_YAML, encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    members = []
    for group in data.get("groups", []):
        for member in group.get("members", []):
            name = member.get("name", "").strip()
            surname = member.get("surname", "").strip()
            if name and surname:
                members.append({"name": name, "surname": surname, "full": f"{name} {surname}"})
    return members


def candidate_matches(candidate, name, surname):
    """A candidate OpenAlex author matches when it carries our surname and a
    token that starts with our first name."""
    cand = norm(candidate.get("display_name", ""))
    surname_n = norm(surname)
    name_n = norm(name)
    if surname_n not in cand:
        return False
    tokens = cand.split()
    return any(t.startswith(name_n[:1]) for t in tokens if t != surname_n)


def find_best_author(member, mailto):
    """Return (author_id, works_count) for the best Messina-based profile."""
    url = f"{API}/authors?search={urllib.parse.quote(member['full'])}&per-page=50"
    data = get_json(url, mailto)
    best = None
    for candidate in data.get("results", []):
        if not candidate_matches(candidate, member["name"], member["surname"]):
            continue
        institutions = [i.get("display_name", "") for i in candidate.get("last_known_institutions") or []]
        if not any("messina" in norm(i) for i in institutions):
            continue
        if best is None or candidate.get("works_count", 0) > best[1]:
            best = (candidate["id"], candidate.get("works_count", 0))
    return best


def fetch_works(author_id, mailto):
    works = {}
    cursor = "*"
    while cursor:
        params = {"filter": f"author.id:{author_id}", "per-page": "200", "cursor": cursor}
        url = f"{API}/works?{urllib.parse.urlencode(params)}"
        data = get_json(url, mailto)
        for work in data.get("results", []):
            wid = work.get("id")
            if wid:
                works[wid] = work
        cursor = data.get("meta", {}).get("next_cursor")
        time.sleep(SLEEP)
    return works


def biblio_value(work, key):
    value = work.get("biblio", {}).get(key)
    return str(value) if value not in (None, "0") else ""


def entry_type(work):
    mapping = {
        "article": "article",
        "review": "article",
        "book-chapter": "incollection",
        "proceedings-article": "inproceedings",
        "book": "book",
        "dissertation": "phdthesis",
        "report": "techreport",
        "preprint": "misc",
        "software": "misc",
    }
    return mapping.get(work.get("type"), "misc")


def clean(value):
    value = str(value).replace("{", "").replace("}", "")
    for char in "&%_#":
        value = value.replace(char, "\\" + char)
    return value


def authors_string(work):
    names = [au.get("author", {}).get("display_name") for au in work.get("authorships", [])]
    names = [n for n in names if n]
    if not names:
        return "Anonymous"
    formatted = []
    for name in names:
        parts = str(name).split()
        if len(parts) > 1:
            formatted.append("{}, {}".format(parts.pop(), " ".join(parts)))
        else:
            formatted.append(parts[0])
    return " and ".join(formatted)


def title_slug(title, used):
    base = re.sub(r"[^a-z0-9]+", " ", norm(title)).strip()
    words = base.split()[:3]
    suffix = "".join(words) if words else "work"
    if suffix in used:
        count = 2
        while f"{suffix}-{count}" in used:
            count += 1
        suffix = f"{suffix}-{count}"
    used.add(suffix)
    return suffix


def build_bibtex(work, used):
    key = title_slug(work.get("title") or "", used)
    year = str(work.get("publication_year") or "")
    fields = [
        ("author", authors_string(work)),
        ("title", clean(work.get("title") or "")),
    ]
    source = (work.get("primary_location") or {}).get("source") or {}
    journal = source.get("display_name")
    entry_type_name = entry_type(work)
    if entry_type_name == "inproceedings" and journal:
        fields.append(("booktitle", clean(journal)))
    elif entry_type_name in ("article", "review") and journal:
        fields.append(("journal", clean(journal)))
    elif journal:
        fields.append(("journal", clean(journal)))
    volume = biblio_value(work, "volume")
    if volume:
        fields.append(("volume", volume))
    issue = biblio_value(work, "issue")
    if issue:
        fields.append(("number", issue))
    first_page = biblio_value(work, "first_page")
    last_page = biblio_value(work, "last_page")
    if first_page and last_page and first_page != last_page:
        fields.append(("pages", f"{first_page}--{last_page}"))
    elif first_page:
        fields.append(("pages", first_page))
    if year:
        fields.append(("year", year))
    doi = work.get("doi")
    if doi:
        fields.append(("doi", doi.replace("https://doi.org/", "")))
    raw_html = ((work.get("primary_location") or {}).get("landing_page_url") or "").strip()
    if raw_html:
        fields.append(("html", raw_html))
    pdf_url = ((work.get("best_oa_location") or {}).get("pdf_url") or "").strip()
    if pdf_url:
        fields.append(("pdf", pdf_url))

    lines = [f"@{entry_type_name}{{{key},"]
    for field, value in fields:
        lines.append(f"  {field:8}= {{{value}}},")
    lines.append("}")
    return key, int(year) if year else 0, "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mailto", default=None)
    args = parser.parse_args()
    mailto = args.mailto or os.environ.get("OPENALEX_MAILTO")

    try:
        members = load_members()
    except Exception as exc:  # noqa: BLE001
        print(f"Could not read {PEOPLE_YAML}: {exc}", file=sys.stderr)
        sys.exit(1)

    print(f"Processing {len(members)} member(s)", file=sys.stderr)
    collected = {}
    for member in members:
        try:
            author = find_best_author(member, mailto)
        except Exception as exc:  # noqa: BLE001
            print(f"  {member['full']}: author lookup failed ({exc})", file=sys.stderr)
            continue
        if not author:
            print(f"  {member['full']}: no matching Messina profile on OpenAlex", file=sys.stderr)
            continue
        author_id, works_count = author
        try:
            works = fetch_works(author_id, mailto)
        except Exception as exc:  # noqa: BLE001
            print(f"  {member['full']}: works fetch failed ({exc})", file=sys.stderr)
            continue
        print(f"  {member['full']}: {len(works)} work(s) from {author_id}", file=sys.stderr)
        collected.update(works)
        time.sleep(SLEEP)

    if not collected:
        print("No works found; leaving existing papers.bib untouched.", file=sys.stderr)
        return

    def norm_title(text):
        return " ".join(re.sub(r"[^a-z0-9]+", " ", norm(text)).split())

    def work_score(work):
        updated = work.get("updated_date") or ""
        return (
            1 if work.get("doi") else 0,
            1 if work.get("publication_year") else 0,
            1 if (work.get("primary_location") or {}).get("source") else 0,
            len(work.get("authorships") or []),
            updated,
        )

    final = []
    seen_title = {}
    for work in collected.values():
        key = norm_title(work.get("title") or "")
        if key and key in seen_title:
            if work_score(work) > work_score(seen_title[key]):
                final.remove(seen_title[key])
                seen_title[key] = work
                final.append(work)
        else:
            if key:
                seen_title[key] = work
            final.append(work)

    seen_doi = {}
    final_doi = []
    for work in final:
        doi = (work.get("doi") or "").lower()
        if doi and doi in seen_doi:
            if work_score(work) > work_score(seen_doi[doi]):
                final_doi.remove(seen_doi[doi])
                seen_doi[doi] = work
                final_doi.append(work)
        else:
            if doi:
                seen_doi[doi] = work
            final_doi.append(work)

    used = set()
    entries = []
    for work in final_doi:
        wexp = work.get("is_paratext") or work.get("is_retracted")
        if wexp:
            continue
        entries.append(build_bibtex(work, used))

    entries.sort(key=lambda pair: (-pair[1], pair[0]))

    header = (
        "% This file is AUTO-GENERATED by scripts/update_bibliography.py.\n"
        "% Do not edit manually: it is rebuilt from OpenAlex at every deploy.\n"
        "%\n"
        f"% {len(entries)} publication(s).\n"
    )
    content = header + "\n\n".join(text for _, _, text in entries) + "\n"
    BIB_FILE.write_text(content, encoding="utf-8", newline="\n")
    print(f"Wrote {len(entries)} entries to {BIB_FILE}", file=sys.stderr)


if __name__ == "__main__":
    main()