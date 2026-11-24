# marathon-entry — a one-line joke for make.fun's One-Liner Marathon.
#
# The whole job of this script is to put one joke into /output/entry.txt.
# The sealed gate accepts UTF-8 text between 1 and 280 characters that is
# more than blank space, so the entry is a single short line, written with
# no newline at the end. The program is deterministic: it touches no
# network, reads no clock, imports nothing beyond the standard library, and
# produces identical bytes on every run under Python 3.13.
#
# The joke works by flipping the one job a password manager has. A tool
# built to remember things is the last thing you expect to forget, so the
# setup earns its laugh from that reversal, and the payoff leans into it:
# "we're both locked out" turns the software into a forgetful flatmate who
# got us both stranded. That shared lockout is the line's personality —
# without it the joke would be a flat complaint about apps. It reads clean
# the first time and survives a second read because the contradiction at
# its centre (the rememberer forgetting) is the joke, not a trick word.
#
# Chosen line (89 characters):
#   My password manager forgot my password, so now we're both locked out of my life together.

from pathlib import Path

LINE = "My password manager forgot my password, so now we're both locked out of my life together."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # The file holds the joke alone — no extra newline, no extra text —
    # so the gate measures exactly the line above.
    out.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
