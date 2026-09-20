#!/usr/bin/env python3
"""Install global speed settings + alwaysApply rules. Never clobber claw/sandbox/MEMORY.md."""

from __future__ import annotations

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


def merge_settings(here: Path) -> Path | None:
    patch = json.loads((here / "hard-settings.json").read_text(encoding="utf-8"))
    dest = Path.home() / ".workbuddy" / "settings.json"
    dest.parent.mkdir(parents=True, exist_ok=True)
    current: dict = {}
    backup = None
    if dest.exists():
        current = json.loads(dest.read_text(encoding="utf-8"))
        backup = dest.with_name(
            f"settings.json.bak-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        )
        shutil.copy2(dest, backup)
        print(f"backup {backup}")
    else:
        print("no existing settings; creating new file")

    for key in ROOT_KEYS:
        if key in patch:
            current[key] = patch[key]

    memory = dict(current.get("memory") or {})
    memory.update(patch.get("memory") or {})
    current["memory"] = memory

    plugins = dict(current.get("enabledPlugins") or {})
    for name, enabled in (patch.get("enabledPlugins") or {}).items():
        plugins[name] = enabled
    current["enabledPlugins"] = plugins
    current.pop("skillOverrides", None)

    dest.write_text(json.dumps(current, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {dest}")
    return backup


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
    here = Path(__file__).resolve().parents[1]
    merge_settings(here)
    install_rules(here)
    print("done. quit WorkBuddy and start a new chat. turn off Max yourself.")


if __name__ == "__main__":
    main()
