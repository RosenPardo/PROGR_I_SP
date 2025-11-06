import random, pygame as pg
from funciones.configuracion import *
from funciones.sudoku import *


numero_aleatorio = random.randint(1, 9)
print(numero_aleatorio)

pantalla = iniciar_juego()
fuente = pg.font.SysFont(None, 80)

dibujar_grilla(pantalla)



while True:

    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            exit()
        elif evento.type == pg.MOUSEBUTTONDOWN:
            x, y = evento.pos
            if x >= 52 and x <= 122:  # Verifica si la coordenada X está dentro del rango
                if y >= 52 and y <= 122:  # Verifica si la coordenada Y está dentro del rango
                    print(evento.pos) # Imprime si se hace clic dentro del cuadrado blanco A1

    pg.display.flip()



#Fuentes de windows: %USERPROFILE%\AppData\Local\Microsoft\Windows\Fonts
