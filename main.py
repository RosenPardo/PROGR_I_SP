import pygame as pg
from funciones.configuracion import *
from funciones.sudoku import *
import funciones.botones as botones
from funciones.numeros import *
from funciones.teclas import *

pg.init()   

volumen_musica = 0.5 

puntaje = 0            # score actual
regiones_completas = set()  # para no sumar +9 dos veces por la misma región
juego_terminado = False     # para bloquear inputs cuando gana

pantalla = iniciar_juego()

pantalla.blit(fondo, (0, 0))

reproducir_musica_loop("./sonidos/musica_fondo.mp3", volumen_musica)

dibujar_grilla(pantalla)

# dificultades pruebas
#llenar_tablero(tab_incompleto,pantalla)
#llenar_tablero(facil,pantalla)
#llenar_tablero(medio,pantalla)
llenar_tablero(dificil, pantalla)


# tab_usuario = [fila[:] for fila in tab_incompleto]
tab_usuario = [fila[:] for fila in dificil]


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
    """Compara el tablero del usuario (tab_usuario) contra la solución (tab_completo), y modifica puntaje en pantalla, notificando en consola los errores encontrados. 
    """
    global puntaje, regiones_completas, juego_terminado

    errores = []
    vacias = 0
    
    for fila in range(9):
        for columna in range(9):
            usuario = tab_usuario[fila][columna]
            sudoku_completo = tab_completo[fila][columna]
            
            if usuario == 0:
                vacias += 1
            elif usuario != sudoku_completo:

                
                errores.append((fila, columna, usuario, sudoku_completo))

    # PUNTOS POR ERRORES: -1 por casillero incorrecto
    puntaje -= len(errores)
    
    if len(errores) > 0:
        botones.sonido_error()    

    # PUNTOS POR REGIÓN COMPLETA: +9 por cada bloque 3x3 correcto (solo una vez)
    for start_fila in (0, 3, 6):
        for start_columna in (0, 3, 6):
            id_region = (start_fila // 3, start_columna // 3)
            if id_region in regiones_completas:
                continue  # ya se contó antes

            region_ok = True
            for i in range(start_fila, start_fila + 3):
                for j in range(start_columna, start_columna + 3):
                    if tab_usuario[i][j] != tab_completo[i][j]:
                        region_ok = False
                        break
                if not region_ok:
                    break

            if region_ok:
                puntaje += 9
                regiones_completas.add(id_region)

    if not errores and vacias == 0:
        # Tablero completo y correcto: +81 una vez
        if not juego_terminado:
            puntaje += 81
            juego_terminado = True
            print("Sudoku correcto: ¡ganaste!")

    # Mensajes por consola
    if errores:
        print(f"Encontré {len(errores)} error(es):")
        for fila, columna, usuario, sudoku_completo in errores:
            print(f"  - Celda (fila {fila+1}, col {columna+1}): pusiste {usuario}, debería ser {sudoku_completo}")
    else:
        if vacias > 0:
            print(f"No hay errores, pero quedan {vacias} celdas vacías.")
        else:
            print("Sudoku correcto (sin errores).")

    # Redibujar el fondo / grilla / tablero y el puntaje
    pantalla.blit(fondo, (0, 0))
    dibujar_grilla(pantalla)
    llenar_tablero(tab_usuario, pantalla)
    mostrar_puntaje()




def reiniciar_tablero():
    global tab_usuario, cuadrado_seleccionado, puntaje, regiones_completas, juego_terminado
    # Reset lógico: volver a los valores iniciales del tablero
    tab_usuario = [fila[:] for fila in dificil]
    cuadrado_seleccionado = None

    puntaje = 0
    regiones_completas = set()
    juego_terminado = False

    # Reset visual
    pantalla.blit(fondo, (0, 0))
    dibujar_grilla(pantalla)
    llenar_tablero(tab_usuario, pantalla)
    mostrar_puntaje()

    print("Sudoku reiniciado")


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
                numero_ingresado = valores_teclas(pantalla, evento, pos_x, pos_y)
                
                if numero_ingresado in (1,2,3,4,5,6,7,8,9):
                    botones.sonido_numero_ingresado()
                    fila, columna = pos_a_indices(pos_x, pos_y, columnas_rangos, filas_rangos)
                    tab_usuario[fila][columna] = numero_ingresado
                    
                llenar_tablero(tab_usuario, pantalla)
            except:
                pass
        
    mostrar_puntaje()   
    pg.display.flip()



"""
if evento.type == pg.QUIT:
            pg.quit()
            exit()
        elif evento.type == pg.MOUSEBUTTONDOWN:
            cuadrado_seleccionado = celda_seleccionada(evento, columnas_rangos, filas_rangos, pantalla)
        
        if evento.type == pg.KEYDOWN: 
            try:
                pos_x, pos_y = cuadrado_seleccionado
                valores_teclas(pantalla, evento, pos_x, pos_y)
            except:
                pass
"""