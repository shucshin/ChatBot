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

def solucion():
    '''
    Te da un punto positivo

    :return Da un ona frase de esperanza
    :rtype str
    '''
    solucion = [
        'Tranquilo. Todo se resolvera.'
    ]
    solucion = random.choice(solucion)
    return solucion

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
    Proporciona un consejo para cuando no sepas por qué estudiaste cierta carrera, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    licenciatura = [
        'Tómate un tiempo para reflexionar sobre tus intereses y metas a largo plazo.',
        'Recuerda que la elección de una carrera no define tu valor como persona.',
        'Habla con personas que admires para obtener diferentes perspectivas y consejos.',
        'Explora actividades extracurriculares.'
    ]
    return random.choice(licenciatura)


def consejo_pensativo():
    '''
    Proporciona un consejo para cuando estés pensativo, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    pensativo = [
        'Es normal tomarse un tiempo para reflexionar sobre las cosas.',
        'Intenta escribir tus pensamientos en un diario.',
        'Recuerda que es importante equilibrar el pensamiento reflexivo con la acción.',
        'Date permiso para desconectarte de todo de vez en cuando.'
    ]
    return random.choice(pensativo)


def consejo_frustacion():
    '''
    Proporciona un consejo para cuando te sientas frustrado, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    frustacion = [
        'Respira profundo y toma un descanso breve para despejar tu mente.',
        'Trata de identificar la causa específica de tu frustración y busca soluciones prácticas para abordarla.',
        'Recuerda que es normal sentirse frustrado en ocasiones.',
        'Intenta cambiar tu perspectiva y enfocarte en lo que puedes controlar en lugar de lo que está fuera de tu alcance.'
    ]
    return random.choice(frustacion)


def consejo_carga_trabajo():
    '''
    Proporciona un consejo para cuando sientas una carga de trabajo abrumadora, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    carga_trabajo = [
        'Divide tu trabajo en tareas más pequeñas y priorízalas según su importancia y urgencia.',
        'No temas pedir ayuda si te sientes abrumado.',
        'Asegúrate de tomar descansos regulares.',
        'Comunica tus preocupaciones sobre la carga de trabajo con tu equipo.'
    ]
    return random.choice(carga_trabajo)


def consejo_examenes():
    '''
    Proporciona un consejo para cuando te enfrentes a exámenes, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    examenes = [
        'Prepárate con anticipación.',
        'No te quedes atrapado en la preocupación por los exámenes.',
        'Recuerda la importancia de dormir bien.',
        'No dudes en pedir ayuda si hay algo que no entiendes.'
    ]
    return random.choice(examenes)


def consejo_desconcentrado():
    '''
    Proporciona un consejo para cuando te sientas desconcentrado, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    desconcentrado = [
        'Haz una lista de tareas y priorízalas para ayudarte a enfocarte en lo más importante.',
        'Elimina las distracciones de tu entorno.',
        'Practica técnicas de respiración profunda o meditación.',
        'Divide tu tiempo en bloques de trabajo.'
    ]
    return random.choice(desconcentrado)


def consejo_desmotivado():
    '''
    Proporciona un consejo para cuando te sientas desmotivado, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    desmotivado = [
        'Busca inspiración en personas o historias que te motiven.',
        'Establece metas realistas y alcanzables.',
        'No te castigues por sentirte desmotivado en ocasiones.',
        'Rodéate de personas que te apoyen y te animen a seguir adelante.'
    ]
    return random.choice(desmotivado)


def consejo_gestion_tiempo():
    '''
    Proporciona un consejo para mejorar la gestión del tiempo, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    gestion_tiempo = [
        'Identifica tus tareas y asigna un tiempo específico para cada una de ellas.',
        'Utiliza técnicas como la técnica Pomodoro.',
        'Elimina las distracciones.',
        'Aprende a decir "no" a las tareas que no son prioritarias o que no contribuyen a tus objetivos principales.'
    ]
    return random.choice(gestion_tiempo)

def consejo_presion_familiar():
    '''
    Proporciona un consejo para lidiar con la presión familiar, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    presion_familiar = [
        'Comunica tus sentimientos y límites de manera clara pero respetuosa con tu familia.',
        'Busca apoyo en amigos u otros miembros de la familia que puedan entender y respaldar tus decisiones.',
        'Recuerda que es importante priorizar tu propia felicidad y bienestar.',
        'Busca momentos para cuidarte y recargar energías.'
    ]
    return random.choice(presion_familiar)


