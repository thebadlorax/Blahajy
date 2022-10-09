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



# Combat Variables
    # Player Variables
maxhp = 20
hp = 0
lvl = 1
xp = 0
    # Monster Variables
mmaxhp = 25
mhp = 0
mname = ""


# Combat Variable Manipulation
def changeplayerhp(num):
    global maxhp, hp

    if hp + num <= maxhp:
        if hp + num >= 0:
            if hp + num == 0:
                killplayer()
            else:
                hp += num


def changemonsterhp(num):
    global mmaxhp, mhp

    if mhp + num <= mmaxhp:
        if mhp + num >= 0:
            if mhp + num == 0:
                killmonster()
            else:
                mhp += num


# Combat
def killplayer():
    quitgame()


def killmonster():
    quitgame()



# Clearscreen Functions
def clearscreen(delay=0):
    time.sleep(delay)
    os.system('cls' if os.name == 'nt' else 'clear')




# Text Functions
def bold(text):
    return str("\033[1m" + text + "\033[0m")




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




# Combat Zonemap Functions
def hascombat():
    if "COMBAT" in zonemap.zonemap[str(x) + str(y)]:
        return True
    else:
        return False


def monstername():
    return str(zonemap.zonemap[str(x) + str(y)]["MONSTERNAME"])


def monstermaxhp():
    return int(zonemap.zonemap[str(x) + str(y)]["MONSTERMAXHP"])




# Coordinate Functions
def changex(num):
    global x, narratenow
    updatelastcoords()
    updatenarrator(mode="narratenowfalse")
    x += num


def changey(num):
    global y, narratenow
    updatelastcoords()
    updatenarrator(mode="narratenowfalse")
    y += num


def updatelastcoords():
    global x, y, lastcoords
    lastcoords = str(x) + str(y)




# Screen Writing
def printscenario():
    print(bold(zonename()) + "\n\n" + zonedesc() + "\n\n")


def printnarrator():
    print("\n" + updatenarrator(mode="print") + "\n")


def printcoords():
    print(str(x) + str(y))



# Combat Screen Writing
def printmonster():
    print(bold(mname) + "\n" + str(mhp) + " / " + str(mmaxhp) + "\n")

def printplayer():
    print("\n" + str(hp) + " / " + str(maxhp))





# Game Loop
def update():
    global x, y, lastcoords, latestnarrator, narratenow

    if not narratenow:  # Reset Narrator
        updatenarrator(mode="clear")


def quitgame():
    clearscreen()
    os.system("exit")


def wait(timetowait):
    time.sleep(timetowait)


def setupcombatvariables():
    global mname, mmaxhp, mhp, hp, maxhp, lvl, xp

    mname = monstername()
    mmaxhp = monstermaxhp()
    mhp = mmaxhp

    hp = maxhp




# Narrator
def updatenarrator(text="NULL", mode="change"):
    global latestnarrator, narratenow
    if mode == "change":
        latestnarrator = text
    elif mode == "clear":
        latestnarrator = ""
    elif mode == "coords":
        latestnarrator = str(str(x) + str(y))
    elif mode == "print":
        return latestnarrator
    elif mode == "narratenowfalse":
        narratenow = False
    elif mode == "narratenowtrue":
        narratenow = True




# if __name__ == "__main__": clearscreen(), print("Incorrect Run Type!"), time.sleep(2.5), quitgame()
