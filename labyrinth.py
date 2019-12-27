

class Labyrinth():
    #Open CSV level, register it in a liste named structure as : structure[Y][X]
    #'0' for ground
    #'1' for wall
    #'M' for MacGyver
    #'G' for Guard
    def __init__(self):
        self.structure = {}
        self.ground_list = []
        self.end = None

    def open_csv(self, level, nsprite): 
        #Must init structure as 2D list as structure = [nsprite][nsprite]
        #self.structure = [['0'] * nsprite for line in range(nsprite)]  
        with open(level, newline='') as f:
            x, y = 0, 0
            for line in f:
                line = line.strip('\n\r')
                for raw in line:
                    self.structure[(x, y)] = raw
                    if raw == '0':
                        self.ground_list.append((x, y))
                    x += 1
                x, y = 0, y + 1



 