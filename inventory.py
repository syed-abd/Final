# Imports and Global Variables------------------------------------------------

# Create a dictionary to hold the player's inventory
player_inventory = {
        'diamond': {'amount': 10,'description': "You can trade the diamonds!!"},
        'water': {'amount': 5,'description': "You can quench your thirst!!"},
        'gold': {'amount': 5,'description': "You can trade your gold!!!"},
        'repair kit': {'amount': 1,'description': "You found a repair kit!"}
}


# Functions ----------------------------------------------------------------------------
def access_inventory():
    if not player_inventory:
        print("Your inventory is empty.")
    else:
        print("Your inventory contains:")
        for item in player_inventory:
            print(f"- {player_inventory[item]['amount']} {item}")