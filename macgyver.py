from pygame.locals import *


class Macgyver():

    def __init__(self):
        self.location = None
        self.next_location = None

    def create(self, structure):
        for key, value in structure.items(): 
            if value == 'M':
                self.location = key
        
    def next(self, direction, structure, nsprite):
        #Tcheck if MacGyver stay in the labyrinth and no go trough wall
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
        if structure[(self.next_location[0], self.next_location[1])] != '1':
            return True
        else:
            return False
    
    
 