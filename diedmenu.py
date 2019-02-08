import pygame
from backwall import BackWall
from button import Button
from displayableElement import DisplayableElement
from animationAggregator import aggregateAnim
from textElement import TextElement
from scoreBoard import ScoreBoard
from upgrades import Upgrades

class DiedMenu:
    def __init__(self, SM, player):
        self.sm = SM
        self.player = player
        self.clock = pygame.time.Clock()
        self.gameObjects = []
        self.addbackground()
        self.retry = False
        self.scoreBoard = ScoreBoard()

    def addbackground(self):
        self.gameObjects = []
        for x in range(16):
            for y in range(9):
                self.gameObjects.append(BackWall((x,y)))
                self.gameObjects[-1].display = True


    def display(self):
        self.firstMenu()
        while not self.retry:
            tick = self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #test if we clicked a button
                    for obj in self.gameObjects:
                        if obj.rect.collidepoint(event.pos) and obj.__class__.__name__ == 'Button':
                            obj.click()
            self.sm.displayElements(self.gameObjects)
        self.retry = False

    def firstMenu(self):
        self.addbackground()
        self.gameObjects.append(DisplayableElement(aggregateAnim('sprites/menu/', 'you died'), 0.001))
        self.gameObjects[-1].moveto((530, 140))
        self.gameObjects.append(Button((300, 440), 'sprites/menu/', 'retry', self.retryMenu))
        self.gameObjects.append(Button((700, 440), 'sprites/menu/', 'submit', self.submitMenu))


    def retryMenu(self):
        self.addbackground()
        #add text: choose your upgrades
        self.gameObjects.append(TextElement('Choose your upgrades before starting over!', 'Calibri', 40))
        self.gameObjects[-1].moveto((540, 140))
        self.gameObjects.append(TextElement(str(self.player.score), 'Calibri', 30))
        self.gameObjects[-1].moveto((540, 170))
        #add text: score
        self.gameObjects.append(Button((250, 270), 'sprites/skills/', 'skil - rapid', self.upgradeSpeed))
        self.gameObjects.append(TextElement(str(self.player.upgrades.walkingSpeed * 1000), 'Calibri', 20))
        self.gameObjects[-1].moveto((250, 320))
        self.gameObjects.append(Button((380, 270), 'sprites/skills/', 'skill - attack', self.upgradeAtk))
        self.gameObjects.append(TextElement(str(self.player.upgrades.attackMultiplier * 500), 'Calibri', 20))
        self.gameObjects[-1].moveto((380, 320))
        if not self.player.upgrades.earPods:
            self.gameObjects.append(Button((470, 270), 'sprites/skills/', 'skill - earpods', self.upgradeEarpods))
            self.gameObjects.append(TextElement(str(2000), 'Calibri', 20))
            self.gameObjects[-1].moveto((470, 320))

        self.gameObjects.append(Button((610, 270), 'sprites/skills/', 'skill - resistance', self.upgradeRes))
        self.gameObjects.append(TextElement(str(1/self.player.upgrades.resistance), 'Calibri', 20))
        self.gameObjects[-1].moveto((610, 320))
        self.gameObjects.append(Button((770, 270), 'sprites/skills/', 'skill - saut', self.upgradeJump))
        self.gameObjects.append(TextElement(str(self.player.upgrades.jumpingHeight * 500), 'Calibri', 20))
        self.gameObjects[-1].moveto((770, 320))
        #if not upgraded yeet
        if not self.player.upgrades.heavyHit:
            self.gameObjects.append(Button((850, 270), 'sprites/skills/', 'skills- coup fort', self.upgradeheavyHit))
            self.gameObjects.append(TextElement(str(1000), 'Calibri', 20))
            self.gameObjects[-1].moveto((850, 320))

        self.gameObjects.append(Button((540, 440), 'sprites/menu/', 'retry', self.retryForReal))

    def upgradeSpeed(self):
        self.player.upgrades.buyWalkingSpeed(self.player)
        self.retryMenu()
    def upgradeAtk(self):
        self.player.upgrades.buyAttack(self.player)
        self.retryMenu()
    def upgradeEarpods(self):
        self.player.upgrades.buyEarPods(self.player)
        self.retryMenu()
    def upgradeRes(self):
        self.player.upgrades.buyResistance(self.player)
        self.retryMenu()
    def upgradeJump(self):
        self.player.upgrades.buyJumpingHeight(self.player)
        self.retryMenu()
    def upgradeheavyHit(self):
        self.player.upgrades.buyHeavyHit(self.player)
        self.retryMenu()
    def retryForReal(self):
        self.retry = True


    def submitMenu(self):
        self.addbackground()
        self.gameObjects.append(TextElement('High Scores:', 'Calibri', 40))
        self.gameObjects[-1].moveto((512, 25))
        self.gameObjects.append(Button((512, 65), 'sprites/menu/', 'retry', self.retryForReal))
        self.scoreBoard.ajouterScore(self.player.score)
        self.player.score = 0
        self.player.upgrades = Upgrades()
        i = 0
        for score in self.scoreBoard.scores:
            i += 1
            self.gameObjects.append(TextElement(score[0] + '       ' + str(score[1]), 'Calibri', 20))
            self.gameObjects[-1].moveto((512, 100 + (i*20)))
