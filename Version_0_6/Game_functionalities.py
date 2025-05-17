"""
Nombre: Equipo los Bugs.
Fecha: 16 de mayo del 2025.

Descripción:
En esta versión se implementó la lógica para determinar al ganador del juego.
Se añadió la función check_winner() para detectar si ganó el jugador X, O o si hubo empate.
También se agregó una pantalla de resultados y créditos, mostrando una imagen dependiendo del resultado.
Por último, se incluyó la función game_over_screen() para mostrar el resultado final usando animaciones
simples y redibujado de pantalla.
"""

import pygame
from Configurations import Configurations
from Media import Background, Turn_image
from TikTacToe import TicTacToeMark

def game_event(marks, list_turn, turn, lista_imagen, list_x, list_o) -> bool:
    """
    Función que administra los eventos del juego
    Procesa las teclas presionadas, crea nuevas marcas en el tablero y actualiza los turnos
    Mantiene actualizadas las listas de posiciones ocupadas por cada jugador

    Args:
        marks: Grupo de sprites que contiene las marcas en el tablero
        list_turn: Lista que contiene las casillas ya utilizadas
        turn: Grupo de sprites que contiene la imagen del turno actual
        lista_imagen: Lista que contiene las imágenes de los turnos
        list_x: Lista de posiciones ocupadas por el jugador X
        list_o: Lista de posiciones ocupadas por el jugador O

    Returns:
        bool: La bandera que indica si el juego ha terminado
    """
    game_over = False

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_over = True

        elif event.type == pygame.KEYDOWN:
            #Verificamos si la tecla presionada es válida y aún no ha sido usada
            if event.key in Configurations.get_teclas() and Configurations.get_teclas()[event.key] not in list_turn:
                nueva_marca = TicTacToeMark(Configurations.get_teclas()[event.key]) #Creamos una nueva marca en la casilla correspondiente
                list_turn.append(Configurations.get_teclas()[event.key]) #Guardamos la casilla ya utilizada
                marks.add(nueva_marca) #Agregamos la marca al grupo que se va a dibujar

                turn.remove(lista_imagen[len(list_turn)-1]) #Esto es para remover la imagen del turno anterior

                nueva_image = Turn_image() #Creamos la nueva imagen de turno
                turn.add(nueva_image) #La agregamos al grupo que se va a mostrar
                lista_imagen.append(nueva_image) #La guardamos en la lista para tener el control de turnos

                for i in range(len(list_turn)):
                    if i %2 == 0 and list_turn[i] not in list_x:
                        list_x.append(Configurations.get_teclas()[event.key])
                    elif i %2 != 0 and list_turn[i] not in list_o:
                        list_o.append(Configurations.get_teclas()[event.key])


    return game_over

def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background, marks, turn) -> None:
    """
    Función que administra los elementos visuales del juego
    Dibuja el fondo, las marcas colocadas y el indicador de turno actual
    Actualiza la pantalla y controla la velocidad del juego

    Args:
        screen: Superficie de pygame donde se dibujan los elementos
        clock: Reloj para controlar los FPS
        background: Objeto que contiene la imagen de fondo
        marks: Grupo de sprites con las marcas X y O
        turn: Grupo de sprites con la imagen del turno actual
    """
    background.blit(screen)

    marks.draw(screen)

    turn.draw(screen)

    pygame.display.flip()

    clock.tick(Configurations.get_fps())

def check_winner(list_x, list_o) -> tuple[bool, int]:
    """
    Verifica si hay un ganador o empate en el juego
    Comprueba todas las combinaciones ganadoras posibles para ambos jugadores

    Args:
        list_x: Lista de posiciones ocupadas por el jugador X
        list_o: Lista de posiciones ocupadas por el jugador O

    Returns:
        tuple[bool, int]: Una tupla con:
            - bool: True si el juego ha terminado, False en caso contrario
            - int: 0 si ganó X, 1 si ganó O, 2 si hay empate o aún no hay ganador
    """
    y = False  #Variable para indicar si el jugador O ha ganado
    x = False  #Variable para indicar si el jugador X ha ganado

    #Verificamos filas y columnas para jugador X
    for i in range(3):
       if (i+(i*2) + 1) in list_x and (i+(i*2) + 2) in list_x and (i+(i*2) + 3) in list_x:  #Comprobamos filas
           x = True
           break
       elif i+1 in list_x and i+4 in list_x and i+7 in list_x:  #Comprobamos columnas
           x = True
           break

    #Verificamos diagonales para jugador X
    if not x:
        if 1 in list_x and 5 in list_x and 9 in list_x:  #Comprobamos diagonal principal
            x = True
        elif 3 in list_x and 5 in list_x and 7 in list_x:  #Comprobamos diagonal inversa
            x = True

    #Verificamos filas y columnas para jugador O
    for i in range(3):
       if (i+(i*2) + 1) in list_o and (i+(i*2) + 2) in list_o and (i+(i*2) + 3) in list_o:  #Comprobamos filas
           y = True
           break
       elif i+1 in list_o and i+4 in list_o and i+7 in list_o:  #Comprobamos columnas
           y = True
           break

    #Verificamos diagonales para jugador O
    if not y:
        if 1 in list_o and 5 in list_o and 9 in list_o:  #Comprobamos diagonal principal
            y = True
        elif 3 in list_o and 5 in list_o and 7 in list_o:  #Comprobamos diagonal inversa
            y = True

    #Determinamos el resultado del juego
    if len(list_x) + len(list_o) == 9:  #Si todas las casillas están ocupadas
        return True, 2  #Empate
    elif x:  #Si ganó X
        return True, 0
    elif y:  #Si ganó O
        return True, 1

    return False, 2  #El juego continúa