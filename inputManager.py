import pygame

import sys

upkeys = [pygame.K_UP, pygame.K_z, pygame.K_w]
leftkeys = [pygame.K_LEFT, pygame.K_d]
rightkeys = [pygame.K_RIGHT, pygame.K_q, pygame.K_a]


def processInputs(event, char):  # event.type is guaranteed to be pygame.KEYDOWN
    if event.key in upkeys:
        print("up")
    elif event.key in rightkeys:
        print("right")
    elif event.key in leftkeys:
        print("left")
    elif event.key == pygame.K_SPACE:
        print("Jump !")
    elif event.key == pygame.K_ESCAPE:
        print("Quitting game...")
        sys.exit()
