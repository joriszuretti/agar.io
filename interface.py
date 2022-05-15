from pygame import Vector2
import core
import pygame
class Interface :
    def __init__(self):
        self.score = 0
        self.time = 0
        self.taille = Vector2(100,60)
        self.couleur = (100,100,100, 170)
        self.startButton = pygame.Rect(core.WINDOW_SIZE[0]/2 -150,core.WINDOW_SIZE[1]-150,275,50)
    def ingame(self, player, ennemis):
        core.Draw.rect(self.couleur, (core.WINDOW_SIZE[0]-self.taille.x, 5, self.taille.x, self.taille.y))
        core.Draw.text((0, 0, 0), 'SCORE : ', (core.WINDOW_SIZE[0] - self.taille.x + 10, 10), 20)
        core.Draw.text((0,0,0), str(player.getMass()), (core.WINDOW_SIZE[0]-self.taille.x+10,30), 20)
    def endgame(self, win):
        core.Draw.rect((255,255,255),(0,0,core.WINDOW_SIZE[0], core.WINDOW_SIZE[1]))
        if win :
            core.Draw.text((0, 0, 0), 'CONGRATULATION', ((core.WINDOW_SIZE[0]/2) - 100 , (core.WINDOW_SIZE[1]/2)-50), 50)
        else:
            core.Draw.text((0, 0, 0), 'GAME OVER', ((core.WINDOW_SIZE[0] / 2) - 100, (core.WINDOW_SIZE[1] / 2)-50), 50)
    def menu(self, fenetre):
        fenetre.defCouleur((0,0,0))
        fenetre.set(core)
        core.Draw.text((255, 255, 255), 'Agar.io', ((core.WINDOW_SIZE[0] / 2) - 150, 60), 90)
        core.Draw.rect((255,0,255), self.startButton)
        core.Draw.text((0,0,0), "LET'S PLAY", (core.WINDOW_SIZE[0]/2 - 100, core.WINDOW_SIZE[1]-150), 30)
        if core.getMouseLeftClick() is not None :
            if self.startButton.collidepoint(core.getMouseLeftClick()[0], core.getMouseLeftClick()[1]):
                return True
        return False