"""
Nombre: Galilea Peralta Contreras.
Fecha: 12 de mayo del 2025.

Descripción:
"""

import pygame


def run_game() -> None:
    """
    Función principal.
    """
    #Se inicializa el módulo de pygame.
    pygame.init()

    # Se inicializa la pantalla.
    screen_size =(1288,720) # Resolución de la pantalla (ancho,alto).
    screen = pygame.display.set_mode(screen_size)

    #Se configura el título del juego.
    game_title = "Cat game en pygame"
    pygame.display.set_caption(game_title)

    # Ciclo principal del videojuego.
    game_over = False


    while not game_over:
        # Se verifican los eventos (teclado y ratón) del juego.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        # Se dibujan los elementos gráficos en la pantalla.
        background = (135,206,235) # Fondo de la pantalla en formato RGB.
        screen.fill(background)

        #Se actualiza la pantalla.
        pygame.display.flip()
    pygame.quit()

""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    run_game()