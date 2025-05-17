"""
Nombre: Equipo los Bugs
Fecha: 14 de mayo del 2025.

Descripción:
Se agregaron marcas X y O con imágenes al juego.
Se creó clase TicTacToeMark que muestra la imagen correspondiente según el turno del jugador.
El juego responde a teclas q,w,e,a,s,d,z,x y c para colocar marcas en las 9 casillas.
Aún falta implementar la lógica completa del juego que impida colocar marcas sobre otras ya existentes.
"""

import pygame
from Configurations import Configurations
from Media import Background
from TikTacToe import TicTacToeMark


def game_event(marks) -> bool:
    """
    Función que administra los eventos del juego
    return: La bandera del fin del juego (True si se cierra la ventana)
    """

    game_over = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        #Si el usuario presiona una tecla
        elif event.type == pygame.KEYDOWN:
            #Verificamos si la tecla corresponde a una celda válida del tablero
            if event.key in Configurations.get_teclas():
                #Creamos una nueva marca en la celda correspondiente según la tecla presionada
                nueva_marca = TicTacToeMark(Configurations.get_teclas()[event.key])
                marks.add(nueva_marca)  #Agregamos la nueva marca al grupo de marcas

    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background, marks) -> None:
    """
    Función que administra los elementos visuales del juego
    """

    background.blit(screen)

    #Dibujamos todas las marcas actuales en sus posiciones correspondientes
    marks.draw(screen)

    #Actualizamos la pantalla para mostrar todos los cambios gráficos
    pygame.display.flip()

    clock.tick(Configurations.get_fps())
