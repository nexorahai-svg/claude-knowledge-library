#!/usr/bin/env python3
"""Keep any copy of the knowledge library in sync with the private GitHub repository.

Usage:  python3 scripts/sync.py            # sync this copy (run from anywhere inside it)
        python3 scripts/sync.py --check    # only report: ahead / behind / local changes

What it does, depending on what this folder is:
  A. A clone with the GitHub remote: commit local changes (after build_all.py passes), then
     pull --rebase and push. Newer GitHub work comes in; newer local work goes out.
  B. An old copy of the repository from before the remote existed (has .git, no "origin"):
     add the remote, then do the same as A. Shared history lets git line the two up.
  Contributor (a friend with the Read role, or KL_CONTRIBUTOR=1): instead of pushing, local
     commits go to a branch of the friend's fork and a pull request to the owner; main on GitHub
     only changes when the owner merges it.
  C. A plain copy without .git: nothing is overwritten. The script makes a fresh clone next to
     it, lists every file that differs, and copies files that exist only in the old copy into
     research/inbox/sync-from-copy-<date>/ of the fresh clone so nothing is lost. A person (or
     Claude) then merges them by hand and runs this script in the fresh clone.

Generated files (catalog/README.md, catalog/index.json, llms.txt, dashboard/index.html) are
never merged by hand: on a rebase conflict in them the script rebuilds them and continues.
A conflict in a hand-written file stops the script with a clear message; nothing is discarded.
"""
import datetime
import filecmp
import os
import re
import socket
import subprocess
import sys

OLD_PATH = "owner/knowledge-library"
NEW_PATH = "nexorahai-svg/claude-knowledge-library"
SSH_URL = "https://github.com/nexorahai-svg/claude-knowledge-library.git"
HTTPS_URL = "https://github.com/nexorahai-svg/claude-knowledge-library.git"


def default_remote():
    """SSH, unless GitHub CLI is logged in with HTTPS (the default of `gh auth login`): then no SSH key is on the
    account and SSH would fail with "Permission denied (publickey)" (seen 2026-10-19)."""
    try:
        r = subprocess.run(["gh", "config", "get", "git_protocol", "-h", "github.com"], capture_output=True, text=True)
        a = subprocess.run(["gh", "auth", "status"], capture_output=True, text=True)
        if a.returncode == 0 and r.stdout.strip() == "https":
            subprocess.run(["gh", "auth", "setup-git"], capture_output=True, text=True)   # git uses gh's login
            return HTTPS_URL
    except OSError:
        pass   # no GitHub CLI
    return SSH_URL


REMOTE = os.environ.get("KL_REMOTE") or default_remote()
BRANCH = "main"
GENERATED = {"catalog/README.md", "catalog/index.json", "llms.txt", "llms-full.txt", "dashboard/index.html",
             "research/sweep-state.json", "sources/README.md", "CHANGELOG.md", ".registry-state.json"}
SKIP_DIRS = {".git", "__pycache__", "node_modules"}


def run(cmd, cwd, check=True):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed:\n{r.stdout}{r.stderr}")
    return r


def git(args, cwd, check=True):
    return run(["git", *args], cwd, check)


