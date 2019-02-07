import pygame

from movingObject import MovingObject
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim


class Slime(MovingObject, GridAlignedObject):
    hp = 1
    damage = 50
    speed = 80
    scanningInterval = 1.0
    __timesinceLastDirChange = 0.0

    def __init__(self, startingGridPos):
        GridAlignedObject.__init__(self, startingGridPos, aggregateAnim('sprites/mobs/', 'slime_f'), 20)
        self.move((0, 60))
        pass

    def takeDamage(self, dmg):
        self.hp = self.hp - dmg
        pass

    def flipList(self, listToFlip, flip):
        templist = []
        for frame in listToFlip:
            templist.append(pygame.transform.flip(frame, flip, False))
        return templist

    def update(self, ticktime, objlist):
        pass

    def changeVec(self, newVec):
        MovingObject.changeVec(self, newVec)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime_f'), (self.movementVector[0] > 0))

    def addToVec(self, x, y):
        MovingObject.addToVec(self, x, y)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime_f'), (self.movementVector[0] > 0))
