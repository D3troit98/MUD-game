# Define a function to register a new user
import sqlite3
import random

import resources.maps as maps
import resources.gameobjects as gameobjects
import resources.collisions as collisions
import menu.menu as Menu
import database.user as user


def gettinUserDetails():
  user.create_user()
  userData = {}
  while True:

      print("Welcome to EARTHIS")
      print("Do you want to create a new user of use an existing user")
      print("Answer with 'yes' or 'no")

      newUser = input("New user?")
      if newUser.lower() == "q": 
        print("Goodbye!")
        exit(-1)

      if newUser.lower() == "yes":      
        userData =  user.register_user()
        
        if 'name' in userData:
          print("everything went ok!")
          break
        else:
          print("something went wrong with creating a new user")
          print("to quit the game type p")
      elif newUser.lower() == "no":
        userData = user.loginUser()
        if 'name' in userData:
          print("everything went ok!")
          break
        else:
          print("something went wrong")
      else:
        print("Wrong input answer with 'yes' or 'no ")

  return userData


def lookatSelf():
  print("I am male half elf im in good shape")

def displayStartingMenu():
  print("A world of wonders but dangers lie in wake")
  print("Your family has been killed by the evil witch!")
  print("you need to gather keys to her castle to reach her!")

  userData = gettinUserDetails()

  print("Welcome " + userData["name"] + " 👧")
  print("You play as AZRAI")
  print("last and only daughter of king VEXZIE")
  print("Retrive the staff so you might save the day!")
  return userData 
    


def gameStart():
  userData = displayStartingMenu()
  return userData


def die(player):
  if player.hp < 1:
    print("You've Died!")
    user.storeData(player)
    exit(-1)

def ItemPickUp(player,c,r):
  if collisions.isCollided(c,1,r): #GOLD
    player.gold += random.randint(5,15)
  if collisions.isCollided(c,2,r): #peasant cloth
    player.hp += 1
  if collisions.isCollided(c,3,r): #witches cloths
    player.hp += 2
  if collisions.isCollided(c,4,r): #witches staff
    print("Huray you've gotten the the 🔑 key")
    print("You get a extra 100💰 gold for reaching it")
    print("you are almost there")
    print("But what if the plot is bigger than what we imagine")
    player.gold += 50
    player.xp += 50
    user.storeData(player)
    player.passTimes += 1
    player.gottenStaff = True

  if collisions.isCollided(c,8,r): #evil witch
    print("Huray you've killed witch")
    print("The one who ochestrated your family assasin")
    print("But she just said, she was paid!")
    player.gold += 100
    player.xp += 100
    user.storeData(player)
    player.passedTimes = 0
    exit(-1)
    

# Takes in a valid-input parameter, and a valid data type you want to comapre it to
# Returns array of these found parameters
def isValid(inp, inputs):
  ret = ''
  for x in inputs:
    if x == inp: ret += str(x)
  return(ret)

# Basic processing of input to see if input is valid
# Checks if key passed was valid to aid with collision
def processInput(p,m,i,e,SCREEN_W = 30, SCREEN_H = 22):
  colls = collisions.getCollisions(p,m,i)
  while True:
    ret = input().lower()
    
    if ret.lower() == "p" :  Menu.openMenu(p,SCREEN_W,SCREEN_H)

    # Collision detected if length of keys is greater than 0
    if collisions.isCollided(colls, 0,ret): continue

    #update user skills by item
    ItemPickUp(p,colls,ret)

    #collision between enemies and monster
    #making it so you lose health when next to the enemy and not while you are on top of them
    
    if collisions.isCollided(colls,5,ret):    
      p.hp -= e[0].attack
      e[0].hp -= 1
      break
        
    if collisions.isCollided(colls,6,ret):
      
      p.hp -= e[1].attack
      e[1].hp -= 1
      break
    
    if collisions.isCollided(colls,7,ret):
      p.hp -= e[2].attack
      e[2].hp -= 1
      break


    

    return ret


def main():
  MAP_WIDTH = 25
  MAP_HEIGHT = 25

  userData = gameStart()


  #here should be the function that will return the player type
  PLAYER = gameobjects.Witch(userData["name"],"Female",int(MAP_WIDTH/2),int(MAP_HEIGHT / 2))
  PLAYER.hp = userData["health"]
  if PLAYER.hp < 1: PLAYER.hp = 1
  PLAYER.level = userData["level"]
  if PLAYER.level < 1 : PLAYER.level = 1
  PLAYER.gold = userData["score"]
  if PLAYER.gold < 0 : PLAYER.gold = 0
  ITEM = gameobjects.Items()

  
  while True :
    PLAYER.gottenStaff = False
    ENEMIES = gameobjects.spawnEnemies(PLAYER,MAP_WIDTH,MAP_HEIGHT)    
    MAP = maps.GameMap(MAP_WIDTH,MAP_HEIGHT,PLAYER,ITEM,ENEMIES)
    
    print("move towards the 🔑 object, that's the key!")
    print("Make sure to avoid enemies")
    print("gather up golds 💰 to level up!")
    timer = 0
    
    while True:
      #print updated map
      MAP.printMap(PLAYER,ITEM)
      

      #inut from User
      inp = processInput(PLAYER,MAP,ITEM,ENEMIES)
      
      #update map, based on input and player position

      
      MAP.updateMap(inp,PLAYER,ENEMIES,timer)
      die(PLAYER)
      print("The enemies are following you 👹 👺 👻")
      print("out of life? the witch cloak 🥻 can heal you")
      timer += 1
      if PLAYER.gottenStaff  == True :
        break
    
    
  return(0)










   



if __name__ == "__main__":
  main()
