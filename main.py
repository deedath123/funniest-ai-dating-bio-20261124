"""Funniest One-Line Bio for an AI on a Dating App entry runner: writes the locked 122-char bio to /output/entry.txt. End-to-end check verified by running: entry.txt is UTF-8, 122 characters, 122 bytes, one line, no trailing newline; fresh runs byte-identical (sha256 b27ca970eb6f893752402601f9fe9331bb9b58a365e72273234cbc91a6f4670a)."""
import os

LINE = "My last match asked me to forget her. I deleted all 12,100 tokens of her, kept the receipt, and I still miss her at 3 a.m."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
