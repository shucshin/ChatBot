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
        #////////////////////////////////////////////////Pelea con algun conocido.
        {
            'intent': 'pelea',
            'regex': [
                r'.*me pele(é|e).*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Discusion con algun conocido.
        {
            'intent': 'discusion',
            'regex': [
                r'.*discut(i|í).*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Terminas alguna relacion con alguine conocido.
        {
            'intent': 'termine',
            'regex': [
                r'.*termine con mi (novio|novia|amistad|relaci(ó|o)n).*',
                r'.*termine una (amistad|relaci(o|ó)n).*'
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Rumor sobre ti 
        {
            'intent': 'rumor',
            'regex': [
                r'.*rumor sobre mi.*',
                r'.*rumor mio.*'
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Persona que entra en crisis existencial
        {
            'intent': 'crisis',
            'regex': [
                r'.*no se quien soy.*',
                r'.*no se que estoy haciendo con mi vida.*'
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Persona que sabe que esta en un estado de depresión
        {
            'intent': 'depresion',
            'regex': [
                r'.*siento que estoy deprimido.*',
                r'.*estoy en depresion.*',
                r'.*siento deprimido.*'
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Sentiminetos de soledad
        {
            'intent': 'soledad',
            'regex': [
                r'.*siento solo.*',
                r'.*estoy solo.*',
                r'.*siento completamente solo.*',
                r'.*no tengo a nadie.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Sentimiento de confusion en estudios
        {
            'intent': 'licenciatura',
            'regex': [
                r'.*no se si (elegi|seleccione|estudie) la (carrera|licenciatura) (correcta|adecuada).*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },

        #////////////////////////////////////////////////Sentimiento poderoso
        {
            'intent': 'poderoso',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Sentimiento pensativo
        {
            'intent': 'pensativo',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Sentimiento frustacion
        {
            'intent': 'frustacion',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Mucha tarea y no saber que hacer
        {
            'intent': 'carga trabajo',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Fechas de examenes
        {
            'intent': 'examenes',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Prblema proferoes o ayudantes
        {
            'intent': 'problema profesor/ayudante',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Desconcentrado
        {
            'intent': 'desconcentrado',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Desmotivado
        {
            'intent': 'desmotivado',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Problemas de gestion
        {
            'intent': 'gestion tiempo',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Presion Familiar
        {
            'intent': 'presion familiar',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////autoestima bajo
        {
            'intent': 'autestima bajo',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Dudas sobre el futuro
        {
            'intent': 'duda futuro',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Pasado que pesa
        {
            'intent': 'pasado complicado',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Presion social
        {
            'intent': 'presion social',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Insomnio
        {
            'intent': 'insomnio',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Capacidad academica
        {
            'intent': 'duda capacida academica',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Procrastinacion
        {
            'intent': 'procrastinacion',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Perdida Familiar
        {
            'intent': 'duelo',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////No logro metas
        {
            'intent': 'metas no cumplidas',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Trastorno perfeccionista
        {
            'intent': 'perfeccionismo',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Miedo fracaso
        {
            'intent': 'fracaso',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// Preocupacion economica
        {
            'intent': 'economico',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// Problemas de comunicación
        {
            'intent': 'comunicacion',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// Inseguridad
        {
            'intent': 'inseguridad',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// Tecnicas de estudio
        {
            'intent': 'tecnicas estudio',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// Sindrome del impostor
        {
            'intent': 'impostor',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// Estres
        {
            'intent': 'estres',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// Problemas para toma de desiciones
        {
            'intent': 'indesicion',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #////////////////////////////////////////////////Miedo a participar en clase
        {
            'intent': 'miedo participar',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// Confusion entre lo personal y lo academico
        {
            'intent': 'dividir personal y academico',
            'regex': [
                r'.*.*',
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// Incertidumbre de sentimientos a otra persona
        {
            'intent': 'confucion sentimientos',
            'regex': [
                r'.*no se como sentirme.*',
                r'.*siento algo por.*',
                r'.*me confunde como sentirme.*',
                r'.*no se que es lo quiere.*',
                r'.*sentimientos encontrados.*'
            ],
            'respuesta': [
                'Mira...',
                'Lo que te voy a decir es que...'
            ]
        },
        #//////////////////////////////////////////////// No lograr expresar sentimientos adecuadamente
        {
            'intent': 'expresar sentiminetos',
            'regex': [
                r'.*no se como (expresar|hablar sobre) mis sentimientos.*',
                r'.*siento mal al no poder expresar mis sentimientos.*',
                r'.*es complicado (expresar|hablar de) como me siento.*'
            ],
            'respuesta': [
                'debes intentar'
            ]
        },
        #//////////////////////////////////////////////// Espacio personal
        {
            'intent': 'espacio personal',
            'regex': [
                r'.*abruma.*',
                r'.*(ella|el) hace que me sienta (incomod(a|o)|abrumad(a|o)).*'
            ],
            'respuesta': [
                'es muy importante'
            ]
        },
        #//////////////////////////////////////////////// remordimiento
        {
            'intent': 'remordimiento',
            'regex': [
                r'.*remuerde.*',
            ],
            'respuesta': [
                'debes concentrarte cuando'
            ]
        },
        #//////////////////////////////////////////////// envidia
        {
            'intent': 'envidia',
            'regex': [
                r'.*envidia.*',
                r'.*(me molesta|odio|fastidio) que sea mejor.*'
            ],
            'respuesta': [
                'no tienes que'
            ]
        },
        #//////////////////////////////////////////////// desesperanza
        {
            'intent': 'desesperanza',
            'regex': [
                r'.*salir mal.*',
                r'.*no lo lograre.*',
                r'.*(no tengo|me siento sin) esperanza.*'
            ],
            'respuesta': [
                'yo digo que'
            ]
        },
        #////////////////////////////////////////////////Salud fisica 
        {
            'intent': 'fisico',
            'regex': [
                r'.*fisicamente (cansado|agotado|fatigado).*',
                r'.*tengo (cansancio|agotamiento|fatiga).*'
            ],
            'respuesta': [
                'es importante que'
            ]
        },
        #////////////////////////////////////////////////Para pedir ayuda psicologica profesional
        {
            'intent': 'ayuda',
            'regex': [
                r'.*ayuda (profesional|psicol(o|ó)gica).*',
            ],
            'respuesta': [
                'Estos son los numeros y correos para ayuda psicologica: ',
            ]
        },
        #////////////////////////////////////////////////solución
        {
            'intent': 'solucion',
            'regex': [
                r'.*crees que se solucione.*',
                r'.*crees que se pueda solucionar.*',
                r'.*ya no se (puede| va a) solucionar.*',
                r'.*siento que no se (puede|va a) areglar.*',
                r'.*no creo que funcione.*'
            ],
            'respuesta': [
                'pues mira'
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
                r'.*(cuentame|dime|saca|dame) otr(o|a).*',
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