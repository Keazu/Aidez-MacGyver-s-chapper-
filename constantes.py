"""Constantes du jeu de Labyrinthe Donkey Kong"""
import pygame
from pygame.locals import *
import os

#Paramètres de la fenêtre
nsprite = 15
pxsprite = 40
lenght = nsprite * pxsprite

#Chamin du niveau
csv_level_01 = r"data/level.csv"

#initialisatin de l'affichage
pygame.init()
screen = pygame.display.set_mode((lenght, lenght))

"""
#Automatic variable generator from file in "images" file, import os if is
for path, dirs, files in os.walk(folder_images):
    for filename in files:
        image = os.path.splitext(filename)[0]
        globals()[image] = pygame.image.load(path + "/" + filename).convert_alpha()   
"""

#Static image load into pygame image
img_wall = pygame.image.load(r"images\wall.png").convert()
img_ground = pygame.image.load(r"images\ground.png").convert()
img_guard = pygame.image.load(r"images\guard.png").convert_alpha()

#Hero image load into pygame image
img_macgyver = pygame.image.load(r"images\macgyver.png").convert()

#Item relativ to suringe
img_needle = pygame.image.load(r"images\needle.png").convert_alpha()
img_thumb = pygame.image.load(r"images\thumb.png").convert_alpha()
img_ether = pygame.image.load(r"images\ether.png").convert()
img_suringe = pygame.image.load(r"images\seringue.png").convert()

#Sprite size
img_needle = pygame.transform.scale(img_needle, (pxsprite, pxsprite))
img_thumb = pygame.transform.scale(img_thumb, (pxsprite, pxsprite))
img_ether = pygame.transform.scale(img_ether, (pxsprite, pxsprite))
img_suringe = pygame.transform.scale(img_suringe, (pxsprite, pxsprite))
img_macgyver = pygame.transform.scale(img_macgyver, (pxsprite, pxsprite))