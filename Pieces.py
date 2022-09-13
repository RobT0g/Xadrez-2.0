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
        self.moves = []
        self.atacks = []
        self.loadImage()
    
    def loadImage(self):
        self.image = pygame.image.load(f'''images/{self.__class__.__name__}{'W' if self.isWhite else 'B'}.png''')

    def moveTo(self, newPos):
        if newPos in self.moves + self.atacks:
            self.pos = newPos
            self.updateMoveBox()
            return True
        return False
    
    def getLimits(self, line):
        if line:
            return [[i for i in range(self.pos[0])], [i for i in range(self.pos[0]+1, 8)], 
                [i for i in range(self.pos[1])], [i for i in range(self.pos[1]+1, 8)]]
        return [min((p:=self.pos)), min([7-p[0], p[1]]), min([7-p[0], 7-p[1]]), min([p[0], 7-p[1]])]



class PawnW(BasePiece):
    def loadImage(self):
        self.image = pygame.image.load(f'''images/PawnW.png''')
    
    def getMoveBox(self):
        p = self.pos
        return ([(p[0], p[1]-1)] + [(p[0], p[1]-2)] if p[1] == 6 else [], [(p[0]+1, p[1]-1), (p[0]-1, p[1]-1)])



class PawnB(BasePiece):
    def loadImage(self):
        self.image = pygame.image.load(f'''images/PawnB.png''')

    def getMoveBox(self):
        p = self.pos
        return ([(p[0], p[1]+1)] + [(p[0], p[1]+2)] if p[1] == 6 else [], [(p[0]+1, p[1]+1), (p[0]-1, p[1]+1)])


class Bishop(BasePiece):
    #REVE A ORGANIZAÇÃO DO TABULEIRO TO CONFUNDINDO LINHA COM COLUNA
    def getMoveBox(self):
        p = self.pos
        diag = self.getLimits(False)
        return [[(p[0]-i, p[1]-i) for i in range(diag[0])],
            [(p[0]+i, p[1]-i) for i in range(diag[0])],
            [(p[0]+i, p[1]+i) for i in range(diag[0])],
            [(p[0]-i, p[1]+i) for i in range(diag[0])]]


class Knight(BasePiece):
    pass


class Rook(BasePiece):
    pass


class Queen(BasePiece):
    pass


class King(BasePiece):
    pass


x = Bishop(True, (2, 3))
print(x.getLimits(False))
