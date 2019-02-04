import pygame
from displayableElement import DisplayableElement

class GameObject(DisplayableElement):
     def __init__(self, position, animationFrames, animationFrameRate = 3):
         DisplayableElement.__init__(animationFrames, animationFrameRate)
         self.moveto(position)
