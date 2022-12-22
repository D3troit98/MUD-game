#this class is to check for collision detection
#it checks for boundary
#if  it sees a boundary in bellow the player it returns s
#above the player return w
#wall to the right return d
#wall to the left return a
#I'MAP MAPaking use of the 'wasd' keycode


def checkCollision(character, MAP, ITEMS):
    ret = []
    if MAP[character.coords[0]][character.coords[1] + 1] == ITEMS or MAP[character.coords[0]][character.coords[1] - 1] == ITEMS:
        ret.append(('d' if MAP[character.coords[0]][character.coords[1] + 1] == ITEMS else 'a'))
    if MAP[character.coords[0] + 1][character.coords[1]] == ITEMS or MAP[character.coords[0] - 1][character.coords[1]] == ITEMS:
        ret.append(('s' if MAP[character.coords[0] + 1][character.coords[1]] == ITEMS else 'w'))
    return ret


def isCollided(keys,i,inp,hit= 0):
    if(len(keys[i]) > 0):
        for x in range(len(keys[i])):
            if keys[i][x] == inp: hit += 1
    return(True if hit > 0 else False)



def getCollisions(PLAYER,MAP,ITEMS):
    return [checkCollision(PLAYER,MAP.map,1), checkCollision(PLAYER,MAP.map,ITEMS.GOLD),
    checkCollision(PLAYER, MAP.map, ITEMS.PEASANT_CLOTH),checkCollision(PLAYER, MAP.map, ITEMS.WITCHES_CLOTH),
    checkCollision(PLAYER, MAP.map, ITEMS.WITCHES_STAFF),
     checkCollision(PLAYER, MAP.map, 20), checkCollision(PLAYER, MAP.map, 21),checkCollision(PLAYER, MAP.map, 22),
     checkCollision(PLAYER, MAP.map, ITEMS.EVIL_WITCH)
     
     ]