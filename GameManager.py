import pygame
import os
from ScreenManager import Screen
import Pieces

class Board:
    def __init__(self) -> None:
        toprow = [0, 1, 2, 3, 4, 2, 1, 0]
        self.typeList = [Pieces.Rook, Pieces.Knight, Pieces.Bishop, Pieces.Queen, Pieces.King]
        self.clickedOn = None
        self.board = [
            [self.typeList[v](False, (k, 0)) for k, v in enumerate(toprow)], 
            [Pieces.PawnB(False, (i, 1)) for i in range(8)], 
            *[[None for j in range(8)] for i in range(4)],
            [Pieces.PawnW(True, (i, 6)) for i in range(8)], 
            [self.typeList[v](True, (k, 7)) for k, v in enumerate(toprow)]]
        self.board[3][3] = Pieces.Bishop(True, (3, 3))
        #self.showBoard()

    def showBoard(self):
        for i in self.board:
            a = [j.__class__.__name__ if j else 'N' for j in i]
            print(a)

    def getClicked(self):
        if self.clickedOn:
            return self.board[self.clickedOn[1]][self.clickedOn[0]]

class Manager:
    def __init__(self) -> None:
        self.board = Board()
        self.screen = Screen(self.board)
        self.clickedOn = None

    def update(self):
        coord = pygame.mouse.get_pos()
        b = self.getInBoard(coord)
        if (self.board.board[b[1]][b[0]]):
            self.board.clickedOn = b
        print(self.board.clickedOn)
        self.screen.setOnScreen()

    def getInBoard(self, coord):
        return ((coord[0]-16)//75, (coord[1]-16)//75)


