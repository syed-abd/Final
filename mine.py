# Imports and Global Variables------------------------------------------------
import inventory

# Second map, The Mines (m = 1)
map = [
    ["block1", "block2", "block3", "block4", "an empty room"],
    ["an empty room", "block1", "block2", "block3", "block4"],
    ["block4", "an empty room", "block1", "block2", "block3"],
    ["block3", "block4", "an empty room", "block1", "block2"]
]

# create two inventories using nested dictionaries
objects = {
    "gold": {"location": "block4"},
    "diamond": {"location": "block2"},
}

# Functions ----------------------------------------------------------------------------
def describe_setting(setting):
    '''Describes the setting of the block'''
    print(f"You are in the Mines in {setting}.")

  
def movement(x, y):
    '''Determines where the character will move'''
    thinking = True
    warning = "You have reached the edge of the map!"
    while thinking:
        # ask the user where to move next
        print("You are at the mine.")
        direction = input("Where do you want to go? (north, south, west, east) ")
        # update the character's position based on the user's input
        if direction == "north":
            if y != 0:
                y -= 1
                thinking = False
            else:
                print(warning)
        elif direction == "south":
            if y != 3:
                y += 1
                thinking = False
            else:
                print(warning)
        elif direction == "west":
            if x != 0:
                x -= 1
                thinking = False
            else:
                print(warning)
        elif direction == "east":
            if x != 4:
                x += 1
                thinking = False
            else:
                print(warning)
        else:
            print("Invalid")
    return x, y


# define a function to access the inventory
def access_inventory():
    if not inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in inventory:
            print(f"- {item}")

def search(x, y):
    print("You are now searching the area.")
    for obj in objects:
        if objects[obj]["location"] == map[y][x]:
            print(f"You have found {obj}!")
            print(f"{objects[obj]}")
            take_item(obj, x, y)


# define a function to add an item to the inventory
def take_item(obj, x, y):
    answer = input(f"Do you want to keep the {obj}? (yes, no) ")
    if answer == "yes":
        inventory.player_inventory[obj]["amount"] += 1
        print(f"You have taken the {obj}.")
        map[y][x] = "an empty room"
    elif answer == "no":
        print(f"You did not take the {obj}.")
    else:
        print("Invalid choice")
        take_item(obj)

