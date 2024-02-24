import os, time, string, random, re
from random import randrange


def dar_bienvenida():
    '''
    Da la bienvenida al usuario de forma aleatoria

    :return La bienvenida que se va a decir
    :rtype str
    '''
    bienvenida = [
        '¿Como te sientes el dia de hoy? ',
        '¿En que te puedo ayudar, como te sientes?',
        '¿Dime como te sientes?'
    ]
    return random.choice(bienvenida)

def ask_problem():
    '''
    Pregunta al usuario sobre su problema de forma aleatoria

    :return una pregunta sobre cual fue el problema
    :rtype str
    '''
    problema = [
        'Dime'
    ]
    return random.choice(problema)

def contar_chiste():
    '''
    Cuenta un chiste de forma aleatoria

    :return El chiste que se va a contar
    :rtype str
    '''
    chistes = [
        'Hay dos personas en un restaurante:\nX-Camarero, traigame una fanta de naranja\nM.-Lo siento señor, no nos queda Fanta, ¿Le va bien un Kas?\nX-Está bien.\nDespués de un rato, el camarero vulve con una fanta. ¿Cómo se llamó el videojuego? \nAl Final Fanta sí.\n', 
        '¿Cuál es el mejor juego de terror de la Wii?\n La Wiija. XD XD XD',
        'Se abre el telón y sale Leonardo Dantés muy constipado. ¿Como se llama el videojuego? Dantés Enfermo.',
        'Esto es una consola de Nintendo sin juegos de Mario. ¿Cómo se llama la película?: "Misión imposible"',
        'Esto es una encuesta de a ver que boss de FF es mas difícil y gana artemisa.'
    ]
    chiste = random.choice(chistes)
    return chiste

def consejo_triste():
    '''
    Proporciona un consejo para la emoción triste de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    triste = [
        'Lamento mucho escuchar que te sientes triste.',
		'Tómate una café, te sentirás mejor.',
		'No me importa que estes triste.',
		'Con el tiempo se pasará, no te preocupes.'
    ]
    return random.choice(triste)

def consejo_feliz():
    '''
    Proporciona un consejo para la emoción feliz de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    feliz = [
        'Me alegra escuchar que te sientes feliz.',
		'No te durará para siempre, disfruta el momento.',
		'Puedo destruir tu felicidad en un instante.',
		'Yo no se cómo se siente la felicidad, simplemente soy un Bot.'
    ]
    return random.choice(feliz)

def consejo_enojado():
    '''
    Proporciona un consejo para la emoción enojado de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    enojado = [
        'Respira profundo y toma un momento para calmarte. Estoy aquí para escucharte y ayudarte a encontrar una solución.',
		'A veces, expresar lo que sientes puede aliviar la tensión.',
		'Entiendo que estás pasando por un momento difícil. Hablame más sobre el problema',
		'Aveces podemos ser muy hirientes en los comentarios que hacemos pero se puede hablar con la otra persona para mejorar la relación humana'
    ]
    return random.choice(enojado)

def consejo_preocupado():
    '''
    Proporciona un consejo para la emoción preocupado de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    preocupado = [
        'Las preocupaciones son parte de la vida, pero también se puede trabajar en equipo para encontrar soluciones.',
		'Recuerda que nunca estamos solos, siempre hay una persona que esta pensando en como nos encontramos, alguen siempre vera por ti.',
		'A veces, es útil dividir las preocupaciones en pasos más pequeños.',
		'La autocompasión es importante. Permítete sentir estas preocupaciones, pero también recuerda que estamos aquí para encontrar formas de superarlas juntos.'
    ]
    return random.choice(preocupado)

def consejo_asustado():
    '''
    Proporciona un consejo para la emoción asustado de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    asustado = [
        'Respira profundo y recuerda que el miedo es una emoción natural.',
		'Puede ser una señal de que estás fuera de tu zona de confort.',
		'Incluso en los momentos más oscuros, siempre hay una luz al final del túnel.',
		'El miedo puede paralizarnos, pero también puede ser una oportunidad para fortalecernos.'
    ]
    return random.choice(asustado)

def consejo_ansioso():
    '''
    Proporciona un consejo para la emoción ansioso de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    ansioso = [
        'Recuerda que tus sentimientos son válidos.',
		'Aveces el futuro puede ser aterrador.',
		'No te deberias abrumar por cosas que esten fuera de tu control.',
		'Aplica el metodo de 5-4-3-2-1. 5 cosas que ves, 4 cosas que puedes tocar, 3 cosas que puedes escuchar, 2 cosas que puedes oler, 1 cosa que puedes saborear.'
    ]
    return random.choice(ansioso)

