"""
Nombre:
Fecha: 13 de mayo del 2025.

Descripción: version 4
"""
import pygame
from Configurations import Configurations


class Background:
    """
    Clase que contiene el fondo de pantalla
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(background_image_path)

        # Se escala la imagen al tamaño de la pantalla
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla
        """
        screen.blit(self.image, self.rect)

class Mark_X:
    def __init__(self):

        x_imagex_path = Configurations.get_x_images_path()
        self.imagex = pygame.image.load(x_imagex_path)

        self.imagex = pygame.image.load(Configurations.get_x_images_path())
        self.rect = self.imagex.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibuja
        """
        screen.blit(self.imagex, self.rect)

class Mark_O:
    def __init__(self):

        o_image_path = Configurations.get_o_images_path()
        self.image = pygame.image.load(o_image_path)

        self.image = pygame.image.load(Configurations.get_o_images_path())
        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibuja
        """
        screen.blit(self.image, self.rect)