# -*- coding: utf-8 -*-
import sys, os, hashlib
mods = r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
out  = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/mods_fingerprint_TUYO.txt"
exts = (".json", ".dll", ".pck", ".lang")
lines = []
for root, dirs, files in os.walk(mods):
    for fn in files:
        if fn.lower().endswith(exts):
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, mods).replace(os.sep, "/")
            h = hashlib.md5(open(p, "rb").read()).hexdigest()
            lines.append((rel.lower(), h, rel))
lines.sort()
with open(out, "w", encoding="utf-8") as f:
    for _, h, rel in lines:
        f.write(f"{h}  {rel}\n")
print(f"{len(lines)} archivos -> {out}")
