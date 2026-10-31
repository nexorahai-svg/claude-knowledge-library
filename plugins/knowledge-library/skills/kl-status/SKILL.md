---
name: kl-status
description: Show the health of the knowledge library and its automation (last daily watch and weekly sweep, timers, failures, unreviewed inbox, due cards). Use when the user asks if the library's timer, sweep or automatic runs are working.
---

# Library status

Run `python3 ~/Desktop/knowledge-library/scripts/run_routine.py status` and report its result to the user in Persian:
last run of each routine and whether it succeeded, next scheduled run, unreviewed inbox files, cards past next_check.
If a run failed, read the end of its log under `~/.local/state/knowledge-library/` and explain the cause in one line.
If the timers are not installed, offer `python3 scripts/run_routine.py install`.
