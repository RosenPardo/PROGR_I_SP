import pygame as pg
pg.init()


GRIS = (200, 200, 200)
GRIS_OSCURO = (100, 100, 100) 
NEGRO = (0, 0, 0)


def crear_boton(pantalla, x, y, ancho, alto, texto, accion=None):
    
    mouse = pg.mouse.get_pos()
    clic = pg.mouse.get_pressed()
    
    boton_rect = pg.Rect(x, y, ancho, alto)
    
    if boton_rect.collidepoint(mouse):
        pg.draw.rect(pantalla, GRIS_OSCURO, boton_rect)
        if clic[0] == 1 and accion is not None:
            accion()
    else:
        pg.draw.rect(pantalla, GRIS, boton_rect)
    
    # Dibujar borde y texto
    pg.draw.rect(pantalla, NEGRO, boton_rect, 2)
    fuente = pg.font.Font(None, 36)
    texto_render = fuente.render(texto, True, NEGRO)
    texto_objeto = texto_render.get_rect(center=boton_rect.center)
    pantalla.blit(texto_render, texto_objeto)