import pygame

def crear_barra_texto(screen, x, y, ancho, alto, color_fondo, color_texto, color_borde, 
                     texto_placeholder="Escribe aquí...", fuente=None, tamano_fuente=24):
    """
    Crea una barra de texto con botón de aceptar reutilizable en Pygame.
    
    Args:
        screen: Superficie de Pygame donde se dibujará
        x, y: Posición de la barra de texto
        ancho, alto: Dimensiones de la barra de texto
        color_fondo: Color de fondo de la barra
        color_texto: Color del texto
        color_borde: Color del borde
        texto_placeholder: Texto placeholder (opcional)
        fuente: Fuente personalizada (opcional)
        tamano_fuente: Tamaño de la fuente (opcional)
    
    Returns:
        dict: Objeto con la barra de texto y métodos para manejarla
    """
    
    # Inicializar fuente si no se proporciona
    if fuente is None:
        fuente = pygame.font.Font(None, tamano_fuente)
    
    # Crear el objeto de la barra de texto
    barra_texto = {
        'rect': pygame.Rect(x, y, ancho, alto),
        'rect_boton': pygame.Rect(x + ancho + 10, y, 80, alto),
        'color_fondo': color_fondo,
        'color_texto': color_texto,
        'color_borde': color_borde,
        'texto': '',
        'activo': False,
        'fuente': fuente,
        'texto_placeholder': texto_placeholder,
        'texto_ingresado': None  # Aquí se guardará el texto cuando se presione aceptar
    }
    
    def dibujar():
        """Dibuja la barra de texto y el botón en la pantalla"""
        # Dibujar barra de texto
        pygame.draw.rect(screen, barra_texto['color_fondo'], barra_texto['rect'])
        pygame.draw.rect(screen, barra_texto['color_borde'], barra_texto['rect'], 2)
        
        # Dibujar botón
        color_boton = (100, 200, 100) if not barra_texto['activo'] else (80, 180, 80)
        pygame.draw.rect(screen, color_boton, barra_texto['rect_boton'])
        pygame.draw.rect(screen, (50, 50, 50), barra_texto['rect_boton'], 2)
        
        # Texto del botón
        texto_boton = barra_texto['fuente'].render("Aceptar", True, (255, 255, 255))
        screen.blit(texto_boton, (barra_texto['rect_boton'].x + 10, 
                                 barra_texto['rect_boton'].y + (alto - texto_boton.get_height()) // 2))
        
        # Texto de la barra
        if barra_texto['texto']:
            texto_surface = barra_texto['fuente'].render(barra_texto['texto'], True, barra_texto['color_texto'])
        else:
            texto_surface = barra_texto['fuente'].render(barra_texto['texto_placeholder'], True, (150, 150, 150))
        
        # Ajustar texto si es muy largo
        if texto_surface.get_width() > barra_texto['rect'].width - 10:
            texto_surface = barra_texto['fuente'].render(barra_texto['texto'][-20:], True, barra_texto['color_texto'])
        
        screen.blit(texto_surface, (barra_texto['rect'].x + 5, barra_texto['rect'].y + (alto - texto_surface.get_height()) // 2))
    
    def manejar_evento(event):
        """Maneja los eventos de la barra de texto"""
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Verificar si se hizo click en la barra de texto
            if barra_texto['rect'].collidepoint(event.pos):
                barra_texto['activo'] = True
            elif barra_texto['rect_boton'].collidepoint(event.pos):
                # Guardar texto cuando se presiona el botón
                barra_texto['texto_ingresado'] = barra_texto['texto']
                barra_texto['activo'] = False
                return True  # Indica que se presionó aceptar
            else:
                barra_texto['activo'] = False
            return False
        
        elif event.type == pygame.KEYDOWN:
            if barra_texto['activo']:
                if event.key == pygame.K_RETURN:
                    # Guardar texto al presionar Enter
                    barra_texto['texto_ingresado'] = barra_texto['texto']
                    barra_texto['activo'] = False
                    return True
                elif event.key == pygame.K_BACKSPACE:
                    barra_texto['texto'] = barra_texto['texto'][:-1]
                else:
                    # Agregar caracteres normales
                    barra_texto['texto'] += event.unicode
        return False
    
    def obtener_texto():
        """Devuelve el texto ingresado y lo resetea"""
        texto = barra_texto['texto_ingresado']
        barra_texto['texto_ingresado'] = None
        return texto
    
    def esta_activa():
        """Verifica si la barra de texto está activa"""
        return barra_texto['activo']
    
    def limpiar_texto():
        """Limpia el texto actual"""
        barra_texto['texto'] = ''
        barra_texto['texto_ingresado'] = None
    
    # Agregar métodos al objeto
    barra_texto['dibujar'] = dibujar
    barra_texto['manejar_evento'] = manejar_evento
    barra_texto['obtener_texto'] = obtener_texto
    barra_texto['esta_activa'] = esta_activa
    barra_texto['limpiar_texto'] = limpiar_texto
    
    return barra_texto

# Ejemplo de uso:
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Barra de Texto Reutilizable")
    clock = pygame.time.Clock()
    
    # Crear barra de texto
    barra = crear_barra_texto(
        screen=screen,
        x=100, y=100,
        ancho=300, alto=40,
        color_fondo=(255, 255, 255),
        color_texto=(0, 0, 0),
        color_borde=(0, 0, 0),
        texto_placeholder="Ingresa tu nombre..."
    )
    
    texto_guardado = None
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Manejar eventos de la barra de texto
            if barra['manejar_evento'](event):
                texto_guardado = barra['obtener_texto']()
                print(f"Texto guardado: {texto_guardado}")
        
        # Dibujar
        screen.fill((240, 240, 240))
        barra['dibujar']()
        
        # Mostrar texto guardado
        if texto_guardado:
            fuente = pygame.font.Font(None, 36)
            texto_surface = fuente.render(f"Texto: {texto_guardado}", True, (0, 0, 0))
            screen.blit(texto_surface, (100, 200))
        
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()