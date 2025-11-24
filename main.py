import pygame as pg
from funciones.configuracion import *
from funciones.sudoku import *
import funciones.botones as botones
from funciones.numeros import *
from funciones.teclas import *
import funciones.sudoku as sudoku

pg.init()   

volumen_musica = 0.5 
reproducir_musica_loop("./sonidos/musica_fondo.mp3", volumen_musica)

puntaje = 0  
regiones_completas = set()
tablero_completo_bonificado = False

pantalla = iniciar_juego()
pantalla.blit(fondo, (0, 0))
dibujar_grilla(pantalla)
llenar_tablero(tab_incompleto, pantalla)
tab_usuario = [fila[:] for fila in tab_incompleto]


def pos_a_indices(pos_x: int, pos_y:int, columnas_rangos: list, filas_rangos: list) -> tuple:
    """
    Función que convierte las coordenadas del mouse en índices de fila y columna de la grilla SUDOKU.

    Args:
        pos_x (int): Coordenada X del mouse en la grilla SUDOKU.
        pos_y (int): Coordenada Y del mouse en la grilla SUDOKU.
        columnas_rangos (list, optional): Lista con coordenadas de celdas en columnas. Defaults: columnas_rangos.
        filas_rangos (list, optional): Lista con coordenadas de celdas en filas. Defaults: filas_rangos.

    Returns:
        tuple[int | None, int | None]: Tupla con (fila, columna) donde cada elemento es el índice correspondiente, o None si no se encuentra coincidencia exacta. 
    """
    col = None
    for i in range(len(columnas_rangos)):
        sx, ex = columnas_rangos[i]
        if sx == pos_x:
            col = i
            break

    fila = None
    for j in range(len(filas_rangos)):
        sy, ey = filas_rangos[j]
        if sy == pos_y:
            fila = j
            break

    return fila, col

fuente_puntaje = pg.font.Font(None, 40)

def mostrar_puntaje() -> None:
    """
    Función que muestra el puntaje en pantalla.
    """

    texto = f"Score: {puntaje:04d}"
    render = fuente_puntaje.render(texto, True, (0, 0, 0))

    rectangulo(pantalla, "orange", 293, 8, 170, 30) #Fondo del score en pantalla
    pantalla.blit(render, (298, 10)) #Posición del score en pantalla

def verificar_tablero() -> None:
    """
    Compara el tablero del usuario (tab_usuario) contra la solución (tab_completo)
    y CALCULA el puntaje DESDE CERO según la consigna:

    -1 punto por cada número mal colocado.
    +9 puntos por cada región 3x3 completamente correcta.
    +81 puntos extra si toda la matriz 9x9 está correcta (sin errores ni celdas vacías).
    """
    global puntaje, regiones_completas, tablero_completo_bonificado

    errores = []
    vacias = 0

    # Contar errores y celdas vacías
    for fila in range(9):
        for columna in range(9):
            usuario = tab_usuario[fila][columna]
            sudoku_completo = tab_completo[fila][columna]

            if usuario == 0:
                vacias += 1
            elif usuario != sudoku_completo:
                errores.append((fila, columna))

    # Contar regiones 3x3 completas
    nuevas_regiones = 0
    for start_fila in (0, 3, 6):
        for start_columna in (0, 3, 6):
            region_ok = True
            for i in range(start_fila, start_fila + 3):
                for j in range(start_columna, start_columna + 3):
                    if tab_usuario[i][j] != tab_completo[i][j]:
                        region_ok = False
                        break
                if not region_ok:
                    break
            if region_ok:
                region_id = (start_fila, start_columna)
                if region_id not in regiones_completas:
                    regiones_completas.add(region_id)
                    nuevas_regiones += 1

    # Ver si el tablero completo está perfecto
    tablero_completo_correcto = (len(errores) == 0 and vacias == 0)

    # Calcular puntaje DESDE CERO
    puntaje -= len(errores)           # -1 por cada error en ESTA verificación
    puntaje += nuevas_regiones * 9    # +9 por cada región nueva correcta
    if tablero_completo_correcto and not tablero_completo_bonificado:
        puntaje += 81                 # +81 solo la primera vez que está perfecto
        tablero_completo_bonificado = True

    if len(errores) > 0:
        botones.sonido_error()
    elif tablero_completo_correcto:
        botones.sonido_acierto()

    pantalla.blit(fondo, (0, 0))
    dibujar_grilla(pantalla)
    llenar_tablero(tab_usuario, pantalla)
    
    CELL = 72 
    OFFSET = 52
    
    for fila, columna in errores:
        x = OFFSET + columna * CELL
        y = OFFSET + fila * CELL
        pg.draw.rect(pantalla, (255, 0, 0), (x, y, ancho, alto), 4)
        
    mostrar_puntaje()