def library_root(start):
    d = os.path.abspath(start)
    while True:
        if os.path.isfile(os.path.join(d, "CLAUDE.md")) and os.path.isdir(os.path.join(d, "catalog")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            sys.exit("Not inside a knowledge-library folder (no CLAUDE.md + catalog/ found).")
        d = parent


def build(root):
    r = run([sys.executable, "scripts/build_all.py"], root, check=False)
    tail = "\n".join((r.stdout + r.stderr).strip().splitlines()[-6:])
    if r.returncode != 0:
        sys.exit(f"build_all.py failed; fix the errors before syncing:\n{tail}")
    return tail


def status(root):
    git(["fetch", "--quiet", "origin", BRANCH], root)
    dirty = git(["status", "--porcelain"], root).stdout.strip()
    counts = git(["rev-list", "--left-right", "--count", f"HEAD...origin/{BRANCH}"], root).stdout.split()
    ahead, behind = int(counts[0]), int(counts[1])
    return dirty, ahead, behind


def add_generated(root):
    # Stage only generated files that exist: one missing path (e.g. research/sweep-state.json on a machine that
    # never ran a sweep) makes a single `git add` fail as a whole, which left the conflict unstaged and looped
    # rebase_onto_remote forever (2026-10-21, یک فروشگاه مشتری on debian: 40 minutes).
    for f in sorted(GENERATED):
        if os.path.exists(os.path.join(root, f)):
            git(["add", "--", f], root, check=False)


MAX_REBASE_STEPS = 50


def rebase_onto_remote(root):
    r = git(["rebase", f"origin/{BRANCH}"], root, check=False)
    steps = 0
    while r.returncode != 0:
        steps += 1
        if steps > MAX_REBASE_STEPS:
            git(["rebase", "--abort"], root, check=False)
            sys.exit(f"Rebase did not finish after {MAX_REBASE_STEPS} steps; aborted, nothing lost.\n{r.stdout}{r.stderr}")
        conflicted = set(git(["diff", "--name-only", "--diff-filter=U"], root).stdout.split())
        if not conflicted:
            git(["rebase", "--abort"], root, check=False)
            sys.exit(f"Rebase stopped without file conflicts; aborted, nothing lost.\n{r.stdout}{r.stderr}")
        hand_written = conflicted - GENERATED
        if hand_written:
            git(["rebase", "--abort"], root, check=False)
            sys.exit("Conflict in hand-written files; rebase aborted, nothing lost. Merge these by hand "
                     "(keep both sides' findings), commit, and run sync again:\n  " + "\n  ".join(sorted(hand_written)))
        # The other side's sources table or changelog may carry rows/sections added the old way:
        # move them into their own files before our version of the generated file wins.
        for f in sorted(conflicted & {"sources/README.md", "CHANGELOG.md"}):
            upstream = git(["show", f":2:{f}"], root, check=False).stdout
            if upstream and os.path.exists(os.path.join(root, "scripts", "build_registry.py")):
                with open(os.path.join(root, f), "w", encoding="utf-8") as fh:
                    fh.write(upstream)
                run([sys.executable, "-I", "-X", "utf8", "scripts/build_registry.py", "--absorb"], root, check=False)
        for f in conflicted:
            git(["checkout", "--theirs", f], root, check=False)
        build(root)
        add_generated(root)
        still = set(git(["diff", "--name-only", "--diff-filter=U"], root).stdout.split())
        if still:
            git(["rebase", "--abort"], root, check=False)
            sys.exit("Generated files are still unmerged after rebuilding; rebase aborted, nothing lost:\n  "
                     + "\n  ".join(sorted(still)))
        r = run(["git", "-c", "core.editor=true", "rebase", "--continue"], root, check=False)


def source_ids(root, ref=None):
    """Source IDs at a git ref (or in the working tree): one file per source, plus anchors of
    the old single-file layout so a machine that has not migrated yet is still understood."""
    if ref:
        names = git(["ls-tree", "--name-only", f"{ref}:sources"], root, check=False).stdout.split()
        readme = git(["show", f"{ref}:sources/README.md"], root, check=False).stdout
    else:
        d = os.path.join(root, "sources")
        names = os.listdir(d) if os.path.isdir(d) else []
        p = os.path.join(d, "README.md")
        readme = open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    ids = {n[:-3] for n in names if re.fullmatch(r"S\d+\.md", n)}
    ids |= {a.upper() for a in re.findall(r'<a id="(s\d+)"></a>', readme)}
    return ids


def renumber_collisions(root, ahead):
    """Two machines took the same source number: renumber ours before it is committed.
    (2026-10-21 S129 and S131 were each taken twice and had to be merged by hand.)"""
    if os.path.exists(os.path.join(root, "scripts", "build_registry.py")):
        run([sys.executable, "-I", "-X", "utf8", "scripts/build_registry.py"], root, check=False)   # old-style additions into files first
    base = git(["merge-base", "HEAD", f"origin/{BRANCH}"], root, check=False).stdout.strip()
    if not base:
        return False
    base_ids, remote_ids, local_ids = source_ids(root, base), source_ids(root, f"origin/{BRANCH}"), source_ids(root)
    clashes = sorted((local_ids - base_ids) & (remote_ids - base_ids), key=lambda x: int(x[1:]))
    if not clashes:
        return False
    if ahead:   # our unpushed commits also carry the number: fold them into the working tree
        git(["reset", "--soft", base], root)
    changed = set(git(["diff", "--name-only", base], root).stdout.split())
    changed |= set(git(["ls-files", "-o", "--exclude-standard"], root).stdout.split())
    changed -= GENERATED
    taken = {int(i[1:]) for i in remote_ids | local_ids}
    for old in clashes:
        new = f"S{max(taken) + 1}"
        taken.add(int(new[1:]))
        print(f"Source {old} was also taken on another machine: ours becomes {new}")
        src, dst = os.path.join(root, "sources", f"{old}.md"), os.path.join(root, "sources", f"{new}.md")
        if os.path.exists(src):
            os.rename(src, dst)
            changed.discard(f"sources/{old}.md")
            changed.add(f"sources/{new}.md")
        for rel in sorted(changed):
            p = os.path.join(root, rel)
            if not os.path.isfile(p) or not rel.endswith((".md", ".txt", ".json", ".yaml")):
                continue
            text = open(p, encoding="utf-8").read()
            out = re.sub(rf"\b{old}\b", new, text)
            out = re.sub(rf"#{old.lower()}\b", f"#{new.lower()}", out)
            if out != text:
                with open(p, "w", encoding="utf-8") as fh:
                    fh.write(out)
    return True


def sync_git(root, check_only):
    remotes = git(["remote"], root).stdout.split()
    if "origin" not in remotes:
        print(f"No 'origin' remote: this is an older copy. Adding {REMOTE}")
        if not check_only:
            git(["remote", "add", "origin", REMOTE], root)
        else:
            return
    else:
        url = git(["remote", "get-url", "origin"], root).stdout.strip()
        if OLD_PATH in url:   # the repository moved to the MZia-ai organization on 2026-10-19
            print(f"Updating the old address {url} to {url.replace(OLD_PATH, NEW_PATH)}")
            if not check_only:
                git(["remote", "set-url", "origin", url.replace(OLD_PATH, NEW_PATH)], root)
    dirty, ahead, behind = status(root)
    print(f"local changes: {'yes' if dirty else 'no'} | local commits not on GitHub: {ahead} | GitHub commits not here: {behind}")
    if check_only:
        return
    if (dirty or ahead) and behind and renumber_collisions(root, ahead):
        dirty, ahead, behind = status(root)
    if dirty:
        print("Building and committing local changes...")
        build(root)
        git(["add", "-A"], root)
        msg = f"Sync local changes from {socket.gethostname()} ({datetime.date.today()})"
        git(["commit", "-q", "-m", msg], root)
        ahead += 1
    if behind:
        print("Bringing in newer work from GitHub...")
        rebase_onto_remote(root)
        build(root)
        if git(["status", "--porcelain"], root).stdout.strip():
            add_generated(root)
            git(["commit", "-q", "-m", "Rebuild generated files after sync"], root, check=False)
    _, ahead, behind = status(root)
    if ahead:
        # a commit made by hand may never have been checked: check before anything leaves this machine
        # (2026-10-19 a duplicate source number reached GitHub this way)
        build(root)
    if ahead and not can_push(root):
        propose_changes(root, ahead)
    elif ahead:
        print(f"Sending {ahead} commit(s) to GitHub...")
        git(["push", "-u", "origin", f"HEAD:{BRANCH}"], root)
    _, ahead, behind = status(root)
    print("In sync with GitHub." if not ahead and not behind else f"Still out of sync (ahead {ahead}, behind {behind}).")


def can_push(root):
    """Friends have the Read role in the MZia-ai organization: they read and propose, never push."""
    if os.environ.get("KL_CONTRIBUTOR"):
        return False
    r = run(["gh", "api", f"repos/{NEW_PATH}", "--jq", ".permissions.push"], root, check=False)
    return r.returncode != 0 or r.stdout.strip() != "false"   # unknown -> try a normal push


def propose_changes(root, ahead):
    """Contributor mode: put the local commits on a branch of the friend's own fork and open a pull
    request. The owner reviews it; main on GitHub never changes without the owner's approval."""
    branch = f"contrib/{socket.gethostname()}-{datetime.datetime.now():%Y%m%d-%H%M}"
    print(f"You can read this library but not push to it. Proposing {ahead} commit(s) as a pull request...")
    git(["branch", branch], root)
    me = run(["gh", "api", "user", "--jq", ".login"], root, check=False).stdout.strip()
    if not me:
        sys.exit(f"Your commits are safe on branch {branch}. Log in with `gh auth login`, then run sync again.")
    run(["gh", "repo", "fork", NEW_PATH, "--remote=false", "--clone=false"], root, check=False)
    fork = f"https://github.com/{me}/knowledge-library.git"
    if "fork" not in git(["remote"], root).stdout.split():
        git(["remote", "add", "fork", fork], root)
    git(["push", "-u", "fork", branch], root)
    title = git(["log", "-1", "--format=%s", branch], root).stdout.strip()
    body = ("Proposed from a contributor copy by scripts/sync.py.\n\n"
            + git(["log", "--format=- %s", f"origin/{BRANCH}..{branch}"], root).stdout)
    r = run(["gh", "pr", "create", "--repo", NEW_PATH, "--base", BRANCH, "--head", f"{me}:{branch}",
             "--title", title[:120], "--body", body], root, check=False)
    print(r.stdout.strip() or r.stderr.strip())
    git(["reset", "--keep", f"origin/{BRANCH}"], root)   # main follows GitHub again; the work lives on the branch
    print(f"Done. Your work is on branch {branch} and in the pull request above; the owner will review it.")


def sync_plain_copy(root, check_only):
    target = root.rstrip("/") + "-from-github"
    print(f"This folder has no .git: it is a plain copy. Nothing in it will be changed.")
    if check_only:
        print(f"Run without --check to make a fresh clone at {target} and list the differences.")
        return
    if not os.path.exists(target):
        run(["git", "clone", "--quiet", REMOTE, target], os.path.dirname(target))
    keep = os.path.join(target, "research", "inbox", f"sync-from-copy-{datetime.date.today()}")
    only_here, differ = [], []
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
        for f in files:
            rel = os.path.relpath(os.path.join(d, f), root)
            other = os.path.join(target, rel)
            if not os.path.exists(other):
                only_here.append(rel)
            elif rel not in GENERATED and not filecmp.cmp(os.path.join(d, f), other, shallow=False):
                differ.append(rel)
    for rel in only_here + differ:
        dst = os.path.join(keep, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(os.path.join(root, rel), "rb") as s, open(dst, "wb") as o:
            o.write(s.read())
    print(f"Fresh clone: {target}")
    print(f"Files only in the old copy: {len(only_here)} | files that differ: {len(differ)}")
    if only_here or differ:
        print(f"Copies of all of them are saved in {keep}. Merge what is genuinely new into the clone, "
              f"then run: python3 {target}/scripts/sync.py")


def main():
    check_only = "--check" in sys.argv
    root = library_root(os.getcwd() if len(sys.argv) < 2 or sys.argv[-1].startswith("--") else sys.argv[-1])
    if os.path.isdir(os.path.join(root, ".git")):
        sync_git(root, check_only)
    else:
        sync_plain_copy(root, check_only)


if __name__ == "__main__":
    main()
