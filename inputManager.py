import pygame

import sys

upkeys = [pygame.K_UP, pygame.K_z, pygame.K_w, pygame.K_SPACE]
leftkeys = [pygame.K_RIGHT, pygame.K_d]
rightkeys = [pygame.K_LEFT, pygame.K_q, pygame.K_a]


def processInputs(event, char):  # event.type is guaranteed to be pygame.KEYDOWN
    if event.type == pygame.KEYDOWN:
        if event.key in upkeys:
            char.jump()
        elif event.key in rightkeys:
            char.startRunning(True)
            if char.movementVector[0] >= 0:
                char.movementVector = char.movementVector[0] - 64, char.movementVector[1]
            elif 0 > char.movementVector[0] > -208:
                char.movementVector = char.movementVector[0] - 32, char.movementVector[1]
                # x = 32
            # print(char.movementVector)
            # print('Val ajoutee : ' + str(x))
        elif event.key in leftkeys:
            char.startRunning(False)
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
            print("atak")  # attack
            char.lighHit()
        elif event.key == pygame.K_e:
            print("gross atak")
            # char.heavyHit()
        elif event.key == pygame.K_ESCAPE:
            print("Quitting game...")
            sys.exit()
    elif event.type == pygame.KEYUP:
        if event.key in leftkeys:
            char.stopMoving(False)
            char.movementVector = char.movementVector = char.movementVector[0] - char.movementVector[0], char.movementVector[1]
        if event.key in rightkeys:
            char.stopMoving(True)
            char.movementVector = char.movementVector = char.movementVector[0] - char.movementVector[0], char.movementVector[1]
