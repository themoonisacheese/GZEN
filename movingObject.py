from collisionObject import CollisionObject


class MovingObject(CollisionObject):
    movementVector = 0,0  # in pixels per second

    def __init__(self, position, animationFrames, animationFrameRate = 3):
        CollisionObject.__init__(self, position, animationFrames, animationFrameRate)

    def update(self, ticktime, objlist):
        realVector = self.movementVector[0] * (ticktime/1000), self.movementVector[1] * (ticktime/1000)
        self.move(realVector)

    def changeVec(self, newVec):
        self.movementVector = newVec
