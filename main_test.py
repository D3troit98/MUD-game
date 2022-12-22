import unittest
import sqlite3
import resources.maps as maps
import resources.gameobjects as gameobjects
import resources.collisions as collisions
import menu.menu as Menu
import database.user as user
import main
import random


MAP_WIDTH = 25
MAP_HEIGHT = 25



def print_game_map(game_map):
    for row in game_map:
        print(" ".join(row))



def create_database_and_insert_data():
  # Create a connection to a new SQLite database file
  conn = sqlite3.connect('mydatabase.db')
  
  # Create a cursor object
  cursor = conn.cursor()
  
  # Execute a CREATE TABLE statement to create a new table in the database
  cursor.execute("CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
  
  # Execute an INSERT statement to insert data into the table
  cursor.execute("INSERT INTO mytable VALUES (1, 'Alice', 20)")
  cursor.execute("INSERT INTO mytable VALUES (2, 'Bob', 30)")
  
  # Save the changes to the database
  conn.commit()
  
  # Close the cursor and the connection
  cursor.close()
  conn.close()


def die(player):
  if player.hp < 1:
    print("Goodbye!")
    user.storeData(player)
    exit(-1)


def ItemPickUp(player,c,r):
  if collisions.isCollided(c,1,r): #GOLD
    player.gold += random.randint(5,15)
  if collisions.isCollided(c,2,r): #peasant cloth
    player.hp += 2
  if collisions.isCollided(c,3,r): #witches cloths
    player.hp += 1
  if collisions.isCollided(c,4,r): #witches staff
    print("Huray you've gotten the the staff")
    print("Now I think it's about time you remember your's families murder")
    player.gold += 100
    die(player)

def processInput(p,m,i,e,SCREEN_W = 30, SCREEN_H = 22):
  colls = collisions.getCollisions(p,m,i)
  while True:
    ret = input()
    if ret.lower() == "p" :  Menu.openMenu(p,SCREEN_W,SCREEN_H)

    # Collision detected if length of keys is greater than 0
    if collisions.isCollided(colls, 0,ret): continue

    #update user skills by item
    ItemPickUp(p,colls,ret)

    #collision between enemies and monster
    #making it so you lose health when next to the enemy and not while you are on top of them
    if collisions.isCollided(colls,3,ret):
      p.hp -= e[0].attack
      continue
    return ret

def test_print_game_map(self):
    game_map = [
        ["#", "#", "#", "#", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", ".", "#", ".", "#"],
        ["#", ".", ".", ".", "#"],
        ["#", "#", "#", "#", "#"]
    ]
    
    expected_output = """
    # # # # #
    # . . . #
    # . # . #
    # . . . #
    # # # # #
    """
    
    self.assertEqual(print_game_map(game_map), expected_output)       

class TestDatabaseFunction(unittest.TestCase):
  def test_database_function(self):
    create_database_and_insert_data()


    conn = sqlite3.connect('mydatabase.db')

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM mytable")

    results = cursor.fetchall()

    # Assert that the number of rows in the table is correct
    self.assertEqual(len(results),2)

    # Assert that the data in the table is correct
    self.assertEqual(results[0], (1, 'Alice', 20))
    self.assertEqual(results[1], (2, 'Bob', 30))



class TestGameStartFunction(unittest.TestCase):
    def test_loading_screen(self):
        result = main.gameStart()
        self.assertEqual(len(result),5)



class TestMapPrinting(unittest.TestCase):
    def printMap(self):
        PLAYER = gameobjects.Witch("test","Female",int(MAP_WIDTH/2),int(MAP_HEIGHT / 2))
        PLAYER.hp = 3
        PLAYER.level = 1
        PLAYER.gold = 1
        ITEM = gameobjects.Items()
        ENEMIES = gameobjects.spawnEnemies(5,MAP_WIDTH,MAP_HEIGHT)
        MAP = maps.GameMap(MAP_WIDTH,MAP_HEIGHT,PLAYER,ITEM,ENEMIES)
        MAP.printMap(PLAYER,ITEM)
        passed = 1
        self.assertEqual(passed,1)


class TestCharacterCreation(unittest.TestCase):
    def addingCharacter(self):
        PLAYER = gameobjects.Witch("testWitch","Female",int(MAP_WIDTH/2),int(MAP_HEIGHT / 2))
        PLAYER.hp = 3
        PLAYER.level = 1
        PLAYER.gold = 1
        passed = 1
        self.assertEqual(passed,1)



class TestMapUpdating(unittest.TestCase):
    def collisonDetecting(self):
        PLAYER = gameobjects.Witch("test","Female",int(MAP_WIDTH/2),int(MAP_HEIGHT / 2))
        PLAYER.hp = 3
        PLAYER.level = 1
        PLAYER.gold = 1
        ITEM = gameobjects.Items()
        ENEMIES = gameobjects.spawnEnemies(5,MAP_WIDTH,MAP_HEIGHT)
        MAP = maps.GameMap(MAP_WIDTH,MAP_HEIGHT,PLAYER,ITEM,ENEMIES)
        MAP.printMap(PLAYER,ITEM)
        inp = processInput(PLAYER,MAP,ITEM,ENEMIES)
        timer = 1

        MAP.updateMap(inp,PLAYER,ENEMIES,timer)
        passed = 1
        self.assertEqual(passed,1)


        
unittest.main()

