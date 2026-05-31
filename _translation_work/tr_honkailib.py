# -*- coding: utf-8 -*-
import json, os
M = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/honkai/HonkaiLib/esp"
def patch(fn, ov):
    p = os.path.join(M, fn); d = json.load(open(p, encoding="utf-8-sig")); d.update(ov)
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

patch("card_keywords.json", {
 "HONKAILIB-INSTANT.title":"Instantáneo",
 "HONKAILIB-INSTANT.description":"Cuando robas una carta con [gold]Instantáneo[/gold], se juega gratis.",
 "HONKAILIB-LINGER.title":"Persistencia",
 "HONKAILIB-LINGER.description":"Al final del turno, si la carta con [gold]Persistencia[/gold] sigue en tu mano, se activa su efecto de [gold]Persistencia[/gold] y se mueve a la [gold]pila de descarte[/gold]. Si esa carta también tiene [gold]Retención[/gold], tras activarse vuelve a la [gold]mano[/gold]. Si también tiene [gold]Vacío[/gold], en su lugar se [gold]Agota[/gold].",
 "HONKAILIB-OBLIVION.title":"Olvido",
 "HONKAILIB-OBLIVION.description":"Cuando una carta con [gold]Olvido[/gold] entra en la [gold]pila de agotamiento[/gold] al jugarse, en su lugar entra en la [gold]pila de descarte[/gold]. La carta con [gold]Olvido[/gold] se [gold]Transforma[/gold] en el [gold]Recuerdo[/gold] de la carta original.",
 "HONKAILIB-RECALL.title":"Rememoración",
 "HONKAILIB-RECALL.description":"[gold]Transforma[/gold] el [gold]Recuerdo[/gold] en la carta original. Cuando el [gold]Recuerdo[/gold] entra en la [gold]pila de agotamiento[/gold] al jugarse, en su lugar entra en la [gold]pila de descarte[/gold].",
 "HONKAILIB-IMPERIUM.title":"Decreto",
 "HONKAILIB-IMPERIUM.description":"Cuando una carta con [gold]Decreto[/gold] está en tu [gold]mano[/gold], no puedes jugar otras cartas que no tengan [gold]Decreto[/gold].",
 "HONKAILIB-PURGE.title":"Efímero",
 "HONKAILIB-PURGE.description":"Tras jugar una carta con [gold]Efímero[/gold], se elimina permanentemente del combate y del [gold]mazo[/gold].",
 "HONKAIFLAMECHASERS-UNLIMITED_UPGRADES.title":"Mejoras Ilimitadas",
 "HONKAIFLAMECHASERS-UNLIMITED_UPGRADES.description":"Las cartas con Mejoras Ilimitadas pueden [gold]mejorarse[/gold] infinitamente.",
})
patch("cards.json", {
 "HONKAILIB-FOLDER_DRAW_PILE.title":"Pila de robo",
 "HONKAILIB-FOLDER_DRAW_PILE.description":"Haz clic para ver las cartas de la [gold]pila de robo[/gold].",
 "HONKAILIB-FOLDER_HAND_PILE.title":"Mano",
 "HONKAILIB-FOLDER_HAND_PILE.description":"Haz clic para ver las cartas de la [gold]mano[/gold].",
 "HONKAILIB-FOLDER_DISCARD_PILE.title":"Pila de descarte",
 "HONKAILIB-FOLDER_DISCARD_PILE.description":"Haz clic para ver las cartas de la [gold]pila de descarte[/gold].",
 "HONKAILIB-FOLDER_EXHAUST_PILE.title":"Pila de agotamiento",
 "HONKAILIB-FOLDER_EXHAUST_PILE.description":"Haz clic para ver las cartas de la [gold]pila de agotamiento[/gold].",
 "HONKAILIB-OPTION_TRANSFORM.title":"Transformar",
 "HONKAILIB-OPTION_TRANSFORM.description":"Elige una carta para [gold]Transformar[/gold].",
 "HONKAILIB-OPTION_REMOVE.title":"Eliminar",
 "HONKAILIB-OPTION_REMOVE.description":"Elige una carta para [gold]Eliminar[/gold].",
 "HONKAILIB-MEMORY.title":"Recuerdo",
 "HONKAILIB-MEMORY.description":"[gold]Al jugarse[/gold] o por [gold]Persistencia[/gold]: [gold]Rememoración[/gold].",
 "HONKAILIB-FACTOR_EROSION.title":"Factor de Erosión",
 "HONKAILIB-FACTOR_EROSION.description":"Pierdes {HpLoss:diff()} PV; se [gold]Agota[/gold].\n[gold]Persistencia[/gold]: Obtienes {PoisonPower:diff()} de [gold]veneno[/gold].",
 "HONKAILIB-FACTOR_HYPER_MUTATION.title":"Factor de Hipermutación",
 "HONKAILIB-FACTOR_HYPER_MUTATION.description":"Pierdes {HpLoss:diff()} PV, obtienes permanentemente {MaxHp:diff()} PV máx.; se [gold]Agota[/gold].\n[gold]Persistencia[/gold]: Obtienes {PoisonPower:diff()} de [gold]veneno[/gold] y agregas una copia de esta carta a tu [gold]pila de descarte[/gold].",
})
patch("combat_messages.json", {
 "BLOCKED_BY_IMPERIUM":"¡Debo acatar el «[red]Decreto[/red]»!",
})
patch("powers.json", {
 "HONKAILIB-FLOW_POWER.title":"Circulación",
 "HONKAILIB-FLOW_POWER.description":"Tras jugar una carta, obtienes {energyPrefix:energyIcons(1)}, robas [blue]1[/blue] carta y luego reduces las acumulaciones de [gold]Circulación[/gold] en [blue]1[/blue].",
 "HONKAILIB-FLOW_POWER.smartDescription":"Después de jugar cartas [blue]{Amount}[/blue] veces, obtienes {Energy:energyIcons()} y robas [blue]{Cards}[/blue] cartas.",
 "HONKAILIB-BURN_POWER.title":"Calcinación",
 "HONKAILIB-BURN_POWER.description":"Cuando una criatura con [gold]Calcinación[/gold] recibe daño de ataque, recibe además daño igual al [blue]20%[/blue] de las acumulaciones. Al inicio de cada turno, recibe daño igual a la [blue]mitad[/blue] de las acumulaciones.\nCuando se activa [gold]Calcinación[/gold], las acumulaciones se reducen en [blue]10%[/blue] (al menos [blue]1[/blue]); si es un jugador, se agrega [blue]1[/blue] [gold]Quemadura[/gold] a su [gold]mano[/gold].",
 "HONKAILIB-BURN_POWER.smartDescription":"{BurnAttack:cond:>=1?Cuando {OnPlayer:tú recibes|este recibe} daño de ataque, recibe además [blue]{BurnAttack}[/blue] de daño de [gold]Calcinación[/gold].|}{BurnTurn:cond:>=1?Al inicio {OnPlayer:de tu turno|del turno de este}, recibe [blue]{BurnTurn}[/blue] de daño de [gold]Calcinación[/gold].\nCuando se activa [gold]Calcinación[/gold]|Cuando {OnPlayer:tú recibes|este recibe} daño de ataque o al inicio {OnPlayer:de tu turno|del turno de este}}, las acumulaciones se reducen en [blue]{BurnDecrement}[/blue]{OnPlayer:, se agrega [blue]1[/blue] [gold]Quemadura[/gold] a tu [gold]mano[/gold]|}.",
 "HONKAILIB-FROST_POWER.title":"Escarcha",
 "HONKAILIB-FROST_POWER.description":"El daño de ataque que inflige una criatura con [gold]Escarcha[/gold] se reduce: cuando las acumulaciones son mayores o iguales al [blue]100%[/blue]/[blue]50%[/blue]/[blue]25%[/blue] de sus PV actuales, se reduce en [blue]75%[/blue]/[blue]50%[/blue]/[blue]25%[/blue] respectivamente.\nAl inicio de cada turno, recibe daño igual al [blue]10%[/blue] de las acumulaciones, luego las acumulaciones se [blue]reducen a la mitad[/blue] (al menos [blue]1[/blue]).\nSe acumula el daño de ataque no bloqueado y el daño de [gold]Escarcha[/gold] que recibe; si alcanza las acumulaciones actuales, se activa [gold]Fractura de Hielo[/gold]: recibe daño igual a las acumulaciones y se elimina toda la [gold]Escarcha[/gold].",
 "HONKAILIB-FROST_POWER.smartDescription":"{Reduction:cond:>0?El daño de ataque que {OnPlayer:tú causas|este causa} se reduce en [blue]{Reduction}%[/blue].\n|}Al inicio {OnPlayer:de tu turno|del turno de este}, {FrostTurn:cond:>0?recibe [blue]{FrostTurn}[/blue] de daño, luego |}las acumulaciones de [gold]Escarcha[/gold] se reducen en [blue]{FrostDecrement}[/blue].\nSe acumula el daño de ataque no bloqueado y el daño de [gold]Escarcha[/gold] recibidos; acumulado actual: [blue]{FrostAccumulated}[/blue]. Cuando el valor acumulado alcanza las acumulaciones actuales, se activa [gold]Fractura de Hielo[/gold]: inflige [blue]{Amount}[/blue] de daño y elimina la [gold]Escarcha[/gold].",
})
print("HonkaiLib traducido")
