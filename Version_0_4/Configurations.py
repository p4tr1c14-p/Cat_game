"""
Nombre:
Fecha: 12 de mayo del 2025.

Descripción:
"""
import pygame

class Configurations:
    """
    Clase que continue todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)
    _game_title = "Cat game en pygame"
    _background_image_path =  "../media/background_image.png"
    _fps = 8  # fps del juego

    _mark_O = "../media/markX.png"
    _mark_X = "../media/markO.png"

    _size_block = (80,80)

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

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para screen_size
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para get_game_title
        """
        return cls._game_title


    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        :return:
        """
        return cls._fps

    @classmethod
    def get_mark_O(cls) -> str:
        return cls._mark_O

    @classmethod
    def get_mark_X(cls) -> str:
        return cls._mark_X

    @classmethod
    def get_background_image_path(cls)-> str:
        return cls._background_image_path

    @classmethod
    def get_posiciones(cls)-> dict[int, tuple[int, int]]:
        return cls._posiciones

    @classmethod
    def get_size_block(cls) -> tuple[int,int]:
        return cls._size_block

    @classmethod
    def get_teclas(cls) -> dict[int, int]:
        return cls._teclas
