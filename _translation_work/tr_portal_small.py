# -*- coding: utf-8 -*-
import json, os, re
B = "_translation_work/_pend/portal/sts2_char_portalcraft/localization/eng"
OUT = "_translation_work/_pend/portal_esp/sts2_char_portalcraft/localization/esp"
os.makedirs(OUT, exist_ok=True)
def loadeng(fn): return json.load(open(f"{B}/{fn}.json", encoding="utf-8"))
def save(fn, d): json.dump(d, open(f"{OUT}/{fn}.json","w",encoding="utf-8"), ensure_ascii=False, indent=2)

ancients = {
 "THE_ARCHITECT.talk.STS2_CHAR_PORTALCRAFT-PORTALCRAFT.0-0r.char":"¡Te superaré a ti también!",
 "THE_ARCHITECT.talk.STS2_CHAR_PORTALCRAFT-PORTALCRAFT.0-0r.next":"Continuar",
 "THE_ARCHITECT.talk.STS2_CHAR_PORTALCRAFT-PORTALCRAFT.0-1r.ancient":"Mueres",
 "THE_ARCHITECT.talk.STS2_CHAR_PORTALCRAFT-PORTALCRAFT.0-attack":"Ambos",
}
enchantments = {
 "FLIGHT_OF_ICARUS_ENCHANTMENT.title":"Vuelo de Ícaro",
 "FLIGHT_OF_ICARUS_ENCHANTMENT.description":"[gold]Últimas Palabras[/gold]: Roba 1 carta.",
 "FLIGHT_OF_ICARUS_ENCHANTMENT.extraCardText":"[gold]Últimas Palabras[/gold]: Roba 1 carta.",
}
gameplay_ui = {
 "CARD_TYPE.ARTIFACT":"Artefacto",
 "CARD_TYPE.PUPPET":"Marioneta",
 "CARD_TYPE.AMULET":"Amuleto",
 "EVOLVE_SELECT_HEADER":"Elige una carta para [gold]Evolucionar[/gold]",
 "SUPER_EVOLVE_SELECT_HEADER":"Elige una carta para [gold]Superevolucionar[/gold]",
}
settings_ui = {
 "STS2_CHAR_PORTALCRAFT.mod_title":"PortalCraft",
 "STS2_CHAR_PORTALCRAFT-AUDIO.title":"Audio",
 "STS2_CHAR_PORTALCRAFT-CARD_SFX_VOLUME.title":"Volumen de SFX de cartas",
 "STS2_CHAR_PORTALCRAFT-CARD_SFX_VOLUME.hover.title":"Volumen de SFX de cartas",
 "STS2_CHAR_PORTALCRAFT-CARD_SFX_VOLUME.hover.desc":"Ajusta el volumen de los efectos de sonido personalizados de las cartas.",
}
static_hover_tips = {
 "ARTIFACT.title":"Artefacto",
 "ARTIFACT.description":"Cartas ficha con [gold]Conservar[/gold] y [gold]Agotar[/gold]. Jugar un Artefacto te permite descartar otros Artefactos para fusionarlos en un nivel superior. Fusionar es gratis: la energía solo se gasta al jugarlo por su efecto base.",
}
relics = {
 "STS2_CHAR_PORTALCRAFT-RESONANCE_CORE.title":"Núcleo de Resonancia",
 "STS2_CHAR_PORTALCRAFT-RESONANCE_CORE.description":"Al inicio del combate, gana dos [gold]Puntos de Evolución[/gold] y un [purple]Punto de Superevolución[/purple]",
 "STS2_CHAR_PORTALCRAFT-RESONANCE_CORE.flavor":"TEXTO DE MARCADOR",
 "STS2_CHAR_PORTALCRAFT-FUSION_PLATING.title":"Blindaje de Fusión",
 "STS2_CHAR_PORTALCRAFT-FUSION_PLATING.description":"Cada vez que [gold]Fusionas[/gold] un Artefacto, gana 2 de Bloqueo.",
 "STS2_CHAR_PORTALCRAFT-FUSION_PLATING.flavor":"TEXTO DE MARCADOR",
}
characters = {
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.aromaPrinciple":"Historia",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.banter.alive.endTurnPing":"¡Rápido!",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.banter.dead.endTurnPing":"...",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.cardsModifierDescription":"Las cartas de Portalcraft ahora aparecerán en recompensas y tiendas.",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.cardsModifierTitle":"Cartas de Portalcraft",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.description":"Una poderosa tecnomante capaz de evolucionar sus cartas para alcanzar un poder inmenso.",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.eventDeathPrevention":"Frase de supervivencia co-op",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.goldMonologue":"¡Muchas gracias!",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.possessiveAdjective":"su",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.pronounObject":"ella",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.pronounPossessive":"suya",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.pronounSubject":"ella",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.title":"Portalcraft",
 "STS2_CHAR_PORTALCRAFT-PORTALCRAFT.titleObject":"Portalcraft",
}
card_selection = {
 "ARTIFACT_FUSE_PROMPT":"Elige Artefactos para fusionar (o confirma para jugar en base)",
 "CATALYST_PROMPT":"Elige un Artefacto T2 para añadir a tu mano",
 "CARNELIA_PROMPT":"Elige un Artefacto para darle 'No puede ser Agotado'",
 "ALOUETTE_PROMPT":"Elige un Artefacto para hacerlo gratis este turno",
 "FLIGHT_OF_ICARUS_PROMPT":"Elige un Artefacto para potenciar",
 "ARTIFACT_CATAPULT_PROMPT":"Elige un Artefacto para copiar",
 "FIELD_SCIENTIST_PROMPT":"Elige una carta para descartar",
 "DOOMWRIGHT_RESURGENCE_PROMPT":"Elige Artefactos para copiar (coste 1 o menos)",
 "RALMIA_PROMPT":"Elige Artefactos para activar (coste 2 o menos)",
 "VIER_HEART_SLAYER_PROMPT":"Elige Marioneta(s) para transformar en Verdugos de Muñecas",
 "PUPPET_SHIELD_PROMPT":"Elige Marionetas para agotar a cambio de Bloqueo",
 "RESURRECTION_TUNER_EXHAUST_PROMPT":"Elige una carta para agotar",
 "SUPPLICANT_PROMPT":"Elige una carta para agotar",
 "WASTELAND_PROMPT":"Elige una carta para agotar",
 "DEVASTATING_SOPRANO_PROMPT":"Elige una carta para agotar",
 "BIOFABRICATION_PROMPT":"Elige un Artefacto para producir en masa",
 "SINCERITY_PROMPT":"Elige una carta para transformar en Amiguitos de Imari",
 "CASSIUS_PROMPT":"Elige un Artefacto para determinar el daño",
 "IMARI_DISCARD_PROMPT":"Elige una carta para descartar",
 "IMARI_TUTOR_PROMPT":"Elige una Habilidad para añadir a tu mano",
 "ELD_AXE_REDUCE_PROMPT":"Elige una carta para reducir su coste en 1",
 "ACHIM_EXHAUST_PROMPT":"Elige una carta para agotar",
 "ACHIM_RETRIEVE_PROMPT":"Elige una carta para añadir a tu mano",
 "FLOWERING_ARTISAN_PROMPT":"Elige una Habilidad para añadir a tu mano",
 "DEPTHS_COPY_PROMPT":"Elige una carta (coste base 2+) para copiar",
 "NEW_AGE_CARTOGRAPHER_COPY_PROMPT":"Elige un Artefacto (coste 2 o menos) para copiar",
 "MELODIOUS_MONODY_PROMPT":"Elige una carta para agotar",
 "ALOUETTE_COPY_PROMPT":"Elige un Artefacto (coste 2 o menos) para copiar",
 "EUSTACE_SKYBOUND_PROMPT":"Elige una carta sin evolucionar para evolucionar",
}

