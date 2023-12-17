import tkinter.colorchooser

from GlobalFunctions import Location
from GlobalFunctions import Functions
from GlobalFunctions import Inventory
from GlobalFunctions import LookAround
import tkinter as tk
import tkinter.colorchooser


def main_function(userinput):
    userinput = userinput.lower()
    # beach
    global statue_touch
    while not statue_touch:
        while Location.present_location == "beach":
            if userinput in Functions.globe or userinput in Location.location:
                return Functions.global_functions(userinput)
            elif userinput == "throw rock":
                return ("You pick up a stone and toss it into the ocean \n"
                        "It sinks down into the deep.")
            else:
                return "A mysterious force prevents this."

        # spit

        while Location.present_location == "spit":
            if userinput in Functions.globe or userinput in Location.location:
                return Functions.global_functions(userinput)
            elif userinput == "kick sand":
                return ("You kick the sand. A crab scuttle out of a hole, \n"
                        "gives you a salty glance and disappears into the cold water")
            else:
                return "A mysterious force prevents this."

    # statue

        while Location.present_location == "statue":
            if userinput in Functions.globe or userinput in Location.location:
                return Functions.global_functions(userinput)
            elif userinput == "touch":
                statue_touch = True
                return ("You touch the statue. It glows. You are taken into space.\n"
                        "It was aliens the entire time.\n"
                        "You win?")
            else:
                return "A mysterious force prevents this."

    # Laundry Room

        while Location.present_location == "laundry room":
            if userinput in Functions.globe or userinput in Location.location:
                return Functions.global_functions(userinput)
            elif userinput == "acquire socks":
                if Inventory.advanced_inventory.get("dirty_socks") == 0:
                    Inventory.advanced_inventory.update({"dirty_socks": 1})
                    return "You now have a pair of filthy socks. You should probably clean them"
                elif Inventory.advanced_inventory.get("dirty_socks") == 1:
                    return "You can already smell the horrible stench from your inventory."
                else:
                    return ("You already cleaned one pair of socks. Why clean another? \n"
                            "How many feet do you have??")
            elif userinput == "clean socks" and Inventory.advanced_inventory.get("dirty_socks") == 1:
                Inventory.advanced_inventory.update({"dirty_socks": 2})
                Location.hidden_cave = True
                return ('You place the disgusting foot item in the laundry and hit the start button. \n'
                        'Instead of cleaning the socks, however, the laundry machine ejects them and \n'
                        'shifts to the side, revealing a hidden cave behind it.')
            else:
                return "A mysterious force prevents this."

    # Hidden Cave

        while Location.present_location == "hidden cave":
            if userinput in Functions.globe or userinput in Location.location:
                return Functions.global_functions(userinput)
            else:
                return "A mysterious force prevents this."


statue_touch = False


def user_selection(*ch):
    # Requires *ch as an optional parameter for the key binding for return to work
    userinput = user_entry.get()
    if userinput == '':
        pass
    else:
        lbl_result["text"] = main_function(userinput)


def get_inventory():
    lbl_result["text"] = Inventory.inventory_list()


def get_help():
    lbl_result["text"] = Functions.help_function()


def get_location():
    lbl_result["text"] = Functions.global_functions("location")


def get_look_around():
    lbl_result["text"] = LookAround.look_around()


def get_color_scheme():
    # you have to unpack this because it returns a tuple of (rgb, hexadecimal)
    x, y = tkinter.colorchooser.askcolor()
    lbl_result["fg"] = y


def get_quit():
    quit()


def get_settings():
    settings_window = tk.Tk()
    settings_window.title("Settings")
    settings_window.rowconfigure(0, weight=1, minsize=25)
    settings_window.columnconfigure(0, weight=1, minsize=25)
    color_scheme_btn = tk.Button(master=settings_window, text="Text Color", command=get_color_scheme, width=25)
    color_scheme_btn.grid(row=0, column=0)


window = tk.Tk()
window.title("Beach Explorer")
window.rowconfigure([0, 2], weight=1, minsize=25)
window.columnconfigure(0, weight=1, minsize=25)


lbl_result = tk.Label(master=window, width=65, height=30, bg="black", fg="white", text='''
     You wake up on a beach.
     You feel a strong urge to ask for help.
     You also feel a strong urge to toss your hat.
     Further down the beach, there is a spit of land.
     Past that, there appears to be a shadowy figure.
     What would you like to do?''')

user_entry_frm = tk.Frame(master=window, pady=10)
user_entry = tk.Entry(master=user_entry_frm, width=10)
enter_button = tk.Button(master=user_entry_frm, text="⮡ Enter", command=user_selection)
window.bind("<Return>", user_selection)
user_entry.grid(row=0, column=0)
enter_button.grid(row=0, column=1)

func_frame = tk.Frame(master=window, bg="steel blue")
help_btn = tk.Button(master=func_frame, text="Help", command=get_help, bg="steel blue", fg="white")
help_btn.grid(row=0, column=0)
inventory_btn = tk.Button(master=func_frame, text="Inventory", command=get_inventory, bg="steel blue", fg="white")
inventory_btn.grid(row=0, column=1)
location_btn = tk.Button(master=func_frame, text="Location", command=get_location, bg="steel blue", fg="white")
location_btn.grid(row=0, column=2)
look_around_btn = tk.Button(master=func_frame, text="Look Around", command=get_look_around, bg="steel blue", fg="white")
look_around_btn.grid(row=0, column=3)
settings_btn = tk.Button(master=func_frame, text="Settings", command=get_settings, bg="steel blue", fg="white")
settings_btn.grid(row=0, column=4)
quit_btn = tk.Button(master=func_frame, text="Quit", command=get_quit, bg="steel blue", fg="white")
quit_btn.grid(row=0, column=5)


lbl_result.grid(row=0, column=0, sticky="nsew")
user_entry_frm.grid(row=1, column=0)
func_frame.grid(row=2, column=0)

window.mainloop()
