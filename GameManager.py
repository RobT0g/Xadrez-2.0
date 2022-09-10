import pygame
import os
from ScreenManager import Screen
import Pieces

class Board:
    def __init__(self) -> None:
        empetyrow = [None for i in range(8)]
        toprow = [0, 1, 2, 3, 4, 2, 1, 0]
        self.typeList = [Pieces.Rook, Pieces.Knight, Pieces.Bishop, Pieces.Queen, Pieces.King]
        self.board = [
            [self.typeList[v](False, (k, 0)) for k, v in enumerate(toprow)], 
            [Pieces.PawnB(False, (i, 1)) for i in range(8)], 
            *[empetyrow for i in range(4)],
            [Pieces.PawnW(True, (i, 1)) for i in range(8)], 
            [self.typeList[v](True, (k, 0)) for k, v in enumerate(toprow)]]


class Manager:
    def __init__(self) -> None:
        self.board = Board()
        self.screen = Screen(self.board)

    def update(self):
        pass

    def getMousePos():
        pass


