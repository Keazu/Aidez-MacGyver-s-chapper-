import os
import pygame
from pygame.locals import *
from random import randint

class Labyrinth():
    #Open CSV level, register it in a liste named structure as : structure[Y][X]
    #'0' for ground
    #'1' for wall
    #'M' for MacGyver
    #'G' for Guard
    def __init__(self, level):
        self.structure = []
        self.ground_list = []
        with open(level, newline='') as f:
            for line in f:
                self.structure.append(line.strip('\n\r'))
                
    def create(self, screen, pxsprite, ground, wall):
        x, y = 0, 0
        for raw in self.structure:
            for sprite in raw:
                if sprite == '1':
                    screen.blit(wall, (x * pxsprite, y * pxsprite))
                elif sprite != '1':
                    screen.blit(ground, (x * pxsprite, y * pxsprite))
                    self.ground_list.append((x, y))                    
                x += 1
            x = 0
            y += 1

class Macgyver():
    def __init__(self, location = (0, 0), next_location = (0, 0)):
        self.location = location
        self.next_location = next_location
        self.item_counter = 3
    def create(self, screen, structure, pxsprite, macgyver):
        x, y = 0, 0
        for line in structure:
            for row in line:
                if row == 'M':
                    screen.blit(macgyver, (x * pxsprite, y * pxsprite))
                    self.location = (x, y)
                x += 1
            x = 0
            y += 1

    def next(self, direction, structure, nsprite):
        #Tcheck if MacGyver stay in the labyrinth
        if direction == K_LEFT and self.location[0] > 0:
            self.next_location = (self.location[0] - 1, self.location[1])
        elif direction == K_RIGHT and self.location[0] < nsprite - 1:
            self.next_location = (self.location[0] + 1, self.location[1])
        elif direction == K_UP and self.location[1] > 0:
            self.next_location = (self.location[0], self.location[1] - 1)
        elif direction == K_DOWN and self.location[1] < nsprite - 1:
            self.next_location = (self.location[0], self.location[1] + 1)
        else:
            pass
    
    def move(self, screen, structure, pxsprite, img_ground, img_macgyver):
        #Make Macgaver move if he doesn't going through wall
        if structure[self.next_location[1]][self.next_location[0]] != '1':
            screen.blit(img_ground, (self.location[0] * pxsprite, self.location[1] * pxsprite))
            screen.blit(img_macgyver, (self.next_location[0] * pxsprite, self.next_location[1] * pxsprite))
            self.location = self.next_location
    
    def pick(self, *args):
        for arg in args:
            if self.location == arg:
                self.item_counter -= 1
                print(self.item_counter)
            


class Guard():
    def __init__(self, location = (0, 0)):
        self.location = location
    def create(self, screen, structure, pxsprite, guard):
        x, y = 0, 0
        for raw in structure:
            for line in raw:
                if line == 'G':
                    screen.blit(guard, (x * pxsprite, y * pxsprite))
                    self.location = (x, y)
                    x += 1 
                x = 0
            y += 1

class Item():
    def __init__(self):
        self.location = (0, 0)
        self.pick_counter = 3
    def create(self, screen, ground_list, pxsprite, item): #needle, thumb, ether
        rdm_int = randint(0, len(ground_list) - 1)
        self.location = ground_list.pop(rdm_int)
        screen.blit(item, (self.location[0] * pxsprite, self.location[1] * pxsprite))
        print(self.location)

