# -*- coding: utf-8 -*-
import glob, os, json, re, sys, importlib.util
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
BS=chr(92)
P=max(glob.glob("_translation_work/beta_dl/Herta/**/*.pck",recursive=True),key=os.path.getsize)
with open(P,"rb") as f:
    ents,h=pt.read_dir(f); fb=h[5]; eng={}; pref=None
    for e in ents:
        p=e['path'].replace(BS,'/')
        if '/localization/eng/' in p and p.endswith('.json'):
            if pref is None: pref=p.split('/localization/')[0]
            f.seek(e['off']+fb); eng[os.path.basename(p)]=json.loads(f.read(e['size']))

# Traducciones por CLAVE (una por valor unico; el script propaga a duplicados con igual valor en ingles)
T={
# characters
"MOENEGIMOD-HERTA.aromaPrinciple":"[sine][blue]...variables aburridas...[/blue][/sine]",
"MOENEGIMOD-HERTA.banter.alive.endTurnPing":"¿Todavía no terminás? Ineficiente.",
"MOENEGIMOD-HERTA.banter.dead.endTurnPing":"Hmpf... solo un experimento fallido...",
"MOENEGIMOD-HERTA.cardsModifierDescription":"Las cartas de La Herta ahora pueden aparecer en recompensas y tiendas.",
"MOENEGIMOD-HERTA.cardsModifierTitle":"Cartas de La Herta",
"MOENEGIMOD-HERTA.description":"Una genia que trata al mundo entero como un experimento.\nPara [gold]La Herta[/gold], todo es una variable más que analizar y reconstruir.",
"MOENEGIMOD-HERTA.eventDeathPrevention":"...Eso no alcanza para sacarme del experimento.",
"MOENEGIMOD-HERTA.goldMonologue":"[sine]Recursos, nada más... usalos bien.[/sine]",
"MOENEGIMOD-HERTA.possessiveAdjective":"su","MOENEGIMOD-HERTA.pronounObject":"ella","MOENEGIMOD-HERTA.pronounPossessive":"suyo","MOENEGIMOD-HERTA.pronounSubject":"ella",
"MOENEGIMOD-HERTA.title":"La Herta","MOENEGIMOD-HERTA.titleObject":"La Herta",
"MOENEGIMOD-HERTA.unlockText":"Completa un experimento con [pink]{Prerequisite}[/pink] para desbloquear a este individuo.",
# monsters
"MOENEGIMOD-XIAO_HERTA.name":"Mini Herta","MOENEGIMOD-XIAO_HERTA.title":"Mini Herta",
"MOENEGIMOD-XIAO_HERTA.description":"Mientras Mini Herta esté viva, recibe todo el daño por La Herta, incluido el daño de las propias cartas de La Herta, las cartas de Maldición en mano y la pérdida directa de PV.",
# potions (valor repetido en varias claves)
"MOENEGIMOD-GENIUS_IDEA.title":"Idea Genial",
"MOENEGIMOD-GENIUS_IDEA.description":"Gana {Stars:inspirationIcons()}.",
"MOENEGIMOD-GENIUS_IDEA.selectionScreenPrompt":"Elige un jugador.",
# relics
"MOENEGIMOD-MAO_ZI.title":"El Sombrero de La Herta",
"MOENEGIMOD-MAO_ZI.description":"Al inicio de cada turno, gana [blue]{Stars}[/blue] de Inspiración. Al final de tu turno, pierde toda la Inspiración y gana [blue]3[/blue] de Bloqueo por cada Inspiración perdida. Si perdiste más de [blue]3[/blue] de Inspiración, gana [blue]1[/blue] de Energía y roba [blue]1[/blue] carta adicional el próximo turno.\nMientras Mini Herta esté viva, recibe todo el daño por La Herta, incluido el daño de las propias cartas de La Herta, las cartas de Maldición en mano y la pérdida directa de PV.",
"MOENEGIMOD-MAO_ZI.flavor":"No lo toques. El ángulo es perfecto.",
"MOENEGIMOD-BIGGER_HAT.title":"Un Sombrero Aún Más Grande",
"MOENEGIMOD-BIGGER_HAT.description":"Al inicio de cada turno, gana [blue]{Stars}[/blue] de Inspiración. Al final de tu turno, pierde toda la Inspiración y gana [blue]3[/blue] de Bloqueo por cada Inspiración perdida. Si perdiste más de [blue]3[/blue] de Inspiración, gana [blue]1[/blue] de Energía y roba [blue]1[/blue] carta adicional el próximo turno.",
"MOENEGIMOD-BIGGER_HAT.flavor":"Ahora el ángulo es todavía más perfecto.",
"MOENEGIMOD-END_OF_SEARCH.title":"Fin de la Búsqueda",
"MOENEGIMOD-END_OF_SEARCH.description":"La primera vez que robas una carta de [gold]Estado[/gold] o [gold]Maldición[/gold] cada turno, gana [blue]1[/blue] de Energía.",
"MOENEGIMOD-END_OF_SEARCH.flavor":"La respuesta espera al final de cada pregunta imposible.",
# powers (version powers.json - texto plano)
"MOENEGIMOD-INTERPRETATION_POWER.title":"Interpretación",
"MOENEGIMOD-INTERPRETATION_POWER.description":"Cuando La Herta juega una carta y gasta Inspiración, recibe daño igual a esta Interpretación. Se activa una vez cada vez que se gasta Inspiración. Al final del turno del jugador, pierde 2.",
"MOENEGIMOD-KITCHEN_EXPLOSION_POWER.title":"Explosión de Cocina",
"MOENEGIMOD-KITCHEN_EXPLOSION_POWER.description":"Al inicio del próximo turno, inflige daño a todos los enemigos. Las acumulaciones indican la cantidad de activaciones.",
"MOENEGIMOD-OBSERVATION_MODE_POWER.title":"Modo Observación",
"MOENEGIMOD-OBSERVATION_MODE_POWER.description":"Al inicio de cada turno, aplica Interpretación a un enemigo aleatorio.",
"MOENEGIMOD-MIND_PALACE_POWER.title":"Palacio Mental",
"MOENEGIMOD-MIND_PALACE_POWER.description":"Cada vez que ganas Inspiración este turno, gana el doble.",
"MOENEGIMOD-BIG_PRODUCTION_POWER.title":"Producción en Masa",
"MOENEGIMOD-BIG_PRODUCTION_POWER.description":"Cada vez que juegas 5 cartas, Invoca a Mini Herta. El conteo se mantiene entre turnos.",
"MOENEGIMOD-AUTONOMOUS_DOLL_POWER.title":"Muñeca Autónoma",
"MOENEGIMOD-AUTONOMOUS_DOLL_POWER.description":"Al final de tu turno, si Mini Herta está viva, juega cartas de Ataque aleatorias de tu pila de descarte.",
"MOENEGIMOD-SPIN_AROUND_POWER.title":"Vueltas y Vueltas",
"MOENEGIMOD-SPIN_AROUND_POWER.description":"Este turno, cada vez que juegas Vueltitas, Mini Herta inflige daño adicional a todos los enemigos.",
"MOENEGIMOD-BRAINSTORM_POWER.title":"Lluvia de Ideas",
"MOENEGIMOD-BRAINSTORM_POWER.description":"Durante tu turno, cada vez que gastas 4 de Inspiración, gana 1 de Inspiración.",
"MOENEGIMOD-OPPORTUNITY_POWER.title":"Oportunidad",
"MOENEGIMOD-OPPORTUNITY_POWER.description":"Cada vez que aplicas Interpretación a un enemigo, roba cartas. Si está mejorada, también gana Inspiración.",
"MOENEGIMOD-GENIUS_FOCUS_POWER.title":"Concentración Genial",
"MOENEGIMOD-GENIUS_FOCUS_POWER.description":"Las cartas jugadas este turno se barajan en tu pila de robo.",
"MOENEGIMOD-SIXTEENTH_KEY_POWER.title":"La Decimosexta Llave",
"MOENEGIMOD-SIXTEENTH_KEY_POWER.description":"Cada 15 cartas jugadas, la próxima carta se juega de nuevo. El contador muestra el progreso actual.",
"MOENEGIMOD-IN_THE_GAME_POWER.title":"En el Juego",
"MOENEGIMOD-IN_THE_GAME_POWER.description":"Cuando recibís cualquier daño no bloqueado que no absorba Mini Herta, mueres de inmediato.",
"MOENEGIMOD-THOUGHT_BARRIER_POWER.title":"Barrera de Pensamiento",
"MOENEGIMOD-THOUGHT_BARRIER_POWER.description":"Durante tu turno, cada vez que gastas 1 de Inspiración, gana Bloqueo.",
"MOENEGIMOD-THIS_IS_ANSWER_POWER.title":"Aquí Está la Respuesta",
"MOENEGIMOD-THIS_IS_ANSWER_POWER.description":"La próxima carta que gaste Inspiración se juega de nuevo.",
"MOENEGIMOD-HERTA_ENERGY_NEXT_TURN_POWER.title":"Energía el Próximo Turno",
"MOENEGIMOD-HERTA_ENERGY_NEXT_TURN_POWER.description":"Al inicio del próximo turno, gana Energía.",
"MOENEGIMOD-WAND_RAMPAGE_POWER.title":"Furia de Varita",
"MOENEGIMOD-WAND_RAMPAGE_POWER.description":"La próxima carta jugada automáticamente se juega de nuevo.",
"MOENEGIMOD-EXQUISITE_CRAFT_POWER.title":"Artesanía Exquisita",
"MOENEGIMOD-EXQUISITE_CRAFT_POWER.description":"Al inicio de cada turno, añade una Vueltitas a tu mano. Mini Herta inflige más daño.",
"MOENEGIMOD-SUPERPOSITION_POWER.title":"Superposición",
"MOENEGIMOD-SUPERPOSITION_POWER.description":"La próxima Habilidad se juega de nuevo.",
"MOENEGIMOD-IRON_TOMB_FORM_POWER.title":"Forma Tumba de Hierro",
"MOENEGIMOD-IRON_TOMB_FORM_POWER.description":"Al inicio de cada turno, roba hasta tener 10 cartas en mano.",
"MOENEGIMOD-DOUBLE_XIAO_HERTA_HP_NEXT_TURN_POWER.title":"Génesis de Muñeca",
"MOENEGIMOD-DOUBLE_XIAO_HERTA_HP_NEXT_TURN_POWER.description":"Al inicio del próximo turno, duplica los PV de Mini Herta.",
"MOENEGIMOD-INSPIRATION_KEYWORD.title":"Inspiración",
"MOENEGIMOD-INSPIRATION_KEYWORD.description":"El recurso especial de La Herta. La Inspiración se pierde al final de tu turno. Algunas cartas gastan Inspiración para efectos extra.",
"MOENEGIMOD-INTERPRETATION_KEYWORD.title":"Interpretación",
"MOENEGIMOD-INTERPRETATION_KEYWORD.description":"Una penalización en los enemigos. Cuando La Herta juega una carta y gasta Inspiración, los enemigos con Interpretación reciben daño igual a su Interpretación. Se activa una vez cada vez que se gasta Inspiración. Al final del turno del jugador, pierde 2.",
"MOENEGIMOD-SUMMON_KEYWORD.title":"Invocar",
"MOENEGIMOD-SUMMON_KEYWORD.description":"Invoca a Mini Herta con los PV indicados. Si Mini Herta ya existe, en su lugar aumenta sus PV máximos.",
# cards
"MOENEGIMOD-HERTA_ATTACK.title":"Golpe","MOENEGIMOD-HERTA_ATTACK.description":"Inflige {Damage:diff()} de daño.",
"MOENEGIMOD-HERTA_BLOCK.title":"Defensa","MOENEGIMOD-HERTA_BLOCK.description":"Gana {Block:diff()} de [gold]Bloqueo[/gold].",
"MOENEGIMOD-FLASH_OF_INSIGHT.title":"Destello de Lucidez","MOENEGIMOD-FLASH_OF_INSIGHT.description":"Gana {Stars:inspirationIcons()}.",
"MOENEGIMOD-THOUGHT_FILTER.title":"Filtro de Pensamiento","MOENEGIMOD-THOUGHT_FILTER.description":"Roba {Cards:diff()} cartas. Da [gold]Etérea[/gold] a las cartas robadas.",
"MOENEGIMOD-MAGIC_FINGER.title":"Chasquido Mágico","MOENEGIMOD-MAGIC_FINGER.description":"Inflige {Damage:diff()} de daño.\nGasta {InspirationCost:inspirationIcons()} para infligir {ExtraDamage:diff()} de daño adicional.",
"MOENEGIMOD-YOUR_TURN.title":"¡Tu Turno!","MOENEGIMOD-YOUR_TURN.description":"[gold]Invoca[/gold] {Summon:diff()}.\nSi Mini Herta ya existe, en su lugar inflige {Damage:diff()} de daño a un enemigo aleatorio.",
"MOENEGIMOD-INSPIRATION_EMERGES.title":"Surge la Inspiración","MOENEGIMOD-INSPIRATION_EMERGES.description":"Gana {Block:diff()} de [gold]Bloqueo[/gold].\nDa [gold]Conservar[/gold] a una carta de tu mano.",
"MOENEGIMOD-INSPIRATION_EMERGES.selectionScreenPrompt":"Elige una carta de tu mano para Conservar.",
"MOENEGIMOD-PREPARED_IN_ADVANCE.title":"Preparado de Antemano","MOENEGIMOD-PREPARED_IN_ADVANCE.description":"Gana {Block:diff()} de [gold]Bloqueo[/gold].\nMejora todas las cartas de tu mano.\nGasta {InspirationCost:inspirationIcons()} para dar [gold]Conservar[/gold] a todas las cartas de tu mano.",
"MOENEGIMOD-BYE_BYE.title":"Ya No Servís","MOENEGIMOD-BYE_BYE.description":"Si Mini Herta está viva, muere. Inflige daño a todos los enemigos igual a {Multiplier:diff()} veces sus PV máximos.\nGasta {InspirationCost:inspirationIcons()} para [gold]Invocar[/gold] {Summon:diff()} el próximo turno.",
"MOENEGIMOD-NEW_ISSUE.title":"Nuevo Problema","MOENEGIMOD-NEW_ISSUE.description":"Gasta {InspirationCost:inspirationIcons()} para ganar {InspirationNextTurn:inspirationIcons()} el próximo turno{IfUpgraded:show: y robar {Cards:diff()} cartas adicionales|}.",
"MOENEGIMOD-MAGIC_BOOM.title":"Bombardeo Mágico","MOENEGIMOD-MAGIC_BOOM.description":"Inflige {Damage:diff()} de daño a un enemigo aleatorio X veces.\nGasta toda la Inspiración. Por cada {InspirationCost:inspirationIcons(1)} gastada, ataca una vez adicional. Si se gastó al menos [blue]{InspirationThreshold:diff()}[/blue] de Inspiración, duplica la cantidad de ataques adicionales.",
"MOENEGIMOD-PUPPET_ARMY.title":"Ejército de Marionetas","MOENEGIMOD-PUPPET_ARMY.description":"Añade {Cards:diff()} [gold]Vueltitas{IfUpgraded:show:+|}[/gold] a tu mano.",
"MOENEGIMOD-ZHUAN_QUAN_QUAN.title":"Vueltitas","MOENEGIMOD-ZHUAN_QUAN_QUAN.description":"Solo se puede jugar mientras Mini Herta esté viva.\nMini Herta inflige {Damage:diff()} de daño a todos los enemigos.",
"MOENEGIMOD-UP_GRADE.title":"Mejorar el Build","MOENEGIMOD-UP_GRADE.description":"[gold]Invoca[/gold] {Summon:diff()}.\nVos y Mini Herta ganan {Strength:diff()} de [gold]Fuerza[/gold].\nGasta {InspirationCost:inspirationIcons()} para añadir {Cards:diff()} [gold]Vueltitas[/gold] a tu mano.",
"MOENEGIMOD-LETS_COOK.title":"¡A Cocinar!","MOENEGIMOD-LETS_COOK.description":"Pierde {HpLoss:diff()} PV. Inflige {Damage:diff()} de daño a todos los enemigos.\nGasta {InspirationCost:inspirationIcons()} para añadir esta carta a tu mano y barajar {Cards:diff()} [gold]Hollín[/gold] en tu pila de robo{IfUpgraded:show:, con [blue]{FuelChance:diff()}[/blue]% de probabilidad de barajar un [gold]Combustible[/gold] adicional|}.",
"MOENEGIMOD-GIVE_IT_HERE.title":"¡Dámelo!","MOENEGIMOD-GIVE_IT_HERE.description":"Aplica {Interpretation:diff()} de [gold]Interpretación[/gold].\nSi el objetivo ya tiene al menos [blue]{Threshold:diff()}[/blue] de [gold]Interpretación[/gold], pierde Fuerza este turno igual a su Interpretación, y ganas Vigor igual a su Interpretación.",
"MOENEGIMOD-GOT_IT_YET.title":"¿Ya Entendiste?","MOENEGIMOD-GOT_IT_YET.description":"Inflige {Damage:diff()} de daño. Al atacar a un objetivo con [gold]Interpretación[/gold], aumenta este daño en la [gold]Interpretación[/gold] de ese objetivo.",
"MOENEGIMOD-KITCHEN_EXPLOSION.title":"Explosión de Cocina","MOENEGIMOD-KITCHEN_EXPLOSION.description":"Al inicio del próximo turno, inflige {Damage:diff()} de daño a todos los enemigos {Explosions:diff()} veces. Cada [gold]¡A Cocinar![/gold] jugada este turno añade una activación extra.\nGasta {InspirationCost:inspirationIcons()} para añadir {ExtraExplosions:diff()} activaciones extra.",
"MOENEGIMOD-OBSERVATION_MODE.title":"Modo Observación","MOENEGIMOD-OBSERVATION_MODE.description":"Al inicio de cada turno, aplica {Interpretation:diff()} de [gold]Interpretación[/gold] a un enemigo aleatorio.",
"MOENEGIMOD-LET_ME_SEE.title":"¡Déjame Ver!","MOENEGIMOD-LET_ME_SEE.description":"Aplica {Interpretation:diff()} de [gold]Interpretación[/gold].",
"MOENEGIMOD-Q_E_D.title":"Q.E.D","MOENEGIMOD-Q_E_D.description":"Aplica {Interpretation:diff()} de [gold]Interpretación[/gold]. Añade {Cards:diff()} [gold]Idea Audaz[/gold] y {BoshiZunCards:diff()} [gold]Momento de Nous[/gold] a tu mano.",
"MOENEGIMOD-BOLD_IDEA.title":"Idea Audaz","MOENEGIMOD-BOLD_IDEA.description":"Gana {Energy:diff()} de Energía y {Inspiration:inspirationIcons()}. Roba {Cards:diff()} cartas.",
"MOENEGIMOD-ONE_SHOT_DEAL.title":"Oferta Única","MOENEGIMOD-ONE_SHOT_DEAL.description":"Inflige {Damage:diff()} de daño a todos los enemigos.\nSi Mini Herta está viva, inflige daño a todos los enemigos igual a [blue]{XiaoHertaBaseDamage:diff()}[/blue] más sus PV máximos{IfUpgraded:show:.\n[gold]Invoca[/gold] {Summon:diff()}|}.",
"MOENEGIMOD-MIND_PALACE.title":"Palacio Mental","MOENEGIMOD-MIND_PALACE.description":"Cada vez que ganas Inspiración este turno, gana el doble.",
"MOENEGIMOD-NOT_SCIENCE_MAGIC.title":"No es Ciencia, es Magia","MOENEGIMOD-NOT_SCIENCE_MAGIC.description":"Agota la carta superior de tu pila de descarte. Aplica [gold]Interpretación[/gold] a todos los enemigos igual al coste de la carta agotada x {Multiplier:diff()}.",
"MOENEGIMOD-BIG_PRODUCTION.title":"Producción en Masa","MOENEGIMOD-BIG_PRODUCTION.description":"Cada vez que juegas {CardsPlayed:diff()} cartas, [gold]Invoca[/gold] {SummonPerTrigger:diff()}.",
"MOENEGIMOD-AUTONOMOUS_DOLL.title":"Muñeca Autónoma","MOENEGIMOD-AUTONOMOUS_DOLL.description":"Al final de tu turno, si Mini Herta está viva, juega al azar {Cards:diff()} cartas de Ataque de tu pila de descarte.",
"MOENEGIMOD-SPIN_SPIN_SPIN.title":"Vueltas y Vueltas","MOENEGIMOD-SPIN_SPIN_SPIN.description":"Añade {Cards:diff()} [gold]Vueltitas[/gold] a tu mano.\nEste turno, cada vez que juegas [gold]Vueltitas[/gold], Mini Herta inflige {Damage:diff()} de daño a todos los enemigos {ExtraHits:diff()} veces adicionales.",
"MOENEGIMOD-REFLUX_OPERATION.title":"Operación de Reflujo","MOENEGIMOD-REFLUX_OPERATION.description":"Consume {InterpretationCost:diff()} de [gold]Interpretación[/gold] del objetivo. Gana {Energy:diff()} de Energía.",
"MOENEGIMOD-GENIUS_STOMP.title":"Pisotón Genial","MOENEGIMOD-GENIUS_STOMP.description":"Inflige {Damage:diff()} de daño. Aplica {Interpretation:diff()} de [gold]Interpretación[/gold].\nGasta {InspirationCost:inspirationIcons()} para barajar una copia de coste 0 en tu pila de robo.",
"MOENEGIMOD-ACCOUNT_BAN.title":"Baneo de Cuenta","MOENEGIMOD-ACCOUNT_BAN.description":"Inflige daño igual al [blue]{MaxHpPercent:diff()}[/blue]% de los PV máximos del objetivo.\nSi esta carta mata al objetivo, quítala permanentemente de tu mazo.",
"MOENEGIMOD-CURIO_COLLECTION.title":"Colección de Curiosidades","MOENEGIMOD-CURIO_COLLECTION.description":"Gana {Stars:inspirationIcons()}.",
"MOENEGIMOD-BRAINSTORM.title":"Lluvia de Ideas","MOENEGIMOD-BRAINSTORM.description":"Durante tu turno, cada vez que gastas {InspirationSpent:inspirationIcons()}, gana {Stars:inspirationIcons()}.",
"MOENEGIMOD-OPPORTUNITY.title":"Oportunidad","MOENEGIMOD-OPPORTUNITY.description":"Cada vez que aplicas [gold]Interpretación[/gold] a un enemigo, roba {Cards:diff()} cartas{IfUpgraded:show: y gana {Inspiration:inspirationIcons()}|}.",
"MOENEGIMOD-DARE_TO_PROVOKE_ME.title":"¿Te Atreves a Provocarme?","MOENEGIMOD-DARE_TO_PROVOKE_ME.description":"Inflige {Damage:diff()} de daño.\nGasta {InspirationCost:inspirationIcons()} para barajar una copia de esta carta con el daño duplicado en tu pila de robo.",
"MOENEGIMOD-GENIUS_FOCUS.title":"Concentración Genial","MOENEGIMOD-GENIUS_FOCUS.description":"Roba {Cards:diff()} cartas.\nGasta {InspirationCost:inspirationIcons()} para barajar las cartas jugadas este turno en tu pila de robo.",
"MOENEGIMOD-BE_QUIET.title":"¡Silencio!","MOENEGIMOD-BE_QUIET.description":"Aplica {WeakPower:diff()} de [gold]Débil[/gold] a todos los enemigos.\nGasta {InspirationCost:inspirationIcons()} para ganar {Block:diff()} de [gold]Bloqueo[/gold].",
"MOENEGIMOD-SIXTEENTH_KEY.title":"La Decimosexta Llave","MOENEGIMOD-SIXTEENTH_KEY.description":"Cada [blue]{CardsPlayed:diff()}[/blue] cartas jugadas, la próxima carta se juega {ExtraPlays:diff()} veces adicionales.",
"MOENEGIMOD-OPEN_MIND.title":"Mente Abierta","MOENEGIMOD-OPEN_MIND.description":"Inflige {Damage:diff()} de daño. Gana {Stars:inspirationIcons()}.",
"MOENEGIMOD-IN_THE_GAME.title":"En el Juego","MOENEGIMOD-IN_THE_GAME.description":"Aplica {Interpretation:diff()} de [gold]Interpretación[/gold]. Baraja {Cards:diff()} [gold]Momento de Nous[/gold] en tu pila de robo. Añade {BoldIdeaCards:diff()} [gold]Idea Audaz[/gold] a tu mano. Cuando recibís cualquier daño no bloqueado que no absorba Mini Herta, mueres de inmediato.",
"MOENEGIMOD-GENIUS_WILL.title":"Voluntad Genial","MOENEGIMOD-GENIUS_WILL.description":"Aplica {Interpretation:diff()} de [gold]Interpretación[/gold]. Gana {Energy:diff()} de Energía, roba {Cards:diff()} cartas y gana {Stars:inspirationIcons()}. Baraja {BoshiZunCards:diff()} [gold]Momento de Nous[/gold] en tu pila de robo.",
"MOENEGIMOD-BOSHI_ZUN_MOMENT.title":"Momento de Nous","MOENEGIMOD-BOSHI_ZUN_MOMENT.description":"Al final de tu turno, si esta carta está en tu mano, recibe {SelfDamage:diff()} de daño, luego inflige {Damage:diff()} de daño fijo a todos los enemigos. Este daño solo cambia por el propio efecto de duplicación de esta carta. Cada vez que se activa, duplica el daño de la próxima activación.",
"MOENEGIMOD-THOUGHT_BARRIER.title":"Barrera de Pensamiento","MOENEGIMOD-THOUGHT_BARRIER.description":"Durante tu turno, cada vez que gastas {Stars:inspirationIcons(1)}, gana {Block:diff()} de [gold]Bloqueo[/gold].",
"MOENEGIMOD-RUAN_MEI_SUPPORT.title":"Apoyo de Ruan Mei","MOENEGIMOD-RUAN_MEI_SUPPORT.description":"Roba {Cards:diff()} cartas.\nGasta {InspirationCost:inspirationIcons()} para ganar {Block:diff()} de [gold]Bloqueo[/gold] y {InspirationNextTurn:inspirationIcons()} el próximo turno.",
"MOENEGIMOD-THIS_IS_ANSWER.title":"Aquí Está la Respuesta","MOENEGIMOD-THIS_IS_ANSWER.description":"Gana {Stars:inspirationIcons()}. La próxima carta que gaste Inspiración se juega {ExtraPlays:diff()} veces adicionales.",
"MOENEGIMOD-PREPARE_INGREDIENTS.title":"Preparar Ingredientes","MOENEGIMOD-PREPARE_INGREDIENTS.description":"[gold]Invoca[/gold] {Summon:diff()} el próximo turno.\nGasta {InspirationCost:inspirationIcons()} para ganar {EnergyNextTurn:diff()} de Energía el próximo turno.",
"MOENEGIMOD-READING_COMPREHENSION.title":"Comprensión Lectora","MOENEGIMOD-READING_COMPREHENSION.description":"Elige una carta de coste 0 de tu mano. Baraja {Cards:diff()} copias en tu pila de robo y aumenta el coste de esas copias en {Energy:diff()}.",
"MOENEGIMOD-READING_COMPREHENSION.selectionScreenPrompt":"Elige una carta de coste 0 de tu mano.",
"MOENEGIMOD-I_WANT_TO_LEARN_THIS.title":"Quiero Aprender Esto","MOENEGIMOD-I_WANT_TO_LEARN_THIS.description":"Elige 1 de 3 cartas raras aleatorias de otros personajes y añádela a tu mano.\nGasta {InspirationCost:inspirationIcons()} para que la carta elegida cueste 0 este turno.",
"MOENEGIMOD-I_WANT_TO_LEARN_THIS.selectionScreenPrompt":"Elige una carta para añadir a tu mano.",
"MOENEGIMOD-TYRANT_WITCH.title":"Bruja Tirana","MOENEGIMOD-TYRANT_WITCH.description":"Si Mini Herta está viva, muere. Roba {Cards:diff()} cartas y gana {Energy:diff()} de Energía.",
"MOENEGIMOD-SCREWLLUM_SUPPORT.title":"Apoyo de Screwllum","MOENEGIMOD-SCREWLLUM_SUPPORT.description":"Añade una [gold]IA Creativa[/gold] y un [gold]Aprendizaje Automático[/gold] a tu mano.",
"MOENEGIMOD-WAND_RAMPAGE.title":"Furia de Varita","MOENEGIMOD-WAND_RAMPAGE.description":"Juega las {Cards:diff()} cartas superiores de tu pila de robo {ExtraPlays:diff()} veces adicionales y Agótalas.\nGasta {InspirationCost:inspirationIcons()} para jugarlas {InspiredExtraPlays:diff()} veces adicionales en su lugar.",
"MOENEGIMOD-ORGANIZE_THOUGHTS.title":"Ordenar Pensamientos","MOENEGIMOD-ORGANIZE_THOUGHTS.description":"Roba {Cards:diff()} cartas con efectos de Inspiración de tu pila de robo.",
"MOENEGIMOD-ASTA_SUPPORT.title":"Apoyo de Asta","MOENEGIMOD-ASTA_SUPPORT.description":"Gana {Gold:diff()} de Oro. Hay un [blue]{BonusChance:diff()}[/blue]% de probabilidad de ganar {BonusGold:diff()} de Oro adicional.",
"MOENEGIMOD-MIRROR_ASSISTANT.title":"Asistente Espejo I","MOENEGIMOD-MIRROR_ASSISTANT.description":"Aplica {Interpretation:diff()} de [gold]Interpretación[/gold].\nGasta {InspirationCost:inspirationIcons()} para jugar y Agotar al azar una Habilidad de tu mano.",
"MOENEGIMOD-AUDIENCE.title":"Audiencia","MOENEGIMOD-AUDIENCE.description":"Gasta {InspirationCost:inspirationIcons()} para barajar copias de tu mano actual en tu pila de robo.",
"MOENEGIMOD-KNOWLEDGE_IS_POWER.title":"El Conocimiento es Poder","MOENEGIMOD-KNOWLEDGE_IS_POWER.description":"Inflige {Damage:diff()} de daño. Por cada Habilidad en tu mazo, inflige {SkillBonus:diff()} de daño adicional.",
"MOENEGIMOD-PUPPET_RIOT.title":"Motín de Marionetas","MOENEGIMOD-PUPPET_RIOT.description":"Inflige {Damage:diff()} de daño. Baraja {Cards:diff()} [gold]Vueltitas{IfUpgraded:show:+|}[/gold] en tu pila de robo.",
"MOENEGIMOD-WITCH_APPLE.title":"Manzana de la Bruja","MOENEGIMOD-WITCH_APPLE.description":"Inflige {Damage:diff()} de daño. Aplica [gold]Veneno[/gold] igual a la [gold]Interpretación[/gold] del objetivo.",
"MOENEGIMOD-HIT_FACE.title":"Apunta a la Cara","MOENEGIMOD-HIT_FACE.description":"Inflige {Damage:diff()} de daño. Aplica {WeakPower:diff()} de [gold]Débil[/gold].\nGasta {InspirationCost:inspirationIcons()} para aplicar {VulnerablePower:diff()} de [gold]Vulnerable[/gold].",
"MOENEGIMOD-ARMORY_OPEN.title":"Armería Abierta","MOENEGIMOD-ARMORY_OPEN.description":"[gold]Invoca[/gold] {Summon:diff()}. Añade {Cards:diff()} [gold]Vueltitas{IfUpgraded:show:+|}[/gold] a tu mano.\nGasta {InspirationCost:inspirationIcons()} para añadir una más.",
"MOENEGIMOD-EXQUISITE_CRAFT.title":"Artesanía Exquisita","MOENEGIMOD-EXQUISITE_CRAFT.description":"Al inicio de cada turno, añade una [gold]Vueltitas[/gold] a tu mano por cada copia de este Poder jugada. Mini Herta inflige {DamageBonus:diff()} de daño más.",
"MOENEGIMOD-SUDDEN_KICK.title":"Patada Repentina","MOENEGIMOD-SUDDEN_KICK.description":"Inflige {Damage:diff()} de daño. Aplica {Interpretation:diff()} de [gold]Interpretación[/gold] y {WeakPower:diff()} de [gold]Débil[/gold].",
"MOENEGIMOD-SEE_THROUGH.title":"Ver a Través","MOENEGIMOD-SEE_THROUGH.description":"Inflige {Damage:diff()} de daño. Si el objetivo no tiene [gold]Interpretación[/gold], aplica {Interpretation:diff()} de [gold]Interpretación[/gold].",
"MOENEGIMOD-HERTA_BIG_HAND.title":"La Gran Mano de La Herta","MOENEGIMOD-HERTA_BIG_HAND.description":"Inflige {Damage:diff()} de daño.\nGasta {InspirationCost:inspirationIcons()} para ganar {Energy:diff()} de Energía.",
"MOENEGIMOD-WITCH_COFFEE.title":"Café de la Bruja","MOENEGIMOD-WITCH_COFFEE.description":"Quita {Powers:diff()} poderes negativos aleatorios de otro jugador.",
"MOENEGIMOD-DELICIOUS_MAGIC.title":"Magia Deliciosa","MOENEGIMOD-DELICIOUS_MAGIC.description":"Inflige {Damage:diff()} de daño a todos los enemigos X veces.\nGasta toda la Inspiración. Por cada {Stars:inspirationIcons(1)} gastada, inflige {ExtraDamage:diff()} de daño adicional.",
"MOENEGIMOD-SUPERPOSITION.title":"Superposición","MOENEGIMOD-SUPERPOSITION.description":"Las cartas de tu mazo que compartan nombre con otra carta ganan Repetición {ExtraPlays:diff()} y [gold]Etérea[/gold].",
"MOENEGIMOD-CURIO_CHANGED_KITCHEN.title":"Cocina Alterada por Curiosidad","MOENEGIMOD-CURIO_CHANGED_KITCHEN.description":"Inflige {Damage:diff()} de daño a todos los enemigos. Si no tenés Inspiración, inflige {Multiplier:diff()} veces ese daño.",
"MOENEGIMOD-LEAVE_IT_TO_ME.title":"Déjamelo a Mí","MOENEGIMOD-LEAVE_IT_TO_ME.description":"Inflige {Damage:diff()} de daño. Baraja {Cards:diff()} [gold]Aturdimiento[/gold] en tu pila de robo.\nGasta {InspirationCost:inspirationIcons()} para ganar [gold]Bloqueo[/gold] igual al daño infligido.",
"MOENEGIMOD-IRON_TOMB_FORM.title":"Forma Tumba de Hierro","MOENEGIMOD-IRON_TOMB_FORM.description":"Gana {BufferPower:diff()} de [gold]Búfer[/gold]. Baraja {Cards:diff()} [gold]Momento de Nous[/gold] en tu pila de robo. A partir del próximo turno, roba hasta llenar la mano al inicio de cada turno. Termina tu turno.",
"MOENEGIMOD-PUPPET_GENESIS.title":"Génesis de Muñeca","MOENEGIMOD-PUPPET_GENESIS.description":"[gold]Invoca[/gold] {Summon:diff()}.\nGasta {InspirationCost:inspirationIcons()} para duplicar los PV de Mini Herta al inicio del próximo turno.",
"MOENEGIMOD-DREAM_IN_WITCH_HOUSE.title":"Sueño en la Casa de la Bruja","MOENEGIMOD-DREAM_IN_WITCH_HOUSE.description":"Inflige {Damage:diff()} de daño. Por cada carta que jugaste este turno, aplica {InterpretationPerCard:diff()} de [gold]Interpretación[/gold].",
"MOENEGIMOD-INDUCTIVE_SORTING.title":"Clasificación Inductiva","MOENEGIMOD-INDUCTIVE_SORTING.description":"Agota una carta de tu pila de descarte. Gana {Inspiration:inspirationIcons()}.",
"MOENEGIMOD-INDUCTIVE_SORTING.selectionScreenPrompt":"Elige una carta de tu pila de descarte para Agotar.",
"MOENEGIMOD-HIGH_SPEED_CALCULATION.title":"Cálculo de Alta Velocidad","MOENEGIMOD-HIGH_SPEED_CALCULATION.description":"Inflige {CalculatedDamage:diff()} de daño.\nEsto inflige [blue]1[/blue] de daño más por cada carta que robaste este turno.",
"MOENEGIMOD-EXCLUSION_PLAN.title":"Plan de Exclusión","MOENEGIMOD-EXCLUSION_PLAN.description":"Da [gold]Etérea[/gold] a todas las cartas de tu pila de descarte. Gana {Inspiration:inspirationIcons()}.",
"MOENEGIMOD-WITCH_SNACK.title":"Bocadillo de la Bruja","MOENEGIMOD-WITCH_SNACK.description":"Aplica {Interpretation:diff()} de [gold]Interpretación[/gold] a un enemigo. Si tiene al menos [blue]{Threshold:diff()}[/blue] de [gold]Interpretación[/gold], detónala, infligiendo daño a todos los enemigos igual al [blue]{MaxHpPercent:diff()}[/blue]% de los PV máximos de ese enemigo.",
"MOENEGIMOD-HERTA_IDOL_PROJECT.title":"Proyecto Ídolo Herta","MOENEGIMOD-HERTA_IDOL_PROJECT.description":"Mini Herta inflige {Damage:diff()} de daño a un enemigo. Letal: gana {Gold:diff()} de Oro y aumenta el daño de esta carta en {DamageIncrease:diff()} durante esta partida.",
"MOENEGIMOD-MIRROR_ASSISTANT_I_I.title":"Asistente Espejo II","MOENEGIMOD-MIRROR_ASSISTANT_I_I.description":"Gana {VigorPower:diff()} de [gold]Vigor[/gold].\nGasta {InspirationCost:inspirationIcons()} para ganar {Block:diff()} de [gold]Bloqueo[/gold]. Si esto gastó toda tu Inspiración exactamente, gana {BufferPower:diff()} de [gold]Búfer[/gold].",
"MOENEGIMOD-MIRROR_ASSISTANT_THREE.title":"Asistente Espejo III","MOENEGIMOD-MIRROR_ASSISTANT_THREE.description":"Inflige {Damage:diff()} de daño.\nGasta {InspirationCost:inspirationIcons()} para infligir daño una vez adicional. Si esto gastó toda tu Inspiración exactamente, inflige daño una vez más.",
"MOENEGIMOD-MIRROR_ASSISTANT_I_V.title":"Asistente Espejo IV","MOENEGIMOD-MIRROR_ASSISTANT_I_V.description":"Gana {IntangiblePower:diff()} de [gold]Intangible[/gold]. Roba {Cards:diff()} cartas. Al jugarse, si tu pila de agotamiento contiene los otros tres Asistentes Espejo, ganas este combate.",
"MOENEGIMOD-HYPOTHESIS_ARGUMENT.title":"Argumento de Hipótesis","MOENEGIMOD-HYPOTHESIS_ARGUMENT.description":"Gana Inspiración igual a la cantidad de Habilidades en tu pila de robo.",
"MOENEGIMOD-INSPIRATION_COUNTER":"[gold]Inspiración[/gold]\nAlgunas cartas gastan Inspiración para activar efectos extra.\nAl final de tu turno, pierde toda la Inspiración.",
"MOENEGIMOD-INSPIRATION_COUNTER.title":"Inspiración",
"MOENEGIMOD-INSPIRATION_COUNTER.description":"Algunas cartas gastan Inspiración para activar efectos extra.\nAl final de tu turno, pierde toda la Inspiración.",
}
# construir valmap (valor ingles -> esp) desde T, y propagar a claves con igual valor
valmap={}
for fn,d in eng.items():
    for k,v in d.items():
        if k in T and v.count("{")==T[k].count("{"): valmap[v]=T[k]   # solo mapear si la forma (tokens) coincide
