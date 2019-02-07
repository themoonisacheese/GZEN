import pygame

from gravityobject import GravityObject
from animationAggregator import aggregateAnim
class Chicken(GravityObject):
    def __init__(self, gridPos):
        GridAlignedObject.__init__(self, gridPos, aggregateAnim('sprites/items/', 'meat'), 4)
