"""
Nombre: Equipo los Bugs.
Fecha: 15 de mayo del 2025.

Descripción:
En esta versión se incluye la verificación para evitar colocar marcas en casillas ya ocupadas.
Se agregaron imágenes que indican de forma visual a quién le toca el turno (X o O),
y se alternan dinámicamente con cada jugada.
Se implementó la clase TurnImage para manejar este cambio visual y se integraron todas
las configuraciones necesarias en la clase Configurations.
Aún no se incorpora la lógica para detectar al ganador.
"""

import pygame
from Configurations import Configurations
from Media import Background, Turn_Image
from TikTacToe import TicTacToeMark

def game_event(marks, list_turn, turn, lista_imagen) -> bool:
    """
    Función que administra los eventos del juego.
    return: La bandera del fin del juego.
    """
    game_over = False

    for event in pygame.event.get(): #Revisamos todos los eventos que ocurren.

        if event.type == pygame.QUIT:
            game_over = True

        elif event.type == pygame.KEYDOWN:
            #Verificamos si la tecla presionada es válida y aún no ha sido usada.
            if event.key in Configurations.get_teclas() and Configurations.get_teclas()[event.key] not in list_turn:
                nueva_marca = TicTacToeMark(Configurations.get_teclas()[event.key]) #Creamos una nueva marca en la casilla correspondiente.
                list_turn.append(Configurations.get_teclas()[event.key]) #Guardamos la casilla ya utilizada.
                marks.add(nueva_marca) #Agregamos la marca al grupo que se va a dibujar.

                turn.remove(lista_imagen[len(list_turn)-1]) #Esto es para remover la imagen del turno anterior.

                nueva_image = Turn_Image() #Creamos la nueva imagen de turno.
                turn.add(nueva_image) #La agregamos al grupo que se va a mostrar.
                lista_imagen.append(nueva_image) #La guardamos en la lista para tener el control de turnos.

    return game_over

def screen_refresh(screen: pygame.surface.Surface,
                   clock: pygame.time.Clock, background: Background, marks, turn) -> None:
    """
    Función que administra los elementos visuales del juego.
    """
    background.blit(screen) #Dibujamos el fondo en la pantalla.

    marks.draw(screen) #Dibujamos todas las marcas X y O que se han colocado.

    turn.draw(screen) #Dibujamos la imagen del turno actual.

    pygame.display.flip() #Actualizamos toda la pantalla con los nuevos elementos.

    clock.tick(Configurations.get_fps()) #Limitamos la velocidad del juego a los fps definidos.
