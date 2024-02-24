#------------------------------------------------#
#  ChatBot.py                                    #
#------------------------------------------------#

import string, re, random, sys
from conocimiento import conocimientoT
from ResponseFunctions import dar_bienvenida, ask_problem, contar_chiste, despedida, poner_musica, consejo_triste, consejo_feliz, consejo_enojado, consejo_preocupado, consejo_asustado, consejo_ansioso, consejo_cansado, consejo_orgulloso, consejo_pelea, consejo_discusion, consejo_termine, consejo_rumor, consejo_crisis, consejo_depresion, consejo_soledad, consejo_licenciatura, consejo_poderoso, consejo_pensativo, consejo_frustacion, consejo_carga_trabajo, consejo_examenes, consejo_problema_profesor_ayudante, consejo_desconcentrado, consejo_desmotivado, consejo_gestion_tiempo, consejo_presion_familiar, consejo_autestima_bajo, consejo_duda_futuro, consejo_pasado_complicado, consejo_presion_social, consejo_insomnio, consejo_duda_capacida_academica, consejo_procrastinacion, consejo_duelo, consejo_metas_no_cumplidas, consejo_perfeccionismo, consejo_fracaso, consejo_economico, consejo_comunicacion, consejo_inseguridad, consejo_tecnicas_estudio, consejo_impostor, consejo_estres, consejo_indesicion, consejo_miedo_participar, consejo_dividir_personal_y_academico, consejo_confucion_sentimientos, consejo_expresar_sentiminetos, consejo_espacio_personal, consejo_remordimiento, consejo_envidia, consejo_desesperanza, consejo_fisico, ayuda_psicologica

