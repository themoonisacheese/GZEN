import pygame
from movingObject import MovingObject

class GravityObject(MovingObject):
    def __init__(self, position, animationFrames, animationFrameRate=3):
        MovingObject.__init__(self, position, animationFrames, animationFrameRate)

    def update(self, ticktime, objlist):
        self.movementVector = self.movementVector[0], self.movementVector[1] + 628 * (ticktime/1000) # + parce que +y vers le bas. 628 = 9.81 * 64 = 1g en supposant que 64px = 1m
        MovingObject.update(self, ticktime, objlist)
        for obj in objlist:
            if obj.__class__.__name__ == 'Room':
                for block in obj.roomBlocks:
                    if self.isColliding(block):
                        if block.__class__.__name__ == 'Wall': #FIXME: this code probably wraps you to the top of a block if you try jumping into it.
                            if self.movementVector[0] > 0:
                                self.rect.right = block.rect.left
                            if self.movementVector[0] < 0:
                                self.rect.left = block.rect.right
                            if self.movementVector[1] > 0:
                                self.rect.bottom = block.rect.top
                                self.movementVector = self.movementVector[0], self.movementVector[1] - self.movementVector[1]
                            if self.movementVector[1] < 0:
                                self.rect.top = block.rect.bottom
                                self.movementVector = self.movementVector[0], self.movementVector[1] - self.movementVector[1]
