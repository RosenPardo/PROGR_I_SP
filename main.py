import pygame as pg
from funciones.configuracion import *
from funciones.sudoku import *
import funciones.botones as botones
from funciones.numeros import *
from funciones.teclas import *

print(tab_incompleto)
pantalla = iniciar_juego()

pantalla.blit(fondo, (0, 0))
dibujar_grilla(pantalla)
# dificultades pruebas
#llenar_tablero(tab_incompleto,pantalla)
#llenar_tablero(facil,pantalla)
#llenar_tablero(medio,pantalla)
llenar_tablero(dificil, pantalla)


# tab_usuario = [fila[:] for fila in tab_incompleto]
tab_usuario = [fila[:] for fila in dificil]

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
    
    for fila in range(9):
        for columna in range(9):
            usuario = tab_usuario[fila][columna]
            sudoku_completo = tab_completo[fila][columna]
            
            if usuario == 0:
                vacias += 1
            elif usuario != sudoku_completo:
                errores.append((fila, columna, usuario, sudoku_completo))

    if not errores and vacias == 0:
        print("Sudoku correcto: todo coincide.")
        return

    if errores:
        print(f"Encontré {len(errores)} error(es):")
        for fila, columna, usuario, sudoku_completo in errores:
            # donde está el error
            print(f"  - Celda (fila {fila+1}, col {columna+1}): pusiste {usuario}, debería ser {sudoku_completo}")


def reiniciar_tablero():
    global tab_usuario, cuadrado_seleccionado
    # Reset lógico: volver a los valores iniciales del tablero
    tab_usuario = [fila[:] for fila in dificil]
    cuadrado_seleccionado = None

    # Reset visual
    pantalla.blit(fondo, (0, 0))
    dibujar_grilla(pantalla)
    llenar_tablero(dificil, pantalla)

    print("✔️ Sudoku reiniciado")



while True:
    botones.crear_boton(pantalla, 703, 53, 240, 52, "Verificar", verificar_tablero)
    botones.crear_boton(pantalla, 703, 115, 240, 52, "Reiniciar", reiniciar_tablero)
    botones.crear_boton(pantalla, 703, 177, 240, 52, "Volver", None)

    for evento in pg.event.get():
        
        if evento.type == pg.QUIT:
            pg.quit()
            exit()
            
        elif evento.type == pg.MOUSEBUTTONDOWN:
            cuadrado_seleccionado = celda_seleccionada(evento, columnas_rangos, filas_rangos, pantalla)
            llenar_tablero(dificil,pantalla)
            
        if evento.type == pg.KEYDOWN: 
            try:
                pos_x, pos_y = cuadrado_seleccionado
                numero_ingresado = valores_teclas(pantalla, evento, pos_x, pos_y)
                
                if numero_ingresado in (1,2,3,4,5,6,7,8,9):
                    fila, columna = pos_a_indices(pos_x, pos_y)
                    tab_usuario[fila][columna] = numero_ingresado
                    
                llenar_tablero(dificil,pantalla)
            except:
                pass
        
        
    pg.display.flip()



"""
if evento.type == pg.QUIT:
            pg.quit()
            exit()
        elif evento.type == pg.MOUSEBUTTONDOWN:
            cuadrado_seleccionado = celda_seleccionada(evento, columnas_rangos, filas_rangos, pantalla)
        
        if evento.type == pg.KEYDOWN: 
            try:
                pos_x, pos_y = cuadrado_seleccionado
                valores_teclas(pantalla, evento, pos_x, pos_y)
            except:
                pass
"""