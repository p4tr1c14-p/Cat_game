"""
Nombre: Equipo los Bugs
Fecha: 16 de mayo del 2025.

Descripción:
Se agregó música de fondo y efectos de sonido al juego mediante la clase Audio.
Las funciones del juego ahora reproducen sonidos según la acción del jugador.
Las configuraciones necesarias se integraron en la clase Configurations.
"""

import pygame
from Configurations import Configurations
from Media import Background, Turn_image
from TikTacToe import TicTacToeMark


def game_event(marks, list_turn, turn, lista_imagen, list_x, list_o, audio) -> bool:
    """
    Administra los eventos del juego, como salir o presionar teclas
    Devuelve True si se debe terminar el juego
    """
    game_over = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

        elif event.type == pygame.KEYDOWN:
            #Verificamos si la tecla es válida y no ha sido usada
            if event.key in Configurations.get_teclas() and Configurations.get_teclas()[event.key] not in list_turn:

                nueva_marca = TicTacToeMark(Configurations.get_teclas()[event.key])  #Generamos la marca en la casilla
                list_turn.append(Configurations.get_teclas()[event.key])  #Registramos la casilla usada
                marks.add(nueva_marca)  #La agregamos al grupo de marcas a dibujar

                turn.remove(lista_imagen[len(list_turn)-1])  #Quitamos la imagen del turno anterior

                nueva_image = Turn_image()  #Generamos la imagen del nuevo turno
                turn.add(nueva_image)  #La añadimos al grupo actual
                lista_imagen.append(nueva_image)  #La guardamos en la lista de turnos

                #Clasificamos la jugada como de X o de O
                for i in range(len(list_turn)):
                    if i % 2 == 0 and list_turn[i] not in list_x:
                        list_x.append(Configurations.get_teclas()[event.key])
                    elif i % 2 != 0 and list_turn[i] not in list_o:
                        list_o.append(Configurations.get_teclas()[event.key])

                audio.play_keyboard_sound()  #Reproducimos sonido de acción

    return game_over


def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background, marks, turn) -> None:
    """
    Dibuja y actualiza todos los elementos visuales del juego en la pantalla
    """
    background.blit(screen)
    marks.draw(screen)
    turn.draw(screen)
    pygame.display.flip()
    clock.tick(Configurations.get_fps())


def check_winner(list_x, list_o) -> tuple[bool, int]:
    """
    Verifica si hay un ganador o si se ha empatado
    Devuelve una tupla con:
    - True/False: si hay fin de juego
    - 0 si gana X, 1 si gana O, 2 si es empate o sigue
    """
    x = False
    y = False

    #Comprobamos filas y columnas
    for i in range(3):
        if (i + (i * 2) + 1) in list_x and (i + (i * 2) + 2) in list_x and (i + (i * 2) + 3) in list_x:
            x = True
            break
        elif i + 1 in list_x and i + 4 in list_x and i + 7 in list_x:
            x = True
            break
    if not x:
        if 1 in list_x and 5 in list_x and 9 in list_x:
            x = True
        elif 3 in list_x and 5 in list_x and 7 in list_x:
            x = True

    for i in range(3):
        if (i + (i * 2) + 1) in list_o and (i + (i * 2) + 2) in list_o and (i + (i * 2) + 3) in list_o:
            y = True
            break
        elif i + 1 in list_o and i + 4 in list_o and i + 7 in list_o:
            y = True
            break
    if not y:
        if 1 in list_o and 5 in list_o and 9 in list_o:
            y = True
        elif 3 in list_o and 5 in list_o and 7 in list_o:
            y = True

    #Verificamos si todas las casillas fueron usadas
    if len(list_x) + len(list_o) == 9:
        return True, 2 #Empate
    elif x:
        return True, 0 #Gana X
    elif y:
        return True, 1 #Gana O

    return False, 2 #El juego continúa
