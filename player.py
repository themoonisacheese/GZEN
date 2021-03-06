import pygame

from bat import Bat
from slime import Slime
from gravityObject import GravityObject
from animationAggregator import aggregateAnim
from upgrades import Upgrades
from chicken import Chicken
from room import Room
from npcdialog import NpcDialog


class Player(GravityObject):
    timeSinceLastSwing = 0
    facingLeft = True
    walking =False
    score = 0
    isInCutScene = False
    invincibleTimeLeft = 0
    gravity = 1.0
    nextLevel = False
    respawn = False
    timeUntilGravChange = 0.0
    isSwingingSword = False
    __BossRoom = None
    __bossobj = None
    def __init__(self):
        GravityObject.__init__(self, (512, 128), aggregateAnim('sprites/character/', 'idle'), 5)
        self.upgrades = Upgrades()

    def nextBossDialog(self):
        str = self.__bossobj.nextDialogue()
        if str != '':
            self.__BossRoom.roomBlocks.append(NpcDialog((self.__bossobj.rect.centerx, self.__bossobj.rect.top -10), self.__bossobj.nextDialogue(), self.nextBossDialog))
        else:
            self.stopCutscene()

    def update(self, ticktime, objlist):
        self.timeSinceLastSwing += ticktime/1000.0
        self.invincibleTimeLeft -= ticktime/1000.0
        self.timeUntilGravChange -= ticktime/1000.0
        GravityObject.update(self, ticktime, objlist, self.gravity)
        for obj in objlist:
            if obj.__class__.__name__ == 'Room':
                for block in obj.roomBlocks:
                    if self.respawn and block.__class__.__name__ == 'SpawnPoint':
                        self.respawn = False
                        self.changeVec((0,0))
                        self.moveto(block.rect.center)
                    elif block.__class__.__name__ == 'Wall' and self.nextLevel and block.rect.collidepoint(self.rect.centerx, self.rect.top - 4):
                        self.nextLevel = False
                        self.respawn = True
                        index = objlist.index(obj)
                        objlist[index] = Room(0, obj.floorNumber +1)
                        if obj.floorNumber+1 == 4:
                            self.setGravity(-1.0)
                        else:
                            self.setGravity(1.0)
                        objlist[index].show(True)
                        break;
                    elif block.__class__.__name__ == 'Boss':
                        if not block.alreadyTalked:
                            self.changeVec((0,0))
                            self.isInCutScene = True
                            block.alreadyTalked = True
                            self.__BossRoom = obj
                            self.__bossobj = block
                            obj.roomBlocks.append(NpcDialog((block.rect.centerx, block.rect.top -200), block.nextDialogue(), self.nextBossDialog))
                    if self.isColliding(block):
                        if block.__class__.__name__ == 'Coin':
                            self.score = self.score + 100
                            block.destroy()
                            obj.roomBlocks.remove(block)
                        elif block.__class__.__name__ == 'Chicken':
                            if block.pickupDelay <= 0.0:
                                self.score = self.score + 200
                                block.destroy()
                                obj.roomBlocks.remove(block)
                        elif block.__class__.__name__ == 'Spike':
                                self.takeDamage(200)
                        elif block.__class__.__name__ == 'Spring':
                            self.addToVec(0, -800)
                            self.nextLevel = True
                            block.use()
                        elif block.__class__.__name__ == 'Button':
                            if self.timeUntilGravChange <= 0.0:
                                self.timeUntilGravChange = 2.0
                                self.setGravity(-self.gravity)
                                block.use()
                        elif block.__class__.__name__ == 'PNJ':
                            if not block.alreadyTalked and not self.upgrades.earPods:
                                self.changeVec((0,0))
                                self.isInCutScene = True
                                obj.roomBlocks.append(NpcDialog((block.rect.centerx, block.rect.top -10), block.getDialogue(), self.stopCutscene))


                        # test root class of enemies, to accomodate different enemy levels.
                        elif issubclass(block.__class__, Slime) or issubclass(block.__class__, Bat):
                            if self.isSwingingSword:
                                # damage the enemy
                                block.takeDamage(self.upgrades.attackMultiplier)
                                if block.hp <= 0:
                                    obj.roomBlocks.append(Chicken(block.rect.center))
                                    block.destroy()
                                    obj.roomBlocks.remove(block)
                            else:
                                self.takeDamage(block.damage)

    def stopCutscene(self):
        self.isInCutScene = False

    def flipList(self, listToFlip, flip, gravity):
        boolgrav = gravity < 0
        templist = []
        for frame in listToFlip:
            templist.append(pygame.transform.flip(frame, not flip, boolgrav))
        return templist

    def lighHit(self):
        if self.timeSinceLastSwing >= 0.5:
            self.timeSinceLastSwing = 0
            self.isSwingingSword = True
            self.changeAnimationTemp(self.flipList(aggregateAnim('sprites/character/', 'light_attack'), self.facingLeft, self.gravity), 10, stopHitting)

    def heavyHit(self):
        if self.upgrades.heavyHit:
            if self.timeSinceLastSwing >= 0.5:
                self.isSwingingSword = True
                self.timeSinceLastSwing = 0
                self.changeAnimationTemp(self.flipList(aggregateAnim('sprites/character/', 'strong_attack'), self.facingLeft, self.gravity), 10, stopHitting)

    def jump(self):
        if self.isOnTheGround and not self.isInCutScene:
            self.addToVec(0, -350 * self.upgrades.jumpingHeight * self.gravity)
            self.changeAnimationTemp(self.flipList(aggregateAnim('sprites/character/', 'jumping'), self.facingLeft, self.gravity), 10)
            stopHitting(self)

    def startWalking(self, left):
        if not self.isInCutScene:
            if left:
                self.addToVec(128 * self.upgrades.walkingSpeed, 0)
            else:
                self.addToVec(-128* self.upgrades.walkingSpeed, 0)
            if left != self.facingLeft:
                self.walking = True
                self.facingLeft = left
                self.changeAnimation(self.flipList(aggregateAnim('sprites/character/', 'walking'), left, self.gravity), 5)
                stopHitting(self)

    def startRunning(self, left):
        if not self.isInCutScene:
            if left:
                self.addToVec(64* self.upgrades.walkingSpeed, 0)
            else:
                self.addToVec(-64* self.upgrades.walkingSpeed, 0)
            if left != self.facingLeft or self.walking:
                self.walking = False
                self.facingLeft = left
                self.changeAnimation(self.flipList(aggregateAnim('sprites/character/', 'running'), left, self.gravity), 5)
                stopHitting(self)

    def stopMoving(self):
        self.walking = False
        self.changeAnimation(self.flipList(aggregateAnim('sprites/character/', 'idle'), self.facingLeft, self.gravity), 5)
        stopHitting(self)

    def takeDamage(self, amount):
        if self.invincibleTimeLeft <=0:
            self.score = max(0, self.score - amount)
            self.invincibleTimeLeft = 2.0

    def setGravity(self, gravity):
        self.gravity = gravity

def stopHitting(obj):
    obj.isSwingingSword = False
