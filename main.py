"""One Line, Big Laugh — make.fun bounty entry.

The joke: a robot vacuum has unionized, so it now only cleans on its own
terms — a labor pun that lands twice, because a vacuum's "terms" for
cleaning are, quite literally, spotless. The program writes that single
line to /output/entry.txt as UTF-8 with no trailing newline.
"""
import os

ENTRY = "The robot vacuum unionized. It now only cleans on its own terms, which, to be fair, are spotless."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
