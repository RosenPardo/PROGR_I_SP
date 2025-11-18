import pygame as pg
from funciones.configuracion import reproducir_musica_loop
pg.init()


GRIS = (200, 200, 200)
GRIS_OSCURO = (100, 100, 100) 
NEGRO = (0, 0, 0)

def reproducir_sonido(ruta_sonido, volumen):
    """
    Función para reproducir un sonido una sola vez
    """
    try:
        sonido = pg.mixer.Sound(ruta_sonido)
        sonido.set_volume(volumen)  
        sonido.play()
        return True
    except:
        return False   


def sonido_numero_ingresado():
    reproducir_sonido("C:/Users/juanchoneitor/Desktop/proyecto grupal/PROGR_I_SP/sonidos/numero_ingresado.mp3", 0.2)

def sonido_celda_seleccionada():
    reproducir_sonido("C:/Users/juanchoneitor/Desktop/proyecto grupal/PROGR_I_SP/sonidos/celda_marcada.mp3", 0.2)

def sonido_error():
    reproducir_sonido("C:/Users/juanchoneitor/Desktop/proyecto grupal/PROGR_I_SP/sonidos/error.mp3", 0.3)


def sonido_acierto():
    reproducir_sonido("C:/Users/juanchoneitor/Desktop/proyecto grupal/PROGR_I_SP/sonidos/acierto.mp3", 0.3)

    


    



def crear_boton(pantalla, x, y, ancho, alto, texto, accion=None):
    
    mouse = pg.mouse.get_pos()
    clic = pg.mouse.get_pressed()
    
    boton_rect = pg.Rect(x, y, ancho, alto)
    
    if boton_rect.collidepoint(mouse):

        pg.draw.rect(pantalla, GRIS_OSCURO, boton_rect)
        if clic[0] == 1 and accion is not None:
            pg.draw.rect(pantalla, GRIS_OSCURO, boton_rect)
            reproducir_sonido("C:/Users/juanchoneitor/Desktop/proyecto grupal/PROGR_I_SP/sonidos/numero_ingresado.mp3",0.2)
            accion()
    else:
        pg.draw.rect(pantalla, GRIS, boton_rect)
    
    # Dibujar borde y texto
    pg.draw.rect(pantalla, NEGRO, boton_rect, 2)
    fuente = pg.font.Font(None, 36)
    texto_render = fuente.render(texto, True, NEGRO)
    texto_objeto = texto_render.get_rect(center=boton_rect.center)
    pantalla.blit(texto_render, texto_objeto)