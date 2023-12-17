from GlobalFunctions import Location
from GlobalFunctions import LookAround


def go_to(place):
    go_to_list = []
    output = ""
    for item in LookAround.coordinate_dictionary:
        if Location.present_location == item:
            cord3, cord4 = LookAround.coordinate_dictionary[item]
    for item in LookAround.coordinate_dictionary:
        cord1, cord2 = LookAround.coordinate_dictionary[item]
        if ((abs(cord3 - cord1) == 0 and abs(cord4 - cord2) == 1) or
                (abs(cord3 - cord1) == 1 and abs(cord4 - cord2) == 0)):
            go_to_list.append(item)
        else:
            pass
    if place in go_to_list:
        Location.present_location = place
        output = Location.location_function()
    else:
        output = "A mysterious force prevents this."
    return output

