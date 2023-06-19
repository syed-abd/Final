# Imports and Global Variables ------------------------------------------------
# Describe all variables
tiles = ["parkade", "town hall", "marketplace", "walking park", "restaurant"]

# Third map, The Village (m = 2)
map = [
    [tiles[4], tiles[4], tiles[4], tiles[4]],
    [tiles[1], tiles[1], tiles[1], tiles[1]],
    [tiles[0], tiles[2], tiles[2], tiles[2]],
    [tiles[3], tiles[3], tiles[3], tiles[3]]
]

# Valid directions and actions for the characters
valid_actions = ["actions", "directions"]
possible_directions = ["north", "south", "east", "west"]
possible_actions = ["explore", "trade", "movement", "quit"]
trade_actions = ["buy", "sell"]

# Add comment here
villager_inventory = {
    'apples': {'amount': 6, 'description': "delicious apples for trade!"},
    'rat poison': {'amount': 3, 'description': "a deadly poison for the rats!!"},
    'potion': {'amount': 2, 'description': "a healing potion"}
}

player_inventory = {}  # Declare player inventory

# Functions ----------------------------------------------------------------------------
def describe_setting(setting):
    '''Describes the setting of the block'''
    print(f"You are in the {setting}.")


def movement(x, y):
    '''Determines where the character will move'''
    thinking = True
    warning = "You have reached the edge of the map!"
    while thinking:
        # ask the user where to move next
        print("You are in the village.")
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
            if x != 3:
                x += 1
                thinking = False
            else:
                print(warning)
        else:
            print("Invalid")
    return x, y


def display_inventory():
    '''Displays the player's inventory'''
    print("Your inventory:")
    for item, count in player_inventory.items():
        print(f"{item}: {count}")


def add_item(item, count=1):
    '''Adds items to the player's inventory'''
    if item in player_inventory:
        player_inventory[item] += count
    else:
        player_inventory[item] = count
    print(f"{count} {item}(s) added to your inventory.")


def trade():
    global player_inventory
    global villager_inventory

    print("Available trade actions:")
    for action in trade_actions:
        print(f"* {action}")

    trade_action = input("Choose a trade action: ")

    if trade_action.lower() == "buy":
        print("Available items for purchase:")
        for item, details in villager_inventory.items():
            print(f"{item}: {details['amount']} - {details['description']}")

        item_to_buy = input("Choose an item to buy: ")

        if item_to_buy in villager_inventory:
            amount = int(input("Enter the quantity to buy: "))
            if amount <= villager_inventory[item_to_buy]['amount']:
              if 'points' not in player_inventory:
                    player_inventory['points'] = {'amount': 0, 'description': "Trade points"}
              cost = amount
              if cost <= player_inventory['points']['amount']:
                    player_inventory['points']['amount'] -= cost
                    add_item(item_to_buy, amount)
                    villager_inventory[item_to_buy]['amount'] -= amount
                    print(f"You bought {amount} {item_to_buy} for {cost} points.")
              else:
                    print("You don't have enough points to make the purchase.")
            else:
                print("The villager doesn't have enough of that item to sell.")
        else:
                print("Invalid item.")

    elif trade_action.lower() == "sell":
        print("Items you can sell:")
        display_inventory()

        item_to_sell = input("Choose an item to sell: ")

        if item_to_sell in player_inventory:
            amount = int(input("Enter the quantity to sell: "))
            if amount <= player_inventory[item_to_sell]['amount']:
                cost = amount
                player_inventory[item_to_sell]['amount'] -= amount
                add_item('points', cost)
                villager_inventory[item_to_sell]['amount'] += amount
                print(f"You sold {amount} {item_to_sell} for {cost} points.")
            else:
                print("You don't have enough of that item to sell.")
        else:
            print("Invalid item.")

    else:
        print("Invalid trade action.")
