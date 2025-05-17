"""
Nombre: Equipo los Bugs
Fecha: 13 de mayo del 2025.

Descripción:
Se incorporó el control de fps usando un objeto clock de pygame.time.Clock, y se actualizó
la función screen_refresh() para recibirlo. También se agregó un fondo de pantalla: se creó el
directorio media, se añadió la imagen background_image.jpg, y se creó la clase Background en el
nuevo módulo Media.py. La función screen_refresh() ahora también recibe el objeto background y
muestra la imagen en pantalla. Además, se actualizaron las configuraciones en la clase Configurations.
"""

import pygame
from Configurations import Configurations
from Media import Background


def game_event() -> bool:
    """
    Función que administra los eventos del juego
    return: La bandera del fin del juego
    """

    game_over = False

    #Revisamos todos los eventos generados por el usuario
    for event in pygame.event.get():
        #Si el usuario cierra la ventana, terminamos el juego
        if event.type == pygame.QUIT:
            game_over = True

    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background) -> None:
    """
    Función que administra los elementos visuales del juego
    """
    #Dibujamos la imagen de fondo en la pantalla
    background.blit(screen)

    pygame.display.flip()  #Actualizamos el contenido de la ventana

    clock.tick(Configurations.get_fps())
