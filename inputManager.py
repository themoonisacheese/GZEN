import pygame

import sys

upkeys = [pygame.K_UP, pygame.K_z, pygame.K_w, pygame.K_SPACE]
leftkeys = [pygame.K_LEFT, pygame.K_d]
rightkeys = [pygame.K_RIGHT, pygame.K_q, pygame.K_a]


def processInputs(clocktick, event, char):  # event.type is guaranteed to be pygame.KEYDOWN
    if event.key in upkeys:
        # print(char.movementVector)
        # print("up")
        char.movementVector = char.movementVector[0], char.movementVector[1] - 628 * (clocktick/1000)
        # print(char.movementVector)
    elif event.key in rightkeys:
        # print(char.movementVector)
        # print("right")
        char.movementVector = char.movementVector[0] - 16, char.movementVector[1]
        # print(char.movementVector)
    elif event.key in leftkeys:
        # print(char.movementVector)
        # print("left")
        char.movementVector = char.movementVector[0] + 16, char.movementVector[1]
        # print(char.movementVector)
    elif event.key == pygame.K_ESCAPE:
        print("Quitting game...")
        sys.exit()
