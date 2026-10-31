#!/usr/bin/env python3
"""Release gate: nothing is uploaded or published unless the project's real-state test passed on this exact code.

Why (2026-10-25): a project shipped two defects past 163 green test suites, because every suite ran on a "lab" app
(all modules on, default switches) and none on the state the user really has (the real pack installed by the real
installer, only its modules on, the user's switches, the user's hardware). A memory rule did not stop it; this does.

Each project declares its gate in `<repo>/.release-gate.json`:
    {"test": "node scripts/test-real-state.js",          # the real-state test; exit 0 = pass
     "patterns": ["publish-full", "publish-light"]}       # extra commands that upload or publish (regex, optional)

  release_gate.py pass  [--root DIR]   run the test; on success write .release-gate-pass.json for this code state
  release_gate.py check [--root DIR]   exit 0 if the pass matches the current code, else print why and exit 1

The plugin's PreToolUse hook (pre_tool_guard.py) calls check() before any upload/publish command and denies it when
the pass is missing or stale. The pass is bound to the commit and to every uncommitted change, so editing one line
after the test means testing again. Only this script writes the pass file; never write it by hand.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys

CONFIG, PASS = ".release-gate.json", ".release-gate-pass.json"
# commands that ship something to users, in any project
GENERIC = (r"gh\s+release\s+(create|upload|edit)\b|wrangler\s+r2\s+object\s+put\b|rclone\s+(copy|copyto|sync|move)\b|"
           r"aws\s+s3\s+(cp|sync|mv)\b|netlify\s+deploy\b[^|;&]*--prod|vercel\b[^|;&]*--prod|firebase\s+deploy\b|"
           r"eas\s+(submit|update)\b|fastlane\s+\S*\s*(deliver|supply|pilot|upload_to\w*)\b|"
           # touching upload credentials counts as shipping too (ad-hoc upload scripts have no fixed name)
           r"cloudflare\.env\b|\br2[\w.-]*\.env\b|gh\s+auth\s+token\b|PutObjectCommand|client-s3\b|"
           r"\b(AWS_SECRET_ACCESS_KEY|R2_SECRET\w*|R2_ACCESS_KEY\w*|CLOUDFLARE_API_TOKEN)\b")


def git(root, *args):
    return subprocess.run(["git", "-C", root, *args], capture_output=True, text=True, timeout=20).stdout


def repo_root(start):
    out = git(start, "rev-parse", "--show-toplevel").strip()
    return out or None


def code_state(root):
    """The commit plus a hash of every uncommitted change (tracked diff and untracked files), ignoring the pass file."""
    head = git(root, "rev-parse", "HEAD").strip()
    h = hashlib.sha256()
    h.update(git(root, "diff", "HEAD", "--", ".", f":(exclude){PASS}").encode())
    for line in sorted(git(root, "ls-files", "--others", "--exclude-standard").splitlines()):
        if line == PASS:
            continue
        h.update(line.encode())
        try:
            with open(os.path.join(root, line), "rb") as f:
                h.update(hashlib.sha256(f.read()).digest())
        except OSError:
            pass
    return head, h.hexdigest()[:16]


def candidate_roots(cmd, cwd):
    """Repos a command may act on: the cwd's repo, every directory named in the command (cd, pushd, git -C, --root,
    absolute or ~ paths), and, when the cwd itself is not a repo, its sub-repos that declare a gate (depth 2)."""
    cwd = cwd or os.getcwd()
    dirs = [cwd]
    for m in re.finditer(r"(?:\bcd|\bpushd|git\s+-C|--root)\s+(['\"]?)([^'\";&|]+?)\1(?=\s*(?:&&|;|\||$|\s))", cmd):
        dirs.append(m.group(2).strip())
    dirs += re.findall(r"(?<![\w.])((?:~|/home)/[^\s'\";&|]+)", cmd)
    roots = []
    for d in dirs:
        d = os.path.expanduser(d)
        if not os.path.isabs(d):
            d = os.path.join(cwd, d)
        d = d if os.path.isdir(d) else os.path.dirname(d)
        r = repo_root(d) if os.path.isdir(d) else None
        if r and r not in roots:
            roots.append(r)
    if not repo_root(cwd):
        for base, subdirs, files in os.walk(cwd):
            if base.count(os.sep) - cwd.count(os.sep) >= 2:
                subdirs[:] = []
            subdirs[:] = [x for x in subdirs if not x.startswith(".") and x != "node_modules"]
            if CONFIG in files and base not in roots:
                roots.append(base)
    return roots


def load_config(root):
    try:
        return json.load(open(os.path.join(root, CONFIG), encoding="utf-8"))
    except (OSError, ValueError):
        return None


def matches(cmd, cfg):
    pats = [GENERIC] + list((cfg or {}).get("patterns") or [])
    return any(re.search(p, cmd, re.I) for p in pats)


def check(root):
    """(ok, reason)."""
    cfg = load_config(root)
    if not cfg or not cfg.get("test"):
        return False, (f"this project has no {CONFIG} declaring its real-state test, so nothing may be shipped yet. "
                       "Write the test first (see the library's domains/apps/app-testing.md, 'release gate'), declare it, "
                       "then run the gate.")
    try:
        p = json.load(open(os.path.join(root, PASS), encoding="utf-8"))
    except (OSError, ValueError):
        return False, "the real-state test has not passed on this code yet."
    head, dirty = code_state(root)
    if p.get("head") != head or p.get("dirty") != dirty:
        return False, "the code changed after the last passing real-state test, so it must pass again."
    if p.get("test") != cfg["test"]:
        return False, "the declared test command changed after the last pass."
    return True, f"passed {p.get('at')} on {head[:8]}"


def run_pass(root):
    cfg = load_config(root)
    if not cfg or not cfg.get("test"):
        print(f"No {CONFIG} with a \"test\" command in {root}.")
        return 2
    print(f"Running the real-state test: {cfg['test']}")
    code = subprocess.run(cfg["test"], shell=True, cwd=root).returncode
    if code != 0:
        print(f"Real-state test FAILED (exit {code}); no pass written. Fix the cause everywhere, then run again.")
        try:
            os.remove(os.path.join(root, PASS))
        except OSError:
            pass
        return 1
    head, dirty = code_state(root)
    with open(os.path.join(root, PASS), "w", encoding="utf-8") as f:
        json.dump({"head": head, "dirty": dirty, "test": cfg["test"],
                   "at": dt.datetime.now().isoformat(timespec="seconds")}, f, indent=1)
    print(f"Real-state test passed; gate open for {head[:8]} (+ current uncommitted changes).")
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("action", choices=["pass", "check"])
    ap.add_argument("--root", default=os.getcwd())
    a = ap.parse_args()
    root = repo_root(a.root) or a.root
    if a.action == "pass":
        sys.exit(run_pass(root))
    ok, why = check(root)
    print(("OK: " if ok else "BLOCKED: ") + why)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
