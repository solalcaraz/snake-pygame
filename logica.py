from random import randint

from config import ANCHO, ALTURA, BLOQUE

OPUESTA = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
DESPLAZAMIENTO = {'UP': (0, -BLOQUE), 'DOWN': (0, BLOQUE), 'LEFT': (-BLOQUE, 0), 'RIGHT': (BLOQUE, 0)}


def resolver_direccion(direccion, dir_siguiente):
    '''Aplica la dirección pedida salvo que sea la opuesta a la actual.
    Así, si se presionan dos teclas en el mismo frame, el snake no puede girar 180° sobre sí mismo.'''
    if dir_siguiente != OPUESTA[direccion]:
        return dir_siguiente
    return direccion


def mover(cabeza, direccion):
    dx, dy = DESPLAZAMIENTO[direccion]
    return [cabeza[0] + dx, cabeza[1] + dy]


def posicion_aleatoria(snake, rocas):
    '''Devuelve una posición [x, y] alineada a la grilla que no esté ocupada por el snake ni por una roca.
    Nunca elige la primera fila ni la primera columna.'''
    while True:
        posicion = [randint(1, (ANCHO - BLOQUE) // BLOQUE) * BLOQUE,
                    randint(1, (ALTURA - BLOQUE) // BLOQUE) * BLOQUE]
        if posicion not in snake and posicion not in rocas:
            return posicion


def es_perdedor(snake, rocas):
    cabeza = snake[-1]
    fuera_del_campo = not (0 <= cabeza[0] <= ANCHO - BLOQUE and 0 <= cabeza[1] <= ALTURA - BLOQUE)
    return cabeza in snake[:-1] or fuera_del_campo or cabeza in rocas
