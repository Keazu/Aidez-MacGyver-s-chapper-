
from classes import *
from constantes import *

         
#create level from csv
labyrinth = Labyrinth(csv_level_01)
labyrinth.create(screen, pxsprite, img_ground, img_wall)

guard = Guard()
guard.create(screen, labyrinth.structure, pxsprite, img_guard)

macgyver = Macgyver()
macgyver.create(screen, labyrinth.structure, pxsprite, img_macgyver)

needle = Item()
needle.create(screen, labyrinth.ground_list, pxsprite, img_needle)

thumb = Item()
thumb.create(screen, labyrinth.ground_list, pxsprite, img_thumb)

ether = Item()
ether.create(screen, labyrinth.ground_list, pxsprite, img_ether)


run = True
while run:
    pygame.time.Clock().tick(30)
    pygame.display.flip()
    for event in pygame.event.get():	#Attente des événements
        if event.type == KEYDOWN:
            macgyver.next(event.key, labyrinth.structure, nsprite) #tcheck if MacGyver stay in our labyrinth
             
        macgyver.move(screen, labyrinth.structure, pxsprite, img_ground, img_macgyver)
        
        macgyver.pick(needle.location, thumb.location, ether.location)
        
    pygame.display.flip()



  