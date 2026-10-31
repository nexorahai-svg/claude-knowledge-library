#!/usr/bin/env python3
"""Make this machine match the main one: Claude Code plugins, MCP servers, CLI tools, the
privacy guards on them, Flutter and the Android SDK. Linux, user level only (no sudo).

Usage:
  python3 scripts/setup_machine.py                    # report only: what is there, what is missing
  python3 scripts/setup_machine.py --apply            # install/fix what is missing (idempotent)
  python3 scripts/setup_machine.py --apply --only guards,plugins
  python3 scripts/setup_machine.py --apply --with-optional          # also plugins marked "test"
  python3 scripts/setup_machine.py --apply --accept-android-licenses  # only after the user said yes

Parts: plugins, skills, mcp, npm, guards, flutter, android, system. Every download is checked
against the checksum its publisher lists (Flutter sha256, Android sha1). Anything that needs
sudo is printed for the user to run. What each part is and why: projects/new-machine.md and
projects/user-profile.md.
"""
import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request

HOME = os.path.expanduser("~")
CLAUDE_DIR = os.path.join(HOME, ".claude")
SETTINGS = os.path.join(CLAUDE_DIR, "settings.json")
FLUTTER_DIR = os.path.join(HOME, "development", "flutter")
ANDROID_HOME = os.path.join(HOME, "Android", "Sdk")

# (marketplace repo, plugin@marketplace, optional)
PLUGINS = [
    ("nexorahai-svg/claude-knowledge-library", "knowledge-library@knowledge-library", False),
    ("anthropics/claude-plugins-official", "frontend-design@claude-plugins-official", False),
    ("anthropics/claude-plugins-official", "typescript-lsp@claude-plugins-official", False),   # needs npm typescript-language-server
    ("anthropics/claude-plugins-official", "context7@claude-plugins-official", False),
    ("anthropics/claude-plugins-official", "commit-commands@claude-plugins-official", False),
    ("anthropics/claude-plugins-official", "cloudflare@claude-plugins-official", False),
    ("flutter/skills", "dart-flutter@dart-flutter", False),   # brings its own Dart MCP: no hand-added "dart" server
    ("greensock/gsap-skills", "gsap-skills@gsap-skills", False),
    ("remotion-dev/claude-code-plugin", "remotion@remotion", False),
    ("heygen-com/hyperframes", "hyperframes@hyperframes", False),
    ("Jakeschincariol/instagram-agent-skill", "instagram-agent@instagram-agent-skill", True),
]
# claude.ai-synced plugins kept off on this machine (paid scraping, full shell access, unrelated fields; 2026-10-23)
SYNCED_OFF = ["brightdata-plugin@synced", "desktop-commander@synced", "finance@synced", "data@synced",
              "product-management@synced", "cowork-plugin-management@synced"]
# claude.ai connectors kept out of every Claude Code session here (settings.json deniedMcpServers): write access the
# work does not use (2026-10-23, verified with `claude mcp list`). Does not disconnect them on claude.ai itself.
DENIED_MCP = ["claude.ai Linear", "claude.ai HubSpot"]
# hand-added MCP servers that a plugin now brings itself (would load twice)
MCP_DUPLICATES = {"dart": "dart-flutter@dart-flutter"}
# user skills copied from a repository folder: (name, repo, folder inside the repo)
SKILLS = [("motion-design", "https://github.com/LottieFiles/motion-design-skill", "skills/motion-design")]
MCP = {
    "chrome-devtools": ["npx", "chrome-devtools-mcp@latest", "--isolated", "--no-usage-statistics", "--no-performance-crux"],
    "playwright": ["npx", "@playwright/mcp@latest", "--isolated"],
}   # Dart MCP comes with the dart-flutter plugin (2026-10-23); a hand-added copy would load it twice
NPM_GLOBAL = {"ccusage": "ccusage", "html-validate": "html-validate", "@lhci/cli": "lhci",
              "typescript-language-server@6.0.2": "typescript-language-server"}
DENY = ["Bash(npx hyperframes usage:*)", "Bash(hyperframes usage:*)"]
ENV = {"HYPERFRAMES_NO_TELEMETRY": "1",
       # Resource rule (2026-10-24, after a hard freeze; domains/claude-code/resource-safety.md). Official Claude Code
       # limits: one shared memory cgroup for all Bash/Monitor commands of a session (Linux, v2.1.233+), a warning to
       # Claude when free RAM drops under 4 GiB, and at most 4 parallel subagents / workflow agents (defaults 20 / 16).
       "CLAUDE_CODE_TOOL_MEMORY_LIMIT": "8G", "CLAUDE_CODE_WARN_MEMORY_FREE_GIB": "4",
       "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS": "4", "CLAUDE_CODE_WORKFLOW_MAX_CONCURRENT_AGENTS": "4"}