class ChatBot:
    """
    Clase ChatBot para simular una conversación 
    sobre videojuegos
    """
    contexto = "DEFAULT"
    entrada = ""

    def __init__(self):
        """
        ChatBot consta de una base de conocimiento
        representada como una lista de casos o intents.
        """ 
        self.conocimiento = [] 
        for caso in conocimiento:
            caso['regex'] = list(map(lambda x:re.compile(x, re.IGNORECASE), caso['regex']))
            self.conocimiento.append(caso)

    def responder(self, user_input):
        '''
        Flujo básico para identificar coincidencias de intents para responder al usuario.
        Con el texto del usuario como parámetro, los paso a realizarse son:
        1. Encontrar el caso de la base de conocimiento usando expresiones regulares
        2. Si es necesario, realizar acciones asociadas al intent (por ejemplo: consultar información adicional)
        3. Seleccionar una respuesta de la lista de respuestas según el caso del intent
        4. Si es necesario, identificar los parámetros o entidades del texto para dar formato a la respuesta seleccionada
        5. Devolver la respuesta

        :param str user_input: El texto escrito por el usuario
        :return Un texto de respuesta al usuario
        :rtype: str
        '''
        caso = self.encontrar_intent(user_input)
        self.identifica_contexto(caso) 
        informacion_adicional = self.acciones(caso, user_input)
        respuesta = self.convertir_respuesta(random.choice(caso['respuesta']), caso, user_input)
        respuesta_final = (respuesta + '\n' + informacion_adicional).strip() 
        return respuesta_final

    def encontrar_intent(self, user_input):
        '''
        Encuentra el caso o intent asociado en la base de conocimiento

        :param str user_input: El texto escrito por el usuario
        :return El diccionario que representa el caso o intent deseado
        :rtype: str
        '''
        for caso in self.conocimiento:
            for regularexp in caso['regex']:
                match = regularexp.match(user_input)
                if match:
                    self.regexp_selected = regularexp 
                    return caso
        return {}

    def identifica_contexto(self, caso):
        '''
        Asegura que el contexto sea el adecuado para que
        ChatBot responde de manera coherente

        :param dict caso: El intent del cual se solicita información 
        '''
        intent = caso['intent']
        if intent == 'bienvenida':
            self.contexto = "BIENVENIDA"
        elif intent == 'problema':
            self.contexto = 'PROBLEMA'
        elif intent == 'triste':
            self.contexto = "TRISTE"
        elif intent == 'feliz':
            self.contexto = "FELIZ"
        elif intent == 'enojado':
            self.contexto = "ENOJADO"
        elif intent == 'preocupado':
            self.contexto = "PREOCUPADO"
        elif intent == 'asustado':
            self.contexto = "ASUSTADO"
        elif intent == 'ansioso':
            self.contexto = "ANSIOSO"
        elif intent == 'cansado':
            self.contexto = "CANSADO"
        elif intent == 'orgulloso':
            self.contexto = "ORGULLOSO"
        elif intent == 'pelea':
            self.contexto = 'PELEA'
        elif intent == 'discusion':
            self.contexto = 'DISCUSION'
        elif intent == 'termine':
            self.contexto = 'TERMINE'
        elif intent == 'rumor':
            self.contexto = 'RUMOR'
        elif intent == 'crisis':
            self.contexto = 'CRISIS'
        elif intent == 'depresion':
            self.contexto = 'DEPRESION'
        elif intent == 'soledad':
            self.contexto = 'SOLEDAD'
        elif intent == 'licenciatura':
            self.contexto = 'LICENCIATURA'
        elif intent == 'poderoso':
            self.contexto = 'PODEROSO'
        elif intent == 'pensativo':
            self.contexto = 'PENSATIVO'
        elif intent == 'frustacion':
            self.contexto = 'FRUSTACION'
        elif intent == 'carga trabajo':
            self.contexto = 'CARGA TRABAJO'
        elif intent == 'examenes':
            self.contexto = 'EXAMENES'
        elif intent == 'problema profesor/ayudante':
            self.contexto = 'PROBLEMA PROFESOR/AYUDANTE'
        elif intent == 'desconcentrado':
            self.contexto = 'DESCONCENTRADO'
        elif intent == 'desmotivado':
            self.contexto = 'DESMOTIVADO'
        elif intent == 'gestion tiempo':
            self.contexto = 'GESTION TIEMPO'
        elif intent == 'presion familiar':
            self.contexto = 'PRESION FAMILIAR'
        elif intent == 'autestima bajo':
            self.contexto = 'AUTESTIMA BAJO'
        elif intent == 'duda futuro':
            self.contexto = 'DUDA FUTURO'
        elif intent == 'pasado complicado':
            self.contexto = 'PASADO COMPLICADO'
        elif intent == 'presion social':
            self.contexto = 'PRESION SOCIAL'
        elif intent == 'insomnio':
            self.contexto = 'INSOMNIO'
        elif intent == 'duda capacida academica':
            self.contexto = 'DUDA CAPACIDAD ACADEMICA'
        elif intent == 'procrastinacion':
            self.contexto = 'PROCRASTINACION'
        elif intent == 'duelo':
            self.contexto = 'DUELO'
        elif intent == 'metas no cumplidas':
            self.contexto = 'METAS NO CUMPLIDAS'
        elif intent == 'perfeccionismo':
            self.contexto = 'PERFECCIONISMO'
        elif intent == 'fracaso':
            self.contexto = 'FRACASO'
        elif intent == 'comunicacion':
            self.contexto = 'COMUNICACION'
        elif intent == 'inseguridad':
            self.contexto = 'INSEGURIDAD'
        elif intent == 'tecnicas estudio':
            self.contexto = 'TECNICAS ESTUDIO'
        elif intent == 'impostor':
            self.contexto = 'IMPOSTOR'
        elif intent == 'estres':
            self.contexto = 'ESTRES'
        elif intent == 'indesicion':
            self.contexto = 'INDESICION'
        elif intent == 'miedo participar':
            self.contexto = 'MIEDO PARTICIPAR'
        elif intent == 'dividir personal y academico':
            self.contexto = 'DIVIDIR PERSONAL Y ACADEMICO'
        elif intent == 'confucion sentimientos':
            self.contexto = 'CONFUCION SENTIMIENTOS'
        elif intent == 'expresar sentiminetos':
            self.contexto = 'EXPRESAR SENTIMIENTOS'
        elif intent == 'espacio personal':
            self.contexto = 'ESPACIO PERSONAL'
        elif intent == 'remordimiento':
            self.contexto = 'REMORDIMEINTO'
        elif intent == 'envidia':
            self.contexto = 'ENVIDIA'
        elif intent == 'desesperanza':
            self.contexto = 'DESESPERANZA'
        elif intent == 'fisico':
            self.contexto = 'FISICO'
        elif intent == 'ayuda':
            self.contexto = 'AYUDA'
        elif intent == 'chiste':
            self.contexto = "CHISTE"
        elif intent == 'musica':
            self.contexto = "MUSICA"
        elif intent == 'desconocido':
            self.contexto = "DEFAULT"  

    def convertir_respuesta(self, respuesta, caso, user_input):
        '''
        Cambia los textos del tipo %1, %2, %3, etc., por su correspondiente propiedad
        identificada en los grupos parentizados de la expresión regular asociada.

        :param str respuesta: Una respuesta que desea convertirse
        :param dict caso: El caso o intent asociado a la respuesta
        :param str user_input: El texto escrito por el usuario
        :return La respuesta con el cambio de parámetros
        :rtype: str
        '''
        respuesta_cambiada = respuesta
        intent = caso['intent']
        match = self.regexp_selected.match(user_input)
        if intent == 'estado':
            respuesta_cambiada = respuesta_cambiada.replace('%1', match.group(1))
        return respuesta_cambiada

    def acciones(self, caso, user_input):
        '''
        Obtiene información adicional necesaria para dar una respuesta coherente al usuario.
        El tipo de acciones puede ser una consulta de información, revisar base de datos, generar
        un código, etc. y el resultado final es expresado como una cadena de texto

        :param dict caso: El caso o intent asociado a la respuesta
        :return Texto que representa información adicional para complementar la respuesta al usuario
        :rtype: str
        '''
        intent = caso['intent']
        if intent == 'bienvenida':
            return dar_bienvenida()
        elif intent == 'problema':
            return ask_problem()
        elif intent == 'chiste':
            return contar_chiste()
        elif intent == 'triste':
            return consejo_triste()
        elif intent == 'feliz':
            return consejo_feliz()
        elif intent == 'enojado':
            return consejo_enojado()
        elif intent == 'preocupado':
            return consejo_preocupado()
        elif intent == 'asustado':
            return consejo_asustado()
        elif intent == 'ansioso':
            return consejo_ansioso()
        elif intent == 'cansado':
            return consejo_cansado()
        elif intent == 'orgulloso':
            return consejo_orgulloso()
        elif intent == 'pelea':
            return consejo_pelea()
        elif intent == 'discusion':
            return consejo_discusion()
        elif intent == 'termine':
            return consejo_termine()
        elif intent == 'rumor':
            return consejo_rumor()
        elif intent == 'crisis':
            return consejo_crisis()
        elif intent == 'depresion':
            return consejo_depresion()
        elif intent == 'soledad':
            return consejo_soledad()
        elif intent == 'licenciatura':
            return consejo_licenciatura()
        elif intent == 'poderoso':
            return consejo_poderoso()
        elif intent == 'pensativo':
            return consejo_pensativo() 
        elif intent == 'frustacion':
            return consejo_frustacion() 
        elif intent == 'carga trabajo':
            return consejo_carga_trabajo() 
        elif intent == 'examenes':
            return consejo_examenes() 
        elif intent == 'problema profesor/ayudante':
            return consejo_problema_profesor_ayudante() 
        elif intent == 'desconcentrado':
            return consejo_desconcentrado() 
        elif intent == 'desmotivado':
            return consejo_desmotivado() 
        elif intent == 'gestion tiempo':
            return consejo_gestion_tiempo() 
        elif intent == 'presion familiar':
            return consejo_presion_familiar() 
        elif intent == 'autestima bajo':
            return consejo_autestima_bajo() 
        elif intent == 'duda futuro':
            return consejo_duda_futuro() 
        elif intent == 'pasado complicado':
            return consejo_pasado_complicado() 
        elif intent == 'presion social':
            return consejo_presion_social() 
        elif intent == 'insomnio':
            return consejo_insomnio() 
        elif intent == 'duda capacida academica':
            return consejo_duda_capacida_academica()  
        elif intent == 'procrastinacion':
            return consejo_procrastinacion() 
        elif intent == 'duelo':
            return consejo_duelo() 
        elif intent == 'metas no cumplidas':
            return consejo_metas_no_cumplidas()  
        elif intent == 'perfeccionismo':
            return consejo_perfeccionismo() 
        elif intent == 'fracaso':
            return consejo_fracaso() 
        elif intent == 'comunicacion':
            return consejo_comunicacion() 
        elif intent == 'inseguridad':
            return consejo_inseguridad() 
        elif intent == 'tecnicas estudio':
            return consejo_tecnicas_estudio() 
        elif intent == 'impostor':
            return consejo_impostor() 
        elif intent == 'estres':
            return consejo_estres() 
        elif intent == 'indesicion':
            return consejo_indesicion() 
        elif intent == 'miedo participar':
            return consejo_miedo_participar() 
        elif intent == 'dividir personal y academico':
            return consejo_dividir_personal_y_academico() 
        elif intent == 'confucion sentimientos':
            return consejo_confucion_sentimientos() 
        elif intent == 'expresar sentiminetos':
            return consejo_expresar_sentiminetos() 
        elif intent == 'espacio personal':
            return consejo_espacio_personal() 
        elif intent == 'remordimiento':
            return consejo_remordimiento() 
        elif intent == 'envidia':
            return consejo_envidia() 
        elif intent == 'desesperanza':
            return consejo_desesperanza() 
        elif intent == 'fisico':
            return consejo_fisico() 
        elif intent == 'ayuda':
            return ayuda_psicologica()
        elif intent == 'musica':
            return poner_musica()
        elif intent == 'repetir':
            return self.da_respuesta_apropiada(user_input)
        elif intent == 'terminar':
            print(despedida(user_input))
            sys.exit(0)
        return ''


    def da_respuesta_apropiada(self, user_input):
        '''
        Devuelve la respuesta según el contexto en el que se encuentre

        :param str user_input: El texto escrito por el usuario
        :return Texto que representa la respuesta
        :rtype str
        '''
        if self.contexto == 'CHISTE':
            return 'Aquí va otro: ' + contar_chiste()
        elif self.contexto == 'TRISTE':
            return 'Aquí va otro: ' + consejo_triste()
        elif self.contexto == 'FELIZ':
            return 'Aquí va otro: ' + consejo_feliz()
        elif self.contexto == 'ENOJADO':
            return 'Aquí va otro: ' + consejo_enojado()
        elif self.contexto == 'PREOCUPADO':
            return 'Aquí va otro: ' + consejo_preocupado()
        elif self.contexto == 'ASUSTADO':
            return 'Aquí va otro: ' + consejo_asustado()
        elif self.contexto == 'ANSIOSO':
            return 'Aquí va otro: ' + consejo_ansioso()
        elif self.contexto == 'CANSADO':
            return 'Aquí va otro: ' + consejo_cansado()
        elif self.contexto == 'ORGULLOSO':
            return 'Aquí va otro: ' + consejo_orgulloso()
        elif self.contexto == 'PELEA':
            return 'Aquí va otro: ' + consejo_pelea()
        elif self.contexto == 'DISCUCION':
            return 'Aquí va otro: ' + consejo_discusion()
        elif self.contexto == 'TERMINE':
            return 'Aquí va otro: ' + consejo_termine()
        elif self.contexto == 'RUMOR':
            return 'Aquí va otro: ' + consejo_rumor()
        elif self.contexto == 'CRISIS':
            return 'Aquí va otro: ' + consejo_crisis()
        elif self.contexto == 'DEPRESION':
            return 'Aquí va otro: ' + consejo_depresion()
        elif self.contexto == 'SOLEDAD':
            return 'Aquí va otro: ' + consejo_soledad()
        elif self.contexto == 'LICENCIATURA':
            return 'Aquí va otro: ' + consejo_licenciatura()
        elif self.contexto == 'PODEROSO':
            return 'Aquí va otro: ' + consejo_poderoso()
        elif self.contexto == 'PENSATIVO':
            return 'Aquí va otro: ' + consejo_pensativo()
        elif self.contexto == 'FRUSTACION':
            return 'Aquí va otro: ' + consejo_frustacion()
        elif self.contexto == 'CARGA TRABAJO':
            return 'Aquí va otro: ' + consejo_carga_trabajo()
        elif self.contexto == 'EXAMENES':
            return 'Aquí va otro: ' + consejo_examenes()
        elif self.contexto == 'PROBLEMA PROFESOR/AYUDANTE':
            return 'Aquí va otro: ' + consejo_problema_profesor_ayudante()
        elif self.contexto == 'DESCONCENTRADO':
            return 'Aquí va otro: ' + consejo_desconcentrado()
        elif self.contexto == 'DESMOTIVADO':
            return 'Aquí va otro: ' + consejo_desmotivado()
        elif self.contexto == 'GESTION TIEMPO':
            return 'Aquí va otro: ' + consejo_gestion_tiempo()
        elif self.contexto == 'PRESION FAMILIAR':
            return 'Aquí va otro: ' + consejo_presion_familiar()
        elif self.contexto == 'AUTESTIMA BAJO':
            return 'Aquí va otro: ' + consejo_autestima_bajo()
        elif self.contexto == 'DUDA FUTURO':
            return 'Aquí va otro: ' + consejo_duda_futuro()
        elif self.contexto == 'PASADO COMPLICADO':
            return 'Aquí va otro: ' + consejo_pasado_complicado()
        elif self.contexto == 'PRESION SOCIAL':
            return 'Aquí va otro: ' + consejo_presion_social()
        elif self.contexto == 'INSOMNIO':
            return 'Aquí va otro: ' + consejo_insomnio()
        elif self.contexto == 'DUDA CAPACIDAD ACADEMICA':
            return 'Aquí va otro: ' + consejo_duda_capacida_academica()
        elif self.contexto == 'PROCRASTINACION':
            return 'Aquí va otro: ' + consejo_procrastinacion()
        elif self.contexto == 'DUELO':
            return 'Aquí va otro: ' + consejo_duelo()
        elif self.contexto == 'METAS NO CUMPLIDAS':
            return 'Aquí va otro: ' + consejo_metas_no_cumplidas()
        elif self.contexto == 'PERFECCIONISMO':
            return 'Aquí va otro: ' + consejo_perfeccionismo()
        elif self.contexto == 'FRACASO':
            return 'Aquí va otro: ' + consejo_fracaso()
        elif self.contexto == 'COMUNICACION':
            return 'Aquí va otro: ' + consejo_comunicacion()
        elif self.contexto == 'INSEGURIDAD':
            return 'Aquí va otro: ' + consejo_inseguridad()
        elif self.contexto == 'TECNICAS ESTUDIO':
            return 'Aquí va otro: ' + consejo_tecnicas_estudio()
        elif self.contexto == 'IMPOSTOR':
            return 'Aquí va otro: ' + consejo_impostor()
        elif self.contexto == 'ESTRES':
            return 'Aquí va otro: ' + consejo_estres()
        elif self.contexto == 'INDESICION':
            return 'Aquí va otro: ' + consejo_indesicion()
        elif self.contexto == 'MIEDO PARTICIPAR':
            return 'Aquí va otro: ' + consejo_miedo_participar()
        elif self.contexto == 'DIVIDIR PERSONAL Y ACADEMICO':
            return 'Aquí va otro: ' + consejo_dividir_personal_y_academico()
        elif self.contexto == 'CONFUCION SENTIMIENTOS':
            return 'Aquí va otro: ' + consejo_confucion_sentimientos()
        elif self.contexto == 'EXPRESAR SENTIMIENTOS':
            return 'Aquí va otro: ' + consejo_expresar_sentiminetos()
        elif self.contexto == 'ESPACIO PERSONAL':
            return 'Aquí va otro: ' + consejo_espacio_personal()
        elif self.contexto == 'REMORDIMEINTO':
            return 'Aquí va otro: ' + consejo_remordimiento()
        elif self.contexto == 'ENVIDIA':
            return 'Aquí va otro: ' + consejo_envidia()
        elif self.contexto == 'DESESPERANZA':
            return 'Aquí va otro: ' + consejo_desesperanza()
        elif self.contexto == 'FISICO':
            return 'Aquí va otro: ' + consejo_fisico()
        elif self.contexto == 'MUSICA':
            return 'Aquí va otro: ' + poner_musica()
        elif self.contexto == 'DEFAULT':
            return '¿Podrías tratar de expresarte mejor?'
        else:
            return '¿Podrías tratar de expresarte mejor?'

#---------------------------------------#
#  Base de conocimiento                 #
#---------------------------------------#
conocimiento = conocimientoT()


#---------------------------------------#
#  Interfaz de texto                    #
#---------------------------------------#
def chatBot():
    input_usuario = ''
    asistente = ChatBot()    
    while input_usuario != ' ':
        try:
            input_usuario = input('>> ')            
        except EOFError:
            print('Saliendo...')
            sys.exit(0)
        except KeyboardInterrupt: 
            print('Saliendo...')
            sys.exit(0)
        else:
            print(asistente.responder(input_usuario))

if __name__ == "__main__":
    chatBot()