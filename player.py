import pygame

from bat import Bat
from gravityObject import GravityObject
from animationAggregator import aggregateAnim
from slime import Slime


class Player(GravityObject):
    timeSinceLastSwing = 0
    facingLeft = True

    def __init__(self):
        GravityObject.__init__(self, (512, 128), aggregateAnim('sprites/character/', 'idle'), 5)

    def update(self, ticktime, objlist):
        self.timeSinceLastSwing += ticktime/1000.0
        GravityObject.update(self, ticktime, objlist)
        for obj in objlist:
            if obj.__class__.__name__ == 'Room':
                for block in obj.roomBlocks:
                    if self.isColliding(block):
                        if block.__class__.__name__ == 'Coin':
                            # add score, delete the coin
                            pass
                        elif block.__class__.__name__ == 'Meat':
                            # add score, delete the meat
                            pass
                        elif block.__class__.__name__ == 'Spike':
                            # remove Score
                            pass
                        # test root class of enemies, to accomodate different enemy levels.
                        elif issubclass(block.__class__, Slime) or issubclass(block.__class__, Bat):
                            if self.isSwingingSword:
                                # damage the enemy
                                block.takeDamage(1)
                                print(str(block.hp))
                                if block.hp <= 0:
                                    block.display = False
                                pass
                            else:
                                # remove score, knockback?
                                pass

    def flipList(self, listToFlip, flip):
        templist = []
        for frame in listToFlip:
            templist.append(pygame.transform.flip(frame, flip, False))
        return templist

    def lighHit(self, left):
        self.facingLeft = left
        if self.timeSinceLastSwing >= 0.5:
            self.timeSinceLastSwing = 0
            self.isSwingingSword = True
            self.changeAnimationTemp(self.flipList(aggregateAnim('sprites/character/', 'light_attack'), left), 10, stopHitting)

    def heavyHit(self):
        if self.upgrades.heavyHit:
            if self.timeSinceLastSwing >= 0.5:
                self.isSwingingSword = True
                self.timeSinceLastSwing = 0
                self.changeAnimationTemp(self.flipList(aggregateAnim('sprites/character/', 'strong_attack'), self.facingLeft), 10, stopHitting)

    def jump(self):
        if self.isOnTheGround:
            self.addToVec(0, -300)  # * self.upgrades.jumpingHeight
            self.changeAnimationTemp(self.flipList(aggregateAnim('sprites/character/', 'jumping'), self.facingLeft), 10)
            stopHitting(self)

    def startWalking(self, left):
        self.facingLeft = left
        self.changeAnimation(self.flipList(aggregateAnim('sprites/character/', 'walking'), left), 5)
        stopHitting(self)

    def startRunning(self, left):
        self.facingLeft = left
        self.changeAnimation(self.flipList(aggregateAnim('sprites/character/', 'running'), left), 5)
        stopHitting(self)

    def stopMoving(self, left):
        self.facingLeft = left
        self.changeAnimation(self.flipList(aggregateAnim('sprites/character/', 'idle'), left), 5)
        stopHitting(self)


def stopHitting(obj):
    obj.isSwingingSword = False
