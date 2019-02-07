import pygame
from textElement import TextElement

class NpcDialog(TextElement):
    timeLeftInCutscene = 4.0
    alreadycalled = False
    def __init__(self, position, text, callback):
        TextElement.__init__(self, text, 'Calibri', 20)
        self.moveto(position)
        self.__callback = callback

    def animate(self, clocktick):
        self.timeLeftInCutscene -= clocktick/1000.0
        if self.timeLeftInCutscene <= 0 and not self.alreadycalled:
            self.__callback()
            self.setText('')
            self.alreadycalled = True

        TextElement.animate(self, clocktick)
