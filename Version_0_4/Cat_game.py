"""
Nombre:
Fecha: 12 de mayo del 2025.

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
    #Se inicializa el módulo pygame
    pygame.init()

    clock = pygame.time.Clock()

    #Se inicializa la pantalla
    #screen_size = (1280, 720) #Resolución de la pantalla (ancho, alto)
    screen = pygame.display.set_mode(Configurations.get_screen_size() )

    #Se configura el título del juego
    #game_title = "Snake game en pygame"
    pygame.display.set_caption(Configurations.get_game_title())

    #Ciclo principal de videojuego
    game_over = False
    background = Background()

    marks = pygame.sprite.Group()

    while not game_over:
        game_over = game_event(marks)
        screen_refresh(screen, clock, background, marks)

if __name__ == '__main__':
    run_game()