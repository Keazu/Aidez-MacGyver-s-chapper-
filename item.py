from random import randint      
  
class Item():
    #Contains location of item
    n_item = 0
    def __init__(self, ):
        self.location = (0, 0)
        self.char = None
        self.n_item += 1
        
    def create(self, ground_list, structure, char): #needle, thumb, ether
        #Receive ground sprite location as list of tuple, chose one and delete it from the list
        #Register tuple was choosen and place the item 
        self.char = char
        rdm_int = randint(0, len(ground_list) - 1)
        self.location = ground_list.pop(rdm_int)
        structure[self.location[0]][self.location[1]] = char
        

    def pick(self, structure, location):
        if structure[location[0]][location[1]] == self.char:
            self.item_counter -= 1
            structure[self.location[0]][self.location[1]] = '0'
            print(self.item_counter)
