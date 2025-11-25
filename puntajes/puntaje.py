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

def ver_puntajes() -> list:
    """
    Función que lee el archivo json de mejores puntajes.

    Returns:
        list: Lista de los 5 mejores puntajes obtenidos en el juego.
    """
    with open('./puntajes/mejores_puntajes.json', 'r') as archivo_json:
        puntajes = json.load(archivo_json)
    
    return puntajes

def nombre_usuario(evento, pantalla):
    BLANCO = (255, 255, 255)
    font = pg.font.Font(None, 36)
    user_text = ""
    if evento.type == pg.KEYDOWN:
        if evento.key == pg.K_BACKSPACE:
            user_text = user_text[:-1]
        else:
            user_text += evento.unicode

    input_surface = font.render(user_text, True, BLANCO)

    pantalla.blit(input_surface, (10,20))

    pg.display.flip()

    return user_text