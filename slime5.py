import pygame
from slime import Slime
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim
class Slime5(Slime):
    hp = 50
    damage = 500
    facingLeft = False
    __timeSinceJump = 0.0
    def __init__(self, startingGridPos):
        GridAlignedObject.__init__(self, startingGridPos, aggregateAnim('sprites/mobs/', 'slime color swap purple'), 3)
        self.move((0,50))
    def changeVec(self, newVec):
        GravityObject.changeVec(self, newVec)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime color swap purple'), (self.facingLeft))

    def addToVec(self, x, y):
        GravityObject.addToVec(self, x, y)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime color swap purple'), (self.facingLeft))
