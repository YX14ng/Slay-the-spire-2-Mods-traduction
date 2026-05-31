# -*- coding: utf-8 -*-
import json, os
ESP = r"f:/Programs/Slay-the-spire-2-Mods-traduction/_translation_work/add/Manosaba/localization/esp/ancients.json"
d = json.load(open(ESP, encoding="utf-8"))
A = "THE_ARCHITECT.talk.MANOSABA-"

ov = {
  # NIKAIDO HIRO
  A+"NIKAIDO_HIRO.0-0.char": "En nombre de la correctitud, por la presente declaro:\neres la fuente de todo el mal de este mundo.",
  A+"NIKAIDO_HIRO.0-1.ancient": "¿Correctitud?\n¿Has venido a juzgarme, niñita?",
  A+"NIKAIDO_HIRO.0-2.char": "Esto no es un juicio. Es una corrección.\nEsta torre, esta corrupción, todo este orden equivocado que construiste: lo devolveré todo a su forma correcta.",
  A+"NIKAIDO_HIRO.0-3.ancient": "Vuelve al fondo de la torre, niña terca.\nTu [jitter][red]\"correctitud\"[/red][/jitter] no vale nada aquí.",
  A+"NIKAIDO_HIRO.1-0.char": "He vuelto.\nEsta vez completaré este juicio.",
  A+"NIKAIDO_HIRO.1-1.ancient": "¿Tú otra vez?\nSubes aquí una y otra vez con el poder de volver de la muerte. ¿No te parece patético?",
  A+"NIKAIDO_HIRO.1-2.char": "No importa cuántas veces empiece de nuevo, estaré aquí de pie.\nTus fechorías rendirán cuentas.",
  A+"NIKAIDO_HIRO.1-3.ancient": "Tu supuesta justicia\nno es más que autosuficiencia construida sobre incontables muertes.",
  A+"NIKAIDO_HIRO.2-0.char": "Definiste este mundo\ny luego dejaste que el caos y la masacre se pudrieran. Eres el pecador que más merece la ejecución.",
  A+"NIKAIDO_HIRO.2-1.ancient": "¿Qué sabrías tú del orden?\nNi siquiera puedes sostener tu propia [jitter][red]\"correctitud\"[/red][/jitter], ¿y aun así presumes acusarme?",
  A+"NIKAIDO_HIRO.2-2.char": "No dejaré que más vidas\nse desperdicien por tu arrogancia y obsesión.",
  A+"NIKAIDO_HIRO.2-3.ancient": "Je.\nEres tan necia y confiada como la mujer que me envenenó.",
  A+"NIKAIDO_HIRO.2-4.char": "Juzgaré tus pecados con mis propias manos.",
  A+"NIKAIDO_HIRO.2-5.ancient": "Entonces muéstrame\nsi ese supuesto juicio tuyo tiene el peso suficiente para herirme.",
  A+"NIKAIDO_HIRO.3-1r.ancient": "¿Has agotado incluso tus argumentos?\n¿O por fin has entendido que [jitter][red]las palabras no significan nada[/red][/jitter]?",
  A+"NIKAIDO_HIRO.3-2r.char": "…Vamos.",
  A+"NIKAIDO_HIRO.3-3r.ancient": "Así está mejor.",
  # HIKAMI MERURU
  A+"HIKAMI_MERURU.0-0r.char": "Por favor… ayúdame.\nPuedes traerla de vuelta, ¿no es así?",
  A+"HIKAMI_MERURU.0-1r.ancient": "Otra niña que se manchó ambas manos de sangre\npor una obsesión.",
  A+"HIKAMI_MERURU.0-2r.char": "Solo quiero volver a ver a la Gran Bruja…\nCueste lo que cueste.",
  A+"HIKAMI_MERURU.0-3r.ancient": "Ser abandonado es desagradable, ¿verdad?\nNo reparo pasados rotos hace tiempo por obsesiones necias.",
  # JOGASAKI NOAH (habla en tercera persona)
  A+"JOGASAKI_NOAH.0-0r.char": "¡Guaaa, por fin llegué!\n¿Esta es la cima misma de la torre?\nEl aire está muy seco. A Noah no le gusta mucho este lugar…",
  A+"JOGASAKI_NOAH.0-1r.ancient": "…Otra persona que no sabe nada sobre la creación se planta ante mí.\n¿Quién eres?",
  A+"JOGASAKI_NOAH.0-2r.char": "¡Noah es artista! Oí que creaste todo este mundo…\n¿También dibujaste todas esas cosas?\n¿Cómo hiciste una obra perfecta?\nEnséñale a Noah…",
  A+"JOGASAKI_NOAH.0-3r.ancient": "La creación no es un juego.\n¿Crees que es un garabato en un lienzo?",
  A+"JOGASAKI_NOAH.0-4r.char": "¡Noah no garabatea!",
  A+"JOGASAKI_NOAH.0-5r.ancient": "…Destruir tu entendimiento no es mi propósito.\nVete.",
  # TACHIBANA SHERRY
  A+"TACHIBANA_SHERRY.0-0r.char": "¡Vaya! Así que tú eres el verdadero culpable detrás de esta torre, ¿no?\n¡La Gran Detective Sherry por fin halló la verdad del caso!",
  A+"TACHIBANA_SHERRY.0-1r.ancient": "La verdad no es más que un dramita aburrido\nhilvanado por una niña que busca diversión.",
  A+"TACHIBANA_SHERRY.0-2r.char": "¡No es nada aburrido!\n¡Este es el mayor caso de la historia!",
  A+"TACHIBANA_SHERRY.0-3r.ancient": "Vuelve al fondo de la torre.\nMis creaciones nunca fueron juguetes para tu diversión.",
  # SAEKI MIRIA
  A+"SAEKI_MIRIA.0-0r.char": "Ajaja… No estoy muy acostumbrada a escenas como esta.\nNo me mires tan directamente.",
  A+"SAEKI_MIRIA.0-1r.ancient": "…Un disfraz extraño, un alma estable, una inofensividad autoproclamada.\nEres interesante.",
  A+"SAEKI_MIRIA.0-2r.char": "¿Interesante? Alguien tan insignificante como yo no merece tu atención.\n¿Podrías fingir que nunca me viste?",
  A+"SAEKI_MIRIA.0-3r.ancient": "La próxima vez.\nQuizás.",
  # TONO HANNA
  A+"TONO_HANNA.0-0r.char": "Como una señorita debida, debería ofrecer un saludo elegante antes de negociar…\nPuedes llamarme Hanna. ¿Puedo preguntar si eres el 'amo' de esta torre?",
  A+"TONO_HANNA.0-1r.ancient": "¿Una señorita noble?\nNada más que un sueño autoengañoso tejido de mentiras.",
  A+"TONO_HANNA.0-2r.char": "…¡Qué grosero!\n¡¿Acaso no oyes a una dama saludándote?!",
  A+"TONO_HANNA.0-3r.ancient": "Vuelve al fondo de la torre.\nNo fabrico felicidad falsa para niñas que huyen de la realidad.",
  # HASUMI LEIA
  A+"HASUMI_LEIA.0-0r.char": "Vine a exigir el protagonismo que me pertenece solo a mí.\nEl creador de este mundo debería darle a la protagonista más brillante la atención que merece.",
  A+"HASUMI_LEIA.0-1r.ancient": "¿Una actriz? Aquí no hay público, ni aplausos, ni nadie que te observe.\nAquí no tienes significado.",
  A+"HASUMI_LEIA.0-2r.char": "No necesito público.\nEsta torre me quitó todo, pero jamás pudo quitarme el cuerpo ni la mente.\nMi propia existencia es un escenario lo bastante poderoso para retener tu mirada.",
  A+"HASUMI_LEIA.0-3r.ancient": "…Qué obsesión tan lamentable.\n¿Crees que la sola confianza puede sacudir el orden de esta torre?\nTu resplandor no tiene valor aquí.",
  # KUROBE NANOKA
  A+"KUROBE_NANOKA.0-0r.char": "He visto tu pasado,\ny he visto el ciclo de masacre que creaste.",
  A+"KUROBE_NANOKA.0-1r.ancient": "¿Una niña que sobrevive espiando recuerdos\nse atreve a criticar el orden que creé?",
  A+"KUROBE_NANOKA.0-2r.char": "Con este disparo,\npondré fin a toda conclusión predeterminada.",
  A+"KUROBE_NANOKA.0-3r.ancient": "Entonces déjame ver si esa bala tuya\npuede atravesar el pasado y el futuro que he decretado.",
  # HOSHO MAGO
  A+"HOSHO_MAGO.0-0r.char": "Vaya, vaya. ¿Así que este es el dios que creó el mundo entero?\nQué inesperadamente ordinario.",
  A+"HOSHO_MAGO.0-1r.ancient": "¿Una niña llena de mentiras,\nincapaz siquiera de engañar a su propio corazón,\nse cree digna de burlarse de mí?",
  A+"HOSHO_MAGO.0-2r.char": "Después de todo, en este mundo\nnunca hubo sinceridad alguna de la que hablar.",
  A+"HOSHO_MAGO.0-3r.ancient": "Tu supuesto amor no es más que una torpe imitación de la posesividad.\nVuelve al fondo de la torre, farsante.",
  # NATSUME ANAN
  A+"NATSUME_ANAN.0-0r.char": "Te lo imploro aquí.\n¿Puedes borrar esta magia maldita y liberarme de esta jaula?",
  A+"NATSUME_ANAN.0-1r.ancient": "¿Y ahora deseas borrar los pecados que cometiste?\nQué risible.",
  A+"NATSUME_ANAN.0-2r.char": "Yo simplemente…\nno quiero que nadie más se vuelva infeliz.",
  A+"NATSUME_ANAN.0-3r.ancient": "¿Te falta hasta el valor para enfrentar tu pasado y aun así me pides liberación?",
  # SHITO ALISA
  A+"SHITO_ALISA.0-0r.char": "Oye, tú, el de allá arriba.\n¿Construiste esta maldita torre?\n¿Eres el supuesto 'creador'?",
  A+"SHITO_ALISA.0-1r.ancient": "Tú y esta torre son lo mismo.\nSiempre vienes a mí llena de ira y confusión.",
  A+"SHITO_ALISA.0-2r.char": "Déjate de tonterías.\nO me aplastas ahora, o te reduzco a cenizas. Deja de soltar esas palabras bonitas que me dan asco.",
  A+"SHITO_ALISA.0-3r.ancient": "Si buscas un juicio, te equivocaste de lugar.",
}
d.update(ov)
json.dump(d, open(ESP, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"ancients.json: {len(ov)} dialogos traducidos")
