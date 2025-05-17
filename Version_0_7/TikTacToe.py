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

class TicTacToeMark(Sprite):
    """
    Clase que representa una marca en el tablero de Tic Tac Toe (X o O).
    Alterna dinámicamente las imágenes según el turno actual.
    """
    configurations = Configurations()
    turno = "X" #Inicializamos el turno en "X" para que sea la primera marca en colocarse.

    def __init__(self, casilla):
        """
        Constructor que coloca una marca (X o O) en la casilla indicada,
        alternando el turno y ajustando la imagen y posición
        """
        super().__init__() #Llamamos al constructor de la clase padre Sprite para inicializar correctamente la marca

        if TicTacToeMark.turno == "X":
            self.image = pygame.image.load(Configurations.get_mark_X()) #Cargamos la imagen correspondiente a la marca X
            TicTacToeMark.turno = "O" #Cambiamos el turno a "O" para la siguiente jugada
        else:
            self.image = pygame.image.load(Configurations.get_mark_O()) #Cargamos la imagen correspondiente a la marca O
            TicTacToeMark.turno = "X" #Cambiamos el turno a "X" para la siguiente jugada

        self.image = pygame.transform.scale(self.image, Configurations.get_size_block()) #Ajustamos el tamaño de la imagen al tamaño de bloque definido

        self.rect = self.image.get_rect() #Obtenemos el rectángulo de la imagen para poder posicionarla
        self.rect.center = TicTacToeMark.configurations.get_posiciones().get(casilla, (0, 0)) #Colocamos la marca en el centro de la casilla seleccionada
