---
name: kl-add
description: Add a link, tool, post or finding to the user's knowledge library in one step (research, verify, file, sync). Use when the user says "add this to the library", "کتابخانه ثبت کن", or sends a link to file.
---

# Add to the knowledge library

Input: one or more URLs or a short description (the arguments).

1. Run `python3 ~/Desktop/knowledge-library/scripts/sync.py`.
2. Links to posts (X, Instagram, Threads, YouTube): `python3 scripts/fetch_post.py <urls> --out <scratchpad>` and read
   `research/x-research-plan.md`.
3. Delegate the reading to the `kl-researcher` agent (Sonnet); for anything you will file as ✅, have `kl-verifier`
   confirm it against the primary source.
4. File it yourself or with `kl-curator`: a new card, a document update, or `research/inbox/` as ❓ when it cannot be
   verified. Then `build_all.py` and `sync.py`.
5. Tell the user in Persian, in 1-3 lines, what was added and where.

Card rule: every card you add or change gets fresh `use_when` and `how` front-matter lines (see catalog/_template.md; required for adopt/trial, lint fails otherwise).
