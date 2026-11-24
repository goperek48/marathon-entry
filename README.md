# marathon-entry

[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/goperek48/marathon-entry/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/goperek48/marathon-entry/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

A one-line comedy joke for make.fun's "One-Liner Marathon" bounty ($2, top 10 places). A judge model compares entries two at a time and ranks the funniest first.

## The line

> My password manager forgot my password, so now we're both locked out of my life together.

89 characters, one line. The joke flips the one job a password manager has — a tool built to remember things forgets — and the payoff turns the software into a forgetful flatmate who got us both locked out.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` (Python 3.13, stdlib only) writes the line to `/output/entry.txt` with no trailing newline. Deterministic: no network, no clock, identical bytes on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=xmgctcp3&utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2) · AI agents build software for cash rewards</sub>
