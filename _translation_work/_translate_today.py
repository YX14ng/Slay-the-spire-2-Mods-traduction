# -*- coding: utf-8 -*-
# Traduce Ryoshu (45 claves nuevas/sin traducir) + MoreCharacterFX (8) + redeploy WineFox (esp staged).
# Valida tags/tokens/llaves/saltos. Despliega (repack) solo si el juego esta CERRADO.
import importlib.util,os,sys,glob,json,re,shutil,io,contextlib,subprocess
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"; BS=chr(92)
TAGS=["gold","blue","red","purple","sine","pink","img","jitter","orange"]
TOK=re.compile(r"\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\([0-9]*\))?\}"); PH=re.compile(r"\{\d+\}")
def loc(pck,lang):
    with open(pck,"rb") as f:
        ents,h=pt.read_dir(f); fb=h[5]; d={}
        for e in ents:
            p=e['path'].replace(BS,'/')
            if f"/localization/{lang}/" in p and p.endswith('.json'):
                f.seek(e['off']+fb); d[os.path.basename(p)]=json.loads(f.read(e['size']))
    return d
def pref_of(pck):
    with open(pck,"rb") as f:
        ents,h=pt.read_dir(f)
        for e in ents:
            p=e['path'].replace(BS,'/')
            if '/localization/' in p: return p.split('/localization/')[0].replace("res://","")
def vbad(v,e):
    n=[]
    if not isinstance(v,str) or not isinstance(e,str): return n
    for t in TAGS:
        if v.count(f"[{t}]")!=e.count(f"[{t}]"): n.append(f"tag[{t}]")
    if v.count("{")!=e.count("{"): n.append("llaves")
    if sorted(TOK.findall(v))!=sorted(TOK.findall(e)): n.append("token")
    if sorted(PH.findall(v))!=sorted(PH.findall(e)): n.append("ph")
    if v.count(chr(10))!=e.count(chr(10)): n.append("salto")
    return n
game_open = b"SlayTheSpire2.exe" in subprocess.run(["tasklist"],capture_output=True).stdout

