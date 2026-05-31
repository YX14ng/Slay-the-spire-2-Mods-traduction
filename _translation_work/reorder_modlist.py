import json, shutil, os
S = r"C:/Users/YX14n/AppData/Roaming/SlayTheSpire2/steam/76561199101398442/settings.save"
BAK = S + ".es_backup"
if not os.path.exists(BAK): shutil.copy(S, BAK)   # respaldo una sola vez
raw = open(S, encoding="utf-8-sig").read()
j = json.loads(raw)
ml = j["mod_settings"]["mod_list"]
TOP = ["BaseLib", "ModConfig"]
def key(m):
    i = m["id"]
    return (0, TOP.index(i)) if i in TOP else (1, i.lower())
ml_sorted = sorted(ml, key=key)
j["mod_settings"]["mod_list"] = ml_sorted
# escribir (JSON valido, UTF-8)
open(S, "w", encoding="utf-8").write(json.dumps(j, ensure_ascii=False, indent=2))
# verificar relectura
chk = json.loads(open(S, encoding="utf-8-sig").read())
print("Respaldo en:", BAK)
print("Nuevo orden:")
for n,m in enumerate(chk["mod_settings"]["mod_list"],1): print(f"  {n:2}. {m['id']}")
# bloque para el amigo
block = json.dumps(ml_sorted, ensure_ascii=False, indent=2)
open(r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/mod_list_PARA_AMIGO.json","w",encoding="utf-8").write(block)
print("\nBloque para el amigo guardado en _translation_work/mod_list_PARA_AMIGO.json")
