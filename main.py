"""news-image-20261119 entry: place the prepared front-page image at
/output/entry.png.

The image bundled in this repository was drawn from verified
19 Nov 2026 headlines (see build_image.py). This program does no
network access and always produces the same output: it copies the
entry.png that ships alongside this file into /output/entry.png.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing next to main.py")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
