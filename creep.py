import random
import pygame
from pygame.math import Vector2
import core

class Creep:
    def __init__(self):
        self.position = Vector2(0, 0)
        self.taille = 6
        self.couleur = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        self.masse = 20

    def update(self):
        self.position.x = random.randint(self.taille, core.WINDOW_SIZE[0]-self.taille)
        self.position.y = random.randint(self.taille, core.WINDOW_SIZE[1]-self.taille)
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def show (self,screen):
        pygame.draw.circle(screen,self.couleur,[int(self.position.x),int(self.position.y)],self.taille)
    def getMass(self):
        return self.masse
    def getRadius(self):
        return self.taille
    def getPosition(self):
        return self.position