def consejo_autestima_bajo():
    '''
    Proporciona un consejo para mejorar la autoestima, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    autestima_bajo = [
        'Celebra tus logros, por pequeños que sean, y recuerda tus cualidades positivas.',
        'Haz una lista de afirmaciones positivas sobre ti mismo y repítelas diariamente.',
        'Practica el autocuidado y dedica tiempo a actividades que te hagan sentir bien contigo mismo.',
        'Busca apoyo en amigos, familiares o un profesional de la salud mental para trabajar en tu autoestima.'
    ]
    return random.choice(autestima_bajo)

def consejo_duda_futuro():
    '''
    Proporciona un consejo para lidiar con las dudas sobre el futuro, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    duda_futuro = [
        'Enfócate en el presente y establece metas a corto plazo para sentirte más seguro sobre el futuro.',
        'Habla con personas que han pasado por situaciones similares y busca orientación sobre tus opciones.',
        'Recuerda que es normal sentir incertidumbre sobre el futuro, pero confía en tus habilidades para enfrentarlo.',
        'Explora diferentes posibilidades y mantén una mentalidad abierta hacia nuevas oportunidades.'
    ]
    return random.choice(duda_futuro)

def consejo_presion_social():
    '''
    Proporciona un consejo para manejar la presión social, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    presion_social = [
        'Establece límites claros y no temas decir "no" cuando algo no se alinea con tus valores o metas.',
        'Busca grupos o comunidades donde te sientas aceptado y puedas ser tú mismo sin presiones externas.',
        'Recuerda que es importante priorizar tu bienestar mental y emocional por encima de las expectativas de los demás.',
        'Practica el autocuidado y dedica tiempo a actividades que te ayuden a mantener tu confianza y autoestima.'
    ]
    return random.choice(presion_social)

def consejo_insomnio():
    '''
    Proporciona un consejo para lidiar con el insomnio, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    insomnio = [
        'Establece una rutina de sueño regular y evita las siestas durante el día para mejorar la calidad del sueño.',
        'Crea un ambiente propicio para dormir, como una habitación oscura, tranquila y a una temperatura confortable.',
        'Limita la exposición a pantallas antes de dormir y practica técnicas de relajación como la meditación o la respiración profunda.',
        'Consulta con un profesional de la salud si el insomnio persiste, ya que puede ser un síntoma de un problema subyacente.'
    ]
    return random.choice(insomnio)

def consejo_duda_capacida_academica():
    '''
    Proporciona un consejo para superar las dudas sobre tus capacidades académicas, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    duda_capacida_academica = [
        'Recuerda que el aprendizaje es un proceso gradual y que es normal enfrentarse a desafíos en el camino.',
        'Identifica tus fortalezas y trabaja en ellas, pero también sé amable contigo mismo y reconoce tu progreso.',
        'Busca recursos adicionales como tutorías, grupos de estudio o material complementario para reforzar tu aprendizaje.',
        'Cultiva una mentalidad de crecimiento y enfócate en el esfuerzo y la perseverancia más que en los resultados inmediatos.'
    ]
    return random.choice(duda_capacida_academica)

def consejo_procrastinacion():
    '''
    Proporciona un consejo para superar la procrastinación, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    procrastinacion = [
        'Divide tus tareas en pasos más pequeños y establece plazos realistas para cada uno.',
        'Identifica las causas subyacentes de tu procrastinación y busca soluciones prácticas para abordarlas.',
        'Utiliza técnicas como la técnica Pomodoro para trabajar en intervalos de tiempo definidos y tomar descansos regulares.',
        'Crea un ambiente de trabajo libre de distracciones y establece recompensas para motivarte a completar tus tareas.'
    ]
    return random.choice(procrastinacion)

