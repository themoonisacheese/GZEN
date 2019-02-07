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

pygame.init()
pygame.font.init()
# Vars
size = width, height = 1024, 576
SM = ScreenManager(size)
clock = pygame.time.Clock()
time = 180
roomNumber = 3
floorNumber = 1
pygame.key.set_repeat(1, 200)

gameObjects = []
for x in range(16):
    for y in range(9):
        gameObjects.append(BackWall((x,y)))

gameObjects.append(Room('design niveaux/lvl1.png', roomNumber, floorNumber))
gameObjects.append(Player())
gameObjects.append(DisplayableElement(aggregateAnim('sprites/environment', 'rectangle')))
gameObjects.append(TextElement('texte', 'Calibri', 40, (189, 18, 18)))
# THE ORDER OF GAMEOBJECTS IN THE LIST IS REALLY IMPORTANT: IT DICTATES DRAWING ORDER. DO NOT MESS WITH IT

for obj in gameObjects:
    obj.display = True
gameObjects[-4].show(True)
gameObjects[-3].setGravity(-1.0)

while 1:
    clocktick = clock.tick(60)  # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    # Timer part
    # Start this when someone clicks on play or whatever
    seconds = clocktick/1000.0
    time -= seconds  # while time < 180...
    timeleft = str(int(time)) + "s left"
    gameObjects[-1].setText(timeleft)  # dirty adressing atm
    gameObjects[-1].moveto((98, 28))
    # End timer part
    # Score part
    # print("oui")
    # End score part
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            processInputs(event, gameObjects[-3])

    # room handling
    if gameObjects[-3].rect.centerx > 1024:
        roomNumber += 1
        if roomNumber >= 8:
            roomNumber = 0
        gameObjects[-4] = Room(roomNumber, floorNumber)  # FIXME
        gameObjects[-4].show(True)
        gameObjects[-3].rect.centerx = 0

    if gameObjects[-3].rect.centerx < 0:
        roomNumber -= 1
        if roomNumber <= -1:
            roomNumber = 7
        gameObjects[-4] = Room(roomNumber, floorNumber)  # FIXME
        gameObjects[-4].show(True)
        gameObjects[-3].rect.centerx = 1024

    for obj in gameObjects:
        obj.update(clocktick, gameObjects)
        obj.animate(clocktick)
    SM.displayElements(gameObjects)
