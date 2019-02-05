class DisplayableElement:
    display = True
    isInTempAnim = False
    __timeSinceLastAnimation = 0
    __currentAnimationFrameIndex = 0

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
            if self.__timeSinceLastAnimation > (1/self.animationFrameRate * 1000):
                self.__timeSinceLastAnimation = 0
                self.__currentAnimationFrameIndex += 1
                if self.__currentAnimationFrameIndex >= len(self.animationFrames):
                    if self.isInTempAnim:
                        self.animationFrames = self.__originalAnimation
                        self.animationFrameRate = self.__originalFR
                        self.isInTempAnim = False
                        self.__tempAnimCallBack(self)
                    self.__currentAnimationFrameIndex = 0
                if self.currentTexture is not self.animationFrames[self.__currentAnimationFrameIndex]:
                    self.currentTexture = self.animationFrames[self.__currentAnimationFrameIndex]

    def changeAnimation(self, newAnimation, animationFrameRate=3):
        self.animationFrameRate = animationFrameRate
        self.animationFrames = newAnimation
        self.__currentAnimationFrameIndex = 0
        self.currentTexture = self.animationFrames[0]
        self.rect = self.currentTexture.get_rect()

#this changes the animation for one loop. after the loop, the original animation will be restored and callback(self) will be called
    def changeAnimationTemp(self, tempAnimation, animationFrameRate, callback): #callback must be a function that takes 1 argument: the object that called it.
        self.__originalAnimation = self.animationFrames
        self.__originalFR = self.animationFrameRate
        self.__tempAnimCallBack = callback
        self.isInTempAnim = True
        self.changeAnimation(tempAnimation, animationFrameRate)

    def update(self, ticktime, objlist):
        pass
