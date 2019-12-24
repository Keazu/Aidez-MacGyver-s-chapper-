import pygame
from pygame.locals import *


class Guard():
    def __init__(self):
        self.location = None
"""
    def create(self, screen, structure, pxsprite, guard):
        x, y = 0, 0
        for line in structure:
            for raw in line:
                if raw == 'G':
                self.location = (x, y)
                x += 1 
            x = 0
            y += 1
"""