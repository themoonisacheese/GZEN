import pygame
from animationAggregator import aggregateAnim
from gridAlignedObject import GridAlignedObject

class Wall(GridAlignedObject):
    def __init__(self, gridPosition):
        #TODO:randomly assign cracked wall texture
        GridAlignedObject.__init__(self, gridPosition, aggregateAnim('sprites/murs/', 'mur simple'), 0.001)
