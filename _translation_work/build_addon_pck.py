# -*- coding: utf-8 -*-
"""Crea un .pck GDPC v3 NUEVO (mod aparte) que contiene solo Manosaba/localization/esp/*.json.
Mismas convenciones que el pck original: file_base=112, offsets relativos, alineado a 16, md5 real."""
import struct, os, hashlib, json

SRC_ESP = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/add/Manosaba/localization/esp"
ADDON   = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/ManosabaES"
PCK     = os.path.join(ADDON, "ManosabaES.pck")
ALIGN = 16
FILE_BASE = 112
def _pad(n, a=ALIGN): return (a - (n % a)) % a

os.makedirs(ADDON, exist_ok=True)

# recolectar archivos -> ruta interna res:// (Manosaba/localization/esp/<file>)
records = []
for fn in sorted(os.listdir(SRC_ESP)):
    if fn.endswith(".json"):
        data = open(os.path.join(SRC_ESP, fn), "rb").read()
        records.append((f"Manosaba/localization/esp/{fn}", data))

with open(PCK, "wb") as o:
    o.write(b"GDPC")
    o.write(struct.pack("<5I", 3, 4, 5, 1, 2))   # ver, 4.5.1, flags=2 (REL_FILEBASE)
    o.write(struct.pack("<Q", FILE_BASE))
    o.write(struct.pack("<Q", 0))                 # dir_off placeholder @0x20
    o.write(b"\x00" * (FILE_BASE - o.tell()))     # reservado hasta file_base
    meta = []
    for path, data in records:
        o.write(b"\x00" * _pad(o.tell()))
        abs_off = o.tell()
        o.write(data)
        meta.append((path, abs_off - FILE_BASE, len(data), hashlib.md5(data).digest()))
    dir_off = o.tell()
    o.write(struct.pack("<I", len(meta)))
    for path, rel_off, size, md5 in meta:
        pb = path.encode("utf-8"); pb += b"\x00" * _pad(len(pb), 4)
        o.write(struct.pack("<I", len(pb))); o.write(pb)
        o.write(struct.pack("<QQ", rel_off, size)); o.write(md5)
        o.write(struct.pack("<I", 0))
    o.seek(0x20); o.write(struct.pack("<Q", dir_off))

# manifiesto del mod aparte
manifest = {
    "id": "ManosabaES",
    "name": "Manosaba - Español (Latinoamérica)",
    "pck_name": "ManosabaES",
    "author": "Traducción ES-LATAM",
    "description": "Traducción al español (Latinoamérica) del mod Manosaba.\nAgrega el idioma 'esp' sin modificar el .pck original. Requiere Manosaba instalado y el juego en Español (Latinoamérica).",
    "version": "v1.0.0",
    "has_pck": True,
    "has_dll": False,
    "dependencies": ["BaseLib", "Manosaba"],
    "affects_gameplay": False
}
json.dump(manifest, open(os.path.join(ADDON, "ManosabaES.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"creado {PCK} con {len(records)} archivos + manifiesto")
