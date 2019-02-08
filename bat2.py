import pygame
from bat import Bat
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim
from movingObject import MovingObject

class Bat2(Bat) :
    hp = 20
    damage = 200
    speed = 170
    scanningInterval = 0.9
    __timesinceLastDirChange = 0.0
    def __init__(self, startingGridPos):
        GridAlignedObject.__init__(self, startingGridPos, aggregateAnim('sprites/mobs/', 'bat color-swap-blue'), 20)
        self.move((0, 60))
    def changeVec(self, newVec):
        MovingObject.changeVec(self, newVec)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'bat color-swap-blue'), (self.movementVector[0] > 0))

    def addToVec(self, x, y):
        MovingObject.addToVec(self, x, y)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'bat color-swap-blue'), (self.movementVector[0] > 0))
