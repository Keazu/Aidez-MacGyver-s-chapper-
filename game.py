import pygame
from pygame.locals import *

import constants
from labyrinth import Labyrinth
from view import View
from guard import Guard
from macgyver import Macgyver
from item import Item

def main():

    hero = Macgyver()
    end = Guard() 
    level = Labyrinth()
    
    hero.location, end.location = level.open_csv(constants.CSV_LEVEL, constants.NSPRITE)

    print(hero.location, end.location)
    ether = Item()
    ether.create(level.ground_list, level.structure, 'E')
    print(level.structure[ether.location[0]])

    thumb = Item()
    thumb.create(level.ground_list, level.structure, 'T')
    print(level.structure[thumb.location[0]])

    needle = Item()
    needle.create(level.ground_list, level.structure, 'N')
    print(level.structure[needle.location[0]])

    screen = View()
    screen.load()
    screen.create(level.structure)
    run = True
    while run:
        pygame.time.Clock().tick(30)
        event = pygame.event.wait()	#Attente des événementss
        if event.type == pygame.QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            run = False
            
        elif event.type == KEYDOWN:
            if hero.next(event.key, level.structure, constants.NSPRITE):
                #calculate next position
                #print(hero.location)
                #print(hero.next_location)
            #hero.move(level.structure) #tcheck if MacGyver stay in our labyrinth and attribute the new position
                screen.hero_moved(hero.location, hero.next_location) #update the screen
            hero.location = hero.next_location

            ether.pick(level.structure, hero.location)#Look at if not item was pick
            thumb.pick(level.structure, hero.location)
            needle.pick(level.structure, hero.location)
                
                








if __name__ == '__main__':
    main()











"""from constantes import *
from Labyrinth import *
from Macgyver import *
from Guard import *
from Item import *


def load():
    #create level from csv
    labyrinth = Labyrinth()
    labyrinth.open_csv(csv_level_01, nsprite)
    labyrinth.create(screen, pxsprite, img_ground, img_wall)
    
    guard = Guard()
    guard.create(screen, labyrinth.structure, pxsprite, img_guard)
    
    macgyver = Macgyver()
    macgyver.create(screen, labyrinth.structure, pxsprite, img_macgyver)
    
    needle = Item()
    needle.create(screen, labyrinth.ground_list, labyrinth.structure, pxsprite, img_needle)
    
    #labyrinth.place(needle.location)
    thumb = Item()
    thumb.create(screen, labyrinth.ground_list, labyrinth.structure, pxsprite, img_thumb)
    
    #labyrinth.place(thumb.location)
    ether = Item()
    ether.create(screen, labyrinth.ground_list, labyrinth.structure, pxsprite, img_ether)
    
    #labyrinth.place(ether.location)

run = True
while run:
    pygame.time.Clock().tick(30)
    pygame.display.flip()
    for event in pygame.event.get():	#Attente des événements
        if event.type == KEYDOWN:
            macgyver.next(event.key, labyrinth.structure, nsprite) #tcheck if MacGyver stay in our labyrinth
            macgyver.move(screen, labyrinth.structure, pxsprite, img_ground, img_macgyver)
            macgyver.pick(labyrinth.structure, needle.location, thumb.location, ether.location)
        
        if ((abs(macgyver.location[0] - guard.location[0]) == 1 and macgyver.location[1] - guard.location[1] == 0)) \
        or ((abs(macgyver.location[0] - guard.location[0]) == 0 and abs(macgyver.location[1] - guard.location[1]) == 1)):
            if macgyver.item_counter == 0:
                labyrinth.finish(screen, img_win)
            else:
                labyrinth.finish(screen, img_loose)
            
            #run = False
        
    pygame.display.flip()



  """