import sys

import pygame

from animationAggregator import aggregateAnim
from inputManager import processInputs
from screenmanager import ScreenManager
from wall import Wall

pygame.init()
# Vars
size = width, height = 1280, 576
SM = ScreenManager(size)
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 500)


gameObjects = [Wall((0, 0)), Wall((4, 5)), Wall((2, 5)), Wall((3, 5)), Wall((4, 5)), Wall((4, 6)), Wall((4, 7)),
               Wall((4, 8)), Wall((4, 2)), Wall((4, 3))]

for obj in gameObjects:
    obj.display = True

while 1:
    clocktick = clock.tick(30)  # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            processInputs(event)

    for obj in gameObjects:
        obj.animate(clocktick)
    SM.displayElements(gameObjects)
