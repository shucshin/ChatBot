#----------------------------------------------------------------------
# Base de conocimiento
# La base de conocimiento representa una lista de todos los casos o intents.
#
# Cada caso o intent es un diccionario que incluye los siguientes keys (propiedades):
# - intent: Nombre para identificar el intent
# - regex: Lista de posibles expresiones regulares asociadas al intent, donde los parámetros se obtienen del texto parentizado en la expresión regular
# - respuesta: Lista de posibles respuestas al usuario, indicando los parámetros obtenidos con la notación %1, %2, %3, etc para cada parámetro
#----------------------------------------------------------------------
def conocimientoT():
    '''
    Define la base de conocimiento de glados

    :return El conicimiento a mostrar
    :rtype str 
    '''
    conocimiento = [
        #////////////////////////////////////////////////Bienvenida.
        {
            # r is raw string (no format)
            # if it contains this in my message, any elem of array 'respuesta' will execute
            'intent': 'bienvenida',
            'regex': [ 
                r'.*hola.*', 
                r'.*quiero hablar.*',
                r'.*buen(a|o)s (dias|tardes|noches).*'
            ],
            'respuesta': [
                'Hola soy Link++, tu bot de estabilidad emocional',
                'Hola soy Link++, tu bot de ayuda emocional',
                'Soy Link++, tu doctor psicologico'
            ]
        },
        #////////////////////////////////////////////////Problema.
        {
            # r is raw string (no format)
            # if it contains this in my message, any elem of array 'respuesta' will execute
            'intent': 'problema',
            'regex': [ 
                r'.*problema.*', 
                r'.*situaci(ón|on).*',
                r'.*conflicto.*',
                r'.*dificultad.*',
                r'.*complicaci(on|ón).*',
                r'.*obst(á|a)culo.*',
                r'.*inconveniente.*'
            ],
            'respuesta': [
                'Cuentame un poco más',
                '¿Como puedo ayudarte?',
                '¿Que te sucedio?'
            ]
        },
        #////////////////////////////////////////////////Triste.
        {
            'intent': 'triste',
            'regex': [
                r'.*triste.*',
                r'.*desanimad(o|a).*'
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Feliz.
        {
            'intent': 'feliz',
            'regex': [
                r'.*feliz.*',
                r'.*animad(o|a).*'
            ],
            'respuesta': [
                'Que bueno...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Enojado.
        {
            'intent': 'enojado',
            'regex': [
                r'.*enojad(o|a).*',
                r'.*furios(o|a).*'
            ],
            'respuesta': [
                'Oye calma...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Preocupado.
        {
            'intent': 'preocupado',
            'regex': [
                r'.*preocupad(o|a).*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Asustado.
        {
            'intent': 'asustado',
            'regex': [
                r'.*asustad(o|a).*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Ansioso.
        {
            'intent': 'ansioso',
            'regex': [
                r'.*ansios(o|a).*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Cansado.
        {
            'intent': 'cansado',
            'regex': [
                r'.*cansad(o|a).*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Orgulloso.
        {
            'intent': 'orgulloso',
            'regex': [
                r'.*orgullos(o|a).*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Chiste.
        {
            'intent': 'chiste',
            'regex': [
                r'.*chiste.*',
                r'.*broma.*'
            ],
            'respuesta': [
                'Bien',
                'Ahí te va'
            ]
        },
        #////////////////////////////////////////////////Estado.
        {
            'intent': 'estado',
            'regex': [
                r'^.*me siento (.*)$',
            ],
            'respuesta': [
                'Por que te sientes %1'
            ]
        }, 
        #////////////////////////////////////////////////Musica.
        {
            'intent': 'musica',
            'regex': [
                r'.*(pon|reproduce|toca|recomienda) (musica|una cancion).*',
            ],
            'respuesta': [
                'Ahí te va',
                'Esta es mi favorita:',
                'Aquí tienes'
            ]
        }, 
        #////////////////////////////////////////////////Otro.
        {
            'intent': 'repetir',
            'regex': [
                r'.*(cuentame|dime|saca) otr(o|a).*',
            ],
            'respuesta': [
                'Bueno...'
            ]
        }, 
        #////////////////////////////////////////////////Fin.
        {
            'intent': 'terminar',
            'regex': [
                r'.*salir.*',
                r'.*adios.*',
                r'.*bye.*',
                r'.*hasta luego.*',
                r'.*nos vemos.*'
            ],
            'respuesta': [
                ''
            ]
        },
        #////////////////////////////////////////////////Cualquier caso no contemplado.
        {
            'intent': 'desconocido',
            'regex': [
                r'.*'
            ],
            'respuesta': [
                'No te entendí ¿Puedes repetirlo por favor?',
                'Creo que no tengo información al respecto; lo siento mucho',
                'Creo que no entiendo el problema, podrias ser un poco más concreto'
            ]
        }
        #////////////////////////////////////////////////
    ]
    return conocimiento