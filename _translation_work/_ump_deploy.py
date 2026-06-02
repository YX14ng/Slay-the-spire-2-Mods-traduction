# -*- coding: utf-8 -*-
# Valida y despliega la traduccion esp de UnlimitedMultiplayer (bundle multi-pref).
import importlib.util,os,sys,glob,json,re,shutil,io,contextlib
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
SRC="_translation_work/beta_dl/_src_UMP"; ESP="_translation_work/beta_dl/_esp_UMP"
PKSTG="_translation_work/beta_dl/_esp_UMP_pck"
man=json.load(open(f"{SRC}/_manifest.json",encoding="utf-8"))
TAGS=["gold","blue","red","purple","sine","pink","img","jitter","orange"]
TOK=re.compile(r"\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\([0-9]*\))?\}"); PH=re.compile(r"\{\d+\}")
prob=0; miss=[]
if os.path.isdir(PKSTG): shutil.rmtree(PKSTG)
for flat,info in man.items():
    eng=json.load(open(f"{SRC}/{flat}",encoding="utf-8"))
    ef=f"{ESP}/{flat}"
    if not os.path.exists(ef): miss.append(flat); continue
    esp=json.load(open(ef,encoding="utf-8"))
    for k,v in eng.items():
        if k not in esp: prob+=1; out(f"  [{flat}] falta clave {k}"); continue
        e=esp[k]
        if not isinstance(v,str): continue
        for t in TAGS:
            if v.count(f"[{t}]")!=e.count(f"[{t}]") or v.count(f"[/{t}]")!=e.count(f"[/{t}]"): out(f"  [{flat}] {k}: tag[{t}]"); prob+=1
        if v.count("{")!=e.count("{") or v.count("}")!=e.count("}"): out(f"  [{flat}] {k}: llaves"); prob+=1
        if sorted(TOK.findall(v))!=sorted(TOK.findall(e)) or sorted(PH.findall(v))!=sorted(PH.findall(e)): out(f"  [{flat}] {k}: tokens"); prob+=1
        if v.count(chr(10))!=e.count(chr(10)): out(f"  [{flat}] {k}: saltos"); prob+=1
    # escribir al staging nido segun esp_path
    rel=info["esp_path"].replace("res://","")
    dpath=os.path.join(PKSTG,rel); os.makedirs(os.path.dirname(dpath),exist_ok=True)
    json.dump(esp,open(dpath,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
out(f"faltan_archivos={miss} problemas={prob}")
if prob==0 and not miss:
    pck=glob.glob(f"{SM}/UnlimitedMultiplayer/*.pck")[0]
    new="_translation_work/beta_dl/_new_UMP.pck"
    with contextlib.redirect_stdout(io.StringIO()):
        pt.cmd_repack(pck,new,PKSTG)
    for dst in [f"{SM}/UnlimitedMultiplayer","Traducidos/UnlimitedMultiplayer"]:
        os.makedirs(dst,exist_ok=True)
        sdir=os.path.dirname(pck)
        for fx in os.listdir(sdir):
            if fx.endswith((".dll",".json")):
                s=os.path.join(sdir,fx); dd=os.path.join(dst,fx)
                if os.path.abspath(s)!=os.path.abspath(dd): shutil.copy(s,dd)
        shutil.copy(new,os.path.join(dst,os.path.basename(pck)))
    os.remove(new)
    with open(f"{SM}/UnlimitedMultiplayer/{os.path.basename(pck)}","rb") as f:
        ents,h=pt.read_dir(f); n=sum(1 for e in ents if "/localization/esp/" in e['path'].replace(chr(92),'/'))
    out(f"UnlimitedMultiplayer: OK ✓ esp={n} archivos -> mods/ + Traducidos/")
