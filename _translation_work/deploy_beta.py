# -*- coding: utf-8 -*-
import glob,os,sys,json,importlib.util,shutil,io,contextlib
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
BS=chr(92)
def langfiles(pck,lang):
    with open(pck,"rb") as f:
        ents,h=pt.read_dir(f); fb=h[5]; d={}; pref=None
        for e in ents:
            p=e['path'].replace(BS,'/')
            if f"/localization/{lang}/" in p and p.endswith('.json'):
                if pref is None: pref=p.split('/localization/')[0]
                f.seek(e['off']+fb)
                try: d[os.path.basename(p)]=json.loads(f.read(e['size']))
                except: pass
    return d,pref
GAP={
 "EXTRACTION_TICKETS_PACKS.title":"Paquetes de Tickets de Extracción",
 "EXTRACTION_TICKETS_PACKS.description":"Añade un [gold]Ticket de Extracción[/gold] a tu [gold]mano[/gold] en {ExtractionTicketsPacksPower:diff()} turnos.",
 "TWIN_SISTERS.title":"Hermanas Gemelas",
 "TWIN_SISTERS.description":"Inflige {Damage:diff()} de daño.\nAñade un clon a tu [gold]mano[/gold] cada vez que esta carta se añade a tu [gold]mano[/gold].",
 "EXTRACTION_TICKET.title":"Ticket de Extracción",
 "EXTRACTION_TICKET.description":"[gold]Extrae[/gold] una carta de [gold]Mephistopheles[/gold].",
 "EXTRACTION_TICKETS_PACKS_POWER.title":"Paquetes de Tickets de Extracción",
 "EXTRACTION_TICKETS_PACKS_POWER.description":"Añade un [gold]Ticket de Extracción[/gold] a tu [gold]mano[/gold] en [blue]{Amount}[/blue] turnos.",
 "EXTRACTION_POWER.title":"Extracción",
 "EXTRACTION_POWER.description":"[gold]Encanta[/gold] una carta de [gold]Mephistopheles[/gold] y añádela a tu [gold]mano[/gold].",
 "STS2_CHAR_PORTALCRAFT-EVOLUTION_POTION.title":"Poción de Evolución",
 "STS2_CHAR_PORTALCRAFT-EVOLUTION_POTION.description":"Recupera 1 [gold]Punto de Evolución[/gold].",
 "STS2_CHAR_PORTALCRAFT-SUPER_EVOLUTION_POTION.title":"Poción de Superevolución",
 "STS2_CHAR_PORTALCRAFT-SUPER_EVOLUTION_POTION.description":"Recupera 1 [purple]Punto de Superevolución[/purple].",
 "STS2_CHAR_PORTALCRAFT-MULLIGAN.title":"Mulligan",
 "STS2_CHAR_PORTALCRAFT-MULLIGAN.description":"Al inicio de tu primer turno, elige hasta 4 cartas de tu mano y devuélvelas a tu pila de robo. Roba una carta por cada carta devuelta así.",
 "STS2_CHAR_PORTALCRAFT-MULLIGAN.flavor":"TEXTO DE MARCADOR",
 "STS2_CHAR_PORTALCRAFT-MULLIGAN.selectionScreenPrompt":"Devuelve cartas a tu pila de robo.",
}
if os.path.exists("_translation_work/_extra_gap.json"):
    GAP.update(json.load(open("_translation_work/_extra_gap.json",encoding="utf-8")))
TRAD={"Portalcraft":"sts2_char_portalcraft"}
MORDE=("Mordekaiser",)
for key in sorted(os.listdir("_translation_work/beta_dl")):
    base=f"_translation_work/beta_dl/{key}"
    if not os.path.isdir(base): continue
    pcks=glob.glob(f"{base}/**/*.pck",recursive=True)
    if not pcks: continue
    betapck=max(pcks,key=os.path.getsize)
    srclang="zhs" if key in MORDE else "eng"
    src,pref=langfiles(betapck,srclang)
    if not src: out(f"{key}: SIN {srclang}, omitido"); continue
    tp=glob.glob(f"Traducidos/{TRAD.get(key,key)}/*.pck")
    esp,_=langfiles(tp[0],"esp") if tp else ({},None)
    pref_fs=pref.replace("res://","")   # Windows no admite ':'
    stg=f"_translation_work/beta_dl/_esp_{key}/{pref_fs}/localization/esp"; os.makedirs(stg,exist_ok=True)
    miss=[]
    for fn,srcd in src.items():
        d={}
        for k in srcd:
            if fn in esp and k in esp[fn]: d[k]=esp[fn][k]
            elif k in GAP: d[k]=GAP[k]
            else: miss.append(f"{fn}:{k}"); d[k]=srcd[k]
        json.dump(d,open(f"{stg}/{fn}","w",encoding="utf-8"),ensure_ascii=False,indent=2)
    newpck=f"_translation_work/beta_dl/_new_{key}.pck"
    with contextlib.redirect_stdout(io.StringIO()):
        pt.cmd_repack(betapck,newpck,f"_translation_work/beta_dl/_esp_{key}")
    pdir=os.path.dirname(betapck); dst=f"Traducidos_beta/{key}"; os.makedirs(dst,exist_ok=True)
    for fx in os.listdir(pdir):
        if fx.endswith(('.dll','.json')): shutil.copy(os.path.join(pdir,fx),dst)
    shutil.copy(newpck,os.path.join(dst,os.path.basename(betapck)))
    os.remove(newpck); shutil.rmtree(f"_translation_work/beta_dl/_esp_{key}")
    out(f"{key}: OK (fuente {srclang}, {sum(len(v) for v in src.values())} claves)"+(f"  SIN TRAD: {miss}" if miss else ""))
PYEOF=None
