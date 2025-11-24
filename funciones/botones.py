import pygame as pg
from funciones.configuracion import reproducir_musica_loop
pg.init()

bandera = True

GRIS = (200, 200, 200)
GRIS_OSCURO = (100, 100, 100) 
NEGRO = (0, 0, 0)

_estados_click = {}
_estados_hover = {}

def reproducir_sonido(ruta_sonido, volumen):
    """
    Función para reproducir un sonido una sola vez
    """
    try:
        sonido = pg.mixer.Sound(ruta_sonido)
        sonido.set_volume(volumen)  
        sonido.play(0)
        pg.mixer.music.play(loops=1)
        return True
    except:
        return False   


def sonido_numero_ingresado():
    reproducir_sonido("./sonidos/numero_ingresado.mp3", 0.2)


def sonido_celda_seleccionada():
    reproducir_sonido("./sonidos/celda_marcada.mp3", 0.2)

def sonido_error():
    reproducir_sonido("./sonidos/error.mp3", 0.3)


def sonido_acierto():
    reproducir_sonido("./sonidos/acierto.mp3", 0.3)




def crear_boton(pantalla, x, y, ancho, alto, texto, accion=None):
    mouse = pg.mouse.get_pos()
    click_izquierdo = pg.mouse.get_pressed()[0]

    boton_rect = pg.Rect(x, y, ancho, alto)
    hover = boton_rect.collidepoint(mouse)

    # Estados anteriores (por texto de botón)
    click_anterior = _estados_click.get(texto, False)
    hover_anterior = _estados_hover.get(texto, False)

    if hover and not hover_anterior:
        reproducir_sonido("./sonidos/pop.mp3", 0.3)

    # ----- DIBUJO DEL BOTÓN -----
    if hover:
        # Si está apretado, se ve más oscuro
        color_boton = GRIS_OSCURO if click_izquierdo else (250, 100, 0)
    else:
        color_boton = GRIS

    pg.draw.rect(pantalla, color_boton, boton_rect)

    # ----- CLICK: ACCIÓN SOLO EN EL CAMBIO 0 -> 1 -----
    es_nuevo_click = hover and click_izquierdo and not click_anterior

    if es_nuevo_click and accion is not None:
        reproducir_sonido("./sonidos/numero_ingresado.mp3", 0.3)
        accion()

    # Actualizar estados
    _estados_click[texto] = click_izquierdo
    _estados_hover[texto] = hover

    pg.draw.rect(pantalla, NEGRO, boton_rect, 2)
    fuente = pg.font.Font(None, 36)
    texto_render = fuente.render(texto, True, NEGRO)
    texto_objeto = texto_render.get_rect(center=boton_rect.center)
    pantalla.blit(texto_render, texto_objeto)
    