# Claude Code's own `language` setting puts "Always respond in <language>" into the system prompt, which holds much
# better than a CLAUDE.md line (2026-10-23: replies kept drifting into English between tool calls).
# The library is shared, so the language is each user's own choice, kept on their machine (never in the library):
# ~/.config/knowledge-library/user.json {"language": "Persian (فارسی)"}. With no choice yet, the SessionStart hook has
# Claude ask the user, in the language they write in, and save it with `--set-language`.
USER_CONF = os.path.join(HOME, ".config", "knowledge-library", "user.json")


def user_language():
    return (load_json(USER_CONF, {}) or {}).get("language")
CLAUDE_MD_GUARDS = {
    "HyperFrames (installed user-wide)": (
        "- HyperFrames (installed user-wide): never run `hyperframes usage` (it reads the Claude Code\n"
        "  login token); telemetry stays off (`HYPERFRAMES_NO_TELEMETRY=1`); pin the CLI version inside\n"
        "  each project; keep Persian fonts local; do not set `GEMINI_API_KEY` for `snapshot --describe`.\n"),
    "Instagram Agent Skill": (
        "- Instagram Agent Skill (installed user-wide for testing): never run `ig-human` (humanize.py /\n"
        "  detect.py) on Persian or Arabic text; it strips ZWNJ (نیم‌فاصله), ZWJ and direction marks.\n"),
    "Nothing half-done or forgotten": (
        "- Nothing half-done or forgotten (strictest rule): end every turn that did work with a\n"
        "  \"remaining work\" list (or an explicit \"none\"); never drop or defer anything on your own,\n"
        "  the human decides what is done next.\n"),
    "projects/user-profile.md": (
        "- Read the knowledge library's projects/user-profile.md (taste, budget rules, tool guards)\n"
        "  before choosing tools or designs in any project.\n"),
}
ANDROID_PACKAGES = ["platform-tools", "emulator", "platforms;android-36", "platforms;android-37.0",
                    "build-tools;37.0.0", "build-tools;36.1.0",
                    "system-images;android-37.0;google_apis_playstore;x86_64"]
APT = {"ninja": "ninja-build", "pkg-config": "pkg-config", "javac": "openjdk-21-jdk-headless", "cmake": "cmake", "clang": "clang"}


class Report:
    def __init__(self, apply):
        self.apply, self.rows, self.todo_user = apply, [], []

    def line(self, part, item, ok, note=""):
        mark = "✓" if ok else ("→" if self.apply else "✗")
        self.rows.append(f"{mark} {part:8} {item}{('  — ' + note) if note else ''}")


def sh(cmd, check=False, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, check=check, **kw)


def load_json(path, default):
    try:
        return json.load(open(path, encoding="utf-8"))
    except (OSError, ValueError):
        return default


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
        fh.write("\n")
    os.replace(tmp, path)


def download(url, expect, algo):
    fd, path = tempfile.mkstemp(suffix=os.path.splitext(url)[1] or ".bin")
    os.close(fd)
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "setup-machine"}), timeout=600) as r, \
            open(path, "wb") as fh:
        h = hashlib.new(algo)
        for chunk in iter(lambda: r.read(1 << 20), b""):
            fh.write(chunk)
            h.update(chunk)
    if h.hexdigest() != expect:
        os.remove(path)
        sys.exit(f"Checksum mismatch for {url}: refusing to install")
    return path


# ---------------------------------------------------------------- parts

def part_plugins(r, with_optional):
    if not shutil.which("claude"):
        r.line("plugins", "Claude Code CLI", False, "install Claude Code first")
        return
    listed = sh(["claude", "plugin", "list"]).stdout
    markets = sh(["claude", "plugin", "marketplace", "list"]).stdout
    for repo, plug, optional in PLUGINS:
        if optional and not with_optional:
            continue
        have = plug in listed
        r.line("plugins", plug + (" (test)" if optional else ""), have)
        if not have and r.apply:
            if repo.split("/")[1] not in markets and plug.split("@")[1] not in markets:
                sh(["claude", "plugin", "marketplace", "add", repo])
            sh(["claude", "plugin", "install", plug, "--scope", "user"])


