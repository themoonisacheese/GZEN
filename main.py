import sys

import pygame

from animationAggregator import aggregateAnim
from inputManager import processInputs
from screenmanager import ScreenManager
from textElement import TextElement

from room import Room

pygame.init()
pygame.font.init()
# Vars
size = width, height = 1024, 576
SM = ScreenManager(size)
clock = pygame.time.Clock()
time = 0
pygame.key.set_repeat(1, 500)

gameObjects = [Room('design niveaux/lvl1.png', 2), TextElement('texte', 'Arial', 30, (0,0,255))] # text elements must be after everything else to ensure drawing order

for obj in gameObjects:
    obj.display = True

gameObjects[0].show(True)

while 1:
    clocktick = clock.tick(60)  # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    # Timer part
    # Start this when someone clicks on play or whatever
    seconds = clocktick/1000
    time += seconds  # while time < 180...
    gameObjects[-1].setText(str(clocktick)) #dirty adressing atm
    # End timer part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            processInputs(event)

    for obj in gameObjects:
        obj.animate(clocktick)
    SM.displayElements(gameObjects)
