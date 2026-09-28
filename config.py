ANCHO = 800
ALTURA = 600
BLOQUE = 20

VELOCIDAD_INICIAL = 10  # movimientos por segundo
ACELERACION = 1.05      # factor aplicado a la velocidad por cada fruta comida

NEGRO = (0, 0, 0, 100)  # el alfa solo se usa en la capa semitransparente del game over
BLANCO = (255, 255, 255)

# La cabeza es el último elemento: el snake avanza agregando al final y quitando del principio.
SNAKE_INICIAL = [[400, 300], [380, 300], [360, 300], [340, 300]]
DIRECCION_INICIAL = 'LEFT'

ROCAS_FIJAS = [[400, 400], [420, 420], [420, 400], [400, 420], [160, 160], [180, 180], [200, 200]]
CANTIDAD_ROCAS_ALEATORIAS = 4