def drift(with_optional=False):
    """Fast, offline check (no network, no subprocess) for the SessionStart hook: what differs from the plan."""
    settings = load_json(SETTINGS, {})
    enabled = settings.get("enabledPlugins", {})
    installed = set((load_json(os.path.join(CLAUDE_DIR, "plugins", "installed_plugins.json"), {}).get("plugins") or {}).keys())
    # the built-in directory is "anthropic-plugin-directory" on some machines: the same plugins, another suffix
    installed |= {p.replace("@anthropic-plugin-directory", "@claude-plugins-official") for p in installed}
    user_mcp = (load_json(os.path.join(HOME, ".claude.json"), {}).get("mcpServers") or {})
    out = {"missing": [p for _, p, opt in PLUGINS if (with_optional or not opt) and p not in installed],
           "turn_off": [p for p in SYNCED_OFF if enabled.get(p) is not False and os.path.isdir(os.path.join(CLAUDE_DIR, "plugins", "synced"))],
           "duplicate_mcp": [m for m, plug in MCP_DUPLICATES.items() if m in user_mcp and plug in installed],
           "language": (["ask the user"] if not user_language() and not settings.get("language") else
                        [user_language()] if user_language() and settings.get("language") != user_language() else []),
           "env": [k for k, v in ENV.items() if settings.get("env", {}).get(k) != v],
           "deny_mcp": [n for n in DENIED_MCP if n not in {e.get("serverName") for e in settings.get("deniedMcpServers", [])
                                                             if isinstance(e, dict)}],
           "npm": [pkg for pkg, binary in NPM_GLOBAL.items() if shutil.which("npm") and not shutil.which(binary)]}
    return {k: v for k, v in out.items() if v}


def part_synced(r):
    settings = load_json(SETTINGS, {})
    enabled = settings.get("enabledPlugins", {})
    for p in SYNCED_OFF:
        off = enabled.get(p) is False
        r.line("synced-off", p, off)
        if not off and r.apply and shutil.which("claude"):
            sh(["claude", "plugin", "disable", p])
    denied = settings.setdefault("deniedMcpServers", [])
    have = {e.get("serverName") for e in denied if isinstance(e, dict)}
    for n in DENIED_MCP:
        r.line("mcp-deny", n, n in have)
        if n not in have and r.apply:
            denied.append({"serverName": n})
    if r.apply and any(n not in have for n in DENIED_MCP):
        save_json(SETTINGS, settings)
    user_mcp = load_json(os.path.join(HOME, ".claude.json"), {}).get("mcpServers") or {}
    installed = set((load_json(os.path.join(CLAUDE_DIR, "plugins", "installed_plugins.json"), {}).get("plugins") or {}).keys())
    for m, plug in MCP_DUPLICATES.items():
        dup = m in user_mcp and plug in installed
        r.line("mcp-dup", f"{m} (comes with {plug})", not dup)
        if dup and r.apply:
            sh(["claude", "mcp", "remove", m, "-s", "user"])


def part_skills(r):
    for name, repo, folder in SKILLS:
        dest = os.path.join(CLAUDE_DIR, "skills", name)
        have = os.path.exists(os.path.join(dest, "SKILL.md"))
        r.line("skills", name, have)
        if not have and r.apply:
            with tempfile.TemporaryDirectory() as t:
                sh(["git", "clone", "-q", "--depth", "1", repo, t], check=True)
                shutil.copytree(os.path.join(t, folder), dest)
                lic = os.path.join(t, "LICENSE")
                if os.path.exists(lic):
                    shutil.copy(lic, dest)


def part_mcp(r):
    if not shutil.which("claude"):
        return
    listed = sh(["claude", "mcp", "list"]).stdout
    for name, cmd in MCP.items():
        have = re.search(rf"^{re.escape(name)}:", listed, re.M) is not None
        r.line("mcp", f"{name} ({' '.join(cmd[1:])})", have)
        if not have and r.apply:
            sh(["claude", "mcp", "add", name, "--scope", "user", "--", *cmd])


def part_npm(r):
    if not shutil.which("npm"):
        r.line("npm", "Node.js / npm", False, "install Node LTS (nvm) first")
        return
    for pkg, binary in NPM_GLOBAL.items():
        have = shutil.which(binary) is not None
        r.line("npm", pkg, have)
        if not have and r.apply:
            sh(["npm", "i", "-g", pkg])


