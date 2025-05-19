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
from Game_functionalities import game_event, screen_refresh, check_winner
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

    creditos = CreditsIma()  #Imagen de créditos.
    lista_x = []  #Jugadas del jugador X.
    lista_o = []  #Jugadas del jugador O.

    audio = Audio()
    audio.play_music(0.25)

    while not game_over:
        game_over = game_event(marks, list_turn, turno, lista_imagen, lista_x, lista_o, audio)

        screen_refresh(screen, clock, background, marks, turno)

        check_winner(lista_x, lista_o)  #Verificamos si hay un ganador en esta ronda.

        if game_over:
            break

        game_over, winner = check_winner(lista_x, lista_o)  #Revisamos ganador y lo guardamos.

        if game_over:
            result = ResultadoImage(winner)  #Imagen del resultado.
            bandera = True
            start_time = pygame.time.get_ticks()
            audio.play_results_sound()  #Reproducimos sonido final.

            while pygame.time.get_ticks() - start_time < 4000:  #Parpadeamos 4 segundos.
                screen_refresh(screen, clock, background, marks, turno)  #Redibujamos fondo y marcas sin cambios.

                if bandera:
                    result.blit(screen)  #Mostramos imagen del resultado.

                creditos.blit(screen)  # Mostramos créditos.
                pygame.display.flip()
                pygame.time.delay(400)  #Tiempo entre parpadeos.
                bandera = not bandera  #Alternamos mostrar/ocultar.


if __name__ == '__main__':
    run_game()