from functools import lru_cache
from pathlib import Path

import pygame

from config import ANCHO, ALTURA, NEGRO, BLANCO

CARPETA_ASSETS = Path(__file__).parent / 'assets'

# La imagen de la cabeza mira a la derecha; se rota según la dirección.
ROTACION_CABEZA = {'RIGHT': 0, 'UP': 90, 'LEFT': 180, 'DOWN': 270}


def cargar_imagen(nombre, color_transparente=None):
    imagen = pygame.image.load(CARPETA_ASSETS / nombre).convert()
    if color_transparente is not None:
        imagen.set_colorkey(color_transparente)
    return imagen


def cargar_imagenes():
    return {
        'menu': cargar_imagen('menu.png'),
        'fondo': cargar_imagen('fondo.png'),
        'cabeza': cargar_imagen('cabeza.png', NEGRO),
        'cuerpo': cargar_imagen('cuerpo.png', NEGRO),
        'fruta': cargar_imagen('manzana.png', NEGRO),
        'roca': cargar_imagen('roca.png', BLANCO),
    }


@lru_cache
def fuente(nombre, tamaño):
    return pygame.font.SysFont(nombre, tamaño)


def dibujar_menu(ventana, imagenes):
    ventana.blit(imagenes['menu'], (0, 0))
    pygame.display.update()


def dibujar_campo(ventana, imagenes, snake, rocas, fruta, direccion):
    ventana.blit(imagenes['fondo'], (0, 0))
    for posicion in snake[:-1]:
        ventana.blit(imagenes['cuerpo'], posicion)
    ventana.blit(pygame.transform.rotate(imagenes['cabeza'], ROTACION_CABEZA[direccion]), snake[-1])
    ventana.blit(imagenes['fruta'], fruta)
    for roca in rocas:
        ventana.blit(imagenes['roca'], roca)


def dibujar_puntaje(ventana, puntaje):
    texto = fuente('Arial', 30).render('Puntaje: ' + str(puntaje), True, NEGRO)
    ventana.blit(texto, (0, 0))


def dibujar_game_over(ventana, puntaje):
    capa = pygame.Surface((ANCHO, ALTURA), pygame.SRCALPHA)
    capa.fill(NEGRO)
    ventana.blit(capa, (0, 0))

    titulo = fuente('Times new roman', 55).render('Has Muerto. Puntaje: ' + str(puntaje), True, NEGRO)
    ventana.blit(titulo, titulo.get_rect(midtop=(ANCHO / 2, ALTURA / 2 - 50)))

    texto_salir = fuente('Times new roman', 30).render('Presione [q] para salir.', True, NEGRO)
    texto_reintentar = fuente('Times new roman', 30).render('Presione [r] para volver a jugar.', True, NEGRO)
    rect_salir = texto_salir.get_rect(midtop=(ANCHO / 2 - 100, ALTURA / 2 + 10))
    # Las dos opciones comparten el borde izquierdo para leerse como una lista.
    rect_reintentar = texto_reintentar.get_rect(topleft=(rect_salir.left, ALTURA / 2 + 50))
    ventana.blit(texto_salir, rect_salir)
    ventana.blit(texto_reintentar, rect_reintentar)

    pygame.display.flip()
