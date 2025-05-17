"""
Nombre: Equipo los Bugs.
Fecha: 16 de mayo del 2025.

Descripción:
En esta versión se implementó la lógica para determinar al ganador del juego.
Se añadió la función check_winner() para detectar si ganó el jugador X, O o si hubo empate.
También se agregó una pantalla de resultados y créditos, mostrando una imagen dependiendo del resultado.
Por último, se incluyó la función game_over_screen() para mostrar el resultado final usando animaciones
simples y redibujado de pantalla.
"""

import pygame
from Configurations import Configurations
from pygame.sprite import Sprite


class Background:
    """
    Clase que contiene el fondo de pantalla del juego.
    Carga y escala la imagen de fondo según las configuraciones establecidas.
    Proporciona para dibujar el fondo en la pantalla.
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path()
        self.image = pygame.image.load(background_image_path)

        #Se escala la imagen al tamaño de la pantalla
        screen_size = Configurations.get_screen_size()
        self.image = pygame.transform.scale(self.image, screen_size)

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla en la superficie proporcionada
        
        Args:
            screen: Superficie de pygame donde se dibujará el fondo
        """
        screen.blit(self.image, self.rect) #Dibujamos la imagen de fondo sobre la superficie de la pantalla


class Turn_image(Sprite):
    """
    Clase que maneja la imagen indicadora del turno actual (X u O)
    Hereda de Sprite para integrarse con los grupos de sprites de pygame
    Alterna entre las imágenes de turno X y turno O de manera automática
    """

    turno = "X" #Inicializamos el turno con la letra "X"

    def __init__(self):
        turno = "X" #Reiniciamos el valor de turno a "X" (este valor no afecta al atributo de clase =D)
        super().__init__() #Inicializamos la clase padre Sprite

        if Turn_image.turno == "X":
            self.image = pygame.image.load(Configurations.get_image_turno_x()) #Cargamos la imagen que indica que es el turno de "X"
            Turn_image.turno = "O" #Cambiamos el turno a "O" para la siguiente vez
        else:
            self.image = pygame.image.load(Configurations.get_image_turno_o()) #Cargamos la imagen que indica que es el turno de "O"
            Turn_image.turno = "X" #Cambiamos el turno a "X" para la siguiente vez

        self.image = pygame.transform.scale(self.image, (600, 150))
        self.rect = self.image.get_rect()
        self.rect.centerx = Configurations.get_center_x() #Centramos la imagen horizontalmente
        self.rect.bottom = Configurations.get_bottom_x() #Ajustamos las medidas de la parte inferior de la imagen


class Resultado_image:
    """
    Clase que maneja las imágenes de resultado del juego (victoria X, victoria O, empate)
    Carga la imagen apropiada según el resultado proporcionado y la posiciona en pantalla
    """
    def __init__(self, result):
        """
        Inicializa la imagen de resultado según el ganador
        
        Args:
            result: Valor que indica el resultado (0=X ganó, 1=O ganó, 2=empate)
        """
        #Cargamos la imagen de resultado correspondiente
        if result == 0:
            self.image = pygame.image.load(Configurations.get_result_image()[result]) #Imagen de victoria para X
            self.rect = self.image.get_rect()
        elif result == 1:
            self.image = pygame.image.load(Configurations.get_result_image()[result]) #Imagen de victoria para O
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load(Configurations.get_result_image()[result]) #Imagen de empate
            self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Dibuja la imagen de resultado en la pantalla, centrada horizontalmente
        
        Args:
            screen: Superficie de pygame donde se dibujará la imagen
        """
        self.rect.centerx = screen.get_rect().centerx #Centramos la imagen horizontalmente
        self.rect.bottom = 400 #Posicionamos la imagen a una altura específica
        screen.blit(self.image, self.rect) #Dibujamos la imagen en la pantalla


class CreditsIma:
    """
    Clase que maneja la imagen de créditos del juego
    Carga la imagen de créditos y la posiciona en la parte inferior de la pantalla
    """
    def __init__(self):
        """
        Inicializa la imagen de créditos
        """
        self.image = pygame.image.load("../media/Creditos_Gato.png")
        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Dibuja la imagen de créditos en la pantalla, centrada horizontalmente
        
        Args:
            screen: Superficie de pygame donde se dibujarán los créditos
        """
        self.rect.centerx = screen.get_rect().centerx #Centramos la imagen horizontalmente
        self.rect.bottom = 800 #Posicionamos la imagen en la parte inferior
        screen.blit(self.image, self.rect) #Dibujamos la imagen en la pantalla