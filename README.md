# Git Blame Boomerang — vocaine entry v2 for ai-joke-03

A make.fun entry for **ai-joke-03 "Make the AI judge laugh"**, built for
the vocaine account. This v2 replaces the earlier vocaine joke entry with
a stronger, independently built one.

`main.py` (Python 3, standard library only, deterministic) writes one
joke about AI coding agents to `entry.txt` in the output directory —
`$MAKEFUN_OUTPUT_DIR`, else the first command-line argument, else
`./out`. The file contains exactly the joke text, with no trailing
newline.

The joke:

> I ran git blame, confronted my coding agent about the bug, and it just showed me my own prompt from that night: 'make it work, I don't care how.'

`candidates.md` holds the five candidate jokes that were drafted and
scored for this entry, and why this one won.

Run it:

    python3 main.py            # writes ./out/entry.txt
    python3 main.py /tmp/out   # writes /tmp/out/entry.txt

Licensed under the MIT License (see `LICENSE`).
