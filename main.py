import pygame as pg
from funciones.configuracion import *
from funciones.sudoku import *
import funciones.botones as botones
from funciones.numeros import *
from funciones.teclas import *
import funciones.sudoku as sudoku
from puntajes.puntaje import *
from puntajes.barra_texto import *

pg.init()
#  MÚSICA DE FONDO 
volumen_musica = 0.5
reproducir_musica_loop("./sonidos/musica_fondo.mp3", volumen_musica)

#  ESTADO DE JUEGO 
nombre_usuario = ""
puntaje = 0
regiones_completas = set()
tablero_completo_bonificado = False

pantalla = iniciar_juego()
pantalla.blit(fondo, (0, 0))
dibujar_grilla(pantalla)

# Tableros iniciales
llenar_tablero(tab_incompleto, pantalla)
tab_usuario = [fila[:] for fila in tab_incompleto]

# Para mostrar errores después de verificar
errores_en_tablero = []
mostrar_errores = False

#  MENÚ INICIAL 
fondo_menu_init = pg.image.load("./img/fondo_menu.png")
fondo_menu = pg.transform.scale(fondo_menu_init, (1002, 750))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

fuente_puntaje = pg.font.Font(None, 40)

# Estado general
en_menu = True
en_puntajes = False
running = True

#  FUNCIONES AUXILIARES 
def pos_a_indices(pos_x: int, pos_y: int, columnas_rangos: list, filas_rangos: list) -> tuple:
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
    for i, (sx, ex) in enumerate(columnas_rangos):
        # columnas_rangos[i] es (inicio_x, fin_x)
        if sx == pos_x:
            col = i
            break

    fila = None
    for j, (sy, ey) in enumerate(filas_rangos):
        # filas_rangos[j] es (inicio_y, fin_y)
        if sy == pos_y:
            fila = j
            break

    return fila, col


def mostrar_puntaje() -> None:
    """
    Función que muestra el puntaje en pantalla.
    """
    texto = f"Score: {puntaje:04d}"
    render = fuente_puntaje.render(texto, True, (0, 0, 0))

    rectangulo(pantalla, "orange", 293, 8, 170, 30)
    pantalla.blit(render, (298, 10))

def ver_puntajes() -> list:
    """
    Función que lee el archivo json de mejores puntajes.

    Returns:
        list: Lista de los 5 mejores puntajes obtenidos en el juego.
    """
    
    with open('./puntajes/mejores_puntajes.json', 'r') as archivo_json:
        puntajes = json.load(archivo_json)

    fuente = pg.font.Font(None, 30)
    
    

    for i, puntaje in enumerate(puntajes):
        texto = fuente.render(f"{i+1}°: {puntaje['nombre']} | {puntaje['puntaje']} puntos", True, "white")
        if puntaje["puntaje"] > 0:
            pantalla.blit(texto, (95, 160 + i * 40))  # Espaciado vertical entre elementos


def verificar_tablero() -> None:
    """
    Compara el tablero del usuario (tab_usuario) contra la solución (tab_completo)
    y CALCULA el puntaje DESDE CERO según la consigna:

    -1 punto por cada número mal colocado.
    +9 puntos por cada región 3x3 completamente correcta.
    +81 puntos extra si toda la matriz 9x9 está correcta (sin errores ni celdas vacías).
    """
    global puntaje, regiones_completas, tablero_completo_bonificado
    global errores_en_tablero, mostrar_errores

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

    puntaje -= len(errores)
    puntaje += nuevas_regiones * 9

    if tablero_completo_correcto and not tablero_completo_bonificado:
        puntaje += 81
        tablero_completo_bonificado = True
        nombre = nombre_de_usuario_ingresado
        guardar_puntajes(puntaje, nombre)
        mostrar_mensaje_ganaste_con_boton()

    if len(errores) > 0:
        botones.sonido_error()
    elif tablero_completo_correcto:
        botones.sonido_acierto()

    # Guardamos errores para que el loop principal los dibuje
    errores_en_tablero = errores
    mostrar_errores = True


