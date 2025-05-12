"""
Nombre:
Fecha: 12 de mayo del 2025.

Descripción:
"""

import pygame
from Configurations import Configurations

def game_events() -> bool:
    """
    Función que administra fps eventos del juego
    :return: La bandera del fin del juego
    """

    #Se declara la bandera del fin del juego
    game_over = False

    #Se verifican los eventos de
    for event in pygame.event.get():
        #Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

    #Se regresa la bandera
    return game_over

def screen_refresh(screen: pygame.surface.Surface) -> None:
    """
    Función que administrar los elementos visuales del juego
    """
    #Fondo de la pantaña
    screen.fill(Configurations.get_background())

    pygame.display.flip()
