"""
Nombre: Equipo los Bugs.
Fecha: 14 de mayo del 2025.

Descripción:
Se agregaron marcas X y O con imágenes al juego.
Se creó clase TicTacToeMark que muestra la imagen correspondiente según el turno del jugador.
El juego responde a teclas q,w,e,a,s,d,z,x y c para colocar marcas en las 9 casillas.
Aún falta implementar la lógica completa del juego que impida colocar marcas sobre otras ya existentes.
"""

import pygame

from Configurations import Configurations
from Game_functionalities import game_event, screen_refresh
from Media import Background

def run_game() -> None:
    """
    Función principal del videojuego.
    """
    pygame.init()

    clock = pygame.time.Clock()

    #Creamos la ventana con el tamaño definido en las configuraciones.
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    pygame.display.set_caption(Configurations.get_game_title())

    game_over = False
    background = Background()

    #Creamos un grupo para contener las marcas.
    marks = pygame.sprite.Group()

    while not game_over:
        #Gestionamos eventos y actualizamos la lógica del juego.
        game_over = game_event(marks)

        #Actualizamos la pantalla con los elementos visuales.
        screen_refresh(screen, clock, background, marks)

if __name__ == '__main__':
    run_game()
