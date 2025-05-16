import pygame
from Configurations import Configurations
from pygame.sprite import Sprite


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

class Turn_Image(Sprite):

    configurations = Configurations()
    turno = "X"

    def __init__(self):
        turno = "X"
        super().__init__()
        if Turn_Image.turno == "X":
            self.image = pygame.image.load(Configurations.get_image_turno_x())
            Turn_Image.turno = "O"
        else:
            self.image = pygame.image.load(Configurations.get_image_turno_o())
            Turn_Image.turno = "X"

        self.image = pygame.transform.scale(self.image, (500, 200)
                                            )
        self.rect = self.image.get_rect()
        self.rect.centerx = 650
        self.rect.bottom = 250







