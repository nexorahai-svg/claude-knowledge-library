#!/usr/bin/env python3
"""Rebuild everything and run all checks, in order.

Usage:  python3 scripts/build_all.py
Steps: sources + changelog registries -> catalog index -> llms.txt + catalog/index.json -> dashboard -> lint -> links -> due report.
Exits 1 if lint or link checks fail.
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STEPS = [
    ["build_registry.py"],
    ["build_catalog.py"],
    ["build_llms.py"],
    ["build_dashboard.py"],
    ["lint_library.py"],
    ["check_links.py"],
    ["build_catalog.py", "--due"],
]


def main():
    failed = False
    for step in STEPS:
        print(f"== {' '.join(step)}")
        # -X utf8: -I ignores PYTHONUTF8, and on Windows a piped stdout is cp1252, which cannot print Persian
        res = subprocess.run([sys.executable, "-I", "-X", "utf8", os.path.join(HERE, step[0]), *step[1:]])
        if res.returncode != 0:
            failed = True
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