def consejo_duelo():
    '''
    Proporciona un consejo para lidiar con el duelo, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    duelo = [
        'Permítete sentir y expresar tus emociones de duelo, ya que es parte del proceso de sanación.',
        'Busca apoyo en amigos, familiares o grupos de apoyo que puedan entender y acompañarte durante este momento difícil.',
        'Encuentra formas de honrar y recordar a la persona que has perdido, como crear un altar o participar en actividades significativas en su memoria.',
        'Considera hablar con un terapeuta o consejero para recibir orientación adicional y aprender estrategias para afrontar el duelo.'
    ]
    return random.choice(duelo)

def consejo_metas_no_cumplidas():
    '''
    Proporciona un consejo para lidiar con metas no cumplidas, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    metas_no_cumplidas = [
        'Reevalúa tus metas y ajusta tus expectativas si es necesario, recordando que el camino hacia el éxito puede ser irregular.',
        'Identifica las lecciones aprendidas de tus experiencias y utilízalas para crecer y mejorar en el futuro.',
        'Busca el apoyo de amigos, familiares o mentores para obtener perspectivas externas y encontrar nuevas formas de abordar tus metas.',
        'Recuerda que el fracaso es parte del proceso de aprendizaje y que cada obstáculo te acerca más a tus objetivos si perseveras.'
    ]
    return random.choice(metas_no_cumplidas)

def consejo_perfeccionismo():
    '''
    Proporciona un consejo para superar el perfeccionismo, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    perfeccionismo = [
        'Fija estándares realistas y celebra el progreso, no solo los resultados finales.',
        'Aprende a aceptar la imperfección como parte del proceso de crecimiento y aprendizaje.',
        'Practica la autocompasión y recuerda que eres humano, con virtudes y limitaciones.',
        'Busca ayuda profesional si el perfeccionismo te está causando malestar emocional o afectando tu vida diaria.'
    ]
    return random.choice(perfeccionismo)

def consejo_fracaso():
    '''
    Proporciona un consejo para lidiar con el fracaso, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    fracaso = [
        'Usa el fracaso como una oportunidad para aprender y crecer, en lugar de verlo como un revés permanente.',
        'Recuerda que el fracaso es parte del camino hacia el éxito y no define tu valía como persona.',
        'Busca el apoyo de amigos, familiares o mentores para obtener perspectivas externas y orientación.',
        'Establece metas realistas y celebra tus esfuerzos y logros, incluso si no alcanzas tus objetivos inmediatos.'
    ]
    return random.choice(fracaso)

def consejo_economico():
    '''
    Proporciona un consejo para manejar problemas económicos, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    economico = [
        'Crea un presupuesto y haz un seguimiento de tus gastos para tener un mejor control de tus finanzas.',
        'Busca oportunidades para aumentar tus ingresos, como trabajos a tiempo parcial o actividades freelance.',
        'Prioriza tus necesidades básicas y elimina gastos innecesarios para aliviar la presión financiera.',
        'Explora opciones de ayuda financiera, como becas, préstamos estudiantiles o programas de asistencia.'
    ]
    return random.choice(economico)

def consejo_comunicacion():
    '''
    Proporciona un consejo para mejorar la comunicación interpersonal, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    comunicacion = [
        'Escucha activamente a los demás y muestra empatía hacia sus perspectivas y sentimientos.',
        'Expresa tus pensamientos y emociones de manera clara y asertiva, evitando la confrontación innecesaria.',
        'Busca resolver los conflictos de manera constructiva, buscando soluciones que beneficien a ambas partes.',
        'Practica la comunicación no verbal, como el contacto visual y el lenguaje corporal, para mejorar tu conexión con los demás.'
    ]
    return random.choice(comunicacion)

def consejo_inseguridad():
    '''
    Proporciona un consejo para superar la inseguridad personal, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    inseguridad = [
        'Desafía tus pensamientos negativos y reconoce tus logros y cualidades positivas.',
        'Fomenta una mentalidad de crecimiento y acepta los desafíos como oportunidades para aprender y crecer.',
        'Busca el apoyo de amigos, familiares o un profesional de la salud mental para trabajar en tu autoestima y confianza.',
        'Practica el autocuidado y dedica tiempo a actividades que te hagan sentir bien contigo mismo y fortalezcan tu sentido de valía.'
    ]
    return random.choice(inseguridad)

def consejo_tecnicas_estudio():
    '''
    Proporciona un consejo para mejorar las técnicas de estudio, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    tecnicas_estudio = [
        'Establece un horario de estudio regular y asegúrate de tener un espacio tranquilo y libre de distracciones.',
        'Utiliza técnicas de organización como la creación de resúmenes, mapas mentales o tarjetas de memoria para revisar la información.',
        'Practica la autoevaluación regular para identificar áreas de mejora y ajustar tus estrategias de estudio en consecuencia.',
        'Explora diferentes métodos de estudio y encuentra el que mejor se adapte a tu estilo de aprendizaje y tipo de material.'
    ]
    return random.choice(tecnicas_estudio)

