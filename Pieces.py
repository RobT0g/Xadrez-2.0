import pygame

pygame.init()

def getTransparentSurf(dimension):
    s = pygame.Surface(dimension).convert_alpha()
    s.fill((0, 0, 0, 0))
    return s

class BasePiece:
    def __init__(self, isWhite, pos) -> None:
        self.isWhite = isWhite
        self.pos = pos
        self.loadImage()
        #self.updateMoveBox()
    
    def loadImage(self):
        self.image = pygame.image.load(f'''images/{self.__class__.__name__}{'W' if self.isWhite else 'B'}.png''')

    def moveTo(self, newPos):
        if newPos in self.moves + self.atacks:
            self.pos = newPos
            self.updateMoveBox()
            return True
        return False

    def getMoveBox(self):
        pass


class PawnW(BasePiece):
    def loadImage(self):
        self.image = pygame.image.load(f'''images/PawnW.png''')



class PawnB(BasePiece):
    def loadImage(self):
        self.image = pygame.image.load(f'''images/PawnB.png''')


class Bishop(BasePiece):
    pass


class Knight(BasePiece):
    pass


class Rook(BasePiece):
    pass


class Queen(BasePiece):
    pass


class King(BasePiece):
    pass

