# -*- coding: utf-8 -*-
# Valida y despliega traducciones esp de los mods nuevos.
# Para cada mod con staging en _esp_<mod>/, valida contra la fuente (_src_<mod>/),
# y si esta OK reempaca el pck (agregando localization/esp) y lo despliega a mods/ + Traducidos/.
# Uso: python _deploy_newmods.py [mod1 mod2 ...]   (sin args = todos los que tengan staging)
import importlib.util,os,sys,glob,json,re,shutil,io,contextlib
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
META=json.load(open("_translation_work/beta_dl/_src_meta.json",encoding="utf-8"))
TAGS=["gold","blue","red","purple","sine","pink","img","jitter","orange","green","yellow"]
TOK=re.compile(r"\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\([0-9]*\))?\}")
targets=sys.argv[1:] or list(META)
for mod in targets:
    m=META.get(mod)
    if not m: out(f"{mod}: sin metadata"); continue
    pref_fs=m["pref"].replace("res://","")
    stg=f"_translation_work/beta_dl/_esp_{mod}/{pref_fs}/localization/esp"
    srcd=f"_translation_work/beta_dl/_src_{mod}"
    if not os.path.isdir(stg): out(f"{mod}: SIN staging esp ({stg})"); continue
    prob=0; missfiles=[]; misskeys=0
    for sf in sorted(glob.glob(srcd+"/*.json")):
        fn=os.path.basename(sf); src=json.load(open(sf,encoding="utf-8"))
        ef=f"{stg}/{fn}"
        if not os.path.exists(ef): missfiles.append(fn); continue
        esp=json.load(open(ef,encoding="utf-8"))
        for k,v in src.items():
            if k not in esp: misskeys+=1; continue
            e=esp[k]
            if not isinstance(v,str): continue
            for t in TAGS:
                if v.count(f"[{t}]")!=e.count(f"[{t}]") or v.count(f"[/{t}]")!=e.count(f"[/{t}]"):
                    out(f"  [{mod}/{fn}] {k}: tag[{t}] {e.count(f'[{t}]')}/{e.count(f'[/{t}]')} != {v.count(f'[{t}]')}/{v.count(f'[/{t}]')}"); prob+=1
            if v.count("{")!=e.count("{") or v.count("}")!=e.count("}"): out(f"  [{mod}/{fn}] {k}: llaves {e.count('{')}!={v.count('{')}"); prob+=1
            if sorted(TOK.findall(v))!=sorted(TOK.findall(e)): out(f"  [{mod}/{fn}] {k}: tokens {sorted(TOK.findall(e))} != {sorted(TOK.findall(v))}"); prob+=1
            if v.count(chr(10))!=e.count(chr(10)): out(f"  [{mod}/{fn}] {k}: saltos {e.count(chr(10))}!={v.count(chr(10))}"); prob+=1
    if missfiles: out(f"{mod}: FALTAN archivos {missfiles}"); prob+=99
    if misskeys: out(f"{mod}: faltan {misskeys} claves"); prob+=misskeys
    if prob:
        out(f"{mod}: PROBLEMAS={prob} -> NO desplegado"); continue
    # repack + deploy
    pck=m["pck"]; new=f"_translation_work/beta_dl/_new_{mod}.pck"
    with contextlib.redirect_stdout(io.StringIO()):
        pt.cmd_repack(pck,new,f"_translation_work/beta_dl/_esp_{mod}")
    folder=os.path.basename(os.path.dirname(pck))  # carpeta del mod en mods/
    pckname=os.path.basename(pck)
    srcdir=os.path.dirname(pck)
    for dst in [f"{SM}/{folder}", f"Traducidos/{folder}"]:
        os.makedirs(dst,exist_ok=True)
        for fx in os.listdir(srcdir):
            if fx.endswith((".dll",".json")):
                s=os.path.join(srcdir,fx); d=os.path.join(dst,fx)
                if os.path.abspath(s)!=os.path.abspath(d): shutil.copy(s,d)
        shutil.copy(new,os.path.join(dst,pckname))
    os.remove(new)
    # verificar esp en el pck desplegado
    with open(f"{SM}/{folder}/{pckname}","rb") as f:
        ents,h=pt.read_dir(f); n=sum(1 for e in ents if "/localization/esp/" in e['path'].replace(chr(92),'/'))
    out(f"{mod}: OK ✓ desplegado a mods/{folder} + Traducidos/{folder} (esp: {n} archivos)")
