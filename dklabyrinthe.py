#! /usr/bin/env python3
#! coding: utf-8


"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, niveau1.txt, niveau2.txt + images
"""

import pygame
from pygame.locals import *
from constantes import *
from classes import *

pygame.init()

# carteG.affiche()

pygame.Surface.scroll(fenetre)

# Chargement et collage du donkey:

donkey = Donkey(dkFront, dkBack, dkLeft, dkRight, "niveau1.txt")
donkey.afficheDepart()
donk = donkey.face
position_donkey = dkFront.get_rect()
position_donkey2 = dkFront.get_rect()
num_x = int(position_donkey[0] / 50)
num_y = int(position_donkey[1] / 50)

fenetre.blit(accueil, (0, 0))

# Rafraîchissement de l'écran
pygame.display.flip()

sig = 1
sigue = 1

continuer = 1

# Boucle infinie
while continuer:
    # Limitation de vitesse de la boucle
    # 30 frames par secondes suffisent
    pygame.time.Clock().tick(30)

    if sig == 1:
        fenetre.blit(accueil, (0, 0))
        # Rafraîchissement de l'écran
        pygame.display.flip()
        while sigue:
            # 30 frames par secondes suffisent
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:  # Si un de ces événements est de type QUIT
                    sigue = 0
                    continuer = 0  # On arrête la boucle
                if event.type == KEYDOWN and event.key == K_F1:
                    carteN = carta("niveau1.txt")
                    position_donkey = position_donkey2
                    sig = 0
                    sigue = 0
                elif event.type == KEYDOWN and event.key == K_F2:
                    carteN = carta("niveau2.txt")
                    position_donkey = position_donkey2
                    sig = 0
                    sigue = 0
    for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
        if event.type == QUIT:  # Si un de ces événements est de type QUIT
            continuer = 0  # On arrête la boucle
        if event.type == KEYDOWN:
            num_x = int(position_donkey[0] / 50)
            num_y = int(position_donkey[1] / 50)
            if event.key == K_ESCAPE or sig == 1:
                sigue = 1
                sig = 1
            # Si "flèche bas"
            # num_y + 1 <= 14 condition in order to stay on the screen
            elif num_y + 1 <= 14 and event.key == K_DOWN and carteN[num_y + 1][num_x] != "m":
                # On descend le perso
                position_donkey = position_donkey.move(0, 50)
                donk = donkey.face
            # Si "flèche haut"
            elif event.key == K_UP and carteN[num_y - 1][num_x] != "m":
                # On monte le perso
                if num_y - 1 >= 0:
                    position_donkey = position_donkey.move(0, -50)
                    donk = donkey.back
            # Si "flèche left"
            elif event.key == K_LEFT and carteN[num_y][num_x - 1] != "m":
                if num_x - 1 >= 0:
                    position_donkey = position_donkey.move(-50, 0)
                    donk = donkey.left
            # Si "flèche bas"
            elif num_x + 1 <= 14 and event.key == K_RIGHT and carteN[num_y][num_x + 1] != "m":
                # On descend le perso
                position_donkey = position_donkey.move(50, 0)
                donk = donkey.right
                if carteN[num_y][num_x + 1] == "a":
                    sig = 1
                    sigue = 1
                    print("Gagné!")
        if sig != 1:
            Carte(carteN, fond, mur, depart, banane).affiche()
            # fenetre.blit(fond, (0,0))
            fenetre.blit(donk, position_donkey)

        # Rafraichissement
        pygame.display.flip()
