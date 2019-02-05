import pygame
from displayableElement import DisplayableElement

class TextElement(DisplayableElement): #enjoys the moving methods of DisplayableElement
    def __init__(self, text, font, fontsize, color=(255,255,255)):
        self.font = pygame.font.SysFont(font, fontsize)
        self.color = color
        self.text = text
        tex = [self.font.render(text, True, color)]
        DisplayableElement.__init__(self, tex, 0.001)

    def setText(self, newText):
        self.text = newText
        tex = [self.font.render(newText, True, self.color)]
        self.changeAnimation(tex, 0.001)

    def setColor(self, color):
        self.color = color
        self.setText(self.text)

    def setFont(self, font, fontsize):
        self.font = pygame.font.SysFont(font, fontsize)
        self.setText(self.text)

    def animate(self, clocktick):
        pass
