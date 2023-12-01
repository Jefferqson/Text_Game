from GlobalFunctions.Help import help_function
from GlobalFunctions import Inventory
from GlobalFunctions import Location
from GlobalFunctions import LookAround
from GlobalFunctions import GoTo

globe = {
    "help": help_function(),
    "location": Location.location_function(),
    "inventory": Inventory.inventory_list(),
    "toss hat": "Tosses hat",
    "remove pants": "Removes pants",
    "remove shoes": "Removes shoes",
    "look around": LookAround.look_around(),

}


def global_functions(user_input):
    if user_input == "help":
        print(help_function())
    elif user_input == "location":
        print(f'{Location.present_location} \n'
              f'{Location.location_function()}')
    elif user_input == "inventory":
        print(Inventory.inventory_list())
    elif user_input == "toss hat":
        if Inventory.inventory["hat"]:
            print("You throw away your hat, the only thing you've ever loved'.")
            Inventory.inventory["hat"] = False
        else:
            print("You already threw your hat away, you monster.")
    elif user_input == "remove pants":
        if Inventory.inventory["pants"]:
            print("You tear your pants off and live free")
            Inventory.inventory["pants"] = False
        else:
            print("You realize, sadly, that this as free as you will ever be.")
    elif user_input == "remove shoes":
        if Inventory.inventory["shoes"]:
            print("You take off your shoes and let your toes out!\n"
                  "Ouch!\n"
                  "You have stepped on glass")
            Inventory.inventory["shoes"] = False
        else:
            print("You have no shoes, already.\n"
                  "In fact, your feet have begun to callous.\n"
                  "You feel all-powerful.")
    elif user_input == "look around":
        print(LookAround.look_around())
    elif user_input in Location.location:
        print(GoTo.go_to(place=user_input))
    else:
        pass
