import pygame
from pygame.locals import * 

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((750, 750), RESIZABLE)

#Chargement et collage du fond
fond = pygame.image.load("images/fond2.jpg").convert()
accueil = pygame.image.load("images/homepage2.png").convert()

#chargement des murs, du départ et de l'arrivée:
mur = pygame.image.load("images/mur2.jpg").convert()
depart = pygame.image.load("images/depart2.png").convert()
banane = pygame.image.load("images/banane2.png").convert_alpha()

#Chargement du donkey:
dkFront = pygame.image.load("images/DK_front2.png").convert_alpha()
dkBack = pygame.image.load("images/DK_back2.png").convert_alpha()
dkRight = pygame.image.load("images/DK_right_move2.png").convert_alpha()
dkLeft = pygame.image.load("images/DK_left_move2.png").convert_alpha()
