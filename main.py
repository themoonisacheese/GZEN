import pygame
import sys

# TODO:process key presses etc

from displayableElement import DisplayableElement
from screenmanager import ScreenManager


def main():
    pygame.init()
    size = width, height = 1280, 720
    SM = ScreenManager(size)
    disElem = []
    disElem[0] = DisplayableElement('test.')

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)


if __name__ == '__main__':
    main()
