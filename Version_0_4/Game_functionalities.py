"""
Nombre:
Fecha: 12 de mayo del 2025.

Descripción:
"""

import pygame
from Configurations import Configurations
from Media import Background
from TikTacToe import TicTacToeMark

def game_event(marks) -> bool:
    """
    Función que administra ñps eneventos del juego
    retrun: La bandera del fin del juego
    """

    #Se declara la bandera del fin del juego
    game_over = False

    #Se verifican los eventos de
    for event in pygame.event.get():
        #Un clic en cerrar el juego
        if event.type == pygame.QUIT:
            game_over = True

        elif event.type == pygame.KEYDOWN:
            if event.key in Configurations.get_teclas():
                nueva_marca = TicTacToeMark(Configurations.get_teclas()[event.key])
                marks.add(nueva_marca)
    return game_over

def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background,marks) -> None:
    """
    Función que administrar los elementos visuales del juego
    """
    #Fondo de la pantaña
    background.blit(screen)

    # Se dibuja ya sea X o O
    marks.draw(screen)

    pygame.display.flip()

    # Se controla la velocidad de FPS
    clock.tick(Configurations.get_fps())