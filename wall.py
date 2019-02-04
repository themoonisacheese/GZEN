import pygame
from collisionObject import CollisionObject
from animationAggregator import aggregateAnim

class Wall(CollisionObject):
    def __init__(self, gridPosition):
        position = gridPosition[0] * 32, gridPosition[1] * 32 #multiply 32 by the scaling factor once decided
        CollisionObject.__init__(self, position, aggregateAnim('sprites/bat/', 'bat_'), 0.001)
        #do texture scaling stuff here.
