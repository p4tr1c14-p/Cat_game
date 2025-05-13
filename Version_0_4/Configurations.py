"""
Nombre:
Fecha: 13 de mayo del 2025.

Descripción: version 4
"""


class Configurations:
    """
    Clase que continue todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)
    _game_title = "Cat game en pygame"
    _background_image_path =  "../media/background_image.png"
    _fps = 8  # fps del juego

    _x_images_path = "../media/markX.png"
    _o_images_path = "../media/markO.png"

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
    def get_background_image_path(cls) -> str:
        return cls._background_image_path

    @classmethod
    def get_x_images_path(cls) -> str:
        return cls._x_images_path

    @classmethod
    def get_o_images_path(cls) -> str:
        return cls._o_images_path