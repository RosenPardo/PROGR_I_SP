import pygame as pg
from main import *
pg.init()

if True:
    pantalla.blit(numeros.numero_1, (pos_x , pos_y ))
    f, c = pos_a_indices(pos_x, pos_y)
    tab_usuario[f][c] = 1
elif evento.key == pg.K_2:
    pos_x, pos_y = cuadrado_seleccionado
    pantalla.blit(numeros.numero_2, (pos_x , pos_y ))
    f, c = pos_a_indices(pos_x, pos_y)
    tab_usuario[f][c] = 2
elif evento.key == pg.K_3:
    pos_x, pos_y = cuadrado_seleccionado
    pantalla.blit(numeros.numero_3, (pos_x , pos_y ))
    f, c = pos_a_indices(pos_x, pos_y)
    tab_usuario[f][c] = 3
elif evento.key == pg.K_4:
    pos_x, pos_y = cuadrado_seleccionado
    pantalla.blit(numeros.numero_4, (pos_x , pos_y ))
    f, c = pos_a_indices(pos_x, pos_y)
    tab_usuario[f][c] = 4
elif evento.key == pg.K_5:
    pos_x, pos_y = cuadrado_seleccionado
    pantalla.blit(numeros.numero_5, (pos_x , pos_y ))
    f, c = pos_a_indices(pos_x, pos_y)
    tab_usuario[f][c] = 5
elif evento.key == pg.K_6: 
    pos_x, pos_y = cuadrado_seleccionado
    pantalla.blit(numeros.numero_6, (pos_x , pos_y ))
    f, c = pos_a_indices(pos_x, pos_y)
    tab_usuario[f][c] = 6
elif evento.key == pg.K_7:
    pos_x, pos_y = cuadrado_seleccionado
    pantalla.blit(numeros.numero_7, (pos_x , pos_y ))
    f, c = pos_a_indices(pos_x, pos_y)
    tab_usuario[f][c] = 7
elif evento.key == pg.K_8:
    pos_x, pos_y = cuadrado_seleccionado
    pantalla.blit(numeros.numero_8, (pos_x , pos_y ))  
    f, c = pos_a_indices(pos_x, pos_y)
    tab_usuario[f][c] = 8
elif evento.key == pg.K_9:
    pos_x, pos_y = cuadrado_seleccionado
    pantalla.blit(numeros.numero_9, (pos_x , pos_y )) 
    f, c = pos_a_indices(pos_x, pos_y)
    tab_usuario[f][c] = 9

