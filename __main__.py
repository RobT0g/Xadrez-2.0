import pygame
from GameManager import Manager

def main():
    pygame.init()                       # Init
    man = Manager()                     # Game manager
    pygame.display.flip()               # Update display

    running = True                      # looping variable
    while running:                      # looping
        for e in pygame.event.get():
            if e.type == pygame.MOUSEBUTTONDOWN:
                man.update()
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False

if __name__ == '__main__':
    main()
