import pygame
from  Configurations import Configurations
from pygame.sprite import Sprite

class TicTacToeMark(Sprite):
    configurations = Configurations()
    turno = "O"

    def __init__(self, casilla):
        super().__init__()
        if TicTacToeMark.turno == "X":
            self.image = pygame.image.load(Configurations.get_mark_X())
            TicTacToeMark.turno = "O"
        else:
            self.image = pygame.image.load(Configurations.get_mark_O())
            TicTacToeMark.turno = "X"


        self.image = pygame.transform.scale(self.image, Configurations.get_size_block())

        self.rect = self.image.get_rect()
        self.rect.center = TicTacToeMark.configurations.get_posiciones().get(casilla, (0, 0))
