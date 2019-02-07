import pygame
from gravityObject import GravityObject
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim


class Slime(GravityObject, GridAlignedObject):
    hp = 1
    damage = 100
    facingLeft = False
    __timeSinceJump = 0.0
    def __init__(self, startingGridPos):
        GridAlignedObject.__init__(self, startingGridPos, aggregateAnim('sprites/mobs/', 'slime_f'), 3)
        self.move((0,50))


    def update(self,ticktime, objlist):
        self.__timeSinceJump += ticktime/1000.0
        player = None
        for obj in objlist:
            if obj.__class__.__name__ == 'Player':
                player = obj
                break
        if player is not None:
            if self.currentAnimationFrameIndex == 2:
                playerDirection = pygame.math.Vector2( player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery)
                self.facingLeft =not  playerDirection.x <0
                if playerDirection.x < 0:
                    self.changeVec((-100, -200))
                else:
                    self.changeVec((100, -200))
            if self.currentAnimationFrameIndex ==5 :
                self.changeVec((0,300))
                self.__timeSinceJump = 0

        GravityObject.update(self,ticktime, objlist)


    def flipList(self, listToFlip, flip):
        templist = []
        for frame in listToFlip:
            templist.append(pygame.transform.flip(frame, not flip, False))
        return templist

    def changeVec(self, newVec):
        GravityObject.changeVec(self, newVec)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime_f'), (self.facingLeft))

    def addToVec(self, x, y):
        GravityObject.addToVec(self, x, y)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'slime_f'), (self.facingLeft))
