"""
Nombre: Equipo los Bugs
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

class TicTacToeMark(Sprite):
    configurations = Configurations()
    turno = "X" #Inicializamos el turno en "X" para que sea la primera marca en colocarse

    def __init__(self, casilla):
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
