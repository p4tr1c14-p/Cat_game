"""
Nombre:
Fecha: 13 de mayo del 2025.

Descripción: version 4
"""

import pygame
from pygame.sprite import Sprite
from Configurations import Configurations
from Media import Mark_X
from random import randint

class TicTacToeMark(Sprite):
    def __init__(self, is_turno: bool = True):
        """
        Constructor de la clase
        """
        super().__init__()

        if is_turno:
            self.image = pygame.image.load(Configurations.get_o_images_path())

            is_turno = False
        else:
            self.image = pygame.image.load(Configurations.get_x_images_path())
            is_turno = True

        cat_block_size = 50
        self.image = pygame.transform.scale(self.image, (cat_block_size, cat_block_size))

        self.rect = self.image.get_rect()


    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar el bloque de la serpiente
        param screen: Pantalla en dnde se dibuja
        """
        screen.blit(self.image, self.rect)

    def snake_head_init(self) -> None:
        for event in pygame.event.get():
            if event.key == pygame.K_a:
                pass
