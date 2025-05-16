"""
Nombre:
Fecha: 12 de mayo del 2025.

Descripción: En esta primera versión solo se creó la pantalla de fondo
"""

import pygame

def run_game() -> None:
    """
    Función principal.
    """
    pygame.init()

    #Definimos el tamaño de la pantalla donde se mostrará el juego
    screen_size = (1288, 720)  #Resolución de la pantalla (ancho, alto)
    screen = pygame.display.set_mode(screen_size)

    #Establecemos el título que aparecerá en la ventana del juego
    game_title = "Cat game en pygame"
    pygame.display.set_caption(game_title)

    game_over = False

    #Iniciamos el ciclo principal del juego
    while not game_over:
        #Revisamos todos los eventos que ocurren
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True  #Cambiamos la bandera si se cierra la ventana

        #Dibujamos el fondo de la pantalla con un color azul cielo
        background = (135, 206, 235)
        screen.fill(background)

        #Actualizamos la pantalla con los nuevos elementos gráficos
        pygame.display.flip()

    pygame.quit()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    run_game()
