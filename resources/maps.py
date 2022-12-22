import random



class GameMap:
    def __init__(self,width,height,player, items,enemies):
        
        map_rectangle = [([1] * width)] + ([([1] + ([0] * (width - 2)) + [1]) for _ in range(height - 2)]) + [([1] * width)]

        #placing the character
        map_rectangle[player.coords[0]][player.coords[1]] = 200

        
        if player.passTimes < 3:
            #Randomizes the Gold drops
            for r in range(25): map_rectangle[random.randint(1,width - 2)][random.randint(1,height-2)] = items.GOLD

        #places clothes
        while True:
            r = random.randint(1,width -2)
            c = random.randint(1,height - 2)
            if map_rectangle[r][c] != 0 : continue
            itemChoice = random.randint(1,2)
            if itemChoice == 1:
                map_rectangle[r][c] = items.WITCHES_CLOTH
            else:
                map_rectangle[r][c] = items.PEASANT_CLOTH
            break

        #placing enemies
        for e in enemies:
            map_rectangle[e.coords[0]][e.coords[1]] = e.id
        self.map = map_rectangle


        if player.passTimes == 3:
            map_rectangle[random.randint(1,width - 2)][random.randint(1,height -2)] = items.EVIL_WITCH
        else:
            #placing the witches staff to be picked
            map_rectangle[random.randint(1,width - 2)][random.randint(1,height -2)] = items.WITCHES_STAFF


    
    def controls(self):
        return "WALK: W, A, S, and D\nPAUSE: P\n\n"

    def printMap(self,player, items):

        out = ""
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if r == 0:
                    if c == 0: out += "┌"
                    elif c == len(self.map[r]) - 1: out += "┐"
                    else: out += "──"
                if r > 0 and r < len(self.map) - 1:
                    if self.map[r][c] == 1: out += "│"
                    if self.map[r][c] == player.id: out += "👧"
                    if self.map[r][c] == items.GOLD: out += "💰"
                    if self.map[r][c] == items.WITCHES_STAFF : out += "🔑"
                    if self.map[r][c] == items.WITCHES_CLOTH : out += "🥻"
                    if self.map[r][c] == items.PEASANT_CLOTH : out += "👚"
                    if self.map[r][c] == items.EVIL_WITCH : out += "🧝🏿"
                    if self.map[r][c] == 20: out += "👹"
                    if self.map[r][c] == 21: out += " 👺" 
                    if self.map[r][c] == 22: out += "👻"
                    if self.map[r][c] == 0: out += "  "
                if r == len(self.map) - 1:
                    if c == 0: out += "└"
                    elif c == len(self.map[r]) - 1: out += "┘"
                    else: out += "──"
            out += "\n"
        print(out + "CONTROLS:\n" + self.controls() + "STATS:\n" + player.printCondition() + "\n\n\n")


               

 # Function SAVES the old address of the player position, then updates it with player / ENEMY pos
    def updateMap(self, items, player,enemies, t):
        player.move(self.map,items)
        if((t % 3) == 2):
            for e in enemies:
                e.move(self.map, player)
        return 0