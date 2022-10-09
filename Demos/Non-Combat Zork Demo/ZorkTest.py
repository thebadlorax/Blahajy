import os
import Blahajy


def main():
    Blahajy.clearscreen()
    Blahajy.update()
    Blahajy.printscenario()
    Blahajy.printnarrator()
    playerinput = str(input(": "))

    if playerinput == 'north':
        if Blahajy.north():
            Blahajy.changey(1)
            main()
        else:
            Blahajy.updatenarrator("Walking that way would be impossible")
            Blahajy.updatenarrator(mode="narratenowtrue")
            main()
    elif playerinput == 'south':
        if Blahajy.south():
            Blahajy.changey(-1)
            main()
        else:
            Blahajy.updatenarrator("Walking that way would be impossible")
            Blahajy.updatenarrator(mode="narratenowtrue")
            main()
    elif playerinput == 'east':
        if Blahajy.east():
            Blahajy.changex(1)
            main()
        else:
            Blahajy.updatenarrator("Walking that way would be impossible")
            Blahajy.updatenarrator(mode="narratenowtrue")
            main()
    elif playerinput == 'west':
        if Blahajy.west():
            Blahajy.changex(-1)
            main()
        else:
            Blahajy.updatenarrator("Walking that way would be impossible")
            Blahajy.updatenarrator(mode="narratenowtrue")
            main()
    elif playerinput == "exit":
        Blahajy.quitgame()
    else:
        Blahajy.updatenarrator("I do not understand")
        main()


main()
