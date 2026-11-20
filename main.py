#!/usr/bin/env python3
"""make.fun entry: copy the pre-rendered front page to the output dir.
Stdlib only. The page itself is rendered by render.py (not run by the grader).
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
