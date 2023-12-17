from GlobalFunctions import Location

coordinate_dictionary = {
    "deepest bluest": [0, -1],
    "super beach": [-1, 0],
    "beach": [0, 0],
    "mainland": [0, 1],
    "spit": [1, 0],
    "statue": [2, 0],
    "the dune": [2, 1],
    "laundry room": [1, -1],
    "hidden cave": [1, -2]
}


def look_around():
    output = "Around you, you see:"
    for item in coordinate_dictionary:
        if Location.present_location == item:
            cord3, cord4 = coordinate_dictionary[item]
    for item in coordinate_dictionary:
        cord1, cord2 = coordinate_dictionary[item]
        if ((abs(cord3 - cord1) == 0 and abs(cord4 - cord2) == 1) or
                (abs(cord3 - cord1) == 1 and abs(cord4 - cord2) == 0)):
            output += '\n' + item
        else:
            pass
    return output
