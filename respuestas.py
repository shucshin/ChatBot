import random

def get_response(message: str) -> str:
	mensaje = message.lower()

	if mensaje == 'hola':
		return '¡Hola!'

	if mensaje == 'dado':
		return str(random.randint(1, 6))

	if mensaje == 'chiste':
		return randomChiste()

	return 'Lo siento, no te entendí'

def randomChiste():
    chistes = ['Chiste1', 'Chiste2', 'Chiste3']

    return chistes[random.randint(0,2)]