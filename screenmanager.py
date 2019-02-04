import pygame


class ScreenManager:
    def __init__(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(size)

    def displayElements(self, elements):
        screen.fill(0, 0, 0)
        for elem in elements:
            elem.draw(self.screen)
        pygame.display.flip()