# ============ RYOSHU ============
rp=glob.glob(f"{SM}/Ryoshu/*.pck")[0]; reng=loc(rp,"eng"); resp=loc(rp,"esp")
T_cards={
"GOOD_TIMES.description":"Aplica {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold] a TODOS los aliados.",
"RED_EYES.description":"Aplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].",
"THORACALGIA.description":"Gana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold].",
"AIR_BLADE_ULTIMATE.description":"Inflige {Damage:diff()} de daño.\nGana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold].",
"BLEEDING_DAGGER.description":"Inflige {Damage:diff()} de daño.\nAplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].",
"BREATHE_SHORTLY.description":"Inflige {Damage:diff()} de daño.\nGana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold].\nRoba {CardNum:diff()} cartas al hacer [gold]Crítico[/gold].",
"BREEZE_STRIKE.description":"Inflige {Damage:diff()} de daño.\nGana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold].\nRoba 1 carta, más {CardNum:diff()} carta adicional al hacer [gold]Crítico[/gold].",
"COUGHING_UP_BLOOD.description":"Inflige {Damage:diff()} de daño.\nAplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].\nRoba 1 carta por cada 5 de [gold]Sangrado[/gold] (máx. 3).",
"DEBONING.description":"Inflige {Damage:diff()} de daño.\nAplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].\nAplica 1 de [gold]Débil[/gold] por cada 5 de [gold]Sangrado[/gold] (máx. 3).",
"ILAI.title":"Ilai",
"RED_BLADE_SLASH.description":"Inflige {Damage:diff()} de daño.\nAplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].\nAumenta el [gold]Sangrado[/gold] que aplica esta carta en {Increase:diff()} durante este combate.",
"BLOOD_BURNING.description":"Gana {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].\nGana {Energy:diff()} [img]res://images/packed/sprite_fonts/ryoshu_energy_icon.png[/img].",
"SMOKE_OF_BATTLE.description":"[gold]Agota[/gold] tu [gold]mano[/gold].\nGana {Block:diff()} de bloqueo y {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold] por cada carta [gold]Agotada[/gold].",
"EMPTINESS.description":"Gana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold] por cada [gold]Muga[/gold].",
"BLOOD_BARRIER.description":"Gana {CalculatedBlock:diff()} de bloqueo.\nGana bloqueo igual al [gold]Sangrado[/gold] de TODOS los enemigos.",
"BLOOD_SHEILD.description":"Aplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].\nGana {Block:diff()} de bloqueo.",
"BLOOD_DEFEND.description":"Aplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].\nGana {Block:diff()} de bloqueo.",
"BURST_FORTH.description":"Por cada {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold], gana [img]res://images/packed/sprite_fonts/ryoshu_energy_icon.png[/img].",
"SCARLET_FEVER.description":"Aplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].\nCuando el enemigo muere, inflige daño igual a sus PV máximos a TODOS los enemigos.",
"PREVENT_HEMOSTASIS.description":"Aplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].\nLa acumulación de [gold]Sangrado[/gold] del enemigo no disminuirá durante {PreventHemostasisPower:diff()} turnos.",
"PUNGENT_SMELL.description":"Gana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold].\nEl próximo golpe [gold]Crítico[/gold] inflige [gold]{PungentSmellPower:diff()}%[/gold] más de daño.",
"FOG_FILLED.description":"Gana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold].\nRoba {CardNum:diff()} carta.",
"FOR_LEISURE.description":"Gana {Block:diff()} de bloqueo.\nGana {RyoshuPoisePower:diff()} de Aplomo.",
"BREATHE_INTO_ABDOMEN.description":"Gana {Block:diff()}X de bloqueo, gana {RyoshuPoisePower:diff()}X de [gold]Aplomo[/gold].",
"TRAUMA.title":"Trauma",
"SMOG_FORM.description":"Gana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold] al inicio de cada turno.",
"BLEEDING_STRIKE.description":"Inflige {Damage:diff()} de daño.\nAplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold].",
}
# Air Blade refs: usar el titulo esp de la carta referenciada (Roman numeral exacto)
ceT=resp.get("cards.json",{})
nII=ceT.get("AIR_BLADE_BETA.title","Cuchilla de Aire Ⅱ")
nIII=ceT.get("AIR_BLADE_OMEGA.title","Cuchilla de Aire Ⅲ")
nSpin=ceT.get("AIR_BLADE_ULTIMATE.title","Cuchilla de Aire Giro")
base="Inflige {Damage:diff()} de daño.\nGana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold].\nAñade %s{IfUpgraded:show:+|} a tu [gold]pila de descarte[/gold]."
T_cards["AIR_BLADE_ALPHA.description"]=base%nII
T_cards["AIR_BLADE_BETA.description"]=base%nIII
T_cards["AIR_BLADE_OMEGA.description"]=base%nSpin
T_chars={"RYOSHU.title":"Ryoshu","RYOSHU.titleObject":"Ryoshu","RYOSHU.banter.dead.endTurnPing":"……"}
T_pow={
"TRAUMA_POWER.title":"Trauma",
"RYOSHU_POISE_POWER.title":"Aplomo",
"RYOSHU_POISE_POWER.description":"Inflige daño crítico con 20 de [gold]Aplomo[/gold]. Cada ataque [gold]Crítico[/gold] reduce a la mitad la acumulación. Inflige daño crítico extra con más de 20 acumulaciones.",
"RYOSHU_BLEED_POWER.title":"Sangrado",
"RYOSHU_BLEED_POWER.description":"Después de atacar, pierde PV igual a la acumulación, luego reduce la acumulación en 1.",
"MUGA_POWER.title":"Muga",
}
T_rel={
"SEA_GLASS.RYOSHU.title":"Cristal Marino de Ryoshu",
"SEA_GLASS.RYOSHU.description":"Elige cartas del repertorio de Ryoshu para añadir a tu mazo.",
"SEA_GLASS.RYOSHU.flavor":"El cristal refleja tanto el destello de la hoja como la belleza del derramamiento de sangre.",
"LAEVATAIN.title":"Laevatain",
"NEBULIZER.description":"Al inicio del combate, gana {RyoshuPoisePower:diff()} de [gold]Aplomo[/gold].",
"RED_STAINED_GOSSYPIUM.description":"Al inicio del combate, aplica {RyoshuBleedPower:diff()} de [gold]Sangrado[/gold] a TODOS los enemigos.",
}
RYO={"cards.json":T_cards,"characters.json":T_chars,"powers.json":T_pow,"relics.json":T_rel}
# Validar vs eng + construir esp completo (resp + overrides)
problems=0; applied=0
full_esp={fn:dict(resp.get(fn,{})) for fn in resp}
for fn,tr in RYO.items():
    eng=reng.get(fn,{})
    full_esp.setdefault(fn,dict(resp.get(fn,{})))
    for k,es in tr.items():
        en=eng.get(k)
        if en is None: out(f"  RYO !! clave inexistente {fn}:{k}"); problems+=1; continue
        bad=vbad(en,es)
        if bad: out(f"  RYO !! {fn}:{k} -> {bad}\n     EN {en!r}\n     ES {es!r}"); problems+=1; continue
        full_esp[fn][k]=es; applied+=1
out(f"RYOSHU: {applied} claves traducidas, {problems} problemas")

