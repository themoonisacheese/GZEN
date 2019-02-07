from movingObject import MovingObject


class GravityObject(MovingObject):
    isOnTheGround = False
    def __init__(self, position, animationFrames, animationFrameRate=3):
        MovingObject.__init__(self, position, animationFrames, animationFrameRate)

    def update(self, ticktime, objlist, gravity = 1.0):
        self.isOnTheGround = False
        # + parce que +y vers le bas. 628 = 9.81 * 64 = 1g en supposant que 64px = 1m
        self.movementVector = self.movementVector[0], self.movementVector[1] + 628 * (ticktime/1000.0) * gravity
        MovingObject.update(self, ticktime, objlist)
        for obj in objlist:
            if obj.__class__.__name__ == 'Room':
                for block in obj.roomBlocks:
                    if gravity > 0 and block.__class__.__name__ == 'Wall' and (block.rect.collidepoint(self.rect.right-5, self.rect.bottom+2) or block.rect.collidepoint(self.rect.left+5, self.rect.bottom+2)):
                        self.isOnTheGround = True
                    if gravity < 0 and block.__class__.__name__ == 'Wall' and (block.rect.collidepoint(self.rect.right-5, self.rect.top-2) or block.rect.collidepoint(self.rect.left+5, self.rect.top-2)):
                        self.isOnTheGround = True

                    if self.isColliding(block):
                        if block.__class__.__name__ == 'Wall':
                            if (block.rect.collidepoint(self.rect.right, self.rect.bottom) or block.rect.collidepoint(self.rect.left, self.rect.bottom)) and not (block.rect.collidepoint(self.rect.right, self.rect.centery) or block.rect.collidepoint(self.rect.left, self.rect.centery)):
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
