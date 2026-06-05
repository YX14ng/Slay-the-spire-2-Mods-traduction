# -*- coding: utf-8 -*-
# Actualiza mods (reaplicando esp existente) y agrega nuevos (sin traducir). Set MAIN.
import importlib.util,os,sys,glob,json,re,shutil,io,contextlib,hashlib
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
F="_translation_work/beta_dl/_today_full"; BS=chr(92)
TAGS=["gold","blue","red","purple","sine","pink","img","jitter","orange"]
TOK=re.compile(r"\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\([0-9]*\))?\}"); PH=re.compile(r"\{\d+\}")

def loc(pck):
    r={}; pref=None
    with open(pck,"rb") as f:
        ents,h=pt.read_dir(f); fb=h[5]
        for e in ents:
            p=e['path'].replace(BS,'/')
            if '/localization/' in p and p.endswith('.json'):
                if pref is None: pref=p.split('/localization/')[0]
                rel=p.split('/localization/')[1]
                f.seek(e['off']+fb)
                try: r[rel]=json.loads(f.read(e['size']))
                except: pass
    return r,pref,h[7]

def srcdir_for(tag,modid):
    for j in glob.glob(f"{F}/{tag}/**/*.json",recursive=True):
        try: m=json.load(open(j,encoding="utf-8-sig"))
        except: continue
        if isinstance(m,dict) and m.get("id")==modid: return os.path.dirname(j)
    return None

def vbad(v,e):
    if not isinstance(v,str): return False
    for t in TAGS:
        if v.count(f"[{t}]")!=e.count(f"[{t}]"): return True
    if v.count("{")!=e.count("{"): return True
    if sorted(TOK.findall(v))!=sorted(TOK.findall(e)): return True
    if sorted(PH.findall(v))!=sorted(PH.findall(e)): return True
    if v.count(chr(10))!=e.count(chr(10)): return True
    return False

# (mod_folder, tag, modid)
UPDATES=[("BaseLib","BaseLib","BaseLib"),("Ryoshu","Ryoshu","Ryoshu"),
         ("DamageMeter","Skada","DamageMeter"),("Rewind","Rewind","Rewind"),("QuickLink","QuickLink","QuickLink")]
NEW=[("STS2-RitsuLib","RitsuLibCompat","STS2-RitsuLib"),
     ("STS2_WineFox","WineFox","STS2_WineFox"),
     ("STS2-ShowPlayerHandCards","ShowHandCards","STS2-ShowPlayerHandCards"),
     ("MoreCharacterFX","MoreCharacterFX","MoreCharacterFX")]

out("===== UPDATES (reaplicando esp) =====")
for folder,tag,modid in UPDATES:
    sd=srcdir_for(tag,modid)
    if not sd: out(f"!! {folder}: no encontre src"); continue
    cur=glob.glob(f"{SM}/{folder}/*.pck")
    old_esp={}
    if cur:
        ol,_,_=loc(cur[0]); old_esp={k:v for k,v in ol.items() if k=="esp.json" or k.startswith("esp/")}
    newpck=glob.glob(f"{sd}/*.pck")
    if not newpck: out(f"!! {folder}: update sin pck"); continue
    newpck=newpck[0]; nl,pref,mode=loc(newpck)
    # archivos fuente (en.json plano o eng/...)
    srcfiles=[rel for rel in nl if rel=="en.json" or rel.startswith("eng/")]
    stg=f"_translation_work/beta_dl/_upd_{folder}";
    if os.path.isdir(stg): shutil.rmtree(stg)
    pref_fs=pref.replace("res://","")
    gaps=0; total=0
    for rel in srcfiles:
        esp_rel=rel.replace("en.json","esp.json").replace("eng/","esp/")
        oe=old_esp.get(esp_rel,{}); src=nl[rel]; o={}
        for k,v in src.items():
            total+=1
            es=oe.get(k)
            if es is None or vbad(v,es):
                if es is None: gaps+=1
                es=v if es is None else (v if vbad(v,es) else es)
                if vbad(v,oe.get(k,v)): es=v  # gap o cambio -> usar fuente
            o[k]=es
        dp=os.path.join(stg,pref_fs,"localization",esp_rel); os.makedirs(os.path.dirname(dp),exist_ok=True)
        json.dump(o,open(dp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    # repack + deploy (copia dll/json/pck nuevos + esp)
    newp=f"_translation_work/beta_dl/_new_upd_{folder}.pck"
    with contextlib.redirect_stdout(io.StringIO()):
        pt.cmd_repack(newpck,newp,stg)
    for dst in [f"{SM}/{folder}",f"Traducidos/{folder}"]:
        os.makedirs(dst,exist_ok=True)
        for fx in os.listdir(sd):
            if fx.endswith((".dll",".json")): shutil.copy(os.path.join(sd,fx),dst)
        shutil.copy(newp,os.path.join(dst,os.path.basename(newpck)))
    os.remove(newp)
    nv=json.load(open(glob.glob(f"{SM}/{folder}/*.json")[0],encoding="utf-8-sig")).get("version")
    out(f"  {folder}: actualizado a v{nv}  (esp reusado, {gaps}/{total} claves nuevas sin traducir)")

out("\n===== NUEVOS (sin traducir) =====")
for folder,tag,modid in NEW:
    sd=srcdir_for(tag,modid)
    if not sd: out(f"!! {folder}: no encontre src"); continue
    dst=f"{SM}/{folder}"
    if os.path.isdir(dst): shutil.rmtree(dst)
    shutil.copytree(sd,dst)
    m=json.load(open(glob.glob(f"{dst}/*.json")[0],encoding="utf-8-sig"))
    pck=glob.glob(f"{dst}/*.pck"); lg=""
    if pck:
        l,_,_=loc(pck[0]); langs=sorted(set(r.split('/')[0] if '/' in r else r[:-5] for r in l))
        lg=f" loc={langs}"
    out(f"  + {folder}: id={m.get('id')} v={m.get('version')} deps={m.get('dependencies')}{lg}")

out(f"\nset main: {len([d for d in os.listdir(SM) if os.path.isdir(os.path.join(SM,d))])} mods")
