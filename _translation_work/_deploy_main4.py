# -*- coding: utf-8 -*-
# Valida y despliega esp de los 4 mods de UI del main: DamageMeter/Rewind/ModConfig (flat esp.json) + BaseLib (esp/ folder).
import importlib.util,os,sys,glob,json,re,shutil,io,contextlib
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
META=json.load(open("_translation_work/beta_dl/_src2_meta.json",encoding="utf-8"))
BS=chr(92)
# ModConfig inline (7 claves)
MODCONFIG={"tab_mods":"Mods","no_configs":"Ningún mod registró configuraciones.","reset_defaults":"Restablecer","press_any_key":"Presioná una tecla...","key_unbound":"Sin asignar","keybind_tooltip":"Clic para reasignar. Esc o clic en cualquier lado para borrar.","color_picker_tooltip":"Clic para elegir un color."}
os.makedirs("_translation_work/beta_dl/_esp2_ModConfig",exist_ok=True)
json.dump(MODCONFIG,open("_translation_work/beta_dl/_esp2_ModConfig/esp.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)

TAGS=["gold","blue","red","purple","sine","pink","img","jitter","orange"]
TOK=re.compile(r"\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\([0-9]*\))?\}"); PH=re.compile(r"\{\d+\}")
def vbad(v,e):
    n=0
    for t in TAGS:
        if v.count(f"[{t}]")!=e.count(f"[{t}]"): n+=1
    if v.count("{")!=e.count("{"): n+=1
    if sorted(TOK.findall(v))!=sorted(TOK.findall(e)): n+=1
    if sorted(PH.findall(v))!=sorted(PH.findall(e)): n+=1
    if v.count(chr(10))!=e.count(chr(10)): n+=1
    return n

def game_open():
    import subprocess
    try: return b"SlayTheSpire2.exe" in subprocess.run(["tasklist"],capture_output=True).stdout
    except: return False

results={}
for mod,info in META.items():
    src_dir=f"_translation_work/beta_dl/_src2_{mod}"; esp_dir=f"_translation_work/beta_dl/_esp2_{mod}"
    prob=0; miss=0
    pckstg=f"_translation_work/beta_dl/_pck2_{mod}"
    if os.path.isdir(pckstg): shutil.rmtree(pckstg)
    if info["flat"]:
        src=json.load(open(f"{src_dir}/en.json",encoding="utf-8"))
        ef=f"{esp_dir}/esp.json"
        if not os.path.exists(ef): out(f"{mod}: SIN esp.json"); continue
        esp=json.load(open(ef,encoding="utf-8"))
        for k,v in src.items():
            if k not in esp: miss+=1; continue
            if isinstance(v,str): prob+=vbad(v,esp[k])
        rel=info["esp_path"].replace("res://","")
        dp=os.path.join(pckstg,rel); os.makedirs(os.path.dirname(dp),exist_ok=True)
        json.dump(esp,open(dp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    else:  # BaseLib folder
        for sf in glob.glob(f"{src_dir}/*.json"):
            fn=os.path.basename(sf); src=json.load(open(sf,encoding="utf-8"))
            ef=f"{esp_dir}/{fn}"
            if not os.path.exists(ef): miss+=len(src); continue
            esp=json.load(open(ef,encoding="utf-8"))
            for k,v in src.items():
                if k not in esp: miss+=1; continue
                if isinstance(v,str): prob+=vbad(v,esp[k])
            rel=info["pref"].replace("res://","")+f"/localization/esp/{fn}"
            dp=os.path.join(pckstg,rel); os.makedirs(os.path.dirname(dp),exist_ok=True)
            json.dump(esp,open(dp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    results[mod]=(prob,miss,pckstg)
    out(f"{mod}: problemas={prob} faltan={miss}")

bad=[m for m,(p,ms,_) in results.items() if p or ms]
if bad: out(f"\nNO desplegado (con problemas): {bad}"); sys.exit(0)
if game_open():
    out("\n⚠ JUEGO ABIERTO — todo validado y staging listo, pero NO puedo reemplazar los pck. Cerrá el juego y reintento.")
    sys.exit(0)
# deploy
for mod,(p,ms,pckstg) in results.items():
    info=META[mod]; pck=info["pck"]; new=f"_translation_work/beta_dl/_new2_{mod}.pck"
    with contextlib.redirect_stdout(io.StringIO()):
        pt.cmd_repack(pck,new,pckstg)
    sdir=os.path.dirname(pck)
    for dst in [f"{SM}/{mod}", f"Traducidos/{mod}"]:
        os.makedirs(dst,exist_ok=True)
        for fx in os.listdir(sdir):
            if fx.endswith((".dll",".json")):
                s=os.path.join(sdir,fx); d=os.path.join(dst,fx)
                if os.path.abspath(s)!=os.path.abspath(d): shutil.copy(s,d)
        shutil.copy(new,os.path.join(dst,os.path.basename(pck)))
    os.remove(new)
    out(f"{mod}: OK ✓ desplegado a mods/{mod} + Traducidos/{mod}")
