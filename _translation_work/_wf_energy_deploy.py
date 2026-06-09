# -*- coding: utf-8 -*-
# Despliega el fix de energia de WineFox (reemplaza {X:energyIcons()} por {X}[img]icono[/img]).
# Reusa el staging _translation_work/beta_dl/_wf_energyfix. Requiere el juego CERRADO.
import importlib.util,os,glob,sys,shutil,io,contextlib,subprocess,json
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"; BS=chr(92)
STG="_translation_work/beta_dl/_wf_energyfix"
if not os.path.isdir(STG): out("!! no existe el staging; reejecutá el script de fix primero"); sys.exit(1)
if b"SlayTheSpire2.exe" in subprocess.run(["tasklist"],capture_output=True).stdout:
    out("⚠ JUEGO ABIERTO — cerralo y reintento."); sys.exit(0)
wp=glob.glob(f"{SM}/STS2_WineFox/*.pck")[0]
new="_translation_work/beta_dl/_wf_energyfix_new.pck"
with contextlib.redirect_stdout(io.StringIO()): pt.cmd_repack(wp,new,STG)
for dst in [f"{SM}/STS2_WineFox","Traducidos/STS2_WineFox"]:
    os.makedirs(dst,exist_ok=True)
    shutil.copy(new,os.path.join(dst,os.path.basename(wp)))
os.remove(new)
# verificar
with open(f"{SM}/STS2_WineFox/{os.path.basename(wp)}","rb") as f:
    ents,h=pt.read_dir(f); fb=h[5]; bad=0
    for e in ents:
        p=e['path'].replace(BS,'/')
        if p.endswith("/cards.json") and "/localization/" in p:
            f.seek(e['off']+fb); cj=json.loads(f.read(e['size']))
            for k,v in cj.items():
                if isinstance(v,str) and "energyIcons()" in v: bad+=1
            if p.endswith("zhs/cards.json"):
                out("zhs Pico de Madera: "+cj.get("STS2_WINE_FOX_CARD_WOODEN_PICKAXE.description","?"))
    out(f"DESPLEGADO ✓  (claves con energyIcons() restantes en cards: {bad})")
