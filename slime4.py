import pygame
from slime import Slime
class Slime4(Slime):
    hp = 40
    damage = 400
    facingLeft = False
    __timeSinceJump = 0.0
    def __init__(self, startingGridPos):
        GridAlignedObject.__init__(self, startingGridPos, aggregateAnim('sprites/mobs/', 'slime color swap red'), 3)
        self.move((0,50))
    def changeVec(self, newVec):
        GravityObject.changeVec(self, newVec)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime color swap red'), (self.facingLeft))

    def addToVec(self, x, y):
        GravityObject.addToVec(self, x, y)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime color swap red'), (self.facingLeft))