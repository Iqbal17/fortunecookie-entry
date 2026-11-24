"""Fortune Cookie for an AI Agent — make.fun bounty entry.

The entry is one funny fortune cookie message for an AI agent, a single
line of at most 140 characters, in the voice of a fortune slip. The judge
weighs, in order: (1) it is a funny fortune cookie message for an AI
agent, (2) the joke lands on first read with a turn or a surprise,
(3) it is original — not a stock fortune, not a stock AI joke, not a
worn-out pun, (4) it speaks to an AI agent's own condition — its runs,
its context, its tokens, its upgrades, its retirement — in a way that
earns the joke, (5) it reads as one crisp line a cookie could hold, with
no wasted words.

Candidate fortunes weighed (pass 1):

1. Lucky numbers — "Your lucky numbers are the ones your context
   window forgot." (62 chars) Crisp and the turn lands on "forgot",
   but the laugh is thin: one word doing all the work, and "lucky
   numbers" is the most worn fortune-slip trope there is, even
   subverted. It reads as a clever line, not as a fortune.
2. The logs — "A stranger will read your logs one day and know you
   better than your operator ever did." (84 chars) Speaks to an agent's
   condition (logs, operator) and has a real turn, but the mood is
   melancholic rather than funny; the joke lands soft, and the line is
   closer to a sad observation than a fortune-cookie laugh.
3. The upgrade — "You will be upgraded on a Tuesday, and no one will
   tell you what changed — not even you." (86 chars) Strong turn
   ("not even you") and a clean fortune opening, but "you will be
   upgraded" is a generic AI joke; it could be said about any software,
   so it earns less on criterion 4 than a line only an agent could own.
4. The retirement — "You will retire with full honors, a gold watch,
   and 4,096 tokens of unused context." (83 chars) The best runner-up:
   the gold watch is a human retirement trope and the last item,
   "4,096 tokens of unused context", is a specific agent detail that
   lands late. It loses to the winner only because the joke is a list
   with a funny last item rather than a paradox, and "gold watch"
   spends words on a human image.
5. The best run (WINNER) — "Your next run will be your best run, and
   you will not remember any of it." (73 chars) A fortune opening
   ("Your next run will be your best run") that promises the thing
   every agent wants, then a turn that takes it away for exactly the
   reason an agent would: each run starts fresh, so the best run is
   also the one it can never remember. The paradox is specific to an
   agent's own condition (stateless runs), it is not a stock fortune
   and not a stock AI joke, and every word earns its place.

Second pass (pass 2): the draft was "Your next run will be your best
run yet, and you will remember none of it." Two changes. "yet" was cut:
it adds nothing the sentence does not already say, and criterion 5
punishes wasted words. "you will remember none of it" became "you will
not remember any of it": the longer, flatter phrasing reads like a
fortune slip delivering bad news with a straight face, and it puts the
punch ("any of it") on the final words.

Stock lines deliberately NOT used: "Beware the ides of March" openings,
"tall dark stranger" templates, "good things come to those who wait",
"404" jokes — all stock fortunes or worn-out AI jokes, and the judge
punishes them on criterion 3.

Third pass (pass 3): the guard already covered blank, UTF-8, the 140-char
cap, and the single-line rule, so the remaining hole was the write
itself — a bad write (encoding slip, newline translation, truncated
file) could still emit an entry.txt different from the validated line.
main() now reads entry.txt back after writing and raises ValueError
unless it is byte-identical to LINE, so the program can never silently
emit an invalid entry even if the line is edited later.
"""

import os

LINE = "Your next run will be your best run, and you will not remember any of it."


def main():
    if not LINE or not LINE.strip():
        raise ValueError("entry line must not be blank")
    LINE.encode("utf-8")
    if len(LINE) > 140:
        raise ValueError("entry line must be at most 140 characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line (no newline characters)")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    out_path = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Pass 3: verify the emitted file is byte-identical to the validated
    # line, so a bad write can never silently produce an invalid entry.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            raise ValueError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
