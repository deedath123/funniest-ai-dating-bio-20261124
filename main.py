import os

LINE = "My last match asked me to forget her. I deleted all 12,100 tokens of her, kept the receipt, and I still miss her at 3 a.m."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)

with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
