# Just messing around with OOP
present_location = "beach"


class Location:

    def __init__(self, name, short, long, count):
        self.name = name
        self.short = short
        self.long = long
        self.count = count

    def location(self):
        output = ""
        global present_location
        if present_location == self.name and self.count < 1:
            output = self.long
            self.count += 1
        elif present_location == self.name and self.count == 1:
            output = self.short
            self.count += 1
        return output

    def go_to(self):
        global present_location
        if present_location != self.name:
            present_location = self.name
        return present_location


beach = Location("beach", "sandy place", "very sandy place", 0)
spit = Location("spit", "small land", "small sandy land", 0)

print('''
 You wake up on a beach.
 You feel a strong urge to ask for help.
 You also feel a strong urge to toss your hat.
 Further down the beach, there is a spit of land.
 Past that, there appears to be a shadowy figure.
 What would you like to do?''')

while present_location == "beach":
    userinput = input("> ").lower()
    if userinput == "spit":
        print(spit.go_to)
