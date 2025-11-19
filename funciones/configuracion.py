import pygame as pg
from funciones.sudoku import tab_incompleto, tab_completo, facil, medio, dificil
import funciones.numeros as numeros 

pg.init()


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
celdas_ocupadas = []
fondito = pg.image.load("./img/fondo.png")
fondo = pg.transform.scale(fondito,(1002, 750))  



def reproducir_musica_loop(ruta_mp3,volumen):
    """
    Función para reproducir MP3 en loop infinito
    """
    try:
        pg.mixer.init()
        pg.mixer.music.load(ruta_mp3)
        pg.mixer.music.set_volume(volumen)  
        pg.mixer.music.play(-1)
        return True
    except:
        return False




def coordenadas_celdas(pos_inicial, ancho_celda, espaciado_celdas, cantidad):
    rangos = []
    actual = pos_inicial
    
    for _ in range(cantidad):
        inicio = actual
        fin = actual + ancho_celda
        rangos.append((inicio, fin))
        actual = fin + espaciado_celdas
    
    return rangos

columnas_rangos = coordenadas_celdas(pos_x, ancho, espaciado_extra, 9)
filas_rangos = coordenadas_celdas(pos_y, alto, espaciado_extra, 9)






def contador(lista):
    acumulador = 0
    for _ in range(len(lista)):
        acumulador += 1
    
    return acumulador


def llenar_tablero(sudoku_incompleto, visor):
    CELL = 72
    OFFSET = 52

    # numeros de sudoku
    numero_imagenes = {
        1: numeros.numero_1,
        2: numeros.numero_2,
        3: numeros.numero_3,
        4: numeros.numero_4,
        5: numeros.numero_5,
        6: numeros.numero_6,
        7: numeros.numero_7,
        8: numeros.numero_8,
        9: numeros.numero_9,
    }

    for posicion_fila in range(9):
        fila = sudoku_incompleto[posicion_fila]
        for posicion_columna in range(9):
            numero = fila[posicion_columna]
            if numero != 0:
                x = OFFSET + posicion_columna * CELL
                y = OFFSET + posicion_fila * CELL
                celdas_ocupadas.append((x, y))
                visor.blit(numero_imagenes[numero], (x, y))

    # print(f"la cantidad de celdas ocupadas es :{contador(celdas_ocupadas)}")
    # print("Celdas ocupadas:")
    # print(celdas_ocupadas)  




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
    rectangulo(pantalla, COLOR_NEGRO, pos_x, pos_y, ancho = 645, alto = 645)
    
    x = pos_x
    y = pos_y

    for fila in range(3):
        for columna in range(3): 
            rectangulo(pantalla, COLOR_GRIS, x, y, ancho = 214, alto = 214)
            x += 216
        y += 216
        x = pos_x

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
                                rectangulo(pantalla, COLOR_AMARILLO, inicio_x, inicio_y, ancho, alto)
                                
                                #botones.sonido_celda_seleccionada()
                                
                                return inicio_x, inicio_y

