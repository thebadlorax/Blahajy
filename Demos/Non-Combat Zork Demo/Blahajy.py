import time
import random
import os
import platform
import zonemap


# Coordinate Variables
x = 0
y = 0
lastcoords = ""

# Narrator Variables
latestnarrator = ""
narratenow = False


# Clearscreen Functions
def clearscreen(delay=0):
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')


# Text Functions
def bold(text):
    return str("\033[1m" + text + "\033[0m")


# Stolen Functions
def wait(timetowait):
    time.sleep(timetowait)


# Zonemap Functions
def zonename():
    return zonemap.zonemap[str(x) + str(y)]["ZONENAME"]


def zonedesc():
    return zonemap.zonemap[str(x) + str(y)]["ZONEDESC"]


def north():
    return zonemap.zonemap[str(x) + str(y)]["NORTH"]


def south():
    return zonemap.zonemap[str(x) + str(y)]["SOUTH"]


def east():
    return zonemap.zonemap[str(x) + str(y)]["EAST"]


def west():
    return zonemap.zonemap[str(x) + str(y)]["WEST"]


def hascombat():
    if "COMBAT" in zonemap.zonemap[str(x) + str(y)]:
        return True
    else:
        return False


# Coordinate Functions
def changex(num):
    global x
    updatelastcoords()
    x += num


def changey(num):
    global y
    updatelastcoords()
    y += num


def updatelastcoords():
    global x, y, lastcoords
    lastcoords = str(x) + str(y)


# Screen Writing Variables
def printscenario():
    print(bold(zonename()) + "\n\n" + zonedesc() + "\n\n")


def printnarrator():
    print("\n" + latestnarrator + "\n")


# Game Loop Functions
def update():
    global x, y, lastcoords, latestupdate, narratenow

    if not narratenow:  # Reset Narrator
        latestupdate = ""


# Narrator Functions
def updatenarrator(text="NULL", mode="change"):
    global latestnarrator
    if mode == "change":
        latestnarrator = text


if __name__ == "__main__":
    clearscreen()
    print("Incorrect Run Type!")
    time.sleep(2.5)
    os.system("exit")
