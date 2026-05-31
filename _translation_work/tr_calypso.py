# -*- coding: utf-8 -*-
import json, os, glob, sys
M = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/pendientes/CalypsosHappyHour"
ESP = os.path.join(M, "esp")

# Traduccion por VALOR ingles -> esp (cubre las 3 copias de cada carta).
TR = {
 # --- card_keywords ---
 "Permaborrow X":"Permapréstamo X",
 "Gain up to X gold from one other teammate.":"Obtienes hasta X de oro de otro compañero.",
 "Crowdfund X":"Colecta X",
 "Gain up to X gold from each other teammate.":"Obtienes hasta X de oro de cada uno de los otros compañeros.",
 # --- titulos (memes se mantienen en ingles) ---
 "Venmo Me 50":"Venmo Me 50",
 "What the Dog Doin'?":"What the Dog Doin'?",
 "Bibi-Labu!":"Bibi-Labu!",
 "Art-i-fract":"Arte-facto",
 "Wanted!":"¡Se Busca!",
 "Trust Me, Bro":"Trust Me, Bro",
 "Clinging to You":"Aferrándome a Ti",
 "Protecting You":"Protegiéndote",
 "Expecting You":"Esperándote",
 "Spoiling You":"Consintiéndote",
 "Infesting You":"Infestándote",
 "Let Me Cook!":"Let Me Cook!",
 "Stop Yapping!":"Stop Yapping!",
 "Hell is Others":"El Infierno son los Otros",
 "Goo Goo Ga Ga":"Goo Goo Ga Ga",
 "I'll Drop You":"Te Voy a Soltar",
 "Iron Sharpens Iron":"Hierro Afila Hierro",
 "Banecode Art":"Banecode Art",
 "Hardened Together":"Endurecidos Juntos",
 "Yummy Drumstick":"Muslito Rico",
 "Beefy Square":"Cuadrado de Carne",
 "Chicken Burger":"Hamburguesa de Pollo",
 "Lil' Nuggets":"Nuggetcitos",
 "Pell's Egg Tart":"Tarta de Huevo de Pell",
 "Sus Purple Drink":"Bebida Morada Sus",
 "Short Circuit":"Cortocircuito",
 "Trauma Team":"Equipo de Trauma",
 "Networking":"Networking",
 "Hired Muscle":"Matón a Sueldo",
 "Friendship Tax":"Impuesto de la Amistad",
 "Bundled Deal":"Paquete Combo",
 "Royal Tribute":"Tributo Real",
 "Paid Update":"Actualización de Pago",
 "Gold Bounty":"Recompensa de Oro",
 "Head Chef":"Chef Principal",
 "Mutual Aid":"Ayuda Mutua",
 "Gold Transfer":"Transferencia de Oro",
 # --- descripciones ---
 "[gold]Permaborrow {Gold:diff()}[/gold]. Shuffle {Cards:diff()} random fast-food cards into your teammate's draw pile.":
   "[gold]Permapréstamo {Gold:diff()}[/gold]. Baraja {Cards:diff()} cartas de comida rápida al azar en la pila de robo de tu compañero.",
 "Deal damage to a random enemy equal to another teammate's Block.":
   "Inflige a un enemigo al azar daño igual al bloqueo de otro compañero.",
 "Deal {Damage:diff()} damage. Shuffle {Cards:diff()} copies of this card into your teammates' draw piles at random.":
   "Inflige {Damage:diff()} de daño. Baraja {Cards:diff()} copias de esta carta en las pilas de robo de tus compañeros al azar.",
 "Draw {Cards:diff()} card. Remove all Artifact from all enemies. For each stack removed, all players gain 1 Strength.":
   "Roba {Cards:diff()} carta. Elimina todo el Artefacto de todos los enemigos. Por cada acumulación eliminada, todos los jugadores obtienen 1 de fuerza.",
 "Apply {Gold:diff()} Gold Bounty to an enemy.":
   "Aplica {Gold:diff()} de Recompensa de Oro a un enemigo.",
 "Apply 10 Strength and 10 Dexterity to an enemy. Apply Gold Bounty equal to that enemy's current HP/10.":
   "Aplica 10 de fuerza y 10 de destreza a un enemigo. Aplica Recompensa de Oro igual a los PV actuales de ese enemigo/10.",
 "Another teammate loses all Block. For every 5 Block removed, you gain 1 Strength.":
   "Otro compañero pierde todo su bloqueo. Por cada 5 de bloqueo eliminado, obtienes 1 de fuerza.",
 "You and an ally each gain {Block:diff()} Block.":
   "Tú y un aliado obtienen {Block:diff()} de bloqueo cada uno.",
 "Another player draws {Cards:diff()} card.":
   "Otro jugador roba {Cards:diff()} carta.",
 "Transfer up to {Gold:diff()} of your gold to a teammate.":
   "Transfiere hasta {Gold:diff()} de tu oro a un compañero.",
 "Another player gains {IntangiblePower:diff()} Intangible. Put {Cards:diff()} Infection into their draw pile.":
   "Otro jugador obtiene {IntangiblePower:diff()} de intangibilidad. Pon {Cards:diff()} Infección en su pila de robo.",
 "This turn, for every 3 cards you play, restore 1 Energy to all teammates at 0 Energy, and put 2 Stop Yapping! into their hands.":
   "Este turno, por cada 3 cartas que juegas, restaura 1 de energía a todos los compañeros con 0 de energía, y pon 2 Stop Yapping! en sus manos.",
 "Another teammate loses {HpLoss:diff()} HP. You and they gain {StrengthPower:diff()} Strength.":
   "Otro compañero pierde {HpLoss:diff()} PV. Tú y él obtienen {StrengthPower:diff()} de fuerza.",
 "Transform attacks in another teammate's hand into {IfUpgraded:show:Giant Rock+|Giant Rock}.":
   "Transforma los ataques en la mano de otro compañero en {IfUpgraded:show:Roca Gigante+|Roca Gigante}.",
 "Forge {Forge:diff()}. If you have a Sovereign Blade in hand, shuffle a copy of it into your teammate's draw pile.":
   "Forja {Forge:diff()}. Si tienes una Hoja Soberana en la mano, baraja una copia de ella en la pila de robo de tu compañero.",
 "Give another teammate {Cards:diff()} {IfUpgraded:show:Shiv+|Shiv}. You and they gain {AccuracyPower:diff()} Accuracy.":
   "Dale a otro compañero {Cards:diff()} {IfUpgraded:show:Púa+|Púa}. Tú y él obtienen {AccuracyPower:diff()} de Precisión.",
 "Deal {HpLoss:diff()} HP loss to yourself X{IfUpgraded:show:+1} times. Each time, apply 20 Doom to all enemies. If your HP is ≤50%, apply an extra 20 Doom.":
   "Te infliges {HpLoss:diff()} de pérdida de PV a ti mismo X{IfUpgraded:show:+1} veces. Cada vez, aplica 20 de condena a todos los enemigos. Si tus PV son ≤50%, aplica 20 de condena extra.",
 "You and another ally each gain {Forge:diff()} Forge and {Block:diff()} Block.":
   "Tú y otro aliado obtienen {Forge:diff()} de Forja y {Block:diff()} de bloqueo cada uno.",
 "Gain {StrengthPower:diff()} Strength and {VigorPower:diff()} Vigor. Draw {Cards:diff()} card.":
   "Obtienes {StrengthPower:diff()} de fuerza y {VigorPower:diff()} de Vigor. Roba {Cards:diff()} carta.",
 "Gain {RegenPower:diff()} Regen. Draw {Cards:diff()} card.":
   "Obtienes {RegenPower:diff()} de Regeneración. Roba {Cards:diff()} carta.",
 "Gain {Block:diff()} Block, {StrengthPower:diff()} Strength, and {DexterityPower:diff()} Dexterity. Draw {Cards:diff()} card.":
   "Obtienes {Block:diff()} de bloqueo, {StrengthPower:diff()} de fuerza y {DexterityPower:diff()} de destreza. Roba {Cards:diff()} carta.",
 "Heal {Heal:diff()} HP. Draw {Cards:diff()} card.":
   "Recupera {Heal:diff()} PV. Roba {Cards:diff()} carta.",
 "Gain {Energy:diff()} Energy. Draw {Cards:diff()} card.":
   "Obtienes {Energy:diff()} de energía. Roba {Cards:diff()} carta.",
 "Apply {DoomPower:diff()} Doom to an enemy. Draw {Cards:diff()} card.":
   "Aplica {DoomPower:diff()} de condena a un enemigo. Roba {Cards:diff()} carta.",
 "All players gain {Energy:diff()} Energy.{IfUpgraded:show:| Put 1 Dazed into all players' draw piles.}":
   "Todos los jugadores obtienen {Energy:diff()} de energía.{IfUpgraded:show:| Pon 1 Aturdimiento en las pilas de robo de todos los jugadores.}",
 "[gold]Permaborrow {Gold:diff()}[/gold]. Heal that teammate for half the gold transferred.":
   "[gold]Permapréstamo {Gold:diff()}[/gold]. Cura a ese compañero por la mitad del oro transferido.",
 "[gold]Permaborrow {Gold:diff()}[/gold]. Shuffle 2 copies of this card into your teammate's draw pile. Draw {Cards:diff()} card.":
   "[gold]Permapréstamo {Gold:diff()}[/gold]. Baraja 2 copias de esta carta en la pila de robo de tu compañero. Roba {Cards:diff()} carta.",
 "[gold]Permaborrow {Gold:diff()}[/gold]. Gain {Block:diff()} Block. This turn, you take attacks that would hit that teammate.":
   "[gold]Permapréstamo {Gold:diff()}[/gold]. Obtienes {Block:diff()} de bloqueo. Este turno, recibes los ataques que golpearían a ese compañero.",
 "[gold]Permaborrow {Gold:diff()}[/gold]. Apply {Summon:diff()} Summon to them.":
   "[gold]Permapréstamo {Gold:diff()}[/gold]. Aplícales {Summon:diff()} de Invocación.",
 "[gold]Permaborrow {Gold:diff()}[/gold]. Put a {IfUpgraded:show:Shiv+, Adrenaline+, and Deadly Poison+|Shiv, Adrenaline, and Deadly Poison} into your teammate's hand.":
   "[gold]Permapréstamo {Gold:diff()}[/gold]. Pon una {IfUpgraded:show:Púa+, Adrenalina+ y Veneno Mortal+|Púa, Adrenalina y Veneno Mortal} en la mano de tu compañero.",
 "[gold]Crowdfund {Gold:diff()}[/gold]. Then they gain {Energy:diff()} Energy and draw {Cards:diff()} card.":
   "[gold]Colecta {Gold:diff()}[/gold]. Luego obtienen {Energy:diff()} de energía y roban {Cards:diff()} carta.",
 "[gold]Permaborrow {Gold:diff()}[/gold]. Add Orb slots until they have 3. Channel 1 Plasma, 1 Lightning, and 1 Frost for them.":
   "[gold]Permapréstamo {Gold:diff()}[/gold]. Agrega espacios de orbe hasta que tengan 3. Canaliza 1 Plasma, 1 Rayo y 1 Escarcha por ellos.",
 "Gain {Block:diff()} Block. Deal damage to a random enemy equal to another teammate's Block.":
   "Obtienes {Block:diff()} de bloqueo. Inflige a un enemigo al azar daño igual al bloqueo de otro compañero.",
 "Deal {Damage:diff()} damage. Shuffle 2 copies of this card into your teammates' draw piles at random.":
   "Inflige {Damage:diff()} de daño. Baraja 2 copias de esta carta en las pilas de robo de tus compañeros al azar.",
 "Apply 6 Ritual, 6 Slippery, and 6 Regen to an enemy. Apply Gold Bounty equal to that enemy's current HP/3.{IfUpgraded:show:\nApply all effects again.}":
   "Aplica 6 de Ritual, 6 de Escurridizo y 6 de Regeneración a un enemigo. Aplica Recompensa de Oro igual a los PV actuales de ese enemigo/3.{IfUpgraded:show:\nAplica todos los efectos de nuevo.}",
 "When this creature dies, the killer gains {Amount} gold. If there is no damage source, the bounty is split among all players.":
   "Cuando esta criatura muere, quien la mata obtiene {Amount} de oro. Si no hay fuente de daño, la recompensa se reparte entre todos los jugadores.",
 # --- rest_site ---
 "You and {HasTarget:{Name}|another player} each heal for 15% of your respective Max HP{HasTarget: ({Heal})|}.":
   "Tú y {HasTarget:{Name}|otro jugador} se curan cada uno el 15% de sus PV máx. respectivos{HasTarget: ({Heal})|}.",
 "Transfer 50% of your gold{HasTarget: ({Gold})| } to {HasTarget:{Name}|a teammate}.":
   "Transfiere el 50% de tu oro{HasTarget: ({Gold})| } a {HasTarget:{Name}|un compañero}.",
 "[red]You have no gold to transfer.[/red]":"[red]No tienes oro para transferir.[/red]",
 "[red]Your teammates are too sticky to receive gold.[/red]":"[red]Tus compañeros están demasiado pegajosos para recibir oro.[/red]",
 # --- combat_messages ---
 "Something sticky is preventing me from gaining gold...":"Algo pegajoso me impide obtener oro...",
}

missing=set()
for fp in sorted(glob.glob(os.path.join(M,"src","*.json"))):
    fn=os.path.basename(fp); e=json.load(open(fp,encoding="utf-8-sig")); p=os.path.join(ESP,fn)
    d=json.load(open(p,encoding="utf-8-sig"))
    for k,v in e.items():
        if isinstance(v,str) and v.strip() and d.get(k)==v:
            if v in TR: d[k]=TR[v]
            else: missing.add(v)
    json.dump(d, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
if missing:
    sys.stdout.buffer.write(b"FALTAN traducciones:\n")
    for m in sorted(missing): sys.stdout.buffer.write(("  "+repr(m)+"\n").encode())
else:
    print("CalypsosHappyHour: todos los pendientes traducidos por valor")
