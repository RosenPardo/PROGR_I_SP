import pygame as pg
import funciones.sudoku as sudoku
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
COLOR_CELDA_FIJA = (220, 230, 255)
MARGEN = 3

espaciado = 72
espaciado_extra = 2
celdas_ocupadas = []
fondito = pg.image.load("./img/fondo.png")
fondo = pg.transform.scale(fondito,(1002, 750))  


def reproducir_musica_loop(ruta_mp3,volumen):
    """
    reproduce un sonido MP3 en loop infinito
    """
    try:
        pg.mixer.init()
        pg.mixer.music.load(ruta_mp3)
        pg.mixer.music.set_volume(volumen)  
        pg.mixer.music.play(-1)
        return True
    except:
        return False


def coordenadas_celdas(pos_inicial, ancho_celda, espaciado_celdas, cantidad) -> list:
    """
    calcula las coordenadas de inicio y fin para una serie 
    de celdas consecutivas, considerando el ancho de cada celda y el espacio entre ellas

    Args:
        pos_inicial : posicion en el eje inicial
        ancho_celda : ancho de la celda individual
        espaciado_celdas : espacio entre celdas
        cantidad : cantidad de celdas

    Returns:
        lista de rangos de de las celdas
    """
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


def llenar_tablero(sudoku_incompleto, visor) -> None:
    """
    Dibuja un tablero de Sudoku incompleto en la superficie especificada.

    Args:
        sudoku_incompleto (list): Matriz 9x9 del tablero de Sudoku incompleto.
                                Cada elemento es un entero entre 0-9, donde 0 indica celda vacía.
       
        visor : Superficie donde se dibujará el tablero.

    """
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
            x = OFFSET + posicion_columna * CELL
            y = OFFSET + posicion_fila * CELL

            if sudoku.tab_incompleto[posicion_fila][posicion_columna] != 0:
                pg.draw.rect(
                    visor,
                    COLOR_CELDA_FIJA,
                    (x + MARGEN, y + MARGEN, CELL - 2 * MARGEN, CELL - 2 * MARGEN),
                )

            numero = fila[posicion_columna]
            if numero != 0:
                celdas_ocupadas.append((x, y))
                visor.blit(numero_imagenes[numero], (x, y))


def iniciar_juego():
    """
    inicializa la pantalla del juego con sus dimenciones, icono y titulo.
    """
    pg.init()

    icono = pg.image.load("./img/icono.png") 
    pg.display.set_icon(icono)
    
    titulo = "SUDOKU UTN FRA"
    dimension_pantalla = (1002, 750)

    pg.display.set_caption(titulo)
    pantalla = pg.display.set_mode(dimension_pantalla)
    pantalla.fill((77, 154, 163))

    return pantalla


def rectangulo(pantalla, color, pos_x, pos_y, ancho, alto) -> None:
    """
    dibuja un rectangulo en pantalla

    Args:
        pantalla : superficie donde de va dibujar
        color : color del rectangulo
        pos_x : posicion x del rectangulo
        pos_y : posicion y del rectangulo
        ancho : ancho del rectangulo
        alto : alto del rectangulo
    """
    pg.draw.rect(pantalla, color, (pos_x, pos_y, ancho, alto))


def dibujar_grilla(pantalla):
    """
    Dibuja la grilla completa de un tablero de Sudoku en la pantalla especificada.

    Args:
        pantalla : Superficie donde se dibujará la grilla.
    """
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
    """
        sellecciona y resalta la celda de un tablero de Sudoku seleccionada por el usuario.

        Args:
            evento (pygame.Event): Evento de PyGame de la posición del clic del mouse.
            columnas_rangos (list): Lista de tuplas con los rangos (inicio, fin) de las columnas.
            filas_rangos (list): Lista de tuplas con los rangos (inicio, fin) de las filas.
            pantalla : Superficie donde se dibujará el resaltado.

        Returns:
            tuple or None: Tupla con las coordenadas (x, y) de la celda seleccionada si es válida,
                        o None si:
                                    - La celda pertenece al tablero original (no editable)
                                    - El clic está fuera del tablero
                                    - No se encuentra una celda válida
    """
    x, y = evento.pos
    for col in range(9):
        inicio_x, fin_x = columnas_rangos[col]
        if inicio_x <= x <= fin_x:
            for fila in range(9):
                inicio_y, fin_y = filas_rangos[fila]
                if inicio_y <= y <= fin_y:

                    if sudoku.tab_incompleto[fila][col] != 0:
                        return None

                    dibujar_grilla(pantalla)
                    pg.draw.rect(pantalla, COLOR_AMARILLO, (inicio_x, inicio_y, ancho, alto), 4)
                    return inicio_x, inicio_y