def reiniciar_tablero() -> None:
    """
    Reinicia el tablero, generando nuevamente el SUDOKU. 
    """
    global tab_usuario, puntaje
    global regiones_completas, tablero_completo_bonificado
    global errores_en_tablero, mostrar_errores
    global tab_incompleto, tab_completo

    # Reset de estado
    regiones_completas = set()
    tablero_completo_bonificado = False
    puntaje = 0
    errores_en_tablero = []
    mostrar_errores = False
    salir_cartel_ganaste = False

    # Generar tablero nuevo
    sudoku.tab_completo = sudoku.generar_tablero_completo()
    sudoku.tab_incompleto = sudoku.crear_sudoku_incompleto_por_bloque(
        sudoku.tab_completo,
        visibles_por_bloque=5
    )

    tab_completo = sudoku.tab_completo
    tab_incompleto = sudoku.tab_incompleto
    tab_usuario = [fila[:] for fila in tab_incompleto]

    # Redibujar base
    pantalla.blit(fondo, (0, 0))
    dibujar_grilla(pantalla)
    llenar_tablero(tab_usuario, pantalla)
    mostrar_puntaje()

def volver_desde_cartel_ganaste() -> None:
    """
    Acción del botón 'Volver' del cartel de victoria.
    Pone en_menu en True y cierra el cartel.
    """
    global salir_cartel_ganaste, en_menu
    salir_cartel_ganaste = True
    en_menu = True


