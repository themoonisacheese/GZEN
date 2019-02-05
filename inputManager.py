import pygame

import sys

upkeys = [pygame.K_UP, pygame.K_z, pygame.K_w, pygame.K_SPACE]
leftkeys = [pygame.K_LEFT, pygame.K_d]
rightkeys = [pygame.K_RIGHT, pygame.K_q, pygame.K_a]


def processInputs(event, char):  # event.type is guaranteed to be pygame.KEYDOWN
    if event.key in upkeys:
        print("up")
        char.movementVector = char.movementVector[0], char.movementVector[1]
    elif event.key in rightkeys:
        print("right")
        char.movementVector = char.movementVector[0] + 5, char.movementVector[1]
    elif event.key in leftkeys:
        print("left")
        char.movementVector = char.movementVector[0] - 5, char.movementVector[1]
    elif event.key == pygame.K_ESCAPE:
        print("Quitting game...")
        sys.exit()
