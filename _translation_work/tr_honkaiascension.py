# -*- coding: utf-8 -*-
import json, os
M = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/honkai/HonkaiAscension/esp"
def patch(fn, ov):
    p = os.path.join(M, fn); d = json.load(open(p, encoding="utf-8-sig")); d.update(ov)
    json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

patch("acts.json", {"HONKAI_ACT4.title":"Acto Final"})
patch("afflictions.json", {
 "DEVOURED.title":"Devorado",
 "DEVOURED.description":"Añade [gold]Agotar[/gold] a esta carta.",
 "WEIGHTED.title":"Lastrado",
 "WEIGHTED.description":"Al jugar esta carta, pierdes {Amount:energyIcons()}.",
 "WEIGHTED.extraCardText":"Pierdes {Amount:energyIcons()}.",
})
NI_T="Aún no implementado"; NI_D="Aún no implementado…"
asc={
 "LEVEL_11.title":"Llegada del Honkai I",
 "LEVEL_11.description":"Al final del Acto 1, libra un combate adicional contra una élite.",
 "LEVEL_12.title":"Llegada del Honkai II",
 "LEVEL_12.description":"Al final del Acto 2, libra un combate contra dos jefes.",
 "LEVEL_13.title":"Llegada del Honkai III",
 "LEVEL_13.description":"Activa el Acto 4, con un jefe más poderoso.",
 "LEVEL_14.title":"Erosión Letal",
 "LEVEL_14.description":"Mejora las reliquias iniciales; la torre ya está profundamente [red]erosionada[/red] por el Honkai.",
 "LEVEL_15.title":"Apocalipsis Final",
 "LEVEL_15.description":"Al entrar en el Acto 2 y el Acto 3, obtienes [gold]un gran poder[/gold]; todos los enemigos se vuelven más [red]feroces[/red].",
 "LEVEL_20.title":"¡Sorpresa!",
 "LEVEL_20.description":"Aunque no sé por qué has vuelto aquí, pero… ¡bienvenido!",
}
for n in (16,17,18,19,21,22,23,24,25,26,27,28,29,30):
    asc[f"LEVEL_{n}.title"]=NI_T; asc[f"LEVEL_{n}.description"]=NI_D
