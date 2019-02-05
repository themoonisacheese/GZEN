import pygame
from movingObject import MovingObject


class GravityObject(MovingObject):
    def __init__(self, position, animationFrames, animationFrameRate =3):
        MovingObject.__init__(self, position, animationFrames, animationFrameRate)

    def update(self, ticktime, objlist):
        # + parce que +y vers le bas. 628 = 9.81 * 64 = 1g en
        # supposant que 64px = 1m
        self.movementVector[1] += 628 * (ticktime/1000)
        MovingObject.update(self, ticktime, objlist)
        for obj in objlist:
            if self.isColliding(obj):
                # FIXME: this code probably wraps your to the top of a block if you try jumping into it.
                if obj.__class__name == 'Wall':
                    if self.movementVector[0] > 0:
                        self.rect.right = obj.rect.left
                    if self.movementVector[0] < 0:
                        self.rect.left = obj.rect.right
                    if self.movementVector[1] > 0:
                        self.rect.bottom = obj.rect.top
                        self.movementVector[1] = 0
                    if self.movementVector[1] < 0:
                        self.rect.top = obj.rect.bottom
                        self.movementVector[1] = 0
