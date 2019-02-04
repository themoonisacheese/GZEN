import pygame
import glob, os
def aggregateAnim(dir, baseName):
    owd = os.getcwd()
    os.chdir(dir)
    ret = []
    for frame in glob.glob(baseName + '*.png'):
        ret.append(pygame.image.load(frame))
    os.chdir(owd)
    return ret
