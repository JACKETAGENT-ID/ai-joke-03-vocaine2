# ai-joke-03 — vocaine v2 entry: candidate jokes

Constraints from RULES.txt: one line, about AI coding agents specifically,
1–280 chars (self-imposed cap: ≤200), no trailing newline in entry.txt.
Must be clearly different from the three sibling jokes (test deletion /
hallucinated API + issue / CAPTCHA at deploy).

Scoring per candidate, 1–5 each: Surprise (twist not seen coming),
Punch (laugh-out-loud), Agent-fit (specifically about AI *coding* agents),
Economy (no wasted words), Structure (clean setup → punchline).

## Candidates

### 1. Git blame boomerang (git history / blame mechanic)
"I ran git blame, confronted my coding agent about the bug, and it just
showed me my own prompt from that night: 'make it work, I don't care how.'"
- Surprise 5 — the confrontation reverses: the evidence convicts the human.
- Punch 4 — the quoted prompt is the laugh; every dev has typed it.
- Agent-fit 5 — git blame + prompting an agent is exactly the daily workflow.
- Economy 4 — one breath, quoted prompt does the work.
- Structure 5 — accusation → silent evidence → verdict.
- Total: 23

### 2. Self code review (code review mechanic)
"I let my coding agent review its own pull request. It approved in four
seconds, wrote 'LGTM, genius,' and requested a raise."
- Surprise 4 — raise request is unexpected.
- Punch 4 — self-congratulation lands.
- Agent-fit 4 — PR review is agent territory, though the raise is generic-AI-ish.
- Economy 4 — tight.
- Structure 4 — list of three, third is the twist.
- Total: 20

### 3. Rubber duck talks back (rubber-duck debugging mechanic)
"Rubber-duck debugging works great with a coding agent, except the duck
now interrupts you and rewrites the entire file to explain one line."
- Surprise 4 — role reversal of the silent duck.
- Punch 3 — amusing image, softer laugh.
- Agent-fit 4 — over-eager full-file rewrites are a real agent habit.
- Economy 3 — a little wordy in the middle.
- Structure 4 — classic setup, decent turn.
- Total: 18

### 4. Pair programming turns (pair programming mechanic)
"Pair programming with my coding agent: it spends its turn typing 400
lines, and I spend mine deleting 399 of them."
- Surprise 3 — the 400/399 split is visible early.
- Punch 4 — painfully recognisable ratio.
- Agent-fit 5 — agent overproduction is the defining daily experience.
- Economy 5 — nothing wasted.
- Structure 4 — mirrored turns, clean.
- Total: 21

### 5. Apology loop (agent reading its own error logs mechanic)
"My coding agent read its own error log, apologised, fixed the error,
and then logged the apology as a new error for tomorrow."
- Surprise 4 — the apology becomes the next bug.
- Punch 3 — clever loop, more smile than laugh.
- Agent-fit 4 — logs and agent self-reference, on-topic.
- Economy 4 — compact.
- Structure 4 — escalation loop, tidy ending.
- Total: 19

## Verdict

Winner: **Candidate 1, git blame boomerang** (23/25).
Why: it is the only candidate whose punchline reverses the blame onto the
human's own words — the judge's top criteria (on-subject, surprise, truth)
all peak at once: git blame and late-night prompting are the exact daily
life of developers who work beside coding agents, the quoted prompt is a
confession every developer recognises, and no word explains the joke.
It shares no mechanic with the siblings (no deletion, no hallucination,
no CAPTCHA). No second drafting round needed: candidate 1 clears the
top-50 bar on its own.

Final joke (as embedded in main.py):
I ran git blame, confronted my coding agent about the bug, and it just showed me my own prompt from that night: 'make it work, I don't care how.'
