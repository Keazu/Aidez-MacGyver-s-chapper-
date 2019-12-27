import pygame
from pygame.locals import *
import constants



class View():
    def __init__(self):
        self.screen = None
        self.ground = None
        self.wall = None
        self.macgyver = None
        self.guard = None
        self.ether = None
        self.thum = None
        self.needle = None
        self.suringe = None
        self.win = None
        self.loose = None
        
    def load(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

        #Images load into pygame image
        self.ground = pygame.image.load(constants.GROUND).convert()
        self.wall = pygame.image.load(constants.WALL).convert()
        self.guard = pygame.image.load(constants.GUARD).convert_alpha()
        self.macgyver = pygame.image.load(constants.MACGYVER).convert()
        self.needle = pygame.image.load(constants.NEEDLE).convert_alpha()
        self.thumb = pygame.image.load(constants.THUMB).convert_alpha()
        self.ether = pygame.image.load(constants.ETHER).convert()
        self.suringe = pygame.image.load(constants.SURINGE).convert()

        #resize Sprite
        self.needle = pygame.transform.scale(self.needle, (constants.PXSPRITE, constants.PXSPRITE))
        self.thumb = pygame.transform.scale(self.thumb, (constants.PXSPRITE, constants.PXSPRITE))
        self.ether = pygame.transform.scale(self.ether, (constants.PXSPRITE, constants.PXSPRITE))
        self.suringe = pygame.transform.scale(self.suringe, (constants.PXSPRITE, constants.PXSPRITE))
        self.macgyver = pygame.transform.scale(self.macgyver, (constants.PXSPRITE, constants.PXSPRITE))

        #Win and Loose
        self.win = pygame.image.load(constants.WIN).convert_alpha()
        self.loose = pygame.image.load(constants.LOOSE).convert_alpha()

    def create(self, structure):
        x, y = 0, 0
        for y in range(constants.NSPRITE):
            for x in range(constants.NSPRITE):
                sprite = structure[(x, y)]
                if sprite == '1':
                    self.screen.blit(self.wall, (x * constants.PXSPRITE, y * constants.PXSPRITE))
                elif sprite == '0':
                    self.screen.blit(self.ground, (x * constants.PXSPRITE, y * constants.PXSPRITE))
                elif sprite == 'M':
                    self.screen.blit(self.macgyver, (x * constants.PXSPRITE, y * constants.PXSPRITE))
                elif sprite == 'G':
                    self.screen.blit(self.guard, (x * constants.PXSPRITE, y * constants.PXSPRITE))
                elif sprite == 'E':
                    self.screen.blit(self.ether, (x * constants.PXSPRITE, y * constants.PXSPRITE))
                elif sprite == 'T':
                    self.screen.blit(self.thumb, (x * constants.PXSPRITE, y * constants.PXSPRITE))
                elif sprite == 'N':
                    self.screen.blit(self.needle, (x * constants.PXSPRITE, y * constants.PXSPRITE))
                x += 1
            x = 0
            y += 1
        pygame.display.flip()
        
    def hero_moved(self, location, next_location):
        self.screen.blit(self.ground, (location[0] * constants.PXSPRITE, location[1] * constants.PXSPRITE))
        self.screen.blit(self.macgyver, (next_location[0] * constants.PXSPRITE, next_location[1] * constants.PXSPRITE))
        pygame.display.flip()

    def hero_pick(self, char, n_item):
        if char == 'E':
            self.screen.blit(self.ether, (constants.NSPRITE * constants.PXSPRITE, (n_item - 1) * constants.PXSPRITE))
        elif char == 'T':
            self.screen.blit(self.thumb, (constants.NSPRITE * constants.PXSPRITE, (n_item - 1) * constants.PXSPRITE))
        elif char == 'N':
            self.screen.blit(self.needle, (constants.NSPRITE * constants.PXSPRITE, (n_item - 1) * constants.PXSPRITE))
        if n_item == 3:
            self.screen.blit(self.suringe, (constants.NSPRITE * constants.PXSPRITE, n_item * constants.PXSPRITE))
        pygame.display.flip()

    def finish(self, n_item):
        if n_item == 3:
            self.screen.blit(self.win, (0, 0))

        else:
             self.screen.blit(self.loose,(0, 0))
        pygame.display.flip()
