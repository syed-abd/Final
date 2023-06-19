# Imports and Global Variables -----------------------------------------------
# First map (m = 0)
map = [
    ["living room", "kitchen", "basement", "washroom", "garage"],
    ["garage", "living room", "kitchen", "basement", "washroom"],
    ["washroom", "garage", "living room", "kitchen", "basement"],
    ["basement", "washroom", "garage", "living room", "kitchen"]
]

# Describe tiles here
tile = {
    "living room": {"Description": 
                    "You are chilling in the living room"},
    "kitchen": {"Description": 
                "You are in the kitchen, get cooking or get going"},
    "basement": {"Description": 
                 "You have entered the basement, it's spooky down here"},
    "washroom": {"Description": 
                 "You have entered the washroom; the toilets smell stinky."},
    "garage": {"Description": 
               "You have entered the garage, your jet is fueled up and ready"
               + "to go"},
}


# Functions ------------------------------------------------------------------
def describe_setting(setting):
    '''Describes the setting of the block'''
    print(f"You are in the {setting}. {tile[setting]['Description']}")


def movement(x, y):
    '''Determines where the character will move'''
    thinking = True
    warning = "You have reached the edge of the map!"
    while thinking:
        # ask the user where to move next
        print("You are at home.")
        direction = input("Where do you want to go? (north, south, west, east)\n ")
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
  

