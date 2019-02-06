import pygame
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim
import random

class Spike(GridAlignedObject):
    def __init__(self, gridPosition, facing = 0):#0=up, 1=left, 2=down, 3= right
        GridAlignedObject.__init__(self, gridPosition, self.__spinList(aggregateAnim('sprites/environment/', 'spike_f0'), facing), 0.001)
        self.facing = facing

    def animate(self, clocktick):
        if (not self.isInTempAnim) and random.random() > 0.999:
            self.changeAnimationTemp(self.__spinList(aggregateAnim('sprites/environment/', 'spike'), self.facing), 10)
        GridAlignedObject.animate(self, clocktick)

    def __spinList(self, animList, facing):
        tempList = []
        for item in animList:
            tempList.append(pygame.transform.rotate(item, 90*facing))
        return tempList
