# AGENTS.md — Slay the Spire 2 Mods Traduction

Contexto para Hermes Agent y otros agentes de IA trabajando en este repositorio.

## Proyecto

Traducción de mods de *Slay the Spire 2*, empezando por **Manosaba** (mod inspired by Magical Girl Witch Trials, de Clione). El repositorio contiene los artefactos binarios del mod (no es un árbol de código fuente compilable) y el trabajo consiste en localizar texto del juego a nuevos idiomas.

## Estructura

| Directorio | Propósito |
|-----------|-----------|
| `Manosaba/` | Carpeta del mod desplegable (.dll, .pck, manifiesto) |
| `Manosaba/localization/` | Archivos JSON de traducción por idioma (eng, jpn, kor, zhs) |
| `Traducidos/` | Traducciones completadas |
| `Traducidos_beta/` | Traducciones en revisión |
| `Por_traducir/` | Pendientes de traducción |
| `_translation_work/` | Herramientas de desarrollo (pck_tool.py) |
| `BetterSpire2/` / `BetterSpire2_localization/` | Otros mods en progreso |

## Operaciones comunes

- **Agregar un idioma nuevo**: crear carpeta con código ISO 639-2 (3 letras) en `Manosaba/localization/`, copiar los 12 JSON de `eng/`, traducir valores
- **Extraer textos**: `python _translation_work/pck_tool.py extract Manosaba/Manosaba.pck <out> Manosaba/localization/`
- **Reempaquetar**: `python _translation_work/pck_tool.py repack Manosaba/Manosaba.pck Manosaba_new.pck <dir>`
- **Actualizar versión**: modificar `version` en `Manosaba/Manosaba.json`

## Reglas

- NO modificar las claves JSON — solo traducir valores
- Preservar markup: `[gold]...[/gold]`, `{Summon:diff()}`, `\n`, emojis
- Mantener consistencia terminológica entre archivos (mismos términos = mismas traducciones)
- El manifiesto (`Manosaba.json`) requiere `BaseLib` como dependencia
- ~1837 strings / ~97k caracteres en inglés (source of truth)
