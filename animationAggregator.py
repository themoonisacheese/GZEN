import pygame
import glob, os
def aggregateAnim(dir, baseName):
    owd = os.getcwd()
    os.chdir(dir)
    ret = []
    frames = glob.glob(baseName + '*.png')
    frames.sort() #very important
    for frame in frames:
        ret.append(pygame.image.load(frame))
    os.chdir(owd)
    return ret
