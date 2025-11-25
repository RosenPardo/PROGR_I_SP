import pygame as pg

pg.init()
pg.mixer.init()

#  COLORES

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
GRIS = (200, 200, 200)
GRIS_OSCURO = (100, 100, 100)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

# Fuente general para los botones
font = pg.font.SysFont('Arial', 24)

#  SONIDOS
def reproducir_sonido(ruta_sonido, volumen):
    """
    Función para reproducir un sonido una sola vez
    """
    try:
        sonido = pg.mixer.Sound(ruta_sonido)
        sonido.set_volume(volumen)
        sonido.play()
        return True
    except Exception:
        return False   


def sonido_numero_ingresado():
    reproducir_sonido("./sonidos/numero_ingresado.mp3", 0.2)


def sonido_celda_seleccionada():
    reproducir_sonido("./sonidos/celda_marcada.mp3", 0.2)

def sonido_error():
    reproducir_sonido("./sonidos/error.mp3", 0.3)


def sonido_acierto():
    reproducir_sonido("./sonidos/acierto.mp3", 0.3)


class Boton:
    """
    Botón que:
    - Muestra texto.
    - Cambia de color con hover.
    - Opcional: maneja estado ON/OFF interno.
    - Ejecuta una acción en el click.
    """

    def __init__(
        self,
        x,
        y,
        width,
        height,
        texto,
        color_base=GRIS,
        color_hover=(250, 100, 0),
        toggle=False,
        accion=None,
    ):
        self.rect = pg.Rect(x, y, width, height)
        self.texto = texto
        self.color_base = color_base
        self.color_hover = color_hover
        self.color_actual = color_base

        # Si toggle=True, el botón tendrá self.estado ON/OFF
        self.toggle = toggle
        self.estado = False

        # Acción al hacer click
        self.accion = accion

        # Para detectar flanco de click y sonido de hover
        self._hover_anterior = False
        self._click_anterior = False

    def dibujar(self, superficie):
        mouse_pos = pg.mouse.get_pos()
        click_izquierdo = pg.mouse.get_pressed()[0]

        hover = self.rect.collidepoint(mouse_pos)

        # Sonido al entrar en hover
        if hover and not self._hover_anterior:
            reproducir_sonido("./sonidos/pop.mp3", 0.3)

        # Color del botón
        if hover:
            self.color_actual = GRIS_OSCURO if click_izquierdo else self.color_hover
        else:
            self.color_actual = self.color_base

        # Dibujar rectángulo del botón
        pg.draw.rect(superficie, self.color_actual, self.rect, border_radius=10)
        pg.draw.rect(superficie, NEGRO, self.rect, 2, border_radius=10)

        # Texto del botón
        texto_surface = font.render(self.texto, True, NEGRO)
        texto_rect = texto_surface.get_rect(center=self.rect.center)
        superficie.blit(texto_surface, texto_rect)

        # Si es toggle, dibujar ON/OFF debajo
        if self.toggle:
            estado_texto = "ON" if self.estado else "OFF"
            estado_color = VERDE if self.estado else ROJO
            estado_surface = font.render(estado_texto, True, estado_color)
            estado_rect = estado_surface.get_rect(
                center=(self.rect.centerx, self.rect.centery + 30)
            )
            superficie.blit(estado_surface, estado_rect)

        # Detectar "nuevo click" (flanco de subida)
        es_nuevo_click = hover and click_izquierdo and not self._click_anterior
        if es_nuevo_click:
            # Si es toggle, cambiar estado
            if self.toggle:
                self.estado = not self.estado
                sonido_acierto()  # podés cambiar a otro sonido si querés
            else:
                sonido_numero_ingresado()

            # Ejecutar acción
            if self.accion is not None:
                self.accion()

        # Guardar estados para el próximo frame
        self._hover_anterior = hover
        self._click_anterior = click_izquierdo
