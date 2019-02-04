import pygame
import sys

from displayableElement import DisplayableElement
from screenmanager import ScreenManager
from animationAggregator import aggregateAnim
pygame.init()
# Vars
size = width, height = 1280, 720
SM = ScreenManager(size)
disElems = []
disElems.append(DisplayableElement(aggregateAnim('sprites/bat/', 'bat_Animation'), 0.1))
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 500)
while 1:
    clocktick = clock.tick(30) # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in upkeys:
                print("up")
            elif event.key in rightkeys:
                print("right")
            elif event.key in leftkeys:
                print("left")
            elif event.key == pygame.K_SPACE:
                print("Jump !")

    dep = 2, 2
    disElems[1].move(dep)
        #TODO:process keypresses etc


    for elem in disElems:
        elem.animate(clocktick)
    SM.displayElements(disElems)
