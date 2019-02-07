import pygame
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim

class Spring(GridAlignedObject):
    def __init__(self, gridPos):
        GridAlignedObject.__init__(self, gridPos, aggregateAnim('sprites/environment/', 'spring_f0'), 0.001)


    def use(self):
        self.changeAnimationTemp(aggregateAnim('sprites/environment/', 'spring'), 3)
