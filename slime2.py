import pygame
from slime import Slime
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim
from gravityObject import GravityObject
class Slime2(Slime):
    hp = 20
    damage = 200
    facingLeft = False
    __timeSinceJump = 0.0
    def __init__(self, startingGridPos):
        GridAlignedObject.__init__(self, startingGridPos, aggregateAnim('sprites/mobs/', 'slime swap color blue'), 3)
        self.move((0,50))
    def changeVec(self, newVec):
        GravityObject.changeVec(self, newVec)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime swap color blue'), (self.facingLeft))

    def addToVec(self, x, y):
        GravityObject.addToVec(self, x, y)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime swap color blue'), (self.facingLeft))