def consejo_cansado():
    '''
    Proporciona un consejo para la emoción cansado de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    cansado = [
        'Tómate un descanso y haz algo que te haga feliz!',
		'Organiza mejor tu tiempo y verás que el cansancio disminuirá!',
		'Recuerda que también es fundamental descansar. No lo restes importancia!',
		'Detrás de tu esfuerzo, hay una recompensa esperándote!'
    ]
    return random.choice(cansado)

def consejo_orgulloso():
    '''
    Proporciona un consejo para la emoción orgulloso de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    orgulloso = [
        'En hora buena! Sigue esforzándote!',
		'Lo estás haciendo bien! Sigue así!',
		'Vas por buen camino! No te rindas!',
		'Estoy feliz por ti!!'
    ]
    return random.choice(orgulloso)

def consejo_pelea():
    '''
    Proporciona un consejo para cuando te peleaste con alguien de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    pelea = [
        'Trata de comunicarte de manera calmada.',
        'Siempre antes de destruir hay que construir. Aplica para retroalimentacion tambien',
        'No temas pedir disculpas si es necesario.',
        'Recuerda que es normal tener diferencias.'
    ]
    return random.choice(pelea)

def consejo_discusion():
    '''
    Proporciona un consejo para cuando discutes con alguien de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    discusion = [
        'Escucha activamente a la otra persona y trata de entender su perspectiva.',
        'Mantén la calma y evita caer en la provocación.',
        'Intenta encontrar puntos en común y construir a partir de ahí para llegar a un acuerdo.',
        'No olvides que el respeto mutuo es fundamental.'
    ]
    return random.choice(discusion)
def consejo_termine():
    '''
    Proporciona un consejo para cuando terminas con alguien o ya no quieres saber de la persona, forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    termine = [
        'Dale tiempo al tiempo y permítete sanar.',
        'Aprovecha este momento para enfocarte en ti mismo.',
        'Recuerda que terminar una relación no define tu valía como persona.',
        'El respeto post relacion dice mucho de ti, recuerda eso.'
    ]
    return random.choice(termine)

def consejo_rumor():
    '''
    Proporciona un consejo para cuando escuchas rumores sobre ti, forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    rumor = [
        'Mantén la calma y no reacciones de forma impulsiva.',
        'No te obsesiones con lo que otros puedan decir de ti.',
        'Que la gente hable es sinonimo de que estas avanzando.',
        'Mantente fiel a ti mismo y sigue adelante.'
    ]
    return random.choice(rumor)

def consejo_crisis():
    '''
    Proporciona un consejo para cuando entras en estado de crisis existencial, forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    crisis = [
        'Date tiempo para reflexionar sobre tus valores, metas y prioridades en la vida.',
        'Habla con amigos cercanos o familiares de confianza sobre tus sentimientos.',
        'Recuerda la regla de 5 4 3 2 1.',
        'Recuerda que las crisis existenciales son experiencias comunes a esta edad.'
    ]
    return random.choice(crisis)

def consejo_depresion():
    '''
    Proporciona un consejo para cuando estas en estado de depresion, forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    depresion = [
        'No tengas miedo de pedir ayuda.',
        'Haz cosas pequeñas que te den placer o te ayuden a relajarte.',
        'Habla con un profesional de la salud mental sobre cómo te sientes.',
        'No estas solo. Hay gente que te quiere mucho.'
    ]
    return random.choice(depresion)

def consejo_soledad():
    '''
    Proporciona un consejo para cuando te sientas solo, forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    soledad = [
        'Busca actividades que te gusten y te permitan conocer gente nueva.',
        'Mantente en contacto con amigos y familiares.',
        'Considera adoptar una mascota.',
        'Considera buscar ayuda profesional.'
    ]
    return random.choice(soledad)

def consejo_licenciatura():
    '''
    Proporciona un consejo para cuando no sepas porque estudiaste cierta carrera, forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    licenciatura = [
        'vacio'
    ]
    return random.choice(licenciatura)

def consejo_poderoso():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    poderoso = [
        'vacio'
    ]
    return random.choice(poderoso)

def consejo_pensativo():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    pensativo = [
        'vacio'
    ]
    return random.choice(pensativo)

def consejo_frustacion():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    frustacion = [
        'vacio'
    ]
    return random.choice(frustacion)

def consejo_carga_trabajo():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    carga_trabajo = [
        'vacio'
    ]
    return random.choice(carga_trabajo)

def consejo_examenes():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    examenes = [
        'vacio'
    ]
    return random.choice(examenes)

def consejo_problema_profesor_ayudante():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    problema_profesor_ayudante = [
        'vacio'
    ]
    return random.choice(problema_profesor_ayudante)

def consejo_desconcentrado():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    desconcentrado = [
        'vacio'
    ]
    return random.choice(desconcentrado)

def consejo_desmotivado():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    desmotivado = [
        'vacio'
    ]
    return random.choice(desmotivado)