def part_guards(r):
    s = load_json(SETTINGS, {})
    env_ok = all(s.get("env", {}).get(k) == v for k, v in ENV.items())
    deny_ok = all(d in s.get("permissions", {}).get("deny", []) for d in DENY)
    want = user_language()
    lang_ok = bool(s.get("language")) and (not want or s.get("language") == want)
    r.line("guards", f"settings.json: reply language = {s.get('language') or want or 'not chosen yet (Claude asks the user)'}", lang_ok)
    if r.apply and want and s.get("language") != want:
        s["language"] = want
        save_json(SETTINGS, s)
    r.line("guards", "settings.json: HyperFrames telemetry off + `usage` denied + Claude resource limits", env_ok and deny_ok)
    if r.apply and not (env_ok and deny_ok):
        s.setdefault("env", {}).update(ENV)
        deny = s.setdefault("permissions", {}).setdefault("deny", [])
        deny += [d for d in DENY if d not in deny]
        save_json(SETTINGS, s)
    hf = os.path.join(HOME, ".hyperframes", "config.json")
    c = load_json(hf, {})
    r.line("guards", "~/.hyperframes/config.json telemetryEnabled=false", c.get("telemetryEnabled") is False)
    if r.apply and c.get("telemetryEnabled") is not False:
        c["telemetryEnabled"] = False
        save_json(hf, c)
    rc = os.path.join(HOME, ".androidrc")
    have = os.path.exists(rc) and "--no-metrics" in open(rc).read().split()
    r.line("guards", "~/.androidrc --no-metrics", have)
    if r.apply and not have:
        with open(rc, "a") as fh:
            fh.write("--no-metrics\n")
    md = os.path.join(CLAUDE_DIR, "CLAUDE.md")
    text = open(md, encoding="utf-8").read() if os.path.exists(md) else ""
    for key, block in CLAUDE_MD_GUARDS.items():
        have = key in text
        r.line("guards", f"~/.claude/CLAUDE.md: {key}", have)
        if r.apply and not have:
            with open(md, "a", encoding="utf-8") as fh:
                fh.write(("" if text.endswith("\n") or not text else "\n") + block)
            text += block


def part_flutter(r):
    flutter = os.path.join(FLUTTER_DIR, "bin", "flutter")
    have = os.path.exists(flutter)
    r.line("flutter", f"Flutter SDK in {FLUTTER_DIR}", have)
    if not have and r.apply:
        base = "https://storage.googleapis.com/flutter_infra_release/releases/"
        d = json.load(urllib.request.urlopen(base + "releases_linux.json", timeout=60))
        h = d["current_release"]["stable"]
        rel = next(x for x in d["releases"] if x["hash"] == h)
        print(f"Downloading Flutter {rel['version']} (sha256 checked)...")
        archive = download(base + rel["archive"], rel["sha256"], "sha256")
        os.makedirs(os.path.dirname(FLUTTER_DIR), exist_ok=True)
        sh(["tar", "-xf", archive, "-C", os.path.dirname(FLUTTER_DIR)], check=True)
        os.remove(archive)
        sh([flutter, "--disable-analytics"])
    line = f'export PATH="{FLUTTER_DIR}/bin:$PATH"'
    bashrc = os.path.join(HOME, ".bashrc")
    on_path = os.path.exists(bashrc) and "development/flutter/bin" in open(bashrc).read()
    r.line("flutter", "~/.bashrc PATH", on_path)
    if r.apply and not on_path:
        with open(bashrc, "a") as fh:
            fh.write(line + "\n")


