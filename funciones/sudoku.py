import random

def generar_tablero_completo():
    """
    Crea un tablero vacío (lleno de ceros) y utiliza la función resolver para
    rellenarlo siguiendo las reglas del Sudoku.

    Returns:
        list[list[int]]: Matriz 9x9 con un Sudoku completo y válido (sin ceros).
    """
    tablero = [[0 for _ in range(9)] for _ in range(9)]
    resolver(tablero)
    return tablero


def crear_sudoku_incompleto_por_bloque(tablero_completo, visibles_por_bloque=5):
    """
    Crea un Sudoku incompleto a partir de un tablero completo, ocultando valores por bloque.

    En cada bloque 3x3 se eligen al azar una cierta cantidad de casilleros que quedarán visibles,
    y el resto se reemplaza por 0 para que el jugador los complete.

    Args:
        tablero_completo (list[list[int]]): Matriz 9x9 con un Sudoku completo y válido.
        visibles_por_bloque (int, opcional): Cantidad de casilleros visibles por cada bloque 3x3. Por defecto es 5.

    Returns:
        list[list[int]]: Matriz 9x9 con el Sudoku incompleto (contiene ceros en los casilleros ocultos).
    """
    tablero = [fila[:] for fila in tablero_completo]

    for start_fila in (0, 3, 6):
        for start_columna in (0, 3, 6):
            posiciones = [
                (start_fila + df, start_columna + dc)
                for df in range(3)
                for dc in range(3)
            ]

            visibles = set(random.sample(posiciones, visibles_por_bloque))

            for f, c in posiciones:
                if (f, c) not in visibles:
                    tablero[f][c] = 0

    return tablero


def es_valido(tablero, fila, columna, numero):
    """
    Verifica si un número se puede colocar en una posición del tablero respetando las reglas del Sudoku.

    Args:
        tablero (list[list[int]]): Matriz 9x9 que representa el tablero de Sudoku.
        fila (int): Índice de la fila donde se quiere colocar el número (0 a 8).
        columna (int): Índice de la columna donde se quiere colocar el número (0 a 8).
        numero (int): Número a colocar (1 a 9).

    Returns:
        bool: True si el número se puede colocar en esa posición sin romper las reglas, False en caso contrario.
    """
    # Chequear fila
    if numero in tablero[fila]:
        return False

    # Chequear columna
    for i in range(9):
        if tablero[i][columna] == numero:
            return False

    # Chequear subcuadrante 3x3
    start_fila = 3 * (fila // 3)
    start_columna = 3 * (columna // 3)

    for i in range(start_fila, start_fila + 3):
        for j in range(start_columna, start_columna + 3):
            if tablero[i][j] == numero:
                return False

    return True


def resolver(tablero):
    """
    Recorre el tablero buscando casilleros vacíos (0) e intenta rellenarlos con números
    del 1 al 9 de forma aleatoria, validando cada intento con la función es_valido.

    Args:
        tablero (list[list[int]]): Matriz 9x9 que representa el tablero de Sudoku a resolver. Se modifica en el lugar.

    Returns:
        bool: True si el tablero se pudo resolver completamente, False si no existe solución válida.
    """
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



def imprimir_tablero(tablero):
    """
    Imprime el tablero de Sudoku en consola con separadores entre filas y columnas.

    Args:
        tablero (list[list[int]]): Matriz 9x9 que representa el tablero de Sudoku a imprimir.

    Returns:
        None
    """
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
