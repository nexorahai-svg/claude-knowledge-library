---
name: knowledge-library
description: The user's personal knowledge library of verified tools, methods and sources for their main work: cross-platform apps (mobile and desktop), websites, and social media content (video, images, posts), plus Claude Code cost, plugins, MCP servers, skills and agents. Use it in EVERY project: before choosing or recommending any tool, library, plugin, MCP server, skill, font, asset, host, design style or workflow; when starting a project; and at the end of any task that used a tool or method not yet in the library, to file it back. Also use it whenever the user mentions their library, playbook or "منابع".
---

> **Public read-only copy** (https://github.com/nexorahai-svg/claude-knowledge-library): update it with `git -C <library> pull`, not sync.py; nothing can be filed back, so skip section 3 and the sync steps; projects/ (the owner's profile and project log) is not included. Reply in the user's own language.

# Knowledge library

The library is a git repository, shared across the user's computers through the private
GitHub repository `nexorahai-svg/claude-knowledge-library`. Its usual local path is
`~/Desktop/knowledge-library/` (on the main Linux machine `~/Desktop/knowledge-library/`).
It is written in Persian; prompts inside it are in English. Reply in the language the user chose (Claude Code `language` setting; ask if none).

## 0. Sync first and last (every session, every machine)

1. Find the local copy: usually `~/Desktop/knowledge-library`. The user may also introduce a
   copy at another path (for example an old copy inside a project); use that one.
   If no copy exists on this machine, tell the user and, only with their OK, clone it:
   `git clone https://github.com/nexorahai-svg/claude-knowledge-library.git ~/Desktop/knowledge-library`
2. **Start of the task:** run `python3 <library>/scripts/sync.py`. It works for every kind of copy:
   - a clone: commits pending library changes (after `build_all.py` passes), pulls newer work
     from GitHub and pushes local work, rebuilding generated files on conflict;
   - an old copy with `.git` but no remote: adds the GitHub remote and catches up the same way,
     without overwriting newer work;
   - a plain copy without `.git`: changes nothing, makes a fresh clone next to it and saves the
     copy's differing files under `research/inbox/sync-from-copy-<date>/` for review. Tell the user
     and continue in the fresh clone.
   If it stops on a conflict in a hand-written file, merge both sides by hand (never drop the
   other machine's findings), commit, and run it again.
3. **End of the task, after filing back:** run `python3 <library>/scripts/sync.py` again so the
   new findings reach GitHub and the other machines.
4. Paths inside library documents that start with `~/Desktop/knowledge-library`
   mean "the local library copy" on other machines.

## 0.05 Rule: setup is Claude's job (every topic, every project)

The user does not want setup chores. Whatever Claude can do itself (install, enable, disable, configure) it does after one short yes from the user, not as a list of commands. Only steps Claude truly cannot do (sudo password, browser sign-in/OAuth, clicks on claude.ai or other websites, licence acceptance) go to the user: the exact command in its own bash block or the exact menu path, in order, each with a one-line reason. Every topic, every project.
Explain reasons in the user's language. Machine setup has one entry point: `python3 <library>/scripts/setup_machine.py --apply`
(the SessionStart hook says when this machine differs from the plan). If a safety check blocks a step, say so plainly
and give the user that one command instead of looking for a way around it.

## 0.1 What runs by itself (plugin hooks and timers)

- **Session start (hook):** fetches GitHub in the background and fast-forwards a clean copy; adds a status line
  to your context (last daily watch, last weekly sweep, unreviewed inbox, due cards). If it says an automatic run
  is overdue, tell the user in one line and offer `python3 scripts/run_routine.py status`.
- **Stop (hook):** if the session installed or cloned something and never touched the library, you get one
  reminder to file findings back (section 3). Do it, or say in one line that nothing is new.
- **Daily watch and weekly sweep:** systemd user timers run `scripts/run_routine.py` (prompts in
  `research/routines/`), daily 10:00 and Monday 11:00 Dubai time, with a desktop alert on failure. They need no
  open Claude app. A cloud routine may run the same prompt; the runner skips work already done.
- **Agents:** `kl-researcher` (read-only research), `kl-verifier` (checks claims at the primary source),
  `kl-curator` (files verified findings). **Commands:** `/kl-add <links>`, `/kl-review` (weekly inbox),
  `/kl-status` (automation health).

## 0.5 Quick routes (after sync)

Read `projects/user-profile.md` first (the user's design taste, budget rules and tool guards),
then go straight to the file for the task:

| The user wants… | Open |
|---|---|
| to build an app (any kind; Android, iOS, desktop) | `playbooks/mobile-app.md` or `desktop-app.md`; design phase 1.5 uses `domains/apps/app-design-system.md`, `app-styles.md`, `app-screen-patterns.md`; code starts from `starters/flutter-app/` |
| a website, store, dashboard, local-business app, brand, social content, AI feature | the matching file in `playbooks/` (router: `playbooks/README.md`) |
| you to check a post, reel, link or tool they sent | `python3 scripts/fetch_post.py <urls> --out <scratch>` then `research/x-research-plan.md` |
| this machine set up like the main one | `python3 scripts/setup_machine.py` (report), `--apply` to install; sudo steps are printed for the user |
| to know if tools are current or ready for a better verdict | `python3 scripts/check_updates.py` (or `--promotions`, offline) |
| which plugins, connectors or Claude features to turn on (start of every project) | `domains/claude-code/claude-toolkit.md`: always-on set, per-project-type table, what to keep off |
| a source by ID (S12) | `sources/S12.md` |
| to know if the automatic runs work, or to install them on this machine | `python3 scripts/run_routine.py status` / `install` |

New sources go in `sources/S<next>.md` and changelog rows in `changes/<date>-<HHMMSS>00-<host>.txt`;
`sources/README.md` and `CHANGELOG.md` are generated (sync renumbers a clashing source ID by itself).

## 1. Before choosing anything: the playbook is your teacher

1. Read `llms.txt` first: a short router (about 3 KB). The full list of every document and tool
   is `llms-full.txt`; open it only when you need to search the whole library. Its first section lists the **project
   playbooks** (`playbooks/`). Classify the project with the router in `playbooks/README.md`
   (business website, online store, web app/dashboard, mobile app, desktop app, local business
   app, social content, brand identity, AI feature/agent) and open that playbook.
2. Follow the playbook phase by phase: ask only its "before you start" questions whose answers
   you do not already have, show the default stack with verdicts and get approval, read each
   phase's linked section before doing it, and never call a phase done until its "done" gate
   passes. When the playbook does not cover a situation, use its "why this order" reasoning,
   then file the new situation back. If no playbook fits, say so and use the domain documents.
3. Open `README.md`, `catalog/README.md` or `catalog/index.json` only if you need more.
4. Read the cards and the matching `domains/<domain>/` documents for the task.
5. Respect the verdict: adopt (✅ use) · trial (🧪 small test first) · assess (👀 not
   recommended yet) · hold (⛔ do not use; tell the user why). A `status: queued` card is not
   a recommendation.
6. Prefer the newest stable version of an adopted tool. If a card's `next_check` date has
   passed, or a newer version or a better tool may exist, re-check it against the primary
   source before relying on it, and update the card.
7. Only research from scratch for what the library does not cover.

## 2. While working

Aim for the best result the current tools allow: use the library's verification stack
(`domains/claude-code/verification.md`), its cost guide, and its safety rules. Set up the
automated checks in the first working session, before features, not at the end. Use the
built-in browser rather than the user's logged-in Chrome, and leave payment, billing,
account and verification steps to the user. Never copy
other people's designs, prompts or code; use only assets with a clear license. Do not
install third-party plugins, hooks, MCP servers or skills without the user's request and a
read of their files.

## 3. Filing back (required)

At the end of a task, if the project discovered anything genuinely new, or found the library
wrong — a new tool, plugin, MCP server, skill or agent; a newer version; a license or
price change; a method that worked; a tool that failed — add it to the library in the same
session:

1. Work in `~/Desktop/knowledge-library/` and follow its `CLAUDE.md`
   (verify against the primary source, confidence labels, card or domain document, source
   entry, `CHANGELOG.md`), then run `python3 scripts/build_all.py`, which rebuilds the
   catalog, `llms.txt`, the dashboard and runs all checks; it must pass.
2. Record the project's real-world experience in `projects/README.md` (which cards it used,
   what worked, what did not); a tool that worked in a real project earns the 🔬 label. Real
   use can raise or lower a verdict. Routine use of an existing card needs only that row.
3. Commit in the library repository with a message that names the project. Keep library
   commits separate from the project's own commits.
4. Tell the user in one or two sentences in the user's language what was added. If something could not be
   verified, file it as ❓ in `research/inbox/` instead of a card.
