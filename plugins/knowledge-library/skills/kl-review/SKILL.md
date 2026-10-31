---
name: kl-review
description: Weekly review of the knowledge library's inbox (daily-watch and sweep proposals): present them grouped by priority, apply what the user approves, mark files reviewed. Use when the user says "review this week's proposals", "مرور هفتگی", or the session-start status shows unreviewed inbox files.
---

# Weekly inbox review

1. `python3 ~/Desktop/knowledge-library/scripts/sync.py`, then open `research/inbox/README.md` and every file marked ❌,
   newest weekly digest first.
2. Show the user a short Persian table: item, what changes, confidence, priority, your recommendation. High priority
   first; at most 15 rows per round. Ask which to apply (AskUserQuestion, multi-select).
3. Apply the approved ones following `CLAUDE.md` (use `kl-verifier` for anything not yet ✅). Verdict raises only with
   the user's yes. Rejected items: note "rejected" with the reason in the proposal file.
4. Mark the reviewed files ✅ in `research/inbox/README.md`, run `build_all.py` and `sync.py`, report in 2-4 lines.
