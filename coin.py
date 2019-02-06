import pygame

from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim
class Coin(GridAlignedObject):
    def __init__(self, gridPos):
        GridAlignedObject.__init__(self, gridPos, aggregateAnim('sprites/items/', 'coin'))