_kw_artifact = "[gold]Conservar[/gold]. [gold]Agotar[/gold]. Puede [gold]Fusionarse[/gold] con otros Artefactos de tu mano, creando un Artefacto de nivel superior gratis."
_kw_puppet = "[gold]Agotar[/gold]. Una ficha desechable que inflige daño. Sinergiza con cartas relacionadas con Marionetas."
_kw_amulet = "[gold]Conservar[/gold]. No se puede jugar."
_kw_fuse = "Al jugarse, puedes elegir Artefactos coincidentes de tu mano para agotarlos y combinarlos en un Artefacto de nivel superior. Fusionar reembolsa el coste de energía."
_kw_cryst = "Si no puedes pagar el coste completo de esta carta, puede jugarse por su coste de [gold]Cristalizar[/gold], añadiendo una copia [gold]Amuleto[/gold] a tu mano. Solo se activan los efectos de Cristalizar de esta forma."
_kw_count = "Al inicio de tu turno, resta 1. Cuando llega a 0, la carta se [gold]Agota[/gold]."
_kw_lw = "Se activa cuando esta carta se [gold]Agota[/gold]."
_kw_sba = "Una habilidad que se activa cuando el medidor de [gold]Arte Celestial[/gold] de la carta es mayor o igual a [gold]10[/gold]. El medidor de Arte Celestial de una carta equivale al número del turno actual más la cantidad de veces que una carta ha evolucionado mientras está en tu mano."
_kw_ssba = "Una habilidad que se activa cuando el medidor de [gold]Arte Celestial[/gold] de la carta es mayor o igual a [gold]15[/gold]. El medidor de Arte Celestial de una carta equivale al número del turno actual más la cantidad de veces que una carta ha evolucionado mientras está en tu mano."
_kw_ep = "Puntos que gastas para [gold]Evolucionar[/gold] seguidores. Empiezas la partida con [gold]2[/gold]."
_kw_sep = "Puntos que gastas para [gold]Superevolucionar[/gold] seguidores. Empiezas la partida con [gold]2[/gold]."
_kw_evolution = "Evolucionar un seguidor le da un bono fijo de +2 al daño infligido/Bloqueo ganado. Un seguidor evolucionado no puede volver a evolucionar. Puedes gastar un [gold]PE[/gold] para evolucionar un seguidor una vez por turno. No puedes [gold]Evolucionar[/gold] y [gold]Superevolucionar[/gold] en el mismo turno."
_kw_sevolution = "Superevolucionar un seguidor le da un bono fijo de +3 al daño infligido/Bloqueo ganado y lo siguiente: — Este seguidor no puede ser agotado. Los seguidores superevolucionados también se consideran [gold]Evolucionados[/gold]. Puedes gastar un [gold]PSE[/gold] para superevolucionar un seguidor una vez por turno. No puedes [gold]Evolucionar[/gold] y [gold]Superevolucionar[/gold] en el mismo turno."
_kw_evolve = "Una habilidad que se activa cuando la carta está [gold]evolucionada[/gold] o [purple]superevolucionada[/purple]."
_kw_sevolve = "Una habilidad que se activa cuando la carta está [purple]superevolucionada[/purple]."
_kw_bane = "Destruye cualquier [gold]esbirro[/gold] enemigo al que ataque esta carta tras infligir el daño. En su lugar, inflige +10 de daño a enemigos que no sean esbirros."
_kw_cbe = "Esta carta no puede ser [gold]Agotada[/gold] por ningún medio."
_kw_summon = "Añade la carta indicada a tu mano. Cuesta [gold]0[/gold] este turno y gana [gold]Etérea[/gold] y [gold]Agotar[/gold]."

