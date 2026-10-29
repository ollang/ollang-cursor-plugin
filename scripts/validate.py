#!/usr/bin/env python3
"""Dependency-free package checks; not an authenticated Cursor runtime test."""

import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise SystemExit(message)


def relative_file(value):
    require(isinstance(value, str) and value, "Empty or invalid component path")
    path = Path(value)
    require(not path.is_absolute() and ".." not in path.parts, f"Unsafe path: {value}")
    resolved = (ROOT / path).resolve()
    require(resolved.is_relative_to(ROOT), f"Path escapes package: {value}")
    require(resolved.exists(), f"Missing path: {value}")
    return resolved


manifest = json.loads((ROOT / ".cursor-plugin/plugin.json").read_text())
require(bool(re.fullmatch(r"[a-z0-9]+(?:[.-][a-z0-9]+)*", manifest["name"])), "Invalid plugin name")
require(bool(re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"])), "Invalid release version")
require(bool(manifest.get("description")), "Missing description")
require(manifest["author"]["name"] == "Ollang Inc.", "Unexpected publisher")
require(manifest["license"] == "MIT", "Manifest/license mismatch")
require("hooks" not in manifest and "variables" not in manifest, "Unexpected scripts or credentials")

for key in ("homepage", "repository"):
    require(manifest[key].startswith("https://"), f"Expected HTTPS {key}")
for key in ("logo", "skills", "mcpServers"):
    relative_file(manifest[key])

mcp = json.loads(relative_file(manifest["mcpServers"]).read_text())
require(mcp == {"mcpServers": {"ollang": {"url": "https://mcp.ollang.com/mcp"}}},
        "Unexpected MCP config; do not include headers, tokens or local commands")

skills = list(relative_file(manifest["skills"]).glob("*/SKILL.md"))
require(bool(skills), "Missing workflow skill")
for skill in skills:
    text = skill.read_text()
    require(text.startswith("---\n") and "\n---\n" in text[4:], f"Invalid frontmatter: {skill.name}")
    frontmatter = text.split("---", 2)[1]
    require(bool(re.search(r"^name: [a-z0-9-]+$", frontmatter, re.M)), "Invalid skill name")
    require(bool(re.search(r"^description: .+", frontmatter, re.M)), "Missing skill description")

for asset in (ROOT / "assets").glob("*.svg"):
    tree = ET.parse(asset)
    for node in tree.iter():
        require(node.tag.rsplit("}", 1)[-1] not in {"script", "foreignObject"}, "Active SVG content")
        require(not any(key.lower().startswith("on") for key in node.attrib), "SVG event handler")
        for key, value in node.attrib.items():
            if key.rsplit("}", 1)[-1] == "href":
                require(value.startswith("#"), "External SVG reference")

for path in (ROOT / "README.md", ROOT / "LICENSE"):
    require(path.is_file() and path.stat().st_size > 0, f"Missing {path.name}")

require(not any(ROOT.glob(".env*")), "Environment files must not enter the public package")
print(f"Package checks passed: {manifest['name']} {manifest['version']}; one OAuth MCP endpoint; {len(skills)} skill.")
print("Authenticated Cursor connection and marketplace review are separate checks.")
