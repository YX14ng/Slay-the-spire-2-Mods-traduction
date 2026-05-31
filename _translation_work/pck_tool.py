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

def _parse_entries(f, n):
    entries = []
    for _ in range(n):
        pl = struct.unpack("<I", f.read(4))[0]
        raw = f.read(pl)
        path = raw.rstrip(b"\x00").decode("utf-8")
        off, size = struct.unpack("<QQ", f.read(16))
        md5 = f.read(16)
        eflags = struct.unpack("<I", f.read(4))[0]
        entries.append({"path": path, "off": off, "size": size, "md5": md5, "flags": eflags})
    return entries

def read_dir(f):
    """Lee el directorio de un PCK GDPC. Autodetecta dos variantes:
    - 'tail' : el header trae dir_off en 0x20 y el directorio esta al final (mods traducidos / Manosaba).
    - 'std'  : Godot 4 estandar; directorio justo tras el header de 96 bytes, datos en file_base.
    En ambas, los datos de cada archivo estan en off + file_base.
    Devuelve (entries, header) donde header = (version,vmaj,vmin,vrev,flags,file_base,dir_off,mode).
    """
    f.seek(0, os.SEEK_END); fsize = f.tell()
    f.seek(0)
    assert f.read(4) == b"GDPC", "no es un PCK GDPC"
    version, vmaj, vmin, vrev, flags = struct.unpack("<5I", f.read(20))
    file_base = struct.unpack("<Q", f.read(8))[0]
    dir_off_cand = struct.unpack("<Q", f.read(8))[0]   # 0x20: dir_off ('tail') o reservado[0]=0 ('std')
    mode = None
    if 96 <= dir_off_cand < fsize:
        f.seek(dir_off_cand)
        try:
            n = struct.unpack("<I", f.read(4))[0]
            if 0 < n < 10_000_000:
                mode = "tail"; dir_off = dir_off_cand
        except Exception:
            pass
    if mode is None:
        mode = "std"; dir_off = 96
        f.seek(dir_off)
        n = struct.unpack("<I", f.read(4))[0]
    entries = _parse_entries(f, n)
    header = (version, vmaj, vmin, vrev, flags, file_base, dir_off, mode)
    return entries, header

def cmd_list(pck):
    with open(pck, "rb") as f:
        entries, h = read_dir(f)
    print(f"version={h[0]} godot={h[1]}.{h[2]}.{h[3]} flags={h[4]} file_base={h[5]} mode={h[7]} files={len(entries)}")
    for e in entries:
        print(f"  {e['size']:9d}  {e['path']}")

def _fsname(path):
    """Quita el esquema res:// (':' es invalido en rutas de Windows)."""
    return path[len("res://"):] if path.startswith("res://") else path

def cmd_extract(pck, out, prefix=""):
    with open(pck, "rb") as f:
        entries, h = read_dir(f)
        fb = h[5]
        for e in entries:
            if prefix and not e["path"].startswith(prefix):
                continue
            dst = os.path.join(out, _fsname(e["path"]))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            f.seek(e["off"] + fb); open(dst, "wb").write(f.read(e["size"]))
    print("extraido a", out)

def cmd_repack(src, dst, add_dir):
    with open(src, "rb") as f:
        entries, h = read_dir(f)
        version, vmaj, vmin, vrev, flags, file_base, _, mode = h
        # cargar datos: nuevos archivos desde add_dir sobreescriben por ruta
        # en modo 'std' las rutas del PCK llevan prefijo res://; los archivos nuevos
        # se extraen/staquean sin el (Windows no admite ':'), asi que lo re-anadimos.
        scheme = "res://" if (mode == "std" and entries and entries[0]["path"].startswith("res://")) else ""
        new_files = {}
        for root, _, files in os.walk(add_dir):
            for fn in files:
                full = os.path.join(root, fn)
                rel = os.path.relpath(full, add_dir).replace("\\", "/")
                if scheme and not rel.startswith("res://"):
                    rel = scheme + rel
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

    if mode == "tail":
        _write_tail(dst, records, version, vmaj, vmin, vrev, flags, file_base)
    else:
        _write_std(dst, records, version, vmaj, vmin, vrev, flags)

