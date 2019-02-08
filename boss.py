import pygame
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim

class Boss(GridAlignedObject):
    alreadyTalked = False
    def __init__(self, gridPosition):
        GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'boss_idle_f'), 4)
        self.currentLine=0;
        self.dialogues=['Hehehe!','Bien joue d\'etre arrive jusqu\'ici.','Hihihi! ','Mais c\'etait en vain.','Tu ne peux pas sauver le monde.',' Hohoho!','Tu es destine a rester dans cette salle jusqu\'a la fin de tes jours...','Soit dans pas longtemps','Huhuhu!','']
    def getDialogue(self):
        self.alreadyTalked = True
    def nextDialogue(self):
        self.currentLine+=1
        return self.dialogues[self.currentLine-1]