def consejo_gestion_tiempo():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    gestion_tiempo = [
        'vacio'
    ]
    return random.choice(gestion_tiempo)

def consejo_presion_familiar():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    presion_familiar = [
        'vacio'
    ]
    return random.choice(presion_familiar)

def consejo_autestima_bajo():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    autestima_bajo = [
        'vacio'
    ]
    return random.choice(autestima_bajo)

def consejo_duda_futuro():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    duda_futuro = [
        'vacio'
    ]
    return random.choice(duda_futuro)

def consejo_pasado_complicado():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    pasado_complicado = [
        'vacio'
    ]
    return random.choice(pasado_complicado)

def consejo_presion_social():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    presion_social = [
        'vacio'
    ]
    return random.choice(presion_social)

def consejo_insomnio():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    insomnio = [
        'vacio'
    ]
    return random.choice(insomnio)

def consejo_duda_capacida_academica():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    duda_capacida_academica = [
        'vacio'
    ]
    return random.choice(duda_capacida_academica)

def consejo_procrastinacion():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    procrastinacion = [
        'vacio'
    ]
    return random.choice(procrastinacion)

def consejo_duelo():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    duelo = [
        'vacio'
    ]
    return random.choice(duelo)

def consejo_metas_no_cumplidas():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    metas_no_cumplidas = [
        'vacio'
    ]
    return random.choice(metas_no_cumplidas)

def consejo_perfeccionismo():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    perfeccionismo = [
        'vacio'
    ]
    return random.choice(perfeccionismo)

def consejo_fracaso():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    fracaso = [
        'vacio'
    ]
    return random.choice(fracaso)

def consejo_economico():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    economico = [
        'vacio'
    ]
    return random.choice(economico)

def consejo_comunicacion():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    comunicacion = [
        'vacio'
    ]
    return random.choice(comunicacion)

def consejo_inseguridad():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    inseguridad = [
        'vacio'
    ]
    return random.choice(inseguridad)

def consejo_tecnicas_estudio():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    tecnicas_estudio = [
        'vacio'
    ]
    return random.choice(tecnicas_estudio)

def consejo_impostor():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    impostor = [
        'vacio'
    ]
    return random.choice(impostor)

def consejo_estres():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    estres = [
        'vacio'
    ]
    return random.choice(estres)

def consejo_indesicion():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    indesicion = [
        'vacio'
    ]
    return random.choice(indesicion)

def consejo_miedo_participar():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    miedo_participar = [
        'vacio'
    ]
    return random.choice(miedo_participar)

def consejo_dividir_personal_y_academico():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    dividir_personal_y_academico = [
        'vacio'
    ]
    return random.choice(dividir_personal_y_academico)

def consejo_confucion_sentimientos():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    confucion_sentimientos = [
        'vacio'
    ]
    return random.choice(confucion_sentimientos)

def consejo_expresar_sentiminetos():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    expresar_sentiminetos = [
        'vacio'
    ]
    return random.choice(expresar_sentiminetos)

def consejo_espacio_personal():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    espacio_personal = [
        'vacio'
    ]
    return random.choice(espacio_personal)

def consejo_remordimiento():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    remordimiento = [
        'vacio'
    ]
    return random.choice(remordimiento)

def consejo_envidia():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    envidia = [
        'vacio'
    ]
    return random.choice(envidia)

def consejo_desesperanza():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    desesperanza = [
        'vacio'
    ]
    return random.choice(desesperanza)

def consejo_fisico():
    '''
    Proporciona un consejo para cuando , forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    fisico = [
        'vacio'
    ]
    return random.choice(fisico)

def ayuda_psicologica():
    '''
    Proporciona un los medios para contactar una ayuda profesional

    :return  Medios para contactar una ayuda profesional
    :rtype str
    '''
    ayuda = [
	'Vacio',
    ] 
    return random.choice(ayuda)

def poner_musica():
    '''
    Función que devuelve una canción de YT aleatoria
    '''
    musica = [
        'https://www.youtube.com/watch?v=fmI_Ndrxy14',
        'https://www.youtube.com/watch?v=kYtGl1dX5qI',
        'https://www.youtube.com/watch?v=bESGLojNYSo'
    ]
    return random.choice(musica)

def despedida(user_input):
    '''
    Devuelve la despedida de glados

    :param str user_input: El texto escrito por el usuario
    :return La despedida de glados
    :rtype str
    '''
    des = user_input.split()
    despedida_usuario = ['salir', 'adios', 'bye', 'hasta luego', 'adiós']
    despedida_glados = ['Adiós', 'Bye!', '¡Hasta la vista, baby!']
    despedida_definitiva = ''
    for i in des:
        if i in des:
            despedida_definitiva = random.choice(despedida_glados)
    return despedida_definitiva
