import pygame


class ScreenManager:
    def __init__(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(size)



    def displayElements(self, elements):
        black = 0, 0, 0
        self.screen.fill(black)
        for elem in elements:
            elem.draw(self.screen)
        pygame.display.flip()
    def fadeOut(self):
        for i in range(250):
            s = pygame.Surface(self.size)  # the size of your rect
            s.set_alpha(i)                # alpha level
            s.fill((255,255,255))           # this fills the entire surface
            self.screen.blit(s, (0,0))
            pygame.time.delay(30)
            pygame.display.flip()
