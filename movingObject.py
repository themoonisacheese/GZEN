from collisionObject import CollisionObject


class MovingObject(CollisionObject):
    movementVector = 0.0, 0.0  # in pixels per second
    __additiveVector = 0.0, 0.0

    def __init__(self, position, animationFrames, animationFrameRate=3):
        CollisionObject.__init__(self, position, animationFrames, animationFrameRate)

    def update(self, ticktime, objlist):
        realVector = self.movementVector[0] * (ticktime/1000.0), self.movementVector[1] * (ticktime/1000.0)
        self.__additiveVector = self.__additiveVector[0] + realVector[0], self.__additiveVector[1] + realVector[1]
        self.move(self.__additiveVector)
        # this is to make sure that we can still move even if the framerate is high. having a high framerate induces sub-pixel moves that do not work.
        if self.__additiveVector[0] >= 1:
            self.__additiveVector = 0, self.__additiveVector[1]
        if self.__additiveVector[1] >= 1:
            self.__additiveVector = self.__additiveVector[0], 0
        if self.__additiveVector[0] <=-1:
            self.__additiveVector = 0, self.__additiveVector[1]
        if self.__additiveVector[1] <=-1:
            self.__additiveVector = self.__additiveVector[0], 0

    def changeVec(self, newVec):
        self.movementVector = newVec

    def addToVec(self, x, y):
        self.movementVector = self.movementVector[0] + x, self.movementVector[1] + y
