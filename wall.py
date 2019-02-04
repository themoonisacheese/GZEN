import pygame
from animationAggregator import aggregateAnim
from gridAlignedObject import GridAlignedObject

class Wall(GridAlignedObject):
    def __init__(self, gridPosition):
        GridAlignedObject.__init__(self, gridPosition, aggregateAnim('sprites/murs/', 'mur simple'), 0.001)
        #do texture scaling stuff here.
