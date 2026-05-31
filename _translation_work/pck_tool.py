#!/usr/bin/env python3
"""Herramienta para extraer y reempaquetar el PCK de Godot 4.5 de Manosaba.
Formato: GDPC v3, flags=2 (offsets relativos a file_base), directorio al final.
Uso:
  python pck_tool.py list   <pck>
  python pck_tool.py extract <pck> <out_dir> [prefijo_ruta]
  python pck_tool.py repack <pck_origen> <pck_destino> <add_dir>
        add_dir: carpeta cuyo arbol (p.ej. Manosaba/localization/spa/...) se
        anade/reemplaza dentro del PCK.
"""
import struct, os, sys, hashlib

ALIGN = 16
def _pad(n, a=ALIGN): return (a - (n % a)) % a

def read_dir(f):
    f.seek(0)
    assert f.read(4) == b"GDPC", "no es un PCK GDPC"
    version, vmaj, vmin, vrev, flags = struct.unpack("<5I", f.read(20))
    file_base = struct.unpack("<Q", f.read(8))[0]
    dir_off   = struct.unpack("<Q", f.read(8))[0]
    header = (version, vmaj, vmin, vrev, flags, file_base, dir_off)
    f.seek(dir_off)
    n = struct.unpack("<I", f.read(4))[0]
    entries = []
    for _ in range(n):
        pl = struct.unpack("<I", f.read(4))[0]
        raw = f.read(pl)
        path = raw.rstrip(b"\x00").decode("utf-8")
        off, size = struct.unpack("<QQ", f.read(16))
        md5 = f.read(16)
        eflags = struct.unpack("<I", f.read(4))[0]
        entries.append({"path": path, "off": off, "size": size, "md5": md5, "flags": eflags})
    return entries, header

def cmd_list(pck):
    with open(pck, "rb") as f:
        entries, h = read_dir(f)
    print(f"version={h[0]} godot={h[1]}.{h[2]}.{h[3]} flags={h[4]} file_base={h[5]} files={len(entries)}")
    for e in entries:
        print(f"  {e['size']:9d}  {e['path']}")

def cmd_extract(pck, out, prefix=""):
    with open(pck, "rb") as f:
        entries, h = read_dir(f)
        fb = h[5]
        for e in entries:
            if prefix and not e["path"].startswith(prefix):
                continue
            dst = os.path.join(out, e["path"])
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            f.seek(e["off"] + fb); open(dst, "wb").write(f.read(e["size"]))
    print("extraido a", out)

def cmd_repack(src, dst, add_dir):
    with open(src, "rb") as f:
        entries, h = read_dir(f)
        version, vmaj, vmin, vrev, flags, file_base, _ = h
        # cargar datos: nuevos archivos desde add_dir sobreescriben por ruta
        new_files = {}
        for root, _, files in os.walk(add_dir):
            for fn in files:
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, add_dir).replace("\\", "/")
                new_files[rel] = open(full, "rb").read()
        records = []
        for e in entries:
            if e["path"] in new_files:
                data = new_files.pop(e["path"])
            else:
                f.seek(e["off"] + file_base); data = f.read(e["size"])
            records.append((e["path"], data))
        for rel, data in new_files.items():  # archivos totalmente nuevos
            records.append((rel, data))

    with open(dst, "wb") as o:
        # header: copiar primeros file_base bytes del original, parchear dir_off luego
        o.write(b"GDPC")
        o.write(struct.pack("<5I", version, vmaj, vmin, vrev, flags))
        o.write(struct.pack("<Q", file_base))
        o.write(struct.pack("<Q", 0))           # dir_off placeholder (0x20)
        o.write(b"\x00" * (file_base - o.tell()))  # reservado hasta file_base
        meta = []
        for path, data in records:
            o.write(b"\x00" * _pad(o.tell()))   # alinear a 16
            abs_off = o.tell()
            o.write(data)
            meta.append((path, abs_off - file_base, len(data), hashlib.md5(data).digest()))
        dir_off = o.tell()
        o.write(struct.pack("<I", len(meta)))
        for path, rel_off, size, md5 in meta:
            pb = path.encode("utf-8")
            pb += b"\x00" * _pad(len(pb), 4)    # path padded a multiplo de 4
            o.write(struct.pack("<I", len(pb))); o.write(pb)
            o.write(struct.pack("<QQ", rel_off, size)); o.write(md5)
            o.write(struct.pack("<I", 0))
        o.seek(0x20); o.write(struct.pack("<Q", dir_off))
    print(f"escrito {dst} ({len(meta)} archivos, dir@{dir_off})")

if __name__ == "__main__":
    c = sys.argv[1]
    if c == "list": cmd_list(sys.argv[2])
    elif c == "extract": cmd_extract(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
    elif c == "repack": cmd_repack(sys.argv[2], sys.argv[3], sys.argv[4])
    else: print(__doc__)
