import sys

import pygame

from animationAggregator import aggregateAnim
from displayableElement import DisplayableElement
from inputManager import processInputs
from screenmanager import ScreenManager
from textElement import TextElement

from room import Room
from gravityObject import GravityObject

pygame.init()
pygame.font.init()
# Vars
size = width, height = 1024, 576
SM = ScreenManager(size)
clock = pygame.time.Clock()
time = 180
score = 0
pygame.key.set_repeat(1, 200)

# text elements must be after everything else to ensure drawing order
gameObjects = [
    Room('design niveaux/lvl1.png', 2),
    GravityObject((512, 128), aggregateAnim('sprites/character/', 'running'), 3.0),
    DisplayableElement(aggregateAnim('sprites/environment', 'RECTANGLE')),
    TextElement('texte', 'Calibri', 40, (189, 18, 18))
]

for obj in gameObjects:
    obj.display = True
gameObjects[1].movementVector = (0, 0)
gameObjects[0].show(True)
# gameObjects[2].moveto()

while 1:
    clocktick = clock.tick(60)  # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    # Timer part
    # Start this when someone clicks on play or whatever
    seconds = clocktick/1000.0
    time -= seconds  # while time < 180...
    timeleft = str(int(time)) + "s left ! "
    gameObjects[-1].setText(timeleft)  # dirty adressing atm
    gameObjects[-1].moveto((100, 25))
    # End timer part
    # Score part
    # print("oui")
    # End score part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            processInputs(event, gameObjects[1])

    for obj in gameObjects:
        obj.animate(clocktick)
        obj.update(clocktick, gameObjects)
    SM.displayElements(gameObjects)
