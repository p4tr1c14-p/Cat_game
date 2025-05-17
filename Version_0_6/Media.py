"""
Nombre:
Fecha: 15 de mayo del 2025.

Descripción:
En esta versión se incluye la verificación para evitar colocar marcas en casillas ya ocupadas.
Se agregaron imágenes que indican de forma visual a quién le toca el turno (X o O),
y se alternan dinámicamente con cada jugada.
Se implementó la clase TurnImage para manejar este cambio visual y se integraron todas
las configuraciones necesarias en la clase Configurations.
Aún no se incorpora la lógica para detectar al ganador
"""

import pygame
from Configurations import Configurations
from pygame.sprite import Sprite


class Background:
    """
    Clase que contiene el fondo de pantalla
    """

    def __init__(self):
        background_image_path = Configurations.get_background_image_path() #Esto es para tener la ruta de la imagen de fondo desde las configuraciones
        self.image = pygame.image.load(background_image_path)

        #Se escala la imagen al tamaño de la pantalla
        screen_size = Configurations.get_screen_size() #Obtenemos el tamaño de la pantalla definido en las configuraciones
        self.image = pygame.transform.scale(self.image, screen_size) #Escalamos la imagen para que se ajuste al tamaño de la pantalla

        self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface):
        """
        Se utiliza para dibujar el fondo de pantalla
        """
        screen.blit(self.image, self.rect) #Dibujamos la imagen de fondo sobre la superficie de la pantalla

class Turn_image(Sprite):

    turno = "X" #Inicializamos el turno con la letra "X"

    def __init__(self):
        turno = "X" #Reiniciamos el valor de turno a "X" (este valor no afecta al atributo de clase =D)
        super().__init__()

        if Turn_image.turno == "X":
            self.image = pygame.image.load(Configurations.get_image_turno_x()) #Cargamos la imagen que indica que es el turno de "X"
            Turn_image.turno = "O" #Cambiamos el turno a "O" para la siguiente vez
        else:
            self.image = pygame.image.load(Configurations.get_image_turno_o()) #Cargamos la imagen que indica que es el turno de "O"
            Turn_image.turno = "X" #Cambiamos el turno a "X" para la siguiente vez

        self.image = pygame.transform.scale(self.image, (500, 200)) #Escalamos la imagen del turno para que tenga el tamaño adecuado
        self.rect = self.image.get_rect()
        self.rect.centerx = Configurations.get_center_x() #Centramos la imagen horizontalmente
        self.rect.bottom = Configurations.get_bottom_x() #Ajustamos las medidas de la parte inferior de la imagen

class Resultado_image:
    configurations = Configurations()

    def __init__(self, result):
        super().__init__()  # Llamamos al constructor de la clase padre Sprite para inicializar correctamente la marca

        if result == 0:
            self.image = pygame.image.load(Configurations.get_result_image()[result])
            self.rect = self.image.get_rect()
        elif result == 1:
            self.image = pygame.image.load(Configurations.get_result_image()[result])
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.image.load(Configurations.get_result_image()[result])
            self.rect = self.image.get_rect()

    def blit(self, screen: pygame.surface.Surface) -> None:
        """
        Se utiliza para dibujar la manzana
        :param screen: Pantalla en donde se dibujaa
        """
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = 500
        screen.blit(self.image, self.rect)
