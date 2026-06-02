# -*- coding: utf-8 -*-
# Extrae e instala los mods nuevos de StS2 en el set MAIN. Omite BaseLib empaquetado,
# corrige deps objeto->string, y reporta idiomas de localizacion (backlog de traduccion).
import subprocess,os,sys,glob,json,shutil,importlib.util
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
SZ=r"C:/Program Files/7-Zip/7z.exe"; DL=r"C:/Users/YX14n/Downloads"
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
FULL="_translation_work/beta_dl/_newmods_full"
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
BS=chr(92)

ARCH={
 "QuickLink":"QuickLink - Multiplayer Quick Rewind.zip",
 "UnlimitedMultiplayer":"Unlimited Multiplayer-66-0-2-0-1773829559.zip",
 "LibraryOfRuina":"LibraryOfRuina 0.5.5 Public Version-368-0-5-5-1779164287.zip",
 "CivilightEterna":"Civilight Eterna Defect Main File-737-1-1777574929.rar",
 "WineFox":"STS2-WineFox(For 0.103.2)-859-1-1-21-1779226328.zip",
 "Elaina":"Sts2ElainaMod-792-1-0-4-1778294622.zip",
 "AkiSister":"AkiSister-654-1-0-2-1778556860.rar",
 "Shinki":"ShinkiMod-634-4-1778579724.zip",
 "SlayTheSchale":"SlayTheSchale-806-2-1778366664.zip",
 "LunaDelta":"LunaDelta V1.8.0-667-7-1780217625.7z",
 "MzmChar":"MzmChar - stable-915-0-2-0-1780293106.zip",
 "Faust":"Faust 0.1.6-1046-0-1-6-1780333752.zip",
 "PAINTER":"PAINTER-813-0-55-1779606568.zip",
 "Shadowverse":"ShadowversebydmodV0.8.7-977-0-8-7-1779690211.rar",
}
# NO instalar: Kaguya (beta PowerInstanceType), Wuwancients (patron crash Herta), HexBrawl (update de HextechRunes ya instalado)

def manifest_info(j):
    try: m=json.load(open(j,encoding="utf-8-sig"))
    except: return None
    if isinstance(m,dict) and "id" in m and ("has_pck" in m or "version" in m or "dependencies" in m or "pck_name" in m):
        return m
    return None

def fix_deps(folder):
    for j in glob.glob(folder+"/*.json"):
        m=manifest_info(j)
        if not m: continue
        deps=m.get("dependencies")
        if isinstance(deps,list) and deps and isinstance(deps[0],dict):
            m["dependencies"]=[d.get("id") for d in deps if d.get("id")]
            json.dump(m,open(j,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
            return f"deps objeto->string {m['dependencies']}"
    return ""

def loc_langs(folder):
    pcks=glob.glob(folder+"/*.pck")
    if not pcks: return "(sin pck)"
    res={}
    for pck in pcks:
        try:
            with open(pck,"rb") as f:
                ents,h=pt.read_dir(f); fb=h[5]
                for e in ents:
                    p=e['path'].replace(BS,'/')
                    if '/localization/' in p and p.endswith('.json'):
                        lang=p.split('/localization/')[1].split('/')[0]
                        f.seek(e['off']+fb)
                        try: n=len(json.loads(f.read(e['size'])))
                        except: n=0
                        res[lang]=res.get(lang,0)+n
        except Exception as ex: return f"(err {ex})"
    if not res: return "(sin localization -> solo arte)"
    return ", ".join(f"{l}:{n}" for l,n in sorted(res.items()))

installed=[]
for tag,fn in ARCH.items():
    od=os.path.join(FULL,tag)
    if not os.path.isdir(od) or not glob.glob(od+"/**/*.pck",recursive=True):
        os.makedirs(od,exist_ok=True)
        r=subprocess.run([SZ,"x","-y",os.path.join(DL,fn),f"-o{od}"],stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
        if r.returncode!=0: out(f"!! {tag}: error extraccion {r.stderr.decode(errors='ignore')[:120]}"); continue
    root=os.path.abspath(od)
    # carpetas-mod = dir padre de un manifest, que no sea la raiz de extraccion ni BaseLib
    modfolders={}
    for j in glob.glob(od+"/**/*.json",recursive=True):
        m=manifest_info(j)
        if not m: continue
        d=os.path.abspath(os.path.dirname(j))
        if d==root: continue                 # RitsuLib suelto en raiz (Elaina) -> se ignora; viene de WineFox
        if m.get("id")=="BaseLib": continue   # no pisar BaseLib bueno
        modfolders[os.path.basename(d)]=(d,m)
    if not modfolders: out(f"!! {tag}: no detecte carpetas-mod"); continue
    for name,(d,m) in modfolders.items():
        dst=os.path.join(SM,name)
        existed = os.path.isdir(dst)
        if existed: shutil.rmtree(dst)
        shutil.copytree(d,dst)
        note=fix_deps(dst)
        langs=loc_langs(dst)
        installed.append((tag,name,m.get("id"),m.get("version"),langs))
        out(f"[{tag}] -> mods/{name}  id={m.get('id')} v={m.get('version')}  {'(REEMPLAZADO)' if existed else ''} {note}")
        out(f"        localizacion: {langs}")

out("\n===== RESUMEN INSTALADOS =====")
for tag,name,mid,ver,langs in installed:
    out(f"  {name} (v{ver})  loc=[{langs}]")
out(f"\nTotal carpetas instaladas: {len(installed)}")
out(f"Set MAIN ahora: {len([d for d in os.listdir(SM) if os.path.isdir(os.path.join(SM,d))])} mods")
