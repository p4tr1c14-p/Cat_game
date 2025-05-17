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

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _screen_size = (1280, 720)  # Definimos el tamaño de la ventana del juego.
    _game_title = "Cat game en pygame"  # Título que aparece en la ventana del juego.
    _background_image_path = "../media/background_image.png"  # Ruta de la imagen de fondo.
    _fps = 8  # FPS del juego.

    _mark_X = "../media/markX.png"
    _mark_O = "../media/markO.png"

    _image_turno_x = "../media/turnX.png"
    _image_turno_o = "../media/turnO.png"

    _size_block = (80, 80)  # Tamaño de cada marca que se coloca en el tablero.

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
    }  # Coordenadas centrales de cada una de las nueve casillas del tablero.

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
    }  # Asignamos teclas del teclado a cada casilla del tablero.

    _cell_number = []  # Lista vacía para llevar el control de las casillas ocupadas.

    _center_x = 650  # Centramos la imagen horizontalmente.
    _bottom_x = 250  # Ajustamos las medidas de la parte inferior de la imagen.

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

    @classmethod
    def get_cell_number(cls) -> list:
        """
        Retorna la lista de casillas ocupadas en el tablero.

        Returns:
            list: Lista que contiene los números de las casillas que ya están ocupadas.
        """
        return cls._cell_number

    @classmethod
    def get_image_turno_x(cls) -> str:
        """
        Retorna la ruta de la imagen que indica el turno del jugador X.

        Returns:
            str: Ruta del archivo de imagen que indica que es turno del jugador X.
        """
        return cls._image_turno_x

    @classmethod
    def get_image_turno_o(cls) -> str:
        """
        Retorna la ruta de la imagen que indica el turno del jugador O.

        Returns:
            str: Ruta del archivo de imagen que indica que es turno del jugador O.
        """
        return cls._image_turno_o

    @classmethod
    def get_center_x(cls) -> int:
        """
        Retorna la coordenada X para centrar elementos horizontalmente.

        Returns:
            int: Valor de la coordenada X para centrar elementos en la pantalla.
        """
        return cls._center_x

    @classmethod
    def get_bottom_x(cls) -> int:
        """
        Retorna la coordenada X para posicionar elementos en la parte inferior.

        Returns:
            int: Valor de la coordenada X para posicionar elementos en la parte inferior.
        """
        return cls._bottom_x
