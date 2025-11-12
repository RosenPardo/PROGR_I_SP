import pygame as pg
from funciones.configuracion import *
from funciones.sudoku import *
import funciones.botones as botones
import funciones.numeros as numeros

pantalla = iniciar_juego()

pantalla.blit(fondo, (0, 0))
dibujar_grilla(pantalla)

tab_usuario = [fila[:] for fila in tab_incompleto]

def pos_a_indices(pos_x, pos_y):
    # Buscar por igualdad exacta del inicio de celda
    col = None
    for i in range(len(columnas_rangos)):
        sx, ex = columnas_rangos[i]
        if sx == pos_x:
            col = i
            break

    fila = None
    for j in range(len(filas_rangos)):
        sy, ey = filas_rangos[j]
        if sy == pos_y:
            fila = j
            break

    return fila, col


def verificar_tablero():
    # Compara tab_usuario contra la solución tab_completo
    errores = []
    vacias = 0
    for f in range(9):
        for c in range(9):
            u = tab_usuario[f][c]
            s = tab_completo[f][c]
            if u == 0:
                vacias += 1
            elif u != s:
                errores.append((f, c, u, s))

    if not errores and vacias == 0:
        print("Sudoku correcto: todo coincide.")
        return

    if errores:
        print(f"Encontré {len(errores)} error(es):")
        for f, c, u, s in errores:
            # donde está el error
            print(f"  - Celda (fila {f+1}, col {c+1}): pusiste {u}, debería ser {s}")


while True:
    botones.crear_boton(pantalla, 703, 53, 240, 52, "Verificar", verificar_tablero)
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