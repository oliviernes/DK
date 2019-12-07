from constantes import *
from functions import * 

class Carte:
    """Show the map in graphic mode"""
    def __init__(self, carte, mapa, wall, depart, arrive):
        """Initialize map object"""
        self.carte = carte
        self.mapa = mapa
        self.wall = wall
        self.depart = depart
        self.arrive = arrive
        
    def affiche(self):
        """display the map"""
        fenetre.blit(self.mapa, (0,0))
        i = 0
        while i < len(self.carte):
            j = 0
            while j < len(self.carte[i]):
                if self.carte[i][j] == "m":
                    fenetre.blit(self.wall, (j * 50, i * 50))
                elif self.carte[i][j] == "d":
                    fenetre.blit(self.depart, (j * 50, i * 50))
                elif self.carte[i][j] == "a":
                    fenetre.blit(self.arrive, (j * 50, i * 50))
                else:
                    pass
                j += 1
            i += 1

class Donkey:
    """Show and Move Donkey Kong"""
    def __init__(self, face, back, left, right, fichier):
        """Initialize the donkey"""
        self.face = face
        self.back = back
        self.left = left
        self.right = right
        self.fichier = fichier

    def afficheDepart(self):
        fenetre.blit(self.face, (coord(self.fichier)[0][1] * 50, coord(self.fichier)[0][0] * 50))
        
        
