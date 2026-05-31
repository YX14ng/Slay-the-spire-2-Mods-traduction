# -*- coding: utf-8 -*-
import struct, os, sys, glob, re, json, hashlib
PEND = r"f:/Programs/Slay-the-spire-2-Mods-traduction/Por_traducir"
WORK = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/pendientes"
BASE = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/basegame/localization"
os.makedirs(WORK, exist_ok=True)

# memoria de traduccion oficial del juego base eng->esp
mem = {}
for p in glob.glob(f"{BASE}/eng/*.json"):
    fn = os.path.basename(p); sp = f"{BASE}/esp/{fn}"
    if not os.path.exists(sp): continue
    e = json.load(open(p, encoding="utf-8-sig")); s = json.load(open(sp, encoding="utf-8-sig"))
    for k, v in e.items():
        if isinstance(v, str) and k in s and isinstance(s[k], str): mem.setdefault(v.strip(), s[k])

def read_pck(path):
    f = open(path, "rb")
    if f.read(4) != b"GDPC": return None, None
    struct.unpack("<5I", f.read(20)); fb = struct.unpack("<Q", f.read(8))[0]; do = struct.unpack("<Q", f.read(8))[0]
    f.seek(do); n = struct.unpack("<I", f.read(4))[0]; ent = []
    for _ in range(n):
        pl = struct.unpack("<I", f.read(4))[0]; p = f.read(pl).rstrip(b"\x00").decode("utf-8", "replace")
        off, sz = struct.unpack("<QQ", f.read(16)); f.read(20); ent.append((p, off + fb, sz))
    return f, ent

PRI = ["eng", "zhs", "jpn", "kor"]
manifest = {}
for d in sorted(os.listdir(PEND)):
    dp = os.path.join(PEND, d)
    if not os.path.isdir(dp): continue
    pcks = glob.glob(os.path.join(dp, "*.pck"))
    if not pcks: continue
    f, ent = read_pck(pcks[0])
    if ent is None: continue
    # agrupar por lang, capturar prefijo interno
    bylang = {}; prefix = None
    for p, off, sz in ent:
        m = re.search(r'^(.*/localization/)([a-z]{2,4})/(.+\.json)$', p)
        if m:
            bylang.setdefault(m.group(2), []).append((m.group(3), off, sz))
            prefix = m.group(1)
    if not bylang: f.close(); continue
    src = next((l for l in PRI if l in bylang), None)
    if not src: f.close(); continue
    srcdir = os.path.join(WORK, d, "src"); espdir = os.path.join(WORK, d, "esp")
    os.makedirs(srcdir, exist_ok=True); os.makedirs(espdir, exist_ok=True)
    filled = total = 0
    for fname, off, sz in bylang[src]:
        f.seek(off); data = f.read(sz)
        open(os.path.join(srcdir, fname), "wb").write(data)
        try: d2 = json.loads(data)
        except: d2 = {}
        out = {}
        for k, v in d2.items():
            if isinstance(v, str):
                total += 1
                if v.strip() in mem: out[k] = mem[v.strip()]; filled += 1
                else: out[k] = v
            else: out[k] = v
        json.dump(out, open(os.path.join(espdir, fname), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    f.close()
    manifest[d] = {"pck": os.path.basename(pcks[0]), "prefix": prefix, "src": src,
                   "langs": sorted(bylang.keys()), "total": total, "auto": filled}
    print(f"{d:30} src={src} prefix={prefix} auto={filled}/{total}")
json.dump(manifest, open(os.path.join(WORK, "_manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("\nmanifest -> _translation_work/pendientes/_manifest.json")
