"""
Nombre:
Fecha: 13 de mayo del 2025.

Descripción:
"""
import pygame

from Configurations import Configurations
from Game_functionalities import game_event, screen_refresh
from Media import Background


def run_game() -> None:
    """
    Función principal del videojuego
    """
    #Inicializamos pygame antes de usar sus funcionalidades
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(Configurations.get_screen_size())

    pygame.display.set_caption(Configurations.get_game_title())

    game_over = False
    background = Background()

    while not game_over:
        game_over = game_event()  #Verificamos si se debe cerrar el juego
        screen_refresh(screen, clock, background)  #Actualizamos la pantalla en cada iteración


if __name__ == '__main__':
    run_game()
