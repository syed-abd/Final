# Imports and Global Variables -----------------------------------------------
import home
import mine
import village
import inventory

#character location variables
m, x, y = 0, 0, 0


# Functions ------------------------------------------------------------------
def homeMenu():
    global x, y
    # ask the user where to move next
    print("Menu Options: walk, travel, inventory")
    mainMenu = input("What do you want to do? ")
    # update the character's position based on the user's input
    if mainMenu == "walk":
        x, y = home.movement(x, y)
    elif mainMenu == "travel":
        if home.map[y][x] == "garage":
          switch_map()
        else:
          print("invalid talk about space ship/find garage")
    elif mainMenu == "inventory":
          inventory.access_inventory()
    else:
        print("Invalid")

def switch_map():
  ''' describe'''
  global m , x, y
  if m == 0: # Home
      answer = input("Do you want to travel to The Mines or The Village? ")
      if answer == "mine":
          m, x, y = 1, 0, 0
      elif answer == "village":
          m, x, y = 2, 0, 0
  elif m == 1: # Mine
      answer = input("Do you want to travel back Home or The Village? ")
      if answer == "home":
          m, x, y = 0, 1, 0
      elif answer == "village":
          m, x, y = 2, 0, 0
  elif m == 2: # Village
      answer = input("Do you want to travel to The Mines or back Home ")
      if answer == "mine":
          m, x, y = 1, 0, 0
      elif answer == "home":
          m, x, y = 0, 1, 0


def mineMenu(): 
  global x, y
  # ask the user where to move next
  print("Menu Options: walk, travel, inventory, search")
  mainMenu = input("What do you want to do? ")
  # update the character's position based on the user's input
  if mainMenu == "walk":
      x, y = mine.movement(x, y)
  elif mainMenu == "travel":
      if mine.map[y][x] == "block1":
          switch_map()
      else:
          print("Must be on any block1 to travel.")
  elif mainMenu == "inventory":
      inventory.access_inventory()
  elif mainMenu == "search":
      if mine.map[y][x] == "block4" or mine.map[y][x] == "block2":
          mine.search(x, y)  
      else:
          print("There are no items at the location.")
  else:
        print("Invalid")
  
  
def villageMenu(): 
  global x, y
  # ask the user where to move next
  print("Menu Options: walk, travel, inventory, trade")
  mainMenu = input("What do you want to do? ")
  # update the character's position based on the user's input
  if mainMenu == "walk":
      x, y = village.movement(x, y)
  elif mainMenu == "travel":
      if village.map[y][x] == "parkade":
          switch_map()
      else:
          print("Must be on any block1 to travel.")
  elif mainMenu == "inventory":
          inventory.access_inventory()
  elif mainMenu == "trade":
          village.trade()
  else:
        print("Invalid")



# Main -----------------------------------------------------------------------
# loop through the map and describe the setting when the character moves 
# into a block
while True:
    if m == 0:
        setting = home.map[y][x] 
        home.describe_setting(setting)
        homeMenu()
    elif m == 1:
        setting = mine.map[y][x] 
        mine.describe_setting(setting)
        mineMenu()
        
    elif m == 2:
        setting = village.map[y][x] 
        village.describe_setting(setting)
        villageMenu()
    else:
      print("Error, map is missing.")