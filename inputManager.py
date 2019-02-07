import pygame

import sys

upkeys = [pygame.K_UP, pygame.K_z, pygame.K_w, pygame.K_SPACE]
leftkeys = [pygame.K_RIGHT, pygame.K_d]
rightkeys = [pygame.K_LEFT, pygame.K_q, pygame.K_a]
lastevent = True


def processInputs(event, char):  # event.type is guaranteed to be pygame.KEYDOWN
    global lastevent
    if event.type == pygame.KEYDOWN:
        if event.key in upkeys:
            char.jump()
        elif event.key in rightkeys:
            char.startRunning(True)
            lastevent = True
            if char.movementVector[0] >= 0:
                char.movementVector = char.movementVector[0] - 80, char.movementVector[1]
            elif 0 > char.movementVector[0] > -280:
                char.movementVector = char.movementVector[0] - 48, char.movementVector[1]
        elif event.key in leftkeys:
            char.startRunning(False)
            lastevent = False
            if char.movementVector[0] <= 0:
                char.movementVector = char.movementVector[0] + 80, char.movementVector[1]
            elif 0 < char.movementVector[0] < 280:
                char.movementVector = char.movementVector[0] + 48, char.movementVector[1]
        elif event.key == pygame.K_f:
            char.lighHit(lastevent)
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
