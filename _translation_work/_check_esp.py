# -*- coding: utf-8 -*-
import glob
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SM = r"C:\Program Files (x86)\Steam\steamapps\common\Slay the Spire 2\mods"
spec = importlib.util.spec_from_file_location(
    "pt", os.path.join(ROOT, "_translation_work", "pck_tool.py")
)
pt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pt)


def langs(pck):
    with open(pck, "rb") as f:
        ents, _ = pt.read_dir(f)
    ls = set()
    for e in ents:
        p = e["path"].replace("\\", "/")
        if "/localization/" in p and p.endswith(".json"):
            ls.add(p.split("/localization/")[1].split("/")[0])
    return sorted(ls)


def out(s):
    sys.stdout.buffer.write((str(s) + "\n").encode("utf-8"))


for d in sorted(os.listdir(SM)):
    pcks = glob.glob(os.path.join(SM, d, "*.pck"))
    if not pcks:
        continue
    p = pcks[0]
    l = langs(p)
    flag = "OK" if "esp" in l else "SIN-ESP"
    out(f"{flag:8} {d:30} {l}")
