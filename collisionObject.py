from gameObject import GameObject


class CollisionObject(GameObject):
    def __init__(self, position, animationFrames, animationFrameRate=3):
        GameObject.__init__(self, position, animationFrames, animationFrameRate)

    def isColliding(self, otherObject):
        return self.rect.colliderect(otherObject.rect)
