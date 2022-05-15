from pygame.math import Vector2
from joueur import Joueur
import core
import random


class Ennemi(Joueur):
    def __init__(self):
        Joueur.__init__(self)
        self.target = Vector2(0,0)
        self.nom = ""
        self.couleur = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

    def deplacer(self, joueur, creeps):
        self.comportement(joueur, creeps)
        if self.target != Vector2(0,0):
            self.vitesse = Vector2(self.target.x - self.position.x, self.target.y - self.position.y)
            self.vitesse = self.vitesse.normalize()
            self.vitesse = self.vitesse*self.vitesseMax
        if self.position.x+self.vitesse.x+self.rayon >= core.WINDOW_SIZE[0] or self.position.x+self.vitesse.x-self.rayon <= 0:
            self.vitesse.x = 0
        if self.position.y+self.vitesse.y+self.rayon >= core.WINDOW_SIZE[1] or self.position.y+self.vitesse.y-self.rayon <= 0:
            self.vitesse.y = 0
        self.remiseSurTerrain()
        self.position += self.vitesse
    def distance(self, circle):
        return Vector2(self.position.x-circle.getPosition().x, self.position.y-circle.getPosition().y).magnitude()
    def mangerCreep(self, creeps):
        dist = []
        for c in creeps :
            dist.append(self.distance(c))
            if min(dist)==self.distance(c) :
                self.target = c.getPosition()
    def mangerJoueur(self, joueur):
        self.target = joueur.getPosition()
    def fuirJoueur(self, joueur):
        point = Vector2(self.position.x-joueur.getPosition().x, self.position.y-joueur.getPosition().y)
        self.target = self.position+point
    def comportement(self, joueur, creeps):
        if joueur.getMass()<self.masse :
            self.mangerJoueur(joueur)
        elif joueur.getMass()>self.masse and self.distance(joueur)<200 :
            self.fuirJoueur(joueur)
        else:
            self.mangerCreep(creeps)
    def setPosition(self, p):
        self.position = p
