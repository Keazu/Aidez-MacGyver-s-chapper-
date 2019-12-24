

class Labyrinth():
    #Open CSV level, register it in a liste named structure as : structure[Y][X]
    #'0' for ground
    #'1' for wall
    #'M' for MacGyver
    #'G' for Guard
    def __init__(self):
        self.structure = []
        self.ground_list = []

    def open_csv(self, level, nsprite): 
        #Must init structure as 2D list as structure = [nsprite][nsprite]
        self.structure = [['0'] * nsprite for line in range(nsprite)]  
        with open(level, newline='') as f:
            x, y = 0, 0
            for line in f:
                line = line.strip('\n\r')
                for raw in line:
                    self.structure[y][x] = raw
                    if raw == '0':
                        self.ground_list.append((y,x))
                    elif raw == 'M':
                        champion_location = (y, x)
                    elif raw == 'G':
                        end_location = (y, x)
                    x += 1
                x, y = 0, y + 1
        return champion_location, end_location

    def update(self, char, location):
        self.structure[location[0]][location[1]] = char

    def finish(self, screen, image):
        screen.blit(image, (0, 0))


 