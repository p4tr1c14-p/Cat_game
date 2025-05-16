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

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720) #Definimos el tamaño de la ventana del juego
    _game_title = "Cat game en pygame" #Título que aparece en la ventana del juego
    _background_image_path =  "../media/background_image.png" #Ruta de la imagen de fondo
    _fps = 8  #fps del juego

    _mark_X = "../media/markX.png"
    _mark_O = "../media/markO.png"

    _image_turno_x = "../media/turnX.png"
    _image_turno_o = "../media/turnO.png"

    _size_block = (80,80) #Tamaño de cada marca que se coloca en el tablero

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
    } #Coordenadas centrales de cada una de las nueve casillas del tablero

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
    } #Asignamos teclas del teclado a cada casilla del tablero

    _cell_number = [] #Lista vacía para llevar el control de las casillas ocupadas

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
    def get_size_block(cls) -> tuple[int,int]:
        return cls._size_block

    @classmethod
    def get_teclas(cls) -> dict[int, int]:
        return cls._teclas

    @classmethod
    def get_cell_number(cls) -> list:
        return cls._cell_number

    @classmethod
    def get_image_turno_x(cls) -> str:
        return cls._image_turno_x

    @classmethod
    def get_image_turno_o(cls) -> str:
        return cls._image_turno_o
