"""
Nombre: Equipo los Bugs
Fecha: 16 de mayo del 2025.

Descripción:
Se agregó música de fondo y efectos de sonido al juego mediante la clase Audio.
Las funciones del juego ahora reproducen sonidos según la acción del jugador.
Las configuraciones necesarias se integraron en la clase Configurations.
"""

import pygame

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)  #Definimos el tamaño de la ventana del juego
    _game_title = "Cat game en pygame"  #Título que aparece en la ventana del juego
    _background_image_path =  "../media/background_image.png"
    _fps = 8  #fps del juego

    _mark_X = "../media/markX.png"
    _mark_O = "../media/markO.png"

    _image_turno_x = "../media/turnX.png"
    _image_turno_o = "../media/turnO.png"

    _size_block = (80,80)  #Tamaño de cada marca que se coloca en el tablero

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
    }  #Coordenadas centrales de cada una de las nueve casillas del tablero

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
    }  #Asignamos teclas del teclado a cada casilla del tablero

    _cell_number = []  #Lista vacía para llevar el control de las casillas ocupadas

    _center_x = 650  #Centramos la imagen horizontalmente
    _bottom_x = 250  #Ajustamos las medidas de la parte inferior de la imagen

    _result_image = ["../media/winX.png","../media/winO.png","../media/draw.png"]  #Imágenes de resultados

    _music_path = "../media/music.mp3"
    _keyboard_sound = "../media/keyboard_sound.mp3"
    _results_sound = "../media/results_sound.mp3"

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """Devuelve el tamaño de la pantalla"""
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """Devuelve el título del juego"""
        return cls._game_title

    @classmethod
    def get_fps(cls) -> int:
        """Devuelve los cuadros por segundo"""
        return cls._fps

    @classmethod
    def get_mark_O(cls) -> str:
        """Devuelve la ruta de la imagen de la marca O"""
        return cls._mark_O

    @classmethod
    def get_mark_X(cls) -> str:
        """Devuelve la ruta de la imagen de la marca X"""
        return cls._mark_X

    @classmethod
    def get_background_image_path(cls) -> str:
        """Devuelve la ruta de la imagen de fondo"""
        return cls._background_image_path

    @classmethod
    def get_posiciones(cls) -> dict[int, tuple[int, int]]:
        """Devuelve las posiciones del tablero"""
        return cls._posiciones

    @classmethod
    def get_size_block(cls) -> tuple[int,int]:
        """Devuelve el tamaño de cada bloque"""
        return cls._size_block

    @classmethod
    def get_teclas(cls) -> dict[int, int]:
        """Devuelve el diccionario de teclas asignadas"""
        return cls._teclas

    @classmethod
    def get_cell_number(cls) -> list:
        """Devuelve la lista de casillas ocupadas"""
        return cls._cell_number

    @classmethod
    def get_image_turno_x(cls) -> str:
        """Devuelve la ruta de la imagen de turno X"""
        return cls._image_turno_x

    @classmethod
    def get_image_turno_o(cls) -> str:
        """Devuelve la ruta de la imagen de turno O"""
        return cls._image_turno_o

    @classmethod
    def get_center_x(cls) -> int:
        """Devuelve la coordenada X central para el resultado"""
        return cls._center_x

    @classmethod
    def get_bottom_x(cls) -> int:
        """Devuelve la coordenada inferior para el resultado"""
        return cls._bottom_x

    @classmethod
    def get_result_image(cls) -> list[str]:
        """Devuelve la lista de imágenes de resultados"""
        return cls._result_image

    @classmethod
    def get_music_path(cls) -> str:
        """Devuelve la ruta de la música de fondo"""
        return cls._music_path

    @classmethod
    def get_keyboard_sound(cls) -> str:
        """Devuelve la ruta del sonido de teclado"""
        return cls._keyboard_sound

    @classmethod
    def get_results_sound(cls) -> str:
        """Devuelve la ruta del sonido de resultado"""
        return cls._results_sound
