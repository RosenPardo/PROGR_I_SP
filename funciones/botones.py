import pygame as pg

pg.init()



GRIS = (200, 200, 200)
GRIS_OSCURO = (100, 100, 100) 
NEGRO = (0, 0, 0)

def reproducir_sonido(ruta_sonido, volumen):
    """
    Función para reproducir un sonido una sola vez
    """
    try:
        sonido = pg.mixer.Sound(ruta_sonido)
        sonido.set_volume(volumen)  
        sonido.play(0)
       
        return True
    except:
        return False   


def sonido_opcion_seleccionada():
    reproducir_sonido("./sonidos/boton_seleccionado.mp3", 0.2)




    


    



def crear_boton(pantalla, x, y, ancho, alto, texto, accion=None):
    
    mouse = pg.mouse.get_pos()
    clic = pg.mouse.get_pressed()
    
    boton_rect = pg.Rect(x, y, ancho, alto)
    
    

    if boton_rect.collidepoint(mouse):
        
        


        pg.draw.rect(pantalla, (250,100,0), boton_rect)
       
       
    else:
        
        pg.draw.rect(pantalla, GRIS, boton_rect)
    
    # Dibujar borde y texto
    pg.draw.rect(pantalla, NEGRO, boton_rect, 2) #color bordes
    fuente = pg.font.Font(None, 36)
    texto_render = fuente.render(texto, True, NEGRO) # color letras
    texto_objeto = texto_render.get_rect(center=boton_rect.center)
    pantalla.blit(texto_render, texto_objeto)






    