from animationAggregator import aggregateAnim
from gridAlignedObject import GridAlignedObject
import random
class Table(GridAlignedObject):
    def __init__(self, gridPosition):
        GridAlignedObject.__init__(self, gridPosition, aggregateAnim('sprites/environment/', 'table'), 3)
