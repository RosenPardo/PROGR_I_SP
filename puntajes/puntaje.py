import json


def guardar_puntajes(puntaje, nombre):
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