card_keywords = {
 "ARTIFACT.title":"Artefacto","ARTIFACT.description":_kw_artifact,
 "STS2_CHAR_PORTALCRAFT-ARTIFACT.title":"Artefacto","STS2_CHAR_PORTALCRAFT-ARTIFACT.description":_kw_artifact,
 "PUPPET.title":"Marioneta","PUPPET.description":_kw_puppet,
 "STS2_CHAR_PORTALCRAFT-PUPPET.title":"Marioneta","STS2_CHAR_PORTALCRAFT-PUPPET.description":_kw_puppet,
 "AMULET.title":"Amuleto","AMULET.description":_kw_amulet,
 "STS2_CHAR_PORTALCRAFT-AMULET.title":"Amuleto","STS2_CHAR_PORTALCRAFT-AMULET.description":_kw_amulet,
 "WASTELAND_TOKEN.title":"Ficha de Páramo","WASTELAND_TOKEN.description":"No se puede jugar. Al agotarse, roba 1.",
 "STS2_CHAR_PORTALCRAFT-WASTELAND_TOKEN.title":"Ficha de Páramo","STS2_CHAR_PORTALCRAFT-WASTELAND_TOKEN.description":"No se puede jugar. Al agotarse, roba 1 carta.",
 "FUSE.title":"Fusionar","FUSE.description":_kw_fuse,
 "STS2_CHAR_PORTALCRAFT-FUSE.title":"Fusionar","STS2_CHAR_PORTALCRAFT-FUSE.description":_kw_fuse,
 "CRYSTALLIZE.title":"Cristalizar","CRYSTALLIZE.description":_kw_cryst,
 "STS2_CHAR_PORTALCRAFT-CRYSTALLIZE.title":"Cristalizar","STS2_CHAR_PORTALCRAFT-CRYSTALLIZE.description":_kw_cryst,
 "COUNTDOWN.title":"Cuenta Atrás","COUNTDOWN.description":_kw_count,
 "STS2_CHAR_PORTALCRAFT-COUNTDOWN.title":"Cuenta Atrás","STS2_CHAR_PORTALCRAFT-COUNTDOWN.description":_kw_count,
 "LASTWORDS.title":"Últimas Palabras","LASTWORDS.description":_kw_lw,
 "STS2_CHAR_PORTALCRAFT-LASTWORDS.title":"Últimas Palabras","STS2_CHAR_PORTALCRAFT-LASTWORDS.description":_kw_lw,
 "SKYBOUNDART.title":"Arte Celestial","SKYBOUNDART.description":_kw_sba,
 "STS2_CHAR_PORTALCRAFT-SKYBOUNDART.title":"Arte Celestial","STS2_CHAR_PORTALCRAFT-SKYBOUNDART.description":_kw_sba,
 "SUPERSKYBOUNDART.title":"Súper Arte Celestial","SUPERSKYBOUNDART.description":_kw_ssba,
 "STS2_CHAR_PORTALCRAFT-SUPERSKYBOUNDART.title":"Súper Arte Celestial","STS2_CHAR_PORTALCRAFT-SUPERSKYBOUNDART.description":_kw_ssba,
 "EVOLUTIONPOINT.title":"PE (Punto de Evolución)","EVOLUTIONPOINT.description":_kw_ep,
 "STS2_CHAR_PORTALCRAFT-EVOLUTIONPOINT.title":"PE (Punto de Evolución)","STS2_CHAR_PORTALCRAFT-EVOLUTIONPOINT.description":_kw_ep,
 "SUPEREVOLUTIONPOINT.title":"PSE (Punto de Superevolución)","SUPEREVOLUTIONPOINT.description":_kw_sep,
 "STS2_CHAR_PORTALCRAFT-SUPEREVOLUTIONPOINT.title":"PSE (Punto de Superevolución)","STS2_CHAR_PORTALCRAFT-SUPEREVOLUTIONPOINT.description":_kw_sep,
 "EVOLUTION.title":"Evolución","EVOLUTION.description":_kw_evolution,
 "STS2_CHAR_PORTALCRAFT-EVOLUTION.title":"Evolución","STS2_CHAR_PORTALCRAFT-EVOLUTION.description":_kw_evolution,
 "SUPEREVOLUTION.title":"Superevolución","SUPEREVOLUTION.description":_kw_sevolution,
 "STS2_CHAR_PORTALCRAFT-SUPEREVOLUTION.title":"Superevolución","STS2_CHAR_PORTALCRAFT-SUPEREVOLUTION.description":_kw_sevolution,
 "EVOLVE.title":"Evolucionar","EVOLVE.description":_kw_evolve,
 "STS2_CHAR_PORTALCRAFT-EVOLVE.title":"Evolucionar","STS2_CHAR_PORTALCRAFT-EVOLVE.description":_kw_evolve,
 "SUPEREVOLVE.title":"Superevolucionar","SUPEREVOLVE.description":_kw_sevolve,
 "STS2_CHAR_PORTALCRAFT-SUPEREVOLVE.title":"Superevolucionar","STS2_CHAR_PORTALCRAFT-SUPEREVOLVE.description":_kw_sevolve,
 "BANE.title":"Aniquilación","BANE.description":_kw_bane,
 "STS2_CHAR_PORTALCRAFT-BANE.title":"Aniquilación","STS2_CHAR_PORTALCRAFT-BANE.description":_kw_bane,
 "CANNOTBEEXHAUSTED.title":"No puede ser Agotado","CANNOTBEEXHAUSTED.description":_kw_cbe,
 "STS2_CHAR_PORTALCRAFT-CANNOTBEEXHAUSTED.title":"No puede ser Agotado","STS2_CHAR_PORTALCRAFT-CANNOTBEEXHAUSTED.description":_kw_cbe,
 "SUMMON.title":"Invocar","SUMMON.description":_kw_summon,
 "STS2_CHAR_PORTALCRAFT-SUMMON.title":"Invocar","STS2_CHAR_PORTALCRAFT-SUMMON.description":_kw_summon,
}

