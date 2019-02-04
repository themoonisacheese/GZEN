import sys, pygame
from displayableElement import DisplayableElement
from screenmanager import ScreenManager
from array import array
pygame.init()
size = width, height = 1280, 720
SM = ScreenManager(size)
disElems = []
disElems.append(DisplayableElement('sprites/bat/bat_Animation 1_0.png'))
disElems.append(DisplayableElement('sprites/bat/bat_Animation 1_5.png'))
clock = pygame.time.Clock()
while 1:
    clocktick = clock.tick(60) # on peut multiplier toutes les vitesses par ca pour les adapater au framerate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #TODO:process keypresses etc
    dep = 2,2
    disElems[1].move(dep)
    SM.displayElements(disElems)
