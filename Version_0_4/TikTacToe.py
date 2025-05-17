"""
Nombre: Equipo los Bugs.
Fecha: 14 de mayo del 2025.

Descripción:
Se agregaron marcas X y O con imágenes al juego.
Se creó clase TicTacToeMark que muestra la imagen correspondiente según el turno del jugador.
El juego responde a teclas q,w,e,a,s,d,z,x y c para colocar marcas en las 9 casillas.
Aún falta implementar la lógica completa del juego que impida colocar marcas sobre otras ya existentes.
"""

import pygame
from Configurations import Configurations
from pygame.sprite import Sprite


class TicTacToeMark(Sprite):  #Creamos una clase para representar cada marca como un sprite.
    configurations = Configurations()
    turno = "X"  #Inicializamos el turno con la letra "X".

    def __init__(self, casilla):
        super().__init__()

        #Dependiendo del turno, cargamos la imagen correspondiente y alternamos el turno.
        if TicTacToeMark.turno == "X":
            self.image = pygame.image.load(Configurations.get_mark_X())
            TicTacToeMark.turno = "O"  #Cambiamos el turno a O.
        else:
            self.image = pygame.image.load(Configurations.get_mark_O())  #Cargamos la imagen de la O.
            TicTacToeMark.turno = "X"  #Cambiamos el turno a X.

        #Escalamos la imagen para que se ajuste al tamaño de cada celda.
        self.image = pygame.transform.scale(self.image, Configurations.get_size_block())

        self.rect = self.image.get_rect()

        #Colocamos la marca en el centro de la celda correspondiente.
        self.rect.center = TicTacToeMark.configurations.get_posiciones().get(casilla, (0, 0))
