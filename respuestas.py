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

	if mensaje == 'asustado':
		return asustado()
	
	if mensaje == 'ansioso':
		return ansioso()

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
		'Aveces podemos ser muy hirientes en los comentarios que hacemos pero se puede hablar con la otra persona para mejorar la relación humana'
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

def asustado():
	asustados = [
		'Respira profundo y recuerda que el miedo es una emoción natural.',
		'Puede ser una señal de que estás fuera de tu zona de confort.',
		'Incluso en los momentos más oscuros, siempre hay una luz al final del túnel.',
		'El miedo puede paralizarnos, pero también puede ser una oportunidad para fortalecernos.'
	]
	return asustados[random.randint(0,len(asustados)-1)]

def ansioso():
	ansiosos = [
		'Recuerda que tus sentimientos son válidos.',
		'Aveces el futuro puede ser aterrador.',
		'No te deberias abrumar por cosas que esten fuera de tu control.',
		'Aplica el metodo de 5-4-3-2-1. 5 cosas que ves, 4 cosas que puedes tocar, 3 cosas que puedes escuchar, 2 cosas que puedes oler, 1 cosa que puedes saborear.'
	]
	return ansiosos[random.randint(0,len(ansiosos)-1)]
