"""
Nombre: Equipo los Bugs
Fecha: 13 de mayo del 2025.

Descripción:
"""

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Definimos el tamaño de la pantalla, el título, la ruta del fondo y los fps del juego
    _screen_size = (1280, 720)
    _game_title = "Cat game en pygame"
    _background_image_path =  "../media/background_image.png"
    _fps = 8  #fps del juego

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para screen_size
        """
        return cls._screen_size  #Regresamos el tamaño de la pantalla

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para get_game_title
        """
        return cls._game_title  #Regresamos el título del juego

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps
        """
        return cls._fps

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path
        """
        return cls._background_image_path
