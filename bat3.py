import pygame
from bat import Bat
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim
from movingObject import MovingObject
class Bat3(Bat) :
    hp = 30
    damage = 300
    speed = 180
    scanningInterval = 0.8
    __timesinceLastDirChange = 0.0
    def __init__(self, startingGridPos):
        GridAlignedObject.__init__(self, startingGridPos, aggregateAnim('sprites/mobs/', 'bat color-swap-red'), 20)
        self.move((0, 60))
    def changeVec(self, newVec):
        MovingObject.changeVec(self, newVec)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'bat color-swap-red'), (self.movementVector[0] > 0))

    def addToVec(self, x, y):
        MovingObject.addToVec(self, x, y)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'bat color-swap-red'), (self.movementVector[0] > 0))
