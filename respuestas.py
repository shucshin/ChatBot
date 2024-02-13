import random

def get_response(message: str) -> str:
	mensaje = message.lower()

	if mensaje == 'hola':
		return hola()

	if mensaje == 'dado':
		return str(random.randint(1, 6))
	
	if mensaje == 'triste':
		return triste()

	if mensaje == 'feliz':
		return feliz()
	
	if mensaje == 'enojado':
		return enojado()
	
	if mensaje == 'preocupado':
		return preocupado()

	return 'Lo siento, no te entendí'


def hola():
	holas = [
		'¡Hola!',
		'Helou',
		'Bonjour'
	]
	return holas[random.randint(0,len(holas)-1)]

def triste():
	tristes = [
		'Lamento mucho escuchar que te sientes triste.',
		'Tómate una café, te sentirás mejor.',
		'No me importa que estes triste.',
		'Con el tiempo se pasará, no te preocupes.'
	]
	return tristes[random.randint(0,len(tristes)-1)]

def feliz():
	felices = [
		'Me alegra escuchar que te sientes feliz.',
		'No te durará para siempre, disfruta el momento.',
		'Puedo destruir tu felicidad en un instante.',
		'Yo no se cómo se siente la felicidad, simplemente soy un Bot.'
	]
	return felices[random.randint(0,len(felices)-1)]

def enojado():
	enojados = [
		'Respira profundo y toma un momento para calmarte. Estoy aquí para escucharte y ayudarte a encontrar una solución.',
		'A veces, expresar lo que sientes puede aliviar la tensión.',
		'Entiendo que estás pasando por un momento difícil. Hablame más sobre el problema',
		'Aveces podemos ser muy hirientes en los comentarios que hacemos pero se puede habalr con la otra persona para mejorar la relación humana'
	]
	return enojados[random.randint(0,len(enojados)-1)]

def preocupado():
	preocupados = [
		'Las preocupaciones son parte de la vida, pero también se puede trabajar en equipo para encontrar soluciones.',
		'Recuerda que nunca estamos solos, siempre hay una persona que esta pensando en como nos encontramos, alguen siempre vera por ti.',
		'A veces, es útil dividir las preocupaciones en pasos más pequeños.',
		'La autocompasión es importante. Permítete sentir estas preocupaciones, pero también recuerda que estamos aquí para encontrar formas de superarlas juntos.'
	]
	return preocupados[random.randint(0,len(preocupados)-1)]