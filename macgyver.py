from pygame.locals import *


class Macgyver():

    def __init__(self):
        self.location = None
        self.next_location = None
        
    def next(self, direction, structure, nsprite):
        #Tcheck if MacGyver stay in the labyrinth and no go trough wall
        if direction == K_LEFT and self.location[0] > 0:
            self.next_location = (self.location[0] - 1, self.location[1])
            print("Gauche")
        elif direction == K_RIGHT and self.location[0] < nsprite - 1:
            self.next_location = (self.location[0] + 1, self.location[1])
            print("droite")
        elif direction == K_UP and self.location[1] > 0:
            self.next_location = (self.location[0], self.location[1] - 1)
            print("haut")
        elif direction == K_DOWN and self.location[1] < nsprite - 1:
            self.next_location = (self.location[0], self.location[1] + 1)
            print("bas")
        else:
            pass
        if structure[self.next_location[0]][self.next_location[1]] != '1':
            return True
        else:
            return False
            #print(direction)
    
"""    def move(self, structure):
        #Make Macgaver move if he doesn't going through wall
        if structure[self.next_location[0]][self.next_location[1]] != '1':
            self.location = self.next_location
"""    
 