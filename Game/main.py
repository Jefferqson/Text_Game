from GlobalFunctions import Location
from GlobalFunctions import Functions
from GlobalFunctions import Inventory

# beach
statue_touch = False
print('''
 You wake up on a beach.
 You feel a strong urge to ask for help.
 You also feel a strong urge to toss your hat.
 Further down the beach, there is a spit of land.
 Past that, there appears to be a shadowy figure.
 What would you like to do?''')

while not statue_touch:
    while Location.present_location == "beach":
        userinput = input("> ").lower()
        if Functions.globe.__contains__(userinput) or userinput in Location.location:
            Functions.global_functions(userinput)
        elif userinput == "throw rock":
            print("You pick up a stone and toss it into the ocean \n"
                  "It sinks down into the deep.")
        else:
            print("A mysterious force prevents this.")

    # spit

    while Location.present_location == "spit":
        userinput = input("> ").lower()
        if Functions.globe.__contains__(userinput) or userinput in Location.location:
            Functions.global_functions(userinput)
        elif userinput == "kick sand":
            print("You kick the sand. A crab scuttle out of a hole, \n"
                  "gives you a salty glance and disappears into the cold water")
        else:
            print("A mysterious force prevents this.")

# statue

    while Location.present_location == "statue":
        userinput = input("> ").lower()
        if Functions.globe.__contains__(userinput) or userinput in Location.location:
            Functions.global_functions(userinput)
        elif userinput == "touch":
            print("You touch the statue. It glows. You are taken into space.\n"
                  "It was aliens the entire time.\n"
                  "You win?")
            statue_touch = True
            break
        else:
            print("A mysterious force prevents this.")

# Laundry Room

    while Location.present_location == "laundry room":
        userinput = input("> ").lower()
        if Functions.globe.__contains__(userinput) or userinput in Location.location:
            Functions.global_functions(userinput)
        elif userinput == "acquire socks":
            if Inventory.advanced_inventory.get("dirty_socks") == 0:
                Inventory.advanced_inventory.update({"dirty_socks": 1})
                print("You now have a pair of filthy socks. You should probably clean them")
            elif Inventory.advanced_inventory.get("dirty_socks") == 1:
                print("You can already smell the horrible stench from your inventory.")
            else:
                print("You already cleaned one pair of socks. Why clean another? \n"
                      "How many feet do you have??")
        elif userinput == "clean socks" and Inventory.advanced_inventory.get("dirty_socks") == 1:
            Inventory.advanced_inventory.update({"dirty_socks": 2})
            print('You place the disgusting foot item in the laundry and hit the start button. \n'
                  'Instead of cleaning the socks, however, the laundry machine ejects them and \n'
                  'shifts to the side, revealing a hidden cave behind it.')
            Location.hidden_cave = True
        else:
            print("A mysterious force prevents this.")

# Hidden Cave

    while Location.present_location == "hidden cave":
        userinput = input("> ").lower()
        if Functions.globe.__contains__(userinput) or userinput in Location.location:
            Functions.global_functions(userinput)
        else:
            print("A mysterious force prevents this.")
