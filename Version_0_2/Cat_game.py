"""
Nombre:
Fecha: 12 de mayo del 2025.

Descripción:
"""
import pygame
from Configurations import Configurations
from Game_functionalities import game_events, screen_refresh

def run_game() -> None:
    """
    Función principal del videojuego
    """
    pygame.init()

    #Creamos la ventana con el tamaño definido en configuraciones
    screen = pygame.display.set_mode(Configurations.get_screen_size())

    pygame.display.set_caption(Configurations.get_game_title())

    game_over = False

    while not game_over:
        game_over = game_events()  #Procesamos eventos y verificamos si hay que cerrar el juego

        screen_refresh(screen)  #Actualizamos la pantalla en cada iteración

    pygame.quit()

if __name__ == '__main__':
    run_game()
