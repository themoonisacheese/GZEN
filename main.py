import sys, pygame
from displayableElement import DisplayableElement
from screenmanager import ScreenManager
pygame.init()
size = width, height = 1280, 720
SM = ScreenManager(size)
disElem = []
disElem[0] = DisplayableElement('test.')
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #TODO:process keypresses etc
    
