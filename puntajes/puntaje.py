import json
import pygame as pg

pg.init()

def guardar_puntajes(puntaje: int, nombre: str) -> list:
    """
    Extrae los mejores puntajes del archivo json, y guarda los datos "nombre" y "puntaje", solo si es mayor o igual a los existentes. 

    Args:
        puntaje (int): Puntaje obtenido al finalizar la partida. 
        nombre (str): Nombre del jugador que obtuvo el puntaje.

    Returns:
        list: Lista de los 5 mejores puntajes obtenidos en el juego. 
    """
    with open('./puntajes/mejores_puntajes.json', 'r') as archivo_json:
        puntajes = json.load(archivo_json)

    puntaje_actual = puntaje

    for puntaje in reversed(puntajes):
        if puntaje_actual >= puntaje["puntaje"]:
            puntaje["nombre"] = nombre 
            puntaje["puntaje"] = puntaje_actual
            break


    lista_ordenada = sorted(puntajes, key=lambda item: item["puntaje"], reverse=True) #Ordena los puntajes del archivo json

    #Escritura de archivo json
    with open("./puntajes/mejores_puntajes.json", 'w') as archivo_json:
        json.dump(lista_ordenada, archivo_json, indent = 4)
    

    return lista_ordenada



def nombre_ingresado(evento, pantalla, nombre_usuario):
    BLANCO = (255, 255, 255)
    fuente = pg.font.Font(None, 40)

    if evento.type == pg.KEYDOWN:
        if evento.key == pg.K_BACKSPACE:
            nombre_usuario = nombre_usuario[:-1]
        else:
            if evento.unicode.isalpha() or evento.unicode == ' ':
                nombre_usuario += evento.unicode

    input_surface = fuente.render(nombre_usuario, True, BLANCO)

    pantalla.blit(input_surface, (10,20))

    pg.display.flip()

    return nombre_usuario
