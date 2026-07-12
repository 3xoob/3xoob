#!/usr/bin/env python3

import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from pathlib import Path

OWNER = "3xoob"
README_PATH = Path("README.md")

START_MARKER = "<!-- GITHUB-LANGUAGES:START -->"
END_MARKER = "<!-- GITHUB-LANGUAGES:END -->"

TOKEN = os.environ.get("GITHUB_TOKEN", "")

if not TOKEN:
    print("GITHUB_TOKEN is missing.", file=sys.stderr)
    sys.exit(1)


def github_api(path: str):
    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "github-profile-language-updater",
        },
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def get_repositories():
    repositories = []
    page = 1

    while True:
        result = github_api(
            f"/users/{OWNER}/repos"
            f"?type=owner&sort=full_name&per_page=100&page={page}"
        )

        if not result:
            break

        repositories.extend(
            repository
            for repository in result
            if not repository.get("fork", False)
            and not repository.get("archived", False)
            and not repository.get("disabled", False)
        )

        if len(result) < 100:
            break

        page += 1

    return repositories


def get_languages(repository_name: str):
    try:
        return github_api(
            f"/repos/{OWNER}/{repository_name}/languages"
        )
    except urllib.error.HTTPError as error:
        print(
            f"Warning: could not read {repository_name}: {error}",
            file=sys.stderr,
        )
        return {}


def format_bytes(value: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    size = float(value)

    for unit in units:
        if size < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(size)} {unit}"

            return f"{size:.1f} {unit}"

        size /= 1024

    return f"{value} B"


repositories = get_repositories()

language_bytes = defaultdict(int)
language_repositories = defaultdict(set)

for repository in repositories:
    repository_name = repository["name"]
    print(f"Scanning {repository_name}...")

    for language, byte_count in get_languages(repository_name).items():
        language_bytes[language] += int(byte_count)
        language_repositories[language].add(repository_name)

total_bytes = sum(language_bytes.values())

sorted_languages = sorted(
    language_bytes,
    key=lambda language: (
        len(language_repositories[language]),
        language_bytes[language],
    ),
    reverse=True,
)

lines = [
    START_MARKER,
    "",
    f"_Automatically generated from **{len(repositories)}** public, "
    "non-fork, non-archived repositories._",
    "",
    "| Language | Repositories |",
    "|---|---:|",
]

for language in sorted_languages:
    byte_count = language_bytes[language]
    repository_count = len(language_repositories[language])
    percentage = (
        byte_count / total_bytes * 100
        if total_bytes
        else 0
    )

    lines.append(
        f"| {language} | {repository_count} |"
    )

lines.extend(
    [
        "",
        END_MARKER,
    ]
)

generated_section = "\n".join(lines)

readme = README_PATH.read_text(encoding="utf-8")

if START_MARKER not in readme or END_MARKER not in readme:
    print(
        "README language markers were not found.",
        file=sys.stderr,
    )
    sys.exit(1)

before = readme.split(START_MARKER, 1)[0].rstrip()
after = readme.split(END_MARKER, 1)[1].lstrip()

updated_readme = (
    before
    + "\n\n"
    + generated_section
    + "\n\n"
    + after
)

README_PATH.write_text(updated_readme, encoding="utf-8")

print(
    f"Updated README with {len(sorted_languages)} languages "
    f"from {len(repositories)} repositories."
)
