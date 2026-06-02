# -*- coding: utf-8 -*-
"""Audita mods de Steam vs settings.save y detecta desajustes."""
import glob
import json
import os
import sys

SM = r"C:\Program Files (x86)\Steam\steamapps\common\Slay the Spire 2\mods"


def out(s):
    sys.stdout.buffer.write((str(s) + "\n").encode("utf-8"))


def manifest_info(path):
    try:
        m = json.load(open(path, encoding="utf-8-sig"))
    except Exception:
        return None
    if isinstance(m, dict) and "id" in m and (
        "has_pck" in m or "version" in m or "dependencies" in m or "pck_name" in m
    ):
        return m
    return None


def folder_manifests(folder):
    res = []
    for jf in glob.glob(os.path.join(folder, "*.json")):
        m = manifest_info(jf)
        if m:
            res.append((os.path.basename(jf), m))
    return res


def main():
    save = glob.glob(os.path.expandvars(r"%APPDATA%\SlayTheSpire2\steam\*\settings.save"))[0]
    j = json.load(open(save, encoding="utf-8-sig"))
    folders = sorted(os.listdir(SM))
    ids = [m["id"] for m in j["mod_settings"]["mod_list"]]
    folder_set = set(folders)

    out(f"settings: {save}")
    out(f"mods en settings: {len(ids)}")
    out(f"carpetas en Steam/mods: {len(folders)}")
    out("")

    # id -> carpetas
    id_to_folders = {}
    bad_deps = []
    no_esp = []
    for d in folders:
        path = os.path.join(SM, d)
        if not os.path.isdir(path):
            continue
        for jname, m in folder_manifests(path):
            mid = m.get("id")
            id_to_folders.setdefault(mid, []).append(d)
            deps = m.get("dependencies")
            if isinstance(deps, list) and deps and isinstance(deps[0], dict):
                bad_deps.append((d, mid, deps))
        pcks = glob.glob(os.path.join(path, "*.pck"))
        if pcks:
            try:
                import importlib.util

                spec = importlib.util.spec_from_file_location(
                    "pt", os.path.join(os.path.dirname(__file__), "pck_tool.py")
                )
                pt = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(pt)
                with open(pcks[0], "rb") as f:
                    ents, _ = pt.read_dir(f)
                has_esp = any(
                    "/localization/esp/" in e["path"].replace("\\", "/") for e in ents
                )
                if not has_esp:
                    no_esp.append(d)
            except Exception as ex:
                no_esp.append(f"{d} (err: {ex})")

    out("=== IDs en settings.save sin carpeta/manifest ===")
    missing = []
    for mid in ids:
        if mid in folder_set:
            continue
        locs = id_to_folders.get(mid, [])
        if locs:
            out(f"  {mid}: OK via manifest en {locs}")
        else:
            missing.append(mid)
            out(f"  {mid}: FALTA (no hay carpeta ni manifest con este id)")
    if not missing:
        out("  (ninguno)")
    out("")

    out("=== Carpetas con manifest cuyo id NO está en settings ===")
    orphan = []
    for mid, locs in sorted(id_to_folders.items()):
        if mid not in ids:
            orphan.append((mid, locs))
            out(f"  {mid}: {locs}")
    if not orphan:
        out("  (ninguno)")
    out("")

    out("=== dependencies en formato objeto (rompe cargador) ===")
    for d, mid, deps in bad_deps:
        out(f"  {d} ({mid}): {deps[:2]}...")
    if not bad_deps:
        out("  (ninguno)")
    out("")

    out("=== Carpetas sin localization/esp en .pck ===")
    for x in no_esp[:30]:
        out(f"  {x}")
    if len(no_esp) > 30:
        out(f"  ... y {len(no_esp) - 30} más")
    out("")

    out("=== Primeros 5 del orden en settings ===")
    for i, mid in enumerate(ids[:5], 1):
        out(f"  {i}. {mid}")


if __name__ == "__main__":
    main()
