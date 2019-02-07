import pygame
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim

class SpawnPoint(GridAlignedObject):
    def __init__(self, gridPosition):
        GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/environment/', 'spawnpoint'), 0.001)
