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
                r'.*buen(a|o)s (dias|tardes|noches).*',
            ],
            'respuesta': [
                'Hola, ¿Como te sientes el dia de hoy? ',
                'Hola, ¿En que te puedo ayudar, como te sientes?',
                'Hola, soy tu IA de ayuda ¿Dime como te sientes?'
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
        #////////////////////////////////////////////////Chiste.
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
                r'.*hasta luego.*'
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