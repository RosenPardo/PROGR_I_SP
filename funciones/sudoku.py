import random

def generar_tablero_completo():
    """Se genera SUDOKU 9x9 validado"""


    tablero = []
    for _ in range(9):
        fila = []
        for _ in range(9):
            fila.append(0)
        tablero.append(fila)
    
    def es_valido(tablero, fila, columna, numero):
            
            if numero in tablero[fila]:
                return False
        
            for i in range(9):
                if tablero[i][columna] == numero:
                    return False
                
            start_fila = 3 * (fila // 3)
            start_columna = 3 * (columna // 3)
            
            for i in range(start_fila, start_fila + 3):
                for j in range(start_columna, start_columna + 3):
                    if tablero[i][j] == numero:
                        return False
            return True
        
    def resolver(tablero):
        for fila in range(9):
            for col in range(9):
                if tablero[fila][col] == 0:
                    numeros = list(range(1, 10))
                    random.shuffle(numeros)
                    for num in numeros:
                        if es_valido(tablero, fila, col, num):
                            tablero[fila][col] = num
                            if resolver(tablero):
                                return True
                            tablero[fila][col] = 0
                    return False
        return True
    
    resolver(tablero)
    return tablero

def crear_sudoku_incompleto_por_bloque(tablero_completo, visibles_por_bloque=5):

    tablero = [fila[:] for fila in tablero_completo]

    for start_fila in (0, 3, 6):
        for start_columna in (0, 3, 6):
            posiciones = [(start_fila + df, start_columna + dc) for df in range(3) for dc in range(3)]

            visibles = set(random.sample(posiciones, visibles_por_bloque))

            for f, c in posiciones:
                if (f, c) not in visibles:
                    tablero[f][c] = 0

    return tablero

def imprimir_tablero(tablero):
    for i, fila in enumerate(tablero):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        fila_str = ""
        for j, valor in enumerate(fila):
            if j % 3 == 0 and j != 0:
                fila_str += "| "
            fila_str += f"{valor if valor != 0 else 0} "
        print(fila_str)
    print()



# Generar un tablero completo y luego uno incompleto para uso externo
tab_completo = generar_tablero_completo()
tab_incompleto = crear_sudoku_incompleto_por_bloque(tab_completo, visibles_por_bloque=5)


# dificultades predefinidas

facil = crear_sudoku_incompleto_por_bloque(tab_completo, visibles_por_bloque=5)

medio = crear_sudoku_incompleto_por_bloque(tab_completo, visibles_por_bloque=4)

dificil = crear_sudoku_incompleto_por_bloque(tab_completo, visibles_por_bloque=3)
    




if __name__ == "__main__":
    completo = generar_tablero_completo()
    incompleto = crear_sudoku_incompleto_por_bloque(completo, visibles_por_bloque=5)

    print("Sudoku completo")
    imprimir_tablero(completo)

    print("Sudoku con vacios")
    imprimir_tablero(incompleto)


