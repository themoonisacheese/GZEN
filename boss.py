import pygame
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim

class Boss(GridAlignedObject):
    alreadyTalked = False
    def __init__(self, gridPosition):
    GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'boss_idle_f'), 4)

    def getDialogue(self):
        self.alreadyTalked = True
        return ('Hehehe! \n Bien joue d\'etre arrive jusqu\'ici. \n Hihihi! \n Mais c\'etait en vain. \n Tu ne peux pas sauver le monde. \n Hohoho! \n Tu es destine a rester dans cette salle jusqu\'a la fin de tes jours... \n Soit dans pas longtemps. \n Huhuhu!')
