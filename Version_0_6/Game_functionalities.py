"""
Nombre:
Fecha: 15 de mayo del 2025.

Descripción:
En esta versión se incluye la verificación para evitar colocar marcas en casillas ya ocupadas.
Se agregaron imágenes que indican de forma visual a quién le toca el turno (X o O),
y se alternan dinámicamente con cada jugada.
Se implementó la clase TurnImage para manejar este cambio visual y se integraron todas
las configuraciones necesarias en la clase Configurations.
Aún no se incorpora la lógica para detectar al ganador
"""

import pygame
from Configurations import Configurations
from Media import Background, Turn_image
from TikTacToe import TicTacToeMark

def game_event(marks, list_turn, turn, lista_imagen,list_x,list_o) -> bool:
    """
    Función que administra los eventos del juego
    return: La bandera del fin del juego
    """
    game_over = False

    for event in pygame.event.get(): #Revisamos todos los eventos que ocurren

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
    """
    background.blit(screen) #Dibujamos el fondo en la pantalla

    marks.draw(screen) #Dibujamos todas las marcas X y O que se han colocado

    turn.draw(screen) #Dibujamos la imagen del turno actual

    pygame.display.flip() #Actualizamos toda la pantalla con los nuevos elementos

    clock.tick(Configurations.get_fps()) #Limitamos la velocidad del juego a los fps definidos

def check_winner(list_x,list_o)->tuple[bool,int]:
    y = False
    x = False
    for i in range(3):
       if (i+(i*2) + 1) in list_x and (i+(i*2) + 2) in list_x and (i+(i*2) + 3) in list_x:
           x = True
           break
       elif i+1 in list_x and i+4 in list_x and i+7 in list_x:
           x = True
           break
    if not x:
        if 1 in list_x and 5 in list_x and 9  in list_x:
            x = True
        elif 3 in list_x and 5 in list_x and 7  in list_x:
            x = True

    for i in range(3):
       if (i+(i*2) + 1) in list_o and (i+(i*2) + 2) in list_o and (i+(i*2) + 3) in list_o:
           y = True
           break
       elif i+1 in list_o and i+4 in list_o and i+7 in list_o:
           y = True
           break
    if not y:
        if 1 in list_o and 5 in list_o and 9  in list_o:
            y = True
        elif 3 in list_o and 5 in list_o and 7  in list_o:
            y= True

    if len(list_x) + len(list_o) == 9:
        return True, 2
    elif  x:
        return True,0
    elif y:
        return True, 1


    return False,2
















