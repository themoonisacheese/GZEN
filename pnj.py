import pygame
from gridAlignedObject import GridAlignedObject
from animationAggregator import aggregateAnim
import random

class PNJ(GridAlignedObject):
    alreadyTalked = False
    def __init__(self, gridPosition):
        rand = random.random()
        if rand <= 1/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc1_f'), 4)
        elif 1/12.0 < rand <= 2/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc2'), 4)
        elif 2/12.0 < rand <= 3/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc3'), 4)
        elif 3/12.0 < rand <= 4/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc4'), 4)
        elif 4/12.0 < rand <= 5/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc5'), 4)
        elif 5/12.0 < rand <= 6/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc6'), 4)
        elif 6/12.0 < rand <= 7/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc7'), 4)
        elif 7/12.0 < rand <= 8/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc8'), 4)
        elif 8/12.0 < rand <= 9/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc9'), 4)
        elif 9/12.0 < rand <= 10/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc10'), 4)
        elif 10/12.0 < rand <= 11/12.0:
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc11'), 4)
        elif 11/12.0 < rand :
            GridAlignedObject.__init__(self,gridPosition, aggregateAnim('sprites/npc', 'npc12'), 4)

    def getDialogue(self):
        self.alreadyTalked = True
        return random.choice([
            'J\'aime les shorts! Ils sont comfortables et faciles a porter!',
            'Salut.',
            'Hey! tonton! Ca fzait longtemps qu\'on c\'tait pas vu !',
            'Vous ici?!',
            'Un dernier verre et on repart!',
            'Saviez vous que la biere de ce bar etait seulement du pain dans de l\'eau ?'
            'Mais ou est donc passe le bar man?',
            '...et la la souris dit a l\'elephant :"mais mois j\'etais malade"!',
            'Vous auriez pas vu mon Grand-pere?',
            'J\'arrete pas de trouver des pilons de poulet par terre...',
            'T\'es qui?',
            'T\'es pas un peu vieux pour etre emo?',
            'Avant j\'etais un aventurier puis je me suis pris une fleche dans le genou',
            'Je suis degoute j\'ai perdu toutes mes pieces dans le donjon',
            'Je trouve que ce bar manque de dimensions...',
            '...',
            'Eh je vous connais non?',
            'La musique ici est un peu repetitive...',
        ])