def reiniciar_tablero():
    global tab_usuario, cuadrado_seleccionado, puntaje, tab_incompleto, tab_completo
    global regiones_completas, tablero_completo_bonificado

    # Reset de estado del puntaje acumulado
    regiones_completas = set()
    tablero_completo_bonificado = False
    puntaje = 0

    # Generar un tablero COMPLETO nuevo
    sudoku.tab_completo = sudoku.generar_tablero_completo()

    # Generar un tablero INCOMPLETO nuevo
    sudoku.tab_incompleto = sudoku.crear_sudoku_incompleto_por_bloque(
        sudoku.tab_completo,
        visibles_por_bloque=5
    )

    # Actualizar referencias locales de main.py
    tab_completo = sudoku.tab_completo
    tab_incompleto = sudoku.tab_incompleto

    # Nuevo tablero de usuario
    tab_usuario = [fila[:] for fila in tab_incompleto]
    cuadrado_seleccionado = None

    # Redibujar
    pantalla.blit(fondo, (0, 0))
    dibujar_grilla(pantalla)
    llenar_tablero(tab_usuario, pantalla)
    mostrar_puntaje()



def mutear():
    global volumen_musica
    volumen_musica = 0.0
    pg.mixer.music.set_volume(volumen_musica)  


def desmutear():
    global volumen_musica
    volumen_musica = 0.5
    pg.mixer.music.set_volume(volumen_musica)  


while True:
    botones.crear_boton(pantalla, 703, 53, 240, 52, "VERIFICAR", verificar_tablero)
    botones.crear_boton(pantalla, 703, 115, 240, 52, "REINICIAR", reiniciar_tablero)
    botones.crear_boton(pantalla, 703, 177, 240, 52, "VOLVER", None)
    botones.crear_boton(pantalla, 800, 700, 160, 50, "DESMUTEAR", desmutear)
    botones.crear_boton(pantalla, 680, 700, 120, 50, "MUTEAR", mutear)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            exit()
            
        elif evento.type == pg.MOUSEBUTTONDOWN:
            cuadrado_seleccionado = celda_seleccionada(evento, columnas_rangos, filas_rangos, pantalla)
            botones.reproducir_sonido("./sonidos/celda_marcada.mp3", 0.4)
            llenar_tablero(tab_usuario, pantalla)
            
        if evento.type == pg.KEYDOWN: 
            try:
                pos_x, pos_y = cuadrado_seleccionado
                fila, columna = pos_a_indices(pos_x, pos_y, columnas_rangos, filas_rangos)

                if tab_incompleto[fila][columna] != 0:
                    pass
                else:
                    if evento.key in (pg.K_BACKSPACE, pg.K_DELETE, pg.K_0):
                        tab_usuario[fila][columna] = 0
                    else:
                        numero_ingresado = valores_teclas(pantalla, evento, pos_x, pos_y)
                        
                        if numero_ingresado in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                            botones.sonido_numero_ingresado()
                            tab_usuario[fila][columna] = numero_ingresado

                dibujar_grilla(pantalla)
                llenar_tablero(tab_usuario, pantalla)
                pg.draw.rect(pantalla, COLOR_AMARILLO, (inicio_x, inicio_y, ancho, alto), 4)
                
            except:
                pass
        
    mostrar_puntaje()   
    pg.display.flip()