powers = {
 "STS2_CHAR_PORTALCRAFT-KEYWORD_DISPATCHER_POWER.title":"Despachador de Palabras Clave",
 "STS2_CHAR_PORTALCRAFT-KEYWORD_DISPATCHER_POWER.description":"Interno. Despacha efectos de palabras clave personalizadas.",
 "STS2_CHAR_PORTALCRAFT-KEYWORD_DISPATCHER_POWER.smartDescription":"Interno. Despacha efectos de palabras clave personalizadas.",
 "STS2_CHAR_PORTALCRAFT-EVO_POINTS_POWER.title":"Puntos de Evo",
 "STS2_CHAR_PORTALCRAFT-EVO_POINTS_POWER.description":"Interno. Lleva la cuenta de los puntos de evolución restantes este combate.",
 "STS2_CHAR_PORTALCRAFT-EVO_POINTS_POWER.smartDescription":"Interno. Lleva la cuenta de los puntos de evolución restantes este combate.",
 "STS2_CHAR_PORTALCRAFT-SUPER_EVO_POINTS_POWER.title":"Puntos de Súper Evo",
 "STS2_CHAR_PORTALCRAFT-SUPER_EVO_POINTS_POWER.description":"Interno. Lleva la cuenta de los puntos de superevolución restantes este combate.",
 "STS2_CHAR_PORTALCRAFT-SUPER_EVO_POINTS_POWER.smartDescription":"Interno. Lleva la cuenta de los puntos de superevolución restantes este combate.",
 "STS2_CHAR_PORTALCRAFT-EVO_USED_THIS_TURN_POWER.title":"Evo Usada Este Turno",
 "STS2_CHAR_PORTALCRAFT-EVO_USED_THIS_TURN_POWER.description":"Interno. Bloquea más evoluciones/superevoluciones por el resto de este turno.",
 "STS2_CHAR_PORTALCRAFT-EVO_USED_THIS_TURN_POWER.smartDescription":"Interno. Bloquea más evoluciones/superevoluciones por el resto de este turno.",
 "STS2_CHAR_PORTALCRAFT-SKYBOUND_ART_GAUGE_POWER.title":"Medidor de Arte Celestial",
 "STS2_CHAR_PORTALCRAFT-SKYBOUND_ART_GAUGE_POWER.description":"Tu Medidor Celestial. +1 al inicio de cada turno y +1 por evolución. A los [gold]10[/gold], se activan los efectos de [gold]Arte Celestial[/gold]. A los [gold]15[/gold], se activa el [gold]Súper Arte Celestial[/gold].",
 "STS2_CHAR_PORTALCRAFT-SKYBOUND_ART_GAUGE_POWER.smartDescription":"Tu Medidor Celestial. +1 al inicio de cada turno y +1 por evolución. A los [gold]10[/gold], se activan los efectos de [gold]Arte Celestial[/gold]. A los [gold]15[/gold], se activa el [gold]Súper Arte Celestial[/gold].",
 "STS2_CHAR_PORTALCRAFT-SKYBOUND_ART_POWER.title":"Arte Celestial Activo",
 "STS2_CHAR_PORTALCRAFT-SKYBOUND_ART_POWER.description":"Interno. Cada vez que se roba una carta de Arte Celestial, se activa su efecto.",
 "STS2_CHAR_PORTALCRAFT-SKYBOUND_ART_POWER.smartDescription":"Interno. Cada vez que se roba una carta de Arte Celestial, se activa su efecto.",
 "STS2_CHAR_PORTALCRAFT-SUPER_SKYBOUND_ART_POWER.title":"Súper Arte Celestial Activo",
 "STS2_CHAR_PORTALCRAFT-SUPER_SKYBOUND_ART_POWER.description":"Interno. Cada vez que se roba una carta de Súper Arte Celestial, se activa su efecto.",
 "STS2_CHAR_PORTALCRAFT-SUPER_SKYBOUND_ART_POWER.smartDescription":"Interno. Cada vez que se roba una carta de Súper Arte Celestial, se activa su efecto.",
 "STS2_CHAR_PORTALCRAFT-SKYBOUND_ART_AUTO_PLAYING_POWER.title":"Auto-Juego Celestial",
 "STS2_CHAR_PORTALCRAFT-SKYBOUND_ART_AUTO_PLAYING_POWER.description":"Interno. Indica que una carta de Arte Celestial se está jugando automáticamente; su OnPlay solo ejecuta el efecto del arte.",
 "STS2_CHAR_PORTALCRAFT-SKYBOUND_ART_AUTO_PLAYING_POWER.smartDescription":"Interno. Indica que una carta de Arte Celestial se está jugando automáticamente; su OnPlay solo ejecuta el efecto del arte.",
 "STS2_CHAR_PORTALCRAFT-ARTIFACTS_EXHAUSTED_POWER.title":"Artefactos Agotados",
 "STS2_CHAR_PORTALCRAFT-ARTIFACTS_EXHAUSTED_POWER.description":"Interno. Cuenta cuántas cartas de Artefacto se han agotado este combate.",
 "STS2_CHAR_PORTALCRAFT-ARTIFACTS_EXHAUSTED_POWER.smartDescription":"Interno. Cuenta cuántas cartas de Artefacto se han agotado este combate.",
 "STS2_CHAR_PORTALCRAFT-AUGMENTATION_BESTOWAL_POWER.title":"Otorgamiento de Aumento",
 "STS2_CHAR_PORTALCRAFT-AUGMENTATION_BESTOWAL_POWER.description":"Cada vez que juegas un [gold]Artefacto[/gold], gana 1 de Energía y roba 1 carta. Expira al final del turno.",
 "STS2_CHAR_PORTALCRAFT-AUGMENTATION_BESTOWAL_POWER.smartDescription":"Cada vez que juegas un [gold]Artefacto[/gold], gana 1 de Energía y roba 1 carta. Expira al final del turno.",
 "STS2_CHAR_PORTALCRAFT-RETRAFIA_AMULET_POWER.title":"Bendición de la Madre Divina",
 "STS2_CHAR_PORTALCRAFT-RETRAFIA_AMULET_POWER.description":"Todas las cartas de [gold]Artefacto[/gold] cuestan 0 al jugarse.",
 "STS2_CHAR_PORTALCRAFT-RETRAFIA_AMULET_POWER.smartDescription":"Todas las cartas de [gold]Artefacto[/gold] cuestan 0 al jugarse.",
 "STS2_CHAR_PORTALCRAFT-EUDIE_MAIDEN_REBORN_POWER.title":"Emblema: Eudie, Doncella Renacida",
 "STS2_CHAR_PORTALCRAFT-EUDIE_MAIDEN_REBORN_POWER.description":"Al final del turno, si tu mano tiene 5 cartas o menos, roba 1 carta adicional el próximo turno. Si tu mano tiene 6 cartas o más, gana 1 de Energía el próximo turno.",
 "STS2_CHAR_PORTALCRAFT-EUDIE_MAIDEN_REBORN_POWER.smartDescription":"Al final del turno, si tu mano tiene 5 cartas o menos, roba 1 carta adicional el próximo turno. Si tu mano tiene 6 cartas o más, gana 1 de Energía el próximo turno.",
 "STS2_CHAR_PORTALCRAFT-ANCIENT_CANNON_POWER.title":"Cañón Antiguo",
 "STS2_CHAR_PORTALCRAFT-ANCIENT_CANNON_POWER.description":"Cada vez que fusionas un Artefacto, inflige daño a un enemigo aleatorio.",
 "STS2_CHAR_PORTALCRAFT-ANCIENT_CANNON_POWER.smartDescription":"Cada vez que fusionas un Artefacto, inflige {Amount} de daño a un enemigo aleatorio.",
 "STS2_CHAR_PORTALCRAFT-REPLAY_NEXT_PUPPET_POWER.title":"Hilos de Marioneta",
 "STS2_CHAR_PORTALCRAFT-REPLAY_NEXT_PUPPET_POWER.description":"La próxima Marioneta que juegues se repite.",
 "STS2_CHAR_PORTALCRAFT-REPLAY_NEXT_PUPPET_POWER.smartDescription":"La próxima Marioneta que juegues se repite {Amount} vez(ces).",
 "STS2_CHAR_PORTALCRAFT-LIAM_CRAZED_CREATOR_POWER.title":"Emblema: Liam, Creador Enloquecido",
 "STS2_CHAR_PORTALCRAFT-LIAM_CRAZED_CREATOR_POWER.description":"Cada vez que se juega una Marioneta, gana 4 de Bloqueo e inflige 4 de daño a TODOS los enemigos.",
 "STS2_CHAR_PORTALCRAFT-LIAM_CRAZED_CREATOR_POWER.smartDescription":"Cada vez que se juega una Marioneta, gana {Amount} de Bloqueo e inflige {Amount} de daño a TODOS los enemigos.",
 "STS2_CHAR_PORTALCRAFT-ORCHIS_NEWFOUND_HEART_POWER.title":"Orchis, Corazón Recién Hallado",
 "STS2_CHAR_PORTALCRAFT-ORCHIS_NEWFOUND_HEART_POWER.description":"Este turno, cada [gold]Marioneta[/gold] añadida a tu mano obtiene [gold]Repetición[/gold] 1 y [gold]Aniquilación[/gold].",
 "STS2_CHAR_PORTALCRAFT-ORCHIS_NEWFOUND_HEART_POWER.smartDescription":"Este turno, cada [gold]Marioneta[/gold] añadida a tu mano obtiene [gold]Repetición[/gold] 1 y [gold]Aniquilación[/gold].",
 "STS2_CHAR_PORTALCRAFT-AXIA_HEIR_TO_DESTRUCTION_POWER.title":"Heredera de la Destrucción",
 "STS2_CHAR_PORTALCRAFT-AXIA_HEIR_TO_DESTRUCTION_POWER.description":"Al final del turno, Agota todos los [gold]Salmo Blanco, Nueva Revelación[/gold] y [gold]Salmo Negro, Nueva Revelación[/gold] de tu mano.",
 "STS2_CHAR_PORTALCRAFT-AXIA_HEIR_TO_DESTRUCTION_POWER.smartDescription":"Al final del turno, Agota todos los [gold]Salmo Blanco, Nueva Revelación[/gold] y [gold]Salmo Negro, Nueva Revelación[/gold] de tu mano {Amount} vez(ces).",
 "STS2_CHAR_PORTALCRAFT-BEELZEBUB_SUPREME_KING_POWER.title":"Emblema: Belcebú, Rey Supremo",
 "STS2_CHAR_PORTALCRAFT-BEELZEBUB_SUPREME_KING_POWER.description":"Cada vez que infliges daño a un enemigo, inflígele 2 de daño adicional.",
 "STS2_CHAR_PORTALCRAFT-BEELZEBUB_SUPREME_KING_POWER.smartDescription":"Cada vez que infliges daño a un enemigo, inflígele {Amount} de daño adicional.",
 "STS2_CHAR_PORTALCRAFT-RALMIA_SONIC_RACER_POWER.title":"Corredora Sónica",
 "STS2_CHAR_PORTALCRAFT-RALMIA_SONIC_RACER_POWER.description":"Por cada 4 Fusiones, gana 1 de Energía.",
 "STS2_CHAR_PORTALCRAFT-RALMIA_SONIC_RACER_POWER.smartDescription":"Por cada 4 Fusiones, gana {Amount} de Energía.",
 "STS2_CHAR_PORTALCRAFT-MECHANIZED_BEAST_POWER.title":"Bestia Mecanizada",
 "STS2_CHAR_PORTALCRAFT-MECHANIZED_BEAST_POWER.description":"Al ser atacada, devuelve 6 de daño. Expira el próximo turno.",
 "STS2_CHAR_PORTALCRAFT-MECHANIZED_BEAST_POWER.smartDescription":"Al ser atacada, devuelve {Amount} de daño. Expira el próximo turno.",
 "STS2_CHAR_PORTALCRAFT-IMARI_DEWDROP_POWER.title":"Bendición de Rocío",
 "STS2_CHAR_PORTALCRAFT-IMARI_DEWDROP_POWER.description":"Este turno, cada vez que juegas una Habilidad, añade Amiguitos de Imari a tu mano.",
 "STS2_CHAR_PORTALCRAFT-IMARI_DEWDROP_POWER.smartDescription":"Este turno, cada vez que juegas una Habilidad, añade Amiguitos de Imari a tu mano.",
 "STS2_CHAR_PORTALCRAFT-NOAH_DAMAGE_BONUS_POWER.title":"Hilo de la Muerte",
 "STS2_CHAR_PORTALCRAFT-NOAH_DAMAGE_BONUS_POWER.description":"Tus Marionetas infligen daño adicional.",
 "STS2_CHAR_PORTALCRAFT-NOAH_DAMAGE_BONUS_POWER.smartDescription":"Tus Marionetas infligen +{Amount} de daño adicional.",
 "STS2_CHAR_PORTALCRAFT-SLAUS_REVOLVING_WHEEL_POWER.title":"Emblema: Slaus, Rueda Giratoria de la Fortuna",
 "STS2_CHAR_PORTALCRAFT-SLAUS_REVOLVING_WHEEL_POWER.description":"Al inicio del turno, activa una habilidad aleatoria: reduce el coste de toda la mano en 1, gana Fuerza y Destreza, o cúrate. No puede repetir el efecto del turno anterior.",
 "STS2_CHAR_PORTALCRAFT-SLAUS_REVOLVING_WHEEL_POWER.smartDescription":"Al inicio del turno, activa una habilidad aleatoria: reduce el coste de toda la mano en 1 hasta el final del turno, gana 2 de Fuerza y 2 de Destreza hasta el final del turno, o cura 3 PV. No puede repetir el efecto del turno anterior.",
 "STS2_CHAR_PORTALCRAFT-FLOWERING_ARTISAN_POWER.title":"Artesana Floreciente",
 "STS2_CHAR_PORTALCRAFT-FLOWERING_ARTISAN_POWER.description":"Este turno, cada vez que juegas una Habilidad, inflige daño a TODOS los enemigos.",
 "STS2_CHAR_PORTALCRAFT-FLOWERING_ARTISAN_POWER.smartDescription":"Este turno, cada vez que juegas una Habilidad, inflige {Amount} de daño a TODOS los enemigos.",
 "STS2_CHAR_PORTALCRAFT-LU_WOH_INTENT_DEBUFF_POWER.title":"Emblema: Lu Woh, Luz Personificada",
 "STS2_CHAR_PORTALCRAFT-LU_WOH_INTENT_DEBUFF_POWER.description":"Durante los próximos 3 turnos enemigos, los enemigos que pretendan atacar pierden 4 de Fuerza ese turno.",
 "STS2_CHAR_PORTALCRAFT-LU_WOH_INTENT_DEBUFF_POWER.smartDescription":"Durante los próximos {Amount} turno(s) enemigo(s), los enemigos que pretendan atacar pierden 4 de [gold]Fuerza[/gold] ese turno.",
 "STS2_CHAR_PORTALCRAFT-ZWEI_SYMPHONIC_HEART_POWER.title":"Corazón Sinfónico",
 "STS2_CHAR_PORTALCRAFT-ZWEI_SYMPHONIC_HEART_POWER.description":"Este turno, cada vez que se juega una Marioneta, gana 4 de Bloqueo.",
 "STS2_CHAR_PORTALCRAFT-ZWEI_SYMPHONIC_HEART_POWER.smartDescription":"Este turno, cada vez que se juega una [gold]Marioneta[/gold], gana {Amount} de Bloqueo.",
}

