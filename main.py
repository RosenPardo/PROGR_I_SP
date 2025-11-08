import random, pygame as pg
from funciones.configuracion import *
from funciones.sudoku import *


numero_aleatorio = random.randint(1, 9)
print(numero_aleatorio)

pantalla = iniciar_juego()
fuente = pg.font.SysFont(None, 80)


dibujar_grilla(pantalla)

columnas_rangos = [
    (52, 122),    
    (124, 194),   
    (196, 266),   
    (268, 338),   
    (340, 410),   
    (412, 482),   
    (484, 554),   
    (556, 626),   
    (628, 698)    
]

filas_rangos = [
    (52, 122),    
    (124, 194),   
    (196, 266),   
    (268, 338),   
    (340, 410),   
    (412, 482),   
    (484, 554),   
    (556, 626),   
    (628, 698)    
]

columnas = [52, 122]

while True:

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            exit()
        elif evento.type == pg.MOUSEBUTTONDOWN:
            x, y = evento.pos
            for col in range(9):
                inicio_x, fin_x = columnas_rangos[col]
                if inicio_x <= x <= fin_x:
                    for fila in range(9):
                        inicio_y, fin_y = filas_rangos[fila]
                        if inicio_y <= y <= fin_y:
                            dibujar_grilla(pantalla)
                            rectangulo(pantalla, (255, 203, 99), inicio_x, inicio_y, 70, 70)


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