def _enc_path(path):
    pb = path.encode("utf-8")
    pb += b"\x00" * _pad(len(pb), 4)            # path padded a multiplo de 4
    return pb

def _write_tail(dst, records, version, vmaj, vmin, vrev, flags, file_base):
    """Formato 'tail': directorio al final, dir_off en 0x20, datos desde file_base."""
    with open(dst, "wb") as o:
        o.write(b"GDPC")
        o.write(struct.pack("<5I", version, vmaj, vmin, vrev, flags))
        o.write(struct.pack("<Q", file_base))
        o.write(struct.pack("<Q", 0))              # dir_off placeholder (0x20)
        o.write(b"\x00" * (file_base - o.tell()))  # reservado hasta file_base
        meta = []
        for path, data in records:
            o.write(b"\x00" * _pad(o.tell()))      # alinear a 16
            abs_off = o.tell()
            o.write(data)
            meta.append((path, abs_off - file_base, len(data), hashlib.md5(data).digest()))
        dir_off = o.tell()
        o.write(struct.pack("<I", len(meta)))
        for path, rel_off, size, md5 in meta:
            pb = _enc_path(path)
            o.write(struct.pack("<I", len(pb))); o.write(pb)
            o.write(struct.pack("<QQ", rel_off, size)); o.write(md5)
            o.write(struct.pack("<I", 0))
        o.seek(0x20); o.write(struct.pack("<Q", dir_off))
    print(f"escrito {dst} ({len(meta)} archivos, dir@{dir_off}, mode=tail)")

def _write_std(dst, records, version, vmaj, vmin, vrev, flags):
    """Godot 4 estandar: header 96B, directorio inmediato, datos en file_base.
    offsets relativos a file_base; cada archivo alineado a 16."""
    # paso 1: tamano del directorio y offsets relativos
    enc = [(_enc_path(p), d) for p, d in records]
    dir_size = 4 + sum(4 + len(pb) + 8 + 8 + 16 + 4 for pb, _ in enc)
    file_base = 96 + dir_size
    file_base += _pad(file_base)                   # alinear file_base a 16
    metas = []; rel = 0
    for pb, data in enc:
        metas.append((pb, rel, data, hashlib.md5(data).digest()))
        rel += len(data); rel += _pad(rel)         # siguiente archivo alineado a 16
    with open(dst, "wb") as o:
        o.write(b"GDPC")
        o.write(struct.pack("<5I", version, vmaj, vmin, vrev, flags))
        o.write(struct.pack("<Q", file_base))
        o.write(b"\x00" * 64)                       # 16 u32 reservados
        o.write(struct.pack("<I", len(metas)))      # file_count @ 96
        for pb, rel_off, data, md5 in metas:
            o.write(struct.pack("<I", len(pb))); o.write(pb)
            o.write(struct.pack("<QQ", rel_off, len(data))); o.write(md5)
            o.write(struct.pack("<I", 0))
        o.write(b"\x00" * (file_base - o.tell()))   # pad hasta file_base
        for pb, rel_off, data, md5 in metas:
            assert o.tell() == file_base + rel_off, (o.tell(), file_base + rel_off)
            o.write(data)
            o.write(b"\x00" * _pad(len(data)))      # alinear siguiente
    print(f"escrito {dst} ({len(metas)} archivos, file_base={file_base}, mode=std)")

if __name__ == "__main__":
    c = sys.argv[1]
    if c == "list": cmd_list(sys.argv[2])
    elif c == "extract": cmd_extract(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
    elif c == "repack": cmd_repack(sys.argv[2], sys.argv[3], sys.argv[4])
    else: print(__doc__)
