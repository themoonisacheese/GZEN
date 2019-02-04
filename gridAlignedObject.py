import pygame
from collisionObject import CollisionObject
from animationAggregator import aggregateAnim

class GridAlignedObject(CollisionObject):
    def __init__(self, gridPosition, animationFrames, animationFrameRate =3):
        if gridPosition[0] >= 16 or gridPosition[1] >= 9:
            raise ValueError('GridPosition is out of screen bounds')
        position = gridPosition[0] * 32 *2, gridPosition[1] * 32*2
        CollisionObject.__init__(self, position, animationFrames, animationFrameRate)

    def moveto(self, pos):
        self.rect.topleft = pos

    def moveAligned(self, gridPos):
        if gridPosition[0] >= 16 or gridPosition[1] >= 9:
            raise ValueError('GridPosition is out of screen bounds')
        position = gridPosition[0] * 32 *2, gridPosition[1] * 32*2
        self.moveto(position)