patch("ascension.json", asc)
patch("cards.json", {
 "MODIFY_DOMINATE.description":"Otorga {VulnerablePower:diff()} de [gold]vulnerabilidad[/gold].\nPor cada 2 de [gold]vulnerabilidad[/gold] en el enemigo, obtienes 1 de [gold]fuerza[/gold] este turno.",
 "MODIFY_QUADCAST.description":"Obtienes {FocusPower:diff()} de [gold]Enfoque[/gold] este turno.\n[gold]Evoca[/gold] tu orbe más a la derecha {Repeat:diff()} veces.",
 "MODIFY_THE_SEALED_THRONE.description":"Por cada {energyPrefix:energyIcons(2)} que gastas, obtienes {singleStarIcon}.",
 "MODIFY_FORBIDDEN_GRIMOIRE.description":"{IfUpgraded:show:|Al inicio del combate, [gold]Olvido[/gold].\n}Al final del combate, puedes elegir una carta de tu [gold]mazo[/gold] para eliminarla.",
})
patch("encounters.json", {
 "HONKAIASCENSION-DOORMAKER_BOSS.title":"Creador de Puertas",
 "HONKAIASCENSION-DOORMAKER_BOSS.loss":"[gold]{encounter}[/gold] no toleró las molestias de {character}.",
})
patch("monsters.json", {
 "HONKAIASCENSION-DOOR.name":"Puerta",
 "HONKAIASCENSION-DOORMAKER.name":"Creador de Puertas",
 "HONKAIASCENSION-DOORMAKER.moves.DRAMATIC_OPEN":"Apertura Dramática",
 "HONKAIASCENSION-DOORMAKER.moves.DRAMATIC_OPEN.speakLine":"Tengo hambre…",
 "HONKAIASCENSION-DOORMAKER.moves.GRASP_MOVE.title":"Aferramiento",
 "HONKAIASCENSION-DOORMAKER.moves.HUNGER_MOVE.title":"Hambre",
 "HONKAIASCENSION-DOORMAKER.moves.SCRUTINY_MOVE.title":"Escrutinio",
})
patch("powers.json", {
 "HONKAIASCENSION-HUNGER_POWER.title":"Hambre",
 "HONKAIASCENSION-HUNGER_POWER.description":"Cuando juegas una carta de ataque o de habilidad, se [gold]Agota[/gold].",
 "HONKAIASCENSION-HUNGER_POWER.smartDescription":"Cuando juegas una carta de ataque o de habilidad, se [gold]Agota[/gold].",
 "HONKAIASCENSION-SCRUTINY_POWER.title":"Escrutinio",
 "HONKAIASCENSION-SCRUTINY_POWER.description":"Durante tu turno no puedes robar cartas adicionales.",
 "HONKAIASCENSION-SCRUTINY_POWER.smartDescription":"Durante tu turno no puedes robar cartas adicionales.",
 "HONKAIASCENSION-GRASP_POWER.title":"Aferramiento",
 "HONKAIASCENSION-GRASP_POWER.description":"Cada vez que juegas una carta, pierdes [blue]1[/blue] de energía.",
 "HONKAIASCENSION-GRASP_POWER.smartDescription":"Cada vez que juegas una carta, pierdes {Amount:energyIcons()}.",
 "MODIFY_THE_SEALED_THRONE_POWER.description":"Por cada {energyPrefix:energyIcons(2)} que gastas, obtienes {singleStarIcon}.",
 "MODIFY_THE_SEALED_THRONE_POWER.smartDescription":"Por cada {energyPrefix:energyIcons(2)} que gastas, obtienes {singleStarIcon}.",
})
patch("settings_ui.json", {
 "HONKAIASCENSION.mod_title":"Ajustes del mod «Honkai · Mecánicas Avanzadas»",
 "HONKAIASCENSION-ORIGINAL_CHARACTERS_SECTION.title":"Ajustes de personajes originales",
 "HONKAIASCENSION-MODIFY_DOMINATE.title":"Ajustar [gold]Dominación[/gold]",
 "HONKAIASCENSION-MODIFY_DOMINATE.hover.title":"Ajustar Dominación",
 "HONKAIASCENSION-MODIFY_DOMINATE.hover.desc":"Marca esta opción para aplicar el [gold]debilitamiento[/gold] de la carta [gold]Dominación[/gold] de [red]Ironclad[/red].",
 "HONKAIASCENSION-MODIFY_QUADCAST.title":"Ajustar [gold]Lanzamiento Cuádruple[/gold]",
 "HONKAIASCENSION-MODIFY_QUADCAST.hover.title":"Ajustar Lanzamiento Cuádruple",
 "HONKAIASCENSION-MODIFY_QUADCAST.hover.desc":"Marca esta opción para aplicar la [gold]mejora[/gold] de la carta [gold]Lanzamiento Cuádruple[/gold] de [blue]Defect[/blue].",
 "HONKAIASCENSION-MODIFY_BIASED_COGNITION.title":"Ajustar [gold]Cognición Sesgada[/gold]",
 "HONKAIASCENSION-MODIFY_BIASED_COGNITION.hover.title":"Ajustar Cognición Sesgada",
 "HONKAIASCENSION-MODIFY_BIASED_COGNITION.hover.desc":"Marca esta opción para aplicar la [gold]mejora[/gold] de la carta [gold]Cognición Sesgada[/gold] de [blue]Defect[/blue].",
 "HONKAIASCENSION-MODIFY_THE_SEALED_THRONE.title":"Ajustar [gold]Trono Sellado[/gold]",
 "HONKAIASCENSION-MODIFY_THE_SEALED_THRONE.hover.title":"Ajustar Trono Sellado",
 "HONKAIASCENSION-MODIFY_THE_SEALED_THRONE.hover.desc":"Marca esta opción para aplicar el [gold]debilitamiento[/gold] de la carta [gold]Trono Sellado[/gold] de [orange]Regent[/orange].",
 "HONKAIASCENSION-MODIFY_FORBIDDEN_GRIMOIRE.title":"Ajustar [gold]Grimorio Prohibido[/gold]",
 "HONKAIASCENSION-MODIFY_FORBIDDEN_GRIMOIRE.hover.title":"Ajustar Grimorio Prohibido",
 "HONKAIASCENSION-MODIFY_FORBIDDEN_GRIMOIRE.hover.desc":"Marca esta opción para aplicar el [gold]debilitamiento[/gold] de la carta [gold]Grimorio Prohibido[/gold] de [purple]Necrobinder[/purple].",
})
print("HonkaiAscension traducido")