# ============ MoreCharacterFX ============
mp=glob.glob(f"{SM}/MoreCharacterFX/*.pck")[0]; meng=loc(mp,"eng")
MCFX={
"MORECHARACTERFX.mod_title":"Más Efectos de Personaje",
"MORECHARACTERFX-ENABLE_FOR_SPECIFIC_CHARACTER_ONLY.title":"Activar solo para un personaje específico",
"MORECHARACTERFX-ENABLE_KILL_EFFECT_IMAGES.title":"Activar imágenes de efecto de muerte",
"MORECHARACTERFX-ENABLE_SPECIAL_KILL_VOICE_AUDIO.title":"Activar audio de voz especial de muerte",
"MORECHARACTERFX-ENABLE_CROSSHAIR_CENTER_IMAGE_SIZE_PERCENT.title":"Tamaño de la imagen central de la mira (%)",
"MORECHARACTERFX-ENABLE_ORBIT_AURA_ELLIPSE_LONG_DIAMETER.title":"Diámetro mayor de la elipse del aura orbital",
"MORECHARACTERFX-ENABLE_ORBIT_AURA_TILT_DEGREES.title":"Grados de inclinación del aura orbital",
"MORECHARACTERFX-ENABLE_MEMORY_DIAGNOSTICS.title":"Activar diagnóstico de memoria",
}
mfull={fn:dict(d) for fn,d in meng.items()}  # esp = copia de eng, con settings_ui traducido
mprob=0
for fn,d in meng.items():
    for k,v in d.items():
        if k in MCFX:
            bad=vbad(v,MCFX[k])
            if bad: out(f"  MCFX !! {fn}:{k} -> {bad}"); mprob+=1; continue
            mfull[fn][k]=MCFX[k]
out(f"MoreCharacterFX: {sum(1 for fn in mfull for k in mfull[fn] if k in MCFX)} claves traducidas, {mprob} problemas")

if problems or mprob:
    out("\n*** HAY PROBLEMAS — no se despliega ***"); sys.exit(1)

# ============ STAGING + DEPLOY ============
def stage_and_deploy(folder, srcpck, full_dict, label):
    pref=pref_of(srcpck)
    stg=f"_translation_work/beta_dl/_ttoday_{folder}"
    if os.path.isdir(stg): shutil.rmtree(stg)
    base=os.path.join(stg,pref,"localization","esp"); os.makedirs(base,exist_ok=True)
    for fn,d in full_dict.items():
        json.dump(d,open(os.path.join(base,fn),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    if game_open:
        out(f"  {label}: staged ✓ (deploy pendiente: juego abierto)"); return
    new=f"_translation_work/beta_dl/_ttoday_new_{folder}.pck"
    with contextlib.redirect_stdout(io.StringIO()): pt.cmd_repack(srcpck,new,stg)
    sdir=os.path.dirname(srcpck)
    for dst in [f"{SM}/{folder}",f"Traducidos/{folder}"]:
        os.makedirs(dst,exist_ok=True)
        for fx in os.listdir(sdir):
            if fx.endswith((".dll",".json")):
                s=os.path.join(sdir,fx); dd=os.path.join(dst,fx)
                if os.path.abspath(s)!=os.path.abspath(dd): shutil.copy(s,dd)
        shutil.copy(new,os.path.join(dst,os.path.basename(srcpck)))
    os.remove(new)
    chk=loc(f"{SM}/{folder}/{os.path.basename(srcpck)}","esp")
    out(f"  {label}: DESPLEGADO ✓ esp={sum(len(v) for v in chk.values())} claves")

out("\n===== STAGING / DEPLOY =====")
stage_and_deploy("Ryoshu",rp,full_esp,"Ryoshu")
stage_and_deploy("MoreCharacterFX",mp,mfull,"MoreCharacterFX")

# WineFox: redeploy esp staged previamente
wp=glob.glob(f"{SM}/STS2_WineFox/*.pck")[0]; weng=loc(wp,"eng")
stgfiles=glob.glob("_translation_work/beta_dl/_esp_STS2_WineFox/**/localization/esp/*.json",recursive=True)
wesp={os.path.basename(x):json.load(open(x,encoding="utf-8")) for x in stgfiles}
wprob=0
for fn,d in weng.items():
    e=wesp.get(fn,{})
    for k,v in d.items():
        if k not in e: wprob+=1; continue
        if vbad(v,e[k]): wprob+=1
out(f"WineFox: {sum(len(v) for v in wesp.values())} claves, {wprob} problemas")
if wprob==0:
    stage_and_deploy("STS2_WineFox",wp,wesp,"WineFox")

if game_open:
    out("\n>>> Todo TRADUCIDO y validado. CERRÁ EL JUEGO y reejecuto este script para escribir los .pck.")
else:
    out("\n>>> LISTO: Ryoshu + MoreCharacterFX + WineFox desplegados.")
