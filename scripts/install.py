#!/usr/bin/env python3
"""Merge speed settings and/or alwaysApply rules. Never clobber claw/sandbox/MEMORY.md.

Profiles:
  thinking  — thinking off, minimal effort, defer tools (no memory/plugin/rules)
  office    — thinking + memory off + extra plugins off; keep Tencent Docs/PPT/sheet
  full      — office + also turn off Docs/PPT/sheet + install alwaysApply rules
"""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import datetime
from pathlib import Path

ROOT_KEYS = (
    "alwaysThinkingEnabled",
    "reasoningEffort",
    "autoCompactEnabled",
    "promptSuggestionEnabled",
    "deferToolLoading",
)
RULE_DESTS = (
    Path.home() / ".workbuddy" / "rules",
    Path.home() / ".codebuddy" / "rules",
)
KEEP_OFFICE = {
    "tencent-docs-plugin@workbuddy-builtin",
    "tencent-pptx@workbuddy-builtin",
    "tencent-docx@workbuddy-builtin",
    "sheetagent@workbuddy-builtin",
}


def load_patch(here: Path) -> dict:
    return json.loads((here / "hard-settings.json").read_text(encoding="utf-8"))


def backup_settings(dest: Path) -> Path | None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not dest.exists():
        print("no existing settings; creating new file")
        return None
    backup = dest.with_name(f"settings.json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}")
    shutil.copy2(dest, backup)
    print(f"backup {backup}")
    return backup


def merge_settings(here: Path, profile: str) -> None:
    patch = load_patch(here)
    dest = Path.home() / ".workbuddy" / "settings.json"
    current: dict = {}
    if dest.exists():
        current = json.loads(dest.read_text(encoding="utf-8"))
    backup_settings(dest)

    for key in ROOT_KEYS:
        if key in patch:
            current[key] = patch[key]

    if profile in ("office", "full"):
        memory = dict(current.get("memory") or {})
        memory.update(patch.get("memory") or {})
        current["memory"] = memory
        plugins = dict(current.get("enabledPlugins") or {})
        for name, enabled in (patch.get("enabledPlugins") or {}).items():
            if profile == "office" and name in KEEP_OFFICE:
                continue
            plugins[name] = enabled
        current["enabledPlugins"] = plugins

    current.pop("skillOverrides", None)
    dest.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {dest} profile={profile}")


def install_rules(here: Path) -> None:
    src = here / "rules" / "fast-default.md"
    if not src.exists():
        raise SystemExit(f"missing {src}")
    for folder in RULE_DESTS:
        folder.mkdir(parents=True, exist_ok=True)
        dest = folder / "fast-default.md"
        shutil.copy2(src, dest)
        print(f"rules {dest}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Install WorkBuddy speed pack")
    parser.add_argument(
        "profile",
        choices=("thinking", "office", "full"),
        help="thinking | office | full",
    )
    args = parser.parse_args()
    here = Path(__file__).resolve().parents[1]
    merge_settings(here, args.profile)
    if args.profile == "full":
        install_rules(here)
    print("done. quit WorkBuddy and start a new chat. turn off Max yourself.")


if __name__ == "__main__":
    main()
