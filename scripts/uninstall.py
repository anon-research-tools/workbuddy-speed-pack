#!/usr/bin/env python3
"""Remove speed-pack rules and restore the newest settings.json.bak-* if present."""

from __future__ import annotations

import shutil
from pathlib import Path

RULES = (
    Path.home() / ".workbuddy" / "rules" / "fast-default.md",
    Path.home() / ".codebuddy" / "rules" / "fast-default.md",
)


def restore_settings() -> None:
    dest = Path.home() / ".workbuddy" / "settings.json"
    backups = sorted(
        dest.parent.glob("settings.json.bak-*"),
        key=lambda p: p.stat().st_mtime,
        reverse=True,
    )
    if not backups:
        print("no settings.json.bak-* found; left settings.json untouched")
        return
    src = backups[0]
    shutil.copy2(src, dest)
    print(f"restored {dest} from {src}")


def remove_rules() -> None:
    for path in RULES:
        if path.exists():
            path.unlink()
            print(f"removed {path}")
        else:
            print(f"missing {path}")


def main() -> None:
    restore_settings()
    remove_rules()
    print("done. quit WorkBuddy and start a new chat.")


if __name__ == "__main__":
    main()
