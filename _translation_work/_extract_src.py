# -*- coding: utf-8 -*-
# Extrae la localizacion fuente (eng, o zhs para Shadowverse) de cada mod nuevo a JSON plano,
# y guarda metadata (pref/mode/srclang) en _src_meta.json para reempacar luego.
import importlib.util,os,sys,glob,json
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
BS=chr(92)
# mod-folder -> idioma fuente
MODS={
 "MzmChar":"eng","ShinkiMod":"eng","Faust":"eng","LunaDelta":"eng",
 "AkiSister":"eng","Sts2ElainaMod":"eng","Painter":"eng","STS2_WineFox":"eng",
 "LibraryOfRuina":"eng",
}
meta={}
for mod,src in MODS.items():
    pcks=glob.glob(f"{SM}/{mod}/*.pck")
    if not pcks: out(f"!! {mod}: sin pck"); continue
    pck=max(pcks,key=os.path.getsize)
    with open(pck,"rb") as f:
        ents,h=pt.read_dir(f); fb=h[5]
        pref=None; files={}
        for e in ents:
            p=e['path'].replace(BS,'/')
            if f"/localization/{src}/" in p and p.endswith('.json'):
                if pref is None: pref=p.split('/localization/')[0]
                f.seek(e['off']+fb)
                try: files[os.path.basename(p)]=json.loads(f.read(e['size']))
                except Exception as ex: out(f"  {mod} err {p}: {ex}")
    sd=f"_translation_work/beta_dl/_src_{mod}"; os.makedirs(sd,exist_ok=True)
    tot=0
    for fn,d in files.items():
        json.dump(d,open(f"{sd}/{fn}","w",encoding="utf-8"),ensure_ascii=False,indent=2); tot+=len(d)
    meta[mod]={"pck":pck,"pref":pref,"mode":h[7],"srclang":src,"files":sorted(files),"keys":tot}
    out(f"{mod}: src={src} pref={pref} mode={h[7]} files={len(files)} keys={tot}")
json.dump(meta,open("_translation_work/beta_dl/_src_meta.json","w",encoding="utf-8"),ensure_ascii=False,indent=2)
out("\nmetadata -> _translation_work/beta_dl/_src_meta.json")
