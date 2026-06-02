# -*- coding: utf-8 -*-
# Traduce Watcher main v1.4.3 (esp): reusa el esp beta para las claves que calzan,
# sobreescribe las 58 que cambiaron de tags/tokens entre versiones.
import importlib.util,sys,os,json,re,glob,shutil,io,contextlib
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2"
BS=chr(92)
def langfiles(pck,lang):
    with open(pck,"rb") as f:
        ents,h=pt.read_dir(f); fb=h[5]; d={}
        for e in ents:
            p=e['path'].replace(BS,'/')
            if f"/localization/{lang}/" in p and p.endswith('.json'):
                f.seek(e['off']+fb); d[os.path.basename(p)]=json.loads(f.read(e['size']))
    return d

MAINPCK="_translation_work/beta_dl/_watcher_main/TheWatcher/Watcher.pck"
MDIR="_translation_work/beta_dl/_watcher_main/TheWatcher"
FDIR="_translation_work/beta_dl/_watcher_main/WatcherFeminized/watcherFeminized"
eng=langfiles(MAINPCK,"eng")
betaesp=langfiles(glob.glob("Traducidos_beta/Watcher/*.pck")[0],"esp")

# Sobreescrituras: clave -> esp calzado a los tags/tokens del eng main 1.4.3
OV={
# cards
"WATCHER-CUT_THROUGH_FATE.description":"Inflige {Damage:diff()} de daño.\n[gold]Vislumbra[/gold]. {Cards:diff()}\nRoba [blue]1[/blue] carta.",
"WATCHER-EMPTY_FIST.description":"Inflige {Damage:diff()} de daño.\nSal de tu [gold]Postura[/gold].",
"WATCHER-FOLLOW_UP.description":"Inflige {Damage:diff()} de daño.\nSi la última carta jugada fue un Ataque, gana [blue]1[/blue] {energyPrefix:energyIcons(1)}.",
"WATCHER-EMPTY_BODY.description":"Gana {Block:diff()} de [gold]Bloqueo[/gold].\nSal de tu [gold]Postura[/gold].",
"WATCHER-EMPTY_MIND.description":"Roba {Cards:diff()} cartas.\nSal de tu [gold]Postura[/gold].",
"WATCHER-RUSHDOWN.description":"Cada vez que entras en [gold]Ira[/gold], roba [blue]2[/blue] cartas.",
"WATCHER-WEAVE.description":"Inflige {Damage:diff()} de daño. Cada vez que [gold]Vislumbras[/gold], devuelve esta carta de la pila de descarte a tu mano.",
"WATCHER-COLLECT.description":"Pon un [gold]Milagro+[/gold] en\n tu mano al inicio\nde tus próximos {IfUpgraded:show:X+1|X} turnos.",
"WATCHER-MENTAL_FORTRESS.description":"Cada vez que cambias de [gold]Postura[/gold], gana {MentalFortressPower:diff()} de [gold]Bloqueo[/gold].",
"WATCHER-SWIVEL.description":"Gana {Block:diff()} de [gold]Bloqueo[/gold].\nEl próximo Ataque que juegues cuesta 0.",
"WATCHER-WORSHIP.description":"Gana [blue]5[/blue] de [gold]Mantra[/gold].",
"WATCHER-LESSON_LEARNED.description":"Inflige {Damage:diff()} de daño.\nSi es [gold]Letal[/gold], [gold]Mejora[/gold] una carta aleatoria de tu mazo.",
"WATCHER-OMNISCIENCE.description":"Elige una carta de tu pila de robo. Juega la carta elegida dos veces y [gold]Agótala[/gold].",
"WATCHER-MASTER_REALITY.description":"Cada vez que se crea una carta durante el combate, [gold]Mejórala[/gold].",
"WATCHER-DEVA_FORM.description":"Al inicio de tu turno, gana {energyPrefix:energyIcons(1)} y aumenta esta ganancia en 1.",
# potions
"WATCHER-BOTTLED_MIRACLE.description":"Añade {Cards:diff()} [blue]Milagros[/blue] a tu mano.",
"WATCHER-CALM_POTION.description":"Entra en [blue]Calma[/blue].",
"WATCHER-WRATH_POTION.description":"Entra en [blue]Ira[/blue].",
"WATCHER-AMBROSIA.description":"Entra en [blue]Divinidad[/blue].",
# powers
"WATCHER-MARK_POWER.description":"Cada vez que juegas [blue]Puntos de Presión[/blue], pierde [blue]X[/blue] PV.",
"WATCHER-MARK_POWER.smartDescription":"Cada vez que juegas [blue]Puntos de Presión[/blue], pierde [blue]{Amount}[/blue] PV.",
"WATCHER-MANTRA_POWER.description":"Cada vez que ganas 10 de Mantra, entra en [blue]Divinidad[/blue].",
"WATCHER-MANTRA_POWER.smartDescription":"Cada vez que ganas 10 de Mantra, entra en [blue]Divinidad[/blue].",
"WATCHER-BATTLE_HYMN_POWER.description":"Al inicio de tu turno, añade [blue]X[/blue] [blue]Castigos[/blue] a tu mano.",
"WATCHER-BATTLE_HYMN_POWER.smartDescription":"Al inicio de tu turno, añade [blue]{Amount}[/blue] [blue]Castigos[/blue] a tu mano.",
"WATCHER-COLLECT_POWER.description":"Al inicio de tus próximos [blue]X[/blue] turnos, pon un [blue]Milagro+[/blue] en tu mano.",
"WATCHER-COLLECT_POWER.smartDescription":"Al inicio de tus próximos [blue]{Amount}[/blue] turnos, pon un [blue]Milagro+[/blue] en tu mano.",
"WATCHER-FASTING_POWER.description":"Al inicio de tu turno, pierde [blue]X[/blue] {energyPrefix:energyIcons(1)} de Energía.",
"WATCHER-FASTING_POWER.smartDescription":"Al inicio de tu turno, pierde [blue]{Amount}[/blue] {energyPrefix:energyIcons(1)} de Energía.",
"WATCHER-FORESIGHT_POWER.description":"Al inicio de tu turno, [blue]Vislumbra[/blue] [blue]X[/blue].",
"WATCHER-FORESIGHT_POWER.smartDescription":"Al inicio de tu turno, [blue]Vislumbra[/blue] [blue]{Amount}[/blue].",
"WATCHER-LIKE_WATER_POWER.description":"Al final de tu turno, si estás en [blue]Calma[/blue], gana [blue]X[/blue] de [blue]Bloqueo[/blue]",
"WATCHER-LIKE_WATER_POWER.smartDescription":"Al final de tu turno, si estás en [blue]Calma[/blue], gana [blue]{Amount}[/blue] de [blue]Bloqueo[/blue]",
"WATCHER-MENTAL_FORTRESS_POWER.description":"Cada vez que cambias de [blue]Postura[/blue], gana [blue]X[/blue] de [blue]Bloqueo[/blue]",
"WATCHER-MENTAL_FORTRESS_POWER.smartDescription":"Cada vez que cambias de [blue]Postura[/blue], gana [blue]{Amount}[/blue] de [blue]Bloqueo[/blue]",
"WATCHER-NIRVANA_POWER.description":"Cada vez que [blue]Vislumbras[/blue], gana [blue]X[/blue] de [blue]Bloqueo[/blue]",
"WATCHER-NIRVANA_POWER.smartDescription":"Cada vez que [blue]Vislumbras[/blue], gana [blue]{Amount}[/blue] de [blue]Bloqueo[/blue]",
"WATCHER-RUSHDOWN_POWER.description":"Cada vez que entras en [gold]Ira[/gold], roba [blue]X[/blue] cartas.",
"WATCHER-SIMMERING_RAGE_POWER.description":"Entra en [blue]Ira[/blue] al inicio del turno",
"WATCHER-SIMMERING_RAGE_POWER.smartDescription":"Entra en [blue]Ira[/blue] al inicio del turno",
"WATCHER-STUDY_POWER.description":"Al final de tu turno, baraja [blue]X[/blue] [blue]Percepciones[/blue] en tu pila de robo.",
"WATCHER-STUDY_POWER.smartDescription":"Al final de tu turno, baraja [blue]{Amount}[/blue] [blue]Percepciones[/blue] en tu pila de robo.",
"WATCHER-BLOCK_RETURN_POWER.description":"Cuando es atacado, gana [blue]X[/blue] de [blue]Bloqueo[/blue].",
"WATCHER-BLOCK_RETURN_POWER.smartDescription":"Cuando es atacado, gana [blue]{Amount}[/blue] de [blue]Bloqueo[/blue].",
"WATCHER-WAVE_OF_THE_HAND_POWER.description":"Cada vez que ganas [blue]Bloqueo[/blue], aplica [blue]X[/blue] de [blue]Débil[/blue] a TODOS los enemigos.",
"WATCHER-WAVE_OF_THE_HAND_POWER.smartDescription":"Cada vez que ganas [blue]Bloqueo[/blue], aplica [blue]{Amount}[/blue] de [blue]Débil[/blue] a TODOS los enemigos.",
"WATCHER-DEVA_POWER.smartDescription":"Al inicio de tu turno, gana {energyPrefix:energyIcons(1)} [blue]{Energy:diff()}[/blue] veces y aumenta esta ganancia en {Amount}.",
"WATCHER-DEVOTION_POWER.description":"Al inicio de tu turno, gana [blue]X[/blue] de [blue]Mantra[/blue].",
"WATCHER-DEVOTION_POWER.smartDescription":"Al inicio de tu turno, gana [blue]{Amount}[/blue] de [blue]Mantra[/blue].",
"WATCHER-ESTABLISHMENT_POWER.description":"Cada vez que una carta se [blue]Conserva[/blue], reduce su coste en X.",
"WATCHER-ESTABLISHMENT_POWER.smartDescription":"Cada vez que una carta se [blue]Conserva[/blue], reduce su coste en [blue]{Amount}[/blue].",
"WATCHER-MASTER_REALITY_POWER.description":"Cada vez que se crea una carta, se [blue]Mejora[/blue].",
"WATCHER-MASTER_REALITY_POWER.smartDescription":"Cada vez que se crea una carta, se [blue]Mejora[/blue].",
"WATCHER-PLATED_ARMOR_POWER.description":"Al final de tu turno, gana [blue]X[/blue] de [gold]Bloqueo[/gold]. Recibir daño de ataque no bloqueado reduce la [gold]Armadura de Placas[/gold] en [blue]1[/blue].",
"WATCHER-DUALITY_POWER.smartDescription":"Pierde {Amount} de [gold]Destreza[/gold] hasta el final de este turno.",
# relics
"WATCHER-PURE_WATER.description":"Al inicio de cada combate, añade 1 [gold]Milagro[/gold] a tu mano.",
"WATCHER-DUALITY.description":"Cada vez que juegas un [gold]Ataque[/gold], gana 1 de [gold]Destreza[/gold] temporal. ",
"WATCHER-HOLY_WATER.description":"Reemplaza al [gold]Agua Pura[/gold]. Al inicio de cada combate, añade 3 [gold]Milagros[/gold] a tu mano.",
}

