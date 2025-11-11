import pygame as pg
from funciones.configuracion import *
from funciones.sudoku import *
import funciones.botones as botones
import funciones.numeros as numeros

pantalla = iniciar_juego()

pantalla.blit(fondo, (0, 0))
dibujar_grilla(pantalla)


while True:
    botones.crear_boton(pantalla, 703, 53, 240, 52, "Verificar", None)
    botones.crear_boton(pantalla, 703, 115, 240, 52, "Reiniciar", None)
    botones.crear_boton(pantalla, 703, 177, 240, 52, "Volver", None)

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            exit()
        elif evento.type == pg.MOUSEBUTTONDOWN:
            cuadrado_seleccionado = celda_seleccionada(evento, columnas_rangos, filas_rangos, pantalla)
            print(evento.pos)

        if evento.type == pg.KEYDOWN: 
            if evento.key == pg.K_1:
                pos_x, pos_y = cuadrado_seleccionado
                pantalla.blit(numeros.numero_1, (pos_x , pos_y ))
            elif evento.key == pg.K_2:
                pos_x, pos_y = cuadrado_seleccionado
                pantalla.blit(numeros.numero_2, (pos_x , pos_y ))
            elif evento.key == pg.K_3:
                pos_x, pos_y = cuadrado_seleccionado
                pantalla.blit(numeros.numero_3, (pos_x , pos_y ))
            elif evento.key == pg.K_4:
                pos_x, pos_y = cuadrado_seleccionado
                pantalla.blit(numeros.numero_4, (pos_x , pos_y ))
            elif evento.key == pg.K_5:
                pos_x, pos_y = cuadrado_seleccionado
                pantalla.blit(numeros.numero_5, (pos_x , pos_y ))
            elif evento.key == pg.K_6: 
                pos_x, pos_y = cuadrado_seleccionado
                pantalla.blit(numeros.numero_6, (pos_x , pos_y ))      
            elif evento.key == pg.K_7:
                pos_x, pos_y = cuadrado_seleccionado
                pantalla.blit(numeros.numero_7, (pos_x , pos_y ))
            elif evento.key == pg.K_8:
                pos_x, pos_y = cuadrado_seleccionado
                pantalla.blit(numeros.numero_8, (pos_x , pos_y ))  
            elif evento.key == pg.K_9:
                pos_x, pos_y = cuadrado_seleccionado
                pantalla.blit(numeros.numero_9, (pos_x , pos_y )) 
        
        
    
        
    pg.display.flip()

"""

for evento in pg.event.get():
    if evento.type == pg.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = evento.pos
        celda_encontrada = False
        
        # Revisamos cada columna



Fuentes de windows: %USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts
            if x >= 52 and x <= 122:  # Verifica si la coordenada X está dentro del rango
                if y >= 52 and y <= 122:  # Verifica si la coordenada Y está dentro del rango
                    rectangulo(pantalla, (255, 203, 99), 52, 52, 70, 70)
                    print(evento.pos) # Imprime si se hace clic dentro del cuadrado blanco A1
            else:
                dibujar_grilla(pantalla)
"""