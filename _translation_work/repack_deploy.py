# -*- coding: utf-8 -*-
# Reempaca mods de Por_traducir agregando esp (y zhs si existe), los coloca en Traducidos/ y despliega a Steam.
# Uso: python repack_deploy.py Mod1 Mod2 ...
import json, os, sys, shutil, subprocess, struct, hashlib, glob
ROOT = r"f:/Programs/Slay-the-spire-2-Mods-traduction"
PEND = os.path.join(ROOT, "Por_traducir")
WORK = os.path.join(ROOT, "_translation_work", "pendientes")
TRAD = os.path.join(ROOT, "Traducidos")
STEAM = r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
TOOL = os.path.join(ROOT, "_translation_work", "pck_tool.py")
man = json.load(open(os.path.join(WORK, "_manifest.json"), encoding="utf-8"))

def verify(pck):
    f=open(pck,"rb"); f.read(4); struct.unpack("<5I",f.read(20)); fb=struct.unpack("<Q",f.read(8))[0]; do=struct.unpack("<Q",f.read(8))[0]
    f.seek(do); n=struct.unpack("<I",f.read(4))[0]; bad=0; esp=0; zhs=0
    for _ in range(n):
        pl=struct.unpack("<I",f.read(4))[0]; p=f.read(pl).rstrip(b"\x00").decode("utf-8","replace"); off,sz=struct.unpack("<QQ",f.read(16)); md5=f.read(16); struct.unpack("<I",f.read(4))
        cur=f.tell(); f.seek(off+fb); d=f.read(sz); f.seek(cur)
        if hashlib.md5(d).digest()!=md5: bad+=1
        if "/localization/esp/" in p: esp+=1
        if "/localization/zhs/" in p: zhs+=1
    f.close(); return n,bad,esp,zhs

for mod in sys.argv[1:]:
    info = man[mod]; prefix = info["prefix"]; pckname = info["pck"]
    addroot = os.path.join(WORK, mod, "add")
    if os.path.exists(addroot): shutil.rmtree(addroot)
    # construir add/<prefix>esp y <prefix>zhs
    for lang in ("esp","zhs"):
        srcl = os.path.join(WORK, mod, lang)
        if os.path.isdir(srcl):
            dst = os.path.join(addroot, prefix + lang)
            os.makedirs(dst, exist_ok=True)
            for fn in os.listdir(srcl):
                shutil.copy(os.path.join(srcl, fn), os.path.join(dst, fn))
    srcpck = os.path.join(PEND, mod, pckname)
    tmppck = os.path.join(WORK, mod, pckname)
    subprocess.run([sys.executable, TOOL, "repack", srcpck, tmppck, addroot], check=True, capture_output=True)
    n,bad,esp,zhs = verify(tmppck)
    # colocar en Traducidos/<mod>/ (copiar carpeta completa de Por_traducir, luego pck nuevo)
    tdst = os.path.join(TRAD, mod)
    if os.path.exists(tdst): shutil.rmtree(tdst)
    shutil.copytree(os.path.join(PEND, mod), tdst)
    shutil.copy(tmppck, os.path.join(tdst, pckname))
    # deploy a Steam
    sdst = os.path.join(STEAM, mod, pckname)
    if os.path.isdir(os.path.dirname(sdst)): shutil.copy(tmppck, sdst)
    sys.stdout.buffer.write((f"{mod:24} archivos={n} md5OK={n-bad}/{n} esp={esp} zhs={zhs} -> Traducidos/ + Steam\n").encode())
print("OK")
