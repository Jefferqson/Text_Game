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
    "quit": "quit"
}


def global_functions(user_input):
    if user_input == "help":
        return help_function()
    elif user_input == "location":
        return (f'{Location.present_location} \n'
                f'{Location.location_function()}')
    elif user_input == "inventory":
        return Inventory.inventory_list()
    elif user_input == "toss hat":
        if Inventory.inventory["hat"]:
            Inventory.inventory["hat"] = False
            return "You throw away your hat, the only thing you've ever loved'."
        else:
            return "You already threw your hat away, you monster."
    elif user_input == "remove pants":
        if Inventory.inventory["pants"]:
            Inventory.inventory["pants"] = False
            return ("You tear your pants off and live free\n"
                    "Somewhere in the universe you sense that Ambre is happy.")
        else:
            return "You realize, sadly, that this as free as you will ever be."
    elif user_input == "remove shoes":
        if Inventory.inventory["shoes"]:
            Inventory.inventory["shoes"] = False
            return ("You take off your shoes and let your toes out!\n"
                    "Ouch!\n"
                    "You have stepped on glass")
        else:
            return ("You have no shoes, already.\n"
                    "In fact, your feet have begun to callous.\n"
                    "You feel all-powerful.")
    elif user_input == "look around":
        return LookAround.look_around()
    elif user_input in Location.location:
        return GoTo.go_to(user_input)
    elif user_input == "quit":
        quit()
    else:
        pass
