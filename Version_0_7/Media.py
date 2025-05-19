"""
Nombre: Equipo los Bugs.
Fecha: 16 de mayo del 2025.

Descripción:
Se agregó música de fondo y efectos de sonido al juego mediante la clase Audio.
Las funciones del juego ahora reproducen sonidos según la acción del jugador.
Las configuraciones necesarias se integraron en la clase Configurations.
"""

import pygame
from Configurations import Configurations
from pygame.sprite import Sprite

class Background:
    """
    Clase que contiene y dibuja el fondo de pantalla del juego.
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(background_image_path)

        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size) #Aquí nosotros escalamos la imagen al tamaño de la pantalla.

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Dibuja la imagen de fondo en la pantalla.
        """
        screen.blit(self.image, self.rect) #Aquí nosotros dibujamos la imagen de fondo sobre la pantalla.


class TurnoImage(Sprite):
    """
    Clase que maneja la imagen que indica de quién es el turno
    """

    turno = "X" #Aquí nosotros inicializamos el turno con la letra "X".

    def __init__(self):
        super().__init__()

        if TurnoImage.turno == "X":
            self.image = pygame.image.load(Configurations.get_image_turno_x())
            TurnoImage.turno = "O" #Aquí nosotros cambiamos el turno a "O".
        else:
            self.image = pygame.image.load(Configurations.get_image_turno_o())
            TurnoImage.turno = "X" #Aquí nosotros cambiamos el turno a "X".

        self.image = pygame.transform.scale(self.image, (Configurations.get_size()))
        self.rect = self.image.get_rect()
        self.rect.centerx = Configurations.get_center_x() #Aquí nosotros centramos horizontalmente la imagen.
        self.rect.bottom = Configurations.get_bottom_x() #Aquí nosotros ajustamos la posición inferior.


class ResultadoImage:
    """
    Clase que muestra la imagen del resultado del juego.
    """

    def __init__(self, result):
        self.image = pygame.image.load(Configurations.get_result_image()[result])
        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Dibuja la imagen del resultado en pantalla.
        """
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = Configurations.get_bottom()
        screen.blit(self.image, self.rect)


class CreditsIma(Sprite):
    """
    Clase que muestra la imagen de los créditos.
    """

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(Configurations.get_img_creditos()) #Aquí nosotros cargamos la imagen de créditos.
        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Dibuja la imagen de créditos en pantalla
        """
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = Configurations.get_bottom()
        screen.blit(self.image, self.rect)


class Audio:
    """
    Clase que contiene el audio del videojuego, incluyendo la música y los efectos de sonido.
    """

    def __init__(self):
        pygame.mixer.music.load(Configurations.get_music_path()) #Aquí nosotros cargamos la música del juego.
        self._keyboard_sound = pygame.mixer.Sound(Configurations.get_keyboard_sound()) #Aquí nosotros cargamos el sonido del teclado.
        self._results_sound = pygame.mixer.Sound(Configurations.get_results_sound()) #Aquí nosotros cargamos el sonido del resultado.

    @classmethod
    def play_music(cls, volume) -> None:
        """
        Reproduce la música del juego en bucle con el volumen especificado
        """
        pygame.mixer.music.play(loops=-1) #Aquí nosotros activamos la música en bucle
        pygame.mixer.music.set_volume(volume)

    @classmethod
    def music_fadeout(cls, time) -> None:
        """
        Realiza un desvanecimiento de la música.
        :param time: Tiempo del desvanecimiento en milisegundos.
        """
        pygame.mixer.music.fadeout(time)

    def play_keyboard_sound(self) -> None:
        """
        Reproduce el efecto de sonido al seleccionar una casilla.
        """
        self._keyboard_sound.play()

    def play_results_sound(self) -> None:
        """
        Reproduce el efecto de sonido del resultado.
        """
        self._results_sound.play()
