"""
Nombre: Equipo los Bugs.
Fecha: 16 de mayo del 2025.

Descripción:
Se agregó música de fondo y efectos de sonido al juego mediante la clase Audio.
Las funciones del juego ahora reproducen sonidos según la acción del jugador.
Las configuraciones necesarias se integraron en la clase Configurations.
"""

import pygame

from Configurations import Configurations
from Game_functionalities import game_event, screen_refresh, check_winner,screen_game_over
from Media import Background, TurnoImage, ResultadoImage, CreditsIma, Audio

def run_game() -> None:
    """
    Función principal del videojuego.
    Inicializa Pygame, configura la pantalla, carga los recursos multimedia y ejecuta el bucle principal del juego.
    """
    pygame.init()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode(Configurations.get_screen_size())

    pygame.display.set_caption(Configurations.get_game_title())

    game_over = False
    background = Background()

    marks = pygame.sprite.Group()  #Grupo de sprites para las marcas.
    list_turn = Configurations.get_cell_number()  #Lista de casillas ya usadas.

    turno = pygame.sprite.Group()  #Grupo de sprites para imagen del turno.

    nueva_image = TurnoImage()  #Imagen inicial del turno.
    turno.add(nueva_image)  #Agregamos imagen al grupo turno.

    lista_imagen = [nueva_image]  #Lista para controlar la imagen del turno.

    credits = CreditsIma()  #Imagen de créditos.
    lista_x = []  #Jugadas del jugador X.
    lista_o = []  #Jugadas del jugador O.

    audio = Audio()
    audio.play_music(Configurations.get_volumen())

    while not game_over:
        game_over = game_event(marks, list_turn, turno, lista_imagen, lista_x, lista_o, audio)

        screen_refresh(screen, clock, background, marks, turno,credits)

        check_winner(lista_x, lista_o)  #Verificamos si hay un ganador en esta ronda.

        if game_over:
            break

        game_over, winner = check_winner(lista_x, lista_o)  #Revisamos ganador y lo guardamos.

        if game_over:
            result = ResultadoImage(winner)  #Imagen del resultado.
            audio.play_results_sound()  #Reproducimos sonido final.
            screen_game_over(screen, clock, background, marks, turno,result,credits)


if __name__ == '__main__':
    run_game()