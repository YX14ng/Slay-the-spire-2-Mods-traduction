# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

This is a **translation project** for **Manosaba**, a *Slay the Spire 2* mod ("A mod inspired by
Magical Girl Witch Trials", by Clione). It is **not** a buildable source tree — it holds the mod's
distributable binary artifacts. The job here is localizing the mod's in-game text, not writing
application code. There are no build, lint, or test commands; do not invent them.

The repo name ("traduction") and the existing community localizations (e.g. the Korean translation
credited in the manifest) indicate the goal is producing additional language translations of this mod.

## Repository layout

Everything lives under [Manosaba/](Manosaba/) — the deployable mod folder:

- [Manosaba/Manosaba.json](Manosaba/Manosaba.json) — mod manifest. `id`/`name`/`pck_name`,
  `version` (currently `v1.6.4`), `dependencies` (requires the `BaseLib` mod loader),
  `has_pck`/`has_dll`, `affects_gameplay`. Bump `version` when shipping a translated build.
- `Manosaba/Manosaba.dll` (~1.4 MB) — the compiled **C# mod assembly** (game logic). Built against
  Godot 4 (`GodotSharp`) and the game's `MegaCrit.Sts2.Core.*` API plus `BaseLib.*`. This is compiled
  output, not editable source — only touch it if a translation requires code/formatter changes (see below).
- `Manosaba/Manosaba.pck` (~527 MB) — the **Godot 4.5 resource pack** (`GDPC` v3 header). Contains
  all art, audio, scenes, and the translatable text. **This is where virtually all translation work
  happens.**

## How the mod and its localization are structured

*Slay the Spire 2* and its mods run on **Godot 4.5 with C# (.NET/Mono)**. Mods are loaded by the
`BaseLib` mod loader (a dependency declared in the manifest).

Localization is driven by the game's `MegaCrit.Sts2.Core.Localization.LocManager`. The mod extends it:
- `Manosaba.Localization.Formatters` and the patch `Patch_LocManager_AddKotodamaIconsFormatter`
  (in the DLL) register custom text formatters / dynamic vars. The DLL does **not** hardcode the
  language folders — `BaseLib` auto-discovers them.
- **All translatable strings live in plain JSON inside the `.pck`**, under
  `Manosaba/localization/<lang>/`. There is one folder per language and the same **12 files** in each:
  `ancients, card_keywords, cards, characters, events, monsters, orbs, potions, powers, relics,
  settings_ui, static_hover_tips`.
- Shipped languages use **classic Slay the Spire 3-letter codes**: `eng`, `jpn`, `kor`, `zhs`
  (English is the source of truth). Spanish would be `spa`.
- Each JSON is a flat `"key": "value"` dictionary, e.g.
  `"MANOSABA-BATHROOM_TALK.title": "Bathroom Talk"`. **Keys are identical across all languages —
  only values are translated.** Preserve markup/tokens inside values: `[gold]...[/gold]`,
  `{Summon:diff()}`, `\n`, emojis. Total ≈ **1837 strings / ~97k chars** (English).

## PCK format & tooling

`Manosaba.pck` is a **Godot 4.5.1 `GDPC` v3** pack: header (112 bytes, with `file_base=112` and a
**directory offset at the end of the file**), `flags=2` (entry offsets are relative to `file_base`),
file data 16-byte aligned, then the directory (`file_count` + per-entry `path_len`/path padded to 4
bytes / `offset` u64 / `size` u64 / real `md5` / `flags` u32). No `.csv`/`.translation` resources
exist; text is the JSON above.

A validated extract/repack tool lives at [_translation_work/pck_tool.py](_translation_work/pck_tool.py)
(`list` / `extract` / `repack`). `repack` recomputes each file's md5 and adds/overwrites files by
res:// path. (`_translation_work/` is scratch, not part of the shipped mod.)

## Working with translations

1. **Extract**: `python _translation_work/pck_tool.py extract Manosaba/Manosaba.pck <out> Manosaba/localization/`
2. **Add Spanish**: create `Manosaba/localization/spa/` with the 12 files copied from `eng/`, then
   translate only the values (keys and tokens intact).
3. **Repack**: `python _translation_work/pck_tool.py repack Manosaba/Manosaba.pck Manosaba_new.pck <dir-containing Manosaba/localization/spa>`,
   then replace `Manosaba/Manosaba.pck`. Keep the `Manosaba` pack name (`pck_name` in the manifest).
4. Editing the **DLL** is rarely needed (it would require recompiling against the StS2 + BaseLib APIs).
5. For the `spa` folder to activate, the game must report language code `spa` — confirm against the
   base game's own localization folder names and verify in-game. Increment `version` in
   `Manosaba.json` for a translated release; `BaseLib` must be installed.
