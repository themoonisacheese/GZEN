import pygame
from bat import Bat
class Bat5(Bat) :
    hp = 50
    damage = 500
    speed = 160
    scanningInterval = 0.6
    __timesinceLastDirChange = 0.0
    def __init__(self, startingGridPos):
        GridAlignedObject.__init__(self, startingGridPos, aggregateAnim('sprites/mobs/', 'bat color-swap-green'), 20)
        self.move((0, 60))
    def changeVec(self, newVec):
        MovingObject.changeVec(self, newVec)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'bat color-swap-green'), (self.movementVector[0] > 0))

    def addToVec(self, x, y):
        MovingObject.addToVec(self, x, y)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'bat color-swap-green'), (self.movementVector[0] > 0))
