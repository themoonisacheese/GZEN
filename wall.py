from animationAggregator import aggregateAnim
from gridAlignedObject import GridAlignedObject


class Wall(GridAlignedObject):
    def __init__(self, gridPosition):
        # TODO:randomly assign cracked wall texture
        GridAlignedObject.__init__(self, gridPosition, aggregateAnim('sprites/environment/', 'wall'), 0.001)
