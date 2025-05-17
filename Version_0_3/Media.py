"""
Nombre: Equipo los Bugs
Fecha: 13 de mayo del 2025.

Descripción:
Se incorporó el control de fps usando un objeto clock de pygame.time.Clock, y se actualizó
la función screen_refresh() para recibirlo. También se agregó un fondo de pantalla: se creó el
directorio media, se añadió la imagen background_image.jpg, y se creó la clase Background en el
nuevo módulo Media.py. La función screen_refresh() ahora también recibe el objeto background y
muestra la imagen en pantalla. Además, se actualizaron las configuraciones en la clase Configurations.
"""

import pygame
from Configurations import Configurations


class Background:
    """
    Clase que contiene el fondo de pantalla.
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path()  # Obtenemos la ruta de la imagen de fondo.
        self.image = pygame.image.load(background_image_path)

        # Escalamos la imagen para que coincida con el tamaño de la pantalla.
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla.
        """
        screen.blit(self.image, self.rect)  # Dibujamos la imagen del fondo en la superficie de la pantalla.
