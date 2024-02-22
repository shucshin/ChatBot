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
        'En hora buena! Sigue esforzándote!',
		'Lo estás haciendo bien! Sigue así!',
		'Vas por buen camino! No te rindas!',
		'Estoy feliz por ti!!'
    ]
    return random.choice(pelea)

def consejo_discusion():
    '''
    Proporciona un consejo para cuando discutes con alguien de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    discusion = [
        'En hora buena! Sigue esforzándote!',
		'Lo estás haciendo bien! Sigue así!',
		'Vas por buen camino! No te rindas!',
		'Estoy feliz por ti!!'
    ]
    return random.choice(discusion)

def consejo_termine():
    '''
    Proporciona un consejo para cuando terminas con alguien o ya no quieres saber de la persona, forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    termine = [
        'En hora buena! Sigue esforzándote!',
		'Lo estás haciendo bien! Sigue así!',
		'Vas por buen camino! No te rindas!',
		'Estoy feliz por ti!!'
    ]
    return random.choice(termine)

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
