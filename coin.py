import pygame

from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim
class Coin(CollisionObject):
    def __init__(self, gridPos):
        GridAlignedObject.__init__(gridPos, aggregateAnim('sprites/items/', 'coin'))