allfiles = {"ancients":ancients,"enchantments":enchantments,"gameplay_ui":gameplay_ui,
 "settings_ui":settings_ui,"static_hover_tips":static_hover_tips,"relics":relics,
 "characters":characters,"card_selection":card_selection,"card_keywords":card_keywords,"powers":powers}
for fn,d in allfiles.items(): save(fn,d)

TAGS=("[gold]","[/gold]","[blue]","[/blue]","[purple]","[/purple]","[green]","[/green]","[sine]","[/sine]")
ok=True
for fn,d in allfiles.items():
    e=loadeng(fn)
    if set(e)!=set(d): ok=False; print(f"[{fn}] CLAVES faltan={set(e)-set(d)} extra={set(d)-set(e)}")
    for k in e:
        if k not in d: continue
        ev,sv=e[k],d[k]
        for t in TAGS:
            if ev.count(t)!=sv.count(t): ok=False; print(f"[{fn}] {k}: tag {t} {ev.count(t)}!={sv.count(t)}")
        et=sorted(re.findall(r'\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\(\))?\}',ev))
        st=sorted(re.findall(r'\{[A-Za-z][A-Za-z0-9]*(?::[a-zA-Z]+\(\))?\}',sv))
        if et!=st: ok=False; print(f"[{fn}] {k}: tokens {et} != {st}")
print("VALIDACION OK" if ok else "REVISAR ^")
