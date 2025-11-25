import pygame as pg

def crear_barra_texto(x, y, ancho=300, alto=40):
    """Crea una barra de texto mínima"""
    return {
        'rect': pg.Rect(x, y, ancho, alto),
        'rect_boton': pg.Rect(x + ancho + 10, y, 80, alto),
        'texto': '',
        'activo': False,
        'texto_ingresado': None
    }

def dibujar_barra(barra, pantalla):
    """Dibuja la barra de texto"""
    # Barra principal
    pg.draw.rect(pantalla, (255, 255, 255), barra['rect'])
    pg.draw.rect(pantalla, (0, 0, 0), barra['rect'], 2)
    
    # Botón
    color_boton = "orange" if not barra['activo'] else (80, 180, 80)
    pg.draw.rect(pantalla, color_boton, barra['rect_boton'])
    pg.draw.rect(pantalla, (50, 50, 50), barra['rect_boton'], 2)
    
    # Textos
    fuente = pg.font.Font(None, 24)
    
    # Texto botón
    texto_boton = fuente.render("Aceptar", True, (255, 255, 255))
    pantalla.blit(texto_boton, (barra['rect_boton'].x + 10, barra['rect_boton'].y + 10))
    
    # Texto barra
    texto_mostrar = barra['texto'] or "INGRESE SU USUARIO"
    color_texto = (0, 0, 0) if barra['texto'] else (150, 150, 150)
    texto_surface = fuente.render(texto_mostrar[-20:], True, color_texto)

    pantalla.blit(texto_surface, (barra['rect'].x + 50, barra['rect'].y + 10)) #

def manejar_barra(barra, evento):
    """Maneja eventos de la barra"""

    #selecciona para poder empezar a escribir en la barra de texto

    if evento.type == pg.MOUSEBUTTONDOWN:
        barra['activo'] = barra['rect'].collidepoint(evento.pos)
        if barra['rect_boton'].collidepoint(evento.pos):
            barra['texto_ingresado'] = barra['texto']
            return True
        return False
    
    # borra o guarda texto de la barra de texto

    if evento.type == pg.KEYDOWN and barra['activo']:
        if evento.key == pg.K_RETURN:
            barra['texto_ingresado'] = barra['texto']
            return True
        elif evento.key == pg.K_BACKSPACE:
            barra['texto'] = barra['texto'][:-1]
        else:
            barra['texto'] += evento.unicode
    
    return False

def obtener_texto(barra) -> str:
    """Obtiene el texto ingresado"""
    texto = barra['texto_ingresado']
    barra['texto_ingresado'] = None
    return texto