TAGS=["gold","blue","red","purple","sine","pink","img","jitter","orange"]
TOK=re.compile(r"\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\([0-9]*\))?\}")
stg="_translation_work/beta_dl/_esp_WatcherMain/Watcher/localization/esp"; os.makedirs(stg,exist_ok=True)
prob=0; miss=[]
for fn,d in eng.items():
    e=betaesp.get(fn,{}); o={}
    for k,v in d.items():
        if k in OV: es=OV[k]
        elif k in e: es=e[k]
        else: miss.append(f"{fn}:{k}"); es=v
        o[k]=es
        for t in TAGS:
            if v.count(f"[{t}]")!=es.count(f"[{t}]"): out(f"[{fn}] {k}: tag[{t}] {es.count(f'[{t}]')}!={v.count(f'[{t}]')}"); prob+=1
        if v.count("{")!=es.count("{") or v.count("}")!=es.count("}"): out(f"[{fn}] {k}: llaves"); prob+=1
        if sorted(TOK.findall(v))!=sorted(TOK.findall(es)): out(f"[{fn}] {k}: tokens {sorted(TOK.findall(es))} vs {sorted(TOK.findall(v))}"); prob+=1
        if v.count(chr(10))!=es.count(chr(10)): out(f"[{fn}] {k}: saltos {es.count(chr(10))}!={v.count(chr(10))}"); prob+=1
    json.dump(o,open(f"{stg}/{fn}","w",encoding="utf-8"),ensure_ascii=False,indent=2)
out(f"SIN TRADUCIR ({len(miss)}): {miss}")
out(f"PROBLEMAS={prob}")

if prob==0 and not miss:
    new="_translation_work/beta_dl/_new_WatcherMain.pck"
    with contextlib.redirect_stdout(io.StringIO()):
        pt.cmd_repack(MAINPCK,new,"_translation_work/beta_dl/_esp_WatcherMain")
    for dst in [SM+"/mods/Watcher","Traducidos/Watcher"]:
        os.makedirs(dst,exist_ok=True)
        shutil.copy(f"{MDIR}/Watcher.dll",dst); shutil.copy(f"{MDIR}/Watcher.json",dst)
        shutil.copy(new,dst+"/Watcher.pck")
    os.remove(new)
    for dst in [SM+"/mods/watcherFeminized","Traducidos/watcherFeminized"]:
        os.makedirs(dst,exist_ok=True)
        for fx in os.listdir(FDIR): shutil.copy(os.path.join(FDIR,fx),dst)
    e2=langfiles(SM+"/mods/Watcher/Watcher.pck","esp")
    out(f"INSTALADO Watcher: esp={sum(len(v) for v in e2.values())} claves; watcherFeminized: arte copiado")
    out("WATCHER MAIN VALIDACION OK")
