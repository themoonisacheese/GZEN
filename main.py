import sys

import pygame

from animationAggregator import aggregateAnim
from displayableElement import DisplayableElement
from inputManager import processInputs
from screenmanager import ScreenManager
from textElement import TextElement

from room import Room
from player import Player
from backwall import BackWall
from diedmenu import DiedMenu

pygame.init()
pygame.font.init()
# Vars
size = width, height = 1024, 576
SM = ScreenManager(size)
clock = pygame.time.Clock()
time = 5
roomNumber = 0
floorNumber = 5
#roomNumber = 0
#floorNumber = 1
pygame.key.set_repeat(1, 200)
# Music
pygame.mixer.music.load("music.wav")
pygame.mixer.music.set_volume(0.1)

gameObjects = []
for x in range(16):
    for y in range(9):
        gameObjects.append(BackWall((x,y)))

gameObjects.append(Room(roomNumber, floorNumber))
gameObjects.append(DisplayableElement(aggregateAnim('sprites/environment', 'tutorial')))
gameObjects.append(Player())
diedmenu = DiedMenu(SM, gameObjects[-1])
gameObjects.append(DisplayableElement(aggregateAnim('sprites/environment', 'rectangle')))
gameObjects.append(DisplayableElement(aggregateAnim('sprites/environment', 'rectangle')))
gameObjects.append(TextElement('texte', 'Calibri', 35, (189, 18, 18)))
gameObjects.append(TextElement('texte', 'Calibri', 35, (189, 18, 18)))
# THE ORDER OF GAMEOBJECTS IN THE LIST IS REALLY IMPORTANT: IT DICTATES DRAWING ORDER. DO NOT MESS WITH IT

for obj in gameObjects:
    obj.display = True
gameObjects[-7].show(True)

pygame.mixer.music.play(-1)
while 1:
    clocktick = clock.tick(60)  # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    # Timer part
    # Start this when someone clicks on play or whatever
    seconds = clocktick/1000.0
    time -= seconds  # while time < 180...

    timeleft = str(int(time)) + "s left!"
    gameObjects[-2].setText(timeleft)  # dirty adressing atm
    gameObjects[-2].moveto((98, 28))
    # End timer part
    # Score part
    score = str(gameObjects[-5].score)
    gameObjects[-1].setText(score)
    gameObjects[-1].moveto((920, 25))
    gameObjects[-3].moveto((920, 32))
    # End score part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            processInputs(event, gameObjects[-5])
    #room handling
    if roomNumber != 0 or floorNumber != 1 :
        gameObjects[-6].display = False
    else :
        gameObjects[-6].display = True

    if gameObjects[-5].rect.centerx > 1024:
        roomNumber += 1
        if roomNumber >= 8:
            roomNumber = 0
        gameObjects[-7] = Room(roomNumber, floorNumber)
        gameObjects[-7].show(True)
        gameObjects[-5].rect.centerx = 0

    if gameObjects[-5].rect.centerx < 0:
        roomNumber -= 1
        if roomNumber <= -1:
            roomNumber = 7

        gameObjects[-7] = Room(roomNumber, floorNumber)
        gameObjects[-7].show(True)
        gameObjects[-5].rect.centerx = 1024

    if time<1:
        SM.fadeOut(clocktick)
        if SM.currentFadeIndex == 255:
            diedmenu.display()
            sm.currentFadeIndex = 0
            time = 180
            roomNumber = 0
            floorNumber = 0
            gameObjects[-7] = Room(roomNumber, floorNumber)


        continue;

    for obj in gameObjects:
        obj.update(clocktick, gameObjects)
        obj.animate(clocktick)
    roomNumber = gameObjects[-7].roomnumber
    floorNumber = gameObjects[-7].floorNumber
    SM.displayElements(gameObjects)
