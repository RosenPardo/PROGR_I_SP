import pygame as pg
from funciones.sudoku import tab_incompleto, tab_completo, facil, medio, dificil

import funciones.numeros as numeros 


pos_x = 52
pos_y = 52
ancho = 70
alto = 70
COLOR_BLANCO = (235, 235, 235)
COLOR_NEGRO = (0, 0, 0)
COLOR_GRIS = (200, 200, 200)
COLOR_AMARILLO = (255, 230, 133)
espaciado = 72
espaciado_extra = 2
columnas_rangos = [(52, 122), (124, 194), (196, 266), (268, 338), (340, 410), (412, 482), (484, 554), (556, 626), (628, 698)]
filas_rangos = columnas_rangos

def llenar_tablero(sudoku_incompleto,visor):
    for fila in range(9):
        for columna in range(9):
            numero = sudoku_incompleto[fila][columna]
            if numero != 0:
                pos_x = 52 + columna * 72
                pos_y = 52 + fila * 72
                if numero == 1:
                    visor.blit(numeros.numero_1, (pos_x , pos_y ))
                elif numero == 2:
                    visor.blit(numeros.numero_2, (pos_x , pos_y ))
                elif numero == 3:
                    visor.blit(numeros.numero_3, (pos_x , pos_y ))
                elif numero == 4:
                    visor.blit(numeros.numero_4, (pos_x , pos_y ))
                elif numero == 5:
                    visor.blit(numeros.numero_5, (pos_x , pos_y ))
                elif numero == 6: 
                    visor.blit(numeros.numero_6, (pos_x , pos_y ))      
                elif numero == 7:
                    visor.blit(numeros.numero_7, (pos_x , pos_y ))
                elif numero == 8:
                    visor.blit(numeros.numero_8, (pos_x , pos_y ))  
                elif numero == 9:
                    visor.blit(numeros.numero_9, (pos_x , pos_y ))
    


def iniciar_juego():
    pg.init()

    icono = pg.image.load("./img/icono.png") 
    pg.display.set_icon(icono)
    
    titulo = "SUDOKU UTN FRA"
    dimension_pantalla = (1002, 750)

    pg.display.set_caption(titulo)
    pantalla = pg.display.set_mode(dimension_pantalla)
    pantalla.fill((77, 154, 163))

    return pantalla

def rectangulo(pantalla, color, pos_x, pos_y, ancho, alto):
    pg.draw.rect(pantalla, color, (pos_x, pos_y, ancho, alto))

def dibujar_grilla(pantalla):
    rectangulo(pantalla, COLOR_NEGRO, pos_x = 52, pos_y= 52, ancho = 645, alto = 645)
    rectangulo(pantalla, COLOR_GRIS, pos_x = 52, pos_y= 52, ancho = 214, alto = 214)
    rectangulo(pantalla, COLOR_GRIS, pos_x = 268, pos_y= 52, ancho = 214, alto = 214)
    rectangulo(pantalla, COLOR_GRIS, pos_x = 484, pos_y= 52, ancho = 214, alto = 214)

    rectangulo(pantalla, COLOR_GRIS, pos_x = 52, pos_y= 268, ancho = 214, alto = 214)
    rectangulo(pantalla, COLOR_GRIS, pos_x = 268, pos_y= 268, ancho = 214, alto = 214)
    rectangulo(pantalla, COLOR_GRIS, pos_x = 484, pos_y= 268, ancho = 214, alto = 214)

    rectangulo(pantalla, COLOR_GRIS, pos_x = 52, pos_y= 484, ancho = 214, alto = 214)
    rectangulo(pantalla, COLOR_GRIS, pos_x = 268, pos_y= 484, ancho = 214, alto = 214)
    rectangulo(pantalla, COLOR_GRIS, pos_x = 484, pos_y= 484, ancho = 214, alto = 214)

    for fila in range(9):
        for columna in range(9): 
            x = pos_x + columna * espaciado
            y = pos_y + fila * espaciado
            rectangulo(pantalla, COLOR_BLANCO, x, y, ancho, alto)
    
    # dificultades pruebas

    #llenar_tablero(tab_incompleto,pantalla)
    #llenar_tablero(facil,pantalla)
    llenar_tablero(medio,pantalla)
    #llenar_tablero(dificil,pantalla)



def celda_seleccionada(evento, columnas_rangos, filas_rangos, pantalla):
                x, y = evento.pos
                for col in range(9):
                    inicio_x, fin_x = columnas_rangos[col]
                    if inicio_x <= x <= fin_x:
                        for fila in range(9):
                            inicio_y, fin_y = filas_rangos[fila]
                            if inicio_y <= y <= fin_y:
                                dibujar_grilla(pantalla)
                                rectangulo(pantalla, COLOR_AMARILLO, inicio_x, inicio_y, ancho, alto)
                                return inicio_x, inicio_y

