import pygame as pg
pg.init()


GRIS = (200, 200, 200)
GRIS_OSCURO = (100, 100, 100) 
NEGRO = (0, 0, 0)



def create_button(surface, x, y, width, height, text, action=None):
    
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    
    button_rect = pg.Rect(x, y, width, height)
    
    # Cambiar color si el mouse está sobre el botón
    if button_rect.collidepoint(mouse):
        pg.draw.rect(surface, GRIS_OSCURO, button_rect)
        if click[0] == 1 and action is not None:
            action()
    else:
        pg.draw.rect(surface, GRIS, button_rect)
    
    # Dibujar borde y texto
    pg.draw.rect(surface, NEGRO, button_rect, 2)
    font = pg.font.Font(None, 36)
    text_surf = font.render(text, True, NEGRO)
    text_rect = text_surf.get_rect(center=button_rect.center)
    surface.blit(text_surf, text_rect)