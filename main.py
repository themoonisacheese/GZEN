import sys

import pygame

from animationAggregator import aggregateAnim
from inputManager import processInputs
from screenmanager import ScreenManager
from textElement import TextElement

from room import Room
from player import Player

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
    Player(),
    TextElement('texte', 'Calibri', 40, (189, 18, 18))
]

for obj in gameObjects:
    obj.display = True
gameObjects[0].show(True)

while 1:
    clocktick = clock.tick(60)  # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    # Timer part
    # Start this when someone clicks on play or whatever
    seconds = clocktick/1000.0
    time -= seconds  # while time < 180...
    timeleft = str(int(time)) + "s left ! "
    gameObjects[-1].setText(timeleft)  # dirty adressing atm
    # End timer part
    # Score part
    # print("oui")
    # End score part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            processInputs(event, gameObjects[1])

    for obj in gameObjects:
        obj.animate(clocktick)
        obj.update(clocktick, gameObjects)
    SM.displayElements(gameObjects)
