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
from Game_functionalities import game_event, screen_refresh,check_winner
from Media import Background, Turn_image, Resultado_image, CreditsIma

def run_game() -> None:
    """
    Función principal del videojuego
    Inicializa Pygame, configura la pantalla y los recursos necesarios
    Ejecuta el bucle principal del juego controlando los eventos y la lógica del juego
    Muestra el resultado al finalizar una partida con animación de parpadeo
    """
    pygame.init()

    clock = pygame.time.Clock() #Creamos el reloj para controlar los fps

    screen = pygame.display.set_mode(Configurations.get_screen_size())

    pygame.display.set_caption(Configurations.get_game_title())

    game_over = False
    background = Background()

    marks = pygame.sprite.Group() #Creamos un grupo de sprites para las marcas
    list_turn = Configurations.get_cell_number() #Obtenemos la lista de casillas ya utilizadas

    turno = pygame.sprite.Group() #Creamos un grupo de sprites para la imagen del turno

    nueva_image = Turn_image() #Creamos la imagen inicial del turno
    turno.add(nueva_image) #La agregamos al grupo de turno

    lista_imagen = [nueva_image] #Guardamos la imagen en la lista para poder hacer control de turnos

    creditos = CreditsIma()  #
    lista_x = []  #Inicializamos la lista para jugadas del jugador X
    lista_o = []  #Inicializamos la lista para jugadas del jugador O


    while not game_over:
        game_over = game_event(marks, list_turn, turno, lista_imagen,lista_x,lista_o)
        screen_refresh(screen, clock, background, marks, turno)
        check_winner(lista_x,lista_o)  #Verificamos si hay un ganador

        if game_over:
            break

        game_over,winner = check_winner(lista_x,lista_o)  #Obtenemos el estado del juego y el ganador

        if game_over:  #Si el juego terminó mostramos el resultado

            result = Resultado_image(winner)  #Creamos la imagen del resultado según el ganador
            bandera = True  #Variable para controlar el parpadeo
            start_time = pygame.time.get_ticks()  #Capturamos el tiempo de inicio

            while pygame.time.get_ticks() - start_time < 4000:  # Parpadea durante 4 segundos
                #Redibujamos el fondo y marcas sin tocarlas
                screen_refresh(screen, clock, background, marks, turno)

                if bandera:
                    result.blit(screen)  #Mostramos la imagen del resultado

                creditos.blit(screen)  #Mostramos los créditos del juego

                pygame.display.flip()  #Actualizamos la pantalla completa
                pygame.time.delay(400)  # Tiempo entre parpadeos
                bandera = not bandera  # Alternar mostrar/ocultar


if __name__ == '__main__':
    run_game()