import sys

import pygame

from animationAggregator import aggregateAnim
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
pygame.key.set_repeat(1, 500)

# text elements must be after everything else to ensure drawing order
gameObjects = [
    Room('design niveaux/lvl1.png', 2),
    GravityObject((512, 128), aggregateAnim('sprites/character/', 'idle'), 0.5),
    TextElement('texte', 'Arial', 30, (0, 0, 255))
]

for obj in gameObjects:
    obj.display = True
gameObjects[1].movementVector = (20, 5)
gameObjects[0].show(True)

while 1:
    clocktick = clock.tick(60)  # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    # Timer part
    # Start this when someone clicks on play or whatever
    seconds = clocktick/1000
    time -= seconds  # while time < 180...
    gameObjects[-1].setText(str(int(time)))  # dirty adressing atm
    # End timer part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            processInputs(event, gameObjects[1])

    for obj in gameObjects:
        obj.animate(clocktick)
    SM.displayElements(gameObjects)