def consejo_impostor():
    '''
    Proporciona un consejo para superar el síndrome del impostor, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    impostor = [
        'Reconoce tus logros y méritos, y recuerda que tus éxitos no son fruto de la suerte, sino de tu esfuerzo y habilidades.',
        'Habla con personas de confianza sobre tus sentimientos de impostor y busca su apoyo y perspectiva.',
        'Cambia tu diálogo interno negativo por afirmaciones positivas y recuerda que no estás solo en tus experiencias.',
        'Busca oportunidades para salir de tu zona de confort y enfrentar tus miedos, demostrándote a ti mismo que eres capaz.'
    ]
    return random.choice(impostor)

def consejo_estres():
    '''
    Proporciona un consejo para manejar el estrés, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    estres = [
        'Practica técnicas de relajación como la meditación, la respiración profunda o el yoga para reducir los niveles de estrés.',
        'Establece límites claros y aprende a decir "no" cuando te sientas abrumado por tus responsabilidades.',
        'Prioriza tus tareas y haz una lista de actividades para enfocarte en lo que es más importante en el momento.',
        'Busca el apoyo de amigos, familiares o profesionales de la salud mental si sientes que el estrés está afectando tu bienestar.'
    ]
    return random.choice(estres)

def consejo_indesicion():
    '''
    Proporciona un consejo para superar la indecisión, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    indesicion = [
        'Haz una lista de opciones y evalúa los pros y los contras de cada una.',
        'Busca consejos de personas de confianza o expertos en el tema para ayudarte a tomar una decisión informada.',
        'Date un plazo límite para tomar una decisión y comprométete a actuar una vez que hayas evaluado todas las opciones.',
        'Confía en tu instinto y en tus habilidades para tomar decisiones, y recuerda que no existe una opción perfecta.'
    ]
    return random.choice(indesicion)

def consejo_miedo_participar():
    '''
    Proporciona un consejo para superar el miedo a participar, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    miedo_participar = [
        'Empieza con pequeños pasos y desafíate gradualmente a ti mismo a participar en situaciones sociales.',
        'Practica técnicas de relajación como la respiración profunda o la visualización para controlar la ansiedad antes de participar.',
        'Visualiza situaciones sociales exitosas y visualízate a ti mismo participando de manera activa y segura.',
        'Recuerda que es normal sentir miedo al participar, pero que cada experiencia te ayudará a crecer y ganar confianza.'
    ]
    return random.choice(miedo_participar)

def consejo_dividir_personal_y_academico():
    '''
    Proporciona un consejo para equilibrar la vida personal y académica, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    dividir_personal_y_academico = [
        'Establece límites claros entre tu vida personal y académica, asignando tiempo específico para cada una.',
        'Prioriza tus actividades según su importancia y urgencia, y aprende a decir "no" cuando sea necesario para proteger tu tiempo personal.',
        'Busca actividades extracurriculares o pasatiempos que te ayuden a relajarte y desconectar del estrés académico.',
        'Mantén una comunicación abierta con amigos, familiares y profesores sobre tus compromisos y necesidades para recibir apoyo.'
    ]
    return random.choice(dividir_personal_y_academico)

def consejo_confucion_sentimientos():
    '''
    Proporciona un consejo para lidiar con la confusión de sentimientos, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    confucion_sentimientos = [
        'Permítete sentir tus emociones sin juzgarlas y reconoce que es normal experimentar una amplia gama de sentimientos.',
        'Busca identificar y nombrar tus emociones para entender mejor lo que estás sintiendo y por qué.',
        'Practica la autoaceptación y la compasión hacia ti mismo, recordando que tus sentimientos son válidos y dignos de ser reconocidos.',
        'Busca la ayuda de amigos, familiares o un profesional de la salud mental si sientes que la confusión de sentimientos está afectando tu bienestar.'
    ]
    return random.choice(confucion_sentimientos)

