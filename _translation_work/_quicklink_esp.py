# -*- coding: utf-8 -*-
# Traduce QuickLink (localization/en.json plano, placeholders {0}/{1}) -> esp.json, valida e inyecta.
import importlib.util,os,sys,glob,json,re,shutil,io,contextlib
def out(s): sys.stdout.buffer.write((str(s)+"\n").encode("utf-8"))
spec=importlib.util.spec_from_file_location("pt","_translation_work/pck_tool.py"); pt=importlib.util.module_from_spec(spec); spec.loader.exec_module(pt)
SM=r"C:/Program Files (x86)/Steam/steamapps/common/Slay the Spire 2/mods"
BS=chr(92)
pck=glob.glob(f"{SM}/QuickLink/*.pck")[0]
with open(pck,"rb") as f:
    ents,h=pt.read_dir(f); fb=h[5]; en=None
    for e in ents:
        p=e['path'].replace(BS,'/')
        if p.endswith('localization/en.json'): f.seek(e['off']+fb); en=json.loads(f.read(e['size']))

ESP={
 "combat_button":"Reiniciar Combate",
 "combat_button_tooltip":"Solicita un reinicio completo del combate desde el checkpoint de la sala actual. Arrastra para mover.",
 "combat_button_busy_tooltip":"QuickLink ya está procesando otra solicitud.",
 "combat_button_no_checkpoint_tooltip":"Aún no hay checkpoint de entrada a la sala disponible.",
 "dialog_combat_reset_title":"Solicitud de reinicio de combate",
 "dialog_combat_reset_body":"El anfitrión quiere reiniciar este combate al checkpoint de entrada a la sala. ¿Aceptar?",
 "dialog_accept":"Aceptar",
 "dialog_always_agree":"Aceptar siempre",
 "dialog_decline":"Rechazar",
 "dialog_map_rewind_title":"Retroceder Nodo",
 "dialog_map_rewind_confirm":"Retroceder",
 "dialog_map_rewind_before":"Antes",
 "dialog_map_rewind_after":"Después",
 "dialog_cancel":"Cancelar",
 "dialog_map_rewind_confirm_body":"¿Retroceder a este nodo?\n\n{0}\n\nEsto volverá a entrar al nodo.",
 "dialog_map_rewind_combat_body":"Elige cómo retroceder este nodo de combate.\n\n{0}\n\nAntes: vuelve a entrar y pelea el nodo de nuevo.\nDespués: vuelve al estado resuelto del nodo y elige la siguiente ruta sin repetir la pelea.",
 "map_history_button":"Historial de Checkpoints",
 "map_history_title":"Historial de Checkpoints",
 "map_history_empty":"Aún no hay checkpoints disponibles.",
 "map_history_recent_section":"Nodos Recientes",
 "map_history_act_start_section":"Inicios de Acto",
 "map_history_busy":"QuickLink está ocupado en este momento.",
 "toast_no_checkpoints":"Aún no hay checkpoints disponibles.",
 "toast_flow_busy":"QuickLink ya está procesando otro retroceso.",
 "toast_notifying":"Notificando a los jugadores...",
 "toast_warning":"El anfitrión inició un retroceso de QuickLink. Reconectando pronto...",
 "toast_returning_menu":"Volviendo al menú principal...",
 "toast_rehosting":"Recreando la sala de Steam...",
 "toast_waiting_players":"Sala creada. Esperando jugadores...",
 "toast_reconnecting":"Reconectando automáticamente... ({0}/{1})",
 "toast_reconnected":"¡Reconectado! Marcando listo automáticamente...",
 "toast_ready":"Listo. Esperando para empezar...",
 "toast_reconnect_failed":"Falló la reconexión automática. Unite al anfitrión manualmente desde tus amigos de Steam.",
 "toast_autohost_failed":"No se pudo recrear la sala automáticamente. Hospedá manualmente.",
 "toast_players_still_reconnecting":"Los jugadores aún se están reconectando. Usá la sala de carga manualmente si hace falta.",
 "toast_checkpoint_capture_failed":"QuickLink no pudo capturar un checkpoint.",
 "toast_combat_reset_requested":"El anfitrión solicitó un reinicio de combate.",
 "toast_combat_reset_accepted":"Reinicio de combate aceptado. Esperando al anfitrión...",
 "toast_combat_reset_declined":"Reinicio de combate rechazado.",
 "toast_combat_reset_cancelled":"La solicitud de reinicio de combate fue cancelada.",
 "toast_combat_approval_rejected":"Un jugador rechazó el reinicio de combate.",
 "toast_combat_approval_timed_out":"La solicitud de reinicio de combate expiró.",
 "toast_combat_approval_failed":"La solicitud de reinicio de combate falló.",
 "transition_resetting_battle":"Reiniciando combate...",
 "transition_restoring_checkpoint":"Restaurando checkpoint...",
 "transition_reconnecting":"Reconectando jugadores...",
 "transition_loading_battle":"Cargando combate...",
 "transition_loading_checkpoint":"Cargando checkpoint...",
 "toast_combat_waiting_approvals":"Esperando aprobaciones... ({0}/{1})",
 "map_unknown":"Desconocido",
 "map_shop":"Tienda",
 "map_treasure":"Tesoro",
 "map_restsite":"Zona de Descanso",
 "map_monster":"Monstruo",
 "map_elite":"Élite",
 "map_boss":"Jefe",
 "map_ancient":"Ancestro",
 "checkpoint_format":"Acto {0} · Piso {1} · {2} · PV {3}/{4} · {5}O",
 "checkpoint_current":"Actual",
 "checkpoint_act_start":"Inicio de Acto",
}
ph=re.compile(r"\{\d+\}")
prob=0; miss=[]
for k,v in en.items():
    if k not in ESP: miss.append(k); continue
    e=ESP[k]
    if sorted(ph.findall(v))!=sorted(ph.findall(e)): out(f"  {k}: placeholders {sorted(ph.findall(e))}!={sorted(ph.findall(v))}"); prob+=1
    if v.count(chr(10))!=e.count(chr(10)): out(f"  {k}: saltos {e.count(chr(10))}!={v.count(chr(10))}"); prob+=1
extra=[k for k in ESP if k not in en]
out(f"faltan={miss} extra={extra} problemas={prob}")
if prob==0 and not miss and not extra:
    stg="_translation_work/beta_dl/_esp_QuickLink/QuickLink/localization"; os.makedirs(stg,exist_ok=True)
    json.dump(ESP,open(f"{stg}/esp.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)
    new="_translation_work/beta_dl/_new_QuickLink.pck"
    with contextlib.redirect_stdout(io.StringIO()):
        pt.cmd_repack(pck,new,"_translation_work/beta_dl/_esp_QuickLink")
    for dst in [f"{SM}/QuickLink","Traducidos/QuickLink"]:
        os.makedirs(dst,exist_ok=True)
        sdir=os.path.dirname(pck)
        for fx in os.listdir(sdir):
            if fx.endswith((".dll",".json")):
                s=os.path.join(sdir,fx); dd=os.path.join(dst,fx)
                if os.path.abspath(s)!=os.path.abspath(dd): shutil.copy(s,dd)
        shutil.copy(new,os.path.join(dst,os.path.basename(pck)))
    os.remove(new)
    with open(f"{SM}/QuickLink/{os.path.basename(pck)}","rb") as f:
        ents,h=pt.read_dir(f); ok=any(e['path'].replace(BS,'/').endswith('localization/esp.json') for e in ents)
    out(f"QuickLink: OK ✓ esp.json inyectado={ok} -> mods/ + Traducidos/")
