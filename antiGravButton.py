import pygame
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim

class Button(GridAlignedObject):
    def __init__(self, gridPos):
        GridAlignedObject.__init__(self, gridPos, aggregateAnim('sprites/environment', 'button_Animation 1_0'), 0.001)

    def use(self):
        self.changeAnimationTemp(aggregateAnim('sprites/environment', 'button_Animation 1_1'), 0.25)
