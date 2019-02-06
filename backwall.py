import pygame
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim

class BackWall(GridAlignedObject):
    def __init__(self, gridPos):
        GridAlignedObject.__init__(self, gridPos, aggregateAnim('sprites/environment/', 'dark_wall'), 0.001)
