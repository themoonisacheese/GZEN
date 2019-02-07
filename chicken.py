import pygame

from gravityObject import GravityObject
from animationAggregator import aggregateAnim
class Chicken(GravityObject):
    pickupDelay = 1.0
    def __init__(self, startingPos):
        GravityObject.__init__(self, startingPos, aggregateAnim('sprites/items/', 'meat'), 4)
        self.display = True

    def update(self, clocktick, objlist):
        self.pickupDelay -= clocktick/1000.0
        GravityObject.update(self, clocktick, objlist)
