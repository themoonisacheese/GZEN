import pygame
import datetime
class ScoreBoard:
    scores = []

    def ajouterScore(self,score):
        now = datetime.datetime.now()
        self.scores.append((now.strftime("%Y-%m-%d %H:%M"),score))
        scores.sort(key=lambda tup:tup[1])
