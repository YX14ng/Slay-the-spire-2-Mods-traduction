# -*- coding: utf-8 -*-
import json, os
P = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/pendientes"
def wj(mod, lang, fname, data):
    d = os.path.join(P, mod, lang); os.makedirs(d, exist_ok=True)
    json.dump(data, open(os.path.join(d, fname), "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---------- Patchoulib (esp) ----------
wj("Patchoulib","esp","powers.json",{
 "PATCHOUIB-IGNITE_POWER.title":"Ignición",
 "PATCHOUIB-IGNITE_POWER.description":"Al inicio de tu turno, pierdes PV iguales a la acumulación, luego aumentas la acumulación en [blue]1[/blue].",
 "PATCHOUIB-IGNITE_POWER.smartDescription":"Al inicio de tu turno, pierdes [blue]{Amount}[/blue] PV, luego aumentas la acumulación en [blue]1[/blue].",
 "PATCHOUIB-FREEZE_POWER.title":"Congelación",
 "PATCHOUIB-FREEZE_POWER.description":"Reduce el daño infligido en una cantidad.\nAl final de tu turno, reduce las acumulaciones en [blue]1[/blue].",
 "PATCHOUIB-FREEZE_POWER.smartDescription":"Reduce el daño infligido en [blue]{Amount}[/blue].\nAl final de tu turno, reduce las acumulaciones en [blue]1[/blue].",
})
wj("Patchoulib","esp","static_hover_tips.json",{
 "IGNITE_POWER.title":"Ignición",
 "IGNITE_POWER.description":"Al inicio de tu turno, pierdes PV iguales a la acumulación, luego aumentas la acumulación en [blue]1[/blue].",
})

# ---------- RegentFemPortraits (esp) ----------
wj("RegentFemPortraits","esp","settings_ui.json",{
 "REGENTFEMPORTRAITS.mod_title":"Conversión Anime de Retratos de Cartas de Regent",
 "REGENTFEMPORTRAITS.mod_desc":"Reemplaza los retratos de cartas del personaje Regent con ilustraciones estilo anime, con varias opciones de filtro de suavizado.",
 "REGENTFEMPORTRAITS-ENABLE_ANTIALIASING_FILTER.title":"Activar filtro de suavizado",
 "REGENTFEMPORTRAITS-ENABLE_ANTIALIASING_FILTER.hover.title":"Activar filtro de suavizado",
 "REGENTFEMPORTRAITS-ENABLE_ANTIALIASING_FILTER.hover.desc":"Cuando está activado, se aplica filtrado de textura a los retratos de cartas para reducir el dentado en las vistas previas escaladas. Recomendado para mejores efectos visuales.",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE.title":"Modo de filtro",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE.hover.title":"Modo de filtro",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE.hover.desc":"Elige el modo de filtrado de textura para los retratos de cartas. Cada modo afecta la nitidez y la suavidad de los bordes. Se recomienda Bilineal con Anisotrópico.",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-Nearest.title":"Más cercano",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-Nearest.hover.title":"Más cercano",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-Nearest.hover.desc":"Nítido, conserva el estilo pixel art, puede tener dentado notable. Ideal para el estilo pixel art.",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-Linear.title":"Bilineal",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-Linear.hover.title":"Bilineal",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-Linear.hover.desc":"Visualización suave con bordes ligeramente difuminados. Ideal para mostrar imágenes grandes.",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-NearestMipmap.title":"Más cercano+Mipmap",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-NearestMipmap.hover.title":"Más cercano+Mipmap",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-NearestMipmap.hover.desc":"Equilibra nitidez y rendimiento; usa un Mipmap de menor resolución para las vistas previas escaladas.",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-LinearMipmap.title":"Lineal+Mipmap",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-LinearMipmap.hover.title":"Lineal+Mipmap",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-LinearMipmap.hover.desc":"Bordes suaves, menos dentado; usa Mipmap para mantener la calidad al escalar.",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-NearestAnisotropic.title":"Más cercano+Anisotrópico",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-NearestAnisotropic.hover.title":"Más cercano+Anisotrópico",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-NearestAnisotropic.hover.desc":"Alta nitidez, mantiene la definición en ángulos oblicuos; el filtrado anisotrópico mejora la visualización en ángulo.",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-LinearAnisotropic.title":"Lineal+Anisotrópico",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-LinearAnisotropic.hover.title":"Lineal+Anisotrópico",
 "REGENTFEMPORTRAITS-SELECTED_FILTER_MODE-LinearAnisotropic.hover.desc":"El filtrado más suave, recomendado para vistas previas escaladas. Combina las ventajas del filtrado lineal, Mipmap y anisotrópico.",
 "REGENTFEMPORTRAITS-TEXTURE_QUALITY.title":"Calidad de textura",
 "REGENTFEMPORTRAITS-TEXTURE_QUALITY.hover.title":"Calidad de textura",
 "REGENTFEMPORTRAITS-TEXTURE_QUALITY.hover.desc":"Controla el nivel de compresión de textura. Una calidad mayor usa más memoria de video pero muestra los retratos de cartas con más nitidez.",
 "REGENTFEMPORTRAITS-ENABLE_SOVEREIGN_BLADE_REPLACEMENT.title":"Activar reemplazo de SovereignBlade",
 "REGENTFEMPORTRAITS-ENABLE_SOVEREIGN_BLADE_REPLACEMENT.hover.title":"Activar reemplazo de SovereignBlade",
 "REGENTFEMPORTRAITS-ENABLE_SOVEREIGN_BLADE_REPLACEMENT.hover.desc":"Cuando está activado, el retrato de la carta SovereignBlade se reemplaza con ilustración anime y se muestra en estilo Ancient. Desactívalo para ver el retrato original.",
})

# ---------- ChenIronclad (esp) ----------
wj("ChenIronclad","esp","settings_ui.json",{
 "CHENIRONCLAD.mod_title":"Chen Ironclad",
 "CHENIRONCLAD-USE_CHEN_CARD_FRAME.title":"Activar marco de carta",
 "CHENIRONCLAD-USE_CHEN_CARD_FRAME.hover.desc":"Activa el recoloreado del marco de carta para Chen (Ironclad).",
 "CHENIRONCLAD-USE_CHEN_ENERGY.title":"Activar contador de energía",
 "CHENIRONCLAD-USE_CHEN_ENERGY.hover.desc":"Activa el recoloreado del contador de energía para Chen (Ironclad).",
 "CHENIRONCLAD-USE_CHEN_MULT_ARM.title":"Activar brazo de multijugador",
 "CHENIRONCLAD-USE_CHEN_MULT_ARM.hover.desc":"Activa el brazo personalizado de multijugador (piedra/papel/tijera/señalar) para Chen (Ironclad).",
 "CHENIRONCLAD-USE_CHIXIAO_HELLRAISER.title":"Activar Chi Xiao en Hellraiser",
 "CHENIRONCLAD-USE_CHIXIAO_HELLRAISER.hover.desc":"Reemplaza la animación de espada de Hellraiser con Chi Xiao.",
 "CHENIRONCLAD-DEBUG_MODE.title":"Activar modo de depuración",
 "CHENIRONCLAD-DEBUG_MODE.hover.desc":"Activa el modo de depuración, que imprime información en los logs; normalmente se deja desactivado para no saturarlos.",
})
# ---------- ChenIronclad (zhs) — le falta chino ----------
wj("ChenIronclad","zhs","settings_ui.json",{
 "CHENIRONCLAD.mod_title":"橙铁甲",
 "CHENIRONCLAD-USE_CHEN_CARD_FRAME.title":"启用卡牌边框",
 "CHENIRONCLAD-USE_CHEN_CARD_FRAME.hover.desc":"为橙（铁甲）启用卡牌边框重新着色。",
 "CHENIRONCLAD-USE_CHEN_ENERGY.title":"启用能量计数器",
 "CHENIRONCLAD-USE_CHEN_ENERGY.hover.desc":"为橙（铁甲）启用能量计数器重新着色。",
 "CHENIRONCLAD-USE_CHEN_MULT_ARM.title":"启用多人游戏手臂",
 "CHENIRONCLAD-USE_CHEN_MULT_ARM.hover.desc":"为橙（铁甲）启用自定义多人游戏手臂（石头/布/剪刀/指）。",
 "CHENIRONCLAD-USE_CHIXIAO_HELLRAISER.title":"启用赤霄·炼狱使者",
 "CHENIRONCLAD-USE_CHIXIAO_HELLRAISER.hover.desc":"将炼狱使者（Hellraiser）的剑动画替换为赤霄。",
 "CHENIRONCLAD-DEBUG_MODE.title":"启用调试模式",
 "CHENIRONCLAD-DEBUG_MODE.hover.desc":"启用调试模式，会在日志中打印调试信息；通常禁用以防止日志刷屏。",
})
print("Patchoulib, RegentFemPortraits (esp) y ChenIronclad (esp+zhs) traducidos")
