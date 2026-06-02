# -*- coding: utf-8 -*-
"""
Repara el set de mods de Steam para StS2:
- Despliega traducciones esp desde Traducidos/ y Traducidos_beta/
- Limpia settings.save (mods fantasma / rotos)
- Corrige manifests JSON con comentarios //
- Reordena mod_list (BaseLib, ModConfig primero)
"""
from __future__ import annotations

import glob
import importlib.util
import json
import os
import re
import shutil
import sys
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STEAM = r"C:\Program Files (x86)\Steam\steamapps\common\Slay the Spire 2\mods"
TRAD = os.path.join(ROOT, "Traducidos")
TRAD_BETA = os.path.join(ROOT, "Traducidos_beta")

# IDs que quedaron en settings.save pero no tienen mod usable en mods/
REMOVE_FROM_SETTINGS = {
    "STS2-RitsuLib",  # lib suelta de WineFox; no se instala como mod
    "necrobinderSkin",  # carpeta mal extraída, sin .pck
}

TOP_ORDER = ["BaseLib", "ModConfig"]

COMMENT_RE = re.compile(r"//.*?$", re.MULTILINE)


def out(msg: str) -> None:
    sys.stdout.buffer.write((msg + "\n").encode("utf-8"))


def load_pt():
    spec = importlib.util.spec_from_file_location(
        "pt", os.path.join(ROOT, "_translation_work", "pck_tool.py")
    )
    pt = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pt)
    return pt


def langs_in_pck(pt, pck_path: str) -> list[str]:
    with open(pck_path, "rb") as f:
        ents, _ = pt.read_dir(f)
    found = set()
    for e in ents:
        p = e["path"].replace("\\", "/")
        if "/localization/" in p and p.endswith(".json"):
            found.add(p.split("/localization/")[1].split("/")[0])
    return sorted(found)


def manifest_info(path: str) -> dict | None:
    try:
        raw = open(path, encoding="utf-8-sig").read()
        raw = COMMENT_RE.sub("", raw)
        m = json.loads(raw)
    except Exception:
        return None
    if isinstance(m, dict) and "id" in m and (
        "has_pck" in m or "version" in m or "dependencies" in m or "pck_name" in m
    ):
        return m
    return None


def scan_installed_ids() -> dict[str, list[str]]:
    """id del manifest -> carpetas en mods/ que lo declaran."""
    id_map: dict[str, list[str]] = {}
    for folder in os.listdir(STEAM):
        path = os.path.join(STEAM, folder)
        if not os.path.isdir(path):
            continue
        for jf in glob.glob(os.path.join(path, "*.json")) + glob.glob(
            os.path.join(path, "*", "*.json")
        ):
            m = manifest_info(jf)
            if m and m.get("id"):
                id_map.setdefault(m["id"], []).append(folder)
    return id_map


def strip_json_comments(path: str) -> bool:
    raw = open(path, encoding="utf-8-sig").read()
    if "//" not in raw:
        return False
    cleaned = COMMENT_RE.sub("", raw)
    try:
        obj = json.loads(cleaned)
    except json.JSONDecodeError:
        out(f"  !! No se pudo limpiar JSON: {path}")
        return False
    open(path, "w", encoding="utf-8").write(
        json.dumps(obj, ensure_ascii=False, indent=2) + "\n"
    )
    return True


def fix_all_manifests() -> int:
    n = 0
    for jf in glob.glob(os.path.join(STEAM, "**", "*.json"), recursive=True):
        if strip_json_comments(jf):
            out(f"  manifest limpiado: {os.path.relpath(jf, STEAM)}")
            n += 1
    return n


def source_for_folder(folder: str) -> str | None:
    """Traducidos_beta tiene prioridad si existe la misma carpeta."""
    for base in (TRAD_BETA, TRAD):
        cand = os.path.join(base, folder)
        if os.path.isdir(cand) and glob.glob(os.path.join(cand, "*.pck")):
            return cand
    return None


