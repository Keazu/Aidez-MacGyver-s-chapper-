import pygame
from pygame.locals import *


class Guard():
    def __init__(self):
        self.location = None

    def create(self, structure):
        for key, value in structure.items(): 
            if value == 'G':
                self.location = key