def consejo_expresar_sentiminetos():
    '''
    Proporciona un consejo para expresar tus sentimientos, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    expresar_sentiminetos = [
        'Encuentra un momento y un lugar adecuados para hablar sobre tus sentimientos de manera honesta y respetuosa.',
        'Utiliza "yo" en lugar de "tú" al expresar tus emociones para evitar que la otra persona se sienta atacada o culpable.',
        'Sé receptivo a las reacciones de la otra persona y mantén una comunicación abierta para resolver cualquier malentendido o conflicto.',
        'Recuerda que expresar tus sentimientos es un acto de valentía y autenticidad que fortalece tus relaciones y tu bienestar emocional.'
    ]
    return random.choice(expresar_sentiminetos)

def consejo_espacio_personal():
    '''
    Proporciona un consejo para proteger tu espacio personal, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    espacio_personal = [
        'Establece límites claros con los demás sobre tu tiempo, tu energía y tus necesidades personales.',
        'Aprende a decir "no" cuando sientas que tu espacio personal está siendo invadido o comprometido de alguna manera.',
        'Busca momentos de soledad y tranquilidad para recargar tus baterías y cuidar tu bienestar emocional.',
        'Comunica tus necesidades y expectativas de manera clara y respetuosa, fomentando relaciones saludables y equilibradas.'
    ]
    return random.choice(espacio_personal)


def consejo_remordimiento():
    '''
    Proporciona un consejo para cuando sientes remordimiento, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    remordimiento = [
        'Aprende de tus errores y busca maneras de remediarlos.',
        'Perdónate a ti mismo y enfócate en el presente para crecer.',
        'Habla sobre tus sentimientos con alguien de confianza para aliviar la carga.'
    ]
    return random.choice(remordimiento)

def consejo_envidia():
    '''
    Proporciona un consejo para cuando sientes envidia, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    envidia = [
        'Enfócate en tus propias metas y logros en lugar de compararte con los demás.',
        'Practica la gratitud por lo que tienes en lugar de envidiar lo que otros tienen.',
        'Reconoce tus sentimientos de envidia y busca maneras saludables de canalizarlos.'
    ]
    return random.choice(envidia)

def consejo_desesperanza():
    '''
    Proporciona un consejo para cuando te sientes desesperanzado, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    desesperanza = [
        'Busca apoyo de amigos, familiares o profesionales si te sientes abrumado.',
        'Encuentra actividades que te brinden alegría y esperanza.',
        'Recuerda que los tiempos difíciles son temporales y que puedes superarlos.'
    ]
    return random.choice(desesperanza)

def consejo_fisico():
    '''
    Proporciona un consejo para cuando te sientes físicamente agotado, de forma aleatoria

    :return El consejo que se va a dar
    :rtype str
    '''
    fisico = [
        'Prioriza el autocuidado, incluyendo descanso adecuado, alimentación saludable y ejercicio regular.',
        'Tómate descansos cortos durante el día para recargar energías y reducir el estrés físico.',
        'Busca actividades que te relajen, como estiramientos, meditación o respiración profunda.'
    ]
    return random.choice(fisico)

def ayuda_psicologica():
    '''
    Proporciona un los medios para contactar una ayuda profesional

    :return  Medios para contactar una ayuda profesional
    :rtype str
    '''
    ayuda = [
	'Espora: Numero de contacto: 55 5658 1111 \n correo: espora_psicologica@unam.mx \n Web: http://www.espora.unam.mx/',
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
    despedida_usuario = ['salir', 'adios', 'bye', 'hasta luego', 'adiós', 'nos vemos']
    despedida_glados = ['Adiós', 'Bye!', '¡Hasta la vista, baby!', 'Te veo luego!']
    despedida_definitiva = ''
    for i in des:
        if i in des:
            despedida_definitiva = random.choice(despedida_glados)
    return despedida_definitiva
