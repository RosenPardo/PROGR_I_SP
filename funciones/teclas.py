import pygame as pg
from funciones.numeros import *

pg.init()

imagen_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5, numero_6, numero_7, numero_8, numero_9]

def valores_teclas(pantalla, evento, x, y):
    """
    Detecta si se presionó una tecla del 1 al 9 y dibuja la imagen correspondiente en la posición indicada.

    Args:
        pantalla (pygame.Surface): Superficie donde se dibujará la imagen del número.
        evento (pygame.event.Event): Evento de teclado capturado por Pygame.
        x (int): Posición horizontal donde se dibujará la imagen.
        y (int): Posición vertical donde se dibujará la imagen.

    Returns:
        int: Número seleccionado (1 a 9) según la tecla presionada. Si no se presiona una tecla válida, devuelve 0.
    """
    lista_teclas = [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9]
    lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_seleccionado = 0

    for i in range(len(lista_teclas)):
        if evento.key == lista_teclas[i]:
            num_seleccionado = lista_numeros[i]
            pantalla.blit(imagen_numeros[num_seleccionado - 1], (x , y))

    return num_seleccionado