OUT="_translation_work/beta_dl/_esp_Herta/"+pref+"/localization/esp"; os.makedirs(OUT,exist_ok=True)
miss=[]
for fn,d in eng.items():
    esp={}
    for k,v in d.items():
        if v in valmap: esp[k]=valmap[v]       # por VALOR primero (resuelve claves repetidas en powers/cards)
        elif k in T: esp[k]=T[k]
        else: miss.append(f"{fn}:{k}"); esp[k]=v
    json.dump(esp,open(f"{OUT}/{fn}","w",encoding="utf-8"),ensure_ascii=False,indent=2)
# validacion tags/tokens/llaves/saltos
TAGS=("[gold]","[/gold]","[blue]","[/blue]","[sine]","[/sine]","[pink]","[/pink]")
ok=True
for fn,d in eng.items():
    espd=json.load(open(f"{OUT}/{fn}",encoding="utf-8"))
    for k,ev in d.items():
        sv=espd[k]
        for t in TAGS:
            if ev.count(t)!=sv.count(t): ok=False; out(f"[{fn}] {k}: tag {t} {ev.count(t)}!={sv.count(t)}")
        if ev.count("{")!=sv.count("{") or ev.count("}")!=sv.count("}"): ok=False; out(f"[{fn}] {k}: llaves")
        if ev.count("\n")!=sv.count("\n"): ok=False; out(f"[{fn}] {k}: saltos {ev.count(chr(10))}!={sv.count(chr(10))}")
out(f"SIN TRADUCIR ({len(miss)}): {miss[:30]}")
out("HERTA VALIDACION OK" if ok and not miss else "REVISAR ^")
