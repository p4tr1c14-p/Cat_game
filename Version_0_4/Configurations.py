"""
Nombre:
Fecha: 14 de mayo del 2025.

Descripción:
Se agregaron marcas X y O con imágenes al juego.
Se creó clase TicTacToeMark que muestra la imagen correspondiente según el turno del jugador.
El juego responde a teclas q,w,e,a,s,d,z,x y c para colocar marcas en las 9 casillas.
Aún falta implementar la lógica completa del juego que impida colocar marcas sobre otras ya existentes.
"""

import pygame

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """

    #Configuración de pantalla
    _screen_size = (1280, 720)
    _game_title = "Cat game en pygame"
    _background_image_path =  "../media/background_image.png"
    _fps = 8  #Cuadros por segundo

    _mark_O = "../media/markX.png"
    _mark_X = "../media/markO.png"

    _size_block = (80, 80)

    #Posiciones en la pantalla correspondientes a cada celda (1 a 9)
    _posiciones = {
        1: (503, 324),
        2: (639, 324),
        3: (763, 324),
        4: (503, 451),
        5: (639, 451),
        6: (764, 446),
        7: (496, 577),
        8: (629, 566),
        9: (770, 566),
    }

    #Teclas asignadas para cada celda
    _teclas = {
        pygame.K_q: 1,
        pygame.K_w: 2,
        pygame.K_e: 3,
        pygame.K_a: 4,
        pygame.K_s: 5,
        pygame.K_d: 6,
        pygame.K_z: 7,
        pygame.K_x: 8,
        pygame.K_c: 9,
    }

    #Métodos para acceder a cada configuración

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        return cls._game_title

    @classmethod
    def get_fps(cls) -> int:
        return cls._fps

    @classmethod
    def get_mark_O(cls) -> str:
        return cls._mark_O

    @classmethod
    def get_mark_X(cls) -> str:
        return cls._mark_X

    @classmethod
    def get_background_image_path(cls) -> str:
        return cls._background_image_path

    @classmethod
    def get_posiciones(cls) -> dict[int, tuple[int, int]]:
        return cls._posiciones

    @classmethod
    def get_size_block(cls) -> tuple[int, int]:
        return cls._size_block

    @classmethod
    def get_teclas(cls) -> dict[int, int]:
        return cls._teclas
