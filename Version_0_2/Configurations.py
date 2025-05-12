"""
Nombre:
Fecha: 12 de mayo del 2025.

Descripción:
"""

class Configurations:
    """
    Clase que continue todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)
    _game_title = "Cat game en pygame"
    _background = (135,206,235)

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
        return cls._background