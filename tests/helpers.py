from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Iterable

ROOT_DIR = Path(__file__).resolve().parents[1]
JSON_DIR = ROOT_DIR / "JSON"


def load_json(relative_path: str) -> dict[str, Any]:
    path = ROOT_DIR / relative_path
    return json.loads(path.read_text(encoding="utf-8"))


def load_text(relative_path: str) -> str:
    path = ROOT_DIR / relative_path
    return path.read_text(encoding="utf-8")


def write_json(relative_path: str, payload: dict[str, Any]) -> None:
    path = ROOT_DIR / relative_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def parse_semver_like(version: str) -> tuple[int, ...]:
    """Parse versions like 20.2.0 or 20.2.0.min (suffixes are ignored)."""
    cleaned = version.replace(".min", "")
    parts = cleaned.split(".")
    return tuple(int(part) for part in parts if part.isdigit())


def iter_versioned_json_files() -> list[Path]:
    return sorted(
        JSON_DIR.glob("Comm-SCI-v*.json"),
        key=lambda path: parse_semver_like(extract_version_from_filename(path)),
    )


def extract_version_from_filename(path: Path) -> str:
    match = re.match(r"^Comm-SCI-v(.+)\.json$", path.name)
    if not match:
        raise ValueError(f"Invalid filename for version extraction: {path.name}")
    return match.group(1)


def command_tokens(document: dict[str, Any]) -> list[str]:
    groups: dict[str, Any]
    if "commands" in document:
        groups = document["commands"]
    else:
        groups = document["command_model"]["groups"]

    tokens: list[str] = []
    for value in groups.values():
        if isinstance(value, dict):
            tokens.extend(value.keys())
        elif isinstance(value, list):
            tokens.extend(token for token in value if isinstance(token, str))
    return tokens


def recursive_keys(value: Any) -> Iterable[str]:
    if isinstance(value, dict):
        for key, nested in value.items():
            yield key
            yield from recursive_keys(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from recursive_keys(nested)
