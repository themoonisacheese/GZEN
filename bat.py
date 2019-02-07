import pygame
from movingObject import MovingObject
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim


class Bat(MovingObject, GridAlignedObject):
    hp = 1
    damage = 100
    speed = 160
    scanningInterval = 1.0
    __timesinceLastDirChange = 0.0

    def __init__(self, startingGridPos):
        GridAlignedObject.__init__(self, startingGridPos, aggregateAnim('sprites/mobs/', 'bat_f'), 20)
        self.move((0, 60))

    def takeDamage(self, dmg):
        self.hp = self.hp - dmg
        pass

    def flipList(self, listToFlip, flip):
        templist = []
        for frame in listToFlip:
            templist.append(pygame.transform.flip(frame, flip, False))
        return templist

    def update(self, ticktime, objlist):
        self.__timesinceLastDirChange += ticktime/1000.0
        if self.__timesinceLastDirChange > self.scanningInterval:
            self.__timesinceLastDirChange = 0.0
            # find the player
            player = None
            for obj in objlist:
                if obj.__class__.__name__ == 'Player':
                    player = obj
                    break
            if player is not None:
                # calculate the direction he is in
                playerDirection = pygame.math.Vector2(player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery)
                # normalize
                tempvec = pygame.math.Vector2(self.movementVector[0] + playerDirection.x, self.movementVector[1] + playerDirection.y)
                tempvec.scale_to_length(self.speed)
                self.changeVec((tempvec.x, tempvec.y))
        MovingObject.update(self, ticktime, objlist)
        for obj in objlist:
            if obj.__class__.__name__ == 'Room':
                for block in obj.roomBlocks:
                    if self.isColliding(block):
                        if block.__class__.__name__ == 'Wall':
                            if block.rect.collidepoint(self.rect.centerx, self.rect.bottom):
                                self.rect.bottom = block.rect.top
                                self.movementVector = self.movementVector[0], 0
                            elif block.rect.collidepoint(self.rect.centerx, self.rect.top):
                                self.rect.top = block.rect.bottom
                                self.movementVector = self.movementVector[0], 0
                            elif block.rect.collidepoint(self.rect.right, self.rect.centery):
                                self.rect.right = block.rect.left
                                self.movementVector = 0, self.movementVector[1]
                            elif block.rect.collidepoint(self.rect.left, self.rect.centery):
                                self.rect.left = block.rect.right

    def changeVec(self, newVec):
        MovingObject.changeVec(self, newVec)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'bat_f'), (self.movementVector[0] > 0))

    def addToVec(self, x, y):
        MovingObject.addToVec(self, x, y)
        self.animationFrames = self.flipList(aggregateAnim('sprites/mobs/', 'bat_f'), (self.movementVector[0] > 0))
