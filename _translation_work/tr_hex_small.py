# -*- coding: utf-8 -*-
import json, os, glob, sys
M = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/pendientes/HextechRunes"
TR = {
 # keystone_runes_ui
 "Choose A Hextech Rune":"Elige una Runa Hextech",
 "Offense":"Ofensa","Defense":"Defensa","Engine":"Motor","Utility":"Utilidad","Anomaly":"Anomalía",
 # modifiers
 "Hextech Mayhem":"Caos Hextech",
 "At the start of Acts [blue]1[/blue], [blue]2[/blue], and [blue]3[/blue], choose Hextech runes and give monsters of that Act a Hextech bonus of the same rarity.":
   "Al inicio de los Actos [blue]1[/blue], [blue]2[/blue] y [blue]3[/blue], elige runas Hextech y otorga a los monstruos de ese Acto una bonificación Hextech de la misma rareza.",
 "Silver Run":"Partida de Plata","All Hextech runes refreshed this run are Silver tier.":"Todas las runas Hextech generadas en esta partida son de nivel Plata.",
 "Gold Run":"Partida de Oro","All Hextech runes refreshed this run are Gold tier.":"Todas las runas Hextech generadas en esta partida son de nivel Oro.",
 "Prismatic Run":"Partida Prismática","All Hextech runes refreshed this run are Prismatic tier.":"Todas las runas Hextech generadas en esta partida son de nivel Prismático.",
 # relic_collection
 "[gold]Hextech:[/gold] Custom relics from the Hextech rune pool.":"[gold]Hextech:[/gold] Reliquias personalizadas del repertorio de runas Hextech.",
 "[gold]Stat Forgers:[/gold] Custom relics from the stat forging system.":"[gold]Forjadores de Estadísticas:[/gold] Reliquias personalizadas del sistema de forja de estadísticas.",
 "[gold]Ironclad Hexes:[/gold] Hextech runes only available to Ironclad.":"[gold]Hexes de Ironclad:[/gold] Runas Hextech disponibles solo para Ironclad.",
 "[gold]Silent Hexes:[/gold] Hextech runes only available to Silent.":"[gold]Hexes de Silent:[/gold] Runas Hextech disponibles solo para Silent.",
 "[gold]Regent Hexes:[/gold] Hextech runes only available to Regent.":"[gold]Hexes de Regent:[/gold] Runas Hextech disponibles solo para Regent.",
 "[gold]Defect Hexes:[/gold] Hextech runes only available to Defect.":"[gold]Hexes de Defect:[/gold] Runas Hextech disponibles solo para Defect.",
 "[gold]Necrobinder Hexes:[/gold] Hextech runes only available to Necrobinder.":"[gold]Hexes de Necrobinder:[/gold] Runas Hextech disponibles solo para Necrobinder.",
 "Waiting for other players to choose...":"Esperando a que los demás jugadores elijan...",
 "Current Tier: {0}":"Nivel actual: {0}",
 "Enemy Hex This Act":"Hex enemigo de este Acto",
 "Remove":"Quitar","Undo":"Deshacer",
 "No Enemy Hex":"Sin Hex enemigo",
 "No new enemy hex will be added for this act.":"No se añadirá ningún hex enemigo nuevo para este acto.",
 "Silver":"Plata","Prismatic":"Prismático",
 "Generic":"Genérico","Ironclad":"Ironclad","Silent":"Silent","Regent":"Regent","Necrobinder":"Necrobinder","Defect":"Defect",
 "Damage":"Daño","Survival":"Supervivencia","Scaling":"Escalado","Economy":"Economía","Draw":"Robo","Resource":"Recurso",
 "Hybrid":"Híbrido","Blood":"Sangre","Trick":"Truco","Sword":"Espada","Starlight":"Luz Estelar","Colorless":"Incoloro","Orb":"Orbe",
 # powers (dragon souls + utilidades)
 "At the start of this creature's turn, lose HP equal to this amount percent of its current HP, with a minimum equal to this amount. Then Burn is reduced by [blue]10%[/blue].":
   "Al inicio del turno de esta criatura, pierde PV iguales a ese porcentaje de sus PV actuales, con un mínimo igual a esa cantidad. Luego la Quemadura se reduce en [blue]10%[/blue].",
 "At the start of this creature's turn, lose [blue]{Amount}%[/blue] of its current HP, with a minimum of [blue]{Amount}[/blue] HP. Then Burn is reduced by [blue]10%[/blue].":
   "Al inicio del turno de esta criatura, pierde [blue]{Amount}%[/blue] de sus PV actuales, con un mínimo de [blue]{Amount}[/blue] PV. Luego la Quemadura se reduce en [blue]10%[/blue].",
 "Trick Magic":"Magia de Trucos",
 "The next Attack played is replayed a number of times equal to this amount.":"El próximo Ataque jugado se repite un número de veces igual a esa cantidad.",
 "The next Attack played is replayed [blue]{Amount}[/blue] time(s).":"El próximo Ataque jugado se repite [blue]{Amount}[/blue] vez(veces).",
 "Ocean Dragon Soul":"Alma de Dragón Oceánico",
 "At the end of your turn, heal HP equal to this amount.":"Al final de tu turno, recuperas PV iguales a esa cantidad.",
 "At the end of this creature's turn, heal [blue]{Amount}[/blue] HP.":"Al final del turno de esta criatura, recupera [blue]{Amount}[/blue] PV.",
 "Infernal Dragon Soul":"Alma de Dragón Infernal",
 "The first Attack you play each turn applies [gold]Burn[/gold] equal to this amount to enemies.":"El primer Ataque que juegas cada turno aplica [gold]Quemadura[/gold] igual a esa cantidad a los enemigos.",
 "The first Attack played each turn applies [blue]{Amount}[/blue] [gold]Burn[/gold] to enemies.":"El primer Ataque jugado cada turno aplica [blue]{Amount}[/blue] de [gold]Quemadura[/gold] a los enemigos.",
 "Hextech Dragon Soul":"Alma de Dragón Hextech",
 "Gain extra Energy equal to this amount each turn.":"Obtienes energía extra igual a esa cantidad cada turno.",
 "Gain [blue]{Amount}[/blue] extra Energy each turn.":"Obtienes [blue]{Amount}[/blue] de energía extra cada turno.",
 "Mountain Dragon Soul":"Alma de Dragón de Montaña",
 "At the start of your turn, gain [gold]Plating[/gold] equal to this amount.":"Al inicio de tu turno, obtienes [gold]Blindaje[/gold] igual a esa cantidad.",
 "At the start of this creature's turn, gain [blue]{Amount}[/blue] [gold]Plating[/gold].":"Al inicio del turno de esta criatura, obtiene [blue]{Amount}[/blue] de [gold]Blindaje[/gold].",
 "Chemtech Dragon Soul":"Alma de Dragón Quimtech",
 "At the start of your turn, obtain random Potions equal to this amount.":"Al inicio de tu turno, obtienes pociones al azar iguales a esa cantidad.",
 "At the start of this creature's turn, obtain [blue]{Amount}[/blue] random Potion(s).":"Al inicio del turno de esta criatura, obtiene [blue]{Amount}[/blue] poción(es) al azar.",
 "Cloud Dragon Soul":"Alma de Dragón de Nube",
 "Draw extra cards equal to this amount each turn.":"Robas cartas extra iguales a esa cantidad cada turno.",
 "Draw [blue]{Amount}[/blue] extra card(s) each turn.":"Robas [blue]{Amount}[/blue] carta(s) extra cada turno.",
 "Whenever you play a card, deal [blue]3[/blue] damage to a random enemy.":"Cada vez que juegas una carta, infliges [blue]3[/blue] de daño a un enemigo al azar.",
 "At the start of your turn, gain [blue]1[/blue] [gold]Strength[/gold].":"Al inicio de tu turno, obtienes [blue]1[/blue] de [gold]fuerza[/gold].",
 # cards
 "Elicit":"Provocar",
 "Evoke all of your Orbs.":"Evoca todos tus Orbes.",
 "Let every coil discharge at once.":"Que cada bobina se descargue a la vez.",
 "Draw [blue]{Cards}[/blue] cards. Gain [blue]{BufferPower}[/blue] [gold]Buffer[/gold]. The next Attack you play is replayed [blue]{Replays}[/blue] time(s).":
   "Roba [blue]{Cards}[/blue] cartas. Obtienes [blue]{BufferPower}[/blue] de [gold]Amortiguador[/gold]. El próximo Ataque que juegas se repite [blue]{Replays}[/blue] vez(veces).",
 "The audience sees ribbons. The enemy sees the bill.":"El público ve cintas. El enemigo ve la factura.",
 "Blade Waltz":"Vals de Cuchillas",
 "Deal {Damage:diff()} damage to random enemies [blue]{Hits}[/blue] times. Gain [blue]{IntangiblePower}[/blue] [gold]Intangible[/gold].":
   "Infliges {Damage:diff()} de daño a enemigos al azar [blue]{Hits}[/blue] veces. Obtienes [blue]{IntangiblePower}[/blue] de [gold]intangibilidad[/gold].",
 "Spin, cut, bow.":"Gira, corta, reverencia.",
 "Catalyst":"Catalizador",
 "Set an enemy's Poison to [blue]{PoisonMultiplier}[/blue] times its current amount.":"Fija el veneno de un enemigo en [blue]{PoisonMultiplier}[/blue] veces su cantidad actual.",
 "If the toxin is still breathing, it can still grow.":"Si la toxina aún respira, aún puede crecer.",
 "At the end of your turn, heal [blue]{Heal}[/blue] HP.":"Al final de tu turno, recuperas [blue]{Heal}[/blue] PV.",
 "The tide always remembers the way back.":"La marea siempre recuerda el camino de vuelta.",
 "The first Attack you play each turn applies [blue]{BurnPower}[/blue] [gold]Burn[/gold] to enemies.":"El primer Ataque que juegas cada turno aplica [blue]{BurnPower}[/blue] de [gold]Quemadura[/gold] a los enemigos.",
 "The first strike lights the whole fight.":"El primer golpe enciende toda la pelea.",
 "Gain [blue]{Energy}[/blue] extra Energy each turn.":"Obtienes [blue]{Energy}[/blue] de energía extra cada turno.",
 "Lightning in the coil never sleeps.":"El rayo en la bobina nunca duerme.",
 "At the start of your turn, gain [blue]{PlatingPower}[/blue] [gold]Plating[/gold].":"Al inicio de tu turno, obtienes [blue]{PlatingPower}[/blue] de [gold]Blindaje[/gold].",
 "The mountain does not retreat.":"La montaña no retrocede.",
 "At the start of your turn, obtain [blue]{PotionCount}[/blue] random Potion.":"Al inicio de tu turno, obtienes [blue]{PotionCount}[/blue] poción al azar.",
 "No one knows the answer before the cork pops.":"Nadie sabe la respuesta antes de que salte el corcho.",
 "Draw [blue]{Cards}[/blue] extra cards each turn.":"Robas [blue]{Cards}[/blue] cartas extra cada turno.",
 "The wind puts choices in your hand.":"El viento pone opciones en tu mano.",
 "All In":"A Todo o Nada",
 "Deal {Damage:diff()} damage.\nDiscard all non-Attack cards.":"Infliges {Damage:diff()} de daño.\nDescarta todas las cartas que no sean de Ataque.",
 "Only the wager and the edge remain on the table.":"Sobre la mesa solo quedan la apuesta y el filo.",
 "White Hole":"Agujero Blanco",
 "Whenever you draw this, gain {Energy:energyIcons()}.\nDraw {Cards} cards.":"Cada vez que robas esta carta, obtienes {Energy:energyIcons()}.\nRoba {Cards} cartas.",
 "It does not swallow choices. It spits them back into your hand.":"No se traga las opciones. Las escupe de vuelta a tu mano.",
 "Searing Attack":"Ataque Abrasador",
 "Deal {Damage:diff()} damage. Can be upgraded any number of times.":"Infliges {Damage:diff()} de daño. Puede mejorarse cualquier número de veces.",
 "Hotter with each edge.":"Más caliente con cada filo.",
 "Osty's Wish":"El Deseo de Puro Hueso",
 "Gain {WishBlock} Block.\nDeal {WishDamage} damage to all enemies.":"Obtienes {WishBlock} de bloqueo.\nInfliges {WishDamage} de daño a todos los enemigos.",
 "[blue]0[/blue]-cost Skill. Gain [blue]X[/blue] Block and deal [blue]X[/blue] damage to all enemies. [blue]X[/blue] is Osty's Max HP when it died. Exhaust. Upgraded copies retain.":
   "Habilidad de coste [blue]0[/blue]. Obtienes [blue]X[/blue] de bloqueo e infliges [blue]X[/blue] de daño a todos los enemigos. [blue]X[/blue] son los PV máx. de Puro Hueso cuando murió. Se agota. Las copias mejoradas se retienen.",
 "This time, Osty leaves the ending in your hands.":"Esta vez, Puro Hueso deja el final en tus manos.",
 "Choose any number of cards to discard.":"Elige cualquier número de cartas para descartar.",
}
miss=set()
for fn in ("keystone_runes_ui.json","modifiers.json","relic_collection.json","powers.json","cards.json"):
    p=os.path.join(M,"esp",fn); src=json.load(open(os.path.join(M,"src",fn),encoding="utf-8-sig")); d=json.load(open(p,encoding="utf-8-sig"))
    for k,v in src.items():
        if isinstance(v,str) and v.strip() and d.get(k)==v:
            if v in TR: d[k]=TR[v]
            else: miss.add(v)
    json.dump(d, open(p,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
if miss:
    sys.stdout.buffer.write(b"FALTAN:\n")
    for m in sorted(miss): sys.stdout.buffer.write(("  "+repr(m)+"\n").encode())
else: print("HextechRunes pequenos: todo traducido por valor")
