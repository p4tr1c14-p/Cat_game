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

class TicTacToeMark(Sprite):
    """
    Clase que representa las marcas X y O que se colocan en el tablero.
    Hereda de Sprite para integrarse con los grupos de sprites de pygame.
    Alterna automáticamente entre X y O en cada creación de instancia.
    Posiciona las marcas en las coordenadas correspondientes a la casilla seleccionada.
    """
    configurations = Configurations()
    turno = "X"  # Inicializamos el turno en "X" para que sea la primera marca en colocarse.

    def __init__(self, casilla):
        """
        Inicializa una nueva marca en el tablero.

        Crea una marca X u O dependiendo del turno actual y la posiciona
        en la casilla especificada del tablero.

        Args:
            casilla: Número de casilla donde se colocará la marca (1-9).
        """
        super().__init__()  # Llamamos al constructor de la clase padre Sprite para inicializar correctamente la marca.

        # Determinamos qué marca colocar según el turno actual.
        if TicTacToeMark.turno == "X":
            self.image = pygame.image.load(Configurations.get_mark_X())
            TicTacToeMark.turno = "O"
        else:
            self.image = pygame.image.load(Configurations.get_mark_O())
            TicTacToeMark.turno = "X"  # Cambiamos el turno a "X" para la siguiente jugada.

        self.image = pygame.transform.scale(self.image, Configurations.get_size_block())

        self.rect = self.image.get_rect()
        self.rect.center = TicTacToeMark.configurations.get_posiciones().get(casilla, (0, 0))  # Colocamos la marca en el centro de la casilla seleccionada.