def deploy_translations(pt) -> list[str]:
    deployed = []
    for folder in sorted(os.listdir(STEAM)):
        steam_dir = os.path.join(STEAM, folder)
        if not os.path.isdir(steam_dir):
            continue
        steam_pcks = glob.glob(os.path.join(steam_dir, "*.pck"))
        if not steam_pcks:
            continue
        src_dir = source_for_folder(folder)
        if not src_dir:
            continue
        src_pcks = glob.glob(os.path.join(src_dir, "*.pck"))
        if not src_pcks:
            continue
        steam_pck = steam_pcks[0]
        src_pck = max(src_pcks, key=os.path.getsize)
        sl = langs_in_pck(pt, steam_pck)
        tl = langs_in_pck(pt, src_pck)
        if "esp" in sl:
            continue
        if "esp" not in tl:
            continue
        # copiar pck + json + dll del repo de traducción
        shutil.copy2(src_pck, steam_pck)
        for fx in os.listdir(src_dir):
            if fx.endswith((".json", ".dll", ".cfg")):
                shutil.copy2(
                    os.path.join(src_dir, fx), os.path.join(steam_dir, fx)
                )
        deployed.append(folder)
        out(
            f"  esp desplegado: {folder} <- {os.path.basename(src_dir)} "
            f"({os.path.basename(src_pck)}, langs ahora {langs_in_pck(pt, steam_pck)})"
        )
    return deployed


def fix_settings_save(id_map: dict[str, list[str]]) -> tuple[int, int]:
    saves = glob.glob(
        os.path.expandvars(r"%APPDATA%\SlayTheSpire2\steam\*\settings.save")
    )
    if not saves:
        out("  !! No hay settings.save")
        return 0, 0
    save_path = saves[0]
    bak = save_path + ".backup_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy2(save_path, bak)
    out(f"  respaldo settings: {bak}")

    raw = open(save_path, encoding="utf-8-sig").read()
    j = json.loads(raw)
    ml = j["mod_settings"]["mod_list"]
    before = len(ml)

    kept = []
    removed = []
    for entry in ml:
        mid = entry.get("id")
        if mid in REMOVE_FROM_SETTINGS:
            removed.append(mid)
            continue
        if mid not in id_map and mid not in os.listdir(STEAM):
            removed.append(mid)
            continue
        kept.append(entry)

    def sort_key(m):
        i = m["id"]
        if i in TOP_ORDER:
            return (0, TOP_ORDER.index(i))
        return (1, i.lower())

    kept.sort(key=sort_key)
    j["mod_settings"]["mod_list"] = kept
    open(save_path, "w", encoding="utf-8").write(
        json.dumps(j, ensure_ascii=False, indent=2) + "\n"
    )
    out(f"  settings.save: {before} -> {len(kept)} mods")
    if removed:
        out(f"  quitados de la lista: {', '.join(removed)}")
    return before, len(kept)


def main() -> None:
    out("=== Arreglar mods Steam (Slay the Spire 2) ===\n")
    pt = load_pt()

    out("1) Limpiar manifests con comentarios //")
    n_manifests = fix_all_manifests()
    out(f"   ({n_manifests} archivos)\n")

    out("2) Desplegar esp desde Traducidos / Traducidos_beta")
    deployed = deploy_translations(pt)
    if not deployed:
        out("   (nada pendiente)\n")
    else:
        out("")

    out("3) Escanear IDs instalados")
    id_map = scan_installed_ids()
    for mid in ("zsproject", "MeiLinMod", "STS2Trade"):
        if mid in id_map:
            out(f"   {mid} -> {id_map[mid]}")

    out("\n4) Corregir settings.save")
    fix_settings_save(id_map)

    out("\n5) Auditoría rápida post-fix")
    import subprocess

    subprocess.run(
        [sys.executable, os.path.join(ROOT, "_translation_work", "_audit_steam_mods.py")],
        check=False,
    )
    out("\nListo. Cerrá el juego si estaba abierto y volvé a abrirlo.")


if __name__ == "__main__":
    main()
