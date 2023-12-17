inventory = {
        "hat": True,
        "shoes": True,
        "pants": True,
    }
# 0 = not have 1 = have 2 = already had. That way, the player can't just infinitely pick up an item. 
advanced_inventory = {
    "dirty_socks": 0
}


def inventory_list():
    output = ""
    for item in inventory:
        if inventory[item]:
            output += '\n' + item
    for item in advanced_inventory:
        if advanced_inventory[item] == 1:
            output += '\n' + item
    if output == "":
        output += "(empty)"
    elif output != "":
        message = "You have the following items:"
        output = message + output

    return output
