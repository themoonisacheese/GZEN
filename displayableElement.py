import pygame
import sys
class DisplayableElement:
    draw = True
    __timeSinceLastAnimation = 0
    __currentAnimationFrameIndex = 0
    def __init__(self, animationFrames, animationFrameRate = 3):
        self.animationFrames = animationFrames
        self.currentTexture = animationFrames[0]
        self.rect = self.currentTexture.get_rect()
        self.animationFrameRate = animationFrameRate

    def draw(self, screen):
        if self.draw:
            screen.blit(self.currentTexture, self.rect)

    def moveto(self, pos):
        self.rect.center = pos

    def move(self, movement):
        self.rect = self.rect.move(movement)

    def animate(self, clocktick):
        self.__timeSinceLastAnimation += clocktick
        if self.__timeSinceLastAnimation >= (1/self.animationFrameRate):
            self.__currentAnimationFrameIndex +=1
            if self.__currentAnimationFrameIndex >= len(self.animationFrames):
                self.__currentAnimationFrameIndex = 0
            self.currentTexture = self.animationFrames[self.__currentAnimationFrameIndex]

    def changeAnimation(self, newAnimation, animationFrameRate):
        self.animationFrameRate = animationFrameRate
        self.animationFrames = newAnimation
        self.__currentAnimationFrameIndex = 0;
