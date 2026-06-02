# -*- coding: utf-8 -*-
# Actualiza HextechRunes a v0.6.7 beta: reusa esp de 0.6.6 + traduce las 73 claves nuevas, valida y despliega.
import importlib.util,os,sys,glob,json,re,shutil,io,contextlib
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
BS=chr(92)
def lf(pck,lang):
    with open(pck,"rb") as f:
        ents,h=pt.read_dir(f); fb=h[5]; d={}
        for e in ents:
            p=e['path'].replace(BS,'/')
            if f"/localization/{lang}/" in p and p.endswith('.json'):
                f.seek(e['off']+fb); d[os.path.basename(p)]=json.loads(f.read(e['size']))
    return d
new_pck=glob.glob("_translation_work/beta_dl/_watcher_beta/HexBeta/**/*.pck",recursive=True)[0]
new_dir=os.path.dirname(new_pck)
old_pck=glob.glob(f"{SM}/HextechRunes/*.pck")[0]
eng=lf(new_pck,"eng"); esp_old=lf(old_pck,"esp")

# traducciones de las 73 claves nuevas, por VALOR ingles (los pares camel/UPPER comparten valor)
T={
"Dice Maniac":"Maníaco de los Dados",
"After winning combat, there is a [blue]50%[/blue] chance to drop a random stat forger. Gold and Prismatic stat forgers are twice as likely to appear.":"Tras ganar un combate, hay [blue]50%[/blue] de probabilidad de soltar un forjador de estadísticas al azar. Los forjadores de estadísticas Dorados y Prismáticos tienen el doble de probabilidad de aparecer.",
"Sponsor item: Before the dice stop rolling, the prize is already waiting by the forge.":"Objeto patrocinado: Antes de que los dados dejen de rodar, el premio ya espera junto a la forja.",
"Bread Sandwich":"Sándwich de Pan",
"Every card you play is replayed [blue]1[/blue] time.":"Cada carta que juegas se repite [blue]1[/blue] vez.",
"People loudly demanded more fillings, and you quietly said no.":"La gente exigía a gritos más relleno, y en silencio dijiste que no.",
"Upgrade: Juggernaut":"Mejora: Juggernaut",
"Your [gold]Juggernaut[/gold] hits all enemies.":"Tu [gold]Juggernaut[/gold] golpea a todos los enemigos.",
"When the wall falls, every enemy hears it.":"Cuando el muro cae, todos los enemigos lo oyen.",
"Upgrade: Tyranny":"Mejora: Tiranía",
"At the start of your turn, for each [blue]1[/blue] [gold]Tyranny[/gold], add [blue]1[/blue] Ethereal [gold]Debris[/gold] to your hand.":"Al inicio de tu turno, por cada [blue]1[/blue] de [gold]Tiranía[/gold], añade [blue]1[/blue] [gold]Escombro[/gold] Etéreo a tu mano.",
"Every layer of pressure leaves fragments behind.":"Cada capa de presión deja fragmentos atrás.",
"Upgrade: Reanimate":"Mejora: Reanimar",
"Whenever any creature dies, your [gold]Reanimate[/gold] summons [blue]5[/blue] more.":"Cada vez que muere una criatura, tu [gold]Reanimar[/gold] invoca [blue]5[/blue] más.",
"The louder death rings, the deeper the call.":"Cuanto más fuerte suena la muerte, más profundo es el llamado.",
"Upgrade: Hidden Gem":"Mejora: Gema Oculta",
"Your [gold]Hidden Gem[/gold] can add [gold]Replay[/gold] to cards that already have [gold]Replay[/gold].":"Tu [gold]Gema Oculta[/gold] puede añadir [gold]Repetición[/gold] a cartas que ya tienen [gold]Repetición[/gold].",
"A gem can keep finding new faces.":"Una gema puede seguir encontrando nuevas caras.",
"Upgrade: Automation":"Mejora: Automatización",
"Your [gold]Automation[/gold] becomes: every [blue]10[/blue] cards you draw, add [blue]1[/blue] [gold]Fuel[/gold] to your hand.":"Tu [gold]Automatización[/gold] se vuelve: cada [blue]10[/blue] cartas que robas, añade [blue]1[/blue] de [gold]Combustible[/gold] a tu mano.",
"The old machine stops sparking and starts supplying.":"La vieja máquina deja de chispear y empieza a abastecer.",
"Upgrade: Voltaic":"Mejora: Voltaico",
"Your [gold]Voltaic[/gold] records and channels every Orb type.":"Tu [gold]Voltaico[/gold] registra y canaliza cada tipo de Orbe.",
"The current remembers every path it took.":"La corriente recuerda cada camino que tomó.",
"Vampire Crawler":"Reptador Vampírico",
"Power cards you play go to your discard pile.":"Las cartas de Poder que juegas van a tu pila de descarte.",
"A spell lands, then crawls back to the scrap.":"Un hechizo impacta, luego repta de vuelta a la chatarra.",
"Upgrade: Serpent Form":"Mejora: Forma de Serpiente",
"Your [gold]Serpent Form[/gold] gains: whenever you draw a card, deal damage equal to its amount to a random enemy.":"Tu [gold]Forma de Serpiente[/gold] gana: cada vez que robas una carta, inflige daño igual a su cantidad a un enemigo al azar.",
"There is a snake-shadow in every draw.":"Hay una sombra de serpiente en cada robo.",
"Solid Time":"Tiempo Sólido",
"When you play a Power card from your deck, remove it from your deck. At the start of combat, trigger all removed cards.":"Cuando juegas una carta de Poder desde tu mazo, quítala de tu mazo. Al inicio del combate, activa todas las cartas quitadas.",
"Solidified Power Cards":"Cartas de Poder Solidificadas",
"Sponsor item: Time hardens, and old spells echo each fight.":"Objeto patrocinado: El tiempo se endurece, y los viejos hechizos resuenan en cada pelea.",
"Reforged Helmet":"Yelmo Reforjado",
"[gold]Strength[/gold] you gain during combat is doubled.":"La [gold]fuerza[/gold] que ganas durante el combate se duplica.",
"The old helm is reforged, and every roar gains an echo.":"El viejo yelmo se reforja, y cada rugido gana un eco.",
# clave reescrita en 0.6.7 (el esp viejo quedo obsoleto):
"At the start of combat, gain [blue]2[/blue] [gold]Strength[/gold] and [blue]2[/blue] [gold]Dexterity[/gold]. When you die, revive at [blue]30%[/blue] HP, draw until your hand is full, make all cards cost [blue]0[/blue] this turn, apply [blue]2[/blue] [gold]Weak[/gold] and [gold]Vulnerable[/gold] to all enemies, and gain [blue]1[/blue] [gold]Intangible[/gold]. Can revive up to [blue]7[/blue] times per run.":"Al inicio del combate, obtienes [blue]2[/blue] de [gold]fuerza[/gold] y [blue]2[/blue] de [gold]Destreza[/gold]. Cuando mueres, revives con [blue]30%[/blue] de PV, robas hasta llenar tu mano, todas las cartas cuestan [blue]0[/blue] este turno, aplicas [blue]2[/blue] de [gold]Débil[/gold] y [gold]Vulnerable[/gold] a todos los enemigos, y obtienes [blue]1[/blue] de [gold]Intangible[/gold]. Puede revivir hasta [blue]7[/blue] veces por partida.",
}

