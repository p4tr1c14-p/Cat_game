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
from Game_functionalities import game_event, screen_refresh,check_winner,game_over_screen
from Media import Background, Turn_Image, Resultado_image

def run_game() -> None:
    """
    Función principal del videojuego
    """
    pygame.init()

    clock = pygame.time.Clock() #Creamos el reloj para controlar los fps

    screen = pygame.display.set_mode(Configurations.get_screen_size()) #Creamos la ventana del juego con el tamaño definido

    pygame.display.set_caption(Configurations.get_game_title()) #Colocamos el título de la ventana

    game_over = False
    background = Background()

    marks = pygame.sprite.Group() #Creamos un grupo de sprites para las marcas
    list_turn = Configurations.get_cell_number() #Obtenemos la lista de casillas ya utilizadas

    turno = pygame.sprite.Group() #Creamos un grupo de sprites para la imagen del turno

    nueva_image = Turn_Image() #Creamos la imagen inicial del turno
    turno.add(nueva_image) #La agregamos al grupo de turno

    lista_imagen = [nueva_image] #Guardamos la imagen en la lista para poder hacer control de turnos

    b = True
    lista_x = []
    lista_o = []

    mostrar_resultado = True
    intervalo_parpadeo = 500  # milisegundos
    ultimo_cambio = pygame.time.get_ticks()


    while not game_over:
        game_over = game_event(marks, list_turn, turno, lista_imagen,b,lista_x,lista_o)
        screen_refresh(screen, clock, background, marks, turno)
        check_winner(lista_x,lista_o)

        if game_over:
            break

        game_over,winner = check_winner(lista_x,lista_o)
        if game_over:
            result = Resultado_image(winner)
            result.blit(screen)
            pygame.display.flip()
            game_over_screen(screen,result)

if __name__ == '__main__':
    run_game()