def part_android(r, accept):
    tools = os.path.join(ANDROID_HOME, "cmdline-tools", "latest", "bin")
    have = os.path.exists(os.path.join(tools, "sdkmanager"))
    r.line("android", "command-line tools", have)
    if not have and r.apply:
        xml = urllib.request.urlopen("https://dl.google.com/android/repository/repository2-3.xml", timeout=60).read().decode()
        cands = re.findall(r'<checksum type="sha1">(\w+)</checksum>\s*<url>(commandlinetools-linux-(\d+)_latest\.zip)</url>', xml)
        sha1, name, _ = max(cands, key=lambda t: int(t[2]))
        print(f"Downloading {name} (sha1 checked)...")
        z = download("https://dl.google.com/android/repository/" + name, sha1, "sha1")
        with tempfile.TemporaryDirectory() as t:
            sh(["unzip", "-q", z, "-d", t], check=True)
            os.makedirs(os.path.dirname(os.path.dirname(tools)), exist_ok=True)
            shutil.move(os.path.join(t, "cmdline-tools"), os.path.dirname(tools))
        os.remove(z)
    installed = os.path.exists(os.path.join(ANDROID_HOME, "platform-tools", "adb"))
    r.line("android", "SDK packages (platform 36/37, build-tools, emulator, system image)", installed,
           "" if installed or accept else "needs --accept-android-licenses (only after the user says yes)")
    if r.apply and not installed and accept and os.path.exists(os.path.join(tools, "sdkmanager")):
        sm = os.path.join(tools, "sdkmanager")
        subprocess.run(f"yes | {sm} --licenses", shell=True, capture_output=True)
        sh([sm, "--install", *ANDROID_PACKAGES])
        sh([os.path.join(tools, "avdmanager"), "create", "avd", "-n", "pixel_api37", "-k", ANDROID_PACKAGES[-1],
            "-d", "pixel_8"], input="no\n")
        flutter = os.path.join(FLUTTER_DIR, "bin", "flutter")
        if os.path.exists(flutter):
            sh([flutter, "config", "--android-sdk", ANDROID_HOME])
            subprocess.run(f"yes | {flutter} doctor --android-licenses", shell=True, capture_output=True)
    bashrc = os.path.join(HOME, ".bashrc")
    on_path = os.path.exists(bashrc) and "ANDROID_HOME" in open(bashrc).read()
    r.line("android", "~/.bashrc ANDROID_HOME and PATH", on_path)
    if r.apply and not on_path:
        with open(bashrc, "a") as fh:
            fh.write('export ANDROID_HOME="$HOME/Android/Sdk"\n'
                     'export PATH="$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$PATH"\n')
    kvm = os.access("/dev/kvm", os.R_OK | os.W_OK)
    r.line("android", "emulator acceleration (/dev/kvm usable)", kvm, "" if kvm else "user must be in the kvm group")


def part_system(r):
    missing = [pkg for binary, pkg in APT.items() if not shutil.which(binary)]
    r.line("system", "build tools for Flutter Linux/Android (" + ", ".join(APT.values()) + ")", not missing)
    if missing:
        r.todo_user.append("sudo apt install -y " + " ".join(missing))


def main():
    ap = argparse.ArgumentParser(description="Make this machine match the main one (see the module docstring).")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--only", default="plugins,synced,skills,mcp,npm,guards,flutter,android,system")
    ap.add_argument("--drift", action="store_true", help="print the offline drift check as JSON and exit")
    ap.add_argument("--set-language", metavar="LANG", help='save this user\'s reply language, e.g. "Persian (فارسی)", '
                    '"Arabic (العربية)", "English", and apply it to Claude Code at once')
    ap.add_argument("--with-optional", action="store_true")
    ap.add_argument("--accept-android-licenses", action="store_true")
    a = ap.parse_args()
    if a.set_language:
        conf = load_json(USER_CONF, {}) or {}
        conf["language"] = a.set_language
        os.makedirs(os.path.dirname(USER_CONF), exist_ok=True)
        save_json(USER_CONF, conf)
        st = load_json(SETTINGS, {})
        st["language"] = a.set_language
        save_json(SETTINGS, st)
        print(f"Reply language set to {a.set_language} (Claude Code settings + {USER_CONF}). New sessions use it.")
        return
    if a.drift:
        print(json.dumps(drift(a.with_optional)))
        return
    if not sys.platform.startswith("linux"):
        print("Linux only for now; on another system follow projects/new-machine.md by hand.")
    r = Report(a.apply)
    parts = set(a.only.split(","))
    if "system" in parts:
        part_system(r)
    if "plugins" in parts:
        part_plugins(r, a.with_optional)
    if "synced" in parts:
        part_synced(r)
    if "skills" in parts:
        part_skills(r)
    if "npm" in parts:
        part_npm(r)
    if "guards" in parts:
        part_guards(r)
    if "flutter" in parts:
        part_flutter(r)
    if "android" in parts:
        part_android(r, a.accept_android_licenses)
    if "mcp" in parts:
        part_mcp(r)   # last: the dart server needs Flutter
    print("\n".join(r.rows))
    if r.todo_user:
        print("\nRun these yourself (they need your password):")
        for c in r.todo_user:
            print("  " + c)
    if not a.apply and any(row.startswith("✗") for row in r.rows):
        print("\nTo install what is missing: python3 scripts/setup_machine.py --apply")
    if a.apply:
        print("\nDone. Restart Claude Code so new plugins and MCP servers load.")


if __name__ == "__main__":
    main()
