import pygame

from bat import Bat
from slime import Slime
from gravityObject import GravityObject
from animationAggregator import aggregateAnim
from upgrades import Upgrades
from chicken import Chicken


class Player(GravityObject):
    timeSinceLastSwing = 0
    facingLeft = True
    walking =False
    score = 0
    inInCutScene = False
    def __init__(self):
        GravityObject.__init__(self, (512, 128), aggregateAnim('sprites/character/', 'idle'), 5)
        self.upgrades = Upgrades()

    def update(self, ticktime, objlist):
        self.timeSinceLastSwing += ticktime/1000.0
        GravityObject.update(self, ticktime, objlist)
        for obj in objlist:
            if obj.__class__.__name__ == 'Room':
                for block in obj.roomBlocks:
                    if self.isColliding(block):
                        if block.__class__.__name__ == 'Coin':
                            self.score += 100
                            block.destroy()
                            obj.roomBlocks.remove(block)
                        elif block.__class__.__name__ == 'Meat':
                            if block.pickupDelay <=0.0:
                                self.score += 200
                                block.destroy()
                                obj.roomBlocks.remove(block)
                        elif block.__class__.__name__ == 'Spike':
                            # remove Score
                            pass
                        # test root class of enemies, to accomodate different enemy levels.
                        elif issubclass(block.__class__, Slime) or issubclass(block.__class__, Bat):
                            if self.isSwingingSword:
                                # damage the enemy
                                block.takeDamage(1)
                                if block.hp <= 0:
                                    obj.roomBlocks.append(Chicken(block.rect.center))
                                    block.destroy()
                                    obj.roomBlocks.remove(block)


                            else:
                                self.score = max(0, self.score - block.damage)

    def flipList(self, listToFlip, flip):
        templist = []
        for frame in listToFlip:
            templist.append(pygame.transform.flip(frame, not flip, False))
        return templist

    def lighHit(self):
        if self.timeSinceLastSwing >= 0.5:
            self.timeSinceLastSwing = 0
            self.isSwingingSword = True
            self.changeAnimationTemp(self.flipList(aggregateAnim('sprites/character/', 'light_attack'), self.facingLeft), 10, stopHitting)

    def heavyHit(self):
        if self.upgrades.heavyHit:
            if self.timeSinceLastSwing >= 0.5:
                self.isSwingingSword = True
                self.timeSinceLastSwing = 0
                self.changeAnimationTemp(self.flipList(aggregateAnim('sprites/character/', 'strong_attack'), self.facingLeft), 10, stopHitting)

    def jump(self):
        if self.isOnTheGround:
            self.addToVec(0, -350 * self.upgrades.jumpingHeight)
            self.changeAnimationTemp(self.flipList(aggregateAnim('sprites/character/', 'jumping'), self.facingLeft), 10)
            stopHitting(self)

    def startWalking(self, left):
        if left:
            self.addToVec(128 * self.upgrades.walkingSpeed, 0)
        else:
            self.addToVec(-128* self.upgrades.walkingSpeed, 0)
        if left != self.facingLeft:
            self.walking = True
            self.facingLeft = left
            self.changeAnimation(self.flipList(aggregateAnim('sprites/character/', 'walking'), left), 5)
            stopHitting(self)

    def startRunning(self, left):
        if left:
            self.addToVec(64* self.upgrades.walkingSpeed, 0)
        else:
            self.addToVec(-64* self.upgrades.walkingSpeed, 0)
        if left != self.facingLeft or self.walking:
            self.walking = False
            self.facingLeft = left
            self.changeAnimation(self.flipList(aggregateAnim('sprites/character/', 'running'), left), 5)
            stopHitting(self)

    def stopMoving(self):
        self.walking = False
        self.changeAnimation(self.flipList(aggregateAnim('sprites/character/', 'idle'), self.facingLeft), 5)
        stopHitting(self)


def stopHitting(obj):
    obj.isSwingingSword = False
