# Glosario de traducción — Manosaba → Español (LATAM / código `esp`)

Variante: **Español (Latinoamérica)** = código de carpeta **`esp`** en StS2 (`spa` = España/castellano).
El jugador debe tener el juego en "Español (Latinoamérica)" para que cargue.

## Reglas de estilo (imitar el español oficial de StS2)

- **Registro:** 2ª persona singular, presente de indicativo. NO imperativo.
  - `Deal X damage.` → `Infliges X de daño.`
  - `Gain X Block.` → `Obtienes X de [gold]bloqueo[/gold].`
  - `Apply X Vulnerable.` → `Aplicas X de [gold]vulnerabilidad[/gold].`
  - `Gain X [gold]Majoka[/gold].` → `Obtienes X de [gold]Majoka[/gold].`
- **Términos `[gold]...[/gold]` van en minúscula** dentro del texto de cartas/poderes
  (`[gold]bloqueo[/gold]`, `[gold]vulnerabilidad[/gold]`), salvo nombres propios (Majoka, Kotodama,
  nombres de personajes), que conservan mayúscula.
- **Preservar SIEMPRE, sin tocar:** las claves JSON, las variables `{Var:diff()}` / `{X:...}`,
  los tags BBCode (`[gold]`, `[b]`, `[i]`, `[color=X]`, `[jitter]`, `[sine]`, etc.), los `\n`,
  los emojis y los `?` decorativos (p. ej. `Sakuraba Ema?`). Mismo número de tags que el inglés.
- Títulos de cartas/poderes/reliquias: en mayúscula inicial natural en español.

## Términos de mecánica StS2 (oficiales del juego base, código `esp`)

| Inglés | Español oficial |
|---|---|
| Block | bloqueo |
| Strength | fuerza |
| Dexterity | destreza |
| Energy | energía |
| Exhaust | agotamiento (verbo: se agota) |
| Exhaust Pile | pila de agotamiento |
| Draw Pile | pila de robo (UI: "Mazo de robo") |
| Discard Pile | pila de descarte (UI: "Mazo de descarte") |
| Hand | mano |
| Weak | debilitamiento |
| Vulnerable | vulnerabilidad |
| Poison | veneno |
| Burn | quemadura |
| Dazed | deslumbre |
| Wound | herida |
| Doom | condena |
| Intangible | intangibilidad |
| Ethereal | evanescencia |
| Vigor | vigor |
| Stun | aturdimiento |
| Summon | invocación |
| Soar | elevación |
| Evoke | descarga |
| Replay | rejugar |
| Transform | transformación |
| Thorns | espinas |
| Plating | revestimiento |
| Buffer | búfer |
| Artifact | artefacto |
| Void | vacío |
| Orb Slot | espacio de orbe |
| Gold | oro |
| Relic | reliquia |
| Double Damage | daño doble |
| Elite | enemigo élite |
| Boss | jefe |
| Healing | curación |
| Status | estado |

> Más términos en `basegame/localization/esp/*.json` (memoria de 5511 cadenas oficiales). 251 cadenas
> de Manosaba coinciden EXACTO con el juego base y se rellenan con su traducción oficial.

## Términos de lore de Manosaba / *Magical Girl Witch Trials* (魔女裁判)

Decisión por defecto: **los términos-firma japoneses romanizados se conservan** (como en las versiones
EN/zh/ko del juego), los descriptivos se traducen a español natural.

| Término | Decisión | Nota |
|---|---|---|
| Majoka (魔女化) | **Majoka** (invariable) | Recurso/poder estrella del mod. Nombre propio. |
| Kotodama (言霊) | **Kotodama** | "Espíritu de las palabras"; poder textual de Anan. |
| Mahou (魔法) | **Mahou** | Tipo/keyword de carta = magia de bruja. |
| Suspicion | **Sospecha** | Mecánica de los juicios. |
| Clue | **Pista** | |
| Madness | **Locura** | |
| Sanity | **Cordura** | |
| Murderous Impulse | **Impulso Asesino** | "high murderous instinct" del juego. |
| Witch Island Prison | **Prisión de la Isla de las Brujas** | |
| Investigation Moment | **Momento de Investigación** | |
| Blood Orb(s) | **Orbe(s) de Sangre** | |
| Fireball Swarm | **Enjambre de Bolas de Fuego** | |
| Gun Shot | **Disparo** | mecánica de Nanoka |
| Simple Spear | **Lanza Simple** | |
| Sword Technique | **Técnica de Espada** | |
| Two Swords | **Dos Espadas** | |
| Great Detective's Due | **Honorarios del Gran Detective** | revisar en contexto |

### Cartas de Tarot (arcanos mayores → nombres estándar en español)
The World→El Mundo · The Moon→La Luna · The Sun→El Sol · The Star→La Estrella ·
The Lovers→Los Enamorados · The High Priestess→La Sacerdotisa · Temperance→La Templanza ·
Justice→La Justicia · The Tower→La Torre

### Nombres de personajes — SE CONSERVAN (romanización japonesa, sin traducir)
Sakuraba Ema · Nikaido Hiro · Jogasaki Noah · Hasumi Leia · Kurobe Nanoka · Shito Alisa ·
Natsume Anan · Tono Hanna · Saeki Miria · Hikami Meruru · Sawatari Coco · Tachibana Sherry

## Pendiente de confirmar con el usuario
- ¿Conservar Majoka/Kotodama/Mahou romanizados (recomendado) o traducirlos?
- Variante esp (LATAM) confirmada por perfil del usuario; cambiar a `spa` si juega en castellano.
