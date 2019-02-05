import glob
import os

import pygame


def aggregateAnim(dirc, baseName):
    owd = os.getcwd()
    os.chdir(dirc)
    ret = []
    frames = glob.glob(baseName + '*.png')
    frames.sort()  # very important
    for frame in frames:
        ret.append(pygame.transform.scale2x(pygame.image.load(frame)))
    os.chdir(owd)
    return ret
