import pygame
import sys

from displayableElement import DisplayableElement
from screenmanager import ScreenManager

pygame.init()
# Vars
size = width, height = 1280, 720
SM = ScreenManager(size)
disElems = []
disElems.append(DisplayableElement('sprites/bat/bat_Animation 1_0.png'))
disElems.append(DisplayableElement('sprites/bat/bat_Animation 1_5.png'))
upkeys = [pygame.K_UP, pygame.K_z, pygame.K_w]
leftkeys = [pygame.K_LEFT, pygame.K_d]
rightkeys = [pygame.K_RIGHT, pygame.K_q, pygame.K_a]
# Settings
clock = pygame.time.Clock()
pygame.key.set_repeat(1, 500)
while 1:
    clocktick = clock.tick(60)  # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
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
    SM.displayElements(disElems)
