import sys

import pygame

from config import (ANCHO, ALTURA, VELOCIDAD_INICIAL, ACELERACION, SNAKE_INICIAL,
                    DIRECCION_INICIAL, ROCAS_FIJAS, CANTIDAD_ROCAS_ALEATORIAS)
from logica import resolver_direccion, mover, posicion_aleatoria, es_perdedor
from pantallas import cargar_imagenes, dibujar_menu, dibujar_campo, dibujar_puntaje, dibujar_game_over

TECLAS_DIRECCION = {pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN', pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT'}


def salir():
    pygame.quit()
    sys.exit()


def esperar_tecla(tipo_evento, tecla_continuar, tecla_salir):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir()
            if event.type == tipo_evento and event.key == tecla_salir:
                salir()
            if event.type == tipo_evento and event.key == tecla_continuar:
                pygame.event.clear()
                return
        pygame.time.wait(50)  # evita que la espera ocupe el 100% del procesador


def leer_direccion(dir_siguiente):
    '''Procesa los eventos del frame y devuelve la última dirección pedida con las flechas.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            salir()
        if event.type == pygame.KEYDOWN and event.key in TECLAS_DIRECCION:
            dir_siguiente = TECLAS_DIRECCION[event.key]
    return dir_siguiente


def jugar_partida(ventana, reloj, imagenes):
    snake = [posicion.copy() for posicion in SNAKE_INICIAL]
    rocas = [roca.copy() for roca in ROCAS_FIJAS]
    for _ in range(CANTIDAD_ROCAS_ALEATORIAS):
        rocas.append(posicion_aleatoria(snake, rocas))
    fruta = posicion_aleatoria(snake, rocas)
    puntaje = 0
    velocidad = VELOCIDAD_INICIAL
    direccion = dir_siguiente = DIRECCION_INICIAL
    iniciado = False

    while True:
        dir_siguiente = leer_direccion(dir_siguiente)
        direccion = resolver_direccion(direccion, dir_siguiente)
        snake.append(mover(snake[-1], direccion))

        if snake[-1] == fruta:
            fruta = posicion_aleatoria(snake, rocas)
            puntaje += 1
            velocidad *= ACELERACION
        else:
            snake.pop(0)

        dibujar_campo(ventana, imagenes, snake, rocas, fruta, direccion)
        if es_perdedor(snake, rocas):
            return puntaje
        dibujar_puntaje(ventana, puntaje)
        pygame.display.update()

        # El primer frame queda congelado hasta que el jugador toque algo, para que no arranque desprevenido.
        if not iniciado:
            pygame.event.wait()
            iniciado = True
        reloj.tick(velocidad)


def main():
    pygame.init()
    pygame.display.set_caption('Juego Snake')
    ventana = pygame.display.set_mode((ANCHO, ALTURA))
    reloj = pygame.time.Clock()
    imagenes = cargar_imagenes()

    while True:
        dibujar_menu(ventana, imagenes)
        esperar_tecla(pygame.KEYDOWN, tecla_continuar=pygame.K_a, tecla_salir=pygame.K_b)
        puntaje = jugar_partida(ventana, reloj, imagenes)
        dibujar_game_over(ventana, puntaje)
        esperar_tecla(pygame.KEYUP, tecla_continuar=pygame.K_r, tecla_salir=pygame.K_q)


if __name__ == '__main__':
    main()
