import pygame

pygame.init()

class Screen:
    def __init__(self, board) -> None:
        self.board = board
        self.dimensions = (75*8+32, 75*8+32)
        self.display = pygame.display.set_mode(self.dimensions)
        pygame.display.set_caption('Chess')
        self.createFrame()
        self.setOnScreen()

    def createFrame(self):
        self.frame = pygame.Surface(((d:=self.dimensions[0]), d))
        pygame.draw.rect(self.frame, (0, 0, 0), pygame.Rect(0, 0, d, d), 1)
        pygame.draw.rect(self.frame, (132, 86, 43), pygame.Rect(1, 1, d-2, d-2), 14)
        pygame.draw.rect(self.frame, (0, 0, 0), pygame.Rect(15, 15, d-30, d-30), 1)
        tiles = [pygame.Surface((75, 75)) for i in range(2)]
        pygame.draw.rect(tiles[0], (0, 0, 0), pygame.Rect(0, 0, 75, 75), 1)
        pygame.draw.rect(tiles[0], (55, 71, 79), pygame.Rect(1, 1, 73, 73))
        pygame.draw.rect(tiles[1], (0, 0, 0), pygame.Rect(0, 0, 75, 75), 1)
        pygame.draw.rect(tiles[1], (162, 116, 73), pygame.Rect(1, 1, 73, 73))
        for i in range(8):
            for j in range(8):
                self.frame.blit(tiles[(i%2) == (j%2)], (i*75+16, j*75+16))

    def setOnScreen(self):
        self.display.blit(self.frame, (0, 0))
        for k1, v1 in enumerate(self.board.board):
            for k2, v2 in enumerate(v1):
                if v2:
                    self.display.blit(v2.image, self.getBoardCoord(k2, k1))
        pygame.display.flip()

    def getBoardCoord(self, *coord):
        print(coord)
        return (coord[0]*75+16, coord[1]*75+16)

    def update(self):
        pass
