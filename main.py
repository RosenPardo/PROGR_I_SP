import pygame as pg
from funciones.configuracion import *


pantalla = iniciar_juego()

dibujar_grilla(pantalla)

while True:

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            exit()

    pg.display.flip()



#comentario de prueba para git


# asdsad