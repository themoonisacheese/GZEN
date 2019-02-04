import pygame
from displayableElement import DisplayableElement

class GameObject(DisplayableElement):
    def __init__(self, position, animationFrames, animationFrameRate = 3):
        DisplayableElement.__init__(self.animationFrames, self.animationFrameRate)
        self.draw = False

    def instantiate(self):
        self.draw = True

    def destroy(self):#NB: ne detruit pas l'object python.
        self.draw = False
        self.animationFrames = []
        self.animationFrameRate = 0
        self.currentTexture = None
