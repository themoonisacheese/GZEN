def donothing(obj):
    pass


class DisplayableElement:
    display = True
    isInTempAnim = False
    __timeSinceLastAnimation = 0
    currentAnimationFrameIndex = 0

    def __init__(self, animationFrames, animationFrameRate = 3):
        self.animationFrames = animationFrames
        self.currentTexture = animationFrames[0]
        self.rect = self.currentTexture.get_rect()
        self.animationFrameRate = animationFrameRate

    def draw(self, screen):
        if self.display:
            screen.blit(self.currentTexture, self.rect)

    def moveto(self, pos):
        self.rect.center = pos

    def move(self, movement):
        self.rect = self.rect.move(movement)

    def animate(self, clocktick):
        if self.display:
            self.__timeSinceLastAnimation += clocktick
            if self.__timeSinceLastAnimation > (1.0/self.animationFrameRate * 1000):
                self.__timeSinceLastAnimation = 0
                self.currentAnimationFrameIndex += 1
                if self.currentAnimationFrameIndex >= len(self.animationFrames):
                    if self.isInTempAnim:
                        self.changeAnimation(self.__originalAnimation, self.__originalFR)
                        self.__tempAnimCallBack(self)
                    self.currentAnimationFrameIndex = 0
                if self.currentTexture is not self.animationFrames[self.currentAnimationFrameIndex]:
                    self.currentTexture = self.animationFrames[self.currentAnimationFrameIndex]

    def changeAnimation(self, newAnimation, animationFrameRate=3):
        OGPOS = self.rect.center
        self.isInTempAnim = False
        self.animationFrameRate = animationFrameRate
        self.animationFrames = newAnimation
        self.currentAnimationFrameIndex = 0
        self.currentTexture = self.animationFrames[0]
        self.rect = self.currentTexture.get_rect()
        self.rect.center = OGPOS

# this changes the animation for one loop. after the loop, the original animation will be restored and callback(self) will be called
# if no callback is provided, the animation will resume normally and not call anything else
    # callback must be a function that takes 1 argument: the object that called it.
    def changeAnimationTemp(self, tempAnimation, animationFrameRate, callback = donothing):
        self.__originalAnimation = self.animationFrames
        self.__originalFR = self.animationFrameRate
        self.__tempAnimCallBack = callback
        self.changeAnimation(tempAnimation, animationFrameRate)
        self.isInTempAnim = True #this needs to be after changeanimation.


    def update(self, ticktime, objlist):
        pass
