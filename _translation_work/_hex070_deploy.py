# -*- coding: utf-8 -*-
# Actualiza HextechRunes a v0.7.0: 公开版 -> main set, beta版 -> beta set. Reusa esp 0.6.7 + traduce 15 nuevas + 3 cambiadas.
import importlib.util,os,sys,glob,json,re,shutil,io,contextlib
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SMR=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2"
SM=SMR+"/mods"; B="_translation_work/beta_dl/_new2"; BS=chr(92)
def lf(pck,lang):
    with open(pck,"rb") as f:
        ents,h=pt.read_dir(f); fb=h[5]; d={}
        for e in ents:
            p=e['path'].replace(BS,'/')
            if f"/localization/{lang}/" in p and p.endswith('.json'):
                f.seek(e['off']+fb); d[os.path.basename(p)]=json.loads(f.read(e['size']))
    return d
esp_old=lf(glob.glob(f"{SM}/HextechRunes/*.pck")[0],"esp")
T={
"Upgrade: Demon Form":"Mejora: Forma Demoníaca",
"Your [gold]Demon Form[/gold] gains: at the start of your turn, heal HP equal to its amount.":"Tu [gold]Forma Demoníaca[/gold] gana: al inicio de tu turno, cura PV igual a su cantidad.",
"The demon takes strength, then pays some blood back.":"El demonio toma fuerza, y luego paga algo de sangre.",
"Upgrade: Echo Form":"Mejora: Forma de Eco",
"Your [gold]Echo Form[/gold] plays cards three times.":"Tu [gold]Forma de Eco[/gold] juega las cartas tres veces.",
"By the third echo, it sounds like an order.":"Para el tercer eco, suena como una orden.",
"Upgrade: Reaper Form":"Mejora: Forma de Segador",
"Your [gold]Reaper Form[/gold] gains: whenever your attack deals damage, apply [blue]2[/blue] [gold]Doom[/gold] to the target.":"Tu [gold]Forma de Segador[/gold] gana: cada vez que tu ataque inflige daño, aplica [blue]2[/blue] de [gold]Perdición[/gold] al objetivo.",
"When the scythe falls, the countdown starts.":"Cuando cae la guadaña, empieza la cuenta regresiva.",
"Upgrade: Void Form":"Mejora: Forma del Vacío",
"Playing [gold]Void Form[/gold] no longer ends your turn.":"Jugar [gold]Forma del Vacío[/gold] ya no termina tu turno.",
"You fall into the void and keep one hand on your cards.":"Caes en el vacío y mantienes una mano sobre tus cartas.",
"Archmage":"Archimago",
"Whenever you play a Skill, there is a [blue]33%[/blue] chance to make [blue]1[/blue] random card in your hand free this turn.":"Cada vez que juegas una Habilidad, hay [blue]33%[/blue] de probabilidad de hacer gratis [blue]1[/blue] carta al azar de tu mano este turno.",
"A true archmage never pays the cost directly.":"Un verdadero archimago nunca paga el coste directamente.",
# reusadas que cambiaron en 0.7.0:
"At the start of your turn, gain [blue]1[/blue] [gold]Echo Form[/gold].":"Al inicio de tu turno, obtienes [blue]1[/blue] de [gold]Forma de Eco[/gold].",
"Your [gold]Reanimate[/gold] costs [blue]1[/blue] less. Whenever any creature dies, it costs [blue]1[/blue] less this combat.":"Tu [gold]Reanimar[/gold] cuesta [blue]1[/blue] menos. Cada vez que muere una criatura, cuesta [blue]1[/blue] menos este combate.",
"Your [gold]Serpent Form[/gold] gains: each card you draw triggers [blue]1[/blue] hit, dealing damage equal to its amount to a random enemy.":"Tu [gold]Forma de Serpiente[/gold] gana: cada carta que robas activa [blue]1[/blue] golpe, infligiendo daño igual a su cantidad a un enemigo al azar.",
}
TAGS=["gold","blue","red","purple","sine","pink","img","jitter","orange"]; TOK=re.compile(r"\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\([0-9]*\))?\}")
def build_and_deploy(label, srcpck, dst_set, dst_repo):
    eng=lf(srcpck,"eng")
    stg=f"{B}/_esp_hex070/HextechRunes/localization/esp"
    if os.path.isdir(f"{B}/_esp_hex070"): shutil.rmtree(f"{B}/_esp_hex070")
    os.makedirs(stg,exist_ok=True)
    prob=0; miss=[]
    for fn,d in eng.items():
        o={}
        eo=esp_old.get(fn,{})
        for k,v in d.items():
            if isinstance(v,str) and v in T: es=T[v]
            elif k in eo: es=eo[k]
            else: miss.append(f"{fn}:{k}"); es=v
            o[k]=es
            if isinstance(v,str):
                for t in TAGS:
                    if v.count(f"[{t}]")!=es.count(f"[{t}]"): out(f"  [{label}/{fn}] {k}: tag[{t}]"); prob+=1
                if v.count("{")!=es.count("{") or sorted(TOK.findall(v))!=sorted(TOK.findall(es)) or v.count(chr(10))!=es.count(chr(10)): out(f"  [{label}/{fn}] {k}: tok/llaves/saltos"); prob+=1
        json.dump(o,open(f"{stg}/{fn}","w",encoding="utf-8"),ensure_ascii=False,indent=2)
    if miss: out(f"  [{label}] SIN TRADUCIR {len(miss)}: {miss[:10]}"); prob+=len(miss)
    if prob: out(f"[{label}] PROBLEMAS={prob} -> NO desplegado"); return False
    new=f"{B}/_new_hex070_{label}.pck"
    with contextlib.redirect_stdout(io.StringIO()):
        pt.cmd_repack(srcpck,new,f"{B}/_esp_hex070")
    sdir=os.path.dirname(srcpck)
    for dst in [dst_set,dst_repo]:
        os.makedirs(dst,exist_ok=True)
        for fx in os.listdir(sdir):
            if fx.endswith((".dll",".json")): shutil.copy(os.path.join(sdir,fx),dst)
        shutil.copy(new,os.path.join(dst,"HextechRunes.pck"))
    os.remove(new)
    import hashlib
    md5=hashlib.md5(open(f"{dst_set}/HextechRunes.dll","rb").read()).hexdigest()[:12]
    e2=lf(f"{dst_set}/HextechRunes.pck","esp")
    out(f"[{label}] OK ✓ dll={md5} esp={sum(len(v) for v in e2.values())} -> {dst_set} + {dst_repo}")
    return True

pub=glob.glob(f"{B}/Hex070_pub/**/HextechRunes.pck",recursive=True)[0]
beta=glob.glob(f"{B}/Hex070_beta/**/HextechRunes.pck",recursive=True)[0]
build_and_deploy("MAIN(公开版)", pub, f"{SM}/HextechRunes", "Traducidos/HextechRunes")
build_and_deploy("BETA(beta版)", beta, f"{SMR}/mods_beta_test/HextechRunes", "Traducidos_beta/HextechRunes")
