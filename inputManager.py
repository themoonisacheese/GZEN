import pygame

import sys

upkeys = [pygame.K_UP, pygame.K_z, pygame.K_w, pygame.K_SPACE]
leftkeys = [pygame.K_RIGHT, pygame.K_d]
rightkeys = [pygame.K_LEFT, pygame.K_q, pygame.K_a]


def processInputs(event, char):  # event.type is guaranteed to be pygame.KEYDOWN
    # x = 0
    if event.key in upkeys:
        # print(char.movementVector)
        # print("up")
        char.addToVec(0, -300)
        # char.movementVector = char.movementVector[0], char.movementVector[1] - 628 * (clocktick/1000)
        # print(char.movementVector)
    elif event.key in rightkeys:
        # print(char.movementVector)
        # print("right")
        if char.movementVector[0] >= 0:
            char.movementVector = char.movementVector[0] - 64, char.movementVector[1]
            # x = 64
        elif 0 > char.movementVector[0] > -208:
            char.movementVector = char.movementVector[0] - 32, char.movementVector[1]
            # x = 32
        # print(char.movementVector)
        # print('Val ajoutee : ' + str(x))
    elif event.key in leftkeys:
        # print(char.movementVector)
        # print("left")
        if char.movementVector[0] <= 0:
            char.movementVector = char.movementVector[0] + 64, char.movementVector[1]
            # x = 64
        elif 0 < char.movementVector[0] < 208:
            char.movementVector = char.movementVector[0] + 32, char.movementVector[1]
            # x = 32
        # print(char.movementVector)
        # print('Val ajoutee : ' + str(x))
    elif event.key == pygame.K_f:
        print("cc")  # attack
    elif event.key == pygame.K_ESCAPE:
        print("Quitting game...")
        sys.exit()
