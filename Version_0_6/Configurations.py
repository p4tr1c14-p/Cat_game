""""
Nombre: Equipo los Bugs
Fecha: 16 de mayo del 2025.

Descripción:
En esta versión se implementó la lógica para determinar al ganador del juego.
Se añadió la función check_winner() para detectar si ganó el jugador X, O o si hubo empate.
También se agregó una pantalla de resultados y créditos, mostrando una imagen dependiendo del resultado.
Por último, se incluyó la función game_over_screen() para mostrar el resultado final usando animaciones
simples y redibujado de pantalla.
"""

import pygame

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    Proporciona acceso a las constantes de configuración mediante métodos de clase
    Centraliza parámetros como tamaños, rutas de imágenes, asignaciones de teclas y posiciones
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)
    _game_title = "Cat game en pygame"
    _background_image_path =  "../media/background_image.png"
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

    _center_x = 650 #Centramos la imagen horizontalmente
    _bottom_x = 250 #Ajustamos las medidas de la parte inferior de la imagen

    _result_image = ["../media/winX.png","../media/winO.png","../media/draw.png"] #Rutas de las imágenes de resultados

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Devuelve el tamaño de la pantalla del juego
        """
        return cls._screen_size

    @classmethod
    def get_game_title(cls) -> str:
        """
        Devuelve el título del juego para la ventana
        """
        return cls._game_title

    @classmethod
    def get_fps(cls) -> int:
        """
        Devuelve los cuadros por segundo para controlar la velocidad del juego
        """
        return cls._fps

    @classmethod
    def get_mark_O(cls) -> str:
        """
        Devuelve la ruta de la imagen para la marca O
        """
        return cls._mark_O

    @classmethod
    def get_mark_X(cls) -> str:
        """
        Devuelve la ruta de la imagen para la marca X
        """
        return cls._mark_X

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Devuelve la ruta de la imagen de fondo del juego
        """
        return cls._background_image_path

    @classmethod
    def get_posiciones(cls) -> dict[int, tuple[int, int]]:
        """
        Devuelve el diccionario con las posiciones centrales de cada casilla
        """
        return cls._posiciones

    @classmethod
    def get_size_block(cls) -> tuple[int,int]:
        """
        Devuelve el tamaño de los bloques de las marcas
        """
        return cls._size_block

    @classmethod
    def get_teclas(cls) -> dict[int, int]:
        """
        Devuelve el diccionario que mapea teclas a posiciones del tablero
        """
        return cls._teclas

    @classmethod
    def get_cell_number(cls) -> list:
        """
        Devuelve la lista de celdas ocupadas en el tablero
        """
        return cls._cell_number

    @classmethod
    def get_image_turno_x(cls) -> str:
        """
        Devuelve la ruta de la imagen que indica el turno del jugador X
        """
        return cls._image_turno_x

    @classmethod
    def get_image_turno_o(cls) -> str:
        """
        Devuelve la ruta de la imagen que indica el turno del jugador O
        """
        return cls._image_turno_o

    @classmethod
    def get_center_x(cls)->int:
        """
        Devuelve la posición central horizontal para alinear elementos
        """
        return cls._center_x

    @classmethod
    def get_bottom_x(cls)->int:
        """
        Devuelve la posición inferior para alinear elementos
        """
        return cls._bottom_x

    @classmethod
    def get_result_image(cls)-> list[str]:
        """
        Devuelve la lista de rutas de imágenes de resultados (victoria X, victoria O, empate)
        """
        return cls._result_image