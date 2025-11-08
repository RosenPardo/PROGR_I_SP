import pygame as pg

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


def iniciar_juego():
    pg.init()

    icono = pg.image.load("D:/UTN/Programacion_I_312/Pygame/img/icono.png")  #RUTA DE ICONO: COMPU ROSEN
    #icono = pg.image.load("JUNCITO, PONÉ TU URL") #RUTA DE ICONO: COMPU JUANCHI
    #icono = pg.image.load("JESSICAAA, TU URL ACÁ") #RUTA DE ICONO: COMPU VALE
    
    
    pg.display.set_icon(icono)
    
    titulo = "SUDOKU UTN FRA"
    dimension_pantalla = (750, 750)

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

def celda_seleccionada(evento, columnas_rangos, filas_rangos, pantalla):
                x, y = evento.pos
                for col in range(9):
                    inicio_x, fin_x = columnas_rangos[col]
                    if inicio_x <= x <= fin_x:
                        for fila in range(9):
                            inicio_y, fin_y = filas_rangos[fila]
                            if inicio_y <= y <= fin_y:
                                dibujar_grilla(pantalla)
                                return rectangulo(pantalla, COLOR_AMARILLO, inicio_x, inicio_y, ancho, alto)


"""Código DeepSeek:
import pygame as pg

# Constantes
POS_X = 52
POS_Y = 52
ANCHO_CELDA = 70
ALTO_CELDA = 70
COLOR_CELDA = (235, 235, 235)
COLOR_CUADRADO = (200, 200, 200)
COLOR_BORDE = (0, 0, 0)
ESPACIADO = 72
ANCHO_CUADRADO = 214
ALTO_CUADRADO = 214
SEPARACION_CUADRADOS = 216  # 214 + 2

def rectangulo(pantalla, color, pos_x, pos_y, ancho, alto):
    pg.draw.rect(pantalla, color, (pos_x, pos_y, ancho, alto))

def dibujar_grilla(pantalla):
    # Marco exterior
    rectangulo(pantalla, COLOR_BORDE, POS_X, POS_Y, 645, 645)
    
    # Cuadrados 3x3 principales (regiones del Sudoku)
    for fila in range(3):
        for columna in range(3):
            x = POS_X + columna * SEPARACION_CUADRADOS
            y = POS_Y + fila * SEPARACION_CUADRADOS
            rectangulo(pantalla, COLOR_CUADRADO, x, y, ANCHO_CUADRADO, ALTO_CUADRADO)
    
    # Celdas individuales 9x9
    for fila in range(9):
        for columna in range(9):
            x = POS_X + columna * ESPACIADO
            y = POS_Y + fila * ESPACIADO
            rectangulo(pantalla, COLOR_CELDA, x, y, ANCHO_CELDA, ALTO_CELDA)
"""