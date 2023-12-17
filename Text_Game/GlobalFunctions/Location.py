location = {
    "beach": '''You hear the waves crash on the shore.
You feel the white sand beneath your feet.''',
    "spit": '''To one side, you see the vast, unending ocean. To the other, you see 
the intimidating edifice of the land. There is what appears to be a statue up ahead. 
Behind you, a laundry room inside a mountain beckons.''',
    "statue": '''There is a large statue here, halfway buried in the sand. It appears
to be a human head, but it appears partially destroyed. You have an overwhelming
desire to touch it.''',
    "laundry room": '''Inside the mountain, you find a laundry room. There are 
    dirty clothes everywhere. There is a single washer-dryer combo in one corner 
    of the room and a set of stairs disappearing deeper into the mountains. ''',
    "hidden cave": '''Behind the washer-dryer combo, and up several flights of 
    stairs in the dark, you find yourself emerging into the light...the light 
    of a small fluorescent lamp at the top of an iron door. ''',
}

location_count = {
    "beach": 0,
    "spit": 0,
    "statue": 0,
    "laundry room": 0,
    "hidden cave": 0,
}

location_short = {
    "beach": '''Waves and sand and whatnot.''',
    "spit": '''A small stretch of sand between the beach and the statue.''',
    "statue": '''A large human-like statue. You want to touch it.''',
    "laundry room": '''A place where clothes are cleaned.''',
    "hidden cave": '''Down the stairs, laundry. Up the stairs, an iron door.'''
}

present_location = "beach"
hidden_cave = False


def location_function():
    output = ""
    for item in location:
        if present_location == item and location_count[present_location] < 1:
            output = location[present_location]
            location_count[present_location] += 1
        elif present_location == item and location_count[present_location] >= 1:
            output = location_short[present_location]
    return output
