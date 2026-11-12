import os

# Copy the summary held beside this file to the output directory, byte for
# byte, so every run writes identical output. No network, no randomness.
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "summary.txt"), "rb") as f:
    data = f.read()

outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "entry.txt"), "wb") as f:
    f.write(data)
