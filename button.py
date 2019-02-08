import pygame
from animationAggregator import aggregateAnim
from displayableElement import DisplayableElement
class Button(DisplayableElement):
    def __init__(self,pos, animpath, animfile, callback):
        DisplayableElement.__init__(self, aggregateAnim(animpath, animfile), 0.001)
        self.moveto(pos)
        self.__callback = callback

    def click(self):
        self.__callback()
