"""
Nombre: Equipo los Bugs
Fecha: 12 de mayo del 2025.

Descripción:
"""

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Definimos el tamaño de la pantalla, título y color de fondo RGB
    _screen_size = (1280, 720)
    _game_title = "Cat game en pygame"
    _background = (135, 206, 235)  #Color de fondo azul cielo

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
    def get_background(cls) -> tuple[int, int, int]:
        """
        Getter para _background_image_path
        """
        return cls._background  #Regresamos el color de fondo como tupla RGB
