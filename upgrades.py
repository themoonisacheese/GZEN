import pygame

class Upgrades:
    heavyHit = False
    jumpingHeight = 1.0
    walkingSpeed = 1.0
    resistance = 1.0
    earPods = False
    scoreMultiplier = 1.0
    def __init__(self, cheat = False):
        if cheat:
            heavyHit = True
            jumpingHeight = 3.0
            walkingSpeed = 3.0
            resistance = 0.25
            earPods = True
            scoreMultiplier = 10.0

    def buyHeavyHit(self, playerObject):
        if playerObject.score >= 1000:
            playerObject.score -= 1000
            self.heavyHit = True

    def buyJumpingHeight(self, playerObject):
        if playerObject.score >= 500 * self.jumpingHeight:
            playerObject.score -= 500 * self.jumpingHeight
            self.jumpingHeight += 1

    def buyWalkingSpeed(self, playerObject):
        if playerObject.score >= 1000 * self.walkingSpeed:
            playerObject.score -= 1000 * self.walkingSpeed
            self.walkingSpeed += 0.5

    def buyResistance(self, playerObject):
        if playerObject.score >= 1/self.resistance:
            playerObject.score -= 1/self.resistance
            self.resistance -= 0.25

    def buyEarPods(self, playerObject):
        if playerObject.score >= 2000:
            playerObject.score -= 2000
            self.earPods = True

    def buyScoreMultiplier(self, playerObject):
        if playerObject.score >= 5000 * self.scoreMultiplier:
            playerObject.score -= 5000 * self.scoreMultiplier
            self.scoreMultiplier += 1
