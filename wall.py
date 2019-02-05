from animationAggregator import aggregateAnim
from gridAlignedObject import GridAlignedObject
import random


class Wall(GridAlignedObject):
    def __init__(self, gridPosition):
        if random.random() > 0.95:
            GridAlignedObject.__init__(self, gridPosition, aggregateAnim('sprites/environment/', 'cracked_wall'), 0.001)
        else:
            GridAlignedObject.__init__(self, gridPosition, aggregateAnim('sprites/environment/', 'wall'), 0.001)

    def animate(self, clocktick):
        pass
