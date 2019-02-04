import pygame
import sys
class DisplayableElement:

    draw = True

    @property
    def rect(self):
        return self.texture.get_rect()

    def __init__(self, texPath):
        self.texPath = texPath
        self.texture = pygame.image.load(texPath)

    def draw(self, screen):
        if self.draw:
            screen.blit(self.texture, self.rect)

    def moveto(self, pos):
        self.rect.center = pos

    def move(self, movement):
        self.rect.move(movement)
