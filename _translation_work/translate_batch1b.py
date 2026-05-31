# -*- coding: utf-8 -*-
import json, os
ENG = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/extracted/Manosaba/localization/eng"
ESP = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/add/Manosaba/localization/esp"

d = json.load(open(os.path.join(ENG,"settings_ui.json"), encoding="utf-8"))

# nombres de efectos (se reutilizaran en otros archivos)
PB = "Frecuencia de Reproducción"
def desc(nombre, tipo): return f"Elige con qué frecuencia {nombre} reproduce su {tipo} especial: siempre, una vez por partida o nunca."

ov = {
  # HIKAMI_MERURU: el .title es un nombre estilizado con flechas -> se conserva (no se toca)
  "MANOSABA-HIKAMI_MERURU_EXAID_EFFECT_FREQUENCY.hover.title": PB,
  "MANOSABA-HIKAMI_MERURU_EXAID_EFFECT_FREQUENCY.hover.desc": desc(d["MANOSABA-HIKAMI_MERURU_EXAID_EFFECT_FREQUENCY.title"], "SFX"),

  "MANOSABA-LABOURS_OF_HIRO_EFFECT_FREQUENCY.title": "Labores de Hiro",
  "MANOSABA-LABOURS_OF_HIRO_EFFECT_FREQUENCY.hover.title": PB,
  "MANOSABA-LABOURS_OF_HIRO_EFFECT_FREQUENCY.hover.desc": desc("Labores de Hiro", "SFX/VFX"),

  "MANOSABA-NOAH_FRIENDS_EFFECT_FREQUENCY.title": "Amigos Animales de Noah",
  "MANOSABA-NOAH_FRIENDS_EFFECT_FREQUENCY.hover.title": PB,
  "MANOSABA-NOAH_FRIENDS_EFFECT_FREQUENCY.hover.desc": desc("Amigos Animales de Noah", "BGM"),

  "MANOSABA-FIRE_JUDGEMENT_COURT_EFFECT_FREQUENCY.title": "Tribunal de Juicio de Fuego",
  "MANOSABA-FIRE_JUDGEMENT_COURT_EFFECT_FREQUENCY.hover.title": PB,
  "MANOSABA-FIRE_JUDGEMENT_COURT_EFFECT_FREQUENCY.hover.desc": desc("Tribunal de Juicio de Fuego", "BGM"),

  "MANOSABA-UNSHEATHE_BIOS_EFFECT_FREQUENCY.title": "Desenvainar",
  "MANOSABA-UNSHEATHE_BIOS_EFFECT_FREQUENCY.hover.title": PB,
  "MANOSABA-UNSHEATHE_BIOS_EFFECT_FREQUENCY.hover.desc": desc("Desenvainar", "BGM"),

  "MANOSABA-I_AM_REBORN_EFFECT_FREQUENCY.title": "He Renacido",
  "MANOSABA-I_AM_REBORN_EFFECT_FREQUENCY.hover.title": PB,
  "MANOSABA-I_AM_REBORN_EFFECT_FREQUENCY.hover.desc": desc("He Renacido", "BGM"),

  "MANOSABA-PRIDE_EFFECT_FREQUENCY.title": "Orgullo",
  "MANOSABA-PRIDE_EFFECT_FREQUENCY.hover.title": PB,
  "MANOSABA-PRIDE_EFFECT_FREQUENCY.hover.desc": desc("Orgullo", "BGM"),

  "MANOSABA-SFX_SETTINGS.title": "Ajustes de SFX",
  "MANOSABA-MANOSABA_SFX_VOLUME_PERCENT.title": "Volumen de SFX de Manosaba",
  "MANOSABA-MANOSABA_SFX_VOLUME_PERCENT.hover.title": "Volumen",
  "MANOSABA-MANOSABA_SFX_VOLUME_PERCENT.hover.desc": "Ajusta el volumen solo del SFX/BGM personalizado de Manosaba. No afecta el volumen del BGM del juego base.",

  "MANOSABA-LOBBY_SETTINGS.title": "Manosaba (el anfitrión ajusta para multijugador)",
  "MANOSABA-LOBBY_SETTINGS.enemy_hp_percent": "% de PV de enemigos",
  "MANOSABA-LOBBY_SETTINGS.enemy_attack_percent": "% de daño de ataque de enemigos",
  "MANOSABA-LOBBY_SETTINGS.murderous_percent": "% de daño de aliado por Impulso Asesino",
  "MANOSABA-LOBBY_SETTINGS.random_pool": "Conjunto de espacios aleatorios",
  "MANOSABA-LOBBY_SETTINGS.random_pool_manosaba_only": "Solo Manosaba",
  "MANOSABA-LOBBY_SETTINGS.random_pool_all": "Todos los personajes (vanilla)",
}
d.update(ov)
json.dump(d, open(os.path.join(ESP,"settings_ui.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"escrito settings_ui.json ({len(d)} claves, {len(ov)} traducidas, 1 nombre estilizado conservado)")
