# -*- coding: utf-8 -*-
import json, os
ESP = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/add/Manosaba/localization/esp/characters.json"
d = json.load(open(ESP, encoding="utf-8"))  # ya tiene pronombres (su/ella) y nombres correctos

# solo traducimos frases; nombres (.title), pronombres y vacios se conservan
ov = {
  "MANOSABA-NIKAIDO_HIRO.description": "Te equivocas: no soy malvada. Soy la única que puede enderezar este mundo. Yo misma erradicaré el mal de este mundo.",
  "MANOSABA-NIKAIDO_HIRO.eventDeathPrevention": "¿Volví a repetir el ciclo?",
  "MANOSABA-NIKAIDO_HIRO.banter.alive.endTurnPing": "¡Apúrate y actúa!",

  "MANOSABA-HIKAMI_MERURU.description": "Solo quiero que todos sonrían, aunque sea un poco. Es lo único que puedo hacer…",
  "MANOSABA-HIKAMI_MERURU.banter.alive.endTurnPing": "T-tranquilo… tómate tu tiempo…",

  "MANOSABA-JOGASAKI_NOAH.description": "¿Noah no come hoy? Noah todavía va por la mitad de su pintura.",
  "MANOSABA-JOGASAKI_NOAH.banter.alive.endTurnPing": "¡Apúrate!",

  "MANOSABA-TACHIBANA_SHERRY.description": "Ponerme del lado divertido: ¡ese es mi credo!",
  "MANOSABA-TACHIBANA_SHERRY.banter.alive.endTurnPing": "¿Ah, sí…?",

  "MANOSABA-SAEKI_MIRIA.description": "E-este… soy Saeki Miria, ¿sí? Encantada~ Ajaja~",
  "MANOSABA-SAEKI_MIRIA.banter.alive.endTurnPing": "T-tranquilo, señor… puede tomarse su tiempo.",

  "MANOSABA-HASUMI_LEIA.description": "E-este… soy Hasumi Leia, ¿sí? Encantada~ Ajaja~",
  "MANOSABA-HASUMI_LEIA.banter.alive.endTurnPing": "T-tranquilo, señor… puede tomarse su tiempo.",

  "MANOSABA-KUROBE_NANOKA.description": "Soy Kurobe Nanoka. Encantada de conocerte.",

  "MANOSABA-TONO_HANNA.description": "Das lástima… Te recomendaría que te rindas.",
  "MANOSABA-TONO_HANNA.banter.alive.endTurnPing": "¿Qué… qué tan estúpido eres…?",

  "MANOSABA-HOSHO_MAGO.description": "Cuántos pequeñines adorables hay aquí… No puedo evitar relamerme, je je.",
  "MANOSABA-HOSHO_MAGO.banter.alive.endTurnPing": "¡Qué adorable!",

  "MANOSABA-NATSUME_ANAN.description": "Ahora mismo me siento muy mal. Si me hablas fuerte, solo logras que me sienta peor, así que… [Largo de aquí].",

  "MANOSABA-SHITO_ALISA.description": "Las llamas lo consumen todo, pero también alumbran la verdad.",
  "MANOSABA-SHITO_ALISA.banter.alive.endTurnPing": "Mientras quede una chispa, todavía podemos dar vuelta esto.",

  "MANOSABA-SAKURABA_EMA.description": "Próximamente.",
  "MANOSABA-SAKURABA_EMA.unlockText": "Este personaje aún no está disponible.",
  "MANOSABA-SAWATARI_COCO.description": "Próximamente.",
  "MANOSABA-SAWATARI_COCO.unlockText": "Este personaje aún no está disponible.",
  "MANOSABA-TSUKISHIRO_YUKI.description": "Próximamente.",
  "MANOSABA-TSUKISHIRO_YUKI.unlockText": "Este personaje aún no está disponible.",
}
d.update(ov)
json.dump(d, open(ESP, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"characters.json: {len(ov)} frases traducidas (nombres y pronombres conservados)")
