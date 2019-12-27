import pygame
from pygame.locals import *

import constants
from labyrinth import Labyrinth
from view import View
from guard import Guard
from macgyver import Macgyver
from item import Item

def game():

    level = Labyrinth()
    level.open_csv(constants.CSV_LEVEL, constants.NSPRITE)
    print(level.structure)

    hero = Macgyver()
    hero.create(level.structure)
    print(hero.location)

    end = Guard() 
    end.create(level.structure)
    print(end.location)
   
    ether = Item()
    ether.create(level.ground_list, level.structure, 'E')
    print(ether.location)

    thumb = Item()
    thumb.create(level.ground_list, level.structure, 'T')
    print(thumb.location)

    needle = Item()
    needle.create(level.ground_list, level.structure, 'N')
    print(needle.location)

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
                screen.hero_moved(hero.location, hero.next_location) #update the screen
                hero.location = hero.next_location
                if ether.pick(level.structure, hero.location):#Look at if not item was pick
                    screen.hero_pick(ether.char, Item.n_item)
                elif thumb.pick(level.structure, hero.location):
                    screen.hero_pick(thumb.char, Item.n_item)
                elif needle.pick(level.structure, hero.location):
                    screen.hero_pick(needle.char, Item.n_item)

                if (abs(hero.location[0] - end.location[0]) == 1 and hero.location[1] - end.location[1] == 0) \
                or (hero.location[0] - end.location[0] == 0 and abs(hero.location[1] - end.location[1]) == 1):
                    screen.finish(Item.n_item)
                    run = False
                    
    while run == False:
        for events in pygame.event.get():
            if events.type == pygame.QUIT :
                return False
            elif events.type == KEYDOWN:
                if (events.key == K_ESCAPE):
                    return False                
                elif (events.key == K_RETURN):
                    return True
                                        
def main():
    start = True
    while start == True:
        start = game()
        
if __name__ == '__main__':
    main()










