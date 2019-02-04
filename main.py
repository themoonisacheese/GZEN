import pygame
import sys

from displayableElement import DisplayableElement
from screenmanager import ScreenManager
from animationAggregator import aggregateAnim
from inputManager import processInputs

pygame.init()
# Vars
size = width, height = 1280, 720
SM = ScreenManager(size)
disElems = []
disElems.append(DisplayableElement(aggregateAnim('sprites/bat/', 'bat_Animation'), 5))
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 500)
while 1:
    clocktick = clock.tick(30) # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            processInputs(event)

    for elem in disElems:
        elem.animate(clocktick)
    SM.displayElements(disElems)
