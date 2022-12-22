import random

from enum import Enum
from .mazeSearch import *

#object id and verification 
# walls = 1
# empty space = 0 
# a basic character  10 - 19
# an enemy character go from 20 - 29 #
# gold goes for 30
#  amour goes for 31 - 39
# cloths goes for 40 - 49
# random inventory like food and elixer goes for 50  - 59


#listing the objects in game will move to text file later
class Items:
    def __init__(self):
        self.WITCHES_STAFF = 4
        self.GOLD = 3
        self.WITCHES_CLOTH = 5
        self.PEASANT_CLOTH = 6
        self.EVIL_WITCH = 7

#character class
class Character:
  def __init__(self,name,sex,x,y) :
    self.name = name
    self.sex = sex
    self.id = 2
    self.coords = [x,y]
    #attributes
    self.hp = 3
    self.xp = 0
    self.level = 1
    #the dress or cloths acts like a defense
    self.dress = 0
    self.gold = 0
    self.gottenStaff = False
    self.passTimes = 0



  def move(self,movement, input):
    movement[self.coords[0]][self.coords[1]] = 0
    if input == 'w' or input == 's': self.coords[0] += (1 if input == 's' else -1)
    if input == "a" or input == "d" : self.coords[1] += (1 if input == 'd' else -1)
    movement[self.coords[0]][self.coords[1]] = self.id


  def levelUp(self,player):  
    if player.xp < 99:
        print("Not amass the right number of experience")
    else: 
        player.xp -= 100
        player.health += 1
        player.level += 1

  
 

        

  def printname(self):
      print("I am ",self.name,"A strong ", self.sex)

  def printCondition(self):
    ret = "HEALTH: " + str(self.hp)
    ret += "\nGOLD: " + str(self.gold)
    ret += "\nXP: " + str(self.xp)
    ret += "\nLevel: " + str(self.level)
    return(ret)

  def takeDamage(self,damageValue):
    self.hp = self.hp - (damageValue - self.dress.value )




class Enemy:
  def __init__(self, x,y,id):
    self.id = id
    self.coords = [x, y]
    self.hp = 1
    
    #creating character through ID
    if id == 20 :
        self.name = "Ogre"
        self.attack = 1
    elif id == 21:
        self.name = "Dark Elf"
        self.attack = 2
    elif id == 22:     
        self.name = "Ghost"
        self.attack = 3
    
    #neccesary? moving the ememies arond the map?
  def move(self,m,p):
        m[self.coords[0]][self.coords[1]] = 0
        path = search(m, tuple(self.coords), tuple(p.coords))[1:]
        self.coords[0] = path[0][0]
        self.coords[1] = path[0][1]
        m[self.coords[0]][self.coords[1]] = self.id
   
          
        

    


class Witch(Character):
  def __init__(self, name, sex,x,y):
    super().__init__(name, sex,x,y)
    self.id = 200   



def spawnEnemies(n, w, h):
    ret = []
    oldX = oldY = 0
    spawn = n
    if n.level < 5:
      spawn = 5
    elif n.level >5 and n.level < 10:
      spawn = n
    else: spawn = 10

    if n.passTimes == 3 : 
      spawn = 15
      print("The Evil Witch army are protecting her!")
      print("We must get to her to kill her!")

    for i in range(spawn):
        x = random.randint(1, w - 2)
        y = random.randint(1, h - 2)
        enemyId = random.randint(20,22)
        if x == oldX and y == oldY: continue
        enemyObject = Enemy(x,y,enemyId)
        ret.append(enemyObject)
        oldX = x
        oldY = y
    return ret





