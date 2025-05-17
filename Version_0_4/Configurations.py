"""
Nombre: Equipo los Bugs.
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
    Clase que contiene todas las configuraciones del juego.
    """

    #Configuración de pantalla
    _screen_size = (1280, 720)
    _game_title = "Cat game en pygame"
    _background_image_path =  "../media/background_image.png"
    _fps = 8  #Cuadros por segundo.

    _mark_O = "../media/markX.png"
    _mark_X = "../media/markO.png"

    _size_block = (80, 80)

    #Posiciones en la pantalla correspondientes a cada celda (1 a 9).
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

    #Teclas asignadas para cada celda.
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

    #Métodos para acceder a cada configuración.

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Retorna el tamaño de la pantalla del juego.

        Returns:
            tuple[int, int]: Una tupla con el ancho y alto de la pantalla en píxeles.
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Retorna el título del juego.

        Returns:
            str: El título que aparecerá en la ventana del juego.
        """
        return cls._game_title

    @classmethod
    def get_fps(cls) -> int:
        """
        Retorna los cuadros por segundo (FPS) del juego.

        Returns:
            int: La cantidad de FPS configurada para el juego.
        """
        return cls._fps

    @classmethod
    def get_mark_O(cls) -> str:
        """
        Retorna la ruta de la imagen para la marca O.

        Returns:
            str: Ruta del archivo de imagen para la marca O.
        """
        return cls._mark_O

    @classmethod
    def get_mark_X(cls) -> str:
        """
        Retorna la ruta de la imagen para la marca X.

        Returns:
            str: Ruta del archivo de imagen para la marca X.
        """
        return cls._mark_X

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Retorna la ruta de la imagen de fondo del juego.

        Returns:
            str: Ruta del archivo de imagen para el fondo del juego.
        """
        return cls._background_image_path

    @classmethod
    def get_posiciones(cls) -> dict[int, tuple[int, int]]:
        """
        Retorna el diccionario con las posiciones de las casillas del tablero.

        Returns:
            dict[int, tuple[int, int]]: Diccionario que mapea el número de casilla (1-9)
             a sus coordenadas (x, y) en la pantalla.
        """
        return cls._posiciones

    @classmethod
    def get_size_block(cls) -> tuple[int, int]:
        """
        Retorna el tamaño de cada marca (X u O) en el tablero.

        Returns:
            tuple[int, int]: Una tupla con el ancho y alto de cada marca en píxeles.
        """
        return cls._size_block

    @classmethod
    def get_teclas(cls) -> dict[int, int]:
        """
        Retorna el mapeo de teclas a números de casilla.

        Returns:
            dict[int, int]: Diccionario que mapea las constantes de teclas de pygame
             a los números de casilla (1-9) del tablero.
        """
        return cls._teclas