stg="_translation_work/beta_dl/_esp_HexBeta/HextechRunes/localization/esp"; os.makedirs(stg,exist_ok=True)
TAGS=["gold","blue","red","purple","sine","pink","img","jitter","orange"]; TOK=re.compile(r"\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\([0-9]*\))?\}")
miss=[]; prob=0
for fn,d in eng.items():
    o={}
    eo=esp_old.get(fn,{})
    for k,v in d.items():
        if v in T: es=T[v]            # por VALOR primero: corrige claves reescritas entre versiones
        elif k in eo: es=eo[k]
        else: miss.append(f"{fn}:{k}"); es=v
        o[k]=es
        if isinstance(v,str):
            for t in TAGS:
                if v.count(f"[{t}]")!=es.count(f"[{t}]"): out(f"  [{fn}] {k}: tag[{t}] {es.count(f'[{t}]')}!={v.count(f'[{t}]')}"); prob+=1
            if v.count("{")!=es.count("{") or sorted(TOK.findall(v))!=sorted(TOK.findall(es)): out(f"  [{fn}] {k}: tokens/llaves"); prob+=1
            if v.count(chr(10))!=es.count(chr(10)): out(f"  [{fn}] {k}: saltos"); prob+=1
    json.dump(o,open(f"{stg}/{fn}","w",encoding="utf-8"),ensure_ascii=False,indent=2)
out(f"SIN TRADUCIR ({len(miss)}): {miss[:20]}")
out(f"PROBLEMAS={prob}")
if prob==0 and not miss:
    newp="_translation_work/beta_dl/_new_HexBeta.pck"
    with contextlib.redirect_stdout(io.StringIO()):
        pt.cmd_repack(new_pck,newp,"_translation_work/beta_dl/_esp_HexBeta")
    for dst in [f"{SM}/HextechRunes","Traducidos_beta/HextechRunes"]:
        os.makedirs(dst,exist_ok=True)
        for fx in os.listdir(new_dir):
            if fx.endswith((".dll",".json")): shutil.copy(os.path.join(new_dir,fx),dst)
        shutil.copy(newp,os.path.join(dst,os.path.basename(new_pck)))
    os.remove(newp)
    e2=lf(f"{SM}/HextechRunes/{os.path.basename(new_pck)}","esp")
    mj=glob.glob(f"{SM}/HextechRunes/*.json")
    ver=json.load(open(mj[0],encoding="utf-8-sig")).get("version") if mj else "?"
    out(f"HextechRunes: OK ✓ actualizado a v{ver}, esp={sum(len(v) for v in e2.values())} claves -> mods/ + Traducidos_beta/")
