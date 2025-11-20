import pygame as pg
import sys

# funcion para probar
def mutear():
    global volumen_musica
    volumen_musica = 0.0
    pg.mixer.music.set_volume(volumen_musica)  


def desmutear():
    global volumen_musica
    volumen_musica = 0.5
    pg.mixer.music.set_volume(volumen_musica)  


dificultad = None














def reproducir_musica_loop(ruta_mp3,volumen):
    """
    Función para reproducir MP3 en loop infinito
    """
    try:
        pg.mixer.init()
        pg.mixer.music.load(ruta_mp3)
        pg.mixer.music.set_volume(volumen)  
        pg.mixer.music.play(-1)
        return True
    except:
        return False



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
    reproducir_sonido("./sonidos/numero_ingresado.mp3", 0.2)


    










# Inicializar pygame
pg.init()

# Configuración de la pantalla
ANCHO, ALTO = 1002, 750
pantalla = pg.display.set_mode((ANCHO, ALTO))
pg.display.set_caption("Menú de Opciones")

# Colores
FONDO = (30, 30, 50)
COLOR_BARRA_LATERAL = (40, 40, 60)
COLOR_BOTON = ("oranje")
COLOR_BOTON_HOVER = (100, 160, 210)
COLOR_TEXTO_BOTON = (255, 255, 255)
COLOR_TITULO = (220, 220, 220)

#cargo imagen de fondo del menu principal
imagen_fondo_menu1 = pg.image.load("./img/fondo_menu.png")  
imagen_fondo_menu = pg.transform.scale(imagen_fondo_menu1, (1002, 750))
# Fuentes
fuente_titulo = pg.font.SysFont("Arial", 32, bold=True)
fuente_boton = pg.font.SysFont("Arial", 24)

# Configuración del menú lateral
#ANCHO_BARRA_LATERAL = 250
#POS_X_BARRA = ANCHO - ANCHO_BARRA_LATERAL

# Opciones del menú
opciones_menu = [
    "FACIL",
    "MEDIO",
    "DIFICIL","mutear","desmutear","salir"
]

# Función para dibujar botones
def dibujar_boton(texto, x, y, ancho, alto, hover=False):
    color = COLOR_BOTON_HOVER if hover else COLOR_BOTON
    #pygame.draw.rect(pantalla, color, (x, y, ancho, alto), border_radius=8)
    pg.draw.rect(pantalla, (50, 50, 70), (x, y, ancho, alto), 2, border_radius=7)
    
    superficie_texto = fuente_boton.render(texto, True, COLOR_TEXTO_BOTON)
    rectangulo_texto = superficie_texto.get_rect(center=(x + ancho/2, y + alto/2))
    pantalla.blit(superficie_texto, rectangulo_texto)

# Función principal
def main():

    reproducir_musica_loop("./sonidos/musica_fondo.mp3", 0.5)
    reloj = pg.time.Clock()
    
    # Área de contenido principal
    
    #area_contenido = pygame.Rect(0, 0, ANCHO - ANCHO_BARRA_LATERAL, ALTO)

                                    #aca se modifican los botones
    # Botones del menú
    alto_boton = 70
    ancho_boton = 350
    pos_x_boton = 590
    espacio_botones = 30
    
    alto_total_botones = len(opciones_menu) * (alto_boton + espacio_botones) - espacio_botones
    
    inicio_y = (ALTO - alto_total_botones) // 2
    
    # Estado del menú
    opcion_seleccionada = 0

    




    
    ejecutando = True
    while ejecutando:
        posicion_raton = pg.mouse.get_pos()
        
        # Detectar eventos
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                ejecutando = False
            
            if evento.type == pg.MOUSEBUTTONDOWN:

                reproducir_sonido("./sonidos/numero_ingresado.mp3", 0.2)

                # Verificar clic en botones
                for indice, opcion in enumerate(opciones_menu):
                    rectangulo_boton = pg.Rect(pos_x_boton, inicio_y + indice*(alto_boton + espacio_botones), 
                                                 ancho_boton, alto_boton)
                    if rectangulo_boton.collidepoint(posicion_raton):
                        opcion_seleccionada = indice

                        seleccion = opcion
    
                        match opcion:
                            case "FACIL":
                                dificultad = "FACIL"
                            case "MEDIO":
                                dificultad = "MEDIO"
                            case "DIFICIL":
                                dificultad = "DIFICIL"
                            case _:
                                dificultad = None
                        print(f"Opción seleccionada: {opcion}")
                        
                        #selecciona dificultad
                        print(f"Opción DE DIFICULTAD: {type(dificultad)}")
                        
                        # Acción para la opción Salir
                        if opcion == "Salir":
                            ejecutando = False
        
        # Dibujar fondo
        pantalla.blit(imagen_fondo_menu, (0, 0))
        
        # Dibujar área de contenido principal
        #pygame.draw.rect(pantalla, (20, 20, 30), area_contenido)
        
        # Dibujar título en el área principal
        #texto_titulo = fuente_titulo.render("MENU PRINCIPAL", True, "orange")
        #pantalla.blit(texto_titulo, (500, 50))
        
        # Dibujar información de la opción seleccionada
        


                        # opcion seleccionada


        #texto_info = fuente_boton.render(f"Opción actual: {opciones_menu[opcion_seleccionada]}", True, COLOR_TITULO)
        
        
        #pantalla.blit(texto_info, (500, 150))
        
        # Dibujar barra lateral
        #pygame.draw.rect(pantalla, COLOR_BARRA_LATERAL, (POS_X_BARRA, 0, ANCHO_BARRA_LATERAL, ALTO))
        
        # Dibujar título del menú
        titulo_menu = fuente_titulo.render("MENU PRINCIPAL", True, COLOR_TITULO)


        #IMPRIME TITULO MENU

        pantalla.blit(titulo_menu, (630, 120))
        
        # Dibujar botones
        for indice, opcion in enumerate(opciones_menu):
            pos_y_boton = inicio_y + indice*(alto_boton + espacio_botones)
            rectangulo_boton = pg.Rect(pos_x_boton, pos_y_boton, ancho_boton, alto_boton)
            
            # Verificar si el ratón está sobre el botón
            hover = rectangulo_boton.collidepoint(posicion_raton)
            
            # Resaltar la opción seleccionada
            if indice == opcion_seleccionada:
                pg.draw.rect(pantalla, (90, 150, 200, 100), 
                                (pos_x_boton - 5, pos_y_boton - 5, ancho_boton + 10, alto_boton + 10), 
                                border_radius=10)
            
            dibujar_boton(opcion, pos_x_boton, pos_y_boton, ancho_boton, alto_boton, hover)
        
        # Actualizar pantalla
        pg.display.flip()
        reloj.tick(60)

    pg.quit()
    sys.exit()


main()