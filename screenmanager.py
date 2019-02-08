import pygame


class ScreenManager:
    timesincelastfade = 0
    currentFadeIndex = 0
    def __init__(self, size):
        self.size = size
        self.screen = pygame.display.set_mode(size)



    def displayElements(self, elements):
        black = 0, 0, 0
        self.screen.fill(black)
        for elem in elements:
            elem.draw(self.screen)
        pygame.display.flip()

    def fadeOut(self, ticktime):
        self.timesincelastfade += ticktime
        if self.timesincelastfade > 100:
            self.timesincelastfade = 0
            self.currentFadeIndex  = min(255, self.currentFadeIndex +1)
            s = pygame.Surface(self.size)  # the size of your rect
            s.set_alpha(self.currentFadeIndex)                # alpha level
            s.fill((255,255,255))           # this fills the entire surface
            self.screen.blit(s, (0,0))
            pygame.display.flip()
