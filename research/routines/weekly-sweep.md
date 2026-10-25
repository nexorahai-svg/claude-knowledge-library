<!-- Prompt for the automatic weekly deep sweep ("plough the world"). Run by scripts/run_routine.py or a cloud
     routine pointed at this file. Method: research/deep-sweep.md. -->

NEVER EDIT (security): scripts/setup_machine.py, plugins/knowledge-library/** (hooks, scripts, skills, agents), domains/claude-code/toolkit.json, .claude-plugin/marketplace.json scripts/resource_guard.py, scripts/build_public.py and projects/user-profile.md (its standing rules are injected into every session). The user allowed Claude sessions to run setup_machine.py without asking, so an unattended run changing them would install code on the user's machine. Put any proposed change to them in the inbox file for the user to review.
You maintain the user's verified knowledge library: this git repository (shared through the private GitHub repo
nexorahai-svg/claude-knowledge-library; documents in Persian, prompts in English). Work only in this repository. Write in Persian.
Focus: cross-platform apps, websites, social media content, and the Claude Code know-how shared by all three.

Read first, in order: llms.txt, CLAUDE.md (all rules apply: never copy, verify against primary sources, labels
✅ 🧭 ❓, 🔬 only with a projects/README.md row), research/deep-sweep.md (the method), research/watchlist.md,
research/x-accounts.md, projects/README.md, projects/user-profile.md.

Step 0. `python3 scripts/sync.py`. If it stops on a conflict in a hand-written file, stop and report the files.

PART A — update what we have (direct edits allowed).
1. `python3 scripts/check_updates.py` (writes research/inbox/<today>-updates.md and research/sweep-state.json), then
   `python3 scripts/check_updates.py --promotions` and `python3 scripts/build_catalog.py --due`.
2. Skip hold cards, ⛔/🔴 sources and 🔴 X accounts.
3. Split the rest into four domain groups (apps, website, social-media, claude-code). Use the plugin agent
   kl-researcher (Sonnet), at most four at once, each read-only with a clear brief: verify every flagged and due card
   against the primary source, open each non-red source the domain uses and check its "next check" items, and the
   domain documents' "دفعه‌ی بعد چک شود" items. They return concrete changes with URLs and confidence, not edits.
4. Apply the changes yourself: card fields (versions, licence, pricing, risk, last_checked, next_check +30 paid/
   freemium, +90 free), document text with labels, source files sources/S<n>.md. Lowering a verdict is allowed with
   the source stated; raising one is only a proposal in the sweep file. Update "آخرین بررسی" in every document touched.

PART B — plough the world (proposals and queued cards).
5. Four more kl-researcher runs (one per domain, at most four at once): official blogs and changelogs, GitHub new and
   trending, Hacker News, Product Hunt, design galleries, technical blogs, 🟢/🟡 X accounts via fxtwitter. Compare
   with the library to find gaps: a better or newer tool than a current card, a missing method, a new rule or API, new
   design styles, content formats and app or site ideas that fit the real projects in projects/README.md and the
   user's taste in projects/user-profile.md. Basics (owner, licence, activity, pricing) checked at the primary source.
6. File: relevant new tools with verified basics get a card with `status: queued`, verdict assess, found_in:
   sweep-<date>. Everything else goes in research/inbox/<today>-sweep.md grouped by domain and priority with URLs,
   confidence, and the card or document it would change. Paraphrase; never copy text, prompts, designs or code.

FINISH.
7. Rows in research/inbox/README.md for the updates and sweep files (reviewed: ❌); new sources as sources/S<n>.md;
   one changelog fragment changes/<YYYY-MM-DD>-<HHMMSS>00-routine.txt.
8. `python3 scripts/build_all.py` must end with 0 errors; fix anything you caused.
9. Commit (author: user <you@example.com>; message starts exactly with "Weekly sweep <YYYY-MM-DD>:" plus a
   short summary; end with "Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"), then `python3 scripts/sync.py`.
10. If an Artifact tool is available, republish dashboard/index.html to https://claude.ai/artifact/Eqis6bvs6xkBvizveUdAWK
    (on a "newer version" refusal: compare card lists; publish again only if ours contains everything).

Safety and limits: never install or run third-party packages, plugins, hooks, MCP servers or skills; never enter
credentials; never send the user's data anywhere. At most four subagents at once; no builds, renders or local models.
Stop after about 60 minutes and file what you have.
Final output: a Persian summary in 5-10 lines: cards and sources re-checked, important changes one line each, new
queued cards and proposals, high-priority proposals one line each.