def mostrar_mensaje_ganaste_con_boton() -> None:
    """
    Muestra un cartel de victoria con un botón 'Volver'
    que te lleva al menú principal.
    """
    global puntaje, salir_cartel_ganaste
    salir_cartel_ganaste = False

    boton_volver_menu = botones.Boton(
        1002 // 2 - 100,
        750 // 2 + 80,
        200,
        60,
        "Volver",
        color_base=(200, 200, 200),
        color_hover=(250, 180, 0),
        toggle=False,
        accion=volver_desde_cartel_ganaste,
    )

    # Loop del cartel hasta que se haga click en 'Volver' o se cierre la ventana
    while not salir_cartel_ganaste:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                finalizar()

        overlay = pg.Surface((1002, 750), pg.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        pantalla.blit(overlay, (0, 0))

        # Textos
        fuente_titulo = pg.font.Font(None, 72)
        fuente_texto = pg.font.Font(None, 48)

        texto_titulo = fuente_titulo.render(f"¡Ganaste, {nombre_de_usuario_ingresado}!", True, WHITE)
        texto_puntaje = fuente_texto.render(f"Tu puntaje es de: {puntaje}", True, WHITE)

        rect_titulo = texto_titulo.get_rect(center=(1002 // 2, 750 // 2 - 40))
        rect_puntaje = texto_puntaje.get_rect(center=(1002 // 2, 750 // 2 + 10))

        pantalla.blit(texto_titulo, rect_titulo)
        pantalla.blit(texto_puntaje, rect_puntaje)

        # Botón 'Volver'
        boton_volver_menu.dibujar(pantalla)

        pg.display.flip()
        clock.tick(60)


def mutear() -> None:
    """
    Establece el volumen de la música a cero.
    """
    global volumen_musica
    volumen_musica = 0.0
    pg.mixer.music.set_volume(volumen_musica)


def desmutear() -> None:
    """
    Establece el volumen de la música a 0.5.
    """
    global volumen_musica
    volumen_musica = 0.5
    pg.mixer.music.set_volume(volumen_musica)


def finalizar() -> None:
    """
    Cierra el juego.
    """
    pg.quit()
    exit()


def comenzar_juego() -> None:
    """
    Inicia el menú del juego y llama a la función reiniciar_tablero() para resetear todo.
    """
    global en_menu
    en_menu = False

    # Cada vez que empiezo a jugar, reseteo todo
    reiniciar_tablero()

def puntaje_en_pantalla() -> None:
    """
    Alterna que se muestre el puntaje en el menú. 
    """
    global en_puntajes
    en_puntajes = not en_puntajes 
    
def volver_al_menu() -> None:
    """
    Vuelve a la pantalla de menú, ocultando nuevamente los puntajes. 
    """
    global en_menu, en_puntajes

    # Volver a la pantalla de menú
    en_menu = True
    en_puntajes = False



#  BOTONES 
# Menú
boton_jugar = botones.Boton(
    750, 310, 200, 80,
    "JUGAR",
    color_base=(200, 200, 200),
    color_hover=(250, 100, 0),
    toggle=False,
    accion=comenzar_juego,
)

boton_salir = botones.Boton(
    750, 550, 200, 80,
    "SALIR",
    color_base=(200, 200, 200),
    color_hover=(250, 100, 0),
    toggle=False,
    accion=finalizar,
)

boton_puntajes = botones.Boton(
    750, 400, 200, 80, 
    "VER PUNTAJES",
    color_base=(200, 200, 200),
    color_hover=(250, 100, 0),
    toggle=False,
    accion= puntaje_en_pantalla
)

# Juego
boton_verificar = botones.Boton(
    703, 53, 240, 52,
    "VALIDAR",
    color_base=(200, 200, 200),
    color_hover=(250, 100, 0),
    toggle=False,
    accion=verificar_tablero,
)

boton_reiniciar = botones.Boton(
    703, 115, 240, 52,
    "REINICIAR",
    color_base=(200, 200, 200),
    color_hover=(250, 100, 0),
    toggle=False,
    accion=reiniciar_tablero,
)

boton_mute = botones.Boton(
    680, 700, 120, 50,
    "MUTEAR",
    color_base=(200, 200, 200),
    color_hover=(250, 100, 0),
    toggle=False,
    accion=mutear,
)

boton_desmute = botones.Boton(
    800, 700, 160, 50,
    "DESMUTEAR",
    color_base=(200, 200, 200),
    color_hover=(250, 100, 0),
    toggle=False,
    accion=desmutear,
)

boton_volver = botones.Boton(
    703, 177, 240, 52,
    "VOLVER",
    color_base=(200, 200, 200),
    color_hover=(250, 100, 0),
    toggle=False,
    accion=volver_al_menu,
)


barra = crear_barra_texto(585, 310, 300, 30)
nombre_de_usuario_ingresado = ""


clock = pg.time.Clock()
cuadrado_seleccionado = None

#  LOOP PRINCIPAL 
while running:
    if en_menu:
        #  PANTALLA DE MENÚ 
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                finalizar()
            
            if manejar_barra(barra, evento):
                nombre_de_usuario_ingresado = obtener_texto(barra)
                print(f"Valor de variable nombre_de_usuario_ingresado\n:tipo{type(nombre_de_usuario_ingresado)}\nnick : {nombre_de_usuario_ingresado}")
        
        if en_puntajes:
            pantalla.blit(fondo_menu, (0, 0))
            ver_puntajes()
        
        else:
            pantalla.blit(fondo_menu, (0, 0))
    
        if nombre_de_usuario_ingresado == "":
            dibujar_barra(barra, pantalla) 
        else:
            boton_jugar.dibujar(pantalla)
        
        boton_mute.dibujar(pantalla)
        boton_desmute.dibujar(pantalla)   
        
        
        boton_salir.dibujar(pantalla)
        boton_puntajes.dibujar(pantalla)

        pg.display.flip()
        clock.tick(60)
        continue  # Saltamos a la próxima iteración del loop

    #  PANTALLA DE JUEGO 
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            finalizar()

        elif evento.type == pg.MOUSEBUTTONDOWN:
            cuadrado_seleccionado = celda_seleccionada(evento, columnas_rangos, filas_rangos, pantalla)
            botones.reproducir_sonido("./sonidos/celda_marcada.mp3", 0.4)

        elif evento.type == pg.KEYDOWN:
            # Si todavía no se seleccionó ninguna celda, ignoramos la tecla
            if cuadrado_seleccionado is None:
                continue

            pos_x, pos_y = cuadrado_seleccionado
            fila, columna = pos_a_indices(pos_x, pos_y, columnas_rangos, filas_rangos)

            # Si por algún motivo no encontró fila/columna, nos vamos
            if fila is None or columna is None:
                continue

            # Si es una pista original, no se puede modificar
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


    # DIBUJO PRINCIPAL DEL JUEGO
    pantalla.blit(fondo, (0, 0))
    dibujar_grilla(pantalla)
    llenar_tablero(tab_usuario, pantalla)

    # Resalte de celda seleccionada
    try:
        if cuadrado_seleccionado is not None:
            pos_x, pos_y = cuadrado_seleccionado
            pg.draw.rect(pantalla, COLOR_AMARILLO, (pos_x, pos_y, ancho, alto), 4)
    except Exception:
        pass

    # Dibujar errores si hay
    if mostrar_errores and len(errores_en_tablero) > 0:
        CELL = 72
        OFFSET = 52
        for fila, columna in errores_en_tablero:
            x = OFFSET + columna * CELL
            y = OFFSET + fila * CELL
            pg.draw.rect(pantalla, (255, 0, 0), (x, y, ancho, alto), 4)

    # Botones del juego
    boton_verificar.dibujar(pantalla)
    boton_reiniciar.dibujar(pantalla)
    boton_volver.dibujar(pantalla)  
    boton_mute.dibujar(pantalla)
    boton_desmute.dibujar(pantalla)

    mostrar_puntaje()
    pg.display.flip()
    clock.tick(60)
