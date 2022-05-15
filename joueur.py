from pygame.math import Vector2
import pygame
import core
import math


class Joueur:
    def __init__(self):
        self.rayon = 0
        self.position = Vector2(core.WINDOW_SIZE[0]/2,core.WINDOW_SIZE[1]/2)
        self.masse = 400
        self.couleur = (0,0,0)
        self.vitesse = Vector2(0,0)
        self.vitesseMax = 0
        self.nom = "PLAYER"
        self.textSize = (0,0)

    def calculVitesse(self):
        self.vitesseMax = 2.5-self.rayon/100

    def afficher(self, surface):
        pygame.draw.circle(surface, self.couleur, [int(self.position.x), int(self.position.y)], self.rayon)
        self.textSize = core.Draw.text((200,200,200), self.nom, (self.position.x-self.textSize[0]/2, self.position.y-self.textSize[1]/2), 20)

    def deplacer(self):
        if core.getMouseLeftClick() is not None:
            self.vitesse = Vector2(core.getMouseLeftClick()[0] - self.position.x, core.getMouseLeftClick()[1] - self.position.y)
            if self.vitesse != Vector2(0, 0):
                self.vitesse = self.vitesse.normalize()
                self.vitesse = self.vitesse*self.vitesseMax
        if self.position.x+self.vitesse.x+self.rayon >= core.WINDOW_SIZE[0] or self.position.x+self.vitesse.x-self.rayon <= 0:
            self.vitesse.x = 0
        if self.position.y+self.vitesse.y+self.rayon >= core.WINDOW_SIZE[1] or self.position.y+self.vitesse.y-self.rayon <= 0:
            self.vitesse.y = 0
        self.remiseSurTerrain()
        self.position += self.vitesse
    def calculRayon(self):
        self.rayon = round(math.sqrt((self.masse*2)/3.14))
    def addMass(self, m):
        self.masse += m
    def getRadius(self):
        return self.rayon
    def getPosition(self):
        return self.position
    def getMass(self):
        return self.masse
    def remiseSurTerrain(self):
        if self.position.x-self.rayon<=0 :
            self.position.x=self.rayon+1
        elif self.position.x+self.rayon>=core.WINDOW_SIZE[0] :
            self.position.x=core.WINDOW_SIZE[0]-self.rayon-1
        if self.position.y-self.rayon<=0 :
            self.position.y=self.rayon+1
        elif self.position.y+self.rayon>=core.WINDOW_SIZE[1] :
            self.position.y=core.WINDOW_SIZE[1]-self.rayon